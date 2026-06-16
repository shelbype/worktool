from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from time import perf_counter, sleep

import jieba

from fastapi import FastAPI, HTTPException, Query as FastAPIQuery

from ragbot.adapters.wechat import HttpWechatBotAdapter
from ragbot.api_models import (
    HelpDocumentIn,
    QueryIn,
    ReviewDecisionIn,
    WechatWebhookIn,
    WorkToolCallbackConfigIn,
    WorkToolQaCallbackIn,
    WorkToolQaResponse,
)
from ragbot.container import container
from ragbot.domain import ConfidenceLevel, ConversationLog, HelpDocument, ReviewItem, WechatMessage
from ragbot.fast_answer import build_fast_image_answer, has_fast_answer_template
from ragbot.quality_report import build_quality_report

app = FastAPI(title=container.settings.app_name)
logger = logging.getLogger("uvicorn.error")
image_reply_executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="image-reply")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/knowledge/documents")
def ingest_document(payload: HelpDocumentIn) -> dict[str, object]:
    document = HelpDocument(**payload.model_dump())
    chunks = container.ingestion_service.ingest_document(document)
    container.repository.upsert_chunks(chunks)
    return {"document_id": document.id, "chunk_count": len(chunks)}


@app.post("/rag/query")
def query(payload: QueryIn) -> dict[str, object]:
    retrieval = container.retrieval_service.retrieve(payload.question, payload.product_module, payload.audiences)
    decision = container.answer_service.answer(payload.question, retrieval)
    return {
        "answer": decision.answer,
        "confidence": decision.confidence,
        "confidence_score": decision.confidence_score,
        "auto_reply": decision.auto_reply,
        "needs_human": decision.needs_human,
        "cited_chunk_ids": decision.cited_chunk_ids,
        "routed_audiences": retrieval.routed_audiences,
        "routing_confidence": retrieval.routing_confidence,
        "routing_reason": retrieval.routing_reason,
        # Intent classification (P1-11)
        "intent": retrieval.intent,
        "is_multi_intent": retrieval.is_multi_intent,
        "intent_sub_queries": retrieval.intent_sub_queries,
        "intent_reasoning": retrieval.intent_reasoning,
        "needs_handoff": retrieval.needs_handoff,
        "handoff_type": retrieval.handoff_type,
        "handoff_confidence": retrieval.handoff_confidence,
    }


@app.post("/wechat/webhook")
def wechat_webhook(payload: WechatWebhookIn) -> dict[str, object]:
    message = WechatMessage(**payload.model_dump())
    log = container.workflow.handle_message(message)
    if log is None:
        return {"ignored": True}
    return {
        "conversation_id": log.id,
        "auto_replied": log.auto_replied,
        "needs_human": log.needs_human,
        "confidence": log.confidence,
        "confidence_score": log.confidence_score,
        "routed_audiences": log.routed_audiences,
        "routing_confidence": log.routing_confidence,
    }


