from __future__ import annotations

import re
from functools import lru_cache
from typing import Any

from ragbot.domain import RetrievalResult
from ragbot.quality_config import load_json_config, string_list
from ragbot.text_utils import normalize_customer_text


def has_fast_answer_template(question: str) -> bool:
    return _template_answer(normalize_customer_text(question)) is not None


def build_fast_image_answer(retrieval: RetrievalResult, max_chars: int = 700) -> str:
    question = normalize_customer_text(retrieval.query)
    template = _template_answer(question)
    if template:
        return _with_image_note(template, retrieval)

    snippets = _select_relevant_snippets(retrieval)
    if not snippets:
        return "老师，这个问题我先帮您转人工确认一下。"

    answer = "老师，您可以先按这几步看下：\n\n" + "\n".join(
        f"{index}. {snippet}" for index, snippet in enumerate(snippets, start=1)
    )
    if len(answer) > max_chars:
        answer = answer[:max_chars].rstrip(" ，,。") + "。"
    return _with_image_note(answer, retrieval)


def _template_answer(question: str) -> str | None:
    configured_answer = _configured_template_answer(question)
    if configured_answer:
        return configured_answer
    if "班级" in question and "排课" in question:
        return (
            "老师，班级建好后可以这样排课：\n\n"
            "1. 先确认班级已经创建，并且学生已经分到班级里。\n"
            "2. 到【员工管理】确认老师账号已添加，并且设置了老师身份。\n"
            "3. 回到班级创建或编辑页面，把负责老师选上。\n"
            "4. 进入班级里的排课入口，按实际情况选择智能排课、传统排课或常用时间段排课。\n"
            "5. 排好后，可以在课表页按老师、班级或时间维度查看。"
        )
    if "班级" in question and any(word in question for word in ("新建", "创建", "新增", "建班")):
        return (
            "老师，新建班级可以按这几步来：\n\n"
            "1. 先确认对应课程已经创建好。\n"
            "2. 进入左侧导航【班级】或【班级管理】，点击【创建班级】。\n"
            "3. 填写班级信息：所属课程、班级类型、班级名称、老师/助教、开班日期、课时等。\n"
            "4. 如果是一对一班级，需要手动填写班级名称；一对多班级系统会自动匹配学期和班级名称。\n"
            "5. 创建完成后，进入班级选择学生，点击【添加】，把学员加入班级。\n\n"
            "如果后面还要排课，记得先在【员工管理】添加老师，并在建班时选好老师。"
        )
    if "班级" in question and "老师" in question and any(word in question for word in ("选不到", "选择不到", "找不到", "没有")):
        return (
            "老师，班级里选不到老师时，通常先看这几项：\n\n"
            "1. 到【员工管理】确认老师账号已经创建。\n"
            "2. 检查这个员工是否勾选了老师身份，或是否有老师相关权限。\n"
            "3. 再回到班级创建/编辑页面，在老师或助教字段重新选择。\n"
            "4. 如果是刚新增的老师，可以刷新页面或重新进入班级编辑页再试。\n\n"
            "如果这些都没问题还选不到，就需要人工帮您看下账号角色配置。"
        )
    if any(word in question for word in ("学员", "学生")) and any(word in question for word in ("忘记密码", "重置密码", "改密码")):
        return (
            "老师，学员忘记密码可以这样处理：\n\n"
            "1. 学员可在登录页点击【忘记密码】，按页面提示自行重置。\n"
            "2. 教务或校长也可以在后台进入【学员管理】找到对应学员。\n"
            "3. 进入学员编辑页后，按页面提供的密码项进行重置或修改。\n"
            "4. 修改时注意区分学员密码和家长密码，避免改错账号。"
        )
    if "课表" in question and any(word in question for word in ("导出", "下载", "打印")):
        return (
            "老师，课表导出可以这样操作：\n\n"
            "1. 进入【课表】或【课表管理】页面。\n"
            "2. 按课程、班级、老师、助教、课程状态或时间筛选需要的数据。\n"
            "3. 确认筛选结果无误后，点击页面里的【导出】。\n"
            "4. 如果在视图模式下查看，也可以按老师视图、班级视图、时间视图或教室视图导出。"
        )
    if (
        "员工" in question and ("老师" in question or "身份" in question or "角色" in question)
    ) or "老师账号" in question or "新增老师" in question:
        return (
            "老师，添加员工并设置老师身份可以按这个流程：\n\n"
            "1. 进入【员工管理】，先创建员工账号。\n"
            "2. 填写员工姓名、手机号等基础信息，登录密码可自定义；不填时通常默认手机号后六位。\n"
            "3. 在角色或权限设置里勾选【老师】身份。\n"
            "4. 如果需要，也可以继续配置下属、权限范围等信息。\n\n"
            "注意有些角色存在权限冲突，不能同时勾选。"
        )
    if "设备" in question and ("平台" in question or "要求" in question or "浏览器" in question):
        return (
            "老师，校校系统对设备和浏览器的要求是这样的：\n\n"
            "1. 电脑端（Mac/Windows）：请使用 Google Chrome 浏览器。\n"
            "2. iPad：请使用系统自带的 Safari 浏览器。\n"
            "3. Chrome 下载地址：https://www.google.cn/chrome/\n\n"
            "建议按上面的浏览器访问，这样可以减少页面兼容或功能显示异常。"
        )
    if "学员管理" in question or ("学员" in question and "哪里" in question):
        return (
            "老师，学员相关信息一般在【学员管理】里处理：\n\n"
            "1. 进入后台左侧导航，找到【学员】或【学员管理】。\n"
            "2. 可以按姓名、手机号、课程状态等条件搜索学员。\n"
            "3. 进入学员详情后，可以查看基础信息、课程、订单、作业和学习记录。\n"
            "4. 如果是新增学员，先创建学员账号，再根据需要报课或分班。"
        )
    if "员工" in question and ("端口" in question or "权限" in question):
        return (
            "老师，员工端口和权限建议这样确认：\n\n"
            "1. 先进入【员工管理】，找到对应员工账号。\n"
            "2. 查看员工绑定的角色、端口和权限范围。\n"
            "3. 如果员工看不到某个功能，优先检查角色是否包含对应端口权限。\n"
            "4. 修改后让员工刷新页面或重新登录再试。"
        )
    if "消息通知" in question or ("通知" in question and "收到" in question):
        return (
            "老师，如果想更快收到消息通知，可以先这样检查：\n\n"
            "1. 确认系统里的消息通知开关已经开启。\n"
            "2. 检查企业微信、微信或小程序端是否允许通知。\n"
            "3. 手机系统层面也要允许应用通知，不要开启免打扰或后台限制。\n"
            "4. 如果仍然收不到，可以让人工帮您看下账号和通知配置。"
        )
    if "客户端" in question and any(word in question for word in ("下载", "安装", "说明")):
        return (
            "老师，客户端下载可以按设备类型选择：\n\n"
            "1. Windows 电脑请查看 Windows 校校客户端下载安装说明。\n"
            "2. Mac 电脑请查看 MacOS 校校客户端下载安装说明。\n"
            "3. 安装后按页面提示登录校校账号。\n"
            "4. 如果安装时报错，把报错截图发群里，我们再帮您确认。"
        )
    if "课程" in question and any(word in question for word in ("创建", "新建", "新增", "管理")):
        return (
            "老师，创建课程可以按这个流程：\n\n"
            "1. 进入【课程】或【课程管理】页面。\n"
            "2. 点击【创建课程】或【新增课程】。\n"
            "3. 填写课程名称、课程类型、课时等基础信息。\n"
            "4. 保存后，再根据需要创建班级、安排老师和添加学员。"
        )
    if "考勤" in question:
        return (
            "老师，考勤功能一般这样使用：\n\n"
            "1. 先确认课程和课表已经安排好。\n"
            "2. 到【考勤】或对应课次页面查看待考勤课程。\n"
            "3. 按学生实际到课情况记录出勤、请假、缺勤等状态。\n"
            "4. 保存后可在考勤记录或数据统计里查看结果。"
        )
    if "布置作业" in question or ("作业" in question and "发布" in question):
        return (
            "老师，布置作业可以这样操作：\n\n"
            "1. 进入老师端或后台的【作业】相关页面。\n"
            "2. 选择要布置的班级、学员或课程。\n"
            "3. 选择题目、作业大纲或常用作业内容。\n"
            "4. 设置提交时间等要求后发布。\n\n"
            "如果班级还没排课，部分作业场景可能需要先完成班级或课次安排。"
        )
    if "无法加载" in question:
        return (
            "老师，学生端内容无法加载时可以先排查这几项：\n\n"
            "1. 让学生刷新页面，或退出后重新进入。\n"
            "2. 检查当前网络是否稳定，必要时切换网络再试。\n"
            "3. 如果是音频、作业或测试内容无法加载，建议更换浏览器或设备测试。\n"
            "4. 仍然异常的话，把学生账号、作业/测试名称和截图发群里，人工帮您继续查。"
        )
    if "无法提交" in question or "提交不了" in question:
        return (
            "老师，学生测试提交不了时可以先这样处理：\n\n"
            "1. 先确认网络正常，不要重复刷新或关闭页面。\n"
            "2. 让学生尝试重新点击提交，观察是否有报错提示。\n"
            "3. 记录学生账号、测试名称、提交时间和页面截图。\n"
            "4. 如果仍提交失败，发到群里让人工帮您查具体记录。"
        )
    if "题库" in question and any(word in question for word in ("录题", "创建", "上传", "使用")):
        return (
            "老师，机构题库录题可以按这个思路处理：\n\n"
            "1. 进入【题库】或【机构题库】页面。\n"
            "2. 选择题型和对应分类，再新增题目。\n"
            "3. 按页面要求录入题干、选项、答案和解析。\n"
            "4. 保存后可以用于组卷、布置作业或模考。"
        )
    if "销售线索" in question or ("线索" in question and "协作" in question):
        return (
            "老师，销售线索协作一般这样处理：\n\n"
            "1. 先把线索录入到潜客、公池或销售线索模块。\n"
            "2. 按校区、来源、顾问等条件分配或跟进。\n"
            "3. 跟进过程中及时记录沟通内容和下一步计划。\n"
            "4. 需要多人协作时，按系统里的协作或分配规则处理。"
        )
    return None


