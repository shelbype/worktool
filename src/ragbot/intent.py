from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from enum import StrEnum

from ragbot.providers import HttpLLMProvider

logger = logging.getLogger(__name__)


class QueryIntent(StrEnum):
    OPERATIONAL = "operational"
    DEFINITIONAL = "definitional"
    TROUBLESHOOTING = "troubleshooting"
    POLICY = "policy"
    CHITCHAT = "chitchat"


@dataclass(slots=True)
class IntentResult:
    primary_intent: QueryIntent = QueryIntent.OPERATIONAL
    is_multi: bool = False
    sub_queries: list[str] = field(default_factory=list)
    reasoning: str = ""
    needs_handoff: bool = False
    handoff_type: str = ""
    handoff_confidence: float = 0.0

    @classmethod
    def single(cls, query: str, intent: QueryIntent = QueryIntent.OPERATIONAL) -> IntentResult:
        """Fallback: treat query as single-intent."""
        return cls(primary_intent=intent, is_multi=False, sub_queries=[query], reasoning="fallback")


INTENT_CLASSIFY_PROMPT = """你是教育SaaS系统的问题分析助手。分析用户问题，输出JSON。

任务：
1. intent：判断问题的主要意图类型
   - operational：操作指引类（怎么、如何、操作步骤）
   - definitional：定义解释类（是什么、功能说明）
   - troubleshooting：故障排查类（无法、不行、出问题、报错）
   - policy：政策类（价格、退款、合同、条款）
   - chitchat：闲聊类（打招呼、无关话题）
2. is_multi：是否为多个独立诉求的复合问题（如"我想做A，还要做B，以及C"）
3. sub_queries：如果是复合问题，拆分为独立的检索关键词短语（每个用空格分隔关键词）；如果不是，返回一个改写后的检索短语
4. reasoning：简要判断依据

输出JSON格式（不要输出其他内容）：
{"intent":"operational","is_multi":false,"sub_queries":["创建班级 新建班级"],"reasoning":"单一操作指引"}

示例：
用户："怎么创建班级" → {"intent":"operational","is_multi":false,"sub_queries":["创建班级 新建班级 班级管理"],"reasoning":"单一操作指引"}

用户："销售那边签了个新单，我想给这个学生排一对一的课，还要能看到这个学生的入学模考成绩"
→ {"intent":"operational","is_multi":true,"sub_queries":["销售线索 跟进签单","排课 一对一课程 智能排课","入学模考成绩 查看成绩"],"reasoning":"三个独立诉求：签单跟进+排课+查成绩"}

用户："作业做不了怎么办" → {"intent":"troubleshooting","is_multi":false,"sub_queries":["作业无法加载 作业功能异常"],"reasoning":"故障排查"}

用户："你好" → {"intent":"chitchat","is_multi":false,"sub_queries":["你好"],"reasoning":"闲聊"}

用户："什么是AI小新" → {"intent":"definitional","is_multi":false,"sub_queries":["AI小新 智能助手 功能介绍"],"reasoning":"定义解释"}

用户："怎么查看学生出勤记录和布置作业" → {"intent":"operational","is_multi":true,"sub_queries":["考勤功能 查看出勤记录","布置作业 班级作业"],"reasoning":"两个独立操作：查考勤+布置作业"}

5. handoff：判断是否需要转接人工客服
   - needs_handoff=true 且 handoff_type="force" 当用户明确要求找人工、找真人，包括表达：
     "有真人吗""转人工""人工""人工看下""客户经理""麻烦处理一下"
     "不上班吗""人呢""找个活人""你是机器人吗""不想和机器人说"
     "让真人来""叫你们客服出来""有没有人"
   - needs_handoff=true 且 handoff_type="sensitive" 当用户涉及敏感业务操作：
     财务类：合同、合同金额、收费、已收、应收、欠费、优惠、订单、账单、
             收款、付款、金额不对、费用不对、退款、退费、退课
     课时类：课时、剩余课时、扣课时、扣错了、没扣课时、课消、消课、
             课时不对、少课时、多扣了、补课、请假、旷课
     权限类：权限、删除、恢复、修改课消、修改课时、重新计算、强制提交
   - needs_handoff=true 且 handoff_type="negative" 当用户表达不满、催促或暗示之前的方案无效：
     "怎么又不行""一直有问题""影响上课""影响收费""太慢了"
     "没人处理""着急""投诉""严重""紧急""马上""急用"
     "客户等着""家长等着""不是这个意思""还是不对""没解决"
     "看不懂""没用""你没回答我的问题""还是不行""仍然不行"
     "还是这样""依旧""还是一样""试了没用""都试过了"
     "没效果""没帮到我""解决不了""到底行不行""耽误事了"
   - 否则 needs_handoff=false, handoff_type="", handoff_confidence=0.0
   - handoff_confidence 为 0.0-1.0 的置信度

示例：
用户："能找个活人过来吗" → {"intent":"chitchat","is_multi":false,"sub_queries":["转人工"],"reasoning":"要求转人工","needs_handoff":true,"handoff_type":"force","handoff_confidence":0.95}

用户："课时扣错了能改吗" → {"intent":"operational","is_multi":false,"sub_queries":["课时管理 修改课时"],"reasoning":"涉及课时修改","needs_handoff":true,"handoff_type":"sensitive","handoff_confidence":0.92}

用户："试了还是不行，你们到底能不能处理" → {"intent":"troubleshooting","is_multi":false,"sub_queries":["故障排查"],"reasoning":"表达不满和催促","needs_handoff":true,"handoff_type":"negative","handoff_confidence":0.90}

用户："怎么建班" → {"intent":"operational","is_multi":false,"sub_queries":["创建班级 新建班级"],"reasoning":"正常操作指引","needs_handoff":false,"handoff_type":"","handoff_confidence":0.0}

用户："家长等着要答复，你们快一点" → {"intent":"operational","is_multi":false,"sub_queries":["家长端 学生管理"],"reasoning":"催促处理","needs_handoff":true,"handoff_type":"negative","handoff_confidence":0.87}"""


