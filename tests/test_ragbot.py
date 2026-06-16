from ragbot.answering import AnswerService
from ragbot.adapters.wechat import HttpWechatBotAdapter
from ragbot.api_models import WorkToolQaCallbackIn, WorkToolQaResponse
from ragbot.audience import AudienceAssigner, AudienceRouter
from ragbot.cli import evaluate_retrieval_cases, evaluate_routing_cases
from ragbot.config import Settings
from ragbot.domain import (
    ConfidenceLevel,
    ConversationLog,
    HelpDocument,
    ImageRef,
    KnowledgeChunk,
    RetrievalHit,
    RetrievalResult,
    ReviewItem,
    ReviewStatus,
    WechatMessage,
)
from ragbot.fast_answer import build_fast_image_answer, has_fast_answer_template
from ragbot.ingestion import ImageTextExtractor, IngestionService
from ragbot.main import build_human_handoff_message
from ragbot.providers import HashEmbeddingProvider, HttpEmbeddingProvider, MockLLMProvider
from ragbot.quality_report import build_quality_report
from ragbot.repositories import InMemoryKnowledgeRepository
from ragbot.retrieval import RetrievalService
from ragbot.review import ReviewService
from ragbot.text_utils import normalize_customer_text
from ragbot.workflow import CapturingWechatBotAdapter, MessagePreprocessor, WechatRagWorkflow


class FakeImageExtractor(ImageTextExtractor):
    def extract_ocr_text(self, image_url: str) -> str | None:
        return "班级管理入口"

    def generate_caption(self, image_url: str, alt_text: str | None = None) -> str | None:
        return "班级管理页面截图"


def build_services(auto_reply_threshold: float = 0.45):
    settings = Settings(auto_reply_threshold=auto_reply_threshold, draft_only_threshold=0.25, top_k=3)
    repo = InMemoryKnowledgeRepository()
    embedding = HashEmbeddingProvider()
    ingestion = IngestionService(embedding, FakeImageExtractor())
    retrieval = RetrievalService(repo, embedding, settings)
    answering = AnswerService(MockLLMProvider())
    wechat = CapturingWechatBotAdapter()
    workflow = WechatRagWorkflow(repo, retrieval, answering, wechat)
    review = ReviewService(repo, ingestion)
    return repo, ingestion, retrieval, answering, wechat, workflow, review


def test_ingestion_extracts_image_text_and_metadata():
    _, ingestion, *_ = build_services()
    document = HelpDocument(
        source_id="help-1",
        title="如何创建班级",
        body_html='<h1>创建班级</h1><p>进入班级管理，点击新建班级。</p><img src="https://x/a.png" alt="新建班级按钮">',
        product_module="教务",
    )

    chunks = ingestion.ingest_document(document)

    assert len(chunks) == 1
    assert "进入班级管理" in chunks[0].content
    assert "图片 OCR：班级管理入口" in chunks[0].content
    assert chunks[0].image_refs[0].url == "https://x/a.png"
    assert chunks[0].metadata["product_module"] == "教务"


def test_retrieval_returns_high_confidence_for_matching_help_doc():
    repo, ingestion, retrieval, *_ = build_services(auto_reply_threshold=0.35)
    doc = HelpDocument(
        source_id="help-2",
        title="重置学生密码",
        body_html="<p>管理员进入学生管理，搜索学生，点击重置密码。</p>",
    )
    repo.upsert_chunks(ingestion.ingest_document(doc))

    result = retrieval.retrieve("学生忘记密码怎么重置")

    assert result.confidence == ConfidenceLevel.HIGH
    assert result.hits[0].chunk.title == "重置学生密码"


def test_low_confidence_does_not_auto_reply():
    repo, ingestion, retrieval, answering, *_ = build_services()
    doc = HelpDocument(source_id="help-3", title="导出课表", body_html="<p>在课表页面点击导出。</p>")
    repo.upsert_chunks(ingestion.ingest_document(doc))

    retrieval_result = retrieval.retrieve("合同报价怎么签")
    decision = answering.answer("合同报价怎么签", retrieval_result)

    assert decision.auto_reply is False
    assert decision.needs_human is True