def _configured_template_answer(question: str) -> str | None:
    for template in _configured_templates():
        if _matches_template(question, template):
            answer = str(template.get("answer", "")).strip()
            if answer:
                return answer
    return None


@lru_cache(maxsize=1)
def _configured_templates() -> list[dict[str, Any]]:
    templates = load_json_config("config/fast_answer_templates.json", [])
    return [template for template in templates if isinstance(template, dict)]


def _matches_template(question: str, template: dict[str, Any]) -> bool:
    match_all = string_list(template.get("match_all"))
    match_any = string_list(template.get("match_any"))
    match_any_2 = string_list(template.get("match_any_2"))
    match_none = string_list(template.get("match_none"))
    if match_all and not all(word in question for word in match_all):
        return False
    if match_any and not any(word in question for word in match_any):
        return False
    if match_any_2 and not any(word in question for word in match_any_2):
        return False
    if match_none and any(word in question for word in match_none):
        return False
    return bool(match_all or match_any or match_any_2)


def _with_image_note(answer: str, retrieval: RetrievalResult) -> str:
    if any(hit.chunk.image_refs for hit in retrieval.hits):
        return answer.rstrip() + "\n\n我把相关截图也发您，方便对照操作。"
    return answer.rstrip()


def _select_relevant_snippets(retrieval: RetrievalResult, limit: int = 4) -> list[str]:
    query_tokens = _tokens(normalize_customer_text(retrieval.query))
    ranked: list[tuple[float, int, str]] = []
    order = 0
    for hit_index, hit in enumerate(retrieval.hits[:3]):
        for line in _clean_context_lines(hit.chunk.content, hit.chunk.title):
            order += 1
            score = _line_score(query_tokens, line) + max(0.0, hit.rerank_score) * 0.2
            if hit_index == 0:
                score += 0.1
            if score <= 0.1:
                continue
            ranked.append((score, order, line))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    snippets: list[str] = []
    seen: set[str] = set()
    for _, _, line in ranked:
        key = re.sub(r"\W+", "", line)
        if not key or key in seen:
            continue
        seen.add(key)
        snippets.append(line)
        if len(snippets) >= limit:
            break
    return snippets


