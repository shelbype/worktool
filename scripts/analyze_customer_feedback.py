from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd


FIELD_ALIASES = {
    "date": ["\u53cd\u9988\u65e5\u671f", "\u65f6\u95f4"],
    "question": ["\u5ba2\u6237\u95ee\u9898", "\u5ba2\u6237\u95ee\u9898\u63cf\u8ff0", "\u95ee\u9898"],
    "desc": ["\u95ee\u9898\u63cf\u8ff0"],
    "customer": ["\u5ba2\u6237\u540d\u79f0"],
    "manager": ["\u6240\u5c5e\u5ba2\u6237\u7ecf\u7406"],
    "port": ["\u7aef\u53e3"],
    "type": ["\u95ee\u9898\u7c7b\u578b"],
    "status": ["\u5904\u7406\u8fdb\u5ea6"],
    "feedback": ["\u53cd\u9988\u8fdb\u5ea6"],
    "attachment": ["\u9644\u4ef6"],
    "owner": ["\u8ddf\u8fdb\u4eba"],
    "answer": ["\u95ee\u9898\u56de\u7b54", "\u89e3\u51b3\u65b9\u6848"],
    "remark": ["\u5907\u6ce8"],
}

SKIP_SHEETS = {"\u4f01\u4e1a\u7248\u6bcf\u65e5\u6570\u636e\u6c47\u603b "}
FAQ_SHEET = "\u5e38\u89c1\u95ee\u7b54"
DUPLICATE_SHEETS = {"\u5ba2\u6237\u53cd\u9988\u6570\u636e10\u6708\uff08\u526f\u672c\uff09"}

AUDIENCE_BY_PORT = {
    "\u5b66\u751f": "student",
    "\u5b66\u5458": "student",
    "\u5bb6\u957f": "student",
    "\u8001\u5e08": "teacher",
    "\u52a9\u6559": "teacher",
    "\u6821\u957f": "principal",
    "\u6559\u52a1": "academic",
    "\u9500\u552e": "sales",
    "\u5e02\u573a": "sales",
    "\u8d22\u52a1": "sales",
}

AUTO_KB_TYPES = {"\u64cd\u4f5c\u7591\u95ee", "\u4f7f\u7528\u95ee\u9898"}
HUMAN_OR_TICKET_TYPES = {
    "bug",
    "\u9898\u76ee\u95ee\u9898",
    "\u673a\u6784\u9898\u76ee\u95ee\u9898",
    "\u6570\u636e\u6062\u590d\u9700\u6c42",
    "\u5f55\u5165\u9700\u6c42",
    "\u9898\u76ee\u9700\u6c42",
    "\u67e5\u8be2\u9700\u6c42",
    "\u9700\u6c42",
    "\u4f18\u5316",
    "\u5165\u5b66\u6a21\u8003\u914d\u7f6e",
}
RISK_PATTERNS = [
    "\u9000\u8d39",
    "\u9000\u6b3e",
    "\u8d54\u507f",
    "\u5408\u540c",
    "\u53d1\u7968",
    "\u62a5\u4ef7",
    "\u6536\u8d39",
    "\u6298\u6263",
    "\u5220\u9664",
    "\u6062\u590d",
    "\u6570\u636e\u6062\u590d",
    "\u8d26\u53f7\u6570\u636e",
    "\u9898\u76ee\u6709\u8bef",
    "\u7b54\u6848\u9519\u8bef",
]
CUSTOMER_SPECIFIC_PATTERNS = [
    "\u5e2e\u5fd9\u770b",
    "\u8fd9\u4e2a\u5b66\u751f",
    "\u8fd9\u4e2a\u8d26\u53f7",
    "\u8fd9\u4e2a\u73ed",
    "\u9ebb\u70e6\u8001\u5e08",
    "\u94fe\u63a5",
    "http",
    "\u622a\u56fe",
    "\u540e\u53f0\u5e2e\u5fd9",
    "\u6280\u672f\u53ef\u4ee5",
]


