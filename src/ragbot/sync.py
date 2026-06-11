from __future__ import annotations

from datetime import datetime
from typing import Protocol

from ragbot.domain import HelpDocument
from ragbot.ingestion import IngestionService
from ragbot.repositories import KnowledgeRepository


class HelpDocumentSource(Protocol):
    def fetch_updated_since(self, since: datetime | None) -> list[HelpDocument]:
        ...


class KnowledgeSyncJob:
    def __init__(
        self,
        source: HelpDocumentSource,
        ingestion_service: IngestionService,
        repository: KnowledgeRepository,
    ) -> None:
        self.source = source
        self.ingestion_service = ingestion_service
        self.repository = repository

    def run_once(self, since: datetime | None = None) -> int:
        documents = self.source.fetch_updated_since(since)
        chunk_count = 0
        for document in documents:
            chunks = self.ingestion_service.ingest_document(document)
            self.repository.upsert_chunks(chunks)
            chunk_count += len(chunks)
        return chunk_count