class IntentClassifier:
    """Classify query intent and detect/decompose multi-intent compound questions.

    Uses a lightweight LLM call for classification.  Failures are silent —
    the classifier falls back to single-intent with the original query so the
    retrieval pipeline is never blocked.
    """

    def __init__(
        self,
        llm_provider: HttpLLMProvider | None = None,
        enabled: bool = True,
        decompose_enabled: bool = True,
    ) -> None:
        self._llm = llm_provider
        self._enabled = enabled
        self._decompose_enabled = decompose_enabled

    def classify(self, query: str) -> IntentResult:
        """Classify query and decompose if multi-intent.

        Returns IntentResult.single(query) on any failure so the retrieval
        pipeline degrades gracefully to the normal single-query path.
        """
        if not self._enabled:
            return IntentResult.single(query)
        if self._llm is None:
            return IntentResult.single(query)
        try:
            result = self._call_llm(query)
            if result is None:
                return IntentResult.single(query)
            if result.is_multi and not self._decompose_enabled:
                # Decompose disabled: treat as single-intent but use
                # the classifier's rewritten sub_query[0] if available.
                sq = result.sub_queries[0] if result.sub_queries else query
                return IntentResult.single(sq, intent=result.primary_intent)
            if not result.sub_queries:
                return IntentResult.single(query, intent=result.primary_intent)
            return result
        except Exception:
            logger.warning("Intent classify failed, fallback to single-intent", exc_info=True)
            return IntentResult.single(query)

    def _call_llm(self, query: str) -> IntentResult | None:
        """Call LLM and parse the JSON response."""
        assert self._llm is not None  # guarded by classify()
        prompt = f'{INTENT_CLASSIFY_PROMPT}\n\n用户："{query}"\n'
        raw = self._llm.classify_intent(prompt)
        if not raw:
            return None
        # The LLM may wrap JSON in markdown fences or add trailing text.
        return self._parse_response(raw)

    @staticmethod
    def _parse_response(raw: str) -> IntentResult | None:
        """Parse the LLM JSON response, handling common formatting quirks."""
        # Strip markdown code fences if present
        text = raw.strip()
        if text.startswith("```"):
            # Remove opening fence (```json or ```)
            text = text.split("\n", 1)[-1] if "\n" in text else text[3:]
            # Remove closing fence
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()
        # Find the outermost JSON object
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or start >= end:
            logger.warning("No JSON object found in intent classify response: %s", raw[:200])
            return None
        try:
            data = json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            logger.warning("Failed to parse intent classify JSON: %s", raw[:200])
            return None

        intent_str = str(data.get("intent", "operational")).lower()
        try:
            primary_intent = QueryIntent(intent_str)
        except ValueError:
            primary_intent = QueryIntent.OPERATIONAL

        is_multi = bool(data.get("is_multi", False))
        sub_queries_raw = data.get("sub_queries", [])
        if isinstance(sub_queries_raw, list):
            sub_queries = [str(sq).strip() for sq in sub_queries_raw if str(sq).strip()]
        else:
            sub_queries = []

        reasoning = str(data.get("reasoning", ""))

        needs_handoff = bool(data.get("needs_handoff", False))
        handoff_type = str(data.get("handoff_type", ""))
        handoff_confidence = float(data.get("handoff_confidence", 0.0))

        return IntentResult(
            primary_intent=primary_intent,
            is_multi=is_multi,
            sub_queries=sub_queries,
            reasoning=reasoning,
            needs_handoff=needs_handoff,
            handoff_type=handoff_type,
            handoff_confidence=handoff_confidence,
        )
