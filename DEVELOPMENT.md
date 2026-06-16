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
| P1-9 | 2026-06-15 | LLM 点对点重排序 (`feat/llm-rerank`) | ✅ |
| P1-10 | - | MMR 多样性 (`feat/mmr-diversity`) | ⬜ |
| P1-11 | 2026-06-15 | 意图分类 + 多意图分解 (`feat/intent-classify`) | ✅ |
| P1-13 | - | 上下文窗口智能组装 (`feat/context-window`) | ⬜ |
| P1-14 | - | 图片发送意图感知 (`feat/image-intent`) | ⬜ |
| P1-17 | - | 回答质量评估 (`feat/eval-judge`) | ⬜ |
| — | 2026-06-16 | 意图驱动转人工检测 (`feat/handoff-intent`) | ✅ |
| — | 2026-06-16 | Fast Answer 模板关闭（生产） | ✅ |

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
当前生产 (2026-06-16, commit 7bce0bd):
  src/ragbot/intent.py       ← (新建) IntentClassifier + 意图+转人工 Prompt
  src/ragbot/providers.py    ← HttpLLMProvider (rewrite/classify) + HttpRerankProvider
  src/ragbot/retrieval.py    ← 意图分类 + 多意图分解 + LLM 重排 + Jieba 分词
  src/ragbot/repositories.py ← HNSW 索引 + BM25 + list_recent_user_conversations
  src/ragbot/config.py       ← 全部 P1 配置项
  src/ragbot/container.py    ← 全部 Provider 注入
  src/ragbot/domain.py       ← RetrievalHit(LLM_score) + RetrievalResult(intent/handoff)
  src/ragbot/main.py         ← API 响应(intent/handoff) + 转人工判定 + _count_same_topic
  src/ragbot/workflow.py     ← intent_result 透传
  src/ragbot/fast_answer.py  ← 增强去重正则 + Jieba 分词
  src/ragbot/answering.py    ← 上下文使用 answer_content
  src/ragbot/ingestion.py    ← embedding 使用 search_text
  src/ragbot/cli.py          ← eval-full + baseline + migrate-index-type
  eval/baseline.json         ← 评估基线 (top1=95.69%, auto_reply=98.37%)
```

---

### 2026-06-15 — Fast Answer 去重修复增强

**问题**: `feat/intent-classify` 合并到 master 时，DEVELOPMENT.md 冲突导致去重修复(`fd7abd0`)被回退。
同时正则未覆盖全角括号`（1）`、半角括号`(1)`、圈号`①`、字母序号`a.`等。

**修复**:
- 恢复并增强 `_select_relevant_snippets()` 的去重正则：
  `r"^(?:[(（]?\d+[)）.]?\s*|[①②③④⑤⑥⑦⑧⑨⑩]+\s*|[a-z][.)]\s*)+"`
- 覆盖：`1）`, `4. 1）`, `（1）`, `(1)`, `①`, `a.`, `1.` 等序号格式
- 合并回退修复：commit `867c493`

**涉及文件**: `src/ragbot/fast_answer.py`

---

### 2026-06-15 — LLM 点对点重排序 (P1-9, ColdAir-Hao)

**目标**: 使用 qwen3-rerank API 对检索候选做点对点语义重排序，提升 top-3 精度。

**方案** (同学 ColdAir-Hao 提交):
1. **`providers.py`**: `HttpRerankProvider` — 调用 DashScope `/compatible-api/v1/reranks`
2. **`retrieval.py`**: `_llm_rerank()` tiebreak fusion 策略：
   - 主排序：LLM relevance_score 降序
   - 平局区（相邻分数差 < 0.01）：规则 `rerank_score` 重排
   - 最终 `rerank_score` 覆盖为 LLM 分，影响下游置信度
3. **`config.py`**: `llm_rerank_enabled` / `llm_rerank_provider` / `llm_rerank_model`
4. **`container.py`**: 注入 `HttpRerankProvider`
5. **`domain.py`**: `RetrievalHit` 新增 `llm_score` 字段

**集成要点**:
- 重排池扩大至 15 候选项（`rerank_pool_size`），多意图先合并再重排
- 默认关闭 (`llm_rerank_provider=mock`)，失败静默回退

**启用方式** (服务器 `.env`):
```env
LLM_RERANK_ENABLED=true
LLM_RERANK_PROVIDER=http
LLM_RERANK_MODEL=qwen3-rerank
LLM_RERANK_API_BASE=https://dashscope.aliyuncs.com
LLM_RERANK_API_KEY=<DashScope API Key>
```

**涉及文件**:
- `src/ragbot/providers.py` — HttpRerankProvider
- `src/ragbot/retrieval.py` — _llm_rerank()
- `src/ragbot/config.py` — llm_rerank_* 配置
- `src/ragbot/container.py` — 注入
- `src/ragbot/domain.py` — RetrievalHit.llm_score

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

### 2026-06-16 — 意图驱动转人工检测 (ColdAir-Hao, `feat/handoff-intent`)

**目标**: 在意图分类的同一 LLM 调用中自动识别需要转人工的场景，避免机器人处理敏感业务（财务/课时）或激怒已不满的用户。

**方案**:
1. **扩展 `intent.py` 分类 Prompt** — 同一 LLM 调用新增 `needs_handoff` / `handoff_type` / `handoff_confidence` 输出：
   - `force`: 用户明确要求找人工（"有真人吗""转人工""叫客服出来"等）
   - `sensitive`: 涉及财务/课时/权限等敏感操作（合同、退款、扣课时、删除、修改课消等）
   - `negative`: 表达不满或催促（"怎么又不行""还是不行""投诉""着急"等）
2. **`domain.py`**: `RetrievalResult` +3 字段 (`needs_handoff`, `handoff_type`, `handoff_confidence`)
3. **`retrieval.py`**: 新增 `classify_intent()` 公开方法，`retrieve()` 接受可选 `intent_result` 参数防止二次 LLM 调用
4. **`main.py`**: 转人工判定逻辑：
   - `force` / `sensitive` → 立即转人工，跳过 RAG 检索
   - `negative` → 检查同用户近 3 轮对话历史：
     - 短文本(<10字) → 转人工（隐式针对上次 AI 回复）
     - 长文本 → `_count_same_topic()` Jieba+Jaccard 同话题检测 (≥2轮 → 转人工)
5. **`repositories.py`**: 新增 `list_recent_user_conversations()` (内存 + PostgreSQL 双实现)
6. **`workflow.py`**: `handle_message()` 透传 `intent_result`
7. **`main.py` API 响应**: 暴露 `needs_handoff` / `handoff_type` / `handoff_confidence` 字段

**转人工判定流程**:
```
LLM 分类 → needs_handoff?
  ├─ force    → 立即转人工
  ├─ sensitive → 立即转人工
  ├─ negative → 查历史 →
  │     ├─ 短文本(<10字) → 转人工
  │     └─ 长文本 → Jaccard同话题≥2轮 → 转人工
  └─ false → 正常 RAG 流程
