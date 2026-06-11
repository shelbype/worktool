from __future__ import annotations

from typing import Any
from hashlib import sha256

from pydantic import BaseModel, ConfigDict, Field

from ragbot.domain import WechatMessage
from ragbot.text_utils import normalize_customer_text

class HelpDocumentIn(BaseModel):
    source_id: str
    title: str
    body_html: str
    category: str | None = None
    product_module: str | None = None
    product_version: str | None = None
    source_url: str | None = None
    image_urls: list[str] = Field(default_factory=list)


class WechatWebhookIn(BaseModel):
    message_id: str
    group_id: str
    user_id: str
    content: str
    message_type: str = "text"
    quoted_message_id: str | None = None
    attachments: list[dict[str, Any]] = Field(default_factory=list)


class WorkToolQaCallbackIn(BaseModel):
    model_config = ConfigDict(extra="allow")

    spoken: str = ""
    rawSpoken: str = ""
    receivedName: str = ""
    groupName: str = ""
    groupRemark: str = ""
    roomType: int = 0
    atMe: str | bool = False
    textType: int = 1
    fileBase64: Any | None = None
    messageId: str | None = None

    def provided_message_id(self) -> str | None:
        candidates: list[Any] = [self.messageId]
        extras = self.model_extra or {}
        for key in ("message_id", "messageID", "msgId", "msgID", "msgid", "id"):
            candidates.append(extras.get(key))
        for value in candidates:
            if isinstance(value, str) and value.strip():
                return value.strip()
            if isinstance(value, int):
                return str(value)
        return None

    def to_wechat_message(self, fallback_salt: str | None = None) -> WechatMessage:
        content = normalize_customer_text(self.spoken or self.rawSpoken)
        group_id = self.groupRemark or self.groupName or self.receivedName or "unknown"
        message_id = self.provided_message_id() or self._fallback_message_id(
            group_id, self.receivedName, content, fallback_salt
        )
        return WechatMessage(
            message_id=message_id,
            group_id=group_id,
            user_id=self.receivedName or "unknown",
            content=content,
            message_type="text" if self.textType in {0, 1} else str(self.textType),
            attachments=[{"fileBase64": self.fileBase64}] if self.fileBase64 else [],
        )

    def _fallback_message_id(self, group_id: str, user_id: str, content: str, salt: str | None = None) -> str:
        digest = sha256(f"{group_id}|{user_id}|{content}|{self.rawSpoken}|{salt or ''}".encode("utf-8")).hexdigest()
        return f"worktool_{digest[:24]}"


class WorkToolQaInfo(BaseModel):
    text: str


class WorkToolQaData(BaseModel):
    type: int = 5000
    info: WorkToolQaInfo


class WorkToolQaResponse(BaseModel):
    code: int = 0
    message: str = "success"
    data: WorkToolQaData

    @classmethod
    def reply(cls, text: str) -> "WorkToolQaResponse":
        return cls(data=WorkToolQaData(info=WorkToolQaInfo(text=text)))

    @classmethod
    def no_reply(cls) -> "WorkToolQaResponse":
        return cls(data=WorkToolQaData(info=WorkToolQaInfo(text="")))


class WorkToolCallbackConfigIn(BaseModel):
    callback_url: str
    reply_all: int = 1
    open_callback: int = 1


class QueryIn(BaseModel):
    question: str
    product_module: str | None = None
    audiences: list[str] | None = None


class ReviewDecisionIn(BaseModel):
    reviewer_id: str
    answer: str | None = None
