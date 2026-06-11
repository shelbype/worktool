from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import date, datetime
from pathlib import Path

from analyze_customer_feedback import (
    AUDIENCE_BY_PORT,
    AUTO_KB_TYPES,
    FIELD_ALIASES,
    category_hits,
    clean,
    normalize_question,
    quality_bucket,
)
from export_feedback_approval_list import build_approval_rows


DEFAULT_SOURCE = Path("analysis") / "客户反馈记录_数据汇总_数据表（时间）.csv"
DEFAULT_OUTPUT_CSV = Path("analysis") / "customer_feedback_enterprise_2026_approval.csv"
DEFAULT_OUTPUT_MD = Path("analysis") / "customer_feedback_enterprise_2026_approval.md"
DEFAULT_SUMMARY = Path("analysis") / "customer_feedback_enterprise_2026_approval_summary.json"

PUBLIC_OUTPUT_COLUMNS = [
    "review_id",
    "suggested_decision",
    "human_decision",
    "audience",
    "audience_label",
    "port",
    "type",
    "status",
    "category",
    "question",
    "desc",
    "suggested_answer",
    "date",
    "customer",
    "manager",
    "owner",
    "review_note",
    "score",
]

CSV_FIELD_ALIASES = {
    **FIELD_ALIASES,
    "answer": FIELD_ALIASES["answer"] + ["测试备注", "备注"],
}

TYPE_NORMALIZATION = {
    "功能操作疑问（s）": "操作疑问",
    "功能操作疑问(s)": "操作疑问",
    "使用问题（t）": "使用问题",
    "使用问题(t)": "使用问题",
}

FEATURE_COLUMNS = ["所属功能"]