def test_preprocessor_routes_sensitive_and_known_gap_questions_to_human():
    preprocessor = MessagePreprocessor()

    assert preprocessor.requires_human(
        WechatMessage(message_id="s1", group_id="g1", user_id="u1", content="订单退费怎么操作")
    )
    assert preprocessor.requires_human(
        WechatMessage(message_id="s2", group_id="g1", user_id="u1", content="家长端怎么绑定学生")
    )


def test_preprocessor_can_load_handoff_rules_from_config(tmp_path):
    rules_path = tmp_path / "handoff_rules.json"
    rules_path.write_text('{"patterns": ["特殊人工"]}', encoding="utf-8")
    preprocessor = MessagePreprocessor(rules_path=str(rules_path))

    assert preprocessor.requires_human(
        WechatMessage(message_id="s3", group_id="g1", user_id="u1", content="这个要特殊人工处理")
    )
    assert not preprocessor.requires_human(
        WechatMessage(message_id="s4", group_id="g1", user_id="u1", content="订单退费怎么操作")
    )


def test_retrieval_can_load_query_aliases_from_config(tmp_path):
    aliases_path = tmp_path / "query_aliases.json"
    aliases_path.write_text('{"续班": "报课功能 报课 学员课程"}', encoding="utf-8")
    settings = Settings(
        auto_reply_threshold=0.35,
        draft_only_threshold=0.25,
        top_k=3,
        query_aliases_path=str(aliases_path),
    )
    repo = InMemoryKnowledgeRepository()
    embedding = HashEmbeddingProvider()
    ingestion = IngestionService(embedding)
    retrieval = RetrievalService(repo, embedding, settings)
    doc = HelpDocument(
        source_id="help-alias",
        title="一文了解：如何使用报课功能",
        body_html="<p>进入报课功能，为学员添加课程并保存。</p>",
    )
    repo.upsert_chunks(ingestion.ingest_document(doc))

    result = retrieval.retrieve("学员续班怎么处理")

    assert result.hits[0].chunk.title == "一文了解：如何使用报课功能"


def test_answer_service_compacts_image_heavy_context():
    service = AnswerService(MockLLMProvider(), max_context_chars=80)

    contexts = service._compact_contexts(
        [
            "标题\n正文第一段。" + "[图片: 创建班级]" * 20 + "\n图片说明：创建班级截图\n后续内容",
            "第二段内容" * 50,
        ]
    )

    assert contexts
    assert "[图片:" not in contexts[0]
    assert "图片说明" not in contexts[0]
    assert sum(len(context) for context in contexts) <= 80


def test_wechat_workflow_auto_replies_and_creates_review_item():
    repo, ingestion, _, _, wechat, workflow, _ = build_services(auto_reply_threshold=0.35)
    doc = HelpDocument(
        source_id="help-4",
        title="创建班级",
        body_html="<p>进入班级管理，点击新建班级，填写名称后保存。</p>",
    )
    repo.upsert_chunks(ingestion.ingest_document(doc))

    log = workflow.handle_message(
        WechatMessage(message_id="m1", group_id="g1", user_id="u1", content="怎么新建班级")
    )

    assert log is not None
    assert log.auto_replied is True
    assert len(wechat.sent_messages) == 1
    assert repo.list_review_items()[0].question == "怎么新建班级"


def test_review_approval_adds_new_knowledge_chunk():
    repo, ingestion, _, _, _, workflow, review = build_services(auto_reply_threshold=0.99)
    workflow.handle_message(
        WechatMessage(message_id="m2", group_id="g1", user_id="u1", content="家长端如何绑定学生")
    )
    item = repo.list_review_items()[0]

    approved = review.approve(item.id, reviewer_id="admin", answer="家长端打开我的学生，输入学生邀请码完成绑定。")

    assert approved.status == ReviewStatus.APPROVED
    assert any("学生邀请码" in chunk.content for chunk in repo.list_active_chunks())


