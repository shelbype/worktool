from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg
from psycopg import sql

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ragbot.audience import AUDIENCES
from ragbot.cli import build_embedding_provider, build_repository
from ragbot.config import get_settings
from ragbot.domain import DocumentStatus, ImageRef, KnowledgeChunk
from ragbot.repositories import AUDIENCE_TABLES, PostgresKnowledgeRepository


TEMPLATE_FIELDS = [
    "知识ID",
    "入库状态",
    "适用端口",
    "角色库",
    "一级分类",
    "二级分类",
    "问题标题",
    "用户问法示例",
    "意图关键词",
    "RAG检索摘要",
    "标准回答",
    "操作步骤",
    "前置条件",
    "排查项",
    "注意事项",
    "不适用场景",
    "转人工条件",
    "关联知识ID",
    "来源类型",
    "来源ID/链接",
    "图片引用",
    "维护人",
    "复核状态",
    "更新时间",
    "质量标签",
    "内部备注（不入检索正文）",
]

MINIMAL_REQUIRED_FIELDS = [
    "知识ID",
    "入库状态",
    "适用端口",
    "角色库",
    "一级分类",
    "问题标题",
    "用户问法示例",
    "意图关键词",
    "RAG检索摘要",
    "标准回答",
    "转人工条件",
    "来源类型",
    "维护人",
    "复核状态",
    "更新时间",
]

IMPORTABLE_STATUS = "可入库"
PENDING_STATUS = "待复核"
NOISE_PATTERNS = ("[图片:", "图片说明：")
TABLES_TO_BACKUP = [
    "help_documents",
    "knowledge_chunks",
    *AUDIENCE_TABLES.values(),
]

AUDIENCE_HINTS = {
    "student": ("学生", "学员", "家长", "学生库", "家长端", "学生端"),
    "teacher": ("老师", "教师", "助教", "老师库", "教师端", "老师端"),
    "principal": ("校长", "校长库", "校长端"),
    "academic": ("教务", "教务库", "教务端", "班主任"),
    "sales": ("销售", "顾问", "销售库", "销售端", "课程顾问"),
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="将标准入库模板 CSV 导入 RAG 正式知识库。默认只生成预检报告，不写数据库。",
    )
    parser.add_argument("--input", default="analysis/服务器正式知识库_标准模板规范化版.csv")
    parser.add_argument("--output-dir", default="analysis")
    parser.add_argument("--execute", action="store_true", help="实际写入 PostgreSQL。未指定时只做预检。")
    parser.add_argument("--clear-existing", action="store_true", help="写入前清空 help_documents、knowledge_chunks 和各角色库。")
    parser.add_argument(
        "--yes-clear-existing",
        action="store_true",
        help="确认允许清空现有正式知识库。仅在 --execute --clear-existing 时需要。",
    )
    parser.add_argument("--include-pending", action="store_true", help="同时导入“待复核”行。默认只导入“可入库”。")
    parser.add_argument("--activate-pending", action="store_true", help="待复核行也以 active 写入。默认待复核行写入 archived。")
    parser.add_argument("--skip-audience-index", action="store_true", help="只写全局知识库，不写角色库分表。")
    parser.add_argument("--limit", type=int, default=0, help="仅处理前 N 条模板行，便于测试。0 表示不限制。")
    args = parser.parse_args()

    input_path = (ROOT / args.input).resolve() if not Path(args.input).is_absolute() else Path(args.input)
    output_dir = (ROOT / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = load_rows(input_path)
    if args.limit > 0:
        rows = rows[: args.limit]

    validation = validate_rows(rows)
    records = build_import_records(rows, include_pending=args.include_pending, activate_pending=args.activate_pending)
    summary = build_summary(input_path, rows, records, validation, args)

    backups: list[str] = []
    imported = False
    if args.execute:
        imported, backups = execute_import(records, args)
        summary["executed"] = imported
        summary["backup_tables"] = backups
    else:
        summary["executed"] = False
        summary["backup_tables"] = []

    mode = "执行" if args.execute else "预检"
    report_path = output_dir / f"服务器正式知识库_模板重新入库{mode}报告.md"
    summary_path = output_dir / f"服务器正式知识库_模板重新入库{mode}摘要.json"
    write_report(report_path, summary, records, validation, args)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8-sig")

    print(json.dumps({"summary": summary, "report": str(report_path), "summary_json": str(summary_path)}, ensure_ascii=False))


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"输入文件不存在：{path}")
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        missing_fields = [field for field in TEMPLATE_FIELDS if field not in (reader.fieldnames or [])]
        if missing_fields:
            raise SystemExit(f"输入 CSV 缺少模板字段：{', '.join(missing_fields)}")
        return [{key: normalize_cell(value) for key, value in row.items()} for row in reader]