```

**涉及文件**:
- `src/ragbot/intent.py` — 扩展 Prompt + IntentResult 字段 + 解析
- `src/ragbot/domain.py` — RetrievalResult 新增 handoff 字段
- `src/ragbot/retrieval.py` — classify_intent() 公开 + intent_result 参数
- `src/ragbot/repositories.py` — list_recent_user_conversations()
- `src/ragbot/main.py` — 转人工判定 + _count_same_topic() + API 响应
- `src/ragbot/workflow.py` — intent_result 透传

**验收**:
- "课时扣错了能改吗" → `needs_handoff: true, handoff_type: sensitive, confidence: 0.92`
- "能找个活人过来吗" → `needs_handoff: true, handoff_type: force, confidence: 0.95`
- "怎么创建班级" → `needs_handoff: false, handoff_type: ""`

---

### 2026-06-16 — 生产环境配置上线

**服务器**: 139.196.6.90 (Alibaba Cloud ECS)
**部署方式**: paramiko SFTP 上传 tar → 解压 → pkill + nohup 重启

**当前启用的功能**:

| 功能 | 配置项 | 值 |
|------|--------|-----|
| LLM 回答 | `LLM_PROVIDER` | `http` (DeepSeek v4-flash) |
| 语义 Embedding | `EMBEDDING_PROVIDER` | `http` (DashScope text-embedding-v4, 1024维) |
| 受众路由 | `AUDIENCE_ROUTING_ENABLED` | `true` |
| 意图分类 | `INTENT_CLASSIFY_ENABLED` | `true` (qwen-turbo) |
| 多意图分解 | `MULTI_INTENT_DECOMPOSE_ENABLED` | `true` |
| LLM 重排序 | `LLM_RERANK_ENABLED` | `true` (qwen3-rerank) |
| 转人工检测 | 随意图分类自动生效 | `true` |
| 图片回复 | `REPLY_IMAGES_ENABLED` | `true` |

**当前关闭的功能**:

| 功能 | 配置项 | 原因 |
|------|--------|------|
| Fast Answer 模板 | `FAST_IMAGE_REPLY_ENABLED=false` | 全部走 LLM 生成，避免重复拼接 |
| LLM 查询改写 | `LLM_QUERY_REWRITE_ENABLED=false` | 意图分类已含子查询改写 |

**部署历史** (最近 3 次):

| 时间 | Commit | 内容 |
|------|--------|------|
| 2026-06-16 18:25 | `7bce0bd` | handoff-intent 转人工检测 |
| 2026-06-16 18:20 | `867c493` | 同时启用 Intent Classify + Rerank，关闭 Fast Answer |
| 2026-06-16 18:15 | `867c493` | Fast Answer 去重增强 + Rerank 集成 |

---

## 评估基线演进

| 指标 | P0 (Hash) | P1 语义 | P1 +BM25+HNSW | P1 全功能(生产) |
|------|-----------|---------|---------------|-----------------|
| Top-1 命中率 | 93.10% | 96.55% | 95.69% | **95.69%** |
| Top-3 命中率 | 98.28% | 100.00% | 100.00% | **100.00%** |
| 自动回复准确率 | 93.50% | 97.56% | 98.37% | **98.37%** |
| 转人工准确率 | 93.50% | 97.56% | 98.37% | **98.37%** |
| 路由 Top-1 | 92.78% | 92.78% | 92.78% | **92.78%** |
| 路由覆盖 | 100.00% | 100.00% | 100.00% | **100.00%** |

> **生产新增能力**（不改变检索指标，改善回答质量和用户体验）：
> - 意图分类 (5 类) + 多意图分解 (复合问题拆 2-3 子查询)
> - LLM 语义重排序 (qwen3-rerank tiebreak fusion)
> - 意图驱动转人工 (force/sensitive/negative 三级)
> - Fast Answer 模板关闭 (全部走 LLM 生成)
> - 置信度提升: 多意图复合问题从 0.60 → 0.87 (+45%)
