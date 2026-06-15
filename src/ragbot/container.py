from __future__ import annotations

from ragbot.answering import AnswerService
from ragbot.adapters.wechat import HttpWechatBotAdapter
from ragbot.audience import AudienceAssigner
from ragbot.config import get_settings
from ragbot.ingestion import IngestionService
from ragbot.providers import HashEmbeddingProvider, HttpEmbeddingProvider, HttpLLMProvider, HttpRerankProvider, MockLLMProvider
from ragbot.repositories import InMemoryKnowledgeRepository, PostgresKnowledgeRepository
from ragbot.intent import IntentClassifier
from ragbot.retrieval import RetrievalService
from ragbot.review import ReviewService
from ragbot.workflow import CapturingWechatBotAdapter, MessagePreprocessor, WechatRagWorkflow


class AppContainer:
    def __init__(self) -> None:
        self.settings = get_settings()
        if self.settings.repository_provider == "postgres":
            self.repository = PostgresKnowledgeRepository(
                self.settings.postgres_dsn,
                vector_index_type=self.settings.vector_index_type,
                vector_index_m=self.settings.vector_index_m,
                vector_index_ef_construction=self.settings.vector_index_ef_construction,
                vector_index_ef_search=self.settings.vector_index_ef_search,
                vector_index_lists=self.settings.vector_index_lists,
            )
        else:
            self.repository = InMemoryKnowledgeRepository()

        if self.settings.embedding_provider == "http":
            self.embedding_provider = HttpEmbeddingProvider(
                self.settings.embedding_api_base or self.settings.llm_api_base,
                self.settings.embedding_api_key or self.settings.llm_api_key,
                self.settings.embedding_model,
                self.settings.embedding_dimensions,
                self.settings.embedding_encoding_format,
            )
        else:
            self.embedding_provider = HashEmbeddingProvider(self.settings.embedding_dimensions)
        if self.settings.llm_provider == "mock":
            self.llm_provider = MockLLMProvider()
        else:
            self.llm_provider = HttpLLMProvider(
                self.settings.llm_api_base,
                self.settings.llm_api_key,
                self.settings.llm_model,
                self.settings.llm_max_tokens,
            )
        if self.settings.llm_query_rewrite_provider == "mock":
            self.query_rewrite_provider = None
        else:
            self.query_rewrite_provider = HttpLLMProvider(
                self.settings.llm_query_rewrite_api_base or self.settings.llm_api_base,
                self.settings.llm_query_rewrite_api_key or self.settings.llm_api_key,
                self.settings.llm_query_rewrite_model,
            )
        if self.settings.intent_classify_provider == "mock":
            self.intent_classify_provider = None
        else:
            self.intent_classify_provider = HttpLLMProvider(
                self.settings.intent_classify_api_base or self.settings.llm_api_base,
                self.settings.intent_classify_api_key or self.settings.llm_api_key,
                self.settings.intent_classify_model,
            )
        self.intent_classifier = IntentClassifier(
            self.intent_classify_provider,
            enabled=self.settings.intent_classify_enabled,
            decompose_enabled=self.settings.multi_intent_decompose_enabled,
        )
        if self.settings.llm_rerank_provider == "mock":
            self.rerank_provider = None
        else:
            self.rerank_provider = HttpRerankProvider(
                self.settings.llm_rerank_api_base
                or self.settings.llm_query_rewrite_api_base
                or self.settings.llm_api_base,
                self.settings.llm_rerank_api_key
                or self.settings.llm_query_rewrite_api_key
                or self.settings.llm_api_key,
                self.settings.llm_rerank_model,
            )
        self.ingestion_service = IngestionService(self.embedding_provider)
        self.retrieval_service = RetrievalService(
            self.repository, self.embedding_provider, self.settings,
            llm_provider=self.query_rewrite_provider,
            intent_classifier=self.intent_classifier,
            rerank_provider=self.rerank_provider,
        )
        self.answer_service = AnswerService(self.llm_provider, self.settings.max_llm_context_chars)
        if self.settings.worktool_robot_id:
            self.wechat_adapter = HttpWechatBotAdapter(
                self.settings.worktool_api_base,
                self.settings.worktool_robot_id,
                self.settings.worktool_send_api_token,
            )
        else:
            self.wechat_adapter = CapturingWechatBotAdapter()
        self.workflow = WechatRagWorkflow(
            self.repository,
            self.retrieval_service,
            self.answer_service,
            self.wechat_adapter,
            MessagePreprocessor(rules_path=self.settings.handoff_rules_path),
        )
        self.review_service = ReviewService(
            self.repository,
            self.ingestion_service,
            AudienceAssigner(self.settings.audience_routing_path),
            self.settings.audience_routing_enabled,
        )


container = AppContainer()
