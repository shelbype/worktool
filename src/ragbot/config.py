from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "enterprise-wechat-rag"
    environment: str = "development"

    postgres_dsn: str = "postgresql://rag:rag@localhost:5432/rag"
    repository_provider: str = "memory"
    mysql_dsn: str = ""
    mysql_help_doc_table: str = "help_documents"

    llm_provider: str = "mock"
    embedding_provider: str = "hash"
    embedding_dimensions: int = Field(default=64, ge=1)
    llm_api_base: str = ""
    llm_api_key: str = ""
    llm_model: str = "qwen-plus"
    llm_query_rewrite_provider: str = "mock"
    llm_query_rewrite_enabled: bool = False
    llm_query_rewrite_model: str = "qwen3.6-flash"
    llm_query_rewrite_api_base: str = ""
    llm_query_rewrite_api_key: str = ""
    intent_classify_enabled: bool = False
    intent_classify_provider: str = "mock"
    intent_classify_model: str = "qwen3.6-flash"
    intent_classify_api_base: str = ""
    intent_classify_api_key: str = ""
    multi_intent_decompose_enabled: bool = True
    llm_rerank_provider: str = "mock"
    llm_rerank_enabled: bool = False
    llm_rerank_model: str = "qwen3-rerank"
    llm_rerank_api_base: str = ""
    llm_rerank_api_key: str = ""
    embedding_model: str = "text-embedding-v4"
    embedding_api_base: str = ""
    embedding_api_key: str = ""
    embedding_encoding_format: str = "float"

    vector_index_type: str = "hnsw"
    vector_index_m: int = Field(default=8, ge=2, le=100)
    vector_index_ef_construction: int = Field(default=200, ge=10, le=2000)
    vector_index_ef_search: int = Field(default=50, ge=1, le=1000)
    vector_index_lists: int = Field(default=100, ge=10, le=10000)

    auto_reply_threshold: float = Field(default=0.72, ge=0, le=1)
    draft_only_threshold: float = Field(default=0.50, ge=0, le=1)
    top_k: int = Field(default=5, ge=1, le=20)
    reply_images_enabled: bool = True
    max_reply_images: int = Field(default=1, ge=0, le=10)
    image_reply_delay_seconds: float = Field(default=2.5, ge=0, le=30)
    reply_image_captions_enabled: bool = False
    batch_image_reply_enabled: bool = True
    max_llm_context_chars: int = Field(default=2400, ge=500, le=12000)
    llm_max_tokens: int = Field(default=500, ge=100, le=2000)
    fast_image_reply_enabled: bool = True
    fast_image_answer_chars: int = Field(default=700, ge=200, le=2000)
    human_handoff_enabled: bool = True
    human_handoff_mention_name: str = "校校助理"
    human_handoff_message_prefix: str = "老师稍等，我们这边具体看下问题。@校校助理"
    query_aliases_path: str = "config/query_aliases.json"
    fast_answer_templates_path: str = "config/fast_answer_templates.json"
    audience_routing_enabled: bool = False
    audience_routing_path: str = "config/audience_routing.json"
    max_route_audiences: int = Field(default=3, ge=1, le=5)

    worktool_api_base: str = "https://api.worktool.ymdyes.cn"
    worktool_robot_id: str = ""
    worktool_send_api_token: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
