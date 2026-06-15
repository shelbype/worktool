from __future__ import annotations

import functools
import hashlib
import math
import re
from typing import Protocol

import httpx


class EmbeddingProvider(Protocol):
    def embed(self, text: str) -> list[float]:
        ...


class LLMProvider(Protocol):
    def generate_answer(self, question: str, contexts: list[str]) -> str:
        ...


class HashEmbeddingProvider:
    """Deterministic local embedding for development and tests."""

    def __init__(self, dimensions: int = 64) -> None:
        self.dimensions = dimensions

    def embed(self, text: str) -> list[float]:
        vector = [0.0] * self.dimensions
        tokens = self._tokens(text)
        for token in tokens:
            digest = hashlib.sha256(token.encode("utf-8")).digest()
            index = int.from_bytes(digest[:4], "big") % self.dimensions
            vector[index] += 1.0
        norm = math.sqrt(sum(value * value for value in vector)) or 1.0
        return [value / norm for value in vector]

    def _tokens(self, text: str) -> list[str]:
        latin = re.findall(r"[a-zA-Z0-9_./-]+", text.lower())
        chinese = re.findall(r"[一-鿿]{2,}", text)
        chinese_terms: list[str] = []
        for word in chinese:
            chinese_terms.append(word)
            chinese_terms.extend(word[index : index + 2] for index in range(max(1, len(word) - 1)))
        return latin + chinese_terms


class HttpEmbeddingProvider:
    """OpenAI-compatible embedding API provider with LRU caching."""

    def __init__(
        self,
        api_base: str,
        api_key: str,
        model: str,
        dimensions: int | None = None,
        encoding_format: str | None = "float",
    ) -> None:
        self.api_base = api_base.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.dimensions = dimensions
        self.encoding_format = encoding_format
        # Cache up to 500 embeddings to avoid redundant API calls.
        self._embed_cached = functools.lru_cache(maxsize=500)(self._embed_uncached)

    def embed(self, text: str) -> list[float]:
        return list(self._embed_cached(self.model, text))

    def _embed_uncached(self, model: str, text: str) -> tuple[float, ...]:
        payload: dict[str, object] = {"model": model, "input": text}
        if self.dimensions:
            payload["dimensions"] = self.dimensions
        if self.encoding_format:
            payload["encoding_format"] = self.encoding_format
        response = httpx.post(
            f"{self.api_base}/embeddings",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return tuple(float(value) for value in data["data"][0]["embedding"])


class MockLLMProvider:
    def generate_answer(self, question: str, contexts: list[str]) -> str:
        if not contexts:
            return "稍等老师，这个问题 @校校助理 帮您看下，尽快回复您。"
        context = contexts[0].strip().replace("\n", " ")
        return f"老师，您可以先看下这个说明：{context}"


class HttpLLMProvider:
    def __init__(self, api_base: str, api_key: str, model: str, max_tokens: int = 500) -> None:
        self.api_base = api_base.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens

    def generate_answer(self, question: str, contexts: list[str]) -> str:
        prompt = (
            "你是教育 SaaS 客服助手。请只基于给定知识片段回答客户问题，不要编造。\n"
            "回答要求：\n"
            "1. 用真人客服助理口吻回答，可以称呼“老师”，但不要每句都重复称呼。\n"
            "2. 不要使用机械开头，例如“可以，按下面步骤处理”“根据帮助文档”。\n"
            "3. 操作类问题优先用编号步骤，保留菜单名、按钮名、注意事项。\n"
            "4. 如果知识片段不足以确认答案，请只回复“稍等老师，这个问题 @校校助理 帮您看下，尽快回复您。”\n"
            "5. 语气自然、简洁、可执行，不使用表情，不做价格、合同、退款等承诺。\n\n"
            "参考示例：\n"
            "问：学生如何查看错题分析？\n"
            "答：老师，学生可以在学生端首页点击“错题本”，选择对应科目即可查看错题分析和订正建议。\n\n"
            "问：怎么创建班级？\n"
            "答：老师您好，创建班级的步骤是：\n"
            "1. 进入“班级管理”页面，点击右上角“新建班级”\n"
            "2. 填写班级名称、选择科目和年级\n"
            "3. 点击“确定”即可完成创建\n"
            "创建后可以在班级列表找到新班级进行排课。\n\n"
            f"客户问题：{question}\n\n"
            "知识片段：\n" + "\n---\n".join(contexts)
        )
        response = httpx.post(
            f"{self.api_base}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": self.max_tokens,
            },
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    def rewrite_query(self, question: str) -> str:
        """将用户口语问题改写为检索优化的关键词短语。

        Args:
            question: 原始用户问题

        Returns:
            空格分隔的 2-3 个检索短语字符串；失败时向外抛异常，
            调用方负责捕获并 fallback 到原始 query。
        """
        prompt = (
            "你是教育SaaS系统的查询改写助手。将用户口语问题改写为2-3个标准检索关键词短语，"
            "用空格分隔。\n"
            "规则：纠正错别字和口语化表达、补全隐含的功能名/端口关键词、"
            "不改写为不同意图。\n\n"
            "示例：\n"
            '用户："咋建班" → 改写：创建班级 新建班级 班级管理\n'
            '用户："学生做不了作业" → 改写：作业无法加载 作业功能异常\n'
            '用户："老师怎么绑学生" → 改写：绑定学生 家长端绑定 学员管理\n\n'
            f'用户："{question}"\n'
            "改写："
        )
        response = httpx.post(
            f"{self.api_base}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 80,
            },
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    def classify_intent(self, prompt: str) -> str:
        """Send a classification prompt and return raw response text.

        Used by IntentClassifier for intent classification + multi-intent
        decomposition.  Callers should handle exceptions and parse the JSON.

        Args:
            prompt: Full classification prompt including examples and user query.

        Returns:
            Raw LLM response text (expected to be JSON).

        Raises:
            httpx.HTTPError: On network or API errors.
        """
        response = httpx.post(
            f"{self.api_base}/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
                "max_tokens": 300,
            },
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()


class HttpRerankProvider:
    """DashScope qwen3-rerank via OpenAI-compatible rerank API.

    API reference:
      POST {api_base}/compatible-api/v1/reranks
      Body: {"model": "...", "documents": [...], "query": "...", "top_n": N}
      Response: {"results": [{"index": 0, "relevance_score": 0.93}, ...]}
    """

    def __init__(self, api_base: str, api_key: str, model: str) -> None:
        self.api_base = api_base.rstrip("/")
        self.api_key = api_key
        self.model = model

    def rerank(self, query: str, documents: list[str], top_n: int | None = None) -> dict[int, float]:
        """Score candidate documents against the query.

        Args:
            query: The search query.
            documents: Candidate document texts (up to 500).
            top_n: Optional limit on returned results.

        Returns:
            Dict mapping original document index to relevance_score (0–1).
        """
        body: dict[str, object] = {
            "model": self.model,
            "documents": documents,
            "query": query,
        }
        if top_n is not None:
            body["top_n"] = top_n
        response = httpx.post(
            f"{self.api_base}/compatible-api/v1/reranks",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=body,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return {r["index"]: r["relevance_score"] for r in data["results"]}


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left)) or 1.0
    right_norm = math.sqrt(sum(b * b for b in right)) or 1.0
    return max(0.0, min(1.0, dot / (left_norm * right_norm)))
