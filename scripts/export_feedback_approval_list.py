from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd

from analyze_customer_feedback import (
    AUDIENCE_BY_PORT,
    AUTO_KB_TYPES,
    DUPLICATE_SHEETS,
    FIELD_ALIASES,
    FAQ_SHEET,
    SKIP_SHEETS,
    category_hits,
    clean,
    normalize_question,
    pick,
    quality_bucket,
)
from build_feedback_review_batch import rewrite_hint, score_row, suggested_decision


AUDIENCE_LABELS = {
    "student": "学生库",
    "teacher": "老师库",
    "principal": "校长库",
    "academic": "教务库",
    "sales": "销售库",
    "": "未映射",
}

DECISION_ORDER = {
    "建议入库": 0,
    "改写后入库": 1,
    "转人工/暂不入库": 2,
}

OUTPUT_COLUMNS = [
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
    "original_answer",
    "suggested_answer",
    "attachment",
    "source_sheet",
    "date",
    "customer",
    "manager",
    "owner",
    "review_note",
    "score",
]


def source_path_from_arg(path_text: str) -> Path:
    if path_text:
        path = Path(path_text)
        if not path.exists():
            raise SystemExit(f"source file not found: {path}")
        return path
    exact = Path("db/init/客户反馈记录.xlsx")
    if exact.exists():
        return exact
    candidates = list(Path("db/init").glob("*.xlsx"))
    if not candidates:
        raise SystemExit("no xlsx files under db/init")
    return candidates[0]


def read_unique_records(source_path: Path) -> list[dict[str, object]]:
    workbook = pd.ExcelFile(source_path, engine="openpyxl")
    records: list[dict[str, object]] = []
    for sheet in workbook.sheet_names:
        frame = workbook.parse(sheet, dtype=object).dropna(how="all")
        if sheet in SKIP_SHEETS or sheet in DUPLICATE_SHEETS or sheet == FAQ_SHEET:
            continue
        columns = set(map(str, frame.columns))
        if not any(column in columns for column in FIELD_ALIASES["question"] + FIELD_ALIASES["desc"]):
            continue
        for _, row in frame.iterrows():
            record = {key: pick(row, aliases) for key, aliases in FIELD_ALIASES.items()}
            if not (record["question"] or record["desc"] or record["answer"]):
                continue
            record["sheet"] = sheet
            record["normalized_question"] = normalize_question(record["question"], record["desc"])
            record["audience"] = AUDIENCE_BY_PORT.get(record["port"], "")
            record["quality_bucket"] = quality_bucket(record)
            record["categories"] = category_hits(" ".join([record["question"], record["desc"], record["answer"]]))
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
    return list(seen.values())


def normalize_decision(decision: str) -> str:
    if "转人工" in decision:
        return "转人工/暂不入库"
    if "改写" in decision:
        return "改写后入库"
    return "建议入库"


def category_text(categories: object) -> str:
    if isinstance(categories, list):
        return "；".join(str(item) for item in categories if item)
    return str(categories or "")


def should_include(record: dict[str, object], include_risk: bool) -> bool:
    if record.get("type") not in AUTO_KB_TYPES:
        return False
    if not clean(record.get("answer")):
        return False
    bucket = record.get("quality_bucket")
    if bucket in {"kb_candidate", "review_rewrite_needed"}:
        return True
    return include_risk and bucket == "risk_review"


