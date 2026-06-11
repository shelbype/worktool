from __future__ import annotations

import re
from dataclasses import replace

from bs4 import BeautifulSoup

from ragbot.domain import HelpDocument, ImageRef, KnowledgeChunk
from ragbot.providers import EmbeddingProvider


class ImageTextExtractor:
    def extract_ocr_text(self, image_url: str) -> str | None:
        return None

    def generate_caption(self, image_url: str, alt_text: str | None = None) -> str | None:
        if alt_text:
            return alt_text
        return f"相关操作截图：{image_url}"


class IngestionService:
    def __init__(
        self,
        embedding_provider: EmbeddingProvider,
        image_text_extractor: ImageTextExtractor | None = None,
        max_chunk_chars: int = 900,
    ) -> None:
        self.embedding_provider = embedding_provider
        self.image_text_extractor = image_text_extractor or ImageTextExtractor()
        self.max_chunk_chars = max_chunk_chars

    def ingest_document(self, document: HelpDocument) -> list[KnowledgeChunk]:
        clean_text, image_refs = self._clean_html(document.body_html, document.image_urls)
        sections = self._split_sections(document.title, clean_text)
        chunks: list[KnowledgeChunk] = []
        for index, section in enumerate(sections):
            content = self._append_image_text(section, image_refs)
            metadata = {
                "source_id": document.source_id,
                "source_url": document.source_url,
                "category": document.category,
                "product_module": document.product_module,
                "product_version": document.product_version,
                "chunk_index": index,
                "updated_at": document.updated_at.isoformat(),
            }
            chunk = KnowledgeChunk(
                document_id=document.id,
                title=document.title,
                content=content,
                metadata=metadata,
                image_refs=image_refs,
                status=document.status,
            )
            chunks.append(replace(chunk, embedding=self.embedding_provider.embed(content)))
        return chunks

    def _clean_html(self, html: str, explicit_image_urls: list[str]) -> tuple[str, list[ImageRef]]:
        soup = BeautifulSoup(html, "html.parser")
        image_refs: list[ImageRef] = []
        for image in soup.find_all("img"):
            src = image.get("src")
            if not src:
                continue
            alt_text = image.get("alt")
            image_refs.append(self._build_image_ref(src, alt_text))
            image.replace_with(f"\n[图片: {alt_text or src}]\n")
        for url in explicit_image_urls:
            if all(ref.url != url for ref in image_refs):
                image_refs.append(self._build_image_ref(url, None))
        text = soup.get_text("\n")
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+", " ", text)
        return text.strip(), image_refs

    def _build_image_ref(self, url: str, alt_text: str | None) -> ImageRef:
        return ImageRef(
            url=url,
            alt_text=alt_text,
            ocr_text=self.image_text_extractor.extract_ocr_text(url),
            caption=self.image_text_extractor.generate_caption(url, alt_text),
        )

    def _split_sections(self, title: str, text: str) -> list[str]:
        blocks = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]
        if not blocks:
            return [title]
        chunks: list[str] = []
        current = title
        for block in blocks:
            candidate = f"{current}\n{block}" if current else block
            if len(candidate) <= self.max_chunk_chars:
                current = candidate
                continue
            if current:
                chunks.append(current)
            current = block
        if current:
            chunks.append(current)
        return chunks

    def _append_image_text(self, text: str, image_refs: list[ImageRef]) -> str:
        image_text_parts: list[str] = []
        for ref in image_refs:
            if ref.ocr_text:
                image_text_parts.append(f"图片 OCR：{ref.ocr_text}")
            if ref.caption:
                image_text_parts.append(f"图片说明：{ref.caption}")
        if not image_text_parts:
            return text
        return f"{text}\n\n" + "\n".join(image_text_parts)

