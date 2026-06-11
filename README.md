# 企业级微信客服 RAG MVP

这是一个可运行的企业级 RAG 后端骨架，用于把教育 SaaS 帮助文档接入微信客户群自动问答。

## 已实现能力

- MySQL 帮助文档同步的接口抽象和增量同步任务骨架。
- HTML 清洗、图片 URL 抽取、OCR/caption 占位、语义分片。
- 混合检索服务：关键词分数 + 向量相似度 + rerank 简化实现。
- 自动回复策略：高置信自动答，中低置信转人工。
- 微信机器人 Adapter 层：业务逻辑不依赖具体微信 SDK。
- WorkTool QA 回调接口：按 Apifox 文档接收 `spoken/rawSpoken/groupName/messageId` 等字段，并按 `code/message/data.info.text` 同步返回答案。
- WorkTool 主动发送接口：按 `sendRawMessage?robotId=...`、`socketType:2`、`type:203/218` 批量发送群文本和图片。
- 客户群问答日志、待审核知识池、审核通过后入正式知识库。
- FastAPI 接口、PostgreSQL + pgvector 初始化脚本、Docker Compose。
- 单元测试覆盖 ingestion、retrieval、answer policy、review loop、webhook flow。

## 本地运行

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
uvicorn ragbot.main:app --reload
```

接口文档：

```text
http://127.0.0.1:8000/docs
```

运行测试：

```powershell
pytest
```

## 数据库

启动 PostgreSQL + pgvector：

```powershell
docker compose up -d postgres
```

初始化脚本位于 `db/init/001_schema.sql`。本项目支持两种仓库：

```text
REPOSITORY_PROVIDER=memory    # 本地快速测试
REPOSITORY_PROVIDER=postgres  # 服务器持久化，使用 PostgreSQL + pgvector
```

服务器 MVP 使用 PostgreSQL + pgvector，embedding 维度默认 `64`，对应本地 `HashEmbeddingProvider`。切换真实 embedding API 时，必须同步调整 `db/init/001_schema.sql` 里的 `vector(N)` 维度。

## 生产对接点

- `ragbot.sources.mysql_source.MySQLHelpDocumentSource`：按实际帮助文档表字段实现 MySQL 拉取。
- `ragbot.providers.llm.HttpLLMProvider`：按国产大模型 API 协议调整请求和响应字段。
- `ragbot.adapters.wechat.HttpWechatBotAdapter`：已按 WorkTool `sendRawMessage` 主动发送接口实现。
- `ragbot.repositories.PostgresKnowledgeRepository`：PostgreSQL + pgvector 持久化仓库。

## 帮助中心导入

当前帮助中心导入读取这 5 张表：

```text
db/init/osp_helpcenter_cate.xls
db/init/osp_helpcenter_art.xls
db/init/osp_helpcenter_artsubhead.xls
db/init/osp_helpcenter_artsubinc.xls
db/init/osp_helpcenter_kws.xls
```

表关系：

```text
cate.id -> art.cateid
art.id -> artsubhead.artid
artsubhead.id -> artsubinc.headid
art.id -> kws.artid
```

初始化数据库：

```bash
python -m ragbot.cli init-db --schema db/init/001_schema.sql
```

全量重建知识索引：

```bash
python -m ragbot.cli rebuild-index --source db/init
```

增量/追加导入：

```bash
python -m ragbot.cli import-helpcenter --source db/init
```

服务器当前导入规模：

```text
documents: 141
chunks: 171
image_refs: 1297
```

## 运维命令

服务器服务：

```bash
sudo systemctl status worktool-rag --no-pager
sudo systemctl restart worktool-rag
sudo journalctl -u worktool-rag -f
```

数据库检查：

```bash
PGPASSWORD=rag psql -h 127.0.0.1 -U rag -d rag
```

常用 SQL：

```sql
SELECT count(*) FROM help_documents;
SELECT count(*) FROM knowledge_chunks;
SELECT count(*) FROM conversation_logs;
SELECT count(*) FROM review_items WHERE status = 'pending';
```

## WorkTool 接入

QA 回调地址配置为：

```text
POST http://你的服务域名/worktool/qa
```

该接口会读取 WorkTool 回调中的 `spoken` 作为客户问题，优先使用 `groupRemark` 作为群标识，没有时回退到 `groupName`。高置信度时同步返回：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "type": 5000,
    "info": {
      "text": "根据帮助文档生成的回答"
    }
  }
}
```

中低置信度、敏感问题或无匹配知识时返回空文本，并进入人工审核池。

也可以通过接口配置 WorkTool 回调：

```text
POST /worktool/callback-config
```

请求体：

```json
{
  "callback_url": "http://你的服务域名/worktool/qa",
  "reply_all": 1,
  "open_callback": 1
}
```

需要在 `.env` 中配置：

```text
WORKTOOL_API_BASE=https://api.worktool.ymdyes.cn
WORKTOOL_ROBOT_ID=worktool1
```

转人工配置：

```env
HUMAN_HANDOFF_ENABLED=true
HUMAN_HANDOFF_MENTION_NAME=校校助理
HUMAN_HANDOFF_MESSAGE_PREFIX=稍等老师，这个问题 @{mention} 帮您看下，尽快回复您。
HANDOFF_RULES_PATH=config/handoff_rules.json
```