def build_approval_rows(records: list[dict[str, object]], include_risk: bool) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for record in records:
        if not should_include(record, include_risk):
            continue
        row = {
            "audience": clean(record.get("audience")),
            "port": clean(record.get("port")),
            "type": clean(record.get("type")),
            "question": clean(record.get("normalized_question") or record.get("question")),
            "desc": clean(record.get("desc")),
            "answer": clean(record.get("answer")),
            "attachment": clean(record.get("attachment")),
            "categories": category_text(record.get("categories")),
        }
        row["score"] = score_row(pd.Series(row))
        suggested = normalize_decision(suggested_decision(pd.Series(row)))
        if record.get("quality_bucket") == "review_rewrite_needed" and suggested == "建议入库":
            suggested = "改写后入库"
        if record.get("quality_bucket") == "risk_review":
            suggested = "转人工/暂不入库"
        audience = row["audience"]
        rows.append(
            {
                "suggested_decision": suggested,
                "human_decision": "",
                "audience": audience,
                "audience_label": AUDIENCE_LABELS.get(audience, audience or "未映射"),
                "port": row["port"],
                "type": row["type"],
                "status": clean(record.get("status")),
                "category": row["categories"],
                "question": row["question"],
                "desc": row["desc"],
                "original_answer": row["answer"],
                "suggested_answer": rewrite_hint(pd.Series(row)),
                "attachment": row["attachment"],
                "source_sheet": clean(record.get("sheet")),
                "date": clean(record.get("date")),
                "customer": clean(record.get("customer")),
                "manager": clean(record.get("manager")),
                "owner": clean(record.get("owner")),
                "review_note": "",
                "score": row["score"],
            }
        )

    rows.sort(
        key=lambda item: (
            DECISION_ORDER.get(str(item["suggested_decision"]), 9),
            -int(item["score"]),
            str(item["audience"]),
            str(item["category"]),
        )
    )
    for index, row in enumerate(rows, start=1):
        row["review_id"] = f"fb-approval-{index:04d}"
    return rows


def write_csv(rows: list[dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, object]], summary: dict[str, object], output_path: Path) -> None:
    decision_counts = Counter(row["suggested_decision"] for row in rows)
    audience_counts = Counter(row["audience_label"] for row in rows)
    category_counts = Counter(row["category"] or "未分类" for row in rows)
    lines = [
        "# 客户反馈人工审批清单",
        "",
        "## 审核口径",
        "",
        "- 范围：只整理 `问题类型=操作疑问/使用问题` 且有原始回答的数据。",
        "- 目的：审核后作为知识库候选，不直接自动入正式知识库。",
        "- `建议入库`：问题和答案比较通用，负责人确认后可入待发布知识。",
        "- `改写后入库`：原回答偏内部记录，需要按 `suggested_answer` 改成客户可见话术。",
        "- `转人工/暂不入库`：涉及风险、个案或不适合自动回复，只沉淀为转人工规则。",
        "",
        "## 汇总",
        "",
        f"- 审核总数：{len(rows)}",
        f"- 建议入库：{decision_counts.get('建议入库', 0)}",
        f"- 改写后入库：{decision_counts.get('改写后入库', 0)}",
        f"- 转人工/暂不入库：{decision_counts.get('转人工/暂不入库', 0)}",
        f"- 原始唯一记录数：{summary['unique_records']}",
        f"- 操作/使用问题且有回答：{summary['operation_usage_answered']}",
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
                f"- 原回答：{row['original_answer']}",
                f"- 建议话术：{row['suggested_answer']}",
                "",
            ]
        )
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="")
    parser.add_argument("--output-dir", default="analysis")
    parser.add_argument("--include-risk", action="store_true")
    args = parser.parse_args()

    source_path = source_path_from_arg(args.source)
    records = read_unique_records(source_path)
    rows = build_approval_rows(records, include_risk=args.include_risk)

    focus = [record for record in records if record.get("type") in AUTO_KB_TYPES]
    summary = {
        "source_file": str(source_path),
        "unique_records": len(records),
        "operation_usage_unique": len(focus),
        "operation_usage_answered": sum(1 for record in focus if clean(record.get("answer"))),
        "approval_rows": len(rows),
        "decision_counts": Counter(row["suggested_decision"] for row in rows).most_common(),
        "audience_counts": Counter(row["audience_label"] for row in rows).most_common(),
        "category_counts": Counter(row["category"] or "未分类" for row in rows).most_common(20),
    }

    output_dir = Path(args.output_dir)
    csv_path = output_dir / "customer_feedback_approval_all.csv"
    md_path = output_dir / "customer_feedback_approval_all.md"
    json_path = output_dir / "customer_feedback_approval_all_summary.json"
    write_csv(rows, csv_path)
    write_markdown(rows, summary, md_path)
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "source_file": summary["source_file"],
                "approval_rows": summary["approval_rows"],
                "decision_counts": summary["decision_counts"],
                "audience_counts": summary["audience_counts"],
                "outputs": [str(csv_path), str(md_path), str(json_path)],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
