# 五类物理知识库路由说明

## 目标

当前系统把帮助中心知识按使用角色拆成 5 个物理向量表：

- `knowledge_chunks_student`
- `knowledge_chunks_teacher`
- `knowledge_chunks_principal`
- `knowledge_chunks_academic`
- `knowledge_chunks_sales`

`help_documents` 仍然是共享文档主表。一篇帮助文档可以同时写入多个角色表，避免只分到一个库后漏召回。

## 路由流程

1. WorkTool 消息进入 `/worktool/qa`。
2. `AudienceRouter` 根据问题内容匹配 `config/audience_routing.json`。
3. 明确命中时只查 top1 角色库，例如“怎么新建班级”查 `academic`。
4. 多个角色分数接近时查 top2/top3 角色库，例如“学生怎么查看作业”查 `student` 和 `teacher`。
5. 无法判断角色时查 5 个库，并提高自动回复谨慎度。
6. 检索结果携带 `audience`，引用格式为 `audience|chunk_id`，图片也从最终命中的 audience chunk 回查。

## 配置

核心配置文件：

```text
config/audience_routing.json
```

环境变量：

```env
AUDIENCE_ROUTING_ENABLED=true
AUDIENCE_ROUTING_PATH=config/audience_routing.json
MAX_ROUTE_AUDIENCES=3
```

默认代码里 `AUDIENCE_ROUTING_ENABLED=false`，服务器需要在完成建表和导入后再打开。

## 初始化和重建

PostgreSQL 初始化 5 个物理表：

```bash
python -m ragbot.cli init-audience-indexes --dimensions 64
```

按帮助中心 5 张 xls 表重建五类索引：

```bash
python -m ragbot.cli rebuild-audience-index --source db/init
```

检查单个问题会路由到哪个库：

```bash
python -m ragbot.cli inspect-audience --question "怎么新建班级"
```

评测路由准确率：

```bash
python -m ragbot.cli eval-routing --cases eval/questions.json
```

评测五类库检索效果：

```bash
AUDIENCE_ROUTING_ENABLED=true python -m ragbot.cli eval-retrieval --cases eval/questions.json --load-source
```

## 当前本地验收结果

基于 `eval/questions.json` 的 123 条用例：

```text
routing top1_accuracy: 92.78%
routing covered_accuracy: 100%
retrieval top1_hit_rate: 92.24%
retrieval top3_hit_rate: 96.55%
auto_reply_accuracy: 85.37%
false_auto_reply_count: 0
```

这说明五类路由不会增加误答，但仍有部分低路由置信度问题会偏保守转人工，后续可以继续补关键词和 source override。

## 线上切换步骤

1. 部署代码和 `config/audience_routing.json`。
2. 保持 `AUDIENCE_ROUTING_ENABLED=false`，先执行：

```bash
python -m ragbot.cli init-audience-indexes --dimensions 64
python -m ragbot.cli rebuild-audience-index --source db/init
python -m ragbot.cli eval-routing --cases eval/questions.json
```

3. 确认五个表都有数据：

```sql
SELECT 'student' AS audience, count(*) FROM knowledge_chunks_student
UNION ALL SELECT 'teacher', count(*) FROM knowledge_chunks_teacher
UNION ALL SELECT 'principal', count(*) FROM knowledge_chunks_principal
UNION ALL SELECT 'academic', count(*) FROM knowledge_chunks_academic
UNION ALL SELECT 'sales', count(*) FROM knowledge_chunks_sales;
```

4. 修改 `.env`：

```env
AUDIENCE_ROUTING_ENABLED=true
AUDIENCE_ROUTING_PATH=config/audience_routing.json
MAX_ROUTE_AUDIENCES=3
```

5. 重启服务：

```bash
sudo systemctl restart worktool-rag
```

6. 用群消息抽测：

```text
@翁然 怎么新建班级
@翁然 老师怎么布置作业
@翁然 销售线索怎么跟进
@翁然 校长端怎么看运营数据
@翁然 家长端怎么绑定学生
```

## 排查

看最近对话的路由结果：

```bash
curl "http://127.0.0.1:8000/conversations?limit=10"
```

重点看：

- `routed_audiences`
- `routing_confidence`
- `routing_reason`
- `retrieved_chunk_ids`

如果问题走错库，优先改 `config/audience_routing.json` 的关键词或 `source_overrides`，再重建五类索引并重新跑评测。
