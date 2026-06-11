from __future__ import annotations

import json
from dataclasses import asdict, replace
from datetime import datetime
from typing import Protocol

import psycopg
from psycopg.rows import dict_row

from ragbot.audience import AUDIENCES
from ragbot.domain import (
    ConfidenceLevel,
    ConversationLog,
    DocumentStatus,
    ImageRef,
    KnowledgeChunk,
    ReviewItem,
    ReviewStatus,
)


AUDIENCE_TABLES = {audience: f"knowledge_chunks_{audience}" for audience in AUDIENCES}


class KnowledgeRepository(Protocol):
    def upsert_chunks(self, chunks: list[KnowledgeChunk]) -> None:
        ...

    def list_active_chunks(self) -> list[KnowledgeChunk]:
        ...

    def find_candidate_chunks(
        self,
        query: str,
        query_embedding: list[float],
        product_module: str | None,
        limit: int,
        audiences: list[str] | None = None,
    ) -> list[KnowledgeChunk]:
        ...

    def get_chunk(self, chunk_id: str) -> KnowledgeChunk | None:
        ...

    def save_conversation(self, log: ConversationLog) -> None:
        ...

    def get_conversation_by_message_id(self, message_id: str) -> ConversationLog | None:
        ...

    def list_conversations(self, limit: int = 50) -> list[ConversationLog]:
        ...

    def add_review_item(self, item: ReviewItem) -> None:
        ...

    def list_review_items(self, status: ReviewStatus | None = None) -> list[ReviewItem]:
        ...

    def update_review_item(self, item: ReviewItem) -> None:
        ...


class InMemoryKnowledgeRepository:
    def __init__(self) -> None:
        self._chunks: dict[str, KnowledgeChunk] = {}
        self._audience_chunks: dict[str, dict[str, KnowledgeChunk]] = {audience: {} for audience in AUDIENCES}
        self._conversations: dict[str, ConversationLog] = {}
        self._reviews: dict[str, ReviewItem] = {}

    def upsert_chunks(self, chunks: list[KnowledgeChunk]) -> None:
        for chunk in chunks:
            self._chunks[chunk.id] = chunk

    def upsert_audience_chunks(self, audience: str, chunks: list[KnowledgeChunk]) -> None:
        if audience not in self._audience_chunks:
            raise ValueError(f"unknown audience: {audience}")
        for chunk in chunks:
            metadata = {**chunk.metadata, "audience": audience}
            self._audience_chunks[audience][chunk.id] = replace(chunk, metadata=metadata)

    def clear_audience_knowledge(self) -> None:
        self._audience_chunks = {audience: {} for audience in AUDIENCES}

    def list_active_chunks(self) -> list[KnowledgeChunk]:
        return [chunk for chunk in self._chunks.values() if chunk.status == "active"]

    def find_candidate_chunks(
        self,
        query: str,
        query_embedding: list[float],
        product_module: str | None,
        limit: int,
        audiences: list[str] | None = None,
    ) -> list[KnowledgeChunk]:
        chunks: list[KnowledgeChunk] = []
        if audiences:
            for audience in audiences:
                chunks.extend(self._audience_chunks.get(audience, {}).values())
        if not chunks:
            chunks = self.list_active_chunks()
        if product_module:
            chunks = [chunk for chunk in chunks if chunk.metadata.get("product_module") == product_module]
        return chunks[:limit]

    def get_chunk(self, chunk_id: str) -> KnowledgeChunk | None:
        audience, actual_chunk_id = self._split_chunk_reference(chunk_id)
        if audience:
            return self._audience_chunks.get(audience, {}).get(actual_chunk_id)
        return self._chunks.get(chunk_id)

    def save_conversation(self, log: ConversationLog) -> None:
        self._conversations[log.message_id] = log

    def get_conversation_by_message_id(self, message_id: str) -> ConversationLog | None:
        return self._conversations.get(message_id)

    def list_conversations(self, limit: int = 50) -> list[ConversationLog]:
        return sorted(self._conversations.values(), key=lambda log: log.created_at, reverse=True)[:limit]

    def add_review_item(self, item: ReviewItem) -> None:
        self._reviews[item.id] = item

    def list_review_items(self, status: ReviewStatus | None = None) -> list[ReviewItem]:
        items = list(self._reviews.values())
        if status is None:
            return items
        return [item for item in items if item.status == status]

    def update_review_item(self, item: ReviewItem) -> None:
        if item.id not in self._reviews:
            raise KeyError(f"review item not found: {item.id}")
        self._reviews[item.id] = replace(item)

    def _split_chunk_reference(self, value: str) -> tuple[str | None, str]:
        if "|" not in value:
            return None, value
        audience, chunk_id = value.split("|", 1)
        if audience not in AUDIENCE_TABLES:
            return None, value
        return audience, chunk_id