@app.post("/worktool/qa", response_model=WorkToolQaResponse)
def worktool_qa_callback(payload: WorkToolQaCallbackIn) -> WorkToolQaResponse:
    started = perf_counter()
    fallback_salt = datetime.now().strftime("%Y%m%d%H%M")
    message = payload.to_wechat_message(fallback_salt=fallback_salt)
    provided_message_id = payload.provided_message_id()
    extra_keys = ",".join(sorted((payload.model_extra or {}).keys()))
    logger.info(
        "worktool qa received message_id=%s provided_message_id=%s group=%s user=%s at_me=%s text_type=%s "
        "question=%r extra_keys=%s",
        message.message_id,
        provided_message_id or "",
        message.group_id,
        message.user_id,
        payload.atMe,
        payload.textType,
        message.content[:80],
        extra_keys,
    )
    existing = container.repository.get_conversation_by_message_id(message.message_id)
    if existing is not None:
        if existing.auto_replied and existing.final_answer:
            if should_batch_image_reply(existing.retrieved_chunk_ids):
                log_worktool_response(message, "existing_batched_no_reply", started, len(existing.final_answer))
                return WorkToolQaResponse.no_reply()
            log_worktool_response(message, "existing_reply", started, len(existing.final_answer))
            return WorkToolQaResponse.reply(existing.final_answer)
        log_worktool_response(message, "existing_no_reply", started)
        return WorkToolQaResponse.no_reply()

    if container.workflow.preprocessor.should_ignore(message):
        log_worktool_response(message, "ignored", started)
        return WorkToolQaResponse.no_reply()
    if container.workflow.preprocessor.requires_human(message):
        log = container.workflow.handle_message(message, send_auto_reply=False)
        if log is not None:
            submit_human_handoff(payload.groupName or message.group_id, log, "sensitive_or_rule")
        log_worktool_response(message, "human_handoff", started)
        return WorkToolQaResponse.no_reply()

    # ---- Intent-based handoff detection (force / sensitive / negative) ----
    intent_result = container.retrieval_service.classify_intent(message.content)
    if intent_result.needs_handoff:
        handoff_reason = f"intent:{intent_result.handoff_type}"
        escalate = False
        if intent_result.handoff_type in ("force", "sensitive"):
            escalate = True
        elif intent_result.handoff_type == "negative":
            recent_logs = container.repository.list_recent_user_conversations(
                message.group_id, message.user_id, limit=3
            )
            ai_replied = [log for log in recent_logs if log.auto_replied]
            if ai_replied:
                # Condition A: short negative feedback — implicitly about the
                # previous AI reply regardless of token overlap.
                if len(message.content) < 10:
                    escalate = True
                    handoff_reason += "|short_negative"
                else:
                    # Condition B: same-topic tracking — the same problem has
                    # been asked across ≥ 2 AI-replied rounds.
                    same_topic = _count_same_topic(
                        message.content,
                        [log.question for log in ai_replied],
                        threshold=0.4,
                    )
                    if same_topic >= 2:
                        escalate = True
                        handoff_reason += f"|same_topic={same_topic}"
        if escalate:
            log = ConversationLog(
                group_id=message.group_id,
                user_id=message.user_id,
                message_id=message.message_id,
                question=message.content,
                confidence="low",
                confidence_score=0.0,
                retrieved_chunk_ids=[],
                draft_answer=None,
                final_answer=None,
                auto_replied=False,
                needs_human=True,
                routed_audiences=[],
                routing_confidence=None,
                routing_reason=None,
            )
            container.repository.save_conversation(log)
            container.repository.add_review_item(ReviewItem(log.id, message.content, None))
            submit_human_handoff(payload.groupName or message.group_id, log, handoff_reason)
            log_worktool_response(message, "handoff_intent", started)
            return WorkToolQaResponse.no_reply()

    if container.settings.fast_image_reply_enabled:
        retrieval = container.retrieval_service.retrieve(message.content, intent_result=intent_result)
        template_available = has_fast_answer_template(message.content)
        fast_reply_allowed = (
            retrieval.confidence == ConfidenceLevel.HIGH and (retrieval_has_images(retrieval) or template_available)
        ) or (retrieval.confidence == ConfidenceLevel.MEDIUM and template_available)
        if fast_reply_allowed:
            answer = build_fast_image_answer(retrieval, container.settings.fast_image_answer_chars)
            log = ConversationLog(
                group_id=message.group_id,
                user_id=message.user_id,
                message_id=message.message_id,
                question=message.content,
                confidence=retrieval.confidence,
                confidence_score=retrieval.confidence_score,
                retrieved_chunk_ids=[hit.chunk_reference for hit in retrieval.hits],
                draft_answer=answer,
                final_answer=answer,
                auto_replied=True,
                needs_human=False,
                routed_audiences=retrieval.routed_audiences,
                routing_confidence=retrieval.routing_confidence,
                routing_reason=retrieval.routing_reason,
            )
            container.repository.save_conversation(log)
            container.repository.add_review_item(ReviewItem(log.id, message.content, answer))
            send_target = payload.groupName or message.group_id
            if container.settings.reply_images_enabled and should_batch_image_reply(log.retrieved_chunk_ids):
                image_reply_executor.submit(send_batched_reply, send_target, log.message_id, log.retrieved_chunk_ids, answer)
                log_worktool_response(message, "fast_batch_reply", started, len(answer))
                return WorkToolQaResponse.no_reply()
            log_worktool_response(message, "fast_image_reply", started, len(answer))
            return WorkToolQaResponse.reply(answer)

    log = container.workflow.handle_message(message, send_auto_reply=False, intent_result=intent_result)
    if log is None or not log.auto_replied or not log.final_answer:
        if log is not None and log.needs_human:
            submit_human_handoff(payload.groupName or message.group_id, log, "low_confidence")
            log_worktool_response(message, "human_handoff", started)
        else:
            log_worktool_response(message, "no_reply", started)
        return WorkToolQaResponse.no_reply()
    if existing is None and container.settings.reply_images_enabled:
        send_target = payload.groupName or message.group_id
        if should_batch_image_reply(log.retrieved_chunk_ids):
            image_reply_executor.submit(send_batched_reply, send_target, log.message_id, log.retrieved_chunk_ids, log.final_answer)
            log_worktool_response(message, "llm_batch_reply", started, len(log.final_answer))
            return WorkToolQaResponse.no_reply()
        image_reply_executor.submit(send_reply_images, send_target, log.message_id, log.retrieved_chunk_ids)
    log_worktool_response(message, "llm_reply", started, len(log.final_answer))
    return WorkToolQaResponse.reply(log.final_answer)


