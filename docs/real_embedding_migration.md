# 真实 Embedding 迁移步骤

当前系统已经支持把本地 hash embedding 切换为 OpenAI 兼容的真实中文 embedding API，并重建 PostgreSQL + pgvector 索引。

## 推荐配置

DeepSeek 继续用于回答生成，不建议作为 embedding provider。真实向量建议单独配置中文 embedding API，例如千问/DashScope `text-embedding-v4`。

```env
EMBEDDING_PROVIDER=http
EMBEDDING_API_BASE=https://dashscope.aliyuncs.com/compatible-mode/v1
EMBEDDING_API_KEY=你的EmbeddingKey
EMBEDDING_MODEL=text-embedding-v4
EMBEDDING_DIMENSIONS=1024
EMBEDDING_ENCODING_FORMAT=float
```

## 迁移命令

先确认真实模型返回维度：

```bash
python -m ragbot.cli inspect-embedding --text "怎么新建班级"
```

如果输出 `actual_dimensions` 为 `1024`，再迁移 pgvector 列：

```bash
python -m ragbot.cli migrate-vector-dim --dimensions 1024
```

然后全量重建帮助中心索引：

```bash
python -m ragbot.cli rebuild-index --source db/init
```

最后跑评测并重启服务：

```bash
python -m ragbot.cli eval-retrieval --cases eval/questions.json
sudo systemctl restart worktool-rag
```

## 注意事项

- `migrate-vector-dim` 会把旧的 hash 向量清空，所以必须紧接着执行 `rebuild-index`。
- `EMBEDDING_DIMENSIONS` 必须和真实模型返回的向量维度一致。
- 如果 `inspect-embedding` 返回 401/403，说明 key 或 API base 不正确。
- 如果返回 404，通常说明该供应商不提供 OpenAI 兼容的 `/embeddings` 接口，或者 API base 配错。
