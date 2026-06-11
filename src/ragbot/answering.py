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
        compacted: list[str] = []
        remaining = self.max_context_chars
        for context in contexts:
            if remaining <= 0:
                break
            cleaned = self._clean_context(context)
            if not cleaned:
                continue
            clipped = cleaned[:remaining]
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