class PostgresKnowledgeRepository:
    def __init__(self, dsn: str, candidate_limit: int = 200) -> None:
        self.dsn = dsn
        self.candidate_limit = candidate_limit

    def init_schema(self, schema_sql: str) -> None:
        with self._connect() as conn:
            conn.execute(schema_sql)

    def init_audience_indexes(self, dimensions: int) -> None:
        if dimensions < 1 or dimensions > 4096:
            raise ValueError("embedding dimensions must be between 1 and 4096")
        with self._connect() as conn:
            conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
            conn.execute("ALTER TABLE conversation_logs ADD COLUMN IF NOT EXISTS routed_audiences JSONB NOT NULL DEFAULT '[]'")
            conn.execute("ALTER TABLE conversation_logs ADD COLUMN IF NOT EXISTS routing_confidence TEXT")
            conn.execute("ALTER TABLE conversation_logs ADD COLUMN IF NOT EXISTS routing_reason TEXT")
            for audience, table in AUDIENCE_TABLES.items():
                conn.execute(self._create_chunk_table_sql(table, dimensions))
                conn.execute(f"CREATE INDEX IF NOT EXISTS idx_{table}_status ON {table}(status)")
                conn.execute(f"CREATE INDEX IF NOT EXISTS idx_{table}_metadata ON {table} USING gin(metadata)")
                conn.execute(
                    f"""
                    CREATE INDEX IF NOT EXISTS idx_{table}_content_fts
                        ON {table} USING gin(to_tsvector('simple', content))
                    """
                )
                conn.execute(
                    f"""
                    CREATE INDEX IF NOT EXISTS idx_{table}_embedding
                        ON {table} USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)
                    """
                )

    def migrate_embedding_dimension(self, dimensions: int) -> None:
        if dimensions < 1 or dimensions > 4096:
            raise ValueError("embedding dimensions must be between 1 and 4096")
        with self._connect() as conn:
            conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
            conn.execute("DROP INDEX IF EXISTS idx_knowledge_chunks_embedding")
            conn.execute(
                f"""
                ALTER TABLE knowledge_chunks
                ALTER COLUMN embedding TYPE vector({dimensions}) USING NULL
                """
            )
            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_knowledge_chunks_embedding
                    ON knowledge_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)
                """
            )
            for table in AUDIENCE_TABLES.values():
                conn.execute(f"DROP INDEX IF EXISTS idx_{table}_embedding")
                conn.execute(
                    f"""
                    ALTER TABLE IF EXISTS {table}
                    ALTER COLUMN embedding TYPE vector({dimensions}) USING NULL
                    """
                )
                conn.execute(
                    f"""
                    CREATE INDEX IF NOT EXISTS idx_{table}_embedding
                        ON {table} USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)
                    """
                )

    def clear_knowledge(self) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM knowledge_chunks")
            conn.execute("DELETE FROM help_documents")

    def clear_audience_knowledge(self) -> None:
        with self._connect() as conn:
            for table in AUDIENCE_TABLES.values():
                conn.execute(f"DELETE FROM {table}")

    def upsert_chunks(self, chunks: list[KnowledgeChunk]) -> None:
        with self._connect() as conn:
            self._upsert_chunks_to_table(conn, "knowledge_chunks", chunks)

    def upsert_audience_chunks(self, audience: str, chunks: list[KnowledgeChunk]) -> None:
        table = self._audience_table(audience)
        with self._connect() as conn:
            audience_chunks = [replace(chunk, metadata={**chunk.metadata, "audience": audience}) for chunk in chunks]
            self._upsert_chunks_to_table(conn, table, audience_chunks)

    def list_active_chunks(self) -> list[KnowledgeChunk]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, document_id, title, content, search_text, answer_content,
                       image_refs, metadata, embedding::text AS embedding, status
                FROM knowledge_chunks
                WHERE status = 'active'
                ORDER BY updated_at DESC
                LIMIT %s
                """,
                (self.candidate_limit,),
            ).fetchall()
        return [self._row_to_chunk(row) for row in rows]

    def find_candidate_chunks(
        self,
        query: str,
        query_embedding: list[float],
        product_module: str | None,
        limit: int,
        audiences: list[str] | None = None,
    ) -> list[KnowledgeChunk]:
        if audiences:
            chunks: list[KnowledgeChunk] = []
            for audience in audiences:
                table = self._audience_table(audience)
                chunks.extend(
                    self._find_candidate_chunks_in_table(
                        table,
                        query,
                        query_embedding,
                        product_module,
                        limit,
                        audience,
                    )
                )
            return chunks
        return self._find_candidate_chunks_in_table(
            "knowledge_chunks",
            query,
            query_embedding,
            product_module,
            limit,
            None,
        )

    def _find_candidate_chunks_in_table(
        self,
        table: str,
        query: str,
        query_embedding: list[float],
        product_module: str | None,
        limit: int,
        audience: str | None,
    ) -> list[KnowledgeChunk]:
        vector = self._vector_literal(query_embedding)
        with self._connect() as conn:
            rows = conn.execute(
                f"""
                SELECT id, document_id, title, content, search_text, answer_content,
                       image_refs, metadata, embedding::text AS embedding, status
                FROM {table}
                WHERE status = 'active'
                  AND (%(product_module)s::text IS NULL OR metadata->>'product_module' = %(product_module)s::text)
                ORDER BY
                  (
                    CASE
                      WHEN to_tsvector('simple', coalesce(title, '') || ' ' || coalesce(content, ''))
                           @@ plainto_tsquery('simple', %(query)s)
                      THEN 0.25
                      ELSE 0
                    END
                    + coalesce(1 - (embedding <=> %(embedding)s::vector), 0) * 0.75
                  ) DESC
                LIMIT %(limit)s
                """,
                {
                    "query": query,
                    "embedding": vector,
                    "product_module": product_module,
                    "limit": min(limit, self.candidate_limit),
                },
            ).fetchall()
        return [self._row_to_chunk(row, audience) for row in rows]

    def get_chunk(self, chunk_id: str) -> KnowledgeChunk | None:
        audience, actual_chunk_id = self._split_chunk_reference(chunk_id)
        table = self._audience_table(audience) if audience else "knowledge_chunks"
        with self._connect() as conn:
            row = conn.execute(
                f"""
                SELECT id, document_id, title, content, search_text, answer_content,
                       image_refs, metadata, embedding::text AS embedding, status
                FROM {table}
                WHERE id = %s
                """,
                (actual_chunk_id,),
            ).fetchone()
        return self._row_to_chunk(row, audience) if row else None

    def save_conversation(self, log: ConversationLog) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO conversation_logs (
                    id, group_id, user_id, message_id, question, confidence,
                    confidence_score, retrieved_chunks, draft_answer, final_answer,
                    auto_replied, needs_human, created_at, routed_audiences,
                    routing_confidence, routing_reason
                )
                VALUES (
                    %(id)s, %(group_id)s, %(user_id)s, %(message_id)s, %(question)s,
                    %(confidence)s, %(confidence_score)s, %(retrieved_chunks)s::jsonb,
                    %(draft_answer)s, %(final_answer)s, %(auto_replied)s,
                    %(needs_human)s, %(created_at)s, %(routed_audiences)s::jsonb,
                    %(routing_confidence)s, %(routing_reason)s
                )
                ON CONFLICT (message_id) DO UPDATE SET
                    confidence = EXCLUDED.confidence,
                    confidence_score = EXCLUDED.confidence_score,
                    retrieved_chunks = EXCLUDED.retrieved_chunks,
                    draft_answer = EXCLUDED.draft_answer,
                    final_answer = EXCLUDED.final_answer,
                    auto_replied = EXCLUDED.auto_replied,
                    needs_human = EXCLUDED.needs_human,
                    routed_audiences = EXCLUDED.routed_audiences,
                    routing_confidence = EXCLUDED.routing_confidence,
                    routing_reason = EXCLUDED.routing_reason
                """,
                {
                    "id": log.id,
                    "group_id": log.group_id,
                    "user_id": log.user_id,
                    "message_id": log.message_id,
                    "question": log.question,
                    "confidence": str(log.confidence),
                    "confidence_score": log.confidence_score,
                    "retrieved_chunks": json.dumps(log.retrieved_chunk_ids, ensure_ascii=False),
                    "draft_answer": log.draft_answer,
                    "final_answer": log.final_answer,
                    "auto_replied": log.auto_replied,
                    "needs_human": log.needs_human,
                    "created_at": log.created_at,
                    "routed_audiences": json.dumps(log.routed_audiences, ensure_ascii=False),
                    "routing_confidence": log.routing_confidence,
                    "routing_reason": log.routing_reason,
                },
            )

    def get_conversation_by_message_id(self, message_id: str) -> ConversationLog | None:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT id, group_id, user_id, message_id, question, confidence,
                       confidence_score, retrieved_chunks, draft_answer, final_answer,
                       auto_replied, needs_human, routed_audiences,
                       routing_confidence, routing_reason, created_at
                FROM conversation_logs
                WHERE message_id = %s
                """,
                (message_id,),
            ).fetchone()
        if not row:
            return None
        return ConversationLog(
            id=row["id"],
            group_id=row["group_id"],
            user_id=row["user_id"],
            message_id=row["message_id"],
            question=row["question"],
            confidence=ConfidenceLevel(row["confidence"]),
            confidence_score=float(row["confidence_score"]),
            retrieved_chunk_ids=self._json_value(row["retrieved_chunks"], []),
            draft_answer=row["draft_answer"],
            final_answer=row["final_answer"],
            auto_replied=bool(row["auto_replied"]),
            needs_human=bool(row["needs_human"]),
            routed_audiences=self._json_value(row["routed_audiences"], []),
            routing_confidence=row["routing_confidence"],
            routing_reason=row["routing_reason"],
            created_at=row["created_at"],
        )

    def list_conversations(self, limit: int = 50) -> list[ConversationLog]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, group_id, user_id, message_id, question, confidence,
                       confidence_score, retrieved_chunks, draft_answer, final_answer,
                       auto_replied, needs_human, routed_audiences,
                       routing_confidence, routing_reason, created_at
                FROM conversation_logs
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (limit,),
            ).fetchall()
        logs: list[ConversationLog] = []
        for row in rows:
            logs.append(
                ConversationLog(
                    id=row["id"],
                    group_id=row["group_id"],
                    user_id=row["user_id"],
                    message_id=row["message_id"],
                    question=row["question"],
                    confidence=ConfidenceLevel(row["confidence"]),
                    confidence_score=float(row["confidence_score"]),
                    retrieved_chunk_ids=self._json_value(row["retrieved_chunks"], []),
                    draft_answer=row["draft_answer"],
                    final_answer=row["final_answer"],
                    auto_replied=bool(row["auto_replied"]),
                    needs_human=bool(row["needs_human"]),
                    routed_audiences=self._json_value(row["routed_audiences"], []),
                    routing_confidence=row["routing_confidence"],
                    routing_reason=row["routing_reason"],
                    created_at=row["created_at"],
                )
            )
        return logs

    def add_review_item(self, item: ReviewItem) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO review_items (
                    id, conversation_id, question, answer, status, reviewer_id,
                    reviewed_at, created_at
                )
                VALUES (
                    %(id)s, %(conversation_id)s, %(question)s, %(answer)s,
                    %(status)s, %(reviewer_id)s, %(reviewed_at)s, %(created_at)s
                )
                ON CONFLICT (id) DO UPDATE SET
                    answer = EXCLUDED.answer,
                    status = EXCLUDED.status,
                    reviewer_id = EXCLUDED.reviewer_id,
                    reviewed_at = EXCLUDED.reviewed_at
                """,
                self._review_params(item),
            )

    def list_review_items(self, status: ReviewStatus | None = None) -> list[ReviewItem]:
        params: tuple[str, ...] = ()
        sql = """
            SELECT id, conversation_id, question, answer, status, reviewer_id,
                   reviewed_at, created_at
            FROM review_items
        """
        if status is not None:
            sql += " WHERE status = %s"
            params = (str(status),)
        sql += " ORDER BY created_at DESC"
        with self._connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        return [self._row_to_review(row) for row in rows]

    def update_review_item(self, item: ReviewItem) -> None:
        with self._connect() as conn:
            result = conn.execute(
                """
                UPDATE review_items
                SET question = %(question)s,
                    answer = %(answer)s,
                    status = %(status)s,
                    reviewer_id = %(reviewer_id)s,
                    reviewed_at = %(reviewed_at)s
                WHERE id = %(id)s
                """,
                self._review_params(item),
            )
        if result.rowcount == 0:
            raise KeyError(f"review item not found: {item.id}")

    def _connect(self):
        return psycopg.connect(self.dsn, row_factory=dict_row)

    def _create_chunk_table_sql(self, table: str, dimensions: int) -> str:
        return f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL REFERENCES help_documents(id) ON DELETE CASCADE,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                search_text TEXT,
                answer_content TEXT,
                image_refs JSONB NOT NULL DEFAULT '[]',
                metadata JSONB NOT NULL DEFAULT '{{}}',
                embedding vector({dimensions}),
                status TEXT NOT NULL DEFAULT 'active',
                created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
            )
        """

    def _audience_table(self, audience: str | None) -> str:
        if not audience or audience not in AUDIENCE_TABLES:
            raise ValueError(f"unknown audience: {audience}")
        return AUDIENCE_TABLES[audience]

    def _split_chunk_reference(self, value: str) -> tuple[str | None, str]:
        if "|" not in value:
            return None, value
        audience, chunk_id = value.split("|", 1)
        if audience not in AUDIENCE_TABLES:
            return None, value
        return audience, chunk_id

    def _upsert_chunks_to_table(self, conn, table: str, chunks: list[KnowledgeChunk]) -> None:
        for chunk in chunks:
            document_id = self._upsert_document(conn, chunk)
            conn.execute(
                f"""
                INSERT INTO {table} (
                    id, document_id, title, content, search_text, answer_content,
                    image_refs, metadata, embedding, status, updated_at
                )
                VALUES (
                    %(id)s, %(document_id)s, %(title)s, %(content)s,
                    %(search_text)s, %(answer_content)s,
                    %(image_refs)s::jsonb, %(metadata)s::jsonb,
                    %(embedding)s::vector, %(status)s, now()
                )
                ON CONFLICT (id) DO UPDATE SET
                    document_id = EXCLUDED.document_id,
                    title = EXCLUDED.title,
                    content = EXCLUDED.content,
                    search_text = EXCLUDED.search_text,
                    answer_content = EXCLUDED.answer_content,
                    image_refs = EXCLUDED.image_refs,
                    metadata = EXCLUDED.metadata,
                    embedding = EXCLUDED.embedding,
                    status = EXCLUDED.status,
                    updated_at = now()
                """,
                {
                    "id": chunk.id,
                    "document_id": document_id,
                    "title": chunk.title,
                    "content": chunk.content,
                    "search_text": chunk.search_text,
                    "answer_content": chunk.answer_content,
                    "image_refs": self._image_refs_json(chunk.image_refs),
                    "metadata": json.dumps(chunk.metadata, ensure_ascii=False),
                    "embedding": self._vector_literal(chunk.embedding),
                    "status": str(chunk.status),
                },
            )

    def _upsert_document(self, conn, chunk: KnowledgeChunk) -> str:
        metadata = chunk.metadata
        source_id = str(metadata.get("source_id") or chunk.document_id)
        source_updated_at = self._parse_datetime(metadata.get("updated_at"))
        row = conn.execute(
            """
            INSERT INTO help_documents (
                id, source_id, title, category, product_module, product_version,
                source_url, body_html, status, source_updated_at, synced_at
            )
            VALUES (
                %(id)s, %(source_id)s, %(title)s, %(category)s, %(product_module)s,
                %(product_version)s, %(source_url)s, %(body_html)s, %(status)s,
                %(source_updated_at)s, now()
            )
            ON CONFLICT (source_id) DO UPDATE SET
                title = EXCLUDED.title,
                category = EXCLUDED.category,
                product_module = EXCLUDED.product_module,
                product_version = EXCLUDED.product_version,
                source_url = EXCLUDED.source_url,
                body_html = EXCLUDED.body_html,
                status = EXCLUDED.status,
                source_updated_at = EXCLUDED.source_updated_at,
                synced_at = now()
            RETURNING id
            """,
            {
                "id": chunk.document_id,
                "source_id": source_id,
                "title": chunk.title,
                "category": metadata.get("category"),
                "product_module": metadata.get("product_module"),
                "product_version": metadata.get("product_version"),
                "source_url": metadata.get("source_url"),
                "body_html": chunk.content,
                "status": str(chunk.status),
                "source_updated_at": source_updated_at,
            },
        ).fetchone()
        return row["id"]

    def _row_to_chunk(self, row, audience: str | None = None) -> KnowledgeChunk:
        metadata = self._json_value(row["metadata"], {})
        if audience:
            metadata = {**metadata, "audience": audience}
        return KnowledgeChunk(
            id=row["id"],
            document_id=row["document_id"],
            title=row["title"],
            content=row["content"],
            search_text=row.get("search_text"),
            answer_content=row.get("answer_content"),
            image_refs=[
                ImageRef(
                    url=ref.get("url", ""),
                    alt_text=ref.get("alt_text"),
                    ocr_text=ref.get("ocr_text"),
                    caption=ref.get("caption"),
                )
                for ref in self._json_value(row["image_refs"], [])
            ],
            metadata=metadata,
            embedding=self._parse_vector(row["embedding"]),
            status=DocumentStatus(row["status"]),
        )

    def _row_to_review(self, row) -> ReviewItem:
        return ReviewItem(
            id=row["id"],
            conversation_id=row["conversation_id"],
            question=row["question"],
            answer=row["answer"],
            status=ReviewStatus(row["status"]),
            reviewer_id=row["reviewer_id"],
            reviewed_at=row["reviewed_at"],
            created_at=row["created_at"],
        )

    def _review_params(self, item: ReviewItem) -> dict[str, object]:
        return {
            "id": item.id,
            "conversation_id": item.conversation_id,
            "question": item.question,
            "answer": item.answer,
            "status": str(item.status),
            "reviewer_id": item.reviewer_id,
            "reviewed_at": item.reviewed_at,
            "created_at": item.created_at,
        }

    def _image_refs_json(self, refs: list[ImageRef]) -> str:
        return json.dumps([asdict(ref) for ref in refs], ensure_ascii=False)

    def _vector_literal(self, embedding: list[float]) -> str | None:
        if not embedding:
            return None
        return "[" + ",".join(f"{value:.8f}" for value in embedding) + "]"

    def _parse_vector(self, value: object) -> list[float]:
        if value is None:
            return []
        if isinstance(value, list):
            return [float(item) for item in value]
        text = str(value).strip()
        if not text:
            return []
        return [float(item) for item in text.strip("[]").split(",") if item]

    def _json_value(self, value: object, default):
        if value is None:
            return default
        if isinstance(value, str):
            return json.loads(value)
        return value

    def _parse_datetime(self, value: object) -> datetime:
        if isinstance(value, datetime):
            return value
        if isinstance(value, str) and value:
            return datetime.fromisoformat(value)
        return datetime.now().astimezone()
