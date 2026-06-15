# 开发进度记录

## 项目概述

教育 SaaS 领域 RAG 智能客服系统，通过 WorkTool 接入企业微信群自动回复客户问题。

- **技术栈**: FastAPI + PostgreSQL 16 + pgvector + DeepSeek v4-flash + DashScope text-embedding-v4
- **仓库**: `github.com/shelbype/worktool`
- **服务器**: 阿里云 139.196.6.90（华东2上海，宝塔面板）
- **分支策略**: master(生产) ← develop(集成) ← feat/*(功能分支)

---

## 进度总览

| 阶段 | 日期 | 内容 | 状态 |
|------|------|------|------|
| P0-1 | 2026-06-11 | search_text/answer_content 拆分 | ✅ |
| P0-2 | 2026-06-15 | 语义 Embedding (text-embedding-v4, 1024维) | ✅ |
| P0-3 | 2026-06-11 | Embedding LRU 缓存 | ✅ |
| P0-4 | 2026-06-11 | Fast Answer 模板去重 | ✅ |
| P0-5 | 2026-06-11 | Prompt 优化 + few-shot | ✅ |
| P0-6 | 2026-06-11 | Eval baseline 体系 | ✅ |
| P1-7 | 2026-06-15 | LLM 查询改写 (`feat/llm-rewrite`) | ✅ |
| P1-8 | 2026-06-15 | Jieba 分词 + BM25 (`feat/pg-bm25`) | ✅ |
| P1-12 | 2026-06-15 | HNSW 索引 (`feat/hnsw-index`) | ✅ |
| P1-9 | - | LLM 点对点重排序 (`feat/llm-rerank`) | ⬜ |
| P1-10 | - | MMR 多样性 (`feat/mmr-diversity`) | ⬜ |
| P1-11 | 2026-06-15 | 意图分类 + 多意图分解 (`feat/intent-classify`) | ✅ |
| P1-13 | - | 上下文窗口智能组装 (`feat/context-window`) | ⬜ |
| P1-14 | - | 图片发送意图感知 (`feat/image-intent`) | ⬜ |
| P1-17 | - | 回答质量评估 (`feat/eval-judge`) | ⬜ |

---

## 详细记录

### 2026-06-11 — P0 基础优化

**背景**: 系统初版完成，66 条标准知识入库，Hash Embedding (64维) + Mock LLM 验证通过。

**变更**:

1. **search_text/answer_content 拆分** (核心修复)
   - **问题**: `build_chunk_content()` 将所有模板字段拼接为单一 `content`，导致 LLM 把"用户问法示例""意图关键词"当成回答内容
   - **方案**: 新增 `search_text`(检索用) 和 `answer_content`(LLM用) 两个字段，nullable fallback 到 `content`
   - **文件**: domain.py, import_standard_kb.py, 001_schema.sql, ingestion.py, answering.py, fast_answer.py, repositories.py, retrieval.py, cli.py (9个文件)

2. **Embedding LRU 缓存**: `HttpEmbeddingProvider.embed()` 添加 `@lru_cache(maxsize=500)`

3. **Fast Answer 模板去重**: 删除 fast_answer.py 中 18 个硬编码 Python 条件，全部由 JSON 管理

4. **Prompt 优化**: 移除无用的负面指令，新增 2 个 few-shot 示例

5. **Eval 基线体系**: 新增 `eval-full` 命令 + `eval/baseline.json`，支持回归检测(下降 >5% → exit 1)

**基线指标 (Hash 64维)**:
- top1_hit_rate: 0.931, top3_hit_rate: 0.983
- auto_reply_accuracy: 0.935, handoff_accuracy: 0.935
- routing_top1_accuracy: 0.928, routing_covered_accuracy: 1.0

---

### 2026-06-15 — 分支体系 + 语义 Embedding + LLM 改写

**分支体系建立**:
- 创建 `develop` 分支 + 10 个 `feat/*` 分支
- Remote 从 HTTPS 切换到 SSH（生成 ed25519 密钥）
- 分工: 用户(检索核心) / ColdAir-Hao(查询+回答)

**feat/real-embedding** (用户):
- API: 阿里云 DashScope `text-embedding-v4` 1024 维
- DB: `migrate-vector-dim --dimensions 1024` (ALTER COLUMN ... USING NULL)
- KB: 重导 66 条知识 × 5 角色库，453 张图片
- 服务器 `.env` 已配置 EMBEDDING_API_KEY

**新基线 (HTTP 1024维)**:
- top1_hit_rate: 0.9655 (+3.45%), top3_hit_rate: 1.0000 (+1.72%)
- auto_reply_accuracy: 0.9756 (+4.06%), handoff_accuracy: 0.9756 (+4.06%)

**feat/llm-rewrite** (ColdAir-Hao):
- `HttpLLMProvider.rewrite_query()`: 口语→检索关键词，5s超时，temperature=0.1
- `RetrievalService._rewrite_query()`: 静默 fallback，异常时返回原始 query
- 新增配置: `LLM_QUERY_REWRITE_ENABLED`, `LLM_QUERY_REWRITE_MODEL` 等
- 默认关闭 (`llm_query_rewrite_provider=mock`)

---

### 2026-06-15 — HNSW 索引

**目标**: pgvector HNSW 索引替代 IVFFlat，提升查询速度和精度

**当前状态**: IVFFlat (100 lists)，~170 chunks

**HNSW 参数**:
- m = 8 (<1000 向量够用，默认 16)
- ef_construction = 200 (构建精度)

**涉及文件**:
- `src/ragbot/repositories.py`: 索引创建 SQL + 搜索参数
- `src/ragbot/config.py`: 新增 `VECTOR_INDEX_TYPE` 配置项

---

## 协作规范

### Git 工作流
```bash
# 1. 开发
git checkout feat/<功能名>
# 编码 + 本地验证
python -m ragbot.cli eval-full --baseline eval/baseline.json

# 2. 推送提 PR
git push origin feat/<功能名>
# → GitHub 提 PR 到 develop

# 3. 集成
git checkout develop && git merge feat/<功能名>
python -m ragbot.cli eval-full --baseline eval/baseline.json  # 回归检测

# 4. 发布
git checkout master && git merge develop && git push origin master
# → 同步服务器 + 重启 uvicorn
```

### 服务器部署
```bash
# 同步代码
tar czf - <files> | ssh ... "cd /home/admin/worktool && tar xzf -"
# 重启服务
ssh ... "kill \$(ps aux | grep 'uvicorn ragbot' | grep -v grep | awk '{print \$2}') && \
         cd /home/admin/worktool && nohup .venv/bin/python -m uvicorn ragbot.main:app --host 0.0.0.0 --port 8000 &"
```

### 文件更改清单
```
P0 (已部署):
  db/init/001_schema.sql     ← 新增 search_text, answer_content
  scripts/import_standard_kb.py ← build_search_text/build_answer_content
  src/ragbot/domain.py       ← KnowledgeChunk 新增字段
  src/ragbot/ingestion.py    ← embedding 使用 search_text
  src/ragbot/answering.py    ← 上下文使用 answer_content
  src/ragbot/fast_answer.py  ← snippet 使用 answer_content, 模板去重
  src/ragbot/providers.py    ← embedding LRU 缓存, prompt 优化 + rewrite_query
  src/ragbot/repositories.py ← schema/upsert/select 适配新字段
  src/ragbot/retrieval.py    ← 关键词/加权使用 search_text + LLM rewrite
  src/ragbot/config.py       ← 新增 llm_query_rewrite_* 配置
  src/ragbot/container.py    ← 新增 query_rewrite_provider
  src/ragbot/cli.py          ← eval-full 命令 + baseline 对比
  eval/baseline.json         ← 评估基线

待实施:
  src/ragbot/repositories.py ← HNSW 索引替代 IVFFlat
  src/ragbot/config.py       ← VECTOR_INDEX_TYPE 配置
```

---

### 2026-06-15 — 意图分类 + 多意图分解

**目标**: 自动识别用户问题意图类型，检测复合多意图问题并分解为独立子查询分别检索，解决"同一个问题里问了多个不相关的事"导致召回分散的问题。

**背景/动机**:
- 真实用户问题 `"销售那边签了个新单，我想在教务系统里给这个学生排一对一的课，还要能看到这个学生的入学模考成绩"` 包含 3 个独立诉求，作为整体检索导致 recall 分散、回答模糊
- 无意图分类，无法针对不同意图类型（操作指引 vs 故障排查 vs 闲聊）调整检索策略

**实现方案**:
1. **新建 `src/ragbot/intent.py`** — `IntentClassifier` 类，单一 LLM 调用同时完成：
   - 意图分类: `operational` / `definitional` / `troubleshooting` / `policy` / `chitchat`
   - 多意图检测: `is_multi` 标志位
   - 子查询分解: 每个子查询以检索关键词短语形式输出
   - JSON 响应解析，处理 markdown 代码块包裹等格式问题
2. **`providers.py`**: `HttpLLMProvider.classify_intent()` 方法（temperature=0, max_tokens=300, 5s timeout）
3. **`config.py`**: 新增 `intent_classify_enabled` / `intent_classify_provider` / `intent_classify_model` / `multi_intent_decompose_enabled`
4. **`domain.py`**: `RetrievalResult` 新增 `intent` / `is_multi_intent` / `intent_sub_queries` / `intent_reasoning` 字段
5. **`retrieval.py`**: 重构检索流程
   - `_classify_intent()`: 调用意图分类器，返回 `IntentResult`
   - `_retrieve_hits()`: 提取"单次检索+打分"的纯函数，每个子查询独立检索
   - `_merge_multi_hits()`: 跨子查询合并去重（按 chunk.id 去重，保留最高分）
   - `retrieve()`: 编排分类→分解→检索→合并全流程
6. **`container.py`**: 创建 `IntentClassifier` 并注入 `RetrievalService`

**降级策略**:
- 默认关闭 (`intent_classify_enabled=False`)，不影响现有行为
- 分类失败 → 静默 fallback 到单意图模式（`IntentResult.single(query)`）
- 无 LLM provider → 同上 fallback
- `multi_intent_decompose_enabled=False` → 仍做意图分类但不分解

**涉及文件**:
- `src/ragbot/intent.py` (新建) — IntentClassifier + IntentResult + 分类 Prompt
- `src/ragbot/providers.py` — HttpLLMProvider.classify_intent()
- `src/ragbot/config.py` — intent_classify_* 配置
- `src/ragbot/domain.py` — RetrievalResult 新增意图字段
- `src/ragbot/retrieval.py` — 重构 retrieve() + 新增 3 个方法
- `src/ragbot/container.py` — 创建并注入 IntentClassifier

**验收标准**:
- 复合多意图问题能正确分解为独立子查询（如测试案例拆为 3 个子查询）
- 子查询检索结果合并后去重，无重复 chunk
- 分类失败不影响主流程
- 现有 eval baseline 全部通过（关闭状态下零回归）

---

## 评估基线演进

| 指标 | P0 (Hash 64dim) | P1 语义 (1024dim) | P1 BM25 + HNSW |
|------|-----------------|-------------------|----------------|
| Top-1 命中率 | 93.10% | 96.55% | **95.69%** |
| Top-3 命中率 | 98.28% | 100.00% | **100.00%** |
| 自动回复准确率 | 93.50% | 97.56% | **98.37%** |
| 转人工准确率 | 93.50% | 97.56% | **98.37%** |
| 路由 Top-1 | 92.78% | 92.78% | **92.78%** |
| 路由覆盖 | 100.00% | 100.00% | **100.00%** |
