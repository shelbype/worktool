from __future__ import annotations

import re
from functools import lru_cache
from typing import Any

import jieba

from ragbot.domain import RetrievalResult
from ragbot.quality_config import load_json_config, string_list
from ragbot.text_utils import normalize_customer_text


def has_fast_answer_template(question: str) -> bool:
    return _template_answer(normalize_customer_text(question)) is not None


def build_fast_image_answer(retrieval: RetrievalResult, max_chars: int = 700) -> str:
    question = normalize_customer_text(retrieval.query)
    template = _template_answer(question)
    if template:
        return _with_image_note(template, retrieval)

    snippets = _select_relevant_snippets(retrieval)
    if not snippets:
        return "老师，这个问题我先帮您转人工确认一下。"

    answer = "老师，您可以先按这几步看下：\n\n" + "\n".join(
        f"{index}. {snippet}" for index, snippet in enumerate(snippets, start=1)
    )
    if len(answer) > max_chars:
        answer = answer[:max_chars].rstrip(" ，,。") + "。"
    return _with_image_note(answer, retrieval)


def _template_answer(question: str) -> str | None:
    # All fast-answer templates are now managed via config/fast_answer_templates.json.
    # Hardcoded Python conditions have been removed in favor of the JSON-based
    # template system which supports runtime hot-reload.
    return _configured_template_answer(question)


def _configured_template_answer(question: str) -> str | None:
    for template in _configured_templates():
        if _matches_template(question, template):
            answer = str(template.get("answer", "")).strip()
            if answer:
                return answer
    return None


@lru_cache(maxsize=1)
def _configured_templates() -> list[dict[str, Any]]:
    templates = load_json_config("config/fast_answer_templates.json", [])
    return [template for template in templates if isinstance(template, dict)]


def _matches_template(question: str, template: dict[str, Any]) -> bool:
    match_all = string_list(template.get("match_all"))
    match_any = string_list(template.get("match_any"))
    match_any_2 = string_list(template.get("match_any_2"))
    match_none = string_list(template.get("match_none"))
    if match_all and not all(word in question for word in match_all):
        return False
    if match_any and not any(word in question for word in match_any):
        return False
    if match_any_2 and not any(word in question for word in match_any_2):
        return False
    if match_none and any(word in question for word in match_none):
        return False
    return bool(match_all or match_any or match_any_2)


def _with_image_note(answer: str, retrieval: RetrievalResult) -> str:
    if any(hit.chunk.image_refs for hit in retrieval.hits):
        return answer.rstrip() + "\n\n我把相关截图也发您，方便对照操作。"
    return answer.rstrip()


def _select_relevant_snippets(retrieval: RetrievalResult, limit: int = 4) -> list[str]:
    query_tokens = _tokens(normalize_customer_text(retrieval.query))
    ranked: list[tuple[float, int, str]] = []
    order = 0
    for hit_index, hit in enumerate(retrieval.hits[:3]):
        # Use effective_answer_content to avoid listing search metadata (问法示例/关键词) as answer
        snippet_source = hit.chunk.effective_answer_content
        for line in _clean_context_lines(snippet_source, hit.chunk.title):
            order += 1
            score = _line_score(query_tokens, line) + max(0.0, hit.rerank_score) * 0.2
            if hit_index == 0:
                score += 0.1
            if score <= 0.1:
                continue
            ranked.append((score, order, line))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    snippets: list[str] = []
    seen: set[str] = set()
    for _, _, line in ranked:
        # Normalize for dedup: strip leading step numbers ("1）", "4. 1）",
        # "(1)", "（1）", "①", "2.", etc.), then remove all non-word chars.
        # This prevents the same content with different numbering from
        # appearing as duplicate snippets.
        normalized = re.sub(r"^(?:[(（]?\d+[)）.]?\s*|[①②③④⑤⑥⑦⑧⑨⑩]+\s*|[a-z][.)]\s*)+", "", line)
        key = re.sub(r"\W+", "", normalized)
        if not key or key in seen:
            continue
        seen.add(key)
        snippets.append(line)
        if len(snippets) >= limit:
            break
    return snippets


def _clean_context_lines(content: str, title: str) -> list[str]:
    content = re.sub(r"\[图片:[^\]]+\]", "\n", content)
    lines: list[str] = []
    for raw_line in re.split(r"[\n。；;]", content):
        line = re.sub(r"\s+", " ", raw_line).strip(" ，,。；;")
        if not line or line == title:
            continue
        if line.startswith(("图片说明：", "图片 OCR：", "关键词：")):
            continue
        if len(line) < 4:
            continue
        lines.append(line)
    return lines


def _line_score(query_tokens: set[str], line: str) -> float:
    if not query_tokens:
        return 0.0
    line_tokens = _tokens(line)
    if not line_tokens:
        return 0.0
    overlap = len(query_tokens & line_tokens) / max(1, len(query_tokens))
    action_boost = 0.15 if any(word in line for word in ("点击", "填写", "选择", "添加", "进入", "创建")) else 0.0
    return overlap + action_boost


def _tokens(text: str) -> set[str]:
    latin = re.findall(r"[a-zA-Z0-9_./-]+", text.lower())
    chinese = re.findall(r"[\u4e00-\u9fff]+", text)
    chinese_tokens: set[str] = set()
    for segment in chinese:
        for word in jieba.cut(segment):
            word = word.strip()
            if word:
                chinese_tokens.add(word)
        # Keep bigram fallback for substring / fuzzy matching
        for i in range(len(segment) - 1):
            chinese_tokens.add(segment[i:i + 2])
    return set(latin) | chinese_tokens