def test_review_approval_adds_audience_knowledge_when_enabled():
    repo = InMemoryKnowledgeRepository()
    embedding = HashEmbeddingProvider()
    ingestion = IngestionService(embedding)
    review = ReviewService(repo, ingestion, AudienceAssigner(), audience_routing_enabled=True)
    item = ReviewItem("conv-audience", "怎么新建班级", None)
    repo.add_review_item(item)

    approved = review.approve(item.id, reviewer_id="admin", answer="进入班级管理，点击新建班级并保存。")

    settings = Settings(audience_routing_enabled=True, auto_reply_threshold=0.35, draft_only_threshold=0.25)
    retrieval = RetrievalService(repo, embedding, settings)
    result = retrieval.retrieve("怎么新建班级")

    assert approved.status == ReviewStatus.APPROVED
    assert result.routed_audiences == ["academic"]
    assert result.hits[0].audience == "academic"
    assert "进入班级管理" in result.hits[0].chunk.content


def test_worktool_callback_payload_maps_to_message():
    payload = WorkToolQaCallbackIn(
        spoken="怎么新建班级",
        rawSpoken="@机器人 怎么新建班级",
        receivedName="张老师",
        groupName="客户群A",
        groupRemark="VIP客户群",
        roomType=2,
        atMe="true",
        textType=1,
        messageId="worktool-msg-1",
    )

    message = payload.to_wechat_message()

    assert message.message_id == "worktool-msg-1"
    assert message.group_id == "VIP客户群"
    assert message.user_id == "张老师"
    assert message.content == "怎么新建班级"
    assert message.message_type == "text"


def test_worktool_callback_accepts_extra_message_id_alias():
    payload = WorkToolQaCallbackIn(
        spoken="hello",
        receivedName="user",
        groupName="group",
        msgId="worktool-extra-msg-1",
    )

    message = payload.to_wechat_message()

    assert message.message_id == "worktool-extra-msg-1"


def test_worktool_qa_response_uses_documented_text_type():
    response = WorkToolQaResponse.reply("hello")

    assert response.data.type == 5000
    assert response.data.info.text == "hello"


def test_worktool_callback_fallback_id_uses_optional_salt():
    payload = WorkToolQaCallbackIn(
        spoken="hello",
        rawSpoken="@bot hello",
        receivedName="user",
        groupName="group",
    )

    first = payload.to_wechat_message(fallback_salt="202606081554")
    duplicate = payload.to_wechat_message(fallback_salt="202606081554")
    later = payload.to_wechat_message(fallback_salt="202606081555")

    assert first.message_id == duplicate.message_id
    assert first.message_id != later.message_id


def test_worktool_callback_normalizes_leading_mention_and_special_spaces():
    payload = WorkToolQaCallbackIn(
        spoken="",
        rawSpoken="@xclass AI\u2005\u200b怎么新建班级\ufeff",
        receivedName="user",
        groupName="group",
    )

    message = payload.to_wechat_message(fallback_salt="202606081610")

    assert message.content == "怎么新建班级"
    assert normalize_customer_text("\u200b 怎么新建班级\ufeff") == "怎么新建班级"
    assert normalize_customer_text("@翁然班级创建好了为什么选不到老师") == "班级创建好了为什么选不到老师"


def test_fast_image_answer_uses_polished_class_creation_template():
    chunk = KnowledgeChunk(
        document_id="doc-class",
        title="一文读懂：如何进行班级管理",
        content=(
            "一文读懂：如何进行班级管理\n"
            "创建班级\n"
            "添加好课程后，可以在班级管理里创建班级\n"
            "[图片: 创建班级]\n"
            "添加班级：班级信息包括所属课程、班级类型、班级名称、班级老师助教、开班日期、班级课时等\n"
            "图片说明：创建班级"
        ),
        metadata={},
        image_refs=[ImageRef(url="https://example.com/class.png", caption="创建班级")],
    )
    retrieval = RetrievalResult(
        query="怎么新建班级",
        hits=[RetrievalHit(chunk, keyword_score=1.0, vector_score=1.0, rerank_score=0.9)],
        confidence=ConfidenceLevel.HIGH,
        confidence_score=0.9,
    )

    answer = build_fast_image_answer(retrieval)

    assert "进入左侧导航【班级】或【班级管理】" in answer
    assert "一对一班级" in answer
    assert "我把相关截图也发您，方便对照操作" in answer
    assert "图片说明" not in answer
    assert "根据帮助文档" not in answer


