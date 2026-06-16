from __future__ import annotations

import re

from ragbot.domain import AnswerDecision, ConfidenceLevel, RetrievalResult
from ragbot.providers import LLMProvider


class AnswerService:
    def __init__(self, llm_provider: LLMProvider, max_context_chars: int = 2400) -> None:
        self.llm_provider = llm_provider
        self.max_context_chars = max_context_chars

    def answer(self, question: str, retrieval: RetrievalResult) -> AnswerDecision:
        cited_chunk_ids = [hit.chunk_reference for hit in retrieval.hits]
        # Use effective_answer_content (answer-only content) for LLM context generation.
        # Falls back to full content if answer_content is not set.
        contexts = self._compact_contexts([hit.chunk.effective_answer_content for hit in retrieval.hits])
        if retrieval.confidence == ConfidenceLevel.LOW:
            return AnswerDecision(
                answer=None,
                confidence=retrieval.confidence,
                confidence_score=retrieval.confidence_score,
                auto_reply=False,
                needs_human=True,
                cited_chunk_ids=cited_chunk_ids,
            )
        answer = self.llm_provider.generate_answer(question, contexts)
        return AnswerDecision(
            answer=answer,
            confidence=retrieval.confidence,
            confidence_score=retrieval.confidence_score,
            auto_reply=retrieval.confidence == ConfidenceLevel.HIGH,
            needs_human=retrieval.confidence != ConfidenceLevel.HIGH,
            cited_chunk_ids=cited_chunk_ids,
        )

    def _compact_contexts(self, contexts: list[str]) -> list[str]:
        """Keep only short precise answers; skip long generic chunks entirely.

        Long chunks tend to be generic help-center articles that dilute the
        LLM prompt without adding signal.  Short snippets (≤ 200 chars) are
        almost always a targeted answer (操作步骤 / 标准回答).

        When no short snippet survives, the LLM will receive an empty context
        list and fall back to the handoff reply, which is the correct
        behaviour — the KB doesn't have a concise answer for this query.
        """
        cleaned = [self._clean_context(c) for c in contexts]
        short = [c for c in cleaned if c and len(c) <= 200]
        compacted: list[str] = []
        remaining = self.max_context_chars
        for context in short:
            if remaining >= len(context):
                compacted.append(context)
                remaining -= len(context)
        return compacted

    def _clean_context(self, context: str) -> str:
        context = re.sub(r"\[图片:[^\]]+\]", "", context)
        context = re.sub(r"图片说明：.*", "", context)
        context = re.sub(r"图片 OCR：.*", "", context)
        context = re.sub(r"\n{3,}", "\n\n", context)
        context = re.sub(r"[ \t]{2,}", " ", context)
        return context.strip()
