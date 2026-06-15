from __future__ import annotations

import re

import jieba

from ragbot.audience import AudienceRoute, AudienceRouter, AUDIENCES
from ragbot.config import Settings
from ragbot.domain import ConfidenceLevel, RetrievalHit, RetrievalResult
from ragbot.providers import EmbeddingProvider, cosine_similarity
from ragbot.quality_config import load_json_config
from ragbot.repositories import KnowledgeRepository


DEFAULT_QUERY_ALIASES = {
    "分配课程": "添加学员 报名课程 班级学生 学员课程",
    "绑定学生": "家长端 我的学生 学生邀请码 绑定学员",
    "忘记密码": "重置密码 修改密码 学员管理 学生管理",
    "重置密码": "忘记密码 修改密码 学员管理 学生管理",
    "选不到老师": "员工管理 老师身份 班级老师 助教 权限",
    "找不到老师": "员工管理 老师身份 班级老师 助教 权限",
    "排课": "智能排课 传统排课 常用时间段 课表 班级课表",
    "导出": "导出课表 课表管理 视图模式",
    "企业微信": "企业微信 关联 协同 核心功能",
    "设备平台": "设备要求 浏览器 Chrome Safari iPad",
    "没有排课": "还没有排课的班级 可以安排布置作业 班级作业",
    "布置作业": "老师助教布置作业 作业功能 作业大纲",
    "新增老师": "创建员工账号 员工管理 老师身份 老师账号",
    "老师账号": "创建员工账号 员工管理 老师身份",
    "员工端口": "系统各端口权限说明 员工权限",
    "端口权限": "系统各端口权限说明 员工权限",
    "消息通知": "更快接收消息通知 通知设置",
    "客户端": "Windows校校客户端 MacOS校校客户端 下载安装说明书",
    "创建课程": "课程管理 创建课程 课程信息",
    "新增课程": "课程管理 创建课程 课程信息",
    "考勤": "考勤功能 考勤记录 课程考勤",
    "作业无法加载": "学生做作业 无法加载 作业加载",
    "音频无法加载": "学生做题 音频无法加载",
    "提交不了": "学生完成测试 无法提交",
    "无法提交": "学生完成测试 无法提交",
    "机构题库": "机构题库 快捷录题 题库功能",
    "销售线索": "销售线索协作 市场线索 跟进",
    "续期": "学生账号如何续期 账号续期",
    "AI小新": "AI小新智能助手 国际学校校长教务 智能助手",
    "班级管理": "班级管理 班级功能 创建班级",
    "单词书学习词汇": "如何使用单词书学习词汇 单词书学习",
    "快捷排课": "快捷排课 操作技巧 排课技巧",
    "首页功能": "首页功能 首页 使用首页",
    "笔记功能": "笔记功能 笔记",
    "学习报告": "学习报告 查看学习报告",
    "在线课堂": "在线课堂",
}