def normalize_cell(value: object) -> str:
    if value is None:
        return ""
    return re.sub(r"\r\n?", "\n", str(value)).strip()


def validate_rows(rows: list[dict[str, str]]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    id_counter = Counter(row.get("知识ID", "") for row in rows if row.get("知识ID"))

    duplicate_ids = sorted([knowledge_id for knowledge_id, count in id_counter.items() if count > 1])
    for knowledge_id in duplicate_ids:
        errors.append(f"知识ID重复：{knowledge_id}")

    empty_required: dict[str, list[str]] = defaultdict(list)
    noise_rows: dict[str, list[str]] = defaultdict(list)
    title_repeated_rows: list[str] = []
    short_answer_rows: list[str] = []

    for index, row in enumerate(rows, start=2):
        knowledge_id = row.get("知识ID") or f"第{index}行"
        for field in MINIMAL_REQUIRED_FIELDS:
            if not row.get(field):
                empty_required[field].append(knowledge_id)

        standard_answer = row.get("标准回答", "")
        for pattern in NOISE_PATTERNS:
            if pattern in standard_answer:
                noise_rows[pattern].append(knowledge_id)
        if starts_with_duplicate_title(row.get("问题标题", ""), standard_answer):
            title_repeated_rows.append(knowledge_id)
        if len(standard_answer) < 20:
            short_answer_rows.append(knowledge_id)

    for field, ids in empty_required.items():
        errors.append(f"必填字段为空：{field}，影响 {len(ids)} 条")
    if noise_rows:
        for pattern, ids in noise_rows.items():
            warnings.append(f"标准回答包含噪声 {pattern}，影响 {len(ids)} 条")
    if title_repeated_rows:
        warnings.append(f"标准回答疑似以重复标题开头，影响 {len(title_repeated_rows)} 条")
    if short_answer_rows:
        warnings.append(f"标准回答过短，影响 {len(short_answer_rows)} 条")

    return {
        "errors": errors,
        "warnings": warnings,
        "duplicate_ids": duplicate_ids,
        "empty_required": dict(empty_required),
        "noise_rows": dict(noise_rows),
        "title_repeated_rows": title_repeated_rows,
        "short_answer_rows": short_answer_rows,
    }


def starts_with_duplicate_title(title: str, content: str) -> bool:
    title = title.strip()
    content = content.strip()
    if not title or not content.startswith(title):
        return False
    rest = content[len(title) :].lstrip("：: \n\t")
    return rest.startswith(title)


def build_import_records(
    rows: list[dict[str, str]],
    *,
    include_pending: bool,
    activate_pending: bool,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for row in rows:
        status = row.get("入库状态", "")
        if status != IMPORTABLE_STATUS and not (include_pending and status == PENDING_STATUS):
            continue

        knowledge_id = row["知识ID"]
        audiences = infer_audiences(row)
        image_refs = parse_image_refs(row.get("图片引用", ""))
        content = build_chunk_content(row)
        search_text = build_search_text(row)
        answer_content = build_answer_content(row)
        document_status = DocumentStatus.ACTIVE
        if status == PENDING_STATUS and not activate_pending:
            document_status = DocumentStatus.ARCHIVED

        metadata = build_metadata(row, audiences)
        records.append(
            {
                "row": row,
                "knowledge_id": knowledge_id,
                "document_id": stable_prefixed_id("doc", knowledge_id, max_suffix=36),
                "chunk_id": stable_chunk_id(knowledge_id),
                "title": row["问题标题"],
                "content": content,
                "search_text": search_text,
                "answer_content": answer_content,
                "image_refs": image_refs,
                "metadata": metadata,
                "audiences": audiences,
                "status": document_status,
            }
        )
    return records


def infer_audiences(row: dict[str, str]) -> list[str]:
    text = "；".join([row.get("适用端口", ""), row.get("角色库", "")])
    selected: list[str] = []
    for audience, hints in AUDIENCE_HINTS.items():
        if any(hint and hint in text for hint in hints):
            selected.append(audience)
    if not selected:
        return list(AUDIENCES)
    return [audience for audience in AUDIENCES if audience in selected]


def parse_image_refs(raw: str) -> list[ImageRef]:
    raw = raw.strip()
    if not raw:
        return []
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        value = [item.strip() for item in re.split(r"[；;,，\n]+", raw) if item.strip()]

    if isinstance(value, dict):
        value = [value]
    if not isinstance(value, list):
        return []

    refs: list[ImageRef] = []
    for item in value:
        if isinstance(item, str):
            refs.append(ImageRef(url=item))
            continue
        if not isinstance(item, dict):
            continue
        refs.append(
            ImageRef(
                url=str(item.get("url") or item.get("图片") or item.get("path") or "").strip(),
                alt_text=optional_str(item.get("alt_text") or item.get("alt") or item.get("图片说明")),
                ocr_text=optional_str(item.get("ocr_text") or item.get("ocr")),
                caption=optional_str(item.get("caption") or item.get("说明")),
            )
        )
    return [ref for ref in refs if ref.url]


def optional_str(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def build_chunk_content(row: dict[str, str]) -> str:
    """Build the full content string (kept for backward compatibility)."""
    parts = [
        section("问题", row.get("问题标题", "")),
        section("用户可能问法", row.get("用户问法示例", "")),
        section("意图关键词", row.get("意图关键词", "")),
        section("检索摘要", row.get("RAG检索摘要", "")),
        section("标准回答", row.get("标准回答", "")),
        section("操作步骤", row.get("操作步骤", "")),
        section("前置条件", row.get("前置条件", "")),
        section("排查项", row.get("排查项", "")),
        section("注意事项", row.get("注意事项", "")),
        section("不适用场景", row.get("不适用场景", "")),
        section("转人工条件", row.get("转人工条件", "")),
    ]
    content = "\n\n".join(part for part in parts if part)
    return remove_content_noise(content)


def build_search_text(row: dict[str, str]) -> str:
    """Build search-optimized text for embedding and retrieval.

    Contains only fields meant for matching, not for LLM answer generation:
    问题标题, 用户问法示例, 意图关键词, RAG检索摘要
    """
    parts = [
        section("问题", row.get("问题标题", "")),
        section("用户可能问法", row.get("用户问法示例", "")),
        section("意图关键词", row.get("意图关键词", "")),
        section("检索摘要", row.get("RAG检索摘要", "")),
    ]
    text = "\n\n".join(part for part in parts if part)
    return remove_content_noise(text)


def build_answer_content(row: dict[str, str]) -> str:
    """Build answer-only content for LLM context.

    Contains only fields suitable for generating customer-facing responses:
    标准回答, 操作步骤, 前置条件, 排查项, 注意事项, 不适用场景, 转人工条件
    """
    parts = [
        section("标准回答", row.get("标准回答", "")),
        section("操作步骤", row.get("操作步骤", "")),
        section("前置条件", row.get("前置条件", "")),
        section("排查项", row.get("排查项", "")),
        section("注意事项", row.get("注意事项", "")),
        section("不适用场景", row.get("不适用场景", "")),
        section("转人工条件", row.get("转人工条件", "")),
    ]
    text = "\n\n".join(part for part in parts if part)
    return remove_content_noise(text)


def section(label: str, value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    return f"{label}：\n{value}"


def remove_content_noise(content: str) -> str:
    cleaned_lines: list[str] = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("[图片:") or stripped.startswith("图片说明："):
            continue
        cleaned_lines.append(line.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(cleaned_lines)).strip()


def build_metadata(row: dict[str, str], audiences: list[str]) -> dict[str, Any]:
    source_ref = row.get("来源ID/链接", "")
    source_url = source_ref if re.match(r"^https?://", source_ref) else None
    return {
        "source_id": row.get("知识ID"),
        "source_url": source_url,
        "original_source_ref": source_ref,
        "source_type": row.get("来源类型"),
        "category": row.get("一级分类"),
        "product_module": row.get("一级分类"),
        "product_version": row.get("二级分类") or row.get("适用端口"),
        "secondary_category": row.get("二级分类"),
        "template_knowledge_id": row.get("知识ID"),
        "template_status": row.get("入库状态"),
        "audiences": audiences,
        "applicable_ports": split_multi_value(row.get("适用端口", "")),
        "audience_labels": split_multi_value(row.get("角色库", "")),
        "question_variants": split_multi_value(row.get("用户问法示例", "")),
        "intent_keywords": split_multi_value(row.get("意图关键词", "")),
        "rag_summary": row.get("RAG检索摘要"),
        "related_knowledge_ids": split_multi_value(row.get("关联知识ID", "")),
        "maintainer": row.get("维护人"),
        "review_status": row.get("复核状态"),
        "quality_tags": split_multi_value(row.get("质量标签", "")),
        "internal_note": row.get("内部备注（不入检索正文）"),
        "updated_at": normalized_updated_at(row.get("更新时间", "")),
        "normalized_template_version": "标准模板-v1",
    }


def split_multi_value(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[；;、,，\n]+", value or "") if item.strip()]


def normalized_updated_at(value: str) -> str:
    value = value.strip()
    if not value:
        return datetime.now(timezone.utc).isoformat()
    for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc).isoformat()
        except ValueError:
            pass
    try:
        return datetime.fromisoformat(value).astimezone(timezone.utc).isoformat()
    except ValueError:
        return datetime.now(timezone.utc).isoformat()


def stable_prefixed_id(prefix: str, value: str, *, max_suffix: int = 40) -> str:
    safe = re.sub(r"[^0-9A-Za-z_]+", "_", value).strip("_").lower()
    if not safe:
        safe = hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}_{safe[:max_suffix]}"


def stable_chunk_id(knowledge_id: str) -> str:
    digest = hashlib.sha256(f"standard-template:{knowledge_id}".encode("utf-8")).hexdigest()
    return f"chunk_{digest[:32]}"


def build_chunks(records: list[dict[str, Any]], *, embed: bool) -> list[KnowledgeChunk]:
    embedding_provider = build_embedding_provider(get_settings()) if embed else None
    chunks: list[KnowledgeChunk] = []
    for record in records:
        # Embed the search_text (optimized for retrieval) if available, otherwise content
        text_to_embed = record.get("search_text") or record["content"]
        embedding = embedding_provider.embed(text_to_embed) if embedding_provider else []
        chunks.append(
            KnowledgeChunk(
                id=record["chunk_id"],
                document_id=record["document_id"],
                title=record["title"],
                content=record["content"],
                search_text=record.get("search_text"),
                answer_content=record.get("answer_content"),
                metadata=record["metadata"],
                image_refs=record["image_refs"],
                embedding=embedding,
                status=record["status"],
            )
        )
    return chunks


def execute_import(args_records: list[dict[str, Any]], args: argparse.Namespace) -> tuple[bool, list[str]]:
    if not args_records:
        raise SystemExit("没有可导入记录，已停止执行。")
    validation_errors = validate_records_before_execute(args_records)
    if validation_errors:
        raise SystemExit("导入前校验失败：\n" + "\n".join(validation_errors))

    settings = get_settings()
    repository = build_repository(settings)
    if not isinstance(repository, PostgresKnowledgeRepository):
        raise SystemExit("实际入库需要设置 REPOSITORY_PROVIDER=postgres，并提供 POSTGRES_DSN。当前不是 PostgreSQL 仓库。")
    if args.clear_existing and not args.yes_clear_existing:
        raise SystemExit("将清空正式知识库，必须同时指定 --yes-clear-existing。")

    backups: list[str] = []
    if args.clear_existing:
        backups = backup_tables(settings.postgres_dsn)
        repository.clear_audience_knowledge()
        repository.clear_knowledge()

    repository.init_audience_indexes(settings.embedding_dimensions)
    chunks = build_chunks(args_records, embed=True)
    repository.upsert_chunks(chunks)

    if not args.skip_audience_index:
        by_audience: dict[str, list[KnowledgeChunk]] = {audience: [] for audience in AUDIENCES}
        chunk_by_id = {chunk.id: chunk for chunk in chunks}
        for record in args_records:
            chunk = chunk_by_id[record["chunk_id"]]
            for audience in record["audiences"]:
                by_audience[audience].append(chunk)
        for audience, audience_chunks in by_audience.items():
            if audience_chunks:
                repository.upsert_audience_chunks(audience, audience_chunks)
    return True, backups


def validate_records_before_execute(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    for record in records:
        if not record["content"]:
            errors.append(f"{record['knowledge_id']} 清洗后正文为空")
        answer = record.get("answer_content") or ""
        if not answer.strip():
            errors.append(f"{record['knowledge_id']} 回答正文为空，无法生成客服回答")
        for pattern in NOISE_PATTERNS:
            if pattern in record["content"]:
                errors.append(f"{record['knowledge_id']} 正文仍包含噪声：{pattern}")
            if pattern in answer:
                errors.append(f"{record['knowledge_id']} 回答正文包含噪声：{pattern}")
        if not record["audiences"]:
            errors.append(f"{record['knowledge_id']} 未识别角色库")
    return errors


def backup_tables(dsn: str) -> list[str]:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    created: list[str] = []
    with psycopg.connect(dsn) as conn:
        for table in TABLES_TO_BACKUP:
            if not table_exists(conn, table):
                continue
            backup_name = f"kb_backup_{timestamp}_{table}"
            conn.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(backup_name)))
            conn.execute(
                sql.SQL("CREATE TABLE {} AS TABLE {}").format(
                    sql.Identifier(backup_name),
                    sql.Identifier(table),
                )
            )
            created.append(backup_name)
    return created


def table_exists(conn, table: str) -> bool:
    row = conn.execute("SELECT to_regclass(%s) AS table_name", (table,)).fetchone()
    return bool(row and row[0])


def build_summary(
    input_path: Path,
    rows: list[dict[str, str]],
    records: list[dict[str, Any]],
    validation: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    status_counts = Counter(row.get("入库状态", "") or "空" for row in rows)
    category_counts = Counter(record["row"].get("一级分类", "") or "未分类" for record in records)
    audience_counts: Counter[str] = Counter()
    for record in records:
        audience_counts.update(record["audiences"])

    skipped_rows = [
        row.get("知识ID") or row.get("问题标题") or "未命名"
        for row in rows
        if row.get("入库状态") != IMPORTABLE_STATUS and not (args.include_pending and row.get("入库状态") == PENDING_STATUS)
    ]
    active_records = [record for record in records if record["status"] == DocumentStatus.ACTIVE]
    archived_records = [record for record in records if record["status"] == DocumentStatus.ARCHIVED]
    content_lengths = [len(record["content"]) for record in records]

    return {
        "input": str(input_path),
        "total_rows": len(rows),
        "status_counts": dict(status_counts),
        "import_records": len(records),
        "active_records": len(active_records),
        "archived_records": len(archived_records),
        "skipped_rows": len(skipped_rows),
        "skipped_row_ids_preview": skipped_rows[:30],
        "category_counts": dict(category_counts),
        "audience_counts": dict(audience_counts),
        "content_min_chars": min(content_lengths) if content_lengths else 0,
        "content_avg_chars": round(sum(content_lengths) / len(content_lengths), 1) if content_lengths else 0,
        "content_max_chars": max(content_lengths) if content_lengths else 0,
        "image_ref_records": sum(1 for record in records if record["image_refs"]),
        "image_refs": sum(len(record["image_refs"]) for record in records),
        "validation_errors": validation["errors"],
        "validation_warnings": validation["warnings"],
        "execute_requested": bool(args.execute),
        "clear_existing": bool(args.clear_existing),
        "include_pending": bool(args.include_pending),
        "skip_audience_index": bool(args.skip_audience_index),
    }


def write_report(
    path: Path,
    summary: dict[str, Any],
    records: list[dict[str, Any]],
    validation: dict[str, Any],
    args: argparse.Namespace,
) -> None:
    lines: list[str] = []
    mode = "执行报告" if args.execute else "预检报告"
    lines.append(f"# 服务器正式知识库_模板重新入库{mode}")
    lines.append("")
    lines.append("## 总览")
    lines.append("")
    lines.append(f"- 输入文件：`{summary['input']}`")
    lines.append(f"- 模板总行数：{summary['total_rows']}")
    lines.append(f"- 本次准备入库：{summary['import_records']}")
    lines.append(f"- active：{summary['active_records']}")
    lines.append(f"- archived：{summary['archived_records']}")
    lines.append(f"- 跳过行数：{summary['skipped_rows']}")
    lines.append(f"- 图片引用记录：{summary['image_ref_records']} 条，图片引用 {summary['image_refs']} 个")
    lines.append(f"- 正文长度：最短 {summary['content_min_chars']} 字，平均 {summary['content_avg_chars']} 字，最长 {summary['content_max_chars']} 字")
    lines.append(f"- 是否实际执行：{'是' if summary.get('executed') else '否'}")
    lines.append(f"- 是否清空旧库：{'是' if summary['clear_existing'] else '否'}")
    if summary.get("backup_tables"):
        lines.append(f"- 备份表：{', '.join(summary['backup_tables'])}")
    lines.append("")

    lines.append("## 入库状态分布")
    lines.append("")
    lines.extend(counter_lines(summary["status_counts"]))
    lines.append("")

    lines.append("## 分类分布")
    lines.append("")
    lines.extend(counter_lines(summary["category_counts"]))
    lines.append("")

    lines.append("## 角色库分布")
    lines.append("")
    lines.extend(counter_lines(summary["audience_counts"]))
    lines.append("")

    lines.append("## 校验结果")
    lines.append("")
    if summary["validation_errors"]:
        lines.append("### 错误")
        lines.append("")
        lines.extend(f"- {item}" for item in summary["validation_errors"])
        lines.append("")
    else:
        lines.append("- 未发现阻断导入的错误。")
        lines.append("")
    if summary["validation_warnings"]:
        lines.append("### 警告")
        lines.append("")
        lines.extend(f"- {item}" for item in summary["validation_warnings"])
        lines.append("")
    else:
        lines.append("- 未发现明显质量警告。")
        lines.append("")

    lines.append("## 跳过条目预览")
    lines.append("")
    skipped = summary.get("skipped_row_ids_preview") or []
    if skipped:
        lines.extend(f"- {item}" for item in skipped)
    else:
        lines.append("- 无")
    lines.append("")

    lines.append("## 本次入库条目预览")
    lines.append("")
    for record in records[:80]:
        row = record["row"]
        lines.append(f"### {record['knowledge_id']} {record['title']}")
        lines.append("")
        lines.append(f"- 分类：{row.get('一级分类')} / {row.get('二级分类')}")
        lines.append(f"- 角色库：{'；'.join(record['audiences'])}")
        lines.append(f"- 状态：{record['status']}")
        lines.append(f"- 来源：{row.get('来源类型')} | {row.get('来源ID/链接')}")
        lines.append("")
        answer = row.get("标准回答", "").strip()
        lines.append("> " + answer[:220].replace("\n", "\n> "))
        if len(answer) > 220:
            lines.append("> ...")
        lines.append("")
    if len(records) > 80:
        lines.append(f"（仅展示前 80 条，剩余 {len(records) - 80} 条见 CSV 源文件。）")
        lines.append("")

    lines.append("## 服务器执行命令")
    lines.append("")
    lines.append("在服务器项目目录中，确认 `.env` 已设置 `REPOSITORY_PROVIDER=postgres` 和正确 `POSTGRES_DSN` 后执行：")
    lines.append("")
    lines.append("```bash")
    lines.append("python scripts/import_standard_kb.py --execute --clear-existing --yes-clear-existing")
    lines.append("```")
    lines.append("")
    lines.append("如果需要先只预检，不写库：")
    lines.append("")
    lines.append("```bash")
    lines.append("python scripts/import_standard_kb.py")
    lines.append("```")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8-sig")


def counter_lines(counter: dict[str, int]) -> list[str]:
    if not counter:
        return ["- 无"]
    return [f"- {key or '未填写'}：{value}" for key, value in sorted(counter.items(), key=lambda item: (-item[1], item[0]))]


if __name__ == "__main__":
    main()
