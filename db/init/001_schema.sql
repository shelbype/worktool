CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS help_documents (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    category TEXT,
    product_module TEXT,
    product_version TEXT,
    source_url TEXT,
    body_html TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active',
    source_updated_at TIMESTAMPTZ NOT NULL,
    synced_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS knowledge_chunks (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES help_documents(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    image_refs JSONB NOT NULL DEFAULT '[]',
    metadata JSONB NOT NULL DEFAULT '{}',
    embedding vector(64),
    status TEXT NOT NULL DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_knowledge_chunks_status ON knowledge_chunks(status);
CREATE INDEX IF NOT EXISTS idx_knowledge_chunks_metadata ON knowledge_chunks USING gin(metadata);
CREATE INDEX IF NOT EXISTS idx_knowledge_chunks_content_fts
    ON knowledge_chunks USING gin(to_tsvector('simple', content));
CREATE INDEX IF NOT EXISTS idx_knowledge_chunks_embedding
    ON knowledge_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

CREATE TABLE IF NOT EXISTS conversation_logs (
    id TEXT PRIMARY KEY,
    group_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    message_id TEXT NOT NULL UNIQUE,
    question TEXT NOT NULL,
    confidence TEXT NOT NULL,
    confidence_score DOUBLE PRECISION NOT NULL,
    retrieved_chunks JSONB NOT NULL DEFAULT '[]',
    draft_answer TEXT,
    final_answer TEXT,
    auto_replied BOOLEAN NOT NULL DEFAULT false,
    needs_human BOOLEAN NOT NULL DEFAULT true,
    routed_audiences JSONB NOT NULL DEFAULT '[]',
    routing_confidence TEXT,
    routing_reason TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

DO $$
DECLARE
    audience_name TEXT;
    table_name TEXT;
BEGIN
    FOREACH audience_name IN ARRAY ARRAY['student', 'teacher', 'principal', 'academic', 'sales']
    LOOP
        table_name := 'knowledge_chunks_' || audience_name;
        EXECUTE format(
            'CREATE TABLE IF NOT EXISTS %I (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL REFERENCES help_documents(id) ON DELETE CASCADE,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                image_refs JSONB NOT NULL DEFAULT ''[]'',
                metadata JSONB NOT NULL DEFAULT ''{}'',
                embedding vector(64),
                status TEXT NOT NULL DEFAULT ''active'',
                created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
            )',
            table_name
        );
        EXECUTE format('CREATE INDEX IF NOT EXISTS idx_%s_status ON %I(status)', table_name, table_name);
        EXECUTE format('CREATE INDEX IF NOT EXISTS idx_%s_metadata ON %I USING gin(metadata)', table_name, table_name);
        EXECUTE format(
            'CREATE INDEX IF NOT EXISTS idx_%s_content_fts ON %I USING gin(to_tsvector(''simple'', content))',
            table_name,
            table_name
        );
        EXECUTE format(
            'CREATE INDEX IF NOT EXISTS idx_%s_embedding ON %I USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)',
            table_name,
            table_name
        );
    END LOOP;
END $$;

CREATE TABLE IF NOT EXISTS review_items (
    id TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL REFERENCES conversation_logs(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    answer TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    reviewer_id TEXT,
    reviewed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS bot_rules (
    id TEXT PRIMARY KEY,
    rule_type TEXT NOT NULL,
    pattern TEXT NOT NULL,
    action TEXT NOT NULL,
    enabled BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
