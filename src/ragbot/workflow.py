from __future__ import annotations

from ragbot.answering import AnswerService
from ragbot.domain import ConversationLog, ImageRef, ReviewItem, WechatMessage
from ragbot.quality_config import load_json_config, string_list
from ragbot.repositories import KnowledgeRepository
from ragbot.retrieval import RetrievalService


DEFAULT_HANDOFF_PATTERNS = ["报价", "合同", "退款", "退费", "赔偿", "发票", "绑定学生", "签约", "订单取消"]


class MessagePreprocessor:
    def __init__(self, sensitive_patterns: list[str] | None = None, rules_path: str = "config/handoff_rules.json") -> None:
        if sensitive_patterns is not None:
            self.sensitive_patterns = sensitive_patterns
            return
        rules = load_json_config(rules_path, {"patterns": DEFAULT_HANDOFF_PATTERNS})
        configured_patterns = string_list(rules.get("patterns")) if isinstance(rules, dict) else []
        self.sensitive_patterns = configured_patterns or DEFAULT_HANDOFF_PATTERNS

    def should_ignore(self, message: WechatMessage) -> bool:
        content = message.content.strip()
        return message.message_type != "text" or len(content) < 3

    def requires_human(self, message: WechatMessage) -> bool:
        return any(pattern in message.content for pattern in self.sensitive_patterns)


class WechatBotAdapter:
    def send_group_message(self, group_id: str, content: str, at_list: list[str] | None = None) -> None:
        raise NotImplementedError

    def send_group_image(self, group_id: str, image_url: str, caption: str | None = None) -> None:
        raise NotImplementedError


class CapturingWechatBotAdapter(WechatBotAdapter):
    def __init__(self) -> None:
        self.sent_messages: list[tuple[str, str]] = []
        self.sent_message_mentions: list[list[str]] = []
        self.sent_images: list[tuple[str, str, str | None]] = []

    def send_group_message(self, group_id: str, content: str, at_list: list[str] | None = None) -> None:
        self.sent_messages.append((group_id, content))
        self.sent_message_mentions.append(at_list or [])

    def send_group_image(self, group_id: str, image_url: str, caption: str | None = None) -> None:
        self.sent_images.append((group_id, image_url, caption))


class WechatRagWorkflow:
    def __init__(
        self,
        repository: KnowledgeRepository,
        retrieval_service: RetrievalService,
        answer_service: AnswerService,
        wechat_adapter: WechatBotAdapter,
        preprocessor: MessagePreprocessor | None = None,
    ) -> None:
        self.repository = repository
        self.retrieval_service = retrieval_service
        self.answer_service = answer_service
        self.wechat_adapter = wechat_adapter
        self.preprocessor = preprocessor or MessagePreprocessor()

    def handle_message(
        self, message: WechatMessage, send_auto_reply: bool = True, intent_result=None
    ) -> ConversationLog | None:
        existing = self.repository.get_conversation_by_message_id(message.message_id)
        if existing:
            return existing
        if self.preprocessor.should_ignore(message):
            return None
        route = self.retrieval_service.route_query(message.content)
        if self.preprocessor.requires_human(message):
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
                routed_audiences=route.audiences if route else [],
                routing_confidence=route.confidence if route else None,
                routing_reason=route.reason if route else None,
            )
            self.repository.save_conversation(log)
            self.repository.add_review_item(ReviewItem(log.id, message.content, None))
            return log

        retrieval = self.retrieval_service.retrieve(message.content, intent_result=intent_result)
        decision = self.answer_service.answer(message.content, retrieval)
        if send_auto_reply and decision.auto_reply and decision.answer:
            self.wechat_adapter.send_group_message(message.group_id, decision.answer)
        log = ConversationLog(
            group_id=message.group_id,
            user_id=message.user_id,
            message_id=message.message_id,
            question=message.content,
            confidence=decision.confidence,
            confidence_score=decision.confidence_score,
            retrieved_chunk_ids=decision.cited_chunk_ids,
            draft_answer=decision.answer,
            final_answer=decision.answer if decision.auto_reply else None,
            auto_replied=decision.auto_reply,
            needs_human=decision.needs_human,
            routed_audiences=retrieval.routed_audiences,
            routing_confidence=retrieval.routing_confidence,
            routing_reason=retrieval.routing_reason,
        )
        self.repository.save_conversation(log)
        self.repository.add_review_item(ReviewItem(log.id, message.content, decision.answer))
        return log

    def collect_reply_images(self, log: ConversationLog, limit: int) -> list[ImageRef]:
        if limit <= 0 or not log.auto_replied:
            return []
        images: list[ImageRef] = []
        seen_urls: set[str] = set()
        for chunk_id in log.retrieved_chunk_ids[:2]:
            chunk = self.repository.get_chunk(chunk_id)
            if chunk is None:
                continue
            for image in chunk.image_refs:
                if not image.url or image.url in seen_urls:
                    continue
                seen_urls.add(image.url)
                images.append(image)
                if len(images) >= limit:
                    return images
        return images