def test_fast_answer_templates_cover_common_medium_confidence_questions():
    assert has_fast_answer_template("怎么新建班级并把学生加进去") is True
    assert has_fast_answer_template("新建班级后怎么排课") is True
    assert has_fast_answer_template("班级创建好了为什么选不到老师") is True
    assert has_fast_answer_template("学员忘记密码怎么重置") is True
    assert has_fast_answer_template("家长端怎么绑定学生") is False


def test_fast_answer_prefers_class_schedule_template():
    chunk = KnowledgeChunk(
        document_id="doc-class",
        title="如何进行班级管理",
        content="班级创建好并完成分班后，可以给班级排课。排课方式有智能排课、传统排课、常用时间段排课。",
        metadata={},
        image_refs=[],
    )
    retrieval = RetrievalResult(
        query="新建班级后怎么排课",
        hits=[RetrievalHit(chunk, keyword_score=1.0, vector_score=1.0, rerank_score=0.55)],
        confidence=ConfidenceLevel.MEDIUM,
        confidence_score=0.55,
    )

    answer = build_fast_image_answer(retrieval)

    assert "进入班级里的排课入口" in answer
    assert "智能排课、传统排课或常用时间段排课" in answer


def test_worktool_callback_uses_sync_answer_without_async_send():
    repo, ingestion, _, _, wechat, workflow, _ = build_services(auto_reply_threshold=0.35)
    doc = HelpDocument(
        source_id="help-5",
        title="新建班级",
        body_html="<p>进入班级管理，点击新建班级，填写名称后保存。</p>",
    )
    repo.upsert_chunks(ingestion.ingest_document(doc))
    payload = WorkToolQaCallbackIn(
        spoken="怎么新建班级",
        receivedName="张老师",
        groupName="客户群A",
        textType=1,
        messageId="worktool-msg-2",
    )

    log = workflow.handle_message(payload.to_wechat_message(), send_auto_reply=False)

    assert log is not None
    assert log.auto_replied is True
    assert log.final_answer is not None
    assert wechat.sent_messages == []


