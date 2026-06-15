from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import uuid4


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class DocumentStatus(StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"


class ConfidenceLevel(StrEnum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ReviewStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(slots=True)
class HelpDocument:
    source_id: str
    title: str
    body_html: str
    category: str | None = None
    product_module: str | None = None
    product_version: str | None = None
    source_url: str | None = None
    image_urls: list[str] = field(default_factory=list)
    status: DocumentStatus = DocumentStatus.ACTIVE
    updated_at: datetime = field(default_factory=utcnow)
    id: str = field(default_factory=lambda: new_id("doc"))


@dataclass(slots=True)
class ImageRef:
    url: str
    alt_text: str | None = None
    ocr_text: str | None = None
    caption: str | None = None


@dataclass(slots=True)
class KnowledgeChunk:
    document_id: str
    title: str
    content: str
    metadata: dict[str, Any]
    image_refs: list[ImageRef] = field(default_factory=list)
    embedding: list[float] = field(default_factory=list)
    status: DocumentStatus = DocumentStatus.ACTIVE
    search_text: str | None = None
    answer_content: str | None = None
    id: str = field(default_factory=lambda: new_id("chunk"))

    @property
    def effective_search_text(self) -> str:
        """Return search_text if set, otherwise fall back to content."""
        return self.search_text or self.content

    @property
    def effective_answer_content(self) -> str:
        """Return answer_content if set, otherwise fall back to content."""
        return self.answer_content or self.content


@dataclass(slots=True)
class RetrievalHit:
    chunk: KnowledgeChunk
    keyword_score: float
    vector_score: float
    rerank_score: float
    audience: str | None = None

    @property
    def chunk_reference(self) -> str:
        if self.audience:
            return f"{self.audience}|{self.chunk.id}"
        return self.chunk.id


@dataclass(slots=True)
class RetrievalResult:
    query: str
    hits: list[RetrievalHit]
    confidence: ConfidenceLevel
    confidence_score: float
    routed_audiences: list[str] = field(default_factory=list)
    routing_confidence: str | None = None
    routing_reason: str | None = None
    # Intent classification (P1-11)
    intent: str | None = None
    is_multi_intent: bool = False
    intent_sub_queries: list[str] = field(default_factory=list)
    intent_reasoning: str | None = None


@dataclass(slots=True)
class AnswerDecision:
    answer: str | None
    confidence: ConfidenceLevel
    confidence_score: float
    auto_reply: bool
    needs_human: bool
    cited_chunk_ids: list[str]


@dataclass(slots=True)
class WechatMessage:
    message_id: str
    group_id: str
    user_id: str
    content: str
    message_type: str = "text"
    created_at: datetime = field(default_factory=utcnow)
    quoted_message_id: str | None = None
    attachments: list[dict[str, Any]] = field(default_factory=list)


@dataclass(slots=True)
class ConversationLog:
    group_id: str
    user_id: str
    message_id: str
    question: str
    confidence: ConfidenceLevel
    confidence_score: float
    retrieved_chunk_ids: list[str]
    draft_answer: str | None
    final_answer: str | None
    auto_replied: bool
    needs_human: bool
    routed_audiences: list[str] = field(default_factory=list)
    routing_confidence: str | None = None
    routing_reason: str | None = None
    id: str = field(default_factory=lambda: new_id("conv"))
    created_at: datetime = field(default_factory=utcnow)


@dataclass(slots=True)
class ReviewItem:
    conversation_id: str
    question: str
    answer: str | None
    status: ReviewStatus = ReviewStatus.PENDING
    reviewer_id: str | None = None
    id: str = field(default_factory=lambda: new_id("review"))
    created_at: datetime = field(default_factory=utcnow)
    reviewed_at: datetime | None = None
