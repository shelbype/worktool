from __future__ import annotations

import html
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

import xlrd

from ragbot.domain import HelpDocument


class HelpCenterXlsSource:
    def __init__(self, source_dir: str | Path) -> None:
        self.source_dir = Path(source_dir)

    def load_documents(self) -> list[HelpDocument]:
        categories = {self._int(row["id"]): row for row in self._rows("osp_helpcenter_cate.xls")}
        articles = self._rows("osp_helpcenter_art.xls")
        heads = self._rows("osp_helpcenter_artsubhead.xls")
        incs = self._rows("osp_helpcenter_artsubinc.xls")
        keywords = self._rows("osp_helpcenter_kws.xls")

        heads_by_article: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for head in heads:
            heads_by_article[self._int(head["artid"])].append(head)

        incs_by_head: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for inc in incs:
            incs_by_head[self._int(inc["headid"])].append(inc)

        keywords_by_article: dict[int, list[str]] = defaultdict(list)
        for keyword in keywords:
            value = self._text(keyword.get("keyword"))
            if value:
                keywords_by_article[self._int(keyword["artid"])].append(value)

        documents: list[HelpDocument] = []
        for article in sorted(articles, key=lambda row: (self._int(row.get("sort")), self._int(row["id"]))):
            article_id = self._int(article["id"])
            category = categories.get(self._int(article["cateid"]), {})
            body_html, image_urls = self._build_body_html(
                article,
                sorted(heads_by_article[article_id], key=lambda row: (self._int(row.get("sort")), self._int(row["id"]))),
                incs_by_head,
                keywords_by_article[article_id],
            )
            documents.append(
                HelpDocument(
                    id=f"doc_helpcenter_{article_id}",
                    source_id=f"helpcenter:{article_id}",
                    title=self._text(article["title"]) or f"帮助文档 {article_id}",
                    body_html=body_html,
                    category=self._text(category.get("name")),
                    product_module=self._text(category.get("name")),
                    product_version=self._text(article.get("ports")),
                    source_url=None,
                    image_urls=image_urls,
                    updated_at=self._excel_datetime(article.get("ctime")),
                )
            )
        return documents

    def _build_body_html(
        self,
        article: dict[str, Any],
        heads: list[dict[str, Any]],
        incs_by_head: dict[int, list[dict[str, Any]]],
        keywords: list[str],
    ) -> tuple[str, list[str]]:
        image_urls: list[str] = []
        parts = [f"<h1>{html.escape(self._text(article['title']))}</h1>"]
        content = self._text(article.get("content"))
        if content:
            parts.append(self._paragraph(content))
        for head in heads:
            head_title = self._text(head.get("title"))
            if head_title:
                parts.append(f"<h2>{html.escape(head_title)}</h2>")
            for pic in self._split_assets(head.get("pics")):
                image_urls.append(pic)
                parts.append(f'<img src="{html.escape(pic)}" alt="{html.escape(head_title)}">')
            for video in self._split_assets(head.get("videos")):
                parts.append(self._paragraph(f"视频链接：{video}"))

            head_incs = sorted(
                incs_by_head[self._int(head["id"])],
                key=lambda row: (self._int(row.get("sort")), self._int(row["id"])),
            )
            for inc in head_incs:
                inc_content = self._text(inc.get("content"))
                if inc_content:
                    parts.append(self._paragraph(inc_content))
                for pic in self._split_assets(inc.get("pics")):
                    image_urls.append(pic)
                    alt = head_title or self._text(article["title"])
                    parts.append(f'<img src="{html.escape(pic)}" alt="{html.escape(alt)}">')
                for video in self._split_assets(inc.get("videos")):
                    parts.append(self._paragraph(f"视频链接：{video}"))
        if keywords:
            parts.append(self._paragraph("关键词：" + "、".join(sorted(set(keywords)))))
        return "\n".join(parts), image_urls

    def _rows(self, filename: str) -> list[dict[str, Any]]:
        path = self.source_dir / filename
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_index(0)
        headers = [str(sheet.cell_value(0, col)).strip() for col in range(sheet.ncols)]
        return [
            {headers[col]: sheet.cell_value(row, col) for col in range(sheet.ncols)}
            for row in range(1, sheet.nrows)
        ]

    def _paragraph(self, text: str) -> str:
        escaped = html.escape(text)
        escaped = escaped.replace("\n", "<br>")
        return f"<p>{escaped}</p>"

    def _split_assets(self, value: Any) -> list[str]:
        text = self._text(value)
        if not text:
            return []
        return [item.strip() for item in re.split(r"[,，\n\r]+", text) if item.strip()]

    def _text(self, value: Any) -> str:
        if value is None:
            return ""
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        text = str(value).strip()
        if text.lower() in {"null", "none", "nan"}:
            return ""
        return text

    def _int(self, value: Any) -> int:
        if value in {"", None}:
            return 0
        return int(float(value))

    def _excel_datetime(self, value: Any) -> datetime:
        if isinstance(value, (int, float)) and value:
            return xlrd.xldate_as_datetime(value, datemode=0)
        return datetime.now().astimezone()
