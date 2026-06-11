from __future__ import annotations

from collections import Counter
from dataclasses import asdict

from ragbot.domain import ConfidenceLevel, ConversationLog
from ragbot.text_utils import normalize_customer_text


def build_quality_report(logs: list[ConversationLog], limit: int = 10) -> dict[str, object]:
    low_confidence = [
        log for log in logs if log.confidence == ConfidenceLevel.LOW or str(log.confidence) == str(ConfidenceLevel.LOW)
    ]
    handoff = [log for log in logs if log.needs_human]
    no_answer = [log for log in logs if not log.final_answer]
    return {
        "total": len(logs),
        "low_confidence_count": len(low_confidence),
        "handoff_count": len(handoff),
        "no_answer_count": len(no_answer),
        "low_confidence_top": _top_questions(low_confidence, limit),
        "handoff_top": _top_questions(handoff, limit),
        "no_answer_top": _top_questions(no_answer, limit),
        "recent_samples": [_log_summary(log) for log in logs[: min(limit, len(logs))]],
    }


def _top_questions(logs: list[ConversationLog], limit: int) -> list[dict[str, object]]:
    counter: Counter[str] = Counter()
    latest: dict[str, ConversationLog] = {}
    for log in logs:
        question = normalize_customer_text(log.question)
        if not question:
            continue
        counter[question] += 1
        latest[question] = log
    return [
        {
            "question": question,
            "count": count,
            "latest_message_id": latest[question].message_id,
            "latest_confidence": str(latest[question].confidence),
            "latest_confidence_score": round(latest[question].confidence_score, 4),
        }
        for question, count in counter.most_common(limit)
    ]


def _log_summary(log: ConversationLog) -> dict[str, object]:
    data = asdict(log)
    data["confidence"] = str(log.confidence)
    data["created_at"] = log.created_at.isoformat()
    return data
