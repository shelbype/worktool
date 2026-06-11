from __future__ import annotations

from dataclasses import replace

from ragbot.audience import AudienceAssigner
from ragbot.domain import HelpDocument, ReviewItem, ReviewStatus, utcnow
from ragbot.ingestion import IngestionService
from ragbot.repositories import KnowledgeRepository


class ReviewService:
    def __init__(
        self,
        repository: KnowledgeRepository,
        ingestion_service: IngestionService,
        audience_assigner: AudienceAssigner | None = None,
        audience_routing_enabled: bool = False,
    ) -> None:
        self.repository = repository
        self.ingestion_service = ingestion_service
        self.audience_assigner = audience_assigner
        self.audience_routing_enabled = audience_routing_enabled

    def list_pending(self) -> list[ReviewItem]:
        return self.repository.list_review_items(ReviewStatus.PENDING)

    def approve(self, review_id: str, reviewer_id: str, answer: str | None = None) -> ReviewItem:
        item = self._get_review(review_id)
        approved = replace(
            item,
            answer=answer or item.answer,
            status=ReviewStatus.APPROVED,
            reviewer_id=reviewer_id,
            reviewed_at=utcnow(),
        )
        self.repository.update_review_item(approved)
        if approved.answer:
            doc = HelpDocument(
                source_id=f"review:{approved.id}",
                title=approved.question,
                body_html=f"<h1>{approved.question}</h1><p>{approved.answer}</p>",
                category="客户群问答",
            )
            chunks = self.ingestion_service.ingest_document(doc)
            self.repository.upsert_chunks(chunks)
            if self.audience_routing_enabled and self.audience_assigner and hasattr(self.repository, "upsert_audience_chunks"):
                for audience in self.audience_assigner.assign_document(doc):
                    self.repository.upsert_audience_chunks(audience, chunks)
        return approved

    def reject(self, review_id: str, reviewer_id: str) -> ReviewItem:
        item = self._get_review(review_id)
        rejected = replace(item, status=ReviewStatus.REJECTED, reviewer_id=reviewer_id, reviewed_at=utcnow())
        self.repository.update_review_item(rejected)
        return rejected

    def _get_review(self, review_id: str) -> ReviewItem:
        for item in self.repository.list_review_items():
            if item.id == review_id:
                return item
        raise KeyError(f"review item not found: {review_id}")