def test_worktool_send_raw_message_request_shape(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"code": 0, "message": "success"}

    def fake_post(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.adapters.wechat.httpx.post", fake_post)
    adapter = HttpWechatBotAdapter("https://api.worktool.ymdyes.cn", "worktool1")

    adapter.send_group_message("客户群A", "请进入班级管理新建班级。")

    assert captured["url"] == "https://api.worktool.ymdyes.cn/wework/sendRawMessage"
    assert captured["params"] == {"robotId": "worktool1"}
    assert captured["json"]["socketType"] == 2
    assert captured["json"]["list"][0]["type"] == 203
    assert captured["json"]["list"][0]["titleList"] == ["客户群A"]
    assert captured["json"]["list"][0]["receivedContent"] == "请进入班级管理新建班级。"


def test_worktool_send_group_message_supports_at_list(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"code": 0, "message": "success"}

    def fake_post(url, **kwargs):
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.adapters.wechat.httpx.post", fake_post)
    adapter = HttpWechatBotAdapter("https://api.worktool.ymdyes.cn", "worktool1")

    adapter.send_group_message("客户群A", "@校校助理 请协助处理", at_list=["校校助理"])

    item = captured["json"]["list"][0]
    assert item["type"] == 203
    assert item["receivedContent"] == "@校校助理 请协助处理"
    assert item["atList"] == ["校校助理"]


def test_human_handoff_message_uses_fixed_phrase_without_question():
    message = build_human_handoff_message(
        "家长端怎么绑定学生",
        "校校助理",
        "稍等老师，这个问题 @{mention} 帮您看下，尽快回复您。",
    )

    assert message == "稍等老师，这个问题 @校校助理 帮您看下，尽快回复您。"
    assert "家长端怎么绑定学生" not in message


def test_eval_retrieval_cases_reports_hit_and_handoff_metrics():
    repo, ingestion, retrieval, *_ = build_services(auto_reply_threshold=0.35)
    doc = HelpDocument(
        source_id="help-eval",
        title="一文读懂：如何进行班级管理",
        body_html="<p>进入班级管理，点击创建班级，填写班级名称并保存。</p>",
    )
    repo.upsert_chunks(ingestion.ingest_document(doc))

    report = evaluate_retrieval_cases(
        [
            {
                "id": "class_create",
                "question": "怎么新建班级",
                "expected_keywords": ["班级管理"],
                "should_auto_reply": True,
                "should_handoff": False,
            },
            {
                "id": "unknown",
                "question": "校区停车位怎么申请",
                "expected_keywords": [],
                "should_auto_reply": False,
                "should_handoff": True,
            },
        ],
        retrieval,
    )

    assert report["total"] == 2
    assert report["top3_hit_rate"] >= 0.5
    assert "details" in report


def test_quality_report_groups_low_confidence_handoff_and_no_answer():
    logs = [
        ConversationLog(
            group_id="g1",
            user_id="u1",
            message_id="q1",
            question="校区停车位怎么申请",
            confidence=ConfidenceLevel.LOW,
            confidence_score=0.1,
            retrieved_chunk_ids=[],
            draft_answer=None,
            final_answer=None,
            auto_replied=False,
            needs_human=True,
        ),
        ConversationLog(
            group_id="g1",
            user_id="u2",
            message_id="q2",
            question="校区停车位怎么申请",
            confidence=ConfidenceLevel.LOW,
            confidence_score=0.2,
            retrieved_chunk_ids=[],
            draft_answer=None,
            final_answer=None,
            auto_replied=False,
            needs_human=True,
        ),
        ConversationLog(
            group_id="g1",
            user_id="u3",
            message_id="q3",
            question="怎么新建班级",
            confidence=ConfidenceLevel.HIGH,
            confidence_score=0.9,
            retrieved_chunk_ids=["chunk-1"],
            draft_answer="answer",
            final_answer="answer",
            auto_replied=True,
            needs_human=False,
        ),
    ]

    report = build_quality_report(logs, limit=5)

    assert report["low_confidence_count"] == 2
    assert report["handoff_count"] == 2
    assert report["no_answer_top"][0]["question"] == "校区停车位怎么申请"
    assert report["no_answer_top"][0]["count"] == 2


def test_collect_reply_images_dedupes_and_limits():
    repo, ingestion, _, _, _, workflow, _ = build_services(auto_reply_threshold=0.35)
    doc = HelpDocument(
        source_id="help-images",
        title="create class",
        body_html=(
            '<p>Open class management and create class.</p>'
            '<img src="https://example.com/a.png" alt="first">'
            '<img src="https://example.com/a.png" alt="duplicate">'
            '<img src="https://example.com/b.png" alt="second">'
        ),
    )
    repo.upsert_chunks(ingestion.ingest_document(doc))

    log = workflow.handle_message(
        WechatMessage(message_id="img-1", group_id="group", user_id="user", content="create class")
    )
    images = workflow.collect_reply_images(log, limit=1)

    assert log is not None
    assert len(images) == 1
    assert images[0].url == "https://example.com/a.png"


def test_worktool_send_image_request_shape(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"code": 200, "message": "success"}

    def fake_post(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.adapters.wechat.httpx.post", fake_post)
    adapter = HttpWechatBotAdapter("https://api.worktool.ymdyes.cn", "worktool1")

    adapter.send_group_image("客户群A", "https://example.com/path/create-class.png", "创建班级")

    item = captured["json"]["list"][0]
    assert captured["url"] == "https://api.worktool.ymdyes.cn/wework/sendRawMessage"
    assert captured["params"] == {"robotId": "worktool1"}
    assert captured["json"]["socketType"] == 2
    assert item["type"] == 218
    assert item["titleList"] == ["客户群A"]
    assert item["fileUrl"] == "https://example.com/path/create-class.png"
    assert item["objectName"] == "create-class.png"
    assert item["fileType"] == "image"
    assert item["extraText"] == "创建班级"


def test_worktool_send_rich_message_batches_text_then_images(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"code": 200, "message": "success"}

    def fake_post(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.adapters.wechat.httpx.post", fake_post)
    adapter = HttpWechatBotAdapter("https://api.worktool.ymdyes.cn", "worktool1")

    adapter.send_group_rich_message("group", "answer text", ["https://example.com/a.png"])

    items = captured["json"]["list"]
    assert captured["url"] == "https://api.worktool.ymdyes.cn/wework/sendRawMessage"
    assert items[0]["type"] == 203
    assert items[0]["receivedContent"] == "answer text"
    assert items[1]["type"] == 218
    assert items[1]["fileUrl"] == "https://example.com/a.png"
    assert "extraText" not in items[1]


def test_worktool_raw_result_query_request_shape(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"code": 200, "message": "success", "data": []}

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.adapters.wechat.httpx.get", fake_get)
    adapter = HttpWechatBotAdapter("https://api.worktool.ymdyes.cn", "worktool1")

    result = adapter.list_raw_results(message_id="msg-1", raw_type="203", size=5)

    assert result["code"] == 200
    assert captured["url"] == "https://api.worktool.ymdyes.cn/robot/rawMsg/list"
    assert captured["params"] == {
        "robotId": "worktool1",
        "messageId": "msg-1",
        "page": 1,
        "size": 5,
        "sort": "run_time,desc",
        "type": "203",
    }


def test_worktool_send_image_adds_default_extension(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"code": 200, "message": "success"}

    def fake_post(url, **kwargs):
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.adapters.wechat.httpx.post", fake_post)
    adapter = HttpWechatBotAdapter("https://api.worktool.ymdyes.cn", "worktool1")

    adapter.send_group_image("客户群A", "https://example.com/path/oss-object-key", "截图")

    assert captured["json"]["list"][0]["objectName"] == "oss-object-key.jpg"


def test_http_embedding_provider_sends_dimensions(monkeypatch):
    captured = {}

    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {"data": [{"embedding": [0.1, 0.2, 0.3]}]}

    def fake_post(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return FakeResponse()

    monkeypatch.setattr("ragbot.providers.httpx.post", fake_post)
    provider = HttpEmbeddingProvider(
        "https://example.com/compatible-mode/v1",
        "test-key",
        "text-embedding-v4",
        dimensions=1024,
    )

    vector = provider.embed("test question")

    assert vector == [0.1, 0.2, 0.3]
    assert captured["url"] == "https://example.com/compatible-mode/v1/embeddings"
    assert captured["headers"]["Authorization"] == "Bearer test-key"
    assert captured["json"] == {
        "model": "text-embedding-v4",
        "input": "test question",
        "dimensions": 1024,
        "encoding_format": "float",
    }


def test_audience_router_routes_common_role_questions():
    router = AudienceRouter()

    assert router.route("怎么新建班级").audiences == ["academic"]
    assert router.route("老师怎么布置作业").audiences == ["teacher"]
    assert router.route("销售线索怎么跟进").audiences == ["sales"]
    assert router.route("校长端怎么看运营数据").audiences == ["principal"]

    mixed = router.route("学生怎么查看作业")
    assert "student" in mixed.audiences
    assert "teacher" in mixed.audiences


def test_audience_assigner_supports_multi_assignment_and_source_override(tmp_path):
    config_path = tmp_path / "audience.json"
    config_path.write_text(
        """
        {
          "default_audiences": ["student"],
          "audiences": {
            "student": {"keywords": ["学生"], "routing_keywords": ["学生"]},
            "teacher": {"keywords": ["老师", "作业"], "routing_keywords": ["老师", "作业"]},
            "principal": {"keywords": ["校长"], "routing_keywords": ["校长"]},
            "academic": {"keywords": ["班级"], "routing_keywords": ["班级"]},
            "sales": {"keywords": ["销售"], "routing_keywords": ["销售"]}
          },
          "source_overrides": {"override-doc": ["sales"]}
        }
        """,
        encoding="utf-8",
    )
    assigner = AudienceAssigner(str(config_path))

    multi = assigner.assign_document(
        HelpDocument(source_id="normal-doc", title="老师给学生布置作业", body_html="<p>作业说明</p>")
    )
    override = assigner.assign_document(
        HelpDocument(source_id="override-doc", title="老师给学生布置作业", body_html="<p>作业说明</p>")
    )

    assert multi == ["student", "teacher"]
    assert override == ["sales"]


def test_routed_retrieval_uses_audience_chunk_references():
    settings = Settings(
        audience_routing_enabled=True,
        auto_reply_threshold=0.35,
        draft_only_threshold=0.25,
        top_k=3,
    )
    repo = InMemoryKnowledgeRepository()
    embedding = HashEmbeddingProvider()
    ingestion = IngestionService(embedding)
    retrieval = RetrievalService(repo, embedding, settings)
    doc = HelpDocument(
        source_id="help-audience-class",
        title="如何新建班级",
        body_html="<p>进入班级管理，点击新建班级并保存。</p>",
    )
    chunks = ingestion.ingest_document(doc)
    repo.upsert_audience_chunks("academic", chunks)

    result = retrieval.retrieve("怎么新建班级")
    decision = AnswerService(MockLLMProvider()).answer("怎么新建班级", result)

    assert result.routed_audiences == ["academic"]
    assert result.hits[0].audience == "academic"
    assert decision.cited_chunk_ids[0] == f"academic|{chunks[0].id}"
    assert repo.get_chunk(decision.cited_chunk_ids[0]).title == "如何新建班级"


def test_eval_routing_cases_reports_accuracy():
    report = evaluate_routing_cases(
        [
            {"id": "class", "question": "怎么新建班级", "expected_audiences": ["academic"]},
            {"id": "sales", "question": "销售线索怎么跟进", "expected_audiences": ["sales"]},
        ],
        AudienceRouter(),
    )

    assert report["evaluated"] == 2
    assert report["top1_accuracy"] == 1.0


# ── handoff rules enhancement tests ──

def test_handoff_rules_loads_expanded_keywords():
    """New config includes explicit handoff, emotion, and sensitive patterns."""
    preprocessor = MessagePreprocessor()

    # L1: explicit handoff keywords (always trigger)
    assert preprocessor.requires_human(
        WechatMessage(message_id="h1", group_id="g1", user_id="u1", content="转人工")
    )
    assert preprocessor.requires_human(
        WechatMessage(message_id="h2", group_id="g1", user_id="u1", content="有真人吗")
    )

    # L2: emotion keywords (always trigger)
    assert preprocessor.requires_human(
        WechatMessage(message_id="h3", group_id="g1", user_id="u1", content="太慢了影响上课")
    )

    # L3: sensitive business patterns (trigger when not a safe query)
    assert preprocessor.requires_human(
        WechatMessage(message_id="h4", group_id="g1", user_id="u1", content="金额不对")
    )

    # Existing patterns still work
    assert preprocessor.requires_human(
        WechatMessage(message_id="h5", group_id="g1", user_id="u1", content="这个报价有问题")
    )


def test_mock_llm_uses_new_handoff_message():
    """MockLLMProvider returns the updated handoff message when no contexts."""
    provider = MockLLMProvider()

    answer = provider.generate_answer("合同金额不对", [])

    assert answer == "老师稍等，我们这边具体看下问题。"
    assert "@校校助理" not in answer


def test_llm_prompt_contains_prohibited_content_rules():
    """The LLM answer prompt includes the 10 prohibited content rules."""
    # Verify the prompt string embedded in HttpLLMProvider contains the rules
    from ragbot.providers import HttpLLMProvider

    provider = HttpLLMProvider(
        api_base="https://test.example.com",
        api_key="test-key",
        model="test-model",
    )
    # Access the prompt generated within generate_answer by calling with empty contexts
    # We can inspect the source directly since the prompt is constructed in the method
    import inspect

    source = inspect.getsource(provider.generate_answer)

    # Check prohibited content rules are present
    assert "严格禁止输出以下内容" in source
    assert "判断任何金额、费用、结算、退款金额是否正确" in source
    assert "判断课时扣减、课消是否正确" in source
    assert "承诺可以恢复、删除、修改数据" in source
    assert "引导用户绕过权限限制" in source
    assert "编造知识库中没有的功能或操作路径" in source
    assert "给出没有文档依据的原因判断或结论" in source
    assert "对客户内部规则、流程做主观评价" in source
    assert "对财务、合同、经营数据下任何结论" in source