class RetrievalService:
    def __init__(
        self,
        repository: KnowledgeRepository,
        embedding_provider: EmbeddingProvider,
        settings: Settings,
    ) -> None:
        self.repository = repository
        self.embedding_provider = embedding_provider
        self.settings = settings
        configured_aliases = load_json_config(settings.query_aliases_path, DEFAULT_QUERY_ALIASES)
        self.query_aliases = {str(key): str(value) for key, value in configured_aliases.items()}
        self.audience_router = AudienceRouter(settings.audience_routing_path, settings.max_route_audiences)

    def route_query(self, query: str) -> AudienceRoute | None:
        if not self.settings.audience_routing_enabled:
            return None
        return self.audience_router.route(query)

    def retrieve(
        self,
        query: str,
        product_module: str | None = None,
        audiences: list[str] | None = None,
    ) -> RetrievalResult:
        route: AudienceRoute | None = None
        if audiences is None:
            route = self.route_query(query)
            audiences = route.audiences if route else None
        elif audiences:
            audiences = [audience for audience in audiences if audience in AUDIENCES]
        expanded_query = self._expand_query(query)
        query_tokens = self._tokens(expanded_query)
        query_embedding = self.embedding_provider.embed(expanded_query)
        hits: list[RetrievalHit] = []
        chunks = self.repository.find_candidate_chunks(
            expanded_query,
            query_embedding,
            product_module,
            max(self.settings.top_k * 30, 200),
            audiences,
        )
        for chunk in chunks:
            if product_module and chunk.metadata.get("product_module") != product_module:
                continue
            audience = chunk.metadata.get("audience")
            audience = audience if isinstance(audience, str) and audience in AUDIENCES else None
            title_tokens = self._tokens(chunk.title)
            # Use search_text for keyword matching if available (optimized for retrieval)
            search_content = chunk.effective_search_text
            body_tokens = self._tokens(search_content)
            keyword_score = self._keyword_score(query_tokens, body_tokens | title_tokens)
            vector_score = cosine_similarity(query_embedding, chunk.embedding)
            title_boost = self._title_boost(query_tokens, title_tokens, query, chunk.title)
            operation_boost = self._operation_boost(query, chunk.title, search_content)
            rerank_score = min(1.0, 0.45 * keyword_score + 0.45 * vector_score + title_boost + operation_boost)
            if rerank_score > 0:
                hits.append(RetrievalHit(chunk, keyword_score, vector_score, rerank_score, audience))
        hits.sort(key=lambda hit: hit.rerank_score, reverse=True)
        top_hits = hits[: self.settings.top_k]
        score = top_hits[0].rerank_score if top_hits else 0.0
        confidence = self._confidence(score, len(top_hits))
        if confidence == ConfidenceLevel.MEDIUM and top_hits and self._has_strong_title_match(query, top_hits[0], score):
            confidence = ConfidenceLevel.HIGH
        if confidence == ConfidenceLevel.HIGH and self._has_uncertain_sources(top_hits):
            confidence = ConfidenceLevel.MEDIUM
        if route and route.confidence == "low" and confidence == ConfidenceLevel.HIGH:
            if score < self.settings.auto_reply_threshold + 0.08:
                confidence = ConfidenceLevel.MEDIUM
        return RetrievalResult(
            query=query,
            hits=top_hits,
            confidence=confidence,
            confidence_score=score,
            routed_audiences=route.audiences if route else (audiences or []),
            routing_confidence=route.confidence if route else ("manual" if audiences else None),
            routing_reason=route.reason if route else None,
        )

    def _confidence(self, score: float, hit_count: int) -> ConfidenceLevel:
        if hit_count == 0:
            return ConfidenceLevel.LOW
        if score >= self.settings.auto_reply_threshold:
            return ConfidenceLevel.HIGH
        if score >= self.settings.draft_only_threshold:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    def _keyword_score(self, query_tokens: set[str], doc_tokens: set[str]) -> float:
        if not query_tokens or not doc_tokens:
            return 0.0
        overlap = len(query_tokens & doc_tokens)
        return min(1.0, overlap / max(1, len(query_tokens)))

    def _expand_query(self, query: str) -> str:
        additions = [value for key, value in self.query_aliases.items() if key in query]
        if not additions:
            return query
        return f"{query} " + " ".join(additions)

    def _title_boost(self, query_tokens: set[str], title_tokens: set[str], query: str, title: str) -> float:
        if not query_tokens or not title_tokens:
            return 0.0
        boost = 0.12 if query_tokens & title_tokens else 0.0
        compact_query = re.sub(r"\s+", "", query)
        compact_title = re.sub(r"\s+", "", title)
        for size in (4, 3, 2):
            if any(compact_query[index : index + size] in compact_title for index in range(max(1, len(compact_query) - size + 1))):
                return min(0.20, boost + 0.08)
        return boost

    def _operation_boost(self, query: str, title: str, content: str) -> float:
        text = f"{title}\n{content}"
        boost = 0.0
        lower_query = query.lower()
        lower_text = text.lower()
        operation_words = ("怎么", "如何", "新建", "创建", "添加", "导出", "排课", "设置", "重置", "绑定")
        action_words = ("点击", "进入", "填写", "选择", "添加", "创建", "导出", "保存", "设置", "重置")
        if any(word in query for word in operation_words) and any(word in text for word in action_words):
            boost += 0.08
        if "windows" in lower_query and "windows" in lower_text:
            boost += 0.08
        if ("macos" in lower_query or "mac" in lower_query) and ("macos" in lower_text or "mac" in lower_text):
            boost += 0.08
        if "班级" in query and "班级" in text:
            boost += 0.03
        if ("学员" in query or "学生" in query) and ("学员" in text or "学生" in text):
            boost += 0.03
        return min(0.14, boost)

    def _has_uncertain_sources(self, hits: list[RetrievalHit]) -> bool:
        if len(hits) < 2:
            return False
        first, second = hits[0], hits[1]
        if abs(first.rerank_score - second.rerank_score) > 0.03:
            return False
        if first.rerank_score >= self.settings.auto_reply_threshold + 0.08:
            return False
        return self._source_key(first) != self._source_key(second)

    def _has_strong_title_match(self, query: str, hit: RetrievalHit, score: float) -> bool:
        if score < max(self.settings.draft_only_threshold, self.settings.auto_reply_threshold - 0.10):
            return False
        compact_query = re.sub(r"\s+", "", query)
        compact_title = re.sub(r"\s+", "", hit.chunk.title)
        core = compact_query
        for word in (
            "怎么使用",
            "怎么用",
            "如何使用",
            "如何进行",
            "怎么操作",
            "怎么玩",
            "在哪里看",
            "哪里看",
            "功能",
            "说明",
            "一文了解",
            "一文读懂",
        ):
            core = core.replace(word, "")
        if len(core) >= 2 and core in compact_title:
            return True
        important_tokens = {
            token
            for token in self._tokens(query)
            if len(token) >= 2 and token not in {"怎么", "如何", "使用", "功能", "进行", "哪里", "查看", "操作"}
        }
        title_tokens = self._tokens(hit.chunk.title)
        return len(important_tokens & title_tokens) >= 2

    def _source_key(self, hit: RetrievalHit) -> str:
        return str(hit.chunk.metadata.get("source_id") or hit.chunk.document_id)

    def _tokens(self, text: str) -> set[str]:
        latin = re.findall(r"[a-zA-Z0-9_./-]+", text.lower())
        chinese = re.findall(r"[\u4e00-\u9fff]+", text)
        chinese_tokens: set[str] = set()
        for segment in chinese:
            for word in jieba.cut(segment):
                word = word.strip()
                if word:
                    chinese_tokens.add(word)
            # Keep bigram fallback for substring / fuzzy matching
            for i in range(len(segment) - 1):
                chinese_tokens.add(segment[i:i + 2])
        return set(latin) | chinese_tokens