def log_worktool_response(message: WechatMessage, mode: str, started: float, answer_len: int = 0) -> None:
    elapsed_ms = (perf_counter() - started) * 1000
    logger.info(
        "worktool qa completed mode=%s message_id=%s group=%s elapsed_ms=%.1f answer_len=%s",
        mode,
        message.message_id,
        message.group_id,
        elapsed_ms,
        answer_len,
    )


def retrieval_has_images(retrieval) -> bool:
    return any(hit.chunk.image_refs for hit in retrieval.hits)


def should_batch_image_reply(chunk_ids: list[str]) -> bool:
    if not container.settings.batch_image_reply_enabled or not container.settings.reply_images_enabled:
        return False
    if container.settings.max_reply_images <= 0:
        return False
    return bool(reply_image_urls(chunk_ids))


def reply_image_urls(chunk_ids: list[str]) -> list[str]:
    images: list[str] = []
    seen_urls: set[str] = set()
    for chunk_id in chunk_ids[:2]:
        chunk = container.repository.get_chunk(chunk_id)
        if chunk is None:
            continue
        for image in chunk.image_refs:
            if not image.url or image.url in seen_urls:
                continue
            seen_urls.add(image.url)
            images.append(image.url)
            if len(images) >= container.settings.max_reply_images:
                return images
    return images


def send_batched_reply(group_id: str, message_id: str, chunk_ids: list[str], answer: str) -> None:
    image_urls = reply_image_urls(chunk_ids)
    if not image_urls:
        send_fallback_text_reply(group_id, message_id, answer, "no_images")
        return
    logger.info(
        "worktool batch reply sending message_id=%s group=%s image_count=%s",
        message_id,
        group_id,
        len(image_urls),
    )
    send_rich = getattr(container.wechat_adapter, "send_group_rich_message", None)
    if send_rich is None:
        send_fallback_text_reply(group_id, message_id, answer, "rich_sender_missing")
        send_reply_images(group_id, message_id, chunk_ids)
        return
    try:
        result = send_rich(group_id, answer, image_urls)
        logger.info(
            "worktool batch reply sent message_id=%s group=%s image_count=%s worktool_response=%s",
            message_id,
            group_id,
            len(image_urls),
            summarize_worktool_response(result),
        )
    except Exception:
        logger.exception(
            "failed to send WorkTool batch reply; falling back to text",
            extra={"group_id": group_id, "message_id": message_id},
        )
        send_fallback_text_reply(group_id, message_id, answer, "batch_failed")


def send_fallback_text_reply(group_id: str, message_id: str, answer: str, reason: str) -> None:
    try:
        result = container.wechat_adapter.send_group_message(group_id, answer)
        logger.info(
            "worktool fallback text reply sent message_id=%s group=%s reason=%s worktool_response=%s",
            message_id,
            group_id,
            reason,
            summarize_worktool_response(result),
        )
    except Exception:
        logger.exception(
            "failed to send WorkTool fallback text reply",
            extra={"group_id": group_id, "message_id": message_id, "reason": reason},
        )