当问题命中敏感规则、低置信度、或只有草稿但不允许自动回复时，机器人会主动发送：

```text
稍等老师，这个问题 @校校助理 帮您看下，尽快回复您。
```

转人工话术不会复述客户原问题；WorkTool 请求体会同时带上 `atList=["校校助理"]`，确保群内真正 @ 到人工账号。

质量规则配置：

```text
config/query_aliases.json          # 检索 query rewrite 同义词
config/handoff_rules.json          # 转人工关键词
config/fast_answer_templates.json  # 高频问题快速模板
```

新增同义词、转人工关键词或模板时优先改配置文件，再运行评测命令确认指标没有下降。

排查 WorkTool 链路时优先看这几个接口：

```text
GET /worktool/online
GET /worktool/qa-logs?size=10
GET /worktool/raw-messages?size=10
GET /worktool/raw-results?size=10
```

`qa-logs` 用来确认 WorkTool 是否真正回调了 `/worktool/qa`；`raw-messages` 和 `raw-results` 用来确认我们主动发送的文字/图片指令是否被安卓端执行成功。

## DeepSeek 模型

服务器可以使用 DeepSeek 的 OpenAI 兼容接口作为回答生成模型：

```env
LLM_PROVIDER=http
LLM_API_BASE=https://api.deepseek.com
LLM_API_KEY=你的DeepSeekKey
LLM_MODEL=deepseek-v4-flash
```

当前 WorkTool 回调是同步返回，建议优先使用 `deepseek-v4-flash` 控制延迟；如果更看重回答质量，可以改成 `deepseek-v4-pro`，但需要重点观察 `/worktool/qa` 是否能在 3 秒内返回。

embedding 当前仍使用本地 hash 方案：

```env
EMBEDDING_PROVIDER=hash
EMBEDDING_DIMENSIONS=64
```

如果后续切换真实 embedding API，需要同步修改 `db/init/001_schema.sql` 中的 `vector(N)` 维度，并执行：

```bash
python -m ragbot.cli init-db --schema db/init/001_schema.sql
python -m ragbot.cli rebuild-index --source db/init
```

## 图片回复

帮助中心图片会保存在 `knowledge_chunks.image_refs`。高置信度且命中图片时，服务会优先在 3 秒内结束 QA 回调，然后通过 WorkTool 批量指令把文字和图片一起投递到安卓端队列，避免同步回调超时。

相关配置：

```env
REPLY_IMAGES_ENABLED=true
MAX_REPLY_IMAGES=3
FAST_IMAGE_REPLY_ENABLED=true
FAST_IMAGE_ANSWER_CHARS=700
BATCH_IMAGE_REPLY_ENABLED=true
IMAGE_REPLY_DELAY_SECONDS=0
REPLY_IMAGE_CAPTIONS_ENABLED=false
```

实现方式：

```text
/worktool/qa 快速返回空文本，避免 WorkTool 3 秒超时
后台任务读取命中 chunk 的 image_refs
调用 WorkTool sendRawMessage，单次 list 中合并 type=203 文本和 type=218 图片
```

带图片的帮助文档通常上下文较长，等待大模型同步润色容易超过 WorkTool 回调时间。`FAST_IMAGE_REPLY_ENABLED=true` 时，高置信且命中图片的问题会优先返回知识库抽取答案，并批量发送文字和图片；无图片的问题仍走大模型润色。

如果图片发送失败，会尝试降级发送文字回答；可通过服务日志和 WorkTool 指令结果排查：

```bash
sudo journalctl -u worktool-rag -f
curl "http://你的服务域名/worktool/raw-results?size=10"
```

## 检索评测

评测集放在 `eval/questions.json`，用于持续检查 top1/top3 命中、自动回复和转人工决策。当前用例已覆盖 100+ 条真实/模拟问题，并支持 `module`、`expected_source_ids`、`requires_image` 字段：

```bash
python -m ragbot.cli eval-retrieval --cases eval/questions.json
```

五类物理知识库路由的建表、重建、评测和线上切换步骤见 `docs/audience_knowledge_routing.md`。

本地内存模式会自动从 `db/init` 导入帮助中心数据；服务器 PostgreSQL 模式默认使用库内已有知识。如果需要边导入边评测：

```bash
python -m ragbot.cli eval-retrieval --cases eval/questions.json --load-source
```

运营质量报告：

```bash
python -m ragbot.cli quality-report --limit 200 --top 20
curl "http://你的服务域名/quality/report?limit=200&top=20"
```

报告会聚合低置信、转人工、无答案问题 Top 列表，用来决定下一批应该补文档、补 alias、补模板还是保持转人工。

## 核心流程

1. `KnowledgeSyncJob` 从 MySQL 增量拉取帮助文档。
2. `IngestionService` 清洗正文、抽图、生成 OCR/caption 占位文本、分片。
3. embedding 写入知识库。
4. 微信 webhook 收到群消息后调用 `WechatRagWorkflow`。
5. `RetrievalService` 混合召回并计算置信度。
6. `AnswerService` 对高置信问题生成客服化回复。
7. 中低置信问题进入人工处理。
8. 所有问答写入日志和待审核知识池。
9. 审核通过后形成正式知识条目并重新入库。
