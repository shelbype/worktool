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
        """Pack contexts into the token budget, favouring short precise answers.

        Long generic chunks can crowd out the short, high-precision snippet
        that directly answers the question.  A two-pass strategy ensures the
        best-matching short answer is always included intact before large
        chunks consume the remaining capacity.

        * Pass 1 — preserve short snippets (≤ 200 chars) in ranking order.
        * Pass 2 — top-off with longer chunks, each truncated to fit.
        """
        cleaned = [self._clean_context(c) for c in contexts]
        cleaned = [c for c in cleaned if c]

        compacted: list[str] = []
        remaining = self.max_context_chars

        # Pass 1: short, high-signal snippets — keep intact
        for context in cleaned:
            if remaining <= 0:
                break
            if len(context) <= 200 and remaining >= len(context):
                compacted.append(context)
                remaining -= len(context)

        # Pass 2: longer chunks fill the remaining budget
        for context in cleaned:
            if remaining <= 0:
                break
            if len(context) > 200:
                clipped = context[:remaining]
                compacted.append(clipped)
                remaining -= len(clipped)

        return compacted

    def _clean_context(self, context: str) -> str:
        context = re.sub(r"\[图片:[^\]]+\]", "", context)
        context = re.sub(r"图片说明：.*", "", context)
        context = re.sub(r"图片 OCR：.*", "", context)
        context = re.sub(r"\n{3,}", "\n\n", context)
        context = re.sub(r"[ \t]{2,}", " ", context)
        return context.strip()