def submit_human_handoff(group_id: str, log: ConversationLog, reason: str) -> None:
    if not container.settings.human_handoff_enabled:
        return
    mention_name = container.settings.human_handoff_mention_name.strip()
    if not mention_name:
        return
    image_reply_executor.submit(send_human_handoff, group_id, log.message_id, log.question, reason)


def send_human_handoff(group_id: str, message_id: str, question: str, reason: str) -> None:
    mention_name = container.settings.human_handoff_mention_name.strip()
    content = build_human_handoff_message(
        question,
        mention_name,
        container.settings.human_handoff_message_prefix,
    )
    try:
        result = container.wechat_adapter.send_group_message(group_id, content, at_list=[mention_name])
        logger.info(
            "worktool human handoff sent message_id=%s group=%s reason=%s worktool_response=%s",
            message_id,
            group_id,
            reason,
            summarize_worktool_response(result),
        )
    except Exception:
        logger.exception(
            "failed to send WorkTool human handoff",
            extra={"group_id": group_id, "message_id": message_id, "reason": reason},
        )


# High-frequency tokens that carry no topic signal for same-topic detection.
_TOPIC_STOP_WORDS = frozenset(
    {
        "怎么", "如何", "什么", "为什么", "能不能", "可以", "应该",
        "的", "了", "吗", "呢", "吧", "啊", "呀", "是", "有", "在",
        "我", "你", "他", "她", "它", "我们", "你们", "这个", "那个",
        "不", "没", "很", "都", "就", "也", "还", "要", "会", "能",
        "一个", "一下", "搞", "弄", "做", "用", "让", "给", "把", "被",
        "请", "帮", "看", "说", "想", "知道",
    }
)


def _count_same_topic(current: str, history_queries: list[str], threshold: float = 0.4) -> int:
    """Count how many history queries share the same topic as *current*.

    Tokenises with Jieba, strips high-frequency function words, then
    computes Jaccard similarity.  A round counts as same-topic when the
    filtered token-set overlap is ≥ *threshold* (default 0.4).
    """
    curr_tokens = set(jieba.lcut(current)) - _TOPIC_STOP_WORDS
    count = 0
    for prev_q in history_queries:
        prev_tokens = set(jieba.lcut(prev_q)) - _TOPIC_STOP_WORDS
        denom = max(1, min(len(curr_tokens), len(prev_tokens)))
        if denom == 0:
            continue
        overlap = len(curr_tokens & prev_tokens) / denom
        if overlap >= threshold:
            count += 1
    return count


def build_human_handoff_message(question: str, mention_name: str, prefix: str) -> str:
    message = (prefix or "").strip()
    if "{mention}" in message:
        return message.replace("{mention}", mention_name)
    if f"@{mention_name}" in message:
        return message
    return f"@{mention_name} {message}" if message else f"@{mention_name} 稍等老师，这个问题我帮您转人工看下。"


def send_reply_images(group_id: str, message_id: str, chunk_ids: list[str]) -> None:
    log = container.repository.get_conversation_by_message_id(message_id)
    if log is None:
        logger.warning("conversation not found for image reply", extra={"message_id": message_id})
        return
    delay_seconds = container.settings.image_reply_delay_seconds
    if delay_seconds > 0:
        sleep(delay_seconds)
    images = container.workflow.collect_reply_images(log, container.settings.max_reply_images)
    logger.info(
        "worktool image reply sending message_id=%s group=%s count=%s delay_seconds=%.1f",
        message_id,
        group_id,
        len(images),
        delay_seconds,
    )
    for image in images:
        try:
            caption = (image.caption or image.alt_text) if container.settings.reply_image_captions_enabled else None
            result = container.wechat_adapter.send_group_image(group_id, image.url, caption)
            logger.info(
                "worktool image reply sent message_id=%s group=%s worktool_response=%s",
                message_id,
                group_id,
                summarize_worktool_response(result),
            )
        except Exception:
            logger.exception("failed to send WorkTool image reply", extra={"group_id": group_id, "image_url": image.url})