def _clean_context_lines(content: str, title: str) -> list[str]:
    content = re.sub(r"\[图片:[^\]]+\]", "\n", content)
    lines: list[str] = []
    for raw_line in re.split(r"[\n。；;]", content):
        line = re.sub(r"\s+", " ", raw_line).strip(" ，,。；;")
        if not line or line == title:
            continue
        if line.startswith(("图片说明：", "图片 OCR：", "关键词：")):
            continue
        if len(line) < 4:
            continue
        lines.append(line)
    return lines


def _line_score(query_tokens: set[str], line: str) -> float:
    if not query_tokens:
        return 0.0
    line_tokens = _tokens(line)
    if not line_tokens:
        return 0.0
    overlap = len(query_tokens & line_tokens) / max(1, len(query_tokens))
    action_boost = 0.15 if any(word in line for word in ("点击", "填写", "选择", "添加", "进入", "创建")) else 0.0
    return overlap + action_boost


def _tokens(text: str) -> set[str]:
    latin = re.findall(r"[a-zA-Z0-9_./-]+", text.lower())
    chinese = re.findall(r"[\u4e00-\u9fff]{2,}", text)
    chinese_terms: list[str] = []
    for word in chinese:
        chinese_terms.append(word)
        chinese_terms.extend(word[index : index + 2] for index in range(max(1, len(word) - 1)))
    return set(latin + chinese_terms)