def clean(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return re.sub(r"\s+", " ", str(value)).strip()


def pick(row, columns: list[str]) -> str:
    for column in columns:
        if column in row.index:
            value = clean(row[column])
            if value:
                return value
    return ""


def normalize_question(question: str, desc: str) -> str:
    text = question or desc
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[@#][^\s]+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def is_risky(record: dict[str, object]) -> bool:
    text = f"{record['question']} {record['desc']} {record['answer']} {record['type']}"
    return any(pattern in text for pattern in RISK_PATTERNS)


def is_customer_specific(record: dict[str, object]) -> bool:
    text = f"{record['question']} {record['desc']}"
    return any(pattern in text for pattern in CUSTOMER_SPECIFIC_PATTERNS)


def quality_bucket(record: dict[str, object]) -> str:
    if record["type"] in HUMAN_OR_TICKET_TYPES:
        return "ticket_or_handoff"
    if is_risky(record):
        return "risk_review"
    if record["type"] in AUTO_KB_TYPES and record["answer"] and len(str(record["answer"])) >= 8:
        if is_customer_specific(record):
            return "review_rewrite_needed"
        return "kb_candidate"
    if record["answer"]:
        return "review_rewrite_needed"
    return "no_answer_or_low_value"


def category_hits(text: str) -> list[str]:
    rules = {
        "\u8d26\u53f7\u767b\u5f55/\u5bc6\u7801/\u624b\u673a\u53f7": [
            "\u767b\u5f55",
            "\u8d26\u53f7",
            "\u5bc6\u7801",
            "\u624b\u673a\u53f7",
            "\u7eed\u671f",
            "VIP",
            "\u529f\u80fd\u6682\u672a\u5f00\u901a",
        ],
        "\u4f5c\u4e1a/\u5e03\u7f6e/\u6279\u6539/\u53cd\u9988": [
            "\u4f5c\u4e1a",
            "\u5e03\u7f6e",
            "\u6279\u6539",
            "\u53cd\u9988",
            "\u5f85\u53cd\u9988",
            "\u7ec3\u4e60\u60c5\u51b5",
        ],
        "\u97f3\u9891/\u5f55\u97f3/\u542c\u529b": ["\u97f3\u9891", "\u5f55\u97f3", "\u542c\u529b", "\u6ca1\u6709\u58f0\u97f3", "\u52a0\u8f7d"],
        "\u6d4f\u89c8\u5668/\u7f51\u7edc/\u7f13\u5b58": ["\u6d4f\u89c8\u5668", "\u8c37\u6b4c", "\u7f13\u5b58", "\u7f51\u7edc", "\u5237\u65b0"],
        "\u73ed\u7ea7/\u6392\u8bfe/\u8bfe\u65f6/\u8003\u52e4": ["\u73ed\u7ea7", "\u6392\u8bfe", "\u8bfe\u65f6", "\u8003\u52e4", "\u8f6c\u73ed", "\u8bfe\u8868"],
        "\u8ba2\u5355/\u5408\u540c/\u62a5\u8bfe/\u6536\u8d39": ["\u8ba2\u5355", "\u5408\u540c", "\u62a5\u8bfe", "\u6536\u8d39", "\u9000\u8d39", "\u91d1\u989d", "\u5b66\u6742\u8d39"],
        "\u6743\u9650/\u89d2\u8272/\u516c\u6c60": ["\u6743\u9650", "\u89d2\u8272", "\u8eab\u4efd", "\u516c\u6c60", "\u770b\u4e0d\u5230"],
        "\u9898\u5e93/\u5f55\u9898/\u5355\u8bcd\u4e66/\u6a21\u8003": ["\u9898\u5e93", "\u5f55\u9898", "\u5355\u8bcd\u4e66", "\u6a21\u8003", "\u5165\u5b66\u6d4b\u8bd5", "\u8bd5\u5377"],
        "\u5c0f\u7a0b\u5e8f/\u516c\u4f17\u53f7/\u4e8c\u7ef4\u7801": ["\u5c0f\u7a0b\u5e8f", "\u516c\u4f17\u53f7", "\u4e8c\u7ef4\u7801", "\u626b\u7801"],
    }
    return [name for name, keywords in rules.items() if any(keyword in text for keyword in keywords)]


def compact(record: dict[str, object]) -> dict[str, object]:
    return {
        "audience": record.get("audience"),
        "port": record.get("port"),
        "type": record.get("type"),
        "question": record.get("normalized_question") or record.get("question"),
        "desc": record.get("desc"),
        "answer": record.get("answer"),
        "attachment": record.get("attachment"),
        "bucket": record.get("quality_bucket"),
        "categories": record.get("categories"),
    }


def main() -> None:
    xlsx_files = list(Path("db/init").glob("*.xlsx"))
    if not xlsx_files:
        raise SystemExit("no xlsx files under db/init")
    source_path = xlsx_files[0]
    workbook = pd.ExcelFile(source_path, engine="openpyxl")

    records: list[dict[str, object]] = []
    faq: list[dict[str, object]] = []
    sheet_stats: list[dict[str, object]] = []
    for sheet in workbook.sheet_names:
        frame = workbook.parse(sheet, dtype=object).dropna(how="all")
        sheet_stats.append({"sheet": sheet, "rows": int(len(frame)), "columns": list(map(str, frame.columns))})
        if sheet in SKIP_SHEETS or sheet in DUPLICATE_SHEETS:
            continue
        if sheet == FAQ_SHEET:
            for _, row in frame.iterrows():
                question = pick(row, FIELD_ALIASES["question"])
                answer = pick(row, FIELD_ALIASES["answer"])
                if question or answer:
                    faq.append(
                        {
                            "sheet": sheet,
                            "question": question,
                            "answer": answer,
                            "audience": "",
                            "quality_bucket": "kb_candidate" if question and answer else "no_answer_or_low_value",
                        }
                    )
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
            record["has_attachment"] = bool(record["attachment"])
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
    unique = list(seen.values())

    kb_candidates = [record for record in unique if record["quality_bucket"] == "kb_candidate"]
    rewrite_candidates = [record for record in unique if record["quality_bucket"] == "review_rewrite_needed"]
    ticket_candidates = [record for record in unique if record["quality_bucket"] == "ticket_or_handoff"]
    risk_candidates = [record for record in unique if record["quality_bucket"] == "risk_review"]
    focus = [record for record in unique if record["type"] in AUTO_KB_TYPES]

    summary = {
        "source_file": str(source_path),
        "sheets": sheet_stats,
        "raw_records_excluding_summary_and_duplicate": len(records),
        "unique_records": len(unique),
        "unique_answered": sum(1 for record in unique if record["answer"]),
        "faq_rows": len(faq),
        "faq_answered": sum(1 for row in faq if row["answer"]),
        "operation_usage_unique": len(focus),
        "operation_usage_answered": sum(1 for record in focus if record["answer"]),
        "bucket_counts": Counter(record["quality_bucket"] for record in unique).most_common(),
        "type_counts": Counter(str(record["type"] or "(blank)") for record in unique).most_common(20),
        "port_counts": Counter(str(record["port"] or "(blank)") for record in unique).most_common(20),
        "audience_counts": Counter(str(record["audience"] or "(unmapped)") for record in unique).most_common(),
        "category_counts": Counter(category for record in unique for category in record["categories"]).most_common(),
        "kb_candidate_count": len(kb_candidates),
        "rewrite_candidate_count": len(rewrite_candidates),
        "risk_review_count": len(risk_candidates),
        "ticket_or_handoff_count": len(ticket_candidates),
        "kb_candidate_samples": [compact(record) for record in kb_candidates[:30]],
        "rewrite_samples": [compact(record) for record in rewrite_candidates[:20]],
        "ticket_samples": [compact(record) for record in ticket_candidates[:20]],
        "risk_samples": [compact(record) for record in risk_candidates[:20]],
        "faq_samples": faq[:20],
    }

    out_dir = Path("analysis")
    out_dir.mkdir(exist_ok=True)
    (out_dir / "customer_feedback_analysis.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    pd.DataFrame([compact(record) for record in kb_candidates[:300]]).to_csv(
        out_dir / "customer_feedback_kb_candidates_preview.csv", index=False, encoding="utf-8-sig"
    )
    pd.DataFrame([compact(record) for record in rewrite_candidates[:300]]).to_csv(
        out_dir / "customer_feedback_rewrite_candidates_preview.csv", index=False, encoding="utf-8-sig"
    )
    pd.DataFrame([compact(record) for record in ticket_candidates[:300]]).to_csv(
        out_dir / "customer_feedback_ticket_or_handoff_preview.csv", index=False, encoding="utf-8-sig"
    )

    print(
        json.dumps(
            {
                "source_file": summary["source_file"],
                "raw_records_excluding_summary_and_duplicate": summary["raw_records_excluding_summary_and_duplicate"],
                "unique_records": summary["unique_records"],
                "unique_answered": summary["unique_answered"],
                "operation_usage_unique": summary["operation_usage_unique"],
                "operation_usage_answered": summary["operation_usage_answered"],
                "bucket_counts": summary["bucket_counts"],
                "audience_counts": summary["audience_counts"],
                "category_counts": summary["category_counts"][:12],
                "outputs": [
                    str(out_dir / "customer_feedback_analysis.json"),
                    str(out_dir / "customer_feedback_kb_candidates_preview.csv"),
                    str(out_dir / "customer_feedback_rewrite_candidates_preview.csv"),
                    str(out_dir / "customer_feedback_ticket_or_handoff_preview.csv"),
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