def parse_feedback_date(value: object) -> date | None:
    text = clean(value)
    if not text:
        return None
    for fmt in (
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


def pick_dict(row: dict[str, object], columns: list[str]) -> str:
    for column in columns:
        if column in row:
            value = clean(row.get(column))
            if value:
                return value
    return ""


def normalize_type(value: str) -> str:
    return TYPE_NORMALIZATION.get(value, value)


def read_csv_records(source_path: Path, since: date) -> tuple[list[dict[str, object]], dict[str, object]]:
    records: list[dict[str, object]] = []
    raw_rows = 0
    date_matched_rows = 0
    invalid_dates = 0
    source_sheet = source_path.stem

    with source_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_rows += 1
            feedback_date = parse_feedback_date(pick_dict(row, CSV_FIELD_ALIASES["date"]))
            if feedback_date is None:
                invalid_dates += 1
                continue
            if feedback_date < since:
                continue
            date_matched_rows += 1

            record = {key: pick_dict(row, aliases) for key, aliases in CSV_FIELD_ALIASES.items()}
            if not (record["question"] or record["desc"] or record["answer"]):
                continue

            raw_type = record["type"]
            record["raw_type"] = raw_type
            record["type"] = normalize_type(raw_type)
            record["date"] = feedback_date.isoformat()
            record["sheet"] = source_sheet
            record["normalized_question"] = normalize_question(record["question"], record["desc"])
            record["audience"] = AUDIENCE_BY_PORT.get(record["port"], "")
            record["quality_bucket"] = quality_bucket(record)
            feature = pick_dict(row, FEATURE_COLUMNS)
            categories = category_hits(" ".join([record["question"], record["desc"], record["answer"], feature]))
            if feature and feature not in categories:
                categories.append(feature)
            record["categories"] = categories
            records.append(record)

    seen: dict[str, dict[str, object]] = {}
    for record in records:
        key = "\x1f".join(
            [
                str(record["normalized_question"]),
                str(record["desc"]),
                str(record["answer"]),
                str(record["port"]),
                str(record["type"]),
            ]
        )
        seen.setdefault(key, record)

    unique = list(seen.values())
    focus = [record for record in unique if record["type"] in AUTO_KB_TYPES]
    summary = {
        "source_file": str(source_path),
        "since": since.isoformat(),
        "raw_rows": raw_rows,
        "invalid_dates": invalid_dates,
        "date_matched_rows": date_matched_rows,
        "records_after_date_with_content": len(records),
        "unique_records": len(unique),
        "unique_answered": sum(1 for record in unique if record["answer"]),
        "operation_usage_unique": len(focus),
        "operation_usage_answered": sum(1 for record in focus if record["answer"]),
        "bucket_counts": Counter(record["quality_bucket"] for record in unique).most_common(),
        "type_counts": Counter(str(record["type"] or "(blank)") for record in unique).most_common(20),
        "status_counts": Counter(str(record["status"] or "(blank)") for record in unique).most_common(20),
        "port_counts": Counter(str(record["port"] or "(blank)") for record in unique).most_common(20),
        "audience_counts": Counter(str(record["audience"] or "(unmapped)") for record in unique).most_common(),
        "category_counts": Counter(category for record in unique for category in record["categories"]).most_common(),
    }
    return unique, summary


def strip_private_fields(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [{column: row.get(column, "") for column in PUBLIC_OUTPUT_COLUMNS} for row in rows]


def write_public_csv(rows: list[dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=PUBLIC_OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def write_public_markdown(rows: list[dict[str, object]], summary: dict[str, object], output_path: Path) -> None:
    decision_counts = Counter(row["suggested_decision"] for row in rows)
    audience_counts = Counter(row["audience_label"] for row in rows)
    category_counts = Counter(row["category"] or "未分类" for row in rows)
    lines = [
        "# 客户反馈人工审批清单",
        "",
        "## 审核口径",
        "",
        f"- 时间范围：`反馈日期 >= {summary['since']}`。",
        "- 内容范围：只整理 `问题类型=操作疑问/使用问题`，且有可作为回答候选的 `测试备注/备注` 的记录。",
        "- CSV 和 Markdown 已去掉原回答、附件和来源字段，仅保留审批所需上下文与建议话术。",
        "",
        "## 汇总",
        "",
        f"- 审核总数：{len(rows)}",
        f"- 建议入库：{decision_counts.get('建议入库', 0)}",
        f"- 改写后入库：{decision_counts.get('改写后入库', 0)}",
        f"- 转人工/暂不入库：{decision_counts.get('转人工/暂不入库', 0)}",
        f"- 原始日期命中记录：{summary['date_matched_rows']}",
        f"- 操作/使用问题且有回答候选：{summary['operation_usage_answered']}",
        "",
        "## 按角色库统计",
        "",
    ]
    for label, count in audience_counts.most_common():
        lines.append(f"- {label}：{count}")
    lines.extend(["", "## 高频分类", ""])
    for label, count in category_counts.most_common(12):
        lines.append(f"- {label}：{count}")
    lines.extend(
        [
            "",
            "## 负责人填写方式",
            "",
            "请在 CSV 的 `human_decision` 列填写：`通过`、`改写后通过`、`不入库` 或 `转人工规则`。",
            "如需补充说明，写在 `review_note` 列。",
            "",
            "## 前 30 条预览",
            "",
        ]
    )
    for row in rows[:30]:
        lines.extend(
            [
                f"### {row['review_id']} | {row['suggested_decision']} | {row['audience_label']}",
                "",
                f"- 问题：{row['question']}",
                f"- 问题描述：{row['desc'] or '无'}",
                f"- 建议话术：{row['suggested_answer']}",
                f"- 日期：{row['date'] or '无'}；客户：{row['customer'] or '无'}；客户经理：{row['manager'] or '无'}；跟进人：{row['owner'] or '无'}",
                "",
            ]
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--since", default="2026-01-01")
    parser.add_argument("--output-csv", default=str(DEFAULT_OUTPUT_CSV))
    parser.add_argument("--output-md", default=str(DEFAULT_OUTPUT_MD))
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--include-risk", action="store_true", default=True)
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        raise SystemExit(f"source file not found: {source_path}")
    since = datetime.strptime(args.since, "%Y-%m-%d").date()

    records, summary = read_csv_records(source_path, since)
    rows = strip_private_fields(build_approval_rows(records, include_risk=args.include_risk))

    output_csv = Path(args.output_csv)
    output_md = Path(args.output_md)
    summary_path = Path(args.summary)

    write_public_csv(rows, output_csv)
    write_public_markdown(rows, summary, output_md)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps(summary | {"approval_rows": len(rows)}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"wrote {output_csv} ({len(rows)} records)")
    print(f"wrote {output_md}")
    print(f"wrote {summary_path}")


if __name__ == "__main__":
    main()
