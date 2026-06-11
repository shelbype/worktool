from __future__ import annotations

import argparse
import csv
from pathlib import Path

import pandas as pd


AUDIENCE_LABELS = {
    "student": "学生库",
    "teacher": "老师库",
    "principal": "校长库",
    "academic": "教务库",
    "sales": "销售库",
}

HIGH_PRIORITY_CATEGORIES = [
    "账号登录/密码/手机号",
    "作业/布置/批改/反馈",
    "音频/录音/听力",
    "浏览器/网络/缓存",
    "班级/排课/课时/考勤",
    "权限/角色/公池",
]

LOW_VALUE_ANSWER_PATTERNS = [
    "未使用谷歌浏览器",
    "建议使用谷歌浏览器",
    "网络问题",
    "浏览器使用问题",
    "未复现",
    "已处理",
]

RISK_PATTERNS = [
    "合同",
    "退费",
    "退款",
    "发票",
    "报价",
    "赔偿",
    "收费",
    "删除",
    "恢复",
]


def read_candidates(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
    for column in ["audience", "port", "type", "question", "desc", "answer", "attachment", "categories"]:
        if column not in frame.columns:
            frame[column] = ""
    return frame


def score_row(row: pd.Series) -> int:
    text = " ".join([row["question"], row["desc"], row["answer"], row["categories"]])
    score = 0
    for index, category in enumerate(HIGH_PRIORITY_CATEGORIES):
        if category in text:
            score += 30 - index
    if row["audience"] in {"teacher", "student", "academic"}:
        score += 8
    if len(row["answer"]) >= 20:
        score += 6
    if row["attachment"]:
        score += 3
    if any(pattern in text for pattern in RISK_PATTERNS):
        score -= 50
    if any(pattern == row["answer"].strip() for pattern in LOW_VALUE_ANSWER_PATTERNS):
        score -= 10
    return score


def suggested_decision(row: pd.Series) -> str:
    text = " ".join([row["question"], row["desc"], row["answer"]])
    if any(pattern in text for pattern in RISK_PATTERNS):
        return "转人工/暂不入库"
    if any(pattern == row["answer"].strip() for pattern in LOW_VALUE_ANSWER_PATTERNS):
        return "改写后入库"
    if len(row["answer"]) < 12:
        return "改写后入库"
    return "建议入库"


def rewrite_hint(row: pd.Series) -> str:
    answer = row["answer"].strip()
    question = row["desc"].strip() or row["question"].strip()
    context = " ".join([row["question"], row["desc"], answer])
    answer_lower = answer.lower()
    if "没有加入班级" in answer or "未加入班级" in answer:
        return "老师，这种情况通常是学生还没有加入对应班级。您先把学生加入到要布置作业的班级里，再让学生端刷新或重新登录查看。"
    if "只布置给了班级里另一个学生" in answer or "没有选择布置给这个学生" in answer:
        return "老师，先检查作业的布置对象是否勾选了这个学生。当前更像是作业只布置给了其他学生，重新选择该学生后再补发布即可。"
    if "非vip" in answer_lower or "vip账号" in answer_lower:
        return "老师，题库类作业需要学生账号是 VIP 才能完成。如果学生不是 VIP，学生端可能看不到或无法进入作业，需要先确认学生账号权限。"
    if "学生登录的系统和老师不是同一个" in answer or ("系统" in answer and "不是同一个" in answer):
        return "老师，先确认学生登录的系统和老师布置作业的系统是否一致。如果登录到了其他系统或环境，学生端就看不到对应作业。"
    if "公众号需要取消绑定" in answer:
        return "老师，如果学生账号信息换过，公众号需要先取消绑定之前的学生，再让新学生重新绑定，这样通知才会发到正确账号。"
    if "身份数据缓存" in answer or "登陆过员工账号" in answer or "登录过员工账号" in answer:
        return "老师，这种情况一般是浏览器里保留了员工账号的身份缓存。可以先退出账号，清理浏览器缓存后，再用学生账号重新登录测试。"
    if "数据运营板块" in answer:
        return "老师，每月总课时可以在数据运营板块查看。如果教务账号看不到，需要到员工管理里确认是否开通了对应权限。"
    if "老师端首页待反馈只显示老师自己的课程" in answer:
        return "老师，老师端首页的待反馈只显示该老师自己的课程；如果要查看班级全部课程，可以用助教端或有对应权限的账号查看。"
    if "销售的身份" in answer and "教务的身份" in answer:
        return "老师，可以给该员工同时配置销售和教务身份，只勾选公池和查看入学模考相关权限，这样能批改公池学生的入学模考，同时避免看到不需要展示的联系方式。"
    if "作业" in context and any(pattern in context for pattern in ["看不到", "没出现", "没能看见", "查收不到"]):
        return "老师，您可以先检查三点：学生是否在对应班级里、作业布置对象是否包含该学生、学生账号是否有做题权限。确认后让学生端刷新或重新登录再看。"
    if "音频" in question or "听力" in question or "录音" in question:
        return "老师，您可以先让学生使用 Chrome 浏览器重新进入，并刷新页面或清理缓存。如果音频超过 15 秒仍未加载，可按页面提示下载音频本地播放；仍不行的话，再提供学生账号、测试链接和截图转人工排查。"
    if "谷歌浏览器" in answer:
        return "老师，这类情况通常和浏览器兼容性有关，建议学生优先使用 Chrome 浏览器重新进入；如果仍异常，再清理缓存、更换网络后重试。"
    if "权限" in question or "公池" in question:
        return "老师，这个一般和账号角色或权限有关。您可以先确认当前账号是否有对应功能权限；如果需要让其他角色查看，需要在权限配置里开通对应模块。"
    if "作业" in question:
        return "老师，您可以先确认作业是否已经成功布置、学生是否在对应班级内，以及作业状态是否已提交/已完成；如果状态正常但仍看不到，再提供学生账号和作业链接转人工排查。"
    if "班级" in question or "课时" in question or "转班" in question:
        return "老师，您可以先检查班级课时、学生所在班级和转入班级配置是否完整；如果提示无剩余课时，通常需要先确认目标班级是否设置了总课时。"
    return answer


def build_batch(input_path: Path, output_dir: Path, limit: int) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    frame = read_candidates(input_path)
    frame["score"] = frame.apply(score_row, axis=1)
    frame["suggested_decision"] = frame.apply(suggested_decision, axis=1)
    frame["rewrite_hint"] = frame.apply(rewrite_hint, axis=1)
    frame["audience_label"] = frame["audience"].map(AUDIENCE_LABELS).fillna(frame["audience"])
    frame = frame.sort_values(["score", "audience"], ascending=[False, True]).head(limit).copy()
    frame.insert(0, "review_id", [f"fb-review-{index:03d}" for index in range(1, len(frame) + 1)])
    frame["human_decision"] = ""
    frame["review_note"] = ""

    csv_path = output_dir / "customer_feedback_review_batch_001.csv"
    columns = [
        "review_id",
        "suggested_decision",
        "human_decision",
        "audience",
        "audience_label",
        "port",
        "type",
        "question",
        "desc",
        "answer",
        "rewrite_hint",
        "attachment",
        "categories",
        "score",
        "review_note",
    ]
    frame[columns].to_csv(csv_path, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_MINIMAL)

    md_path = output_dir / "customer_feedback_review_batch_001.md"
    lines = [
        "# 客户反馈审核批次 001",
        "",
        "审核规则：",
        "",
        "- `建议入库`：问题和答案相对通用，可审核后进入五类知识库。",
        "- `改写后入库`：答案过短或太像内部记录，需要改成客服话术。",
        "- `转人工/暂不入库`：涉及风险、个案、工单或不适合自动回复。",
        "",
        "建议先审核前 30 条，高频问题优先入库。",
        "",
    ]
    for _, row in frame.head(30).iterrows():
        lines.extend(
            [
                f"## {row['review_id']} | {row['suggested_decision']} | {row['audience_label']}",
                "",
                f"- 问题：{row['question']}",
                f"- 描述：{row['desc']}",
                f"- 原回答：{row['answer']}",
                f"- 建议改写：{row['rewrite_hint']}",
                f"- 附件：{row['attachment'] or '无'}",
                "",
            ]
        )
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return csv_path, md_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="analysis/customer_feedback_kb_candidates_preview.csv")
    parser.add_argument("--output-dir", default="analysis")
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()
    csv_path, md_path = build_batch(Path(args.input), Path(args.output_dir), args.limit)
    print(f"wrote {csv_path}")
    print(f"wrote {md_path}")


if __name__ == "__main__":
    main()
