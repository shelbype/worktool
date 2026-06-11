from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


DECISION_ORDER = {
    "建议入库": 0,
    "改写后入库": 1,
    "转人工/暂不入库": 2,
}

CHECKBOX_LINE = "□ 通过　□ 改写后通过　□ 不入库　□ 转人工规则"


def value(row: dict[str, str], key: str, default: str = "无") -> str:
    text = (row.get(key) or "").strip()
    return text or default


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def sort_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(
        rows,
        key=lambda row: (
            DECISION_ORDER.get(row.get("suggested_decision", ""), 9),
            row.get("audience_label", ""),
            row.get("review_id", ""),
        ),
    )


def render_record(row: dict[str, str]) -> list[str]:
    title_bits = [
        value(row, "review_id"),
        value(row, "category"),
    ]
    lines = [
        f"#### {' | '.join(title_bits)}",
        "",
        f"- 问题：{value(row, 'question')}",
        f"- 问题描述：{value(row, 'desc')}",
        f"- 建议话术：{value(row, 'suggested_answer')}",
    ]

    metadata = [
        ("日期", value(row, "date")),
        ("客户", value(row, "customer")),
        ("客户经理", value(row, "manager")),
        ("跟进人", value(row, "owner")),
    ]
    metadata_text = "；".join(f"{label}：{text}" for label, text in metadata if text != "无")
    if metadata_text:
        lines.append(f"- {metadata_text}")

    lines.extend(
        [
            f"- 审核结论：{CHECKBOX_LINE}",
            "- 审核备注：",
            "",
        ]
    )
    return lines


def render_markdown(rows: list[dict[str, str]], source_path: Path) -> str:
    sorted_rows = sort_rows(rows)
    decision_counts = Counter(row.get("suggested_decision", "") for row in sorted_rows)
    audience_counts = Counter(row.get("audience_label", "") for row in sorted_rows)
    category_counts = Counter(row.get("category") or "未分类" for row in sorted_rows)

    lines = [
        "# 客户反馈人工审批明细",
        "",
        f"- 审核总数：{len(sorted_rows)}",
        "- 审核范围：`问题类型=操作疑问/使用问题`，且有可作为回答候选的话术。",
        "- 使用方式：负责人阅读每条记录后，在 CSV 的 `human_decision` 和 `review_note` 两列填写最终结论。",
        "",
        "## 审核结论口径",
        "",
        "- `建议入库`：问题和答案比较通用，确认无误后可进入待发布知识。",
        "- `改写后入库`：候选话术需要按负责人意见改写后再入库。",
        "- `转人工/暂不入库`：风险、个案、数据恢复、合同收费等问题，不参与自动回复。",
        "",
        "## 汇总",
        "",
        "### 按建议结论",
        "",
    ]
    for decision in ["建议入库", "改写后入库", "转人工/暂不入库"]:
        lines.append(f"- {decision}：{decision_counts.get(decision, 0)}")
    lines.extend(["", "### 按角色库", ""])
    for audience, count in audience_counts.most_common():
        lines.append(f"- {audience or '未映射'}：{count}")
    lines.extend(["", "### 高频分类 Top 20", ""])
    for category, count in category_counts.most_common(20):
        lines.append(f"- {category}：{count}")
    lines.extend(["", "## 审核明细", ""])

    for decision in ["建议入库", "改写后入库", "转人工/暂不入库"]:
        decision_rows = [row for row in sorted_rows if row.get("suggested_decision") == decision]
        if not decision_rows:
            continue
        lines.extend([f"## {decision}（{len(decision_rows)} 条）", ""])
        grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in decision_rows:
            grouped[row.get("audience_label") or "未映射"].append(row)
        for audience, audience_rows in sorted(grouped.items()):
            lines.extend([f"### {audience}（{len(audience_rows)} 条）", ""])
            for row in audience_rows:
                lines.extend(render_record(row))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="analysis/customer_feedback_approval_all.csv")
    parser.add_argument("--output", default="analysis/customer_feedback_approval_all_readable.md")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    rows = read_rows(input_path)
    output_path.write_text(render_markdown(rows, input_path), encoding="utf-8")
    print(f"wrote {output_path} ({len(rows)} records)")


if __name__ == "__main__":
    main()