def summarize_worktool_response(result: object) -> object:
    if not isinstance(result, dict):
        return result
    return {
        "code": result.get("code"),
        "message": result.get("message"),
        "data": result.get("data"),
    }


def build_worktool_adapter() -> HttpWechatBotAdapter:
    if not container.settings.worktool_robot_id:
        raise HTTPException(status_code=400, detail="WORKTOOL_ROBOT_ID is required")
    return HttpWechatBotAdapter(
        container.settings.worktool_api_base,
        container.settings.worktool_robot_id,
        container.settings.worktool_send_api_token,
    )


@app.post("/worktool/callback-config")
def configure_worktool_callback(payload: WorkToolCallbackConfigIn) -> dict[str, object]:
    adapter = build_worktool_adapter()
    adapter.update_callback(payload.callback_url, payload.reply_all, payload.open_callback)
    return {"configured": True, "callback_url": payload.callback_url}


@app.get("/worktool/online")
def get_worktool_online_status() -> dict[str, object]:
    return build_worktool_adapter().online()


@app.get("/worktool/qa-logs")
def list_worktool_qa_logs(
    page: int = 1,
    size: int = 10,
    sort: str = "start_time,desc",
    name: str | None = None,
    start_time: str | None = None,
    end_time: str | None = None,
) -> dict[str, object]:
    return build_worktool_adapter().list_qa_logs(
        page=page,
        size=size,
        sort=sort,
        name=name,
        start_time=start_time,
        end_time=end_time,
    )


@app.get("/worktool/raw-messages")
def list_worktool_raw_messages(
    message_id: str | None = None,
    page: int = 1,
    size: int = 10,
    sort: str = "create_time,desc",
) -> dict[str, object]:
    return build_worktool_adapter().list_raw_messages(
        message_id=message_id,
        page=page,
        size=size,
        sort=sort,
    )


@app.get("/worktool/raw-results")
def list_worktool_raw_results(
    message_id: str | None = None,
    page: int = 1,
    size: int = 10,
    sort: str = "run_time,desc",
    start_time: str | None = None,
    end_time: str | None = None,
    raw_type: str | None = FastAPIQuery(default=None, alias="type"),
) -> dict[str, object]:
    return build_worktool_adapter().list_raw_results(
        message_id=message_id,
        page=page,
        size=size,
        sort=sort,
        start_time=start_time,
        end_time=end_time,
        raw_type=raw_type,
    )


@app.get("/reviews")
def list_reviews() -> list[dict[str, object]]:
    return [
        {
            "id": item.id,
            "conversation_id": item.conversation_id,
            "question": item.question,
            "answer": item.answer,
            "status": item.status,
            "created_at": item.created_at,
        }
        for item in container.review_service.list_pending()
    ]


@app.get("/conversations")
def list_conversations(limit: int = 50) -> list[dict[str, object]]:
    return [
        {
            "id": log.id,
            "group_id": log.group_id,
            "user_id": log.user_id,
            "message_id": log.message_id,
            "question": log.question,
            "confidence": log.confidence,
            "confidence_score": log.confidence_score,
            "retrieved_chunk_ids": log.retrieved_chunk_ids,
            "draft_answer": log.draft_answer,
            "final_answer": log.final_answer,
            "auto_replied": log.auto_replied,
            "needs_human": log.needs_human,
            "routed_audiences": log.routed_audiences,
            "routing_confidence": log.routing_confidence,
            "routing_reason": log.routing_reason,
            "created_at": log.created_at,
        }
        for log in container.repository.list_conversations(limit)
    ]


@app.get("/quality/report")
def quality_report(limit: int = 100, top: int = 10) -> dict[str, object]:
    return build_quality_report(container.repository.list_conversations(limit), top)


@app.post("/reviews/{review_id}/approve")
def approve_review(review_id: str, payload: ReviewDecisionIn) -> dict[str, object]:
    try:
        item = container.review_service.approve(review_id, payload.reviewer_id, payload.answer)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"id": item.id, "status": item.status}


@app.post("/reviews/{review_id}/reject")
def reject_review(review_id: str, payload: ReviewDecisionIn) -> dict[str, object]:
    try:
        item = container.review_service.reject(review_id, payload.reviewer_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"id": item.id, "status": item.status}
