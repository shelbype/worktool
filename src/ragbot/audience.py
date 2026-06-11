from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ragbot.domain import HelpDocument
from ragbot.quality_config import load_json_config, string_list


AUDIENCES = ("student", "teacher", "principal", "academic", "sales")
AUDIENCE_LABELS = {
    "student": "学生",
    "teacher": "老师",
    "principal": "校长",
    "academic": "教务",
    "sales": "销售",
}

DEFAULT_AUDIENCE_CONFIG: dict[str, object] = {
    "max_route_audiences": 3,
    "default_audiences": list(AUDIENCES),
    "audiences": {
        "student": {
            "keywords": ["学生", "学员", "家长", "家长端", "学生端", "VIP学生", "学习报告", "绑定学生"],
            "routing_keywords": ["学生", "学员", "家长", "家长端", "学生端", "学习报告", "续期", "绑定学生"],
        },
        "teacher": {
            "keywords": ["老师", "助教", "课堂反馈", "布置作业", "作业", "批改", "题库", "模考", "单词书"],
            "routing_keywords": ["老师", "助教", "课堂反馈", "布置作业", "作业", "批改", "题库", "模考", "单词书"],
        },
        "principal": {
            "keywords": ["校长", "校长端", "运营数据", "实时数据", "数据分析", "统计", "报表"],
            "routing_keywords": ["校长", "校长端", "运营", "运营数据", "实时数据", "数据分析", "统计"],
        },
        "academic": {
            "keywords": ["教务", "班级", "新建班级", "创建班级", "课程", "排课", "课表", "考勤", "员工", "权限"],
            "routing_keywords": ["教务", "班级", "新建班级", "创建班级", "课程", "排课", "课表", "考勤", "员工", "权限"],
        },
        "sales": {
            "keywords": ["销售", "课程顾问", "线索", "市场线索", "公池", "订单", "合同", "签约", "报课", "退费", "发票", "报价"],
            "routing_keywords": ["销售", "课程顾问", "线索", "市场线索", "公池", "订单", "合同", "签约", "报课", "退费", "发票", "报价"],
        },
    },
    "source_overrides": {},
    "source_excludes": {},
}


@dataclass(slots=True)
class AudienceRoute:
    audiences: list[str]
    confidence: str
    reason: str
    scores: dict[str, int]


def valid_audiences(values: list[str]) -> list[str]:
    seen: set[str] = set()
    audiences: list[str] = []
    for value in values:
        if value in AUDIENCES and value not in seen:
            seen.add(value)
            audiences.append(value)
    return audiences


def load_audience_config(path: str | Path) -> dict[str, object]:
    config = load_json_config(path, DEFAULT_AUDIENCE_CONFIG)
    if not isinstance(config, dict):
        return DEFAULT_AUDIENCE_CONFIG
    return config


class AudienceAssigner:
    def __init__(self, config_path: str | Path = "config/audience_routing.json") -> None:
        self.config = load_audience_config(config_path)
        self.audience_rules = self._audience_rules()
        self.source_overrides = self._source_map("source_overrides")
        self.source_excludes = self._source_map("source_excludes")
        self.default_audiences = valid_audiences(string_list(self.config.get("default_audiences"))) or list(AUDIENCES)

    def assign_document(self, document: HelpDocument) -> list[str]:
        override = self.source_overrides.get(document.source_id)
        if override:
            return override
        text = "\n".join(
            [
                document.title or "",
                document.category or "",
                document.product_module or "",
                document.body_html or "",
            ]
        )
        scores = self._score_text(text, include_routing_keywords=False)
        selected = [audience for audience, score in scores.items() if score > 0]
        if not selected:
            selected = list(self.default_audiences)
        excluded = set(self.source_excludes.get(document.source_id, []))
        selected = [audience for audience in selected if audience not in excluded]
        return valid_audiences(selected) or list(self.default_audiences)

    def _score_text(self, text: str, include_routing_keywords: bool) -> dict[str, int]:
        scores: dict[str, int] = {}
        for audience, rules in self.audience_rules.items():
            score = 0
            for keyword in rules.get("keywords", []):
                if keyword and keyword in text:
                    score += 2 if len(keyword) >= 4 else 1
            if include_routing_keywords:
                for keyword in rules.get("routing_keywords", []):
                    if keyword and keyword in text:
                        score += 3 if len(keyword) >= 4 else 2
            scores[audience] = score
        return scores

    def _audience_rules(self) -> dict[str, dict[str, list[str]]]:
        raw = self.config.get("audiences")
        if not isinstance(raw, dict):
            raw = DEFAULT_AUDIENCE_CONFIG["audiences"]
        rules: dict[str, dict[str, list[str]]] = {}
        for audience in AUDIENCES:
            item = raw.get(audience, {}) if isinstance(raw, dict) else {}
            item = item if isinstance(item, dict) else {}
            rules[audience] = {
                "keywords": string_list(item.get("keywords")),
                "routing_keywords": string_list(item.get("routing_keywords")),
            }
        return rules

    def _source_map(self, key: str) -> dict[str, list[str]]:
        raw = self.config.get(key)
        if not isinstance(raw, dict):
            return {}
        result: dict[str, list[str]] = {}
        for source_id, audiences in raw.items():
            result[str(source_id)] = valid_audiences(string_list(audiences))
        return result


class AudienceRouter:
    def __init__(self, config_path: str | Path = "config/audience_routing.json", max_audiences: int | None = None) -> None:
        self.assigner = AudienceAssigner(config_path)
        configured_max = self.assigner.config.get("max_route_audiences")
        self.max_audiences = max_audiences or int(configured_max or 3)
        self.max_audiences = max(1, min(self.max_audiences, len(AUDIENCES)))

    def route(self, question: str) -> AudienceRoute:
        scores = self.assigner._score_text(question, include_routing_keywords=True)
        positive = [(audience, score) for audience, score in scores.items() if score > 0]
        if not positive:
            return AudienceRoute(
                audiences=list(AUDIENCES),
                confidence="low",
                reason="no audience keyword matched; searching all audience libraries",
                scores=scores,
            )
        positive.sort(key=lambda item: (-item[1], AUDIENCES.index(item[0])))
        top_audience, top_score = positive[0]
        second_score = positive[1][1] if len(positive) > 1 else 0
        if top_score >= 2 and top_score - second_score >= 2:
            return AudienceRoute(
                audiences=[top_audience],
                confidence="high",
                reason=f"matched {top_audience} audience keywords",
                scores=scores,
            )
        selected = [audience for audience, score in positive if top_score - score <= 1][: self.max_audiences]
        return AudienceRoute(
            audiences=selected,
            confidence="medium",
            reason="multiple close audience matches; searching top candidate libraries",
            scores=scores,
        )
