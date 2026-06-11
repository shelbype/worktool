# 服务器正式知识库导出

## 说明

- 数据来自 `db/init/osp_helpcenter_*.xls` 帮助中心导入源。
- 线上正式库的存储形态是 PostgreSQL + pgvector；本文件是按同一导入逻辑生成的 Markdown/CSV 可读快照。
- 每个 `chunk` 对应线上 `knowledge_chunks` 表的一条知识分块，并包含角色库路由信息。

## 汇总

- 文档数：141
- chunk 数：171
- chunk 图片引用数：1297
- embedding 维度：64

## 按角色库统计

- student(学生库)：126
- teacher(老师库)：124
- academic(教务库)：116
- principal(校长库)：60
- sales(销售库)：51

## 按分类统计

- 核心功能介绍：72
- 热门文章：39
- 初次使用指南：22
- 新功能上线：15
- 使用技巧：12
- 热门问题：11

## 知识明细

### chunk_bc416a723118c66a443f4bd047984e00 | 一分钟了解校校AI是什么？

- source_id：helpcenter:18
- document_id：doc_helpcenter_18
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2021-04-06T10:11:57
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2023041216170288120842951070846", "alt_text": "系统一体化", "ocr_text": null, "caption": "系统一体化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121617179003821476068013839", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121617403686612564747820146", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618024475896480828691057", "alt_text": "教务智能化", "ocr_text": null, "caption": "教务智能化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061710465954080439163973413", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618231074434811397154974", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618352786074557841360784", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618486095146855453206906", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618567101822686310745626", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619093559287528424683220", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619206385270902045566166", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619308083111370498797382", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}]

```text
一分钟了解校校AI是什么？
一分钟了解校校AI是什么？
欢迎使用校校AI！ 
校校AI作为国际教育行业可靠的技术合作伙伴，致力于将人工智能技术深度整合到教务、教学、升学和校区管理等教育关键环节，研发了AI教学助手小新，智能选排课、AI智能批改、AI辅助教学等一系列核心功能，是领先的一站式、个性化AI技术教学解决方案服务系统。通过整合招生转化、智能教务、海量题库、高效教学、家校互动、数据分析等多端联动，校校AI为国际学校和语培机构带来前所未有的便利与深刻变革，助力行业数字化转型，形成可持续增长的数字化资产，引领行业迈向更加美好的未来。
系统一体化
校校的系统一体化不仅将原本割裂的销售、教学、老师、学生、管理者系统深度整合，所有数据实时储存在云端，更通过人工智能技术为这一体化系统注入“智慧大脑”。
AI引擎能够自动分析整合后的多维度数据，为校长和管理者提供校区运营的全景洞察与智能预警，如自动识别潜在风险学员、预测班级出勤趋势等。每个角色在独立的操作页面中，都能获得AI辅助，例如老师可随时通过AI助手用自然语言查询班级学情，管理者可获取数据驱动的运营建议，真正实现从数据统一到智能决策的跨越，让一体化系统成为教育机构数字化转型的核心引擎。
[图片: 系统一体化]
销售工作数据化
使用校校AI系统，所有的学员都会记录在系统中。通过在线的入学摸底测试，可以清楚地展现学员的真实水平、距离目标的差距、需要改进的学习方向等。课程顾问在跟进的过程中，所有的信息都会记录在CRM系统中，方便可视化、量化地进行跟踪。系统还支持线上电子签约并生成电子合同。
[图片: 销售工作数据化]
顾问老师可随时管理自己的订单及详情，缴费记录、退费管理、查看订单审批进度等一目了然。
[图片: 销售工作数据化]
当潜客付费成为正式学员之后，课程顾问也可以根据系统的记录，清晰地跟踪到学员的学习情况，包括作业的完成分析、课堂的反馈等，大大提高了内部沟通的效率，并且做到真正的全生命周期的服务，对学生的负责，能够提升教学质量和口碑，带来更多的转介绍。
教务智能化

图片说明：系统一体化
图片说明：销售工作数据化
图片说明：销售工作数据化
图片说明：教务智能化
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：校区管理数字化
图片说明：校区管理数字化
图片说明：办公学习移动化
图片说明：办公学习移动化
图片说明：办公学习移动化
```

### chunk_9a922e83979ad688a297d02e13c4bb7b | 一分钟了解校校AI是什么？

- source_id：helpcenter:18
- document_id：doc_helpcenter_18
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：1
- 状态：active
- 更新时间：2021-04-06T10:11:57
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2023041216170288120842951070846", "alt_text": "系统一体化", "ocr_text": null, "caption": "系统一体化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121617179003821476068013839", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121617403686612564747820146", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618024475896480828691057", "alt_text": "教务智能化", "ocr_text": null, "caption": "教务智能化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061710465954080439163973413", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618231074434811397154974", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618352786074557841360784", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618486095146855453206906", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618567101822686310745626", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619093559287528424683220", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619206385270902045566166", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619308083111370498797382", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}]

```text
教务的数据化智能化管理将会把教务工作者从繁重的、耗时的排课过程中解放出来。通过AI智能排课算法，综合考虑教师时间、教室资源、班级需求、课程规则等多重因素，自动生成最优课表，并支持智能调课、冲突检测，减少教务人员90%以上的工作时长。同时，教务人员通过系统对学员进行数据化量化管理，避免了学员信息更新不及时，所有信息实时同步，并且整合微信公众号，通过公众号对老师、学员进行课程信息通知。
[图片: 教务智能化]
AI教学助手与自适应练习
校校为老师配备了强大的AI教学助手，彻底改变了传统的教学方式。老师只需通过自然语言提问，例如“这个班最近出勤怎么样？”“有哪些学生作业完成率下滑？”等，AI助手便能实时分析班级多维度数据，快速给出精准结论、数据证据和行动建议，帮助老师第一时间掌握学情、定位风险学生，并提供针对性的处理建议。这让老师从繁琐的数据整理中解放出来，将更多精力聚焦于教学本身。
[图片: AI教学助手与自适应练习]
在练习环节，校校实现了自适应练习与AI智能批改的深度融合。系统会根据学生的训练情况，自动生成知识图谱，精准诊断每个学生的薄弱知识点，并智能推送相匹配的题目，实现真正的个性化学习。
[图片: AI教学助手与自适应练习]
同时，学生完成口语练习或写作后，AI口语写作智能批改功能立即启动，自动进行评分、纠错和详细反馈，提供改进建议和范例。老师无需逐一批改，即可通过系统查看全班学生的练习情况与共性问题，从而更有针对性地进行课堂辅导。这一整套AI驱动的教学与练习闭环，不仅减轻了老师负担，更大幅提升了学生的学习效率与效果。
[图片: AI教学助手与自适应练习]
校区管理数字化
校区销售、运营、教务、财务等数据的可视化，各类数据明细的统计分析，将使教育行业管理者清晰全面掌握校区运营现状，为校区运营的科学决策提供强有力的数字依据。
[图片: 校区管理数字化]
校校系统为机构管理者提供全方位数字化运营管理体验，销售、教务、教学、财务收支数据同步实时更新，电脑端、手机小程序、公众号多端口查看，大大节约沟通成本，及时清晰地发现问题，科学精准提高运营效率。

图片说明：系统一体化
图片说明：销售工作数据化
图片说明：销售工作数据化
图片说明：教务智能化
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：校区管理数字化
图片说明：校区管理数字化
图片说明：办公学习移动化
图片说明：办公学习移动化
图片说明：办公学习移动化
```

### chunk_25a5dbc52ec12fa9af17dcaa46fbcf5f | 一分钟了解校校AI是什么？

- source_id：helpcenter:18
- document_id：doc_helpcenter_18
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：2
- 状态：active
- 更新时间：2021-04-06T10:11:57
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2023041216170288120842951070846", "alt_text": "系统一体化", "ocr_text": null, "caption": "系统一体化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121617179003821476068013839", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121617403686612564747820146", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618024475896480828691057", "alt_text": "教务智能化", "ocr_text": null, "caption": "教务智能化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061710465954080439163973413", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618231074434811397154974", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618352786074557841360784", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618486095146855453206906", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121618567101822686310745626", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619093559287528424683220", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619206385270902045566166", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121619308083111370498797382", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}]

```text
[图片: 校区管理数字化]
办公学习移动化
电脑端、小程序、公众号多端联动，随时随地，移动化高效办公学习！
[图片: 办公学习移动化]
微信公众号多场景下的消息通知，实现了各角色之间的高效沟通，如新增潜客通知、潜客跟进通知、新学员入学通知、上课通知、布置新作业通知、完成作业通知、作业过期提醒、工作日报等。
[图片: 办公学习移动化]
微信小程序为校长、销售、老师、学生以及家长等提供了高效便捷的移动化办公媒介，通过小程序实现学员跟进，作业布置，作业检查，作业完成，家长监督，校区数字化管理等。
[图片: 办公学习移动化]
关键词：专家、专注、产品、人工智能、信息、创立、创造、副教授、原、名师、团队、壁垒、工程学院、巴巴、并从、总监、成立、成都、提高、收益、数字化、新东方、机构、校校、百度、联合、行业、解决、资深、运营、阿里

图片说明：系统一体化
图片说明：销售工作数据化
图片说明：销售工作数据化
图片说明：教务智能化
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：校区管理数字化
图片说明：校区管理数字化
图片说明：办公学习移动化
图片说明：办公学习移动化
图片说明：办公学习移动化
```

### chunk_35ad3e98559a36a9c79481267e08616e | 一分钟了解校校AI是什么？

- source_id：helpcenter:82
- document_id：doc_helpcenter_82
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T16:13:03
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608235361519039587858371", "alt_text": "系统一体化", "ocr_text": null, "caption": "系统一体化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608405445774225869474729", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608538251015252640372569", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609223720749451558795777", "alt_text": "教务智能化", "ocr_text": null, "caption": "教务智能化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061814367094238395675573910", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609356015159477713942179", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609435931049834065293448", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609587047817472526272195", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121610073973465516196298620", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612397510651932854173709", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612516733055850629966138", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612597140270223496016097", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}]

```text
一分钟了解校校AI是什么？
一分钟了解校校AI是什么？
欢迎使用校校AI！ 
校校AI作为国际教育行业可靠的技术合作伙伴，致力于将人工智能技术深度整合到教务、教学、升学和校区管理等教育关键环节，研发了AI教学助手小新，智能选排课、AI智能批改、AI辅助教学等一系列核心功能，是领先的一站式、个性化AI技术教学解决方案服务系统。通过整合招生转化、智能教务、海量题库、高效教学、家校互动、数据分析等多端联动，校校AI为国际学校和语培机构带来前所未有的便利与深刻变革，助力行业数字化转型，形成可持续增长的数字化资产，引领行业迈向更加美好的未来。
系统一体化
校校的系统一体化不仅将原本割裂的销售、教学、老师、学生、管理者系统深度整合，所有数据实时储存在云端，更通过人工智能技术为这一体化系统注入“智慧大脑”。
AI引擎能够自动分析整合后的多维度数据，为校长和管理者提供校区运营的全景洞察与智能预警，如自动识别潜在风险学员、预测班级出勤趋势等。每个角色在独立的操作页面中，都能获得AI辅助，例如老师可随时通过AI助手用自然语言查询班级学情，管理者可获取数据驱动的运营建议，真正实现从数据统一到智能决策的跨越，让一体化系统成为教育机构数字化转型的核心引擎。
[图片: 系统一体化]
销售工作数据化
使用校校AI系统，所有的学员都会记录在系统中。通过在线的入学摸底测试，可以清楚地展现学员的真实水平、距离目标的差距、需要改进的学习方向等。课程顾问在跟进的过程中，所有的信息都会记录在CRM系统中，方便可视化、量化地进行跟踪。
[图片: 销售工作数据化]
系统还支持线上电子签约并生成电子合同。顾问老师可随时管理自己的订单及详情，缴费记录，退费管理，查看订单审批进度等一目了然。
[图片: 销售工作数据化]
当潜客付费成为正式学员之后，课程顾问也可以根据系统的记录，清晰地跟踪到学员的学习情况，包括作业的完成分析、课堂的反馈等，大大提高了内部沟通的效率，并且做到真正的全生命周期的服务，对学生的负责，能够提升教学质量和口碑，带来更多的转介绍。
教务智能化

图片说明：系统一体化
图片说明：销售工作数据化
图片说明：销售工作数据化
图片说明：教务智能化
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：校区管理数字化
图片说明：校区管理数字化
图片说明：办公学习移动化
图片说明：办公学习移动化
图片说明：办公学习移动化
```

### chunk_92383335141ff33654368386ce0254b3 | 一分钟了解校校AI是什么？

- source_id：helpcenter:82
- document_id：doc_helpcenter_82
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T16:13:03
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608235361519039587858371", "alt_text": "系统一体化", "ocr_text": null, "caption": "系统一体化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608405445774225869474729", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608538251015252640372569", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609223720749451558795777", "alt_text": "教务智能化", "ocr_text": null, "caption": "教务智能化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061814367094238395675573910", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609356015159477713942179", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609435931049834065293448", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609587047817472526272195", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121610073973465516196298620", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612397510651932854173709", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612516733055850629966138", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612597140270223496016097", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}]

```text
教务的数据化智能化管理将会把教务工作者从繁重的、耗时的排课过程中解放出来，通过算法，自动的将课程以最优的方式排好，减少教务人员90%以上的工作时长。同时，教务人员通过系统对学员进行数据化量化管理，避免了学员信息更新不及时，所有信息实时同步，并且整合微信公众号，通过公众号对老师，学员进行课程信息通知。
[图片: 教务智能化]
AI教学助手与自适应练习
校校为老师配备了强大的AI教学助手，彻底改变了传统的教学方式。老师只需通过自然语言提问，例如“这个班最近出勤怎么样？”“有哪些学生作业完成率下滑？”等，AI助手便能实时分析班级多维度数据，快速给出精准结论、数据证据和行动建议，帮助老师第一时间掌握学情、定位风险学生，并提供针对性的处理建议。这让老师从繁琐的数据整理中解放出来，将更多精力聚焦于教学本身。
[图片: AI教学助手与自适应练习]
教学过程的信息化和学生练习的自适应及自动化诊断，将有效的解决学生课后的练习及学习巩固，老师可以通过系统，查看到每一个学生的学习情况和老师的教学进展，老师并不需要花费课下的时间，就可以轻松的完成作业的安排！
[图片: AI教学助手与自适应练习]
同时，学生完成口语练习或写作后，AI口语写作智能批改功能立即启动，自动进行评分、纠错和详细反馈，提供改进建议和范例。老师无需逐一批改，即可通过系统查看全班学生的练习情况与共性问题，从而更有针对性地进行课堂辅导。这一整套AI驱动的教学与练习闭环，不仅减轻了老师负担，更大幅提升了学生的学习效率与效果。
[图片: AI教学助手与自适应练习]
校区管理数字化
校区销售、运营、教务、财务等数据的可视化，各类数据明细的统计分析，将使教育行业管理者清晰全面掌握校区运营现状，为校区运营的科学决策提供强有力的数字依据。
[图片: 校区管理数字化]
校校系统为机构管理者提供全方位数字化运营管理体验，销售、教务、教学、财务收支数据同步实时更新，电脑端、手机小程序、公众号多端口查看，大大节约沟通成本，及时清晰地发现问题，科学精准提高运营效率。
[图片: 校区管理数字化]
办公学习移动化

图片说明：系统一体化
图片说明：销售工作数据化
图片说明：销售工作数据化
图片说明：教务智能化
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：校区管理数字化
图片说明：校区管理数字化
图片说明：办公学习移动化
图片说明：办公学习移动化
图片说明：办公学习移动化
```

### chunk_d5e1200362d1dffd6ce76705747e5a0c | 一分钟了解校校AI是什么？

- source_id：helpcenter:82
- document_id：doc_helpcenter_82
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：2
- 状态：active
- 更新时间：2023-04-12T16:13:03
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608235361519039587858371", "alt_text": "系统一体化", "ocr_text": null, "caption": "系统一体化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608405445774225869474729", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121608538251015252640372569", "alt_text": "销售工作数据化", "ocr_text": null, "caption": "销售工作数据化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609223720749451558795777", "alt_text": "教务智能化", "ocr_text": null, "caption": "教务智能化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061814367094238395675573910", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609356015159477713942179", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609435931049834065293448", "alt_text": "AI教学助手与自适应练习", "ocr_text": null, "caption": "AI教学助手与自适应练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121609587047817472526272195", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121610073973465516196298620", "alt_text": "校区管理数字化", "ocr_text": null, "caption": "校区管理数字化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612397510651932854173709", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612516733055850629966138", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121612597140270223496016097", "alt_text": "办公学习移动化", "ocr_text": null, "caption": "办公学习移动化"}]

```text
电脑端、小程序、公众号多端联动，随时随地，移动化高效办公学习！
[图片: 办公学习移动化]
微信公众号多场景下的消息通知，实现了各角色之间的高效沟通，如新增潜客通知、潜客跟进通知、新学员入学通知、上课通知、布置新作业通知、完成作业通知、作业过期提醒、工作日报等。
[图片: 办公学习移动化]
微信小程序为校长、销售、老师、学生以及家长等提供了高效便捷的移动化办公媒介，通过小程序实现学员跟进，作业布置，作业检查，作业完成，家长监督，校区数字化管理等。
[图片: 办公学习移动化]

图片说明：系统一体化
图片说明：销售工作数据化
图片说明：销售工作数据化
图片说明：教务智能化
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：AI教学助手与自适应练习
图片说明：校区管理数字化
图片说明：校区管理数字化
图片说明：办公学习移动化
图片说明：办公学习移动化
图片说明：办公学习移动化
```

### chunk_fd68f23a91e114852415aa62af696d34 | 已经确认并转为正式学员的客户订单，还可以撤销或修改吗？

- source_id：helpcenter:158
- document_id：doc_helpcenter_158
- 分类：使用技巧
- 适用角色库：student(学生库);teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:11:38
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061009004559097612724793991", "alt_text": "订单回退", "ocr_text": null, "caption": "订单回退"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061009505080608468071234661", "alt_text": "订单修改或取消", "ocr_text": null, "caption": "订单修改或取消"}]

```text
已经确认并转为正式学员的客户订单，还可以撤销或修改吗？
已经确认并转为正式学员的客户订单，还可以撤销或修改吗？
系统支持订单的回退、修改和退费，您可以通过以下方式进行操作：
订单回退
销售主管/销售总监登录账号，在“订单审批”一栏中，找到需要“回退”的订单，点击“回退”，订单状态即可回归“待确认”，负责该客户的销售老师账号“我的订单”中，订单状态也会随之变化，由此，便可操作订单修改，取消等动作。
[图片: 订单回退]
订单修改或取消
“我的订单”中，待确认订单，均可点击“详情”查看订单，并操作修改、退费、取消订单。
[图片: 订单修改或取消]

图片说明：订单回退
图片说明：订单修改或取消
```

### chunk_86765681f494d74fdbcbc1b0a702a389 | 一文了解：快速玩转单词书

- source_id：helpcenter:185
- document_id：doc_helpcenter_185
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-18T16:17:02
- 图片数：15
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051024504455175787078128707", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051028503839688240599876833", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202305181417213960495645595652195", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051032215168257185509150874", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051032253960258318799565209", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051033377019420691198952767", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305103425647086857596650449", "alt_text": "布置单词书", "ocr_text": null, "caption": "布置单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051035396273013651410146681", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051035432990232382208728296", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305103605523362672309007738", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051037149064231367236507479", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051039035269058913461623386", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051039094529707984542780935", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051040245959912260473122103", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051040277652770540270193553", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}]

```text
一文了解：快速玩转单词书
一文了解：快速玩转单词书
词汇教学是英语教学的重要组成部分，词汇的掌握和运用是增强语言知识和培养语言技能的基础。
老师可以一键导入生成单词书，帮助学生系统性学习单词
自定义单词书
老师可以根据自己的教学任务上传机构独有的单词书。
第1步，导航栏选择题库，点击单词书，点击新增词表，下载系统给出的模版Excel表格
[图片: 自定义单词书]
[图片: 自定义单词书]
第2步，按照模版格式编辑好表格内容
注：
1. 每个sheet是一个单元，每个单元最多300个单词。
2. 一个单词一行，包含单词、音标、解释、例句、例句翻译。
3. 单词例句和例句解释多条用空白换行隔开。
4. 音标、解释、例句、例句翻译，未填写系统将自动匹配。
5. 系统未匹配到相关单词信息内容，可以手动对单词进行编辑。
[图片: 自定义单词书]
第3步，点击上传表格即可一键快速生成单词书
上传好的单词书内容老师可以选择手动调整，可修改单词、音标、解析并添加例句。
[图片: 自定义单词书]
[图片: 自定义单词书]
修改完成后，点击输入单词本标题、并选择科目，确认即可生成单词书！老师可根据上传时间、单元数、单词数、使用次数及正确率进行排序筛选，或点击右侧一键搜索单词书，更便捷！
[图片: 自定义单词书]
布置单词书
布置单词书，可以帮助老师实时掌握学生单词学习的进度，点击布置，可以自定义编辑词表名称和学习时间，快速布置到班级或单独下发给班级内的学生！
[图片: 布置单词书]
多种单词测试形式可选择，包含英译中、中译英、听音选择、看词选释义等，老师可以全方位制定单词学习任务，帮助学生针对性提高单词能力！可以设置该单元单词抽查的数量，还可以设置单词或测试是否限时
老师如何查看单词书学习情况
点击单词书【详情】可查看总体参与学生人数、测试形式、单词测试正确率、及完成率。
[图片: 老师如何查看单词书学习情况]
[图片: 老师如何查看单词书学习情况]
还可以根据参与学生列表查看单词书学习的单元词汇详情，老师可以实时掌握班级学生的单词学习进度！
[图片: 老师如何查看单词书学习情况]

图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：布置单词书
图片说明：老师如何查看单词书学习情况
图片说明：老师如何查看单词书学习情况
图片说明：老师如何查看单词书学习情况
图片说明：老师如何查看单词书学习情况
图片说明：已上传的单词书如何新增词表
图片说明：已上传的单词书如何新增词表
图片说明：已上传的单词书如何新增词表
图片说明：已上传的单词书如何新增词表
```

### chunk_b14596f0489c0b763e4e9e8fbd53298e | 一文了解：快速玩转单词书

- source_id：helpcenter:185
- document_id：doc_helpcenter_185
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-05-18T16:17:02
- 图片数：15
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051024504455175787078128707", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051028503839688240599876833", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202305181417213960495645595652195", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051032215168257185509150874", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051032253960258318799565209", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051033377019420691198952767", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305103425647086857596650449", "alt_text": "布置单词书", "ocr_text": null, "caption": "布置单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051035396273013651410146681", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051035432990232382208728296", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305103605523362672309007738", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051037149064231367236507479", "alt_text": "老师如何查看单词书学习情况", "ocr_text": null, "caption": "老师如何查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051039035269058913461623386", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051039094529707984542780935", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051040245959912260473122103", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051040277652770540270193553", "alt_text": "已上传的单词书如何新增词表", "ocr_text": null, "caption": "已上传的单词书如何新增词表"}]

```text
老师查看学生学习情况之后可以进行抽查。
点击展开列表-选中某一单元，可以点击抽查。
抽查可以选择班级、学生、测试形式、抽查个数，还可以限制时间。
[图片: 老师如何查看单词书学习情况]
已上传的单词书如何新增词表
单词书词表上传后可以再添加新词表，操作更便捷！
老师可以选择需要添加的单词书，点击【详情】
[图片: 已上传的单词书如何新增词表]
点击【新增单元】，就可以上传新的单元，上传后的新单元会自动同步到已布置的单词书中。
[图片: 已上传的单词书如何新增词表]
点击单词，可以修改单词，修改后系统会自动匹配音标、解析、例句。
也可以单独修改音标、解析、例句
[图片: 已上传的单词书如何新增词表]
[图片: 已上传的单词书如何新增词表]

图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：布置单词书
图片说明：老师如何查看单词书学习情况
图片说明：老师如何查看单词书学习情况
图片说明：老师如何查看单词书学习情况
图片说明：老师如何查看单词书学习情况
图片说明：已上传的单词书如何新增词表
图片说明：已上传的单词书如何新增词表
图片说明：已上传的单词书如何新增词表
图片说明：已上传的单词书如何新增词表
```

### chunk_f8d7d80a28514192132e70907ed5a0bb | 开年重磅｜让AI马上成为老师真正的教学工作助手！

- source_id：helpcenter:246
- document_id：doc_helpcenter_246
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2026-03-04T16:09:53
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051133211949959437864496575", "alt_text": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控", "ocr_text": null, "caption": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051136025952833198668895697", "alt_text": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控", "ocr_text": null, "caption": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041545237321981630407038034", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041606366958500475414117678", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051140331261643115736977405", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051143572122399637819219146", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051154088955707143167319430", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051154143504263744151018886", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051154228832425139913401962", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}]

```text
开年重磅｜让AI马上成为老师真正的教学工作助手！
开年重磅｜让AI马上成为老师真正的教学工作助手！
在你为赶晨会、盯作业、看成绩、写周报的日夜里。在你为担心学生状态、反复核对数据、害怕遗漏教学细节的日夜里
校校的AI能力也在悄悄进化，准备好了吗，校校Enterprise系统 AI小新助手正式上线
让 AI，成为老师真正的教学工作助手
小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控
学生、作业、成绩、出勤，一个 AI，统一提醒所有教学待办。
[图片: 小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控]
把系统【新功能提示】交给小新AI，系统更新，小新先告诉你，每一次能力升级，都不会被错过。
[图片: 小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控]
小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
在小新的对话框里，老师可以像和同事、助教、教研搭档，一样自由提问。AI 会自动理解你的问题，给出结论 + 依据 + 可行动建议。
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]
快速了解「我现在教得怎么样」这是老师最常问、但最难自己算清楚的事。
你可以这样问
「我最近一周布置的作业，完成率怎么样？」
「有没有作业我布置了，但还没来得及批改？」
AI 会直接告诉你
作业完成率、查阅率、批改状态的整体结论
哪些作业完成得最好 / 最差
 适合用在：
 周中复盘、教学自检、准备汇报前
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]
一眼看清「学生现在是什么状态」不用翻学生列表，也不用逐个点。
你可以这样问
「最近一周班级出勤情况怎么样？」
「有没有学生最近出勤突然变差？」
AI 会直接告诉你
班级整体状态是稳定还是下滑
哪些学生需要你重点关注
是个别问题，还是整体趋势
适合用在：
 晨会前、上课前、日常管理

图片说明：小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控
图片说明：小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
```

### chunk_c170eac89972863baeecdda528db788f | 开年重磅｜让AI马上成为老师真正的教学工作助手！

- source_id：helpcenter:246
- document_id：doc_helpcenter_246
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2026-03-04T16:09:53
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051133211949959437864496575", "alt_text": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控", "ocr_text": null, "caption": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051136025952833198668895697", "alt_text": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控", "ocr_text": null, "caption": "小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041545237321981630407038034", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041606366958500475414117678", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051140331261643115736977405", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051143572122399637819219146", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051154088955707143167319430", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051154143504263744151018886", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051154228832425139913401962", "alt_text": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？", "ocr_text": null, "caption": "小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？"}]

```text
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]
不止分析，还告诉你「下一步该做什么」这是老师最想要、也最省心的一类问题。
你可以直接问
「我现在最应该关注哪几个学生？」
「这个学生更适合补基础，还是刷题？」
AI 会给你
按优先级排序的建议
对应的教学 / 沟通 / 作业策略参考
适合用在：
 行动决策、学生干预、教学安排
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]
[图片: 小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？]

图片说明：小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控
图片说明：小新AI提示上新【待办提示】功能，统一整合教学待办，让教学管理更清晰、更可控
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
图片说明：小新AI助手 【自由提问】功能，可以帮老师解决哪些教学问题？
```

### chunk_ab28b9b88480bc7d3c58509cd3a84cb2 | Windows校校客户端下载安装说明书

- source_id：helpcenter:250
- document_id：doc_helpcenter_250
- 分类：热门问题
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2026-05-28T18:37:46
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/9af1/202605281830167719844172375256343", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/185e/202605281830452403620673781473528", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/f733/202605281831008117793688608552335", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/bdfa/202605281831267264698475365945036", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/ad0d/202605281831302700957128748857038", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/d6cc/202605281831516922876892259825801", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/3d8e/202605281832418479526802100876629", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/c4a7/202605281836328432841168780595574", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/03cf/202605281837244657910119442819513", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/c428/20260528183743171439075958894831", "alt_text": "Windows校校客户端下载安装", "ocr_text": null, "caption": "Windows校校客户端下载安装"}]

```text
Windows校校客户端下载安装说明书
Windows校校客户端下载安装说明书
校校系统桌面客户端全新上线，相比网页版，不仅严格遵循，国家数据安全等级保护三级标准，保护学生和老师的学习数据安全无忧，还带来了更顺畅的学习体验！
Windows校校客户端下载安装
Step1：打开系统网址登录页，Windows系统点击 Windows版本，下载客户端安装文件
[图片: Windows校校客户端下载安装]
Step2：下载成功后，点击右上角，打开安装文件，双击打开。
[图片: Windows校校客户端下载安装]
[图片: Windows校校客户端下载安装]
Step3：点击“更多信息”，选择“仍要运行”
注：该提示为Windows系统对新发布的、还没有被大量用户下载过的软件的一种常见保护机制。校校客户端系符合国家数据安全等级三级标准，当前软件已经通过代码签名（发行者显示为 Benben Information Tech Co., Ltd.），确保数据安全与隐私保护。
[图片: Windows校校客户端下载安装]
[图片: Windows校校客户端下载安装]
Step4：进入安装界面后，点击“安装”。
[图片: Windows校校客户端下载安装]
Step5：安装成功后，会弹窗次窗口，点击“是”。
[图片: Windows校校客户端下载安装]
Step6：安装完成后点击“完成”。
[图片: Windows校校客户端下载安装]
Step7：在网址栏输入网页端的登录网址。
[图片: Windows校校客户端下载安装]
Step8：输入账号密码即可登录校校客户端。
[图片: Windows校校客户端下载安装]

图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
图片说明：Windows校校客户端下载安装
```

### chunk_63b4810f916a1cda24ed9498f4d52c99 | 快速玩转企业微信！

- source_id：helpcenter:56
- document_id：doc_helpcenter_56
- 分类：初次使用指南
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T16:10:17
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304111752519197448014170000276", "alt_text": "系统与企业微信关联协同能带来哪些便捷操作？", "ocr_text": null, "caption": "系统与企业微信关联协同能带来哪些便捷操作？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304111807346292102810169697009", "alt_text": "系统与企业微信关联协同能带来哪些便捷操作？", "ocr_text": null, "caption": "系统与企业微信关联协同能带来哪些便捷操作？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304111807442570326927445991980", "alt_text": "系统与企业微信关联协同能带来哪些便捷操作？", "ocr_text": null, "caption": "系统与企业微信关联协同能带来哪些便捷操作？"}]

```text
快速玩转企业微信！
快速玩转企业微信！
企业微信，是微信团队专为企业打造的专业通讯工具。一如微信的熟悉体验，让工作与生活分开，助力企业高效办公。企业微信与校校系统的完美结合能为机构解决哪些问题？
企业微信有哪些核心功能？
1. 和微信一样易用，上手快
2. 连接微信
3. 统一的企业通讯录
4. 多平台同步使用
5. 集成多种通讯方式
系统与企业微信关联协同能带来哪些便捷操作？
老师/销售端连通企业微信，用熟悉的方式高效工作！
[图片: 系统与企业微信关联协同能带来哪些便捷操作？]
实时查看跟进详情进度，分享模考结果，添加沟通内容！
[图片: 系统与企业微信关联协同能带来哪些便捷操作？]
随时随地查看课表及课堂反馈！
[图片: 系统与企业微信关联协同能带来哪些便捷操作？]

图片说明：系统与企业微信关联协同能带来哪些便捷操作？
图片说明：系统与企业微信关联协同能带来哪些便捷操作？
图片说明：系统与企业微信关联协同能带来哪些便捷操作？
```

### chunk_2880406bcf4bfd3980d8e0d397636430 | 系统各端口权限说明

- source_id：helpcenter:76
- document_id：doc_helpcenter_76
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T15:03:16
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061110156098659911300038866", "alt_text": "校校系统需要后台操作的权限", "ocr_text": null, "caption": "校校系统需要后台操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061125523188762116875257230", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061126165116118356454465286", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306112934482944573552723556", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061130417434484791682871321", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061132153891928152791704192", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061133215829969830871019924", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061135177303490335389765054", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061135231854549998979974787", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061136347582166568470064231", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061137376485334907959733360", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061139211511013553382369085", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061139257904764582329047718", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061141305559673959648932482", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061142388353088731394020590", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061143338895567294235918438", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}]

```text
系统各端口权限说明
系统各端口权限说明
校校系统需要后台操作的权限
【入学模考的试题增加与隐藏】（针对系统内已有题库）
老师可以选择系统内的试题，自行组卷，内容+标题即可，比如剑17test1 passage1+剑16test3 passage2，命名“阅读专项模考一”告知客户经理，即可由后台教研部门推送至入学模考。
现有模考均可隐藏，单科目自定义模考上限为5套。
机构自有题库推送至入学模考能力测试中，没有套数限制。
[图片: 校校系统需要后台操作的权限]
【自有词表的上传】
老师可以通过Excel表格模板格式，编辑好需要上传的单词发送至校校系统服务群或客户经理，设置好词表命名，由教研部门上传至系统（模板由客户经理提供）。
【机构名称及二级域名的修改】
机构如果需要修改名称和二级域名，需要提供新名称以及域名至客户经理由技术后台操作修改。
【各科目的真题录入】
1、各科目的公开真题，系统免费录入。
2、各科目的独家真题，机构可以在自有题库里录入使用，如果需要教研后台录入至系统，需要收费，具体收费标准可以详询客户经理。
校校系统机构自行开放操作的权限
一、员工账号的建立及权限的设置，以及账号状态的启用及停用
校长、教务可以创建员工账号，可以进行权限的调整，管控账号的使用情况。
[图片: 校校系统机构自行开放操作的权限]
二：系统主页 LOGO、背景图片等功能相关权限的修改
校长、教务可以在导航栏-设置处修改主页的logo以及登陆页的背景图片，可以在设置里修改销售相关，教学相关的设置。
[图片: 校校系统机构自行开放操作的权限]
三、学生账号的开设，以及账号状态的停用及启用等操作
校长、教务可以创建学生账号，管控账号的使用情况。
[图片: 校校系统机构自行开放操作的权限]
四、机构课程体系的建设
课程名称的设置会关联在销售签约时的报名课程名称。
上课内容的设置会在班级内排课时显示，关联排课内容。
课程类型
1、班课：课程总价固定，课时总数固定。 
2、定制课：课时单价固定，可根据学员需求定制课程内容及课时数。
[图片: 校校系统机构自行开放操作的权限]

图片说明：校校系统需要后台操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
```

### chunk_034fcb21dc4ac354b226b79b27d0f6c3 | 系统各端口权限说明

- source_id：helpcenter:76
- document_id：doc_helpcenter_76
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T15:03:16
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061110156098659911300038866", "alt_text": "校校系统需要后台操作的权限", "ocr_text": null, "caption": "校校系统需要后台操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061125523188762116875257230", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061126165116118356454465286", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306112934482944573552723556", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061130417434484791682871321", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061132153891928152791704192", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061133215829969830871019924", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061135177303490335389765054", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061135231854549998979974787", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061136347582166568470064231", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061137376485334907959733360", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061139211511013553382369085", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061139257904764582329047718", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061141305559673959648932482", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061142388353088731394020590", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061143338895567294235918438", "alt_text": "校校系统机构自行开放操作的权限", "ocr_text": null, "caption": "校校系统机构自行开放操作的权限"}]

```text
[图片: 校校系统机构自行开放操作的权限]
五、班级的建设与排课
校长、教务可以创建班级，并给班级进行排课。
[图片: 校校系统机构自行开放操作的权限]
六、课表的查看与调整
校长、教务可以查看所有班级的课表，调整课表并进行导出。
[图片: 校校系统机构自行开放操作的权限]
[图片: 校校系统机构自行开放操作的权限]
七、学生课程考勤情况的查看与调整
校长、教务可以查看学生考勤情况，也可以进行手动修改.
[图片: 校校系统机构自行开放操作的权限]
八、作业的布置与批改
老师、助教可以进行学生作业的布置和批改。
[图片: 校校系统机构自行开放操作的权限]
九、系统题库的查看及机构名师讲解的上传
老师、助教可以查看系统题库，上传机构独有的名师讲解
[图片: 校校系统机构自行开放操作的权限]
[图片: 校校系统机构自行开放操作的权限]
十、自有题库的录入及推送至入学模考（针对系统内没有的题库）
老师可以在自有题库录入题目，可以在机构题库中给学生布置对应的作业，也可以推送至入学模考
[图片: 校校系统机构自行开放操作的权限]
十一、作业大纲的创建与设置
老师可以创建作业大纲，设置好题目，再关联到班级，可以一键下发给学生
[图片: 校校系统机构自行开放操作的权限]
十二、云盘文件的上传与下载
[图片: 校校系统机构自行开放操作的权限]

图片说明：校校系统需要后台操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
图片说明：校校系统机构自行开放操作的权限
```

### chunk_913aa3b4cf83fa903c0ce3e352ab0485 | 销售/课程顾问老师可以查看到自己客户的实时学习数据吗？

- source_id：helpcenter:159
- document_id：doc_helpcenter_159
- 分类：使用技巧
- 适用角色库：sales(销售库);principal(校长库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:15:15
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061016504313604626069922219", "alt_text": "具体操作方式如下图：", "ocr_text": null, "caption": "具体操作方式如下图："}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061017124463917665790528388", "alt_text": "具体操作方式如下图：", "ocr_text": null, "caption": "具体操作方式如下图："}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061017562713313990424140329", "alt_text": "具体操作方式如下图：", "ocr_text": null, "caption": "具体操作方式如下图："}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061018174512761178702484917", "alt_text": "具体操作方式如下图：", "ocr_text": null, "caption": "具体操作方式如下图："}]

```text
销售/课程顾问老师可以查看到自己客户的实时学习数据吗？
销售/课程顾问老师可以查看到自己客户的实时学习数据吗？
可以的，销售/课程顾问老师，可以在登录自己的销售账号，实时查看自己跟进的所有客户的学习情况，包括：课表&任务、课堂反馈、学习报告、练习情况等。
具体操作方式如下图：
点击左侧导航栏【学员】，即可查看自己跟进的学员列表，查找或搜索学员，即可查看到对应学员的学习信息。
[图片: 具体操作方式如下图：]
销售可以在课表查看学生目前的课程、任务安排，如果学生有多个班级，可以进行筛选查看。
[图片: 具体操作方式如下图：]
学习报告可以查看老师给学生生成的学习报告，可以按科目、时间、生成人进行筛选。
[图片: 具体操作方式如下图：]
练习统计下可以查看学生的作业练习统计、错题分析、以及笔记
[图片: 具体操作方式如下图：]

图片说明：具体操作方式如下图：
图片说明：具体操作方式如下图：
图片说明：具体操作方式如下图：
图片说明：具体操作方式如下图：
```

### chunk_13344137082d6e2f9a12ee0aa4ac37fb | 一文了解：机构题库快捷录题

- source_id：helpcenter:180
- document_id：doc_helpcenter_180
- 分类：核心功能介绍
- 适用角色库：teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-27T17:54:59
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051126015097320690797606380", "alt_text": "文档录入", "ocr_text": null, "caption": "文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051126067845782372341762208", "alt_text": "文档录入", "ocr_text": null, "caption": "文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051126231656482199017673971", "alt_text": "复制文本录入", "ocr_text": null, "caption": "复制文本录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051126373631693980390670150", "alt_text": "上传Word文档录入", "ocr_text": null, "caption": "上传Word文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20250904160051103425400400318437", "alt_text": "上传Word文档录入", "ocr_text": null, "caption": "上传Word文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051127408946368572995103196", "alt_text": "上传Word文档录入", "ocr_text": null, "caption": "上传Word文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051127271583939665149932894", "alt_text": "上传Excel文档录入", "ocr_text": null, "caption": "上传Excel文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509041600062543612819646596562", "alt_text": "上传Excel文档录入", "ocr_text": null, "caption": "上传Excel文档录入"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051127494400071848946896564", "alt_text": "上传Excel文档录入", "ocr_text": null, "caption": "上传Excel文档录入"}]

```text
一文了解：机构题库快捷录题
一文了解：机构题库快捷录题
校区机构根据不同的教学任务安排，老师需要定期更新教研题目，除系统支持的题库外，老师可以选择上传机构自有题库，基于此，系统老师端自有题库录题界面及流程已全面优化，支持文档录入！
文档录入
老师点击机构题库，点击新建试卷，在左边可以看到文档录入的按钮，点击即可进入文档录入页面。
[图片: 文档录入]
[图片: 文档录入]
复制文本录入
老师可以选择复制文本：
1：点击格式示例复制示例文本修改 2：复制需要上传的word文本，复制之后可以在当前页面编辑。
【左侧为文本编辑框，右侧为预览框】
[图片: 复制文本录入]
上传Word文档录入
上传文档第一步先下载文档模版，注：需要按模版编辑题目素材！
文档格式必须正确，需要为docx格式
[图片: 上传Word文档录入]
[图片: 上传Word文档录入]
第二步选择一键复制或上传文档，即可快速完成录题！
[图片: 上传Word文档录入]
上传Excel文档录入
上传文档第一步先下载文档模版，可上传的题目类型有：单选题、多选题、填空题、简答题、写作题。注：需要按模版编辑题目素材！
[图片: 上传Excel文档录入]
[图片: 上传Excel文档录入]
第二步选择上传文档，即可快速完成录题！
[图片: 上传Excel文档录入]

图片说明：文档录入
图片说明：文档录入
图片说明：复制文本录入
图片说明：上传Word文档录入
图片说明：上传Word文档录入
图片说明：上传Word文档录入
图片说明：上传Excel文档录入
图片说明：上传Excel文档录入
图片说明：上传Excel文档录入
```

### chunk_721336ec84ac80dbb09d421265003f5a | 校校精读功能全新升级啦！新增「逻辑填空、结构&翻译」2种作答形式～

- source_id：helpcenter:245
- document_id：doc_helpcenter_245
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2026-03-04T15:22:48
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041532391476888269778124938", "alt_text": "01 校校AI 精选阅读材料，帮老师“选对句子”", "ocr_text": null, "caption": "01 校校AI 精选阅读材料，帮老师“选对句子”"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041532594659463737769272534", "alt_text": "02 老师布置作业，一套精读，多种能力训练", "ocr_text": null, "caption": "02 老师布置作业，一套精读，多种能力训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041533465509002257827327887", "alt_text": "04 结果页优化", "ocr_text": null, "caption": "04 结果页优化"}]

```text
校校精读功能全新升级啦！新增「逻辑填空、结构&翻译」2种作答形式～
校校精读功能全新升级啦！新增「逻辑填空、结构&翻译」2种作答形式～
在实际教学中，精读往往是老师最重视、也最难设计的一类作业
- 选句靠经验，标准不统一
- 句子选得对不对，很难提前验证
- 老师批改时，也很难快速定位学生的具体问题
校校【基础练习 - 精读】功能全系升级
让老师 更好布置 让学生 更会学习
让“精读”真正成为一种可训练、可评估的能力
01 校校AI 精选阅读材料，帮老师“选对句子”
校校AI将通过经教研团队评估的统一的选句规则，将精读句选择标准化、规模化，（陆续覆盖 托福 / 雅思 / SAT / 小托福 / KET / PET 等科目），在不同考试体系、不同文章长度下，都能稳定提取可训练、可评估的精读句。
[图片: 01 校校AI 精选阅读材料，帮老师“选对句子”]
02 老师布置作业，一套精读，多种能力训练
在作业布置页，老师可以基础练习-读-精读中选择需要布置的科目、来源，以及测试内容（支持多选）：结构&翻译、逻辑填空，筛选好需要布置的题目内容（支持多选），一键布置给学生！
逻辑填空：基于上下文的逻辑判断，真正考察学生“是否读懂句子在文中的作用”
结构&翻译：找主干、拆结构，理解 + 表达双重输出，避免学生只会“对着词翻译”
[图片: 02 老师布置作业，一套精读，多种能力训练]
03 学生作答，一步一步，把句子“吃透”
学生端作答流程更清晰，简单。在作答精读-逻辑填空板块时，左边展示材料，右边展示精读句，学生需要将精读句以拖拽的形式放入材料中适当的空缺位置，让学生专注思考逻辑，基于材料文本做出整体判断。
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041519397893408202180562084
学生在作答结构&翻译板块时，可以逐句作答，也可以点击对应题号自由切换题目。

图片说明：01 校校AI 精选阅读材料，帮老师“选对句子”
图片说明：02 老师布置作业，一套精读，多种能力训练
图片说明：04 结果页优化
```

### chunk_aa848432aa4c19883c5451fac45c77d3 | 校校精读功能全新升级啦！新增「逻辑填空、结构&翻译」2种作答形式～

- source_id：helpcenter:245
- document_id：doc_helpcenter_245
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：1
- 状态：active
- 更新时间：2026-03-04T15:22:48
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041532391476888269778124938", "alt_text": "01 校校AI 精选阅读材料，帮老师“选对句子”", "ocr_text": null, "caption": "01 校校AI 精选阅读材料，帮老师“选对句子”"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041532594659463737769272534", "alt_text": "02 老师布置作业，一套精读，多种能力训练", "ocr_text": null, "caption": "02 老师布置作业，一套精读，多种能力训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041533465509002257827327887", "alt_text": "04 结果页优化", "ocr_text": null, "caption": "04 结果页优化"}]

```text
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041519452677621147916470286
作答每个精读句时，结构分析部分只要求学生填写主干内容，避免无效负担。再完成句子翻译即可。
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041521315697643715525383217
04 结果页优化
校校精读结果页也进行了优化，老师可以看到学生的总分 / 分项分/正确率 / 用时，一眼看清是逻辑问题？结构没看懂？还是翻译表达不到位？针对学生的作答结果，帮助老师更好的教学！
[图片: 04 结果页优化]

图片说明：01 校校AI 精选阅读材料，帮老师“选对句子”
图片说明：02 老师布置作业，一套精读，多种能力训练
图片说明：04 结果页优化
```

### chunk_27fb6a92497fc00ada1bcf58b06cc44e | MacOS校校客户端下载安装说明书

- source_id：helpcenter:251
- document_id：doc_helpcenter_251
- 分类：热门问题
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2026-05-28T18:42:43
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/d839/202605281839413184998856005147338", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/44af/202605281840108989981347646391579", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2d02/202605281840214535829837390336452", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/db67/20260528184034183930806821467792", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/558f/202605281840558664662574098174723", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/31f9/202605281841379201503485919261492", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/4829/202605281841572071517486529449795", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/12a8/20260528184214818136003133813876", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/6ceb/202605281842381144453788944948803", "alt_text": "MacOS校校客户端下载安装说明", "ocr_text": null, "caption": "MacOS校校客户端下载安装说明"}]

```text
MacOS校校客户端下载安装说明书
MacOS校校客户端下载安装说明书
校校系统桌面客户端全新上线，相比网页版，不仅严格遵循，国家数据安全等级保护三级标准，保护学生和老师的学习数据安全无忧，还带来了更顺畅的学习体验！
MacOS校校客户端下载安装说明
Step1：打开系统网址登录页，苹果系统点击右上角 MacOS 版本，下载客户端安装文件。
[图片: MacOS校校客户端下载安装说明]
Step2：下载成功后，点击右上角，打开安装文件。
[图片: MacOS校校客户端下载安装说明]
Step3：找到下载的文件，双击，将校校移动至 Applications 文件夹。
[图片: MacOS校校客户端下载安装说明]
[图片: MacOS校校客户端下载安装说明]
Step4：在应用程序中，找到校校双击打开。
[图片: MacOS校校客户端下载安装说明]
Step5：在弹窗中点击打开。
注：该提示为Apple系统对新发布的、还没有被大量用户下载过的软件的一种常见保护机制。校校客户端系符合国家数据安全等级三级标准，当前软件已经通过代码签名（发行者显示为 Benben Information Tech Co., Ltd.），确保数据安全与隐私保护。
[图片: MacOS校校客户端下载安装说明]
Step6：在网址栏输入网页端的登录网址。
[图片: MacOS校校客户端下载安装说明]
Step7：输入账号密码即可登录校校客户端。
[图片: MacOS校校客户端下载安装说明]
Step8：登录成功后，将安装程序推出。
[图片: MacOS校校客户端下载安装说明]

图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
图片说明：MacOS校校客户端下载安装说明
```

### chunk_3607ddc4a307fe0bf21c46bce23ae078 | 使用校校系统有哪些设备平台要求？

- source_id：helpcenter:19
- document_id：doc_helpcenter_19
- 分类：初次使用指南
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2021-04-06T10:13:09
- 图片数：2
- 图片引用：[{"url": "http://xiaosaas.oss-cn-beijing.aliyuncs.com/202104091333174666033291634161180.png", "alt_text": "Google Chrome浏览器下载链接", "ocr_text": null, "caption": "Google Chrome浏览器下载链接"}, {"url": "http://xiaosaas.oss-cn-beijing.aliyuncs.com/202104091544367730008205337882987.png", "alt_text": "Safari浏览器：iPad用户请使用苹果内置Safari浏览器。", "ocr_text": null, "caption": "Safari浏览器：iPad用户请使用苹果内置Safari浏览器。"}]

```text
使用校校系统有哪些设备平台要求？
使用校校系统有哪些设备平台要求？
电脑端（Mac&Windows)使用Google Chrome浏览器；iPad 请使用Safari浏览器。
Google Chrome浏览器下载链接
Windows/苹果电脑可前往Google Chrome官方网站下载：https://www.google.cn/chrome/
[图片: Google Chrome浏览器下载链接]
Safari浏览器：iPad用户请使用苹果内置Safari浏览器。
[图片: Safari浏览器：iPad用户请使用苹果内置Safari浏览器。]
关键词：平台、校校、浏览器、电脑、端、系统、设备、请使用

图片说明：Google Chrome浏览器下载链接
图片说明：Safari浏览器：iPad用户请使用苹果内置Safari浏览器。
```

### chunk_766f93b528f85a909ca0e98aa2b0f300 | VIP学生账号和非VIP(普通)学生账号有什么区别？

- source_id：helpcenter:74
- document_id：doc_helpcenter_74
- 分类：热门文章
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T14:08:03
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306115244265628015365810646", "alt_text": "非VIP学生账号权益", "ocr_text": null, "caption": "非VIP学生账号权益"}]

```text
VIP学生账号和非VIP(普通)学生账号有什么区别？
VIP学生账号和非VIP(普通)学生账号有什么区别？
如果学生打开系统提示作业功能暂未开通的提示信息，说明老师给学生开通的是非VIP学生账号，请老师联系客户经理处理！
那么VIP学生账号和非VIP学生账号有什么区别呢？一起来看看吧～
学生账号有哪些功能？
学生账号包含在线作业、自适应练习、课表查看、课堂反馈、学习笔记、学习报告和错题集等。
VIP学生账号权益
VIP学生账号包含上述所有功能！
非VIP学生账号权益
非VIP学生账号无法支持在线作业，即学生无法通过学生端系统在线完成作业（所有作业均无法在线作答），其余功能正常使用，还有系统自带的自适应练习，有效帮助学生定制个性化学习路径，精准定位短板，迅速提升学生的学习成绩！
[图片: 非VIP学生账号权益]
开通VIP账号请联系客户经理处理！

图片说明：非VIP学生账号权益
```

### chunk_4b59411d7d88c2c87132e624bba26510 | 学生如何自己查看自己的错题分析？

- source_id：helpcenter:160
- document_id：doc_helpcenter_160
- 分类：使用技巧
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:16:01
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061021001153453433511471416", "alt_text": "具体操作方法如下图：", "ocr_text": null, "caption": "具体操作方法如下图："}]

```text
学生如何自己查看自己的错题分析？
学生如何自己查看自己的错题分析？
学生可登录网页端账号，随时查看自己的错题分析数据，也可以选择数量重新练习！
具体操作方法如下图：
登录学员账号，点击左侧导航栏【错题】，如果同时有多个班级，可在这里进行班级选择切换，点击【查看详情】，即可看到不同题型下的具体错误题目，学生可以自己选择重新练习错题！
[图片: 具体操作方法如下图：]

图片说明：具体操作方法如下图：
```

### chunk_433a9985bd6e21ba7389ed083117b20e | 如何进行销售线索协作

- source_id：helpcenter:172
- document_id：doc_helpcenter_172
- 分类：核心功能介绍
- 适用角色库：sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-19T18:03:24
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051129305795210104291128274", "alt_text": "添加协作销售", "ocr_text": null, "caption": "添加协作销售"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051129548029689491151469839", "alt_text": "添加协作销售", "ocr_text": null, "caption": "添加协作销售"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051130128886492512064325389", "alt_text": "移除协作销售", "ocr_text": null, "caption": "移除协作销售"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051131238275125104706245763", "alt_text": "协作沟通跟进记录", "ocr_text": null, "caption": "协作沟通跟进记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051132291073671294594124401", "alt_text": "协作沟通跟进记录", "ocr_text": null, "caption": "协作沟通跟进记录"}]

```text
如何进行销售线索协作
如何进行销售线索协作
系统支持一条潜客线索多人协作跟进吗？可以的，添加协作销售可以同时跟进线索，系统会实时记录沟通及变更详情！
添加协作销售
当一条线索无法跟进或需要同事、上级协助时，点击负责销售对应的蓝色名称，即可填写协作销售。
[图片: 添加协作销售]
点击滑动列表可查看并添加协作销售！
[图片: 添加协作销售]
移除协作销售
若误添加或不需要该协作销售了，点击一键移除即可！
[图片: 移除协作销售]
协作沟通跟进记录
查看跟进进度可以清晰的记录线索的跟进情况，包含协作销售的跟进情况。
[图片: 协作沟通跟进记录]
还可以点击编辑，查看详细的沟通及编辑记录，系统会实时记录协作销售的变更记录！
[图片: 协作沟通跟进记录]

图片说明：添加协作销售
图片说明：添加协作销售
图片说明：移除协作销售
图片说明：协作沟通跟进记录
图片说明：协作沟通跟进记录
```

### chunk_8cbb6e584b1bd8e89cd000c938970d51 | 学生如何作答新托福2026模考测试？

- source_id：helpcenter:241
- document_id：doc_helpcenter_241
- 分类：热门问题
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2025-10-20T11:05:34
- 图片数：28
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201059513260136872134171162", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100031777194151194929075", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100172884925955275981935", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100326004729895516855669", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2025102011004252585913348542835", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100546826775906565022148", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201101103923540259282319697", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201114298894088768341749811", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102173615526224953829104", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102351949717921775129405", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102382427623266657609381", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102443167687747485317787", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102502794169298486241319", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103001761035149448691025", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103112430376034353811654", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103334510119783385469133", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103435795360454005344905", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103539079397741062259280", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104108292635574808527496", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104297765507440334583359", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020110437128012233253014915", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104436186246636860184884", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104474836069953403539179", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104561864075402400898186", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104598784576911141183638", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020110503439256234631902533", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201105153944679899010795250", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201105315530791828598840091", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
学生如何作答新托福2026模考测试？
学生如何作答新托福2026模考测试？
校校已上线新托福2026模考系统，一起来看学生如何作答新托福模考测试！
学生端全新答题流程
学生答题前需要进行听力、口语测试，可以调节音量，测试麦克风声音大小，确保考试可以正常进行。
[图片: 学生端全新答题流程]
阅读部分
阅读部分包括两个module，约35-48题，答题时长大约为18-27分钟。
学生在引导页面可以查看阅读考察题型以及要求，点击Begin即可开始答题。
[图片: 阅读部分]
Module 1
学生首先需要作答Complete the Words题型，共10个空，学生需要根据段落填写单词缺失的字母，填写完会自动跳到下一空，点Next即可继续答题。
[图片: 阅读部分]
接着学生需要作答Read in Daily Life：生活化阅读2篇共6题。涵盖海报、菜单、社交媒体帖子或网页等日常素材。学生完成答题后可以点击Next继续答题，或点击Back返回上一题。
[图片: 阅读部分]
最后是Academic Passage：学术文章。题型涵盖否定信息题、推断题、词汇题、修辞题，段落关系题。点击Next继续答题，或点击Back返回上一题。
[图片: 阅读部分]
Module 2 
阅读Module 2和Module1题型一样，包括Complete the Words、Read in Daily Life、Read an Academic Passage，作答流程也与Module1一致。
注意：学生在作答Module2时，不能再返回Module1答题。
[图片: 阅读部分]
听力部分
听力部分包括两个Module，听力材料包括问答、对话、公告、学术讲座，约35-45题，答题时长大约为18-27分钟。
学生在引导页面可以查看听力考察题型以及要求，点击Begin即可开始答题。
[图片: 听力部分]
Module 1 
学生进入答题页面后可以查看Module1答题要求，点击Next即可开始答题。
[图片: 听力部分]
学生需要先听完音频后才会自动进入答题页面，点击Next即可继续答题。

图片说明：学生端全新答题流程
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：写作部分
图片说明：写作部分
图片说明：写作部分
图片说明：写作部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_768d5cf2956b683fd52098184db0eb4e | 学生如何作答新托福2026模考测试？

- source_id：helpcenter:241
- document_id：doc_helpcenter_241
- 分类：热门问题
- 适用角色库：student(学生库)
- 分块序号：1
- 状态：active
- 更新时间：2025-10-20T11:05:34
- 图片数：28
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201059513260136872134171162", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100031777194151194929075", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100172884925955275981935", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100326004729895516855669", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2025102011004252585913348542835", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100546826775906565022148", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201101103923540259282319697", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201114298894088768341749811", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102173615526224953829104", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102351949717921775129405", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102382427623266657609381", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102443167687747485317787", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102502794169298486241319", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103001761035149448691025", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103112430376034353811654", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103334510119783385469133", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103435795360454005344905", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103539079397741062259280", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104108292635574808527496", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104297765507440334583359", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020110437128012233253014915", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104436186246636860184884", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104474836069953403539179", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104561864075402400898186", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104598784576911141183638", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020110503439256234631902533", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201105153944679899010795250", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201105315530791828598840091", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
[图片: 听力部分]
学生作答Conversations，Announcements，Academic Talks题型时，需要听对话、通知、学术讨论完成对应题目。
[图片: 听力部分]
[图片: 听力部分]
[图片: 听力部分]
[图片: 听力部分]
在听力答题过程中，如果有未选择答案点击Next的情况，系统会提示需要选择答案才能离开此题，确保学生答题无遗漏。
[图片: 听力部分]
Module 2
听力部分Module2和Module1一样，包括Listen and Choose a Response，Conversations，Announcements、Academic Talks题型，答题时间与流程均与Module 1一致。
[图片: 听力部分]
写作部分
写作部分保留学术写作，移除了综合写作，新增选词造句、邮件写作题型，共12题，考试时长约23分钟
学生在引导页面可以查看写作考察题型以及要求，点击Continue即可开始答题。
[图片: 写作部分]
学生进入写作部分后，需要先完成Build a Sentence：选词造句题，选择词语组成语法正确的句子。一共10道题目，点击Next即可继续作答。
[图片: 写作部分]
Write an Email：邮件写作，学生需要根据场景在7分钟内完成，需要注重格式、语气与逻辑。
[图片: 写作部分]
Academic Discussion：学术讨论，和改革前一致，学生作答完成点击Next即可进入口语答题。
[图片: 写作部分]
口语部分
口语部分题型为句子复述和模拟面试，共11题，答题时长约8分钟。
学生在引导页面可以查看口语考察题型以及要求，点击Continue即可开始答题。
[图片: 口语部分]
学生进入口语部分后，需要先完成Listen and Repeat：句子复述题，共7题，没有准备时间，学生需要在10秒内完成答题，即时记忆要求较高。
[图片: 口语部分]
[图片: 口语部分]
[图片: 口语部分]

图片说明：学生端全新答题流程
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：写作部分
图片说明：写作部分
图片说明：写作部分
图片说明：写作部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_8736f44f2bc554016f8f63700cfc6e3c | 学生如何作答新托福2026模考测试？

- source_id：helpcenter:241
- document_id：doc_helpcenter_241
- 分类：热门问题
- 适用角色库：student(学生库)
- 分块序号：2
- 状态：active
- 更新时间：2025-10-20T11:05:34
- 图片数：28
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201059513260136872134171162", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100031777194151194929075", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100172884925955275981935", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100326004729895516855669", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2025102011004252585913348542835", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201100546826775906565022148", "alt_text": "阅读部分", "ocr_text": null, "caption": "阅读部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201101103923540259282319697", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201114298894088768341749811", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102173615526224953829104", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102351949717921775129405", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102382427623266657609381", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102443167687747485317787", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201102502794169298486241319", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103001761035149448691025", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103112430376034353811654", "alt_text": "听力部分", "ocr_text": null, "caption": "听力部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103334510119783385469133", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103435795360454005344905", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201103539079397741062259280", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104108292635574808527496", "alt_text": "写作部分", "ocr_text": null, "caption": "写作部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104297765507440334583359", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020110437128012233253014915", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104436186246636860184884", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104474836069953403539179", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104561864075402400898186", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201104598784576911141183638", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020110503439256234631902533", "alt_text": "口语部分", "ocr_text": null, "caption": "口语部分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201105153944679899010795250", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201105315530791828598840091", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
Interview：模拟面试，共4个问题，每个问题答题时长45秒。答题时长结束后自动跳到下一个问题。学生答题完成后，点击Submit即可完成交卷。
[图片: 口语部分]
[图片: 口语部分]
[图片: 口语部分]
学生查看模考测试结果
校校托福测试报告也进行了全新改版，基于新版评分标准，新增6分的四科分与总分；和120分制同时显示，可以直接对标CEFR 等级！学生整体题型分析老师也能直接查看，添加分项精准评价！
[图片: 学生查看模考测试结果]
结果页详情展示学生具体作答情况，客观题自动批改，错题及时定位，精准分析学生知识点掌握薄弱点，帮助学生更好的进步!
[图片: 学生查看模考测试结果]

图片说明：学生端全新答题流程
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：阅读部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：听力部分
图片说明：写作部分
图片说明：写作部分
图片说明：写作部分
图片说明：写作部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：口语部分
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_133e48b9eee439cd7833140ed620eeb1 | 系统题库全新升级：老师选题、筛题、用题效率提升一大步！

- source_id：helpcenter:244
- document_id：doc_helpcenter_244
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2026-03-04T14:51:12
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041526205010161708828483566", "alt_text": "01 题目卡片新增关键教学数据", "ocr_text": null, "caption": "01 题目卡片新增关键教学数据"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041526415328175277593611107", "alt_text": "01 题目卡片新增关键教学数据", "ocr_text": null, "caption": "01 题目卡片新增关键教学数据"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041527304251830102064558531", "alt_text": "01 题目卡片新增关键教学数据", "ocr_text": null, "caption": "01 题目卡片新增关键教学数据"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041528552845247237337201809", "alt_text": "02 排序筛选项更精准", "ocr_text": null, "caption": "02 排序筛选项更精准"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041529213927087340650972504", "alt_text": "02 排序筛选项更精准", "ocr_text": null, "caption": "02 排序筛选项更精准"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260304152955695850496902896586", "alt_text": "03 题目详情页优化", "ocr_text": null, "caption": "03 题目详情页优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041530126829645520794983731", "alt_text": "03 题目详情页优化", "ocr_text": null, "caption": "03 题目详情页优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041531007131400120431019108", "alt_text": "03 题目详情页优化", "ocr_text": null, "caption": "03 题目详情页优化"}]

```text
系统题库全新升级：老师选题、筛题、用题效率提升一大步！
系统题库全新升级：老师选题、筛题、用题效率提升一大步！
在日常教学中，老师会频繁面对一个问题：
题库越来越大，题越来越多
但“找到适合自己班级的题目”反而越来越难
为了帮助老师更高效地管理、筛选和使用
托福、雅思、SAT、AP 等11 类题库资源
校校系统题库全新升级
- 新增关键教学数据展示
- 排序筛选项更精准
- 题目详情页优化
01 题目卡片新增关键教学数据
过去题库页面更多只是展示题目标题、来源等信息。但随着题库规模扩大，仅靠“看标题”已经无法判断：这套题难不难？学生做得怎么样？是否值得用在课堂或作业？校校题目卡片新增：参与数、全网参与数、正确率、完成率、中位分、方差、中位用时、区分度数据，帮助老师快速判断题目质量与教学价值。
[图片: 01 题目卡片新增关键教学数据]
[图片: 01 题目卡片新增关键教学数据]
同时，题库卡片新增题目难度和 top 高错点展示，校校基于学生得分率以及作业详细数据，自动识别最常错知识点，帮助老师精准定位教学重点，让老师挑选题目更有数据判断！
[图片: 01 题目卡片新增关键教学数据]
02 排序筛选项更精准
面对上千套题目，老师最常见的需求是：先看最近学生做过的题，找正确率低的题做强化训练，找区分度高的题做测评。校校题库排序项新增：正确率、全网参与人数、更新日期、中位分、方差、中位用时、区分度等排序项，帮助老师按不同教学目的快速进行题目排序。
[图片: 02 排序筛选项更精准]
校校题库筛选项整合了之前的话题、知识点，新增难度、区分度、最近上新、讲解题目、开放题目筛选。老师可以根据教学情况，筛选精准匹配班级水平的对应难度题目，以及按区分度筛选测评题、分层题。
[图片: 02 排序筛选项更精准]
03 题目详情页优化
老师可以在题库详情页查看每个小题的正确率、中位用时、区分度、争议率，点击旁边问号按钮可以查看对应指标的含义，帮助老师查看学生做题行为画像，更好的进行教学规划。
[图片: 03 题目详情页优化]
[图片: 03 题目详情页优化]

图片说明：01 题目卡片新增关键教学数据
图片说明：01 题目卡片新增关键教学数据
图片说明：01 题目卡片新增关键教学数据
图片说明：02 排序筛选项更精准
图片说明：02 排序筛选项更精准
图片说明：03 题目详情页优化
图片说明：03 题目详情页优化
图片说明：03 题目详情页优化
```

### chunk_408800fd86776537334104138b3580c2 | 系统题库全新升级：老师选题、筛题、用题效率提升一大步！

- source_id：helpcenter:244
- document_id：doc_helpcenter_244
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2026-03-04T14:51:12
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041526205010161708828483566", "alt_text": "01 题目卡片新增关键教学数据", "ocr_text": null, "caption": "01 题目卡片新增关键教学数据"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041526415328175277593611107", "alt_text": "01 题目卡片新增关键教学数据", "ocr_text": null, "caption": "01 题目卡片新增关键教学数据"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041527304251830102064558531", "alt_text": "01 题目卡片新增关键教学数据", "ocr_text": null, "caption": "01 题目卡片新增关键教学数据"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041528552845247237337201809", "alt_text": "02 排序筛选项更精准", "ocr_text": null, "caption": "02 排序筛选项更精准"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041529213927087340650972504", "alt_text": "02 排序筛选项更精准", "ocr_text": null, "caption": "02 排序筛选项更精准"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260304152955695850496902896586", "alt_text": "03 题目详情页优化", "ocr_text": null, "caption": "03 题目详情页优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041530126829645520794983731", "alt_text": "03 题目详情页优化", "ocr_text": null, "caption": "03 题目详情页优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603041531007131400120431019108", "alt_text": "03 题目详情页优化", "ocr_text": null, "caption": "03 题目详情页优化"}]

```text
老师可以点击选项查看该选项的干扰意向标签，查看学生最真实的误区，为什么会做错这道题，帮助老师精准讲题。
[图片: 03 题目详情页优化]

图片说明：01 题目卡片新增关键教学数据
图片说明：01 题目卡片新增关键教学数据
图片说明：01 题目卡片新增关键教学数据
图片说明：02 排序筛选项更精准
图片说明：02 排序筛选项更精准
图片说明：03 题目详情页优化
图片说明：03 题目详情页优化
图片说明：03 题目详情页优化
```

### chunk_1c69cbc72785dd03f9984827eb025f23 | 如何更快接收消息通知？

- source_id：helpcenter:58
- document_id：doc_helpcenter_58
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T18:49:33
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051400004024540951449289616", "alt_text": "电脑端绑定公众号", "ocr_text": null, "caption": "电脑端绑定公众号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304111849296040688275685614424", "alt_text": "小程序端绑定公众号", "ocr_text": null, "caption": "小程序端绑定公众号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304131811288801358404587771138", "alt_text": "公众号消息通知类型", "ocr_text": null, "caption": "公众号消息通知类型"}]

```text
如何更快接收消息通知？
如何更快接收消息通知？
校长、教务、销售、老师、助教、学生、家长均可通过绑定微信公众号快捷接收系统相关消息通知，协助用户更加便捷的掌握最新课程动态。
电脑端绑定公众号
用户打开电脑端系统首页，点击右上角菜单栏-绑定公众号按钮，弹出小程序二维码，用户扫码即可绑定微信公众号，快速接受系统消息通知。
[图片: 电脑端绑定公众号]
小程序端绑定公众号
用户打开微信小程序首页，点击下方导航栏-我的按钮，选择上方-绑定公众号，弹出公众号二维码，长按识别二维码即可绑定公众号，快捷接受系统消息通知。
[图片: 小程序端绑定公众号]
公众号消息通知类型
- 校长端：校长通过公众号可以在每天21：30接受机构的日报，方便校长快速浏览校区的教学情况，运营情况和销售情况。
- 教务端：教务可通过公众号接收新学员转正加入消息通知，教务也能接受机构每天的日报，实时掌握校区的教学情况，运营情况和销售情况。
- 销售端：销售可以通过公众号接收机构每天的销售日报，实时掌握校区销售情况；入学模考的新增潜客，潜客的试听课安排，潜客的分配都会给到销售消息通知，帮助销售实时掌握潜客跟进进度；另外销售订单的确认，市场新增潜客，退费操作也会第一时间给到销售确认信息。
- 老师端：老师也可以通过公众号接收机构每天的日报，实时掌握校区的教学情况；试听课的安排，课表的调整和老师的调课申请状态都会有消息通知给到老师，帮助老师提前做好教学规划；新老师和新学生加入班级会及时通知老师；即将过期作业有未完成的学生，学生有考试安排都有对应消息，提升老师的教学效率。
- 学生端：学生绑定公众号后，会收到新作业的发布通知，以及老师手动推送的作业到期通知，帮助学生了解自己的学习任务；对于课程的调整以及学生的调课申请状况也会及时给到学生，避免学生错过课程。
- 家长端：家长可以通过公众号接收到老师给学生的课堂反馈通知，以及学生完成作业的通知，帮助家长了解学生的学习状态和学习进度。
同时，绑定和解绑公众号都是想用户发送相关的微信公众号消息通知！
[图片: 公众号消息通知类型]

图片说明：电脑端绑定公众号
图片说明：小程序端绑定公众号
图片说明：公众号消息通知类型
```

### chunk_91cc4d061703fa694a63a366b11a255a | 一文了解：如何使用首页功能

- source_id：helpcenter:84
- document_id：doc_helpcenter_84
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:08:33
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051135243114033809674819341", "alt_text": "首页功能介绍", "ocr_text": null, "caption": "首页功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051136421826852180682234652", "alt_text": "首页功能介绍", "ocr_text": null, "caption": "首页功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305113719337660919271245315", "alt_text": "首页功能介绍", "ocr_text": null, "caption": "首页功能介绍"}]

```text
一文了解：如何使用首页功能
一文了解：如何使用首页功能
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍首页的功能。
浏览器使用建议
电脑端 ( Mac&Windows)使用Google Chrome浏览器
iPad 请使用Safari浏览器
首页功能介绍
数据汇总：首页可以查看机构基本运营数据汇总，包括学生、班级、老师人数，以及账号数量。
[图片: 首页功能介绍]
快捷跳转：待办事项会显示待排课、试听排课申请，点击去处理可以一键跳转至班级、申请页面进行排课操作。
[图片: 首页功能介绍]
订单审批：教务老师可以在首页快捷处理订单审批、退费审批相关操作，已确认订单的学生以及点击非正式学员一键转为正式学员。
[图片: 首页功能介绍]

图片说明：首页功能介绍
图片说明：首页功能介绍
图片说明：首页功能介绍
```

### chunk_6b0d05f5384e1899a4c00d554e513ad9 | 如何解决学生已完成作业，老师端该作业显示未完成的情况？

- source_id：helpcenter:102
- document_id：doc_helpcenter_102
- 分类：热门问题
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:20:26
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061058064329633923670427151", "alt_text": "一、学生未完成作业", "ocr_text": null, "caption": "一、学生未完成作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061058104536192403344599540", "alt_text": "一、学生未完成作业", "ocr_text": null, "caption": "一、学生未完成作业"}]

```text
如何解决学生已完成作业，老师端该作业显示未完成的情况？
如何解决学生已完成作业，老师端该作业显示未完成的情况？
当学生说明已完成作业/测试时，老师端发现作业并未完成的现象，可通过以下文档排查。
一、学生未完成作业
如果学生未完成作业，或者作业正在进行中，老师端该学生的作业不会显示为已完成
【解决方法】：
首先确认学生是否有完成作业，老师可以在作业页面查看学生答题录屏。【注：如果学生作业没有录屏就是未完成作业。】
查看学生作业录屏步骤：
1）老师在左侧导航栏点击【作业】，再点击作业详情页面
2）在作业详情页找到对应学生，点击查看详情 
3）点击答题录屏即可看到学生的答题录屏情况
4）查看学生做题时长，是否为0 ，若为0且没有录屏，则学生未完成作业
[图片: 一、学生未完成作业]
[图片: 一、学生未完成作业]
二、学生已完成作业
如果学生已完成作业且可以看到学生的答题录屏，老师端还显示该作业未完成，可以在群里发送作业链接至校校小助手帮您解答！

图片说明：一、学生未完成作业
图片说明：一、学生未完成作业
```

### chunk_fdd8f5182764dd8068f2d24374b803bb | 常用作业如何设置？（常用作业&作业拷贝）

- source_id：helpcenter:161
- document_id：doc_helpcenter_161
- 分类：使用技巧
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:17:13
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306104353575490605003289455", "alt_text": "添加常用作业", "ocr_text": null, "caption": "添加常用作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061044539215999763483295467", "alt_text": "布置常用作业", "ocr_text": null, "caption": "布置常用作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061046375745417765601916116", "alt_text": "拷贝班级作业", "ocr_text": null, "caption": "拷贝班级作业"}]

```text
常用作业如何设置？（常用作业&作业拷贝）
常用作业如何设置？（常用作业&作业拷贝）
老师在布置作业时，可选择将本次作业添加至常用作业，即可在“我的班级”中的“拷贝作业”，查看并编辑作业名称及发布时间，并支持老师在手机端操作。
添加常用作业
老师在布置作业时，可选择将本次作业添加至常用作业。
[图片: 添加常用作业]
布置常用作业
添加好的常用作业，老师可在【班级】中查看的【常用作业】，查看并编辑作业名称及发布时间！
[图片: 布置常用作业]
拷贝班级作业
老师也可在“班级作业”中的“拷贝作业”里，点击班级作业，从已经布置过作业的班级，整体或部分拷贝作业，节省老师重复组卷布置的时间！
[图片: 拷贝班级作业]

图片说明：添加常用作业
图片说明：布置常用作业
图片说明：拷贝班级作业
```

### chunk_7fbfc5ed9f4f5d43051b2659ec2e8f15 | 老师如何布置新托福2026模考测试！

- source_id：helpcenter:240
- document_id：doc_helpcenter_240
- 分类：热门文章
- 适用角色库：teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2025-10-20T10:58:48
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061155267551256806391733226", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158385306466835052081013", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158428414273409093081524", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158452005388724634656695", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158503786048935466082684", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306134856438496563136540903", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201057006145775085401722987", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201058216182897593475309273", "alt_text": "口语写作AI智能批改", "ocr_text": null, "caption": "口语写作AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201058308007636034972232650", "alt_text": "口语写作AI智能批改", "ocr_text": null, "caption": "口语写作AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201058403766628375670913087", "alt_text": "口语写作AI智能批改", "ocr_text": null, "caption": "口语写作AI智能批改"}]

```text
老师如何布置新托福2026模考测试！
老师如何布置新托福2026模考测试！
校校已上线新托福2026模考系统，一起来看老师如何布置新托福模考测试！
老师如何布置模考
老师可以在作业-模考测试/题型训练页面，选择新托福进行作业布置。
[图片: 老师如何布置模考]
布置整套模考测试，可以按照阅读： Module Router（四个模块）+Lower/Upper（四个模块），听力：Module Router（四个模块）+Lower/Upper（四个模块），写作：造句+邮件+学术讨论，口语：复述+模拟面试，进行组卷，一键布置给学生。布置时勾选AI批改即可自动批改学生口语写作！
[图片: 老师如何布置模考]
[图片: 老师如何布置模考]
[图片: 老师如何布置模考]
[图片: 老师如何布置模考]
老师也可以在题库页面，勾选对应题目开放给学生自主练习，在已开放题目或者学员管理中随时查看学生练习情况，精准定位学生薄弱环节。
[图片: 老师如何布置模考]
入学模考新增新托福板块，老师可联系校校推送机构专属入学模考试卷，招生转化更轻松！
[图片: 老师如何布置模考]
口语写作AI智能批改
模拟面试口语AI智能批改
校校AI智能批改根据官方维度，分析学生的发音、流利度，从Task Completion & Elaboration、Language Use、Delivery进行分项批改， 帮助学生作答“练习-反馈-修正”的高效闭环。
[图片: 口语写作AI智能批改]
邮件写作AI智能批改
校校AI针对邮件题型写作，根据口语批改标准，结合学生写作，进行Task Completion & Elaboration（任务阐述）、Language Use（语言使用）、Vocabulary & Register（词汇与语域）、Grammar & Lexical Accuracy（语法词汇准确性）分项批改，快速完成批改，解放老师时间。
[图片: 口语写作AI智能批改]

图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：口语写作AI智能批改
图片说明：口语写作AI智能批改
图片说明：口语写作AI智能批改
```

### chunk_e1ff4aed53ea2a196acf1c88c815d127 | 老师如何布置新托福2026模考测试！

- source_id：helpcenter:240
- document_id：doc_helpcenter_240
- 分类：热门文章
- 适用角色库：teacher(老师库)
- 分块序号：1
- 状态：active
- 更新时间：2025-10-20T10:58:48
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061155267551256806391733226", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158385306466835052081013", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158428414273409093081524", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158452005388724634656695", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061158503786048935466082684", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306134856438496563136540903", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201057006145775085401722987", "alt_text": "老师如何布置模考", "ocr_text": null, "caption": "老师如何布置模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201058216182897593475309273", "alt_text": "口语写作AI智能批改", "ocr_text": null, "caption": "口语写作AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201058308007636034972232650", "alt_text": "口语写作AI智能批改", "ocr_text": null, "caption": "口语写作AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201058403766628375670913087", "alt_text": "口语写作AI智能批改", "ocr_text": null, "caption": "口语写作AI智能批改"}]

```text
学术写作AI智能批改
学术写作批改包括Content、Organization、Grammatical Range and Accuracy、Vocabulary。精确到某个句子语法错误、某个词汇使用不当、段落之间逻辑衔接不紧密等细节问题，错误类型、薄弱知识点都会被记录和分析，让进步看得见！
[图片: 口语写作AI智能批改]

图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：老师如何布置模考
图片说明：口语写作AI智能批改
图片说明：口语写作AI智能批改
图片说明：口语写作AI智能批改
```

### chunk_b74017e5194ac1dabd0ea9bf5ca72e4c | 机构题库功能焕新，新托福命题、组卷、批改效率翻倍！

- source_id：helpcenter:243
- document_id：doc_helpcenter_243
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2025-11-19T17:55:00
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412497533838949008405670", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412597145092691714480939", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413042268196907594358317", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202604201436334735073892983730598", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413141780916963544662585", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413204779993231915449412", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413367964979017538586604", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413468055316818311914755", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202604201438204605349060013732667", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260420143835113345474716426426", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306141355319002515348827844", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413594959771249906367273", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051540582043883103211171437", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051542154251830294340158238", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051545216295248076222085318", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051550405610163202946241409", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}]

```text
机构题库功能焕新，新托福命题、组卷、批改效率翻倍！
机构题库功能焕新，新托福命题、组卷、批改效率翻倍！
托福改革后，老师面临题型重构以及题库创建难题，校校机构题库进行了全面升级，从阅读、听力到口语、写作，全流程支持新题型、新结构，让老师录题、布置、共享都更高效、更省心。
01 全面适配新托福 2026
校校机构题库-托福下新增了“新托福2026”科目，试卷结构为新托福考试框架，从阅读到口语，每一模块还原考试场景。
[图片: 01 全面适配新托福 2026]
阅读
阅读部分包括 3 个Module：Reading Module(Router、Lower、Upper)。
选择新增单道题，题型为Complete the Words，老师可以按照提示，录入字母填空题题目材料以及答案，一个空如果有多个字母，系统会在答题时自动拆分为多个空，不需要手动拆分字母空格。
选择题目组，题型包括Read in Daily Life、Read an Academic Passage，老师可以选择题型，按照选择题录入方式，依次录入题目材料、题干、选项、答案。
[图片: 01 全面适配新托福 2026]
[图片: 01 全面适配新托福 2026]
选择题目组，题型包括Read in Daily Life、Read an Academic Passage，老师可以选择题型，按照选择题录入方式，依次录入题目材料、题干、选项、答案。
[图片: 01 全面适配新托福 2026]
听力
听力部分包括 3 个Module：Listening Module(Router、Lower、Upper)。
选择单道题，题型为Listen and Choose a Response，老师可以录入题目音频材料，可以选择音频音色，系统自动匹配图片，添加听力原文，题目选项以及答案。
选择题目组，题型为Listen to a Conversation、Listen to an Announcement 、Listen to an Academic Talk。老师可以录入题目音频材料、题干、选项以及答案。

图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
```

### chunk_c112e307d338be81e0b15cb4f050370a | 机构题库功能焕新，新托福命题、组卷、批改效率翻倍！

- source_id：helpcenter:243
- document_id：doc_helpcenter_243
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：1
- 状态：active
- 更新时间：2025-11-19T17:55:00
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412497533838949008405670", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412597145092691714480939", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413042268196907594358317", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202604201436334735073892983730598", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413141780916963544662585", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413204779993231915449412", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413367964979017538586604", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413468055316818311914755", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202604201438204605349060013732667", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260420143835113345474716426426", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306141355319002515348827844", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413594959771249906367273", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051540582043883103211171437", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051542154251830294340158238", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051545216295248076222085318", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051550405610163202946241409", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}]

```text
[图片: 01 全面适配新托福 2026]
[图片: 01 全面适配新托福 2026]
写作
写作部分包括 3 个题目类型：Build a Sentence、Write an Email、Write for an Academic Discussion。
老师点击新增题目，选择Build a Sentence-写作拖拽题，老师可以按照填空题的形式录入，系统自动匹配为拖拽题展示。
选择Write an Email、Write for an Academic Discussion，老师可以按照写作题题目录入，编辑好题目材料，题干即可。
[图片: 01 全面适配新托福 2026]
[图片: 01 全面适配新托福 2026]
选择Write an Email、Write for an Academic Discussion，老师可以按照写作题题目录入，编辑好题目材料，题干即可。
Write an Email
[图片: 01 全面适配新托福 2026]
Write for an Academic Discussion
[图片: 01 全面适配新托福 2026]
口语
口语部分包括2 个题目类型：Listen and Repeat、Take an Interview
老师点击新增题目，可以选择Listen and Repeat、Take an Interview题型，先录入题目组总材料（题干+音频），选择音频角色，系统将自动匹配对应图片，再录入每个题目的音频以及听力原文。
学生完成口语写作时，老师可以在结果页点击AI批改，校校AI按照官方评分标准进行批改，节省老师效率
[图片: 01 全面适配新托福 2026]
[图片: 01 全面适配新托福 2026]
02 机构题库试卷共享
机构题库新增“共享试卷”板块，仅显示他人共享的试卷，支持按创建人筛选，让资源获取更加便捷高效。
[图片: 02 机构题库试卷共享]

图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
```

### chunk_ca9d5c88510c654a341eee2d5dcda790 | 机构题库功能焕新，新托福命题、组卷、批改效率翻倍！

- source_id：helpcenter:243
- document_id：doc_helpcenter_243
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：2
- 状态：active
- 更新时间：2025-11-19T17:55:00
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412497533838949008405670", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412597145092691714480939", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413042268196907594358317", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202604201436334735073892983730598", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413141780916963544662585", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413204779993231915449412", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413367964979017538586604", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413468055316818311914755", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202604201438204605349060013732667", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260420143835113345474716426426", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306141355319002515348827844", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061413594959771249906367273", "alt_text": "01 全面适配新托福 2026", "ocr_text": null, "caption": "01 全面适配新托福 2026"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051540582043883103211171437", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051542154251830294340158238", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051545216295248076222085318", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051550405610163202946241409", "alt_text": "02 机构题库试卷共享", "ocr_text": null, "caption": "02 机构题库试卷共享"}]

```text
老师在“我的试卷”也可以操作共享试卷。
- 方式一：在我的试卷中，老师可勾选单份或多份试卷，设定哪些老师可查看并使用
- 方式二：在编辑试卷时，老师可直接选择是否共享，共享给哪些老师
[图片: 02 机构题库试卷共享]
[图片: 02 机构题库试卷共享]
新增状态筛选功能，老师可快速查看哪些试卷已共享，哪些待共享，管理试卷更加有序。
[图片: 02 机构题库试卷共享]

图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：01 全面适配新托福 2026
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
图片说明：02 机构题库试卷共享
```

### chunk_3930c025cfb90c1891321d11f22afec7 | 入门必备-教务创建员工账号

- source_id：helpcenter:66
- document_id：doc_helpcenter_66
- 分类：初次使用指南
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T13:13:13
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305140757425144974512764039", "alt_text": "创建校长账号", "ocr_text": null, "caption": "创建校长账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408196505943112044227132", "alt_text": "创建教务/财务账号", "ocr_text": null, "caption": "创建教务/财务账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408263796721163598422700", "alt_text": "创建教务/财务账号", "ocr_text": null, "caption": "创建教务/财务账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408398554936464019147537", "alt_text": "创建老师/助教账号", "ocr_text": null, "caption": "创建老师/助教账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408431336346870626461956", "alt_text": "创建老师/助教账号", "ocr_text": null, "caption": "创建老师/助教账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408516772883426190050010", "alt_text": "创建销售/销售管理员/市场账号", "ocr_text": null, "caption": "创建销售/销售管理员/市场账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408592750425624380180972", "alt_text": "创建销售/销售管理员/市场账号", "ocr_text": null, "caption": "创建销售/销售管理员/市场账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051409076001776226770875489", "alt_text": "创建销售/销售管理员/市场账号", "ocr_text": null, "caption": "创建销售/销售管理员/市场账号"}]

```text
入门必备-教务创建员工账号
入门必备-教务创建员工账号
员工是组成一个团队的关键，不同的员工角色有不同的工作内容和不同系统权限，校校助力员工建设更方便！
创建校长账号
点击左侧导航栏"员工"，可以看到校校系统提供的所有员工角色:校长、教务、老师、销售管理员、销售、助教、市场、财务（一个员工可以有多个身份）
【校长账号】开通默认拥有教务和财务所有权限，校长身份可以同时拥有老师/助教和销售管理员身份
[图片: 创建校长账号]
创建教务/财务账号
【教务】拥有审批权限，功能权限和数据权限，可以根据机构员工角色去进行权限的管理，没有排课权限的老师可以查看课表，不能进行排课
教务身份可以同时拥有财务，老师/助教，销售管理员/销售身份
[图片: 创建教务/财务账号]
【财务】只拥有审批权限，财务身份可以同时拥有教务身份，老师/助教身份
[图片: 创建教务/财务账号]
创建老师/助教账号
【老师】和【助教】角色创建内容相同，老师和助教唯一的不同点:助教可以看到所在班级的整个班级课表，老师只能看到自己的课表
如果一个老师同时兼任代课老师和班主任，只需开通助教账号即可
[图片: 创建老师/助教账号]
[图片: 创建老师/助教账号]
创建销售/销售管理员/市场账号
【销售管理员】默认拥有销售和市场的所有权限
销售管理员不能同时拥有销售或市场身份，销售管理员管可查看自己以及下属普通销售的客户跟进数据，进行订单审批等
[图片: 创建销售/销售管理员/市场账号]
【销售】拥有审批权限功能权限和数据权限机构可以根据员工角色去进行权限调整，普通销售只能查看分配给自己的客户并跟进
[图片: 创建销售/销售管理员/市场账号]
【市场】身份仅拥有渠道管理和潜客分配的权限，主要用于市场线索的录入
[图片: 创建销售/销售管理员/市场账号]

图片说明：创建校长账号
图片说明：创建教务/财务账号
图片说明：创建教务/财务账号
图片说明：创建老师/助教账号
图片说明：创建老师/助教账号
图片说明：创建销售/销售管理员/市场账号
图片说明：创建销售/销售管理员/市场账号
图片说明：创建销售/销售管理员/市场账号
```

### chunk_6a6f4f1da8d593025a841d9225090f1c | 一文读懂：如何进行员工管理

- source_id：helpcenter:85
- document_id：doc_helpcenter_85
- 分类：核心功能介绍
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:12:14
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051138167902252662573932663", "alt_text": "员工管理功能介绍", "ocr_text": null, "caption": "员工管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051138322726888221875281797", "alt_text": "员工管理功能介绍", "ocr_text": null, "caption": "员工管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030511393981387754932458579", "alt_text": "员工管理功能介绍", "ocr_text": null, "caption": "员工管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051141064357719692768075474", "alt_text": "员工管理功能介绍", "ocr_text": null, "caption": "员工管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051141101470529377194858032", "alt_text": "员工管理功能介绍", "ocr_text": null, "caption": "员工管理功能介绍"}]

```text
一文读懂：如何进行员工管理
一文读懂：如何进行员工管理
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍员工管理的功能
员工管理功能介绍
创建员工账号时需要按要求填写员工姓名手机号基础信息，登录密码可以设置为任意密码，不输入则默认为手机号后六位。
[图片: 员工管理功能介绍]
填写完信息后可以勾选对应角色及权限设置，⼀个账号可以同时勾选多个角色身份，但权限冲突的角色（如：销售管理员和销售、校长和教务、老师和助教）不可同时勾选。
[图片: 员工管理功能介绍]
账号“停用”功能，用于老师离职后的操作：账号停用后将不可登录系统，但账号相关联数据(已上课程/已布置作业等)依然保留。
[图片: 员工管理功能介绍]
教务可以操作给销售和老师添加下属，点击添加下属，选择好老师，点击箭头移动到左边，点击确定即可完成下属添加。
[图片: 员工管理功能介绍]
[图片: 员工管理功能介绍]

图片说明：员工管理功能介绍
图片说明：员工管理功能介绍
图片说明：员工管理功能介绍
图片说明：员工管理功能介绍
图片说明：员工管理功能介绍
```

### chunk_d7d37447e9b6be851bba899e6d03d638 | 快速玩转入学模考

- source_id：helpcenter:93
- document_id：doc_helpcenter_93
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:32:37
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061408594874311909782715467", "alt_text": "发送入学模考的方式", "ocr_text": null, "caption": "发送入学模考的方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061403095211967967465054333", "alt_text": "发送入学模考的方式", "ocr_text": null, "caption": "发送入学模考的方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061403141902164540882950270", "alt_text": "发送入学模考的方式", "ocr_text": null, "caption": "发送入学模考的方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061357095187799829608325779", "alt_text": "学生完成模考", "ocr_text": null, "caption": "学生完成模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061405043550763695754467760", "alt_text": "学生完成模考", "ocr_text": null, "caption": "学生完成模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061406067653608126324582668", "alt_text": "老师批改模考", "ocr_text": null, "caption": "老师批改模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306140657483406353554147012", "alt_text": "老师批改模考", "ocr_text": null, "caption": "老师批改模考"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306140743331142311432142970", "alt_text": "老师批改模考", "ocr_text": null, "caption": "老师批改模考"}]

```text
快速玩转入学模考
快速玩转入学模考
国际教育机构通常需要为咨询潜客进行入学测试，校校系统专为机构在网页端配备多套入学模考测试，包括托福、雅思、SAT、SAT机考、小托福、ACT和基础能力测试，并支持机构根据内部要求进行隐藏或修改模考试卷。
入学模考能为机构提供什么帮助？
在机构网页端右上角配有“入学模考测试”，专为机构引流潜客新生及机构宣传，吸引流量。
同时支持一键复制试题链接，学生无需等待，只要将其复制到Chrome谷歌浏览器，输入手机号和验证码即可做题。
发送入学模考的方式
1）机构网页端右上角可进入【入学模考】页面，可以看到所有的可测试题目，可以复制网页链接给学生，并告知学生需要做的题目
[图片: 发送入学模考的方式]
2）系统内可进入入学模考页面，可一键选择试题，【复制试题链接】发送给学生作答
[图片: 发送入学模考的方式]
[图片: 发送入学模考的方式]
学生完成模考
学生完成入学模考后，系统可自动获取学生入学模测的结果
1）如果学生在系统首页进行入学模考，有选择推荐人（销售），那么该潜客信息会直接进入到对应销售的“潜客”中 
注:学生通过试题具体链接做题，不用填写推荐人，来源默认为发送链接的人，销售发送的链接默认推荐人为该销售
[图片: 学生完成模考]
2）如果学生没有填写推荐人，则潜客信息会进入到校长或销售管理员的公池中，需要再去进行潜客分配跟进。
[图片: 学生完成模考]
老师批改模考
学生完成入学模考之后，对应销售、销售管理员、校长可以查看学生的入学模考详情
注：如果销售不能查看学生入学模考，需要和校长/教务确认是否有查看学生入学模考的权限
1）销售将学生入学模考的结果页二维码分享给老师
[图片: 老师批改模考]
2）老师在电脑上登陆校校系统，打开学生入学模考二维码，复制链接到谷歌浏览器，即可批改学生模考
[图片: 老师批改模考]
3)老师批改之后，再发送保存二维码图片给销售，销售可以继续跟进学生
[图片: 老师批改模考]

图片说明：发送入学模考的方式
图片说明：发送入学模考的方式
图片说明：发送入学模考的方式
图片说明：学生完成模考
图片说明：学生完成模考
图片说明：老师批改模考
图片说明：老师批改模考
图片说明：老师批改模考
```

### chunk_2d4137476580fea2cede1b71639ab0cd | 学生做作业时，如何处理无法加载的情况？

- source_id：helpcenter:104
- document_id：doc_helpcenter_104
- 分类：热门问题
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:25:14
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121824543463690255953227145", "alt_text": "三、浏览器缓存已满", "ocr_text": null, "caption": "三、浏览器缓存已满"}]

```text
学生做作业时，如何处理无法加载的情况？
学生做作业时，如何处理无法加载的情况？
当学生点击进入作业时，发现作业页面加载不出来的现象，可通过以下文档排查。
一、浏览器使用不正确
当学生未使用正确浏览器时，可能会出现兼容性问题或者不稳定的情况
【解决方法】：
确认一下学生是否使用的正确的浏览器，建议【电脑使用谷歌浏览器，iPad使用safari浏览器】
二、学生网络环境不佳
当学生的网络环境异常或不稳定时会造成作业加载慢的问题；网络环境不佳只会影响当前网络环境下的学生
【解决办法】：
首先可以让学生刷新页面，刷新之后重新尝试打开作业，检查网络是否稳定，学生可以更换网络再次尝试打开作业
三、浏览器缓存已满
当学生的浏览器缓存增多的时候，会导致页面卡顿或加载缓慢
【解决办法】：
清理浏览器缓存，步骤如下：
1：打开浏览器设置，选择隐私设置和安全性
2：选择清除浏览数据，将时间范围选为不限
3：清楚数据之后，重新登录学生账号
[图片: 三、浏览器缓存已满]

图片说明：三、浏览器缓存已满
```

### chunk_930ac09f158e9623b6bdfe5975e6cb69 | 学生做作业过程，会有做题过程的一些监控手段吗？

- source_id：helpcenter:162
- document_id：doc_helpcenter_162
- 分类：使用技巧
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:18:51
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061048092811813445122772154", "alt_text": "总答题时长及单个题目答题时长", "ocr_text": null, "caption": "总答题时长及单个题目答题时长"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061048343737456913378837503", "alt_text": "答题时间段详情分析", "ocr_text": null, "caption": "答题时间段详情分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061050337786344688035750119", "alt_text": "学生作答录屏", "ocr_text": null, "caption": "学生作答录屏"}]

```text
学生做作业过程，会有做题过程的一些监控手段吗？
学生做作业过程，会有做题过程的一些监控手段吗？
有的，系统会在学生完成作业的过程中，后台多手段实时跟踪反馈学生做题过程的认真程度，包括：总答题时长，单个题目答题时长，答题次数及时间详情记录，答题过程实时录屏。
这些数据均会在老师端查看到的学生作业结果页中体现，具体如下图：
总答题时长及单个题目答题时长
学生做题过程系统自动记录总答题时长及单个题目的具体答题时间。
[图片: 总答题时长及单个题目答题时长]
答题时间段详情分析
答题时间段分析，包括答题次数及对应具体答题时间详情！
以学生进入作业页面开始计算为第一次做题，屏幕失焦（做题过程中切出做题页面或打开微信等其他程序）则显示中断答题，以此计算每次作业的答题次数以及答题具体时间！
[图片: 答题时间段详情分析]
学生作答录屏
学生整个做题过程的鼠标操作轨迹，中断答题操作都会被完整录屏记录下来，老师在自己端口可以看到学生答题详细过程的记录！
[图片: 学生作答录屏]

图片说明：总答题时长及单个题目答题时长
图片说明：答题时间段详情分析
图片说明：学生作答录屏
```

### chunk_1a56a5009ba03e3713915b597936c3ed | 2026托福改革，校校全新模考系统已经就位！

- source_id：helpcenter:239
- document_id：doc_helpcenter_239
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2025-10-20T10:54:53
- 图片数：38
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554105640513145150860657", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559408454352436002697599", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559477757171154934877718", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559566471868020836988825", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600013583993304671624270", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601457489636603459946459", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051602482203233929042370738", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049211789358611750713100", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049364924087743957887950", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050127448490949825089753", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050244395172588486522451", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050347217383418914529581", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050469158911350338295347", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050598508803312517949549", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105109471413468396571616", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051208382602050842605998", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051304925213941193254975", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105136254384958757750373", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051416008210681646435112", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051462980194901446426958", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051562541160414513656935", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052098887784637567536778", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052227455394327151762315", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052317851683800227453387", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052414172871081750860894", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052517958684496188673548", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053028495776687012334020", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053118158996912059660219", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053162653203804293146440", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053228904835314204864207", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053435920448046343161270", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053484225789167940449775", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053521712714823547756063", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054076531733098186258231", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054184972808893302015284", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054265441375589641076750", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054395196690866997354884", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054503841475130121324906", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
2026托福改革，校校全新模考系统已经就位！
2026托福改革，校校全新模考系统已经就位！
2026年1月21日起，托福考试将实施颠覆性的改革，校校已完成新托福模考系统升级，全面适配新版题型、评分与AI批改，给老师和学生带来更高效的考试体验！
老师组卷布置模考测试
老师可以在作业-模考测试/题型训练页面，选择新托福进行作业布置。
[图片: 老师组卷布置模考测试]
布置整套模考测试，可以按照阅读： Module Router（四个模块）+Lower/Upper（四个模块），听力：Module Router（四个模块）+Lower/Upper（四个模块），写作：造句+邮件+学术讨论，口语：复述+模拟面试，进行组卷，一键布置给学生。布置时勾选AI批改即可自动批改学生口语写作！
[图片: 老师组卷布置模考测试]
[图片: 老师组卷布置模考测试]
[图片: 老师组卷布置模考测试]
[图片: 老师组卷布置模考测试]
老师也可以在题库页面，勾选对应题目开放给学生自主练习，在已开放题目或者学员管理中随时查看学生练习情况，精准定位学生薄弱环节。
[图片: 老师组卷布置模考测试]
入学模考新增新托福板块，老师可联系校校推送机构专属入学模考试卷，招生转化更轻松！
[图片: 老师组卷布置模考测试]
学生端全新答题流程
学生答题前需要进行听力、口语测试，可以调节音量，测试麦克风声音大小，确保考试可以正常进行。
[图片: 学生端全新答题流程]
阅读部分
阅读部分包括两个module，约35-48题，答题时长大约为18-27分钟。
学生在引导页面可以查看阅读考察题型以及要求，点击Begin即可开始答题。
[图片: 学生端全新答题流程]
Module 1
学生首先需要作答Complete the Words题型，共10个空，学生需要根据段落填写单词缺失的字母，填写完会自动跳到下一空，点Next即可继续答题。
[图片: 学生端全新答题流程]

图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_ca9a79cdf3c3619b2e0494f258d2ad9a | 2026托福改革，校校全新模考系统已经就位！

- source_id：helpcenter:239
- document_id：doc_helpcenter_239
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：1
- 状态：active
- 更新时间：2025-10-20T10:54:53
- 图片数：38
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554105640513145150860657", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559408454352436002697599", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559477757171154934877718", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559566471868020836988825", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600013583993304671624270", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601457489636603459946459", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051602482203233929042370738", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049211789358611750713100", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049364924087743957887950", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050127448490949825089753", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050244395172588486522451", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050347217383418914529581", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050469158911350338295347", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050598508803312517949549", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105109471413468396571616", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051208382602050842605998", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051304925213941193254975", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105136254384958757750373", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051416008210681646435112", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051462980194901446426958", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051562541160414513656935", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052098887784637567536778", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052227455394327151762315", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052317851683800227453387", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052414172871081750860894", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052517958684496188673548", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053028495776687012334020", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053118158996912059660219", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053162653203804293146440", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053228904835314204864207", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053435920448046343161270", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053484225789167940449775", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053521712714823547756063", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054076531733098186258231", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054184972808893302015284", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054265441375589641076750", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054395196690866997354884", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054503841475130121324906", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
接着学生需要作答Read in Daily Life：生活化阅读2篇共6题。涵盖海报、菜单、社交媒体帖子或网页等日常素材。学生完成答题后可以点击Next继续答题，或点击Back返回上一题。
[图片: 学生端全新答题流程]
最后是Academic Passage：学术文章。题型涵盖否定信息题、推断题、词汇题、修辞题，段落关系题。点击Next继续答题，或点击Back返回上一题。
[图片: 学生端全新答题流程]
Module 2 
阅读Module 2和Module1题型一样，包括Complete the Words、Read in Daily Life、Read an Academic Passage，作答流程也与Module1一致。
注意：学生在作答Module2时，不能再返回Module1答题。
[图片: 学生端全新答题流程]
听力部分
听力部分包括两个Module，听力材料包括问答、对话、公告、学术讲座，约35-45题，答题时长大约为18-27分钟。
学生在引导页面可以查看听力考察题型以及要求，点击Begin即可开始答题。
[图片: 学生端全新答题流程]
Module 1 
学生进入答题页面后可以查看Module1答题要求，点击Next即可开始答题。
[图片: 学生端全新答题流程]
学生需要先听完音频后才会自动进入答题页面，点击Next即可继续答题。
[图片: 学生端全新答题流程]
学生作答Conversations，Announcements，Academic Talks题型时，需要听对话、通知、学术讨论完成对应题目。
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
在听力答题过程中，如果有未选择答案点击Next的情况，系统会提示需要选择答案才能离开此题，确保学生答题无遗漏。
[图片: 学生端全新答题流程]

图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_8c365261b7cc49b64fe73d230ef71fdb | 2026托福改革，校校全新模考系统已经就位！

- source_id：helpcenter:239
- document_id：doc_helpcenter_239
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：2
- 状态：active
- 更新时间：2025-10-20T10:54:53
- 图片数：38
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554105640513145150860657", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559408454352436002697599", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559477757171154934877718", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559566471868020836988825", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600013583993304671624270", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601457489636603459946459", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051602482203233929042370738", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049211789358611750713100", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049364924087743957887950", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050127448490949825089753", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050244395172588486522451", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050347217383418914529581", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050469158911350338295347", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050598508803312517949549", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105109471413468396571616", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051208382602050842605998", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051304925213941193254975", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105136254384958757750373", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051416008210681646435112", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051462980194901446426958", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051562541160414513656935", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052098887784637567536778", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052227455394327151762315", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052317851683800227453387", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052414172871081750860894", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052517958684496188673548", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053028495776687012334020", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053118158996912059660219", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053162653203804293146440", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053228904835314204864207", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053435920448046343161270", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053484225789167940449775", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053521712714823547756063", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054076531733098186258231", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054184972808893302015284", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054265441375589641076750", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054395196690866997354884", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054503841475130121324906", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
Module 2
听力部分Module2和Module1一样，包括Listen and Choose a Response，Conversations，Announcements、Academic Talks题型，答题时间与流程均与Module 1一致。
[图片: 学生端全新答题流程]
写作部分
写作部分保留学术写作，移除了综合写作，新增选词造句、邮件写作题型，共12题，考试时长约23分钟
学生在引导页面可以查看写作考察题型以及要求，点击Continue即可开始答题。
[图片: 学生端全新答题流程]
学生进入写作部分后，需要先完成Build a Sentence：选词造句题，选择词语组成语法正确的句子。一共10道题目，点击Next即可继续作答。
[图片: 学生端全新答题流程]
Write an Email：邮件写作，学生需要根据场景在7分钟内完成，需要注重格式、语气与逻辑。
[图片: 学生端全新答题流程]
Academic Discussion：学术讨论，和改革前一致，学生作答完成点击Next即可进入口语答题。
[图片: 学生端全新答题流程]
口语部分
口语部分题型为句子复述和模拟面试，共11题，答题时长约8分钟。
学生在引导页面可以查看口语考察题型以及要求，点击Continue即可开始答题。
[图片: 学生端全新答题流程]
学生进入口语部分后，需要先完成Listen and Repeat：句子复述题，共7题，没有准备时间，学生需要在10秒内完成答题，即时记忆要求较高。
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
Interview：模拟面试，共4个问题，每个问题答题时长45秒。答题时长结束后自动跳到下一个问题。学生答题完成后，点击Submit即可完成交卷。
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
[图片: 学生端全新答题流程]
AI智能批改

图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_c12fd9fec8acbe51f555ffb787f1c02a | 2026托福改革，校校全新模考系统已经就位！

- source_id：helpcenter:239
- document_id：doc_helpcenter_239
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：3
- 状态：active
- 更新时间：2025-10-20T10:54:53
- 图片数：38
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554105640513145150860657", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559408454352436002697599", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559477757171154934877718", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559566471868020836988825", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600013583993304671624270", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601457489636603459946459", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051602482203233929042370738", "alt_text": "老师组卷布置模考测试", "ocr_text": null, "caption": "老师组卷布置模考测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049211789358611750713100", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201049364924087743957887950", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050127448490949825089753", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050244395172588486522451", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050347217383418914529581", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050469158911350338295347", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201050598508803312517949549", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105109471413468396571616", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051208382602050842605998", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051304925213941193254975", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20251020105136254384958757750373", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051416008210681646435112", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051462980194901446426958", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201051562541160414513656935", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052098887784637567536778", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052227455394327151762315", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052317851683800227453387", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052414172871081750860894", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201052517958684496188673548", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053028495776687012334020", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053118158996912059660219", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053162653203804293146440", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053228904835314204864207", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053435920448046343161270", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053484225789167940449775", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201053521712714823547756063", "alt_text": "学生端全新答题流程", "ocr_text": null, "caption": "学生端全新答题流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054076531733098186258231", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054184972808893302015284", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054265441375589641076750", "alt_text": "AI智能批改", "ocr_text": null, "caption": "AI智能批改"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054395196690866997354884", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202510201054503841475130121324906", "alt_text": "学生查看模考测试结果", "ocr_text": null, "caption": "学生查看模考测试结果"}]

```text
模拟面试口语AI智能批改
校校AI智能批改根据官方维度，分析学生的发音、流利度，从Task Completion & Elaboration、Language Use、Delivery进行分项批改， 帮助学生作答“练习-反馈-修正”的高效闭环。
[图片: AI智能批改]
邮件写作AI智能批改
校校AI针对邮件题型写作，根据口语批改标准，结合学生写作，进行Task Completion & Elaboration（任务阐述）、Language Use（语言使用）、Vocabulary & Register（词汇与语域）、Grammar & Lexical Accuracy（语法词汇准确性）分项批改，快速完成批改，解放老师时间。
[图片: AI智能批改]
学术写作AI智能批改
学术写作批改包括Content、Organization、Grammatical Range and Accuracy、Vocabulary。精确到某个句子语法错误、某个词汇使用不当、段落之间逻辑衔接不紧密等细节问题，错误类型、薄弱知识点都会被记录和分析，让进步看得见！
[图片: AI智能批改]
学生查看模考测试结果
校校托福测试报告也进行了全新改版，基于新版评分标准，新增6分的四科分与总分；和120分制同时显示，可以直接对标CEFR 等级！学生整体题型分析老师也能直接查看，添加分项精准评价！
[图片: 学生查看模考测试结果]
结果页详情展示学生具体作答情况，客观题自动批改，错题及时定位，精准分析学生知识点掌握薄弱点，帮助学生更好的进步!
[图片: 学生查看模考测试结果]

图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：老师组卷布置模考测试
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：学生端全新答题流程
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：AI智能批改
图片说明：学生查看模考测试结果
图片说明：学生查看模考测试结果
```

### chunk_fe1f02f5280eab788799cec5a4ec2b94 | 入门必备-教务创建学员账号

- source_id：helpcenter:67
- document_id：doc_helpcenter_67
- 分类：初次使用指南
- 适用角色库：student(学生库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T13:19:03
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442174921995357675372001", "alt_text": "创建学员账号", "ocr_text": null, "caption": "创建学员账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442212621456139307617286", "alt_text": "创建学员账号", "ocr_text": null, "caption": "创建学员账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442424248716760579346786", "alt_text": "创建学员账号", "ocr_text": null, "caption": "创建学员账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442578299820898427324312", "alt_text": "创建学员账号", "ocr_text": null, "caption": "创建学员账号"}]

```text
入门必备-教务创建学员账号
入门必备-教务创建学员账号
机构有两种方式可以添加学院账号，第一种是从销售端口完成签约流程进入机构的正式学员，第2种由教务直接添加学生账号，教务添加学生账号更适用于机构有老学员，或者线下签约的学生
创建学员账号
点击左侧导航栏"学员”找到“添加学员”即可填写学生的基本信息，学生年级会在每年9月1日自动变化
可以在账号管理处选择VIP或非VIP账号，注意：如果要进行作业练习的学生请选择VIP账号。
如果需要学生家长了解学生的上课课表以及作业情况，可以输入家长的电话号码，家长可以绑定公众号，可以收到学生的课堂反馈和作业完成进度
[图片: 创建学员账号]
[图片: 创建学员账号]
[图片: 创建学员账号]
如果学生有相关的报名课程及信息，可以填写在报名课程处
[图片: 创建学员账号]

图片说明：创建学员账号
图片说明：创建学员账号
图片说明：创建学员账号
图片说明：创建学员账号
```

### chunk_ca1d6ea75a39b943952e786fa313341c | 快速玩转老师端小程序

- source_id：helpcenter:75
- document_id：doc_helpcenter_75
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T14:56:11
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412135661474212659585850", "alt_text": "老师登录小程序", "ocr_text": null, "caption": "老师登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121428285302712530571729731", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121428347607718220099281353", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121428416726048325938945748", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230412143024494304884639892082", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121430311246452560593965774", "alt_text": "老师班级管理", "ocr_text": null, "caption": "老师班级管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121430436332610823333719733", "alt_text": "老师查看数据报告", "ocr_text": null, "caption": "老师查看数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061418536117967461917497255", "alt_text": "学生登录小程序", "ocr_text": null, "caption": "学生登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121449348507097726283984404", "alt_text": "学生查看课表", "ocr_text": null, "caption": "学生查看课表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121450188587196285635667857", "alt_text": "学生查看课堂反馈", "ocr_text": null, "caption": "学生查看课堂反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121451113994096382502106419", "alt_text": "学生查看黑板报", "ocr_text": null, "caption": "学生查看黑板报"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121453044296392873815354319", "alt_text": "学生完成作业", "ocr_text": null, "caption": "学生完成作业"}]

```text
快速玩转老师端小程序
快速玩转老师端小程序
系统专门为老师和学生提供小程序服务
老师可通过小程序快速管理班级、作业、课堂反馈、课表、黑板报、数据报告等功能！
学生可通过小程序快速完成作业、查看课表、课堂反馈和黑板报等功能！
老师登录小程序
老师进入系统首页，点击右上角菜单栏-小程序按钮，弹出小程序二维码，老师扫码即可登录小程序。
[图片: 老师登录小程序]
老师工作台
老师登录小程序，在首页-【工作台】中，老师可以快速完成作业管理、课堂反馈、课表查看、黑板报发布等功能。
作业管理：在工作台上方菜单栏中点击【作业】按钮，可对班级作业进行筛选，查看作业的完成情况，提高作业管理效率。
[图片: 老师工作台]
课堂反馈：在工作台上方菜单栏中点击【反馈】按钮，可对课堂反馈进行筛选，快捷添加课堂反馈。
[图片: 老师工作台]
查看课表：在工作台上方菜单栏中点击【课表】按钮，可按日期筛选查看老师当日排课；查看上课时间、地点；手动设置学生考勤。
[图片: 老师工作台]
查看黑板报：在工作台上方菜单栏中点击【黑板报】按钮，可快捷发布黑板报、筛选黑板报类型、查看黑板报内容。
[图片: 老师工作台]
老师班级管理
老师点击下方导航中的【班级】按钮，在小程序端进行班级管理，查看班级的相关信息和状态；点击对应班级可在小程序端进行班级的作业管理。
[图片: 老师班级管理]
老师查看数据报告
老师点击下方导航中的【数据报告】按钮，在小程序端查看相关的教学数据报告；包含周作业正确率统计；当日、当周、当月和当季对应的教学数据报告；以及学生的作业完成率和正确率的排行榜。
[图片: 老师查看数据报告]
学生登录小程序
学生进入系统首页，点击右上角菜单栏-小程序按钮，弹出小程序二维码，学生扫码即可登录小程序。
[图片: 学生登录小程序]
学生端小程序功能
学生登录小程序，在小程序首页中，学生可以快速完成课表课程，课堂反馈以及老师发布黑板报的查阅，同时学生也能通过小程序查看并完成自己的作业。
学生查看课表

图片说明：老师登录小程序
图片说明：老师工作台
图片说明：老师工作台
图片说明：老师工作台
图片说明：老师工作台
图片说明：老师班级管理
图片说明：老师查看数据报告
图片说明：学生登录小程序
图片说明：学生查看课表
图片说明：学生查看课堂反馈
图片说明：学生查看黑板报
图片说明：学生完成作业
```

### chunk_a261d8abebae48604a765d05d0785d57 | 快速玩转老师端小程序

- source_id：helpcenter:75
- document_id：doc_helpcenter_75
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T14:56:11
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412135661474212659585850", "alt_text": "老师登录小程序", "ocr_text": null, "caption": "老师登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121428285302712530571729731", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121428347607718220099281353", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121428416726048325938945748", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230412143024494304884639892082", "alt_text": "老师工作台", "ocr_text": null, "caption": "老师工作台"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121430311246452560593965774", "alt_text": "老师班级管理", "ocr_text": null, "caption": "老师班级管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121430436332610823333719733", "alt_text": "老师查看数据报告", "ocr_text": null, "caption": "老师查看数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061418536117967461917497255", "alt_text": "学生登录小程序", "ocr_text": null, "caption": "学生登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121449348507097726283984404", "alt_text": "学生查看课表", "ocr_text": null, "caption": "学生查看课表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121450188587196285635667857", "alt_text": "学生查看课堂反馈", "ocr_text": null, "caption": "学生查看课堂反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121451113994096382502106419", "alt_text": "学生查看黑板报", "ocr_text": null, "caption": "学生查看黑板报"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121453044296392873815354319", "alt_text": "学生完成作业", "ocr_text": null, "caption": "学生完成作业"}]

```text
学生在小程序首页，点击上方菜单栏的【课表】按钮，可以根据日历查看对应日期的相关课程，包括课程名称、上课时间、上课地点、对应班级及考勤状态等。
[图片: 学生查看课表]
学生查看课堂反馈
学生在小程序首页，点击上方菜单栏的【反馈】按钮，可以查看老师给学生的课堂反馈，其中包含对学生课堂相关项的评分以及给学生的学习建议。
[图片: 学生查看课堂反馈]
学生查看黑板报
学生在小程序首页，点击上方菜单栏的【黑板报】按钮，可以快捷查看老师新发布的黑板报；新发布的作业以及课程相关的通知等，都可以在这里查看。
[图片: 学生查看黑板报]
学生完成作业
学生登录小程序，点击下方导航栏的【作业】按钮，即可在小程序端快速查看对应班级的作业以及作业的完成状态；对未完成的作业也可以在小程序端进行快捷的作答。
[图片: 学生完成作业]

图片说明：老师登录小程序
图片说明：老师工作台
图片说明：老师工作台
图片说明：老师工作台
图片说明：老师工作台
图片说明：老师班级管理
图片说明：老师查看数据报告
图片说明：学生登录小程序
图片说明：学生查看课表
图片说明：学生查看课堂反馈
图片说明：学生查看黑板报
图片说明：学生完成作业
```

### chunk_ead8350b8ffabc159985118e92114849 | 如何解决无法登录系统的情况？

- source_id：helpcenter:105
- document_id：doc_helpcenter_105
- 分类：热门问题
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:31:05
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061107416934485026077115428", "alt_text": "三、账号、密码信息不正确", "ocr_text": null, "caption": "三、账号、密码信息不正确"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061107507157914674566829397", "alt_text": "三、账号、密码信息不正确", "ocr_text": null, "caption": "三、账号、密码信息不正确"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061107548479940401387660989", "alt_text": "三、账号、密码信息不正确", "ocr_text": null, "caption": "三、账号、密码信息不正确"}]

```text
如何解决无法登录系统的情况？
如何解决无法登录系统的情况？
当学生/员工登陆系统，发现系统页面加载不出来或账号无法登陆的现象时，可以通过以下文档排查。
一、浏览器使用不正确
当学生/员工未使用正确浏览器时，可能会出现兼容性问题或者不稳定的情况
【解决方法】：
确认一下学生/员工是否使用的正确的浏览器，建议电脑使用谷歌浏览器，iPad使用safari浏览器
二、网址不正确
当学生/员工未输入正确的网址时，可能会出现系统无法打开的情况
【解决方法】：
确认学生/员工输入的网址是否正确（如果背景图不符合机构的背景图，就是网址错误）
三、账号、密码信息不正确
当学生/员工老师未输入正确的账号或密码时，可能会出现系统无法登陆的情况
【解决方法】：
确认学生/员工的账号、密码信息是否正确
如果忘记账号密码，可以在首页账号信息登陆处，点击忘记密码，进行密码重置
[图片: 三、账号、密码信息不正确]
教务端/校长端可以在【学员管理】和【员工管理】--编辑中重置密码。注：修改学生密码时不要修改到家长的密码了哦
[图片: 三、账号、密码信息不正确]
[图片: 三、账号、密码信息不正确]

图片说明：三、账号、密码信息不正确
图片说明：三、账号、密码信息不正确
图片说明：三、账号、密码信息不正确
```

### chunk_830ef955a2b225d5f10ad29f58296f7e | 老师可以看到学生的错题分析吗？

- source_id：helpcenter:163
- document_id：doc_helpcenter_163
- 分类：使用技巧
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:19:26
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061051222219905153909570660", "alt_text": "老师/助教端查看学生错题分析", "ocr_text": null, "caption": "老师/助教端查看学生错题分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061051516794460777060245222", "alt_text": "老师/助教端查看学生错题分析", "ocr_text": null, "caption": "老师/助教端查看学生错题分析"}]

```text
老师可以看到学生的错题分析吗？
老师可以看到学生的错题分析吗？
当然可以，老师可以在老师端口查看到自己所带所有学生的做题分析，具体查看方式如下：
老师/助教端查看学生错题分析
老师/助教点击学员，搜索选择需要查看做题的学生，点击练习情况，即可查看错题分析。
[图片: 老师/助教端查看学生错题分析]
点击“查看详情”即可查看具体错题，或二次布置给学习练习。
[图片: 老师/助教端查看学生错题分析]

图片说明：老师/助教端查看学生错题分析
图片说明：老师/助教端查看学生错题分析
```

### chunk_f73472ac3dcb21fdd156d57caf8d1b93 | 一文了解：如何进行学员管理

- source_id：helpcenter:247
- document_id：doc_helpcenter_247
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2026-03-05T11:49:21
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051146475615037418699768573", "alt_text": "添加学生", "ocr_text": null, "caption": "添加学生"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051148074223226902337466491", "alt_text": "学生账号续期、停用", "ocr_text": null, "caption": "学生账号续期、停用"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051148431499624464561811162", "alt_text": "学生信息查看", "ocr_text": null, "caption": "学生信息查看"}]

```text
一文了解：如何进行学员管理
一文了解：如何进行学员管理
教务可以在学员管理进行学生的信息录入以及学生账号的续期停用操作
添加学生
点击左侧导航栏"学员”找到“新增”即可填写学生的基本信息，学生年级会在每年9月1日自动变化
可以在账号管理处选择VIP或非VIP账号，注意：如果要进行作业练习的学生请选择VIP账号。
如果需要学生家长了解学生的上课课表以及作业情况，可以输入家长的电话号码，家长可以绑定公众号，可以收到学生的课堂反馈和作业完成进度
[图片: 添加学生]
学生账号续期、停用
教务可以点击学生账号旁边的小圆点，进行账号续期、停用
[图片: 学生账号续期、停用]
学生信息查看
学生的基本信息、课表任务、学习报告、课程反馈、合同、回访记录、考试记录都可以在学员管理查看
[图片: 学生信息查看]

图片说明：添加学生
图片说明：学生账号续期、停用
图片说明：学生信息查看
```

### chunk_009ee392aa15c618a2184287d2492e10 | AI 排课 + 调课有更新！教务轻松搞定学期课表

- source_id：helpcenter:248
- document_id：doc_helpcenter_248
- 分类：新功能上线
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2026-05-09T18:39:21
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091831123293475964753919643", "alt_text": "01 AI排课", "ocr_text": null, "caption": "01 AI排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091834381414606323547271746", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091834449177680216090315040", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091840012940637718225263965", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091840245173725182557869381", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091840533332844943730572135", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091936527439880513672709015", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260509184133284972787463928030", "alt_text": "02 调课优化", "ocr_text": null, "caption": "02 调课优化"}]

```text
AI 排课 + 调课有更新！教务轻松搞定学期课表
AI 排课 + 调课有更新！教务轻松搞定学期课表
在国际学校的日常教务管理中
排课、调课一直是老师们最头疼的任务
新开班级时要安排课程、教师与教室
临时课程调整时又要兼顾各班冲突
为此，校校带来了全新的AI排课与调课功能
让排课、调课流程变得智能、高效、可视化！
01 AI排课
校校AI排课更懂老师的需求！以往面对复杂排课可能存在排课冲突，排课数不对应的情况，校校AI排课全新升级，经过千次学校实际场景，不同复杂排课情况模拟，生成最优排课方案，提升老师排课效率！
[图片: 01 AI排课]
02 调课优化
课表优化：校校课表显示优化，课程展示更紧凑，老师查看课程更清晰。课表中直接显示授课教师和教室，无需老师二次点击查看，操作更便捷。课程组和非课程组的课程显示通过样式区分，非课程组显示老师和教室，课程组显示展开图标，一目了然。
[图片: 02 调课优化]
[图片: 02 调课优化]
调课批量操作：老师可以在课表一键勾选同一时间段的课程，进行发布、快速调课、删除等操作。点击快速调课，系统会展示课程表，如果有与已选课程冲突的时间段，系统会提前标明，老师可以直接点击需要调整的对应时间段，完成调课。
[图片: 02 调课优化]
[图片: 02 调课优化]
老师可以多选已发布的课程进行批量取消课程。
[图片: 02 调课优化]
如果有需要调整不同课程到同一天的情况，老师可以多选课程，同时打包拖动到课程格
[图片: 02 调课优化]
新增课程待排区：老师可以将未发布的课程拖入待排区，方便临时存放未排或待调整课程，排课节奏更可控。
[图片: 02 调课优化]

图片说明：01 AI排课
图片说明：02 调课优化
图片说明：02 调课优化
图片说明：02 调课优化
图片说明：02 调课优化
图片说明：02 调课优化
图片说明：02 调课优化
图片说明：02 调课优化
```

### chunk_ecee0d95ca77f9d83d16026865f47faf | 入门必备-教务创建课程班级

- source_id：helpcenter:68
- document_id：doc_helpcenter_68
- 分类：初次使用指南
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T13:29:21
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051451405521142065496448725", "alt_text": "创建课程", "ocr_text": null, "caption": "创建课程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051451515800309589321984792", "alt_text": "创建课程", "ocr_text": null, "caption": "创建课程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051452036684887036752831576", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051452133907022741170177277", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051452218663473451909848899", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051452255701655535192975527", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}]

```text
入门必备-教务创建课程班级
入门必备-教务创建课程班级
在新学员进入之后，教务老师需要根据其报名的科目，创建课程和班级，让学生可以更快进入学习状态。
创建课程
点击左侧导航栏【课程】，找到添加按钮，可以编辑课程名称类别，课程类别可以自行添加不同科目，在选择好课程类别之后，需要关联相关科目的题库，才能给学生布置相关科目的作业。
课程类型可以选择班课和定制课，班课的课程总价和课时总数是固定的，定制课可以根据学生需求进行调整
[图片: 创建课程]
老师可以根据课程，制定不同的【上课内容】，支持修改和删除。创建好课程之后，如果该上课内容已有排课，则不允许删除对应的上课内容。如果这个课程下面创建了班级，也不允许删除这个课程。
[图片: 创建课程]
创建班级
课程创建好之后，老师需要创建班级，可以在导航栏点击班级按钮，点击创建班级即可以进行班级信息的编辑，可以选择校区、课程以及班级类型。选择【一对一】班级，需要老师手动填写班级名称。选择【一对多】班级，系统会自动匹配学期以及班级名称
[图片: 创建班级]
选择好班级类型之后，可以进行老师和助教的添加，选择开课日期和结束日期，可以进行课时的总设置以及班级状态的设置，班级状态可以设置为未开课已开课，已停课已结课的状态。
[图片: 创建班级]
创建好班级之后，教务老师可以选择添加学生到班级
[图片: 创建班级]
[图片: 创建班级]

图片说明：创建课程
图片说明：创建课程
图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
```

### chunk_259bb20f9591b86d8de7567421220329 | 快速玩转学生端小程序

- source_id：helpcenter:78
- document_id：doc_helpcenter_78
- 分类：热门文章
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T15:12:28
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061419493773452362062115181", "alt_text": "学生登录小程序", "ocr_text": null, "caption": "学生登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306142603587309169605519498", "alt_text": "学生查看课表", "ocr_text": null, "caption": "学生查看课表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061426548502713180233716138", "alt_text": "学生查看课堂反馈", "ocr_text": null, "caption": "学生查看课堂反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061427221896127799659314967", "alt_text": "学生完成作业", "ocr_text": null, "caption": "学生完成作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061427435080116358142094486", "alt_text": "单词书学习", "ocr_text": null, "caption": "单词书学习"}]

```text
快速玩转学生端小程序
快速玩转学生端小程序
学生可通过小程序快速完成作业，查看课表，课堂反馈和黑板报等功能。
学生登录小程序
学生进入系统首页，点击右上角菜单栏-小程序按钮，弹出小程序二维码，学生扫码即可登录小程序。
[图片: 学生登录小程序]
学生端小程序功能
学生登录小程序，可以快速查看课表、课堂反馈以及老师发布的黑板报，同时学生也能通过小程序查看并完成除模考作业外的其他作业以及单词书学习。
学生查看课表
学生在小程序首页，点击上方菜单栏的【课表】按钮，可以根据日历查看对应日期的相关课程，包括课程名称，上课时间，上课地点，对应班级及考勤状态等。
[图片: 学生查看课表]
学生查看课堂反馈
学生在小程序首页，点击上方菜单栏的【反馈】按钮，可以查看老师给学生的课堂反馈，其中包含对学生课堂相关项的评分以及给学生的学生建议。
[图片: 学生查看课堂反馈]
学生完成作业
学生登录小程序，点击下方导航栏的【作业】按钮，即可在小程序端快速查看对应班级的作业以及作业的完成状态；对未完成的作业也可以在小程序端进行快捷的作答。
[图片: 学生完成作业]
单词书学习
学生点击单词书即可查看目前已经学习的单词数、错词数。点击单词书可以进行单元的测试练习
[图片: 单词书学习]

图片说明：学生登录小程序
图片说明：学生查看课表
图片说明：学生查看课堂反馈
图片说明：学生完成作业
图片说明：单词书学习
```

### chunk_0a50118b1284dac2795f1349fdaa08f9 | 一文读懂：如何进行课程管理

- source_id：helpcenter:88
- document_id：doc_helpcenter_88
- 分类：核心功能介绍
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:18:55
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305140059292195963498500055", "alt_text": "课程管理功能介绍", "ocr_text": null, "caption": "课程管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305140138602271466384168674", "alt_text": "课程管理功能介绍", "ocr_text": null, "caption": "课程管理功能介绍"}]

```text
一文读懂：如何进行课程管理
一文读懂：如何进行课程管理
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍课程管理的功能。
课程管理功能介绍
可以在这里添加机构所开设的课程，按照要求填写课程名称、课程类别、关联对应科目题库、设置上课内容、填写课程介绍。
课程类别：即托福、雅思、ACT等 点击新增即可新增机构专属课程类别
上课内容：即听力、阅读、口语等具体上课内容
[图片: 课程管理功能介绍]
注：课程下有班级的课程，不允许删除！
可以在学杂处添加书本费、住宿费等费用标准，在创建订单时可以进行学杂费选择。
[图片: 课程管理功能介绍]

图片说明：课程管理功能介绍
图片说明：课程管理功能介绍
```

### chunk_fb4678fa498d98512b45e9e90c7db973 | 学生做题时，如何处理音频无法加载的情况？

- source_id：helpcenter:108
- document_id：doc_helpcenter_108
- 分类：热门问题
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:35:05
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121834503454130506374022535", "alt_text": "三、浏览器缓存已满", "ocr_text": null, "caption": "三、浏览器缓存已满"}]

```text
学生做题时，如何处理音频无法加载的情况？
学生做题时，如何处理音频无法加载的情况？
当学生完成作业时，发现音频加载不出来的现象，可以通过以下文档排查。
一、浏览器使用不正确
当学生未使用正确浏览器时，可能会出现兼容性问题或者不稳定的情况
【解决方法】：
确认一下学生是否使用的正确的浏览器，建议电脑使用谷歌浏览器，iPad使用safari浏览器
二、学生网络环境不佳
当学生的网络环境异常或不稳定时会造成音频加载卡顿或缓慢的问题；网络环境不佳只会影响当前网络环境下的学生
【解决办法】：
首先可以让学生多次刷新页面，让音频充分加载之后重新尝试进入作业打开音频。检查网络是否稳定，学生可以更换网络再次进入作业打开音频
三、浏览器缓存已满
当学生的浏览器缓存增多的时候，会导致页面卡顿或加载缓慢
【解决办法】：
清理浏览器缓存，步骤如下：
1：打开浏览器设置，选择隐私设置和安全性
2：选择清除浏览数据，将时间范围选为不限
3：清楚数据之后，重新登录学生账号
[图片: 三、浏览器缓存已满]
如以上操作均尝试后，仍无法解决问题，您可以提供：学生账号，作业名称，学生音频加载不出来的截图等。发送至校校小助手帮您处理！

图片说明：三、浏览器缓存已满
```

### chunk_5af2dc6d150e74016b84bc40ae349eca | 老师/助教如何快速查看自己的待批改作业？

- source_id：helpcenter:164
- document_id：doc_helpcenter_164
- 分类：使用技巧
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:21:04
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061052241572007339837631319", "alt_text": "老师快速查看自己的待批改作业", "ocr_text": null, "caption": "老师快速查看自己的待批改作业"}]

```text
老师/助教如何快速查看自己的待批改作业？
老师/助教如何快速查看自己的待批改作业？
老师可在自己账号的首页，快速一键点击查看自己的待批改作业。
老师快速查看自己的待批改作业
在老师账号首页，点击待办事项，“待批改作业”，老师可筛选班级查看。
[图片: 老师快速查看自己的待批改作业]

图片说明：老师快速查看自己的待批改作业
```

### chunk_93de3884cc5cc520e7147aa8dffcab60 | 国际学校校长教务的AI小新智能助手来了

- source_id：helpcenter:249
- document_id：doc_helpcenter_249
- 分类：新功能上线
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2026-05-09T19:46:56
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260509194418431633645090472882", "alt_text": "想查询更复杂的排课冲突？", "ocr_text": null, "caption": "想查询更复杂的排课冲突？"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091944537652145548443048540", "alt_text": "智能报表推送", "ocr_text": null, "caption": "智能报表推送"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091945203710510984214629022", "alt_text": "学生数据监控", "ocr_text": null, "caption": "学生数据监控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091945314598986202316843279", "alt_text": "学生数据监控", "ocr_text": null, "caption": "学生数据监控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091945461891058571212440796", "alt_text": "教师动态提醒", "ocr_text": null, "caption": "教师动态提醒"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091945501929363715927316993", "alt_text": "教师动态提醒", "ocr_text": null, "caption": "教师动态提醒"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091946088721659809584784469", "alt_text": "课程与班级管理", "ocr_text": null, "caption": "课程与班级管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260509194612256774037119370573", "alt_text": "课程与班级管理", "ocr_text": null, "caption": "课程与班级管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091946247722671235302238268", "alt_text": "德育表现监控", "ocr_text": null, "caption": "德育表现监控"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202605091946301900800176682955594", "alt_text": "德育表现监控", "ocr_text": null, "caption": "德育表现监控"}]

```text
国际学校校长教务的AI小新智能助手来了
国际学校校长教务的AI小新智能助手来了
校校AI助手新能力
让每位校长和教务老师
拥有专属的教学管理伙伴
随时监控、精准掌握、科学决策
在校校AI 即刻唤起
自己的AI智能伙伴
它会在课程安排、模考规划、学生数据中
随时提供分析与建议
掌握班级进度、薄弱知识点、资源使用情况
越来越懂你的管理需求
真正帮你高效教务、轻松决策，安全可靠
想查询更复杂的排课冲突？
试试AI助手智能问答
支持基于复杂课程和班级数据的智能提问
让你更快找到冲突、优化排课、全面掌控课程安排
[图片: 想查询更复杂的排课冲突？]
智能报表推送
AI助手帮您自动生成周报、月报、季报和年报
再也不用手动统计，让数据一目了然
[图片: 智能报表推送]
学生数据监控
实时发现考试成绩连续下滑
以及班级本周平均出勤率低的情况
快速锁定需要关注的学生和班级
[图片: 学生数据监控]
[图片: 学生数据监控]
教师动态提醒
分析本学期教学效果与学生提升
对比教师工作量与教学成果
及时预警，让教务调配更从容
[图片: 教师动态提醒]
[图片: 教师动态提醒]
课程与班级管理
掌握班级本周平均出勤率及异常情况
轻松查看每个班级的课堂动态
[图片: 课程与班级管理]
[图片: 课程与班级管理]
德育表现监控
及时发现学生违纪或不良记录连续出现
掌握德育管理重点，提前干预
[图片: 德育表现监控]
[图片: 德育表现监控]

图片说明：想查询更复杂的排课冲突？
图片说明：智能报表推送
图片说明：学生数据监控
图片说明：学生数据监控
图片说明：教师动态提醒
图片说明：教师动态提醒
图片说明：课程与班级管理
图片说明：课程与班级管理
图片说明：德育表现监控
图片说明：德育表现监控
```

### chunk_54990e3fa46b3527b47d083623d80900 | 入门必备-教务高效排课

- source_id：helpcenter:69
- document_id：doc_helpcenter_69
- 分类：初次使用指南
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T13:44:47
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051515546999630830364733015", "alt_text": "班级页面智能排课", "ocr_text": null, "caption": "班级页面智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516061006896419573163440", "alt_text": "班级页面智能排课", "ocr_text": null, "caption": "班级页面智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516152613675664167262294", "alt_text": "班级页面智能排课", "ocr_text": null, "caption": "班级页面智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516264791132031551701442", "alt_text": "班级页面传统排课", "ocr_text": null, "caption": "班级页面传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516402402611907554671280", "alt_text": "班级页面传统排课", "ocr_text": null, "caption": "班级页面传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516466883424692881656105", "alt_text": "班级页面传统排课", "ocr_text": null, "caption": "班级页面传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516566691297644335683890", "alt_text": "班级页面传统排课", "ocr_text": null, "caption": "班级页面传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051517043885111842682804529", "alt_text": "课表页面排课", "ocr_text": null, "caption": "课表页面排课"}]

```text
入门必备-教务高效排课
入门必备-教务高效排课
班级多、时间跨度长，如何帮助教务老师实现快速排课？出现特殊情况，排好的课需要调整应该如何操作？校校支持在班级排课和课表排课，可以选择智能排课或传统排课
班级页面智能排课
校校系统支持教务老师进行智能排课，点击导航栏“班级”，选择某个班级进入“排课”页面
[图片: 班级页面智能排课]
教务老师只需输入上课老师和上课时间两类信息，一键智能排课，系统自动排课并识别老师时间，学生时间以及上课地点冲突。
[图片: 班级页面智能排课]
排好的课表会显示未发布状态，教务老师可进行预览，觉得排课没问题点击确认发布即排课成功，觉得个别排课不合理也可拖动调整后再进行发布
[图片: 班级页面智能排课]
班级页面传统排课
传统排课需要老师选择好课程信息，上课时间地点，更适合课程少，或者特定课程使用
[图片: 班级页面传统排课]
校校系统提供添加设置常用时间段和上课地点，可以帮助教务老师高效率排课
1）教务老师可以在【设置-教学相关中】编辑上课时间和上课地点，以供传统排课的时候一键点选
2）教务老师排课时可以点击打开【常用时间】显示，点击任意灰色时间段就可以编辑课程了
[图片: 班级页面传统排课]
[图片: 班级页面传统排课]
教务老师可以选择需要导出课表的月份，校校支持一键导出PDF课表
[图片: 班级页面传统排课]
课表页面排课
教务老师在课表页面查看课表时也可以进行排课，点击视图模式，就可以一键排课了
[图片: 课表页面排课]

图片说明：班级页面智能排课
图片说明：班级页面智能排课
图片说明：班级页面智能排课
图片说明：班级页面传统排课
图片说明：班级页面传统排课
图片说明：班级页面传统排课
图片说明：班级页面传统排课
图片说明：课表页面排课
```

### chunk_7c9c5e5f66b74b99179ea4923896b617 | 销售端如何快速生成订单？

- source_id：helpcenter:77
- document_id：doc_helpcenter_77
- 分类：热门文章
- 适用角色库：sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T15:07:26
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061432054245707717758260129", "alt_text": "录入潜客学员信息", "ocr_text": null, "caption": "录入潜客学员信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061433065411900630643002737", "alt_text": "录入潜客学员信息", "ocr_text": null, "caption": "录入潜客学员信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061434073552857976640621352", "alt_text": "填写沟通记录", "ocr_text": null, "caption": "填写沟通记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061436287367915559979979749", "alt_text": "预约试听", "ocr_text": null, "caption": "预约试听"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061439263236603255072715708", "alt_text": "学员签约", "ocr_text": null, "caption": "学员签约"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061444103703715006514131839", "alt_text": "订单支付", "ocr_text": null, "caption": "订单支付"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061446469077131803756544360", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061448451870391610317358208", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306145027719083254752767047", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061453539172406978692713873", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061457224519526088083404453", "alt_text": "转为正式学员", "ocr_text": null, "caption": "转为正式学员"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306145938973732470581705483", "alt_text": "转为正式学员", "ocr_text": null, "caption": "转为正式学员"}]

```text
销售端如何快速生成订单？
销售端如何快速生成订单？
如何查看学员的入学模考成绩？如何快速生成订单？
潜客录入订单流程操作均在销售端进行！
1 分钟了解如何快速生成学员订单！
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202403141608261332782631566224111
录入潜客学员信息
第一步，在潜客中找到学员，若之前没有录入学员信息，即可点击左上角添加学员信息！
[图片: 录入潜客学员信息]
销售线索分不同跟进进度，可进行筛选，显示该销售人员跟进的客户，在这里可查看潜客的入学模测结果，点击编辑可进行潜客信息编辑，包括基础信息、学习目标、信息来源、沟通信息等，如下图：
[图片: 录入潜客学员信息]
填写沟通记录
沟通过程中可以不断完善基础信息、学习目标、信息来源等，并且在线填写沟通记录，这里的沟通信息包括潜客、跟进中、已预约、已试听、已签约等，所有沟通记录累积保存。填写沟通信息时，可设置下次沟通时间，系统会进行自动跟进提醒！
[图片: 填写沟通记录]
预约试听
已预约试听潜客学员信息会同步到教务的试听排课中，教务进行排课，需要同步给教务的其他课程信息要通过备注填写，填写在沟通记录中的信息不会同步给教务哦！
[图片: 预约试听]
学员签约
已转化的学员可以点击潜客右侧的编辑，下拉选择跟进进度为“已签约”，系统会自动生成学员订单，点击右侧导航栏订单即可查看，不会直接进入到教务端成为正式学生哦！
[图片: 学员签约]
订单支付
系统会自动弹出订单支付页面，选择付款方式，填写支付金额，上传支付凭证。添加好支付信息后，会直接同步到有审批权限的销售账号中，教务或校长端均可查看，并审批确认订单，即可转化为正式学员！
[图片: 订单支付]
订单审批
未付款的学生，销售可以在订单页面，找到未付款的订单，点击订单详情补交学费即可！
[图片: 订单审批]
也可点击“退费”，发起退费申请！
[图片: 订单审批]
具有审批权限的销售老师，可以点击“审批”查看订单的支付信息等，并进行审核确认！
[图片: 订单审批]

图片说明：录入潜客学员信息
图片说明：录入潜客学员信息
图片说明：填写沟通记录
图片说明：预约试听
图片说明：学员签约
图片说明：订单支付
图片说明：订单审批
图片说明：订单审批
图片说明：订单审批
图片说明：订单审批
图片说明：转为正式学员
图片说明：转为正式学员
```

### chunk_cf7d7af1dae6069211766836e4addd5d | 销售端如何快速生成订单？

- source_id：helpcenter:77
- document_id：doc_helpcenter_77
- 分类：热门文章
- 适用角色库：sales(销售库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T15:07:26
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061432054245707717758260129", "alt_text": "录入潜客学员信息", "ocr_text": null, "caption": "录入潜客学员信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061433065411900630643002737", "alt_text": "录入潜客学员信息", "ocr_text": null, "caption": "录入潜客学员信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061434073552857976640621352", "alt_text": "填写沟通记录", "ocr_text": null, "caption": "填写沟通记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061436287367915559979979749", "alt_text": "预约试听", "ocr_text": null, "caption": "预约试听"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061439263236603255072715708", "alt_text": "学员签约", "ocr_text": null, "caption": "学员签约"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061444103703715006514131839", "alt_text": "订单支付", "ocr_text": null, "caption": "订单支付"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061446469077131803756544360", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061448451870391610317358208", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306145027719083254752767047", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061453539172406978692713873", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061457224519526088083404453", "alt_text": "转为正式学员", "ocr_text": null, "caption": "转为正式学员"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306145938973732470581705483", "alt_text": "转为正式学员", "ocr_text": null, "caption": "转为正式学员"}]

```text
也可以对有问题的订单进行“回退”处理，重新编辑！
[图片: 订单审批]
转为正式学员
一键点击上图中的“非正式学员”，直接将客户转为正式学员。转为正式学员的学生会直接进入到教务端的学生管理中，成为正式学员。
[图片: 转为正式学员]
还可以点击公池，找到已签约的学员，点击右侧即可转为正式学员！
[图片: 转为正式学员]

图片说明：录入潜客学员信息
图片说明：录入潜客学员信息
图片说明：填写沟通记录
图片说明：预约试听
图片说明：学员签约
图片说明：订单支付
图片说明：订单审批
图片说明：订单审批
图片说明：订单审批
图片说明：订单审批
图片说明：转为正式学员
图片说明：转为正式学员
```

### chunk_82413599acae12a0249da006df096e3d | 一文读懂：如何进行班级管理

- source_id：helpcenter:90
- document_id：doc_helpcenter_90
- 分类：核心功能介绍
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:24:46
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051403496385987061029118169", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051404158559442903582153654", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051404543633264084494134957", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305140458840939533625469258", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051406182624771163843758617", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051406321185241861068597737", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051406491173050432787914644", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051407082972844805710125263", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408044602827780560134377", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408254775985855103053806", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408497787647380476471000", "alt_text": "排课", "ocr_text": null, "caption": "排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051408525497562335841756542", "alt_text": "排课", "ocr_text": null, "caption": "排课"}]

```text
一文读懂：如何进行班级管理
一文读懂：如何进行班级管理
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍班级管理的功能。
创建班级
添加好课程后，可以在班级管理里创建班级。
[图片: 创建班级]
添加班级：班级信息包括所属课程、班级类型、班级名称、班级老师助教、开班日期、班级课时、大概上课时间等。
选择一对一班级需要手动填写班级名称，添加一对多班级系统会自动匹配学期和班级名称。
[图片: 创建班级]
班级里选择班级学生，点击添加，可以将相应学员添加至班级内。
[图片: 创建班级]
[图片: 创建班级]
排课
班级创建好并完成分班后，可以给班级排课(需提前在员工管理中添加好老师，并且在创 建班级时选定老师)。
[图片: 排课]
排课的方式有三种，智能排课、传统排课、常用时间段排课。
[图片: 排课]
课表支持一键导出。
[图片: 排课]
智能排课
[图片: 排课]
传统排课
[图片: 排课]
常用时间段排课
[图片: 排课]
点击老师名称可以查看该老师的课表周视图，也可以筛选其他老师，助教进行查看。
[图片: 排课]
[图片: 排课]

图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：排课
图片说明：排课
图片说明：排课
图片说明：排课
图片说明：排课
图片说明：排课
图片说明：排课
图片说明：排课
```

### chunk_83ba121ebc33df5e805743f95f563d7f | 学生完成测试，如何处理无法提交的情况？

- source_id：helpcenter:110
- document_id：doc_helpcenter_110
- 分类：热门问题
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:36:44
- 图片数：0
- 图片引用：[]

```text
学生完成测试，如何处理无法提交的情况？
学生完成测试，如何处理无法提交的情况？
当学生完成作业/测试时，发现作业/测试无法提交的现象，可以通过以下文档排查。
一、浏览器使用不正确
当学生未使用正确浏览器时，可能会出现兼容性问题或者不稳定的情况
【解决方法】：
确认一下学生是否使用的正确的浏览器，建议电脑使用谷歌浏览器，iPad使用safari浏览器
二、学生网络环境不佳
当学生的网络环境异常或不稳定时会造成作业无法提交的问题；网络环境不佳只会影响当前网络环境下的学生
【解决办法】：
首先可以让学生刷新页面，刷新之后重新提交作业/测试。检查网络是否稳定，学生可以更换网络再次尝试提交作业
```

### chunk_82880cf5990ee045cd4690913cbbd51f | 老师/助教如何快速查看自己的待反馈课程？

- source_id：helpcenter:165
- document_id：doc_helpcenter_165
- 分类：使用技巧
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:21:46
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061057111167341153500412426", "alt_text": "老师/助教查看“待反馈课程”", "ocr_text": null, "caption": "老师/助教查看“待反馈课程”"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061057156186848218037564483", "alt_text": "老师/助教查看“待反馈课程”", "ocr_text": null, "caption": "老师/助教查看“待反馈课程”"}]

```text
老师/助教如何快速查看自己的待反馈课程？
老师/助教如何快速查看自己的待反馈课程？
老师可在自己账号的首页-待办事项，快速查看到自己已经上课，但还没有反馈的课程。
老师/助教查看“待反馈课程”
1、登录老师账号，首页-待办事项即可查看所带班级的待反馈
2、可筛选班级查看
3、点击课程名称即可快速打开课堂反馈填写界面
[图片: 老师/助教查看“待反馈课程”]
[图片: 老师/助教查看“待反馈课程”]

图片说明：老师/助教查看“待反馈课程”
图片说明：老师/助教查看“待反馈课程”
```

### chunk_9a2385c5be793ab0c9fc4e6e2b20963d | 入门必备-市场线索录入跟进

- source_id：helpcenter:57
- document_id：doc_helpcenter_57
- 分类：初次使用指南
- 适用角色库：teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T16:47:10
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051528214143082176819120491", "alt_text": "潜客信息录入跟进", "ocr_text": null, "caption": "潜客信息录入跟进"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051528294817412250390988331", "alt_text": "潜客信息录入跟进", "ocr_text": null, "caption": "潜客信息录入跟进"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051528427550888761072474470", "alt_text": "潜客信息录入跟进", "ocr_text": null, "caption": "潜客信息录入跟进"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051528494099427226625676781", "alt_text": "潜客信息录入跟进", "ocr_text": null, "caption": "潜客信息录入跟进"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051528575315066767849698979", "alt_text": "潜客信息录入跟进", "ocr_text": null, "caption": "潜客信息录入跟进"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051529132079734014768149499", "alt_text": "潜客分配", "ocr_text": null, "caption": "潜客分配"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051529221235845966001857711", "alt_text": "销售渠道管理", "ocr_text": null, "caption": "销售渠道管理"}]

```text
入门必备-市场线索录入跟进
入门必备-市场线索录入跟进
如何快速录入潜客线索并管理更进？校校销售端支持通过入学模考或者手动快速录入潜客线索，实时调整跟进状态，签约效率提升！
销售端如何掌握潜客跟进主动权！
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202403141601427612585973023012540
潜客信息录入跟进
潜客是销售自己负责的市场线索，分不同跟进进度，显示该销售人员跟进的客户，在这里可查看潜客的入学模测结果，点击编辑可进行潜客信息编辑，包括基础信息、学习目标、信息来源、沟通信息等，如下图：
[图片: 潜客信息录入跟进]
沟通过程中可以不断完善基础信息、学习目标、信息来源等，并且在线填写沟通记录，这里的沟通信息包括潜客、跟进中、已预约、已试听、已签约等，所有沟通记录累积保存。填写沟通信息时，可设置下次沟通时间，系统会进行自动跟进提醒！
[图片: 潜客信息录入跟进]
系统潜客列表支持名单一键导出，也可以批量导入！
[图片: 潜客信息录入跟进]
公池是一个累积显示所有销售跟进的客户信息的客户池，包括已分配未分配，以及各种跟进进度下的客户信息，跟进状态，有分配权限的销售可筛选不同条件下的客户信息进行查看，也可添加、修改、删除客户信息，或将客户指定分配给某个销售进行跟进。销售管理员或有下属的销售分别可以看到整个机构或自己下属的潜客跟进情况！
[图片: 潜客信息录入跟进]
批量潜客名单导入，首先点击下载模版，将文档按照模版整理好后，在点击选择导入文档，即可一键批量导入！
[图片: 潜客信息录入跟进]
潜客分配
潜客录入后如何分配，有分配权限的销售，可选择公池中的潜客将其分配给指定销售进行跟进！
[图片: 潜客分配]
销售渠道管理
销售管理员也可以自定义管理渠道来源，点击左侧导航栏渠道，点击添加即可添加潜客渠道来源！
[图片: 销售渠道管理]

图片说明：潜客信息录入跟进
图片说明：潜客信息录入跟进
图片说明：潜客信息录入跟进
图片说明：潜客信息录入跟进
图片说明：潜客信息录入跟进
图片说明：潜客分配
图片说明：销售渠道管理
```

### chunk_abd904b8366e701b16bb3015a696c7a3 | 如何使用作业大纲发布作业？

- source_id：helpcenter:79
- document_id：doc_helpcenter_79
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T15:28:53
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061503326285719891494801076", "alt_text": "创建大纲", "ocr_text": null, "caption": "创建大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061505146547283392401230511", "alt_text": "添加目录", "ocr_text": null, "caption": "添加目录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061507475340174509918437461", "alt_text": "添加任务", "ocr_text": null, "caption": "添加任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061509196006911389143721611", "alt_text": "关联作业类型", "ocr_text": null, "caption": "关联作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061515075022679624094161801", "alt_text": "题库作业类型", "ocr_text": null, "caption": "题库作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061520108676310527580460889", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061519084040071551983834744", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}]

```text
如何使用作业大纲发布作业？
如何使用作业大纲发布作业？
下发作业步骤太繁琐？题目太多不好筛选？作业大纲助力老师高效管理课堂作业！
创建大纲
进入校校后台老师端，在导航栏中选择教研，在左侧导航栏中找到【教研】，选择创建大纲，即可添加大纲的科目与名称。
[图片: 创建大纲]
添加目录
确认添加大纲后，在左边【大纲目录】部分选择新添加的大纲，点击主页中目录名称旁的【+】号，即可添加目录。
[图片: 添加目录]
添加任务
成功添加目录后，将鼠标移动至目录，点击【+】即可添加其相关任务！
[图片: 添加任务]
关联作业类型
添加任务时，输入【任务名称】，选择【关联作业类型】，下方的关联按钮即可跳出相对应的界面。其中【单词】跳转至系统内的【基础练习（单词部分）】，音视频和课件跳转至云盘，老师可自行上传。
[图片: 关联作业类型]
题库作业类型
在作业关联部分，左上角可以选择多种题库类型
- 基础练习。分为单词，听，说，读，写五个类。为学生之后的学习打牢基础，其题目均来自正规考试。
- 题型训练。分为听力，阅读，写作，口语。系统将题库内的题目根据正规考试中所出现的题型进行分类，使学生能更精确的对自身薄弱的地方进行专项训练。
- 模考测试。校校系统自带的题库，供机构直接使用。
- 机构题库。需要提前在“题库管理”的“自有题库”中录入需要布置的题（录入完成后，即可在这里进行题目筛选布置）
- 自定义作业。机构可将自己的作业资料以复制粘切、图片、超链 接、音频等形式输入到文 本框， 也可以添加附件让学生下载查看做题。 
答题方式分为两种： 
1. 答题卡作答 (老师添加答题卡， 将正确答案输入，学生作答结束后系统自动批改正误。) 
2. 无答题卡作答 (需要学生将写在纸上的答案拍照上传或上传音频作答内容，老师进行批改处理。) 
- 音视频、课件作业。可以上传课件、音视频，让学生查看
[图片: 题库作业类型]
选择好需要关联的题目后，点击确认，作业大纲也就建立成功了。
关联作业大纲，下发作业

图片说明：创建大纲
图片说明：添加目录
图片说明：添加任务
图片说明：关联作业类型
图片说明：题库作业类型
图片说明：关联作业大纲，下发作业
图片说明：关联作业大纲，下发作业
```

### chunk_3e588f18435fe39c9c37d91f38402b2b | 如何使用作业大纲发布作业？

- source_id：helpcenter:79
- document_id：doc_helpcenter_79
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T15:28:53
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061503326285719891494801076", "alt_text": "创建大纲", "ocr_text": null, "caption": "创建大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061505146547283392401230511", "alt_text": "添加目录", "ocr_text": null, "caption": "添加目录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061507475340174509918437461", "alt_text": "添加任务", "ocr_text": null, "caption": "添加任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061509196006911389143721611", "alt_text": "关联作业类型", "ocr_text": null, "caption": "关联作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061515075022679624094161801", "alt_text": "题库作业类型", "ocr_text": null, "caption": "题库作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061520108676310527580460889", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061519084040071551983834744", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}]

```text
在导航栏中，选择【班级】。在我的班级中，找到需要关联作业大纲的班级。在主页面上半部分选择作业大纲 -关联，即可对关联大纲的科目，名称和下发日期进行编辑。
[图片: 关联作业大纲，下发作业]
将该班级确认关联大纲后，点击【发布】，在班级中的学生即可收到关联的作业。
[图片: 关联作业大纲，下发作业]

图片说明：创建大纲
图片说明：添加目录
图片说明：添加任务
图片说明：关联作业类型
图片说明：题库作业类型
图片说明：关联作业大纲，下发作业
图片说明：关联作业大纲，下发作业
```

### chunk_b3b22d084921e5241bbc1baf935c8b50 | 一文读懂：如何进行课表管理

- source_id：helpcenter:91
- document_id：doc_helpcenter_91
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:29:24
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051409236316246707454813491", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305140948700816521396628583", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051410184443666066655943978", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051410512465471849750578166", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051411171154815890910057446", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051411202187755598958727536", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051411442466894622808143994", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051413346226805463140662401", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051412184874082707382929761", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051412528995067122503816666", "alt_text": "课表管理功能介绍", "ocr_text": null, "caption": "课表管理功能介绍"}]

```text
一文读懂：如何进行课表管理
一文读懂：如何进行课表管理
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍课表管理的功能。
课表管理功能介绍
所有班级已排的课表都会显示在这里，可根据课程、班级、老师、助教、课程状态，时间等多个维度筛选数据或导出课表。
[图片: 课表管理功能介绍]
需要调整的课程可以直接点击编辑修改相关内容，修改之后在记录部分可以查看修改记录。
[图片: 课表管理功能介绍]
勾选班级只显示当前班级课表，多选排课或者全选当前页面，可以一键删除排课。
[图片: 课表管理功能介绍]
[图片: 课表管理功能介绍]
教务在课表页面可以分别查看班级调课和学员调课的详情记录，包含课程内容、上课内容、上课时间、上课老师、上课方式、上课地点等调课详情记录。
[图片: 课表管理功能介绍]
[图片: 课表管理功能介绍]
班级调课记录包括：班级排课调整（上课老师、上课内容、上课时间等），老师学生申请调课，调整后记录会在此显示，点击查看详情可以查看具体调整内容。
[图片: 课表管理功能介绍]
学员调课是学生某节课请假后，教务进行跨班级调课，调课记录会在此显示。
点击详情可以查看具体内容。
[图片: 课表管理功能介绍]
视图模式，以老师视图、班级视图、时间视图、教室视图去查看课表，支持切换日/周/月视图查看，视图模式也支持一键导出。
[图片: 课表管理功能介绍]
教务老师在视图模式下点击课程可以直接新增课程或者编辑、删除课程。
[图片: 课表管理功能介绍]

图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
图片说明：课表管理功能介绍
```

### chunk_c6e0b6f80b885d2a0f8c0f9f7b894132 | 还没有排课的班级，可以安排布置作业吗？

- source_id：helpcenter:166
- document_id：doc_helpcenter_166
- 分类：使用技巧
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T18:22:49
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306113929630215354787765339", "alt_text": "1. 教务端新建班级时，将布置作业的老师/助教添加进班级", "ocr_text": null, "caption": "1. 教务端新建班级时，将布置作业的老师/助教添加进班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306114006926875342259120033", "alt_text": "2. 老师/助教被添加进班级后，在自己账号中即可看到对应班级，布置作业", "ocr_text": null, "caption": "2. 老师/助教被添加进班级后，在自己账号中即可看到对应班级，布置作业"}]

```text
还没有排课的班级，可以安排布置作业吗？
还没有排课的班级，可以安排布置作业吗？
未排课班级可以布置作业，操作方法如下：
1. 教务端新建班级时，将布置作业的老师/助教添加进班级
无需排课，老师就可以在自己账号中看到对应班级，然后布置作业。
[图片: 1. 教务端新建班级时，将布置作业的老师/助教添加进班级]
2. 老师/助教被添加进班级后，在自己账号中即可看到对应班级，布置作业
[图片: 2. 老师/助教被添加进班级后，在自己账号中即可看到对应班级，布置作业]

图片说明：1. 教务端新建班级时，将布置作业的老师/助教添加进班级
图片说明：2. 老师/助教被添加进班级后，在自己账号中即可看到对应班级，布置作业
```

### chunk_d7ee497bb63ff779cfc206c789f0e308 | 如何解决班级无法布置模考和题型训练的情况？

- source_id：helpcenter:215
- document_id：doc_helpcenter_215
- 分类：热门问题
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2024-05-31T16:12:01
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061355381001454615503141821", "alt_text": "无法布置模考，题型训练", "ocr_text": null, "caption": "无法布置模考，题型训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061355481391329777503873622", "alt_text": "无法布置模考，题型训练", "ocr_text": null, "caption": "无法布置模考，题型训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061355562165708578860002150", "alt_text": "无法布置模考，题型训练", "ocr_text": null, "caption": "无法布置模考，题型训练"}]

```text
如何解决班级无法布置模考和题型训练的情况？
如何解决班级无法布置模考和题型训练的情况？
无法布置模考，题型训练
如果老师遇到班级无法布置模考和题型作业的情况（如下图），可以按照以下方法解决：
[图片: 无法布置模考，题型训练]
1、教务/校长在课程页面找到对应课程，查看是否有关联对应题库，如未关联，需要选择对应题库
[图片: 无法布置模考，题型训练]
2、课程关联题库之后，需要在班级页面，找到对应班级，在编辑页面点击下确认即可
[图片: 无法布置模考，题型训练]

图片说明：无法布置模考，题型训练
图片说明：无法布置模考，题型训练
图片说明：无法布置模考，题型训练
```

### chunk_5ed29397979f761638f7509534424946 | 入门必备-学员订单签约流程

- source_id：helpcenter:59
- document_id：doc_helpcenter_59
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T19:08:28
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051543206763338700920221185", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051543307579910897021417177", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051543407135278416952617905", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051543487267991706905612881", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051543598210687090598092103", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051544077868101918976359370", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051544422597160196602176523", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051544371325949994513657281", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051547115461041892503974131", "alt_text": "学员订单签约流程", "ocr_text": null, "caption": "学员订单签约流程"}]

```text
入门必备-学员订单签约流程
入门必备-学员订单签约流程
新老师用户如何有效管理学员跟进情况？如何线上签约转为正式学员？
学员订单签约流程操作会在销售端、教务端或校长端进行，校长端默认教务所有权限，操作均一致！
学员订单签约流程
销售线索分不同跟进进度，可进行筛选，显示该销售人员跟进的客户，在这里可查看潜客的入学模测结果，点击编辑可进行潜客信息编辑，包括基础信息、学习目标、信息来源、沟通信息等，如下图：
[图片: 学员订单签约流程]
沟通过程中可以不断完善基础信息、学习目标、信息来源等，并且在线填写沟通记录，这里的沟通信息包括潜客、跟进中、已预约、已试听、已签约等，所有沟通记录累积保存。填写沟通信息时，可设置下次沟通时间，系统会进行自动跟进提醒！
[图片: 学员订单签约流程]
已预约试听潜客学员信息会同步到教务的试听排课中，教务进行排课，需要同步给教务的其他课程信息要通过备注填写，填写在沟通记录中的信息不会同步给教务哦！
[图片: 学员订单签约流程]
已转化的学员可以点击潜客右侧的编辑，下拉选择跟进进度为“已签约”，系统会自动生成学员订单，点击右侧导航栏订单即可查看，不会直接进入到教务端成为正式学生哦！
[图片: 学员订单签约流程]
系统会自动弹出订单支付页面，选择付款方式，填写支付金额，上传支付凭证。添加好支付信息后，会直接同步到有审批权限的销售账号中，教务或校长端均可查看，并审批确认订单，即可转化为正式学员！
[图片: 学员订单签约流程]
订单页面筛选待付款的学员，点击订单详情补交学费即可！
[图片: 学员订单签约流程]
也可点击“退费”，发起退费申请！
[图片: 学员订单签约流程]
具有审批权限的销售老师，可以点击“审批”查看订单的支付信息等，并进行审核确认！确定订单后，学员状态变为“正式学员”。
[图片: 学员订单签约流程]
还可以点击公池，找到已签约的学员，点击右侧即可转为正式学员！
[图片: 学员订单签约流程]

图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
图片说明：学员订单签约流程
```

### chunk_301dc99d084c217bbd0c168d96182c10 | 老师/助教如何布置作业？

- source_id：helpcenter:80
- document_id：doc_helpcenter_80
- 分类：热门文章
- 适用角色库：teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T15:51:32
- 图片数：13
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061523071753953998818213944", "alt_text": "操作步骤", "ocr_text": null, "caption": "操作步骤"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061527114880647012061978952", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061528042931229217669589702", "alt_text": "作业布置类型", "ocr_text": null, "caption": "作业布置类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061528401252267385611981641", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061529187893013763465350582", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061529597030103916723318624", "alt_text": "基础练习", "ocr_text": null, "caption": "基础练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061532043368179782246672161", "alt_text": "题型训练", "ocr_text": null, "caption": "题型训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030615331883839659616003556", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061534543301274828500671657", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306153528905052071247858812", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030615360852235310726500056", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061536383355253708887494071", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061537154733994129609479585", "alt_text": "课件作业", "ocr_text": null, "caption": "课件作业"}]

```text
老师/助教如何布置作业？
老师/助教如何布置作业？
作业是对课堂学习的有效延伸，是教学的重要组成部分，也是老师获取教学反馈信息的重要手段；那么老师如何利用系统快速下发作业呢？
1 分钟了解老师端如何布置作业！
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202403141552094141141548400935345
操作步骤
老师登录系统网址，在左侧导航栏中找到【作业】选项，点击进入作业管理页面；在作业管理页面左上角，点击蓝色【布置作业】按钮即可给班级或学生布置作业。
[图片: 操作步骤]
快捷方式
老师除了按正常布置作业流程进行作业布置外，可以通过快捷方式帮助老师便捷给学生布置作业。
老师在进行班级管理时，进入对应班级管理页面，在班级管理页面右侧有布置作业的快捷功能展示，可快速给该班级布置相关的作业。
[图片: 快捷方式]
作业布置类型
老师布置作业时，除了要选择作业布置对应的班级和学生以外，还需要确认作业布置的类型；系统为老师们提供基础练习、题型训练、模考测试、机构题库、自定义作业、打卡作业和课件作业七种主要的作业类型，帮助老师分层布置作业，精准提升学生能力。
[图片: 作业布置类型]
模考作业
模考作业包含基础练习、题型训练、模考测试和机构题库四种形式；协助老师发现学生薄弱环节，模考作业题型与形式和正式考试接近，能够提升学生对考试题型的掌握，训练学生应对考试的心理。
[图片: 模考作业]
模考作业可以在作业标题栏下方添加作业的关联音视频，方便辅助学生答题；在右下方可以将本次模考作业添加至常用作业，方便进行作业的二次快捷布置（小程序端也能使用常用作业）；也能对模考作业进行答题的预览。
[图片: 模考作业]
基础练习
基础练习包含单词训练和听说读写各分项的专项训练；包含多种训练方式，全方位巩固学生基础知识能力。
[图片: 基础练习]
题型训练
题型训练使用系统现有题目，包含科目相关的所有题型；雅思、托福、GRE、ACT、SAT等科目题型全覆盖，帮助老师为学生制定专属的提分计划。
[图片: 题型训练]
机构题库

图片说明：操作步骤
图片说明：快捷方式
图片说明：作业布置类型
图片说明：模考作业
图片说明：模考作业
图片说明：基础练习
图片说明：题型训练
图片说明：机构题库
图片说明：自定义作业
图片说明：自定义作业
图片说明：打卡作业
图片说明：打卡作业
图片说明：课件作业
```

### chunk_8bbb1fdf7e18d02f4bf2cfd959ea9816 | 老师/助教如何布置作业？

- source_id：helpcenter:80
- document_id：doc_helpcenter_80
- 分类：热门文章
- 适用角色库：teacher(老师库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T15:51:32
- 图片数：13
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061523071753953998818213944", "alt_text": "操作步骤", "ocr_text": null, "caption": "操作步骤"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061527114880647012061978952", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061528042931229217669589702", "alt_text": "作业布置类型", "ocr_text": null, "caption": "作业布置类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061528401252267385611981641", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061529187893013763465350582", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061529597030103916723318624", "alt_text": "基础练习", "ocr_text": null, "caption": "基础练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061532043368179782246672161", "alt_text": "题型训练", "ocr_text": null, "caption": "题型训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030615331883839659616003556", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061534543301274828500671657", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306153528905052071247858812", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030615360852235310726500056", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061536383355253708887494071", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061537154733994129609479585", "alt_text": "课件作业", "ocr_text": null, "caption": "课件作业"}]

```text
机构题库作业可以选择机构自己在系统中录入的题目或试卷布置给学生进行训练、题型、知识点分类更加多样，选择更加灵活。
[图片: 机构题库]
自定义作业
老师可以通过自定义作业、布置课后的相关练习、布置个性化作业练习。
老师布置自定义作业时，可以上传图片、视频、音频和课件等，增加作业的布置形式。
[图片: 自定义作业]
老师可以在布置自定义作业选择是否添加答题卡，添加答题卡输入正确答案，学生作答完成后系统会进行自动批改。无答题卡，学生则需要上传作业相关的作答内容，老师进行手动的批改。
[图片: 自定义作业]
打卡作业
老师可以根据教学计划，使用打卡作业，老师设置打卡的时间段和打卡频次，系统会按照时间每天自动给学生下发打卡作业，还会按时提醒学生完成打卡作业；帮助老师监督学生学习，形成学习习惯。
[图片: 打卡作业]
打卡作业同样可以上传图片、视频、音频和课件等；还可以规定学生上传打卡作业的形式，设置是否允许学生补卡，是否查看其他学生作答内容等；精确打卡练习内容。
[图片: 打卡作业]
课件作业
课件作业主要用于给学生分享一些学习资料，例如课程相关的音视频和课件等；拓展老师的教学分享方式。
[图片: 课件作业]

图片说明：操作步骤
图片说明：快捷方式
图片说明：作业布置类型
图片说明：模考作业
图片说明：模考作业
图片说明：基础练习
图片说明：题型训练
图片说明：机构题库
图片说明：自定义作业
图片说明：自定义作业
图片说明：打卡作业
图片说明：打卡作业
图片说明：课件作业
```

### chunk_72b97433d886ac060f3b1ff12ad3a701 | 一文了解：如何使用考勤功能

- source_id：helpcenter:92
- document_id：doc_helpcenter_92
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:30:17
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051414534778121221075208987", "alt_text": "考勤管理", "ocr_text": null, "caption": "考勤管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051416104396391244766088054", "alt_text": "调课功能", "ocr_text": null, "caption": "调课功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051416154937960742998870174", "alt_text": "调课功能", "ocr_text": null, "caption": "调课功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051417366245642570019654908", "alt_text": "调课功能", "ocr_text": null, "caption": "调课功能"}]

```text
一文了解：如何使用考勤功能
一文了解：如何使用考勤功能
考勤页面可以查看、修改学生的课堂考勤情况，对请假学生进行调课操作，管理课堂考勤更轻松！
考勤管理
已过时间的课程默认为未出勤，计算课消。教务可以通过筛选上课时间，考勤状态，搜索班级或学生查看考勤记录，支持手动修改考勤。
[图片: 考勤管理]
调课功能
考勤状态为已请假的学生可以进行调课。注：班课学生请假调课只能调到本班以外的班级，一对一班级可以不需要调课可以直接在班级重排
[图片: 调课功能]
[图片: 调课功能]
调课后的班级课表出勤会显示有学生插课
[图片: 调课功能]

图片说明：考勤管理
图片说明：调课功能
图片说明：调课功能
图片说明：调课功能
```

### chunk_1337c0f71ab261d1817f767b264c2900 | 老师学生如何实现线上流程化调课？

- source_id：helpcenter:167
- document_id：doc_helpcenter_167
- 分类：使用技巧
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-14T10:50:35
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306134628363047207897864347", "alt_text": "1. 老师/学生发起调课申请", "ocr_text": null, "caption": "1. 老师/学生发起调课申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061346578773178054683072113", "alt_text": "1. 老师/学生发起调课申请", "ocr_text": null, "caption": "1. 老师/学生发起调课申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061348017407555915145595991", "alt_text": "2. 教务老师查看处理“调课申请”", "ocr_text": null, "caption": "2. 教务老师查看处理“调课申请”"}]

```text
老师学生如何实现线上流程化调课？
老师学生如何实现线上流程化调课？
系统支持调课动作线上流程化，节省线下沟通成本，提高沟通效率，避免遗忘！
1. 老师/学生发起调课申请
老师或一对一班级的学生，可发起调课申请。
[图片: 1. 老师/学生发起调课申请]
点击“申请调课”后，进入如下界面，填写调课原因和期望的调课时间，点击确定；这里要注意这只是一个申请，并不会立即生效哦，具体调或不调，调到什么时候，需要教务老师实际发生调课动作才能生效！
[图片: 1. 老师/学生发起调课申请]
2. 教务老师查看处理“调课申请”
教务老师在教务端“调课申请”一栏中，查看核实调课信息。
[图片: 2. 教务老师查看处理“调课申请”]
进行调课动作及调课成功后，状态变为已调整，系统会实时同步在对应老师和学生的课表中！

图片说明：1. 老师/学生发起调课申请
图片说明：1. 老师/学生发起调课申请
图片说明：2. 教务老师查看处理“调课申请”
```

### chunk_4805b8a16cb0aa8fe30f66ab245bc13a | 入门必备-添加电子合同模版

- source_id：helpcenter:70
- document_id：doc_helpcenter_70
- 分类：初次使用指南
- 适用角色库：sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T13:46:46
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554265619111166406912730", "alt_text": "添加合同模板", "ocr_text": null, "caption": "添加合同模板"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554308177201364021969230", "alt_text": "添加合同模板", "ocr_text": null, "caption": "添加合同模板"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051554378332896010730468234", "alt_text": "添加合同模板", "ocr_text": null, "caption": "添加合同模板"}]

```text
入门必备-添加电子合同模版
入门必备-添加电子合同模版
机构如何在线签约？校校提供合同模板的创建，校长和教务可以在设置中添加电子合同的模板
添加合同模板
点击左侧导航栏【设置】按钮，找到【销售相关】，即可看到电子合同，点击添加可以进行合同的创建，合同模板必须拥有合同名称和公章
[图片: 添加合同模板]
[图片: 添加合同模板]
校校提供相应的编辑工具，可以直接插入学生姓名，课程名称，课时数，优惠金额等变量，系统会自动根据学生信息填写，需要手动编辑的地方可以点击编辑工具栏上的[...]按钮，即可生成填空格
可以直接复制PDF或者word版本的文件，但注意要使用格式刷将合同的格式统一，或者使用清除格式，再手动编辑
[图片: 添加合同模板]

图片说明：添加合同模板
图片说明：添加合同模板
图片说明：添加合同模板
```

### chunk_136bc950ac8e989f0a5ffdbbf1c01bae | 如何玩转实时作业？

- source_id：helpcenter:81
- document_id：doc_helpcenter_81
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T16:03:15
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061538448063199392201247234", "alt_text": "实时作业布置", "ocr_text": null, "caption": "实时作业布置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061543216298829352886994378", "alt_text": "开启实时作业", "ocr_text": null, "caption": "开启实时作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121602463101249053597213446", "alt_text": "开启实时作业", "ocr_text": null, "caption": "开启实时作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121602578823596176311496216", "alt_text": "开启实时作业", "ocr_text": null, "caption": "开启实时作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121603082434208658833425595", "alt_text": "开启实时作业", "ocr_text": null, "caption": "开启实时作业"}]

```text
如何玩转实时作业？
如何玩转实时作业？
如何提高学生完成作业的积极性？如何同步监测学生的作答情况？老师可以试试开启实时作业，把作业变成有趣的竞技比赛。
布置流程
目前除了打卡作业、视频课件作业，其他作业类型都支持开启实时作业。
实时作业布置
老师在布置作业页面，选择好需要布置的题目，点击右上方蓝色【开启实时作业】按钮，设置好开始时间和考试时长，最后发布作业，实时作业布置成功。
[图片: 实时作业布置]
开启实时作业
实时作业布置完成后，老师可以直接进入实时作业页面。也可以在作业列表中找到已发布的实时作业，点击进入实时作业等待页面。
[图片: 开启实时作业]
进入实时作业等待页面，老师可在倒计时结束前提前开始作答；倒计时结束自动开始作业答题。
[图片: 开启实时作业]
老师开启实时作业作答后，可以实时查看学生的答题进度和正确率，还有学员的作答排行榜，帮助老师实时掌握学生的答题情况。
[图片: 开启实时作业]
等待学生题目作答完成后，老师可以点击结束答题，并生成本次实时作业的数据分析；从学生的总分，正确率，错误题目数，分项评价及题型分析等多个维度进行分析，帮助老师更加精准的掌握学生的练习情况。
[图片: 开启实时作业]

图片说明：实时作业布置
图片说明：开启实时作业
图片说明：开启实时作业
图片说明：开启实时作业
图片说明：开启实时作业
```

### chunk_e5e5542e6a24e76b80e6687c0a563729 | 一文了解：如何使用申请功能

- source_id：helpcenter:94
- document_id：doc_helpcenter_94
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:33:45
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051418186664167361411753758", "alt_text": "申请功能介绍", "ocr_text": null, "caption": "申请功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051419042421668057723279944", "alt_text": "申请功能介绍", "ocr_text": null, "caption": "申请功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051419278005480879485279425", "alt_text": "申请功能介绍", "ocr_text": null, "caption": "申请功能介绍"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051419494767418145883596966", "alt_text": "申请功能介绍", "ocr_text": null, "caption": "申请功能介绍"}]

```text
一文了解：如何使用申请功能
一文了解：如何使用申请功能
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍申请的功能。
申请功能介绍
申请页面可以查看排课申请、预占请假、试听排课申请、调课申请。
销售发起的排课申请，可以在“排课”查看，排课的备注信息会同步显示，方便老师合理安排课程。已排课的课程可以点击调整状为已处理。
[图片: 申请功能介绍]
可以在这里主动给老师添加预占或请假时间，本时间段不可排课，系统在排课时会自动避开该时间段。老师在自己端口请假的时间也会同步到该表格中。可同时预占/请假多个老师的多个时间段。
[图片: 申请功能介绍]
销售人员通过销售端给客户预约试听课信息会显示在这里，教务或管理员点击排课设置试听课上课老师和时间等信息进行试听排课。也可点击“忽略”，将不需要排课的信息忽略掉。
[图片: 申请功能介绍]
老师或⼀对⼀班级的学生可以在自己端口“我的课表”中发起调课申请，申请调课信息会显示在调课申请这里，管理员或教务可以重新修改上课时间。
[图片: 申请功能介绍]

图片说明：申请功能介绍
图片说明：申请功能介绍
图片说明：申请功能介绍
图片说明：申请功能介绍
```

### chunk_47b6aac37930d2aedc6ce433d2efdc1c | 老师/助教端如何查看学生的错词本

- source_id：helpcenter:228
- document_id：doc_helpcenter_228
- 分类：使用技巧
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2025-05-20T16:05:23
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061349572362502916712988897", "alt_text": "老师/助教端查看学生错词本", "ocr_text": null, "caption": "老师/助教端查看学生错词本"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061350155765101746126353730", "alt_text": "老师如何二次下发错词给学生", "ocr_text": null, "caption": "老师如何二次下发错词给学生"}]

```text
老师/助教端如何查看学生的错词本
老师/助教端如何查看学生的错词本
老师/助教端查看学生错词本
老师/助教在学员管理-练习情况-错词本界面，选择练习单词数量，单词布置范围，点击“布置练习”，即可将错词二次下发给学生练习，老师也可以以同样的方式发布学生的生词练习。
[图片: 老师/助教端查看学生错词本]
老师如何二次下发错词给学生
老师/助教在错词本界面，选择练习单词数量，点击“布置练习”，即可将错词二次下发给学生练习。
[图片: 老师如何二次下发错词给学生]

图片说明：老师/助教端查看学生错词本
图片说明：老师如何二次下发错词给学生
```

### chunk_951bedfce2a8042c37c3473e0961b4cf | 入门必备-老师/助教布置作业

- source_id：helpcenter:60
- document_id：doc_helpcenter_60
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T19:21:31
- 图片数：17
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559241086662610756680990", "alt_text": "操作步骤", "ocr_text": null, "caption": "操作步骤"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559304713404873412583490", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559377563000856427669450", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600517495457299513304227", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601416897933885051229952", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051603016074142845015478569", "alt_text": "作业布置类型", "ocr_text": null, "caption": "作业布置类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051606447907998563063463536", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051606568581051689655822574", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051610456822015369361971686", "alt_text": "基础练习", "ocr_text": null, "caption": "基础练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051610546068072598981342774", "alt_text": "题型训练", "ocr_text": null, "caption": "题型训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611028415148387327623992", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611224094459389549884389", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611307057662607091399084", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611391259085434640265814", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611469028867634987310408", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611503755251323578204973", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611584596481445236775293", "alt_text": "课件作业", "ocr_text": null, "caption": "课件作业"}]

```text
入门必备-老师/助教布置作业
入门必备-老师/助教布置作业
作业是对课堂学习的有效延伸，是教学的重要组成部分，也是老师获取教学反馈信息的重要手段；那么老师如何利用系统快速下发作业呢？
老师端如何在班级布置作业
视频链接：https://xiaosaas.oss-cn-beijing.aliyuncs.com/202403111527102009693189843469354
操作步骤
老师登录系统网址，在左侧导航栏中找到【作业】选项，点击进入作业管理页面；在作业管理页面左上角，点击蓝色【布置作业】按钮即可给班级或学生布置作业。
[图片: 操作步骤]
快捷方式
方式一：老师在进行班级管理时，进入对应班级管理页面，在班级管理页面右侧有布置作业的快捷功能展示，可快速给该班级布置相关的作业。
[图片: 快捷方式]
方式二：课表除了查看日常的上课安排以外，还可以打考勤、线上教学及布置作业，这里老师通常发布课件作业，以提升实际的教学课堂效果，提高学生上课的满意度。
[图片: 快捷方式]
方式三：系统题库可以查看所有科目的题目类型，在题目中添加知识点和名师讲解等内容，添加完后，可以试试多选题目一键布置给班级、学生，流程更高效！
[图片: 快捷方式]
方式四：作业大纲满足老师完成体系化教学的作业编辑与任务下发，可以根据科目、班级情况、学生情况、教学任务等自定义添加个性化的作业大纲，并根据大纲关联题目类型，也是作业下发的一种更系统的方式。
[图片: 快捷方式]
作业布置类型
老师布置作业时，除了要选择作业布置对应的班级和学生以外，还需要确认作业布置的类型；系统为老师们提供基础练习、题型训练、模考测试、机构题库、自定义作业，打卡作业和视频课件作业七种主要的作业类型，帮助老师分层布置作业，精准提升学生能力。
[图片: 作业布置类型]
模考作业
模考作业协助老师发现学生薄弱环节，模考作业题型与形式和正式考试接近，能够提升学生对考试题型的掌握，训练学生应对考试的心理。
[图片: 模考作业]

图片说明：操作步骤
图片说明：快捷方式
图片说明：快捷方式
图片说明：快捷方式
图片说明：快捷方式
图片说明：作业布置类型
图片说明：模考作业
图片说明：模考作业
图片说明：基础练习
图片说明：题型训练
图片说明：机构题库
图片说明：自定义作业
图片说明：自定义作业
图片说明：打卡作业
图片说明：打卡作业
图片说明：打卡作业
图片说明：课件作业
```

### chunk_f25bf592086e4b6bb3a78b4cbb4b20b2 | 入门必备-老师/助教布置作业

- source_id：helpcenter:60
- document_id：doc_helpcenter_60
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-11T19:21:31
- 图片数：17
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559241086662610756680990", "alt_text": "操作步骤", "ocr_text": null, "caption": "操作步骤"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559304713404873412583490", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559377563000856427669450", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600517495457299513304227", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601416897933885051229952", "alt_text": "快捷方式", "ocr_text": null, "caption": "快捷方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051603016074142845015478569", "alt_text": "作业布置类型", "ocr_text": null, "caption": "作业布置类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051606447907998563063463536", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051606568581051689655822574", "alt_text": "模考作业", "ocr_text": null, "caption": "模考作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051610456822015369361971686", "alt_text": "基础练习", "ocr_text": null, "caption": "基础练习"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051610546068072598981342774", "alt_text": "题型训练", "ocr_text": null, "caption": "题型训练"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611028415148387327623992", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611224094459389549884389", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611307057662607091399084", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611391259085434640265814", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611469028867634987310408", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611503755251323578204973", "alt_text": "打卡作业", "ocr_text": null, "caption": "打卡作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611584596481445236775293", "alt_text": "课件作业", "ocr_text": null, "caption": "课件作业"}]

```text
模考作业可以在作业标题栏下方添加作业的【关联音视频】，方便辅助学生答题；在右下方可以将本次模考作业添加至【常用作业】，方便进行作业的二次快捷布置（小程序端也能使用常用作业）；也能对模考作业进行答题的【预览】。
[图片: 模考作业]
基础练习
基础练习包含单词训练和听说读写各分项的专项训练；包含多种训练方式，全方位巩固学生基础知识能力。
[图片: 基础练习]
题型训练
题型训练使用系统现有题目，包含科目相关的所有题型；雅思，托福，GRE，ACT，SAT等科目题型全覆盖，帮助老师为学生制定专属的提分计划。
[图片: 题型训练]
机构题库
机构题库作业可以选择机构自己在系统中录入的题目或试卷布置给学生进行训练，题型，知识点分类更加多样，选择更加灵活。
[图片: 机构题库]
自定义作业
老师可以通过自定义作业，布置课后的相关练习，布置个性化作业练习。
老师布置自定义作业时，可以上传图片，视频，音频和课件等，增加作业的布置形式。
[图片: 自定义作业]
老师可以在布置自定义作业选择是否添加答题卡，添加答题卡输入正确答案，学生作答完成后系统会进行自动批改。无答题卡，学生则需要上传作业相关的作答内容，老师进行手动的批改。
[图片: 自定义作业]
打卡作业
老师可以根据教学计划，使用打卡作业，老师设置打卡的时间段和打卡频次，系统会按照时间每天自动给学生下发打卡作业，还会按时提醒学生完成打卡作业；帮助老师监督学生学习，形成学习习惯。
[图片: 打卡作业]
打卡作业同样可以上传图片，视频，音频和课件等；还可以规定学生上传打卡作业的形式，设置是否允许学生补卡，是否查看其他学生作答内容等；精确打卡练习内容。
[图片: 打卡作业]
[图片: 打卡作业]
课件作业
课件作业主要用于给学生分享一些学习资料，例如课程相关的音视频和课件等；拓展老师的教学分享方式。
[图片: 课件作业]

图片说明：操作步骤
图片说明：快捷方式
图片说明：快捷方式
图片说明：快捷方式
图片说明：快捷方式
图片说明：作业布置类型
图片说明：模考作业
图片说明：模考作业
图片说明：基础练习
图片说明：题型训练
图片说明：机构题库
图片说明：自定义作业
图片说明：自定义作业
图片说明：打卡作业
图片说明：打卡作业
图片说明：打卡作业
图片说明：课件作业
```

### chunk_3a6cc218840f72562c4be4e7783eb328 | 排课时，上课常用时间段如何添加？

- source_id：helpcenter:83
- document_id：doc_helpcenter_83
- 分类：热门文章
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T16:30:59
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061524052339446375916296891", "alt_text": "添加常用时间段", "ocr_text": null, "caption": "添加常用时间段"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061524435925515664155239362", "alt_text": "添加常用时间段", "ocr_text": null, "caption": "添加常用时间段"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061524474475697823402400535", "alt_text": "添加常用时间段", "ocr_text": null, "caption": "添加常用时间段"}]

```text
排课时，上课常用时间段如何添加？
排课时，上课常用时间段如何添加？
系统可设置常用时间段，帮助老师高效排课
添加常用时间段
教务/校长在排课时，想增加或调整常用时间段，可以根据提示在设置-教学相关中增加
[图片: 添加常用时间段]
1）点击左边导航栏“设置”按钮
2）点击“教学相关”-“编辑上课时间”，点击添加，就可以增加常用时间段了
[图片: 添加常用时间段]
[图片: 添加常用时间段]

图片说明：添加常用时间段
图片说明：添加常用时间段
图片说明：添加常用时间段
```

### chunk_ab106dbe4e8c24ae6d8740f879d20918 | 一文读懂：如何进行公池-线索管理

- source_id：helpcenter:95
- document_id：doc_helpcenter_95
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:37:00
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051420544855739068801667050", "alt_text": "线索管理", "ocr_text": null, "caption": "线索管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051421488866805643658136321", "alt_text": "线索管理", "ocr_text": null, "caption": "线索管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051430484303172191174248212", "alt_text": "线索管理", "ocr_text": null, "caption": "线索管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051430526818265477952633608", "alt_text": "线索管理", "ocr_text": null, "caption": "线索管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051431252839348935876798089", "alt_text": "线索管理", "ocr_text": null, "caption": "线索管理"}]

```text
一文读懂：如何进行公池-线索管理
一文读懂：如何进行公池-线索管理
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍公池的功能。
线索管理
除了单个潜客录入，校校支持名单批量导入，方便机构管理数据。根据模版填写，即可一键上传。
[图片: 线索管理]
公池会展示所有跟进进度下的客户信息，教务可以根据有效性、跟进进度、负责销售等信息进潜筛选，查找数据。
[图片: 线索管理]
教务可以通过操作记录查看潜客删除记录以及名单导出记录，点击已查看详情即可查看具体学生信息。
[图片: 线索管理]
[图片: 线索管理]
需要查看潜客入学模考的教务，需要在员工管理，再给教务一个销售身份，打开查看入学模考的权限，即可在公池查看学生入学模考。潜客学生可以操作直接转正。
[图片: 线索管理]

图片说明：线索管理
图片说明：线索管理
图片说明：线索管理
图片说明：线索管理
图片说明：线索管理
```

### chunk_e5c180af04723619e5c156641f3f3af9 | 快捷排课操作技巧

- source_id：helpcenter:236
- document_id：doc_helpcenter_236
- 分类：使用技巧
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2025-09-11T17:28:25
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061354446083068348481458529", "alt_text": "列表模式下，一键修改排课信息", "ocr_text": null, "caption": "列表模式下，一键修改排课信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061355107166146827155853991", "alt_text": "如何查看排课变更记录", "ocr_text": null, "caption": "如何查看排课变更记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061355423780337405174068540", "alt_text": "视图模式下，一键排课技巧", "ocr_text": null, "caption": "视图模式下，一键排课技巧"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061357076230755858326994507", "alt_text": "视图模式下，一键排课技巧", "ocr_text": null, "caption": "视图模式下，一键排课技巧"}]

```text
快捷排课操作技巧
快捷排课操作技巧
快捷排课操作技巧
列表模式下，一键修改排课信息
点击右侧操作列表中的编辑，修改排课信息，选择时间，系统会生成新的排课并同时取消之前的排课！
[图片: 列表模式下，一键修改排课信息]
如何查看排课变更记录
点击操作列表右侧“记录”，即可实时查看排课变更记录！
[图片: 如何查看排课变更记录]
视图模式下，一键排课技巧
老师可以在视图模式下查找需要修改的排课，点击浮窗右侧“编辑”，即可修改排课信息及排课时间！
[图片: 视图模式下，一键排课技巧]
若修改排课时间冲突，系统会提示该时间段已有排课，老师点击切换上课时间段即可！
[图片: 视图模式下，一键排课技巧]

图片说明：列表模式下，一键修改排课信息
图片说明：如何查看排课变更记录
图片说明：视图模式下，一键排课技巧
图片说明：视图模式下，一键排课技巧
```

### chunk_a476767f5db9493f5c301026ed0216ac | 入门必备-老师/助教填写课堂反馈

- source_id：helpcenter:61
- document_id：doc_helpcenter_61
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T19:26:55
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051616536904977381391684530", "alt_text": "操作步骤", "ocr_text": null, "caption": "操作步骤"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051617006226337949956298529", "alt_text": "操作步骤", "ocr_text": null, "caption": "操作步骤"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051617062064737322293286586", "alt_text": "课堂反馈具体内容", "ocr_text": null, "caption": "课堂反馈具体内容"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051617135885298277313115126", "alt_text": "课堂反馈具体内容", "ocr_text": null, "caption": "课堂反馈具体内容"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051617206132894058284057817", "alt_text": "课堂反馈具体内容", "ocr_text": null, "caption": "课堂反馈具体内容"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051617456745115131368828137", "alt_text": "课堂反馈具体内容", "ocr_text": null, "caption": "课堂反馈具体内容"}]

```text
入门必备-老师/助教填写课堂反馈
入门必备-老师/助教填写课堂反馈
课堂反馈是教学中非常重要的一环，能够帮助学生和家长快速了解学生的学习情况，是家长和学生都十分关注的内容，那么老师该如何完成课堂的反馈呢？
操作步骤
老师登录系统，在左侧菜单栏找到【学员】选项，点击进入学员管理页面。
[图片: 操作步骤]
在学员管理页面，找到需要添加课堂反馈的学生，老师也可以通过左侧的搜索栏，输入学生信息，快速找到对应学生；找到对应学生后，点击上方【课程反馈】按钮即可为学员添加课堂反馈。
[图片: 操作步骤]
课堂反馈具体内容
老师在添加课堂反馈时，可选择学生对应的课程内容，设置该课程学生的考勤状态，根据校长/教务设置的课堂评分项对学生在该课程中的表现进行打分。
[图片: 课堂反馈具体内容]
设置完学生的考勤状态以及课堂评分后，老师还可以选择将该项反馈发送给学生，学生家长或者共享给本班级的所有学生及家长进行展示。
[图片: 课堂反馈具体内容]
同时，老师也可以在课程反馈中填写给学生的学习建议，对上一次学生的作业完成情况进行评价，提前告知学生下一次课程的要点，帮助学生更好的融入课程学习。
[图片: 课堂反馈具体内容]
课堂反馈也支持AI一键生成，校校根据学生学习考勤内容给出对应的建议
[图片: 课堂反馈具体内容]

图片说明：操作步骤
图片说明：操作步骤
图片说明：课堂反馈具体内容
图片说明：课堂反馈具体内容
图片说明：课堂反馈具体内容
图片说明：课堂反馈具体内容
```

### chunk_f3141dabb11fd52ace7deacb92f2d5f5 | 教务如何高效排课？

- source_id：helpcenter:86
- document_id：doc_helpcenter_86
- 分类：热门文章
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:13:04
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061517074602199539293742684", "alt_text": "智能排课", "ocr_text": null, "caption": "智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306151758291258417157073523", "alt_text": "智能排课", "ocr_text": null, "caption": "智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306151823885063034783176255", "alt_text": "智能排课", "ocr_text": null, "caption": "智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061520155673236852084655762", "alt_text": "智能排课", "ocr_text": null, "caption": "智能排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306152149746047330844841208", "alt_text": "传统排课", "ocr_text": null, "caption": "传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061522248264863762488063377", "alt_text": "传统排课", "ocr_text": null, "caption": "传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306152302874792353175466004", "alt_text": "传统排课", "ocr_text": null, "caption": "传统排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061523231549787853445256427", "alt_text": "传统排课", "ocr_text": null, "caption": "传统排课"}]

```text
教务如何高效排课？
教务如何高效排课？
班级多、时间跨度长，如何帮助教务老师实现快速排课？传统排课和智能排课的区别是什么，传统排课如何更高效?
智能排课
系统支持教务老师进行智能排课，点击导航栏“班级”，选择某个班级进入“排课”页面
[图片: 智能排课]
教务老师点击空白处可以排课，还可以勾选左侧的日历表，查看某位老师的排课详情！
[图片: 智能排课]
教务老师只需输入上课老师和上课时间两类信息，一键智能排课，系统自动排课并识别老师时间，学生时间以及上课地点冲突。
[图片: 智能排课]
排好的课表会显示未发布状态，教务老师可进行预览，觉得排课没问题点击确认发布即排课成功，觉得个别排课不合理也可拖动调整后再进行发布
[图片: 智能排课]
- 智能排课支持多次预排，即多次点击智能排课，进行课程预排，全部调整好之后，再发布。
- 已发布的课表，也支持拖动调整日期，或者点击设置按钮调整时间点。
传统排课
传统排课需要老师选择好课程信息，上课时间地点，更适合课程少，或者特定课程使用
[图片: 传统排课]
校校系统提供添加设置常用时间段和上课地点，可以帮助教务老师高效率排课
1）教务老师可以在设置-教学相关中编辑上课时间和上课地点，以供传统排课的时候一键点选
[图片: 传统排课]
2）教务老师排课时可以点击打开常用时间显示，点击任意灰色时间段就可以编辑课程了
[图片: 传统排课]
教务老师可以选择需要导出课表的月份，校校支持一键导出PDF课表
[图片: 传统排课]

图片说明：智能排课
图片说明：智能排课
图片说明：智能排课
图片说明：智能排课
图片说明：传统排课
图片说明：传统排课
图片说明：传统排课
图片说明：传统排课
```

### chunk_31d20dc21ebbfba2fcab5425fb4676c6 | 一文读懂：如何进行订单管理

- source_id：helpcenter:97
- document_id：doc_helpcenter_97
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:42:35
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051436081029259112657620415", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305143651419846112318170217", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051437378224575233827722125", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051438061693812069470066601", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051438558354488522840090334", "alt_text": "退费申请", "ocr_text": null, "caption": "退费申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051439571904312347845118309", "alt_text": "退费申请", "ocr_text": null, "caption": "退费申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051440028880495411497092080", "alt_text": "退费申请", "ocr_text": null, "caption": "退费申请"}]

```text
一文读懂：如何进行订单管理
一文读懂：如何进行订单管理
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍订单管理的功能。
订单管理功能介绍
合同订单
这里是所有的签约合同订单，查看合同详情、订单状态、⾦额、时间、实收⾦额、订单余额、课时余额等都可以在这里快速查看。
[图片: 合同订单]
点击订单详情，可以查看订单详情以及变更记录，同时可以添加订单备注。
[图片: 合同订单]
点击退费，可以查看订单剩余课时，金额，可以选退课时费或者资料费，也可以退回课时。备注退费原因方便管理。
[图片: 合同订单]
点击电子合同，可以选择合同模版，在预览界面可以调整公章和签名位置，可以下载合同或者生成合同链接给学生签署。
[图片: 合同订单]
退费申请
发起的订单退费申请，都会同步在这里，拥有审批权限的老师可通过或驳回退费申请，退的类型包括课时费、资料费等，退费方式包括支付宝、微信、退到账户余额等。
[图片: 退费申请]
确认退费前需要进行退费审批，可以在审批-退费审批操作。
[图片: 退费申请]
[图片: 退费申请]

图片说明：合同订单
图片说明：合同订单
图片说明：合同订单
图片说明：合同订单
图片说明：退费申请
图片说明：退费申请
图片说明：退费申请
```

### chunk_fe0625d7b362ae204e408d1ed525f1b4 | 入门必备-老师/助教创建作业大纲

- source_id：helpcenter:62
- document_id：doc_helpcenter_62
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T19:45:59
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051628047093973492031656285", "alt_text": "创建大纲", "ocr_text": null, "caption": "创建大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051625411650898813669649228", "alt_text": "添加目录", "ocr_text": null, "caption": "添加目录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051625497186504456643007820", "alt_text": "添加任务", "ocr_text": null, "caption": "添加任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626017291951323685294804", "alt_text": "关联作业类型", "ocr_text": null, "caption": "关联作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626096831989134589708758", "alt_text": "题库作业类型", "ocr_text": null, "caption": "题库作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626313748965286925467865", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626367052856533656209961", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305162648747501524922250459", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305162657129380580521233943", "alt_text": "修改任务下发时间", "ocr_text": null, "caption": "修改任务下发时间"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051627065066220571927504705", "alt_text": "修改任务下发时间", "ocr_text": null, "caption": "修改任务下发时间"}]

```text
入门必备-老师/助教创建作业大纲
入门必备-老师/助教创建作业大纲
下发作业步骤太繁琐？题目太多不好筛选？作业大纲助力老师高效管理课堂作业！
创建大纲
进入校校后台老师端，在导航栏中选择教研，在左侧导航栏中找到【教研】，选择创建大纲，即可添加大纲的科目与名称。
[图片: 创建大纲]
添加目录
确认添加大纲后，在左边【大纲目录】部分选择新添加的大纲，点击主页中目录名称旁的【+】号，即可添加目录。
[图片: 添加目录]
添加任务
成功添加目录后，将鼠标移动至目录，点击【+】即可添加其相关任务！
[图片: 添加任务]
关联作业类型
添加任务时，输入【任务名称】，选择【关联作业类型】，下方的关联按钮即可跳出相对应的界面。其中【单词】跳转至系统内的【基础练习（单词部分）】，音视频和课件跳转至云盘，老师可自行上传。
[图片: 关联作业类型]
题库作业类型
- 基础练习：分为单词，听，说，读，写五个类。为学生之后的学习打牢基础，其题目均来自正规考试。
- 题型训练：分为听力，阅读，写作，口语。系统将题库内的题目根据正规考试中所出现的题型进行分类，使学生能更精确的对自身薄弱的地方进行专项训练。
- 模考测试：校校系统自带的题库，供机构直接使用。
- 机构题库：需要提前在“题库管理”的“自有题库”中录入需要布置的题（录入完成后，即可在这里进行题目筛选布置）
- 自定义作业：机构可将自己的作业资料以复制粘切、图片、超链 接、音频等形式输入到文 本框， 也可以添加附件让学生下载查看做题。 
答题方式分为两种： 
1. 答题卡作答 (老师添加答题卡，将正确答案输入，学生作答结束后系统自动批改正误。) 
2. 无答题卡作答 (需要学生将写在纸上的答案拍照上传或上传音频作答内容，老师进行批改处理。)
[图片: 题库作业类型]
选择好需要关联的题目后，点击确认，作业大纲也就建立成功了！
关联作业大纲，下发作业
在导航栏中，选择【班级】。在我的班级中，找到需要关联作业大纲的班级。在主页面上半部分选择作业大纲 -关联
关联大纲之后可以选择下发日期、时间以及下发频次：下发频次对应目录的下发时间

图片说明：创建大纲
图片说明：添加目录
图片说明：添加任务
图片说明：关联作业类型
图片说明：题库作业类型
图片说明：关联作业大纲，下发作业
图片说明：关联作业大纲，下发作业
图片说明：关联作业大纲，下发作业
图片说明：修改任务下发时间
图片说明：修改任务下发时间
```

### chunk_00e8e97297bae7a43adf6edc85099392 | 入门必备-老师/助教创建作业大纲

- source_id：helpcenter:62
- document_id：doc_helpcenter_62
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-11T19:45:59
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051628047093973492031656285", "alt_text": "创建大纲", "ocr_text": null, "caption": "创建大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051625411650898813669649228", "alt_text": "添加目录", "ocr_text": null, "caption": "添加目录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051625497186504456643007820", "alt_text": "添加任务", "ocr_text": null, "caption": "添加任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626017291951323685294804", "alt_text": "关联作业类型", "ocr_text": null, "caption": "关联作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626096831989134589708758", "alt_text": "题库作业类型", "ocr_text": null, "caption": "题库作业类型"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626313748965286925467865", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626367052856533656209961", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305162648747501524922250459", "alt_text": "关联作业大纲，下发作业", "ocr_text": null, "caption": "关联作业大纲，下发作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305162657129380580521233943", "alt_text": "修改任务下发时间", "ocr_text": null, "caption": "修改任务下发时间"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051627065066220571927504705", "alt_text": "修改任务下发时间", "ocr_text": null, "caption": "修改任务下发时间"}]

```text
[图片: 关联作业大纲，下发作业]
[图片: 关联作业大纲，下发作业]
关联后可以设置每个目录下任务的下发频次，如果需要每天下发1个，需要选择周一-周天，如果只需要每周特定的某天下发，频次可以选择那一天
[图片: 关联作业大纲，下发作业]
将该班级确认关联大纲后，点击【发布】，在班级中的学生即可收到关联的作业。
修改任务下发时间
在班级界面，进入“作业大纲”后，点击任务列表中显示为蓝色的日期，即可单独调整该任务的下发日期与时间。
[图片: 修改任务下发时间]
勾选【任务下发频次】：子集任务将按照所选频率依次下发！
 不勾选【任务下发频次】：所有子集任务将于同一时间统一下发！
 注：已下发的作业无法修改时间。
[图片: 修改任务下发时间]

图片说明：创建大纲
图片说明：添加目录
图片说明：添加任务
图片说明：关联作业类型
图片说明：题库作业类型
图片说明：关联作业大纲，下发作业
图片说明：关联作业大纲，下发作业
图片说明：关联作业大纲，下发作业
图片说明：修改任务下发时间
图片说明：修改任务下发时间
```

### chunk_7531f7469b915e39c6af648b9d6440d1 | 老师如何填写课堂反馈？

- source_id：helpcenter:89
- document_id：doc_helpcenter_89
- 分类：热门文章
- 适用角色库：teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:24:33
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061511476744461862725051023", "alt_text": "添加课堂反馈", "ocr_text": null, "caption": "添加课堂反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030615120281759982471526908", "alt_text": "添加课堂反馈", "ocr_text": null, "caption": "添加课堂反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061513399015489854930480258", "alt_text": "在“学员管理”页面添加", "ocr_text": null, "caption": "在“学员管理”页面添加"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061514555315041724452600223", "alt_text": "在“班级”页面添加", "ocr_text": null, "caption": "在“班级”页面添加"}]

```text
老师如何填写课堂反馈？
老师如何填写课堂反馈？
课堂完成之后，老师需要给学生添加课堂反馈更好的记录学生上课情况以及知识掌握情况，校校提供多样的反馈形式，支持机构自定义反馈内容。帮助老师更好的记录学生学习！
添加课堂反馈
老师在课堂完成之后，可以在首页-待办事项-待反馈处，点击添加课堂评分和学习建议，学习建议可以使用ai 一键生成。
[图片: 添加课堂反馈]
[图片: 添加课堂反馈]
在“学员管理”页面添加
点击学生头像，可以在课程反馈处添加课堂评分和学习建议，可以选择课堂并修改学生签到状态
[图片: 在“学员管理”页面添加]
在“班级”页面添加
点击某个班级，可以在反馈处添加课堂评分和学习建议，可以选择课堂并修改学生签到状态
[图片: 在“班级”页面添加]
自定义评分项及文字评价项
校长/教务端可以在导航栏“设置”中，点击“教学相关”，下滑页面找到课堂反馈设置，点击自定义设置反馈

图片说明：添加课堂反馈
图片说明：添加课堂反馈
图片说明：在“学员管理”页面添加
图片说明：在“班级”页面添加
```

### chunk_fb5220a389091d73b5d7b98074a7e1fd | 一文了解：如何使用数据分析功能

- source_id：helpcenter:99
- document_id：doc_helpcenter_99
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:06:26
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051441491620785729388896988", "alt_text": "销售数据统计", "ocr_text": null, "caption": "销售数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442251805860564790522763", "alt_text": "运营数据统计", "ocr_text": null, "caption": "运营数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442406761390661777323968", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051442599053450815265080640", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051443224047318367988076834", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051444241081936854846452413", "alt_text": "市场数据统计", "ocr_text": null, "caption": "市场数据统计"}]

```text
一文了解：如何使用数据分析功能
一文了解：如何使用数据分析功能
教务端的功能与校长端相同，但校长是默认拥有所有的权限，教务可以进行选择，您可以根据教务角色的工作分配不同权限，下文将会介绍统计分析的功能。
统计分析功能介绍
销售数据统计
1) 当日、近7天、近30天基础销售数据统计
2) 销售顾问工作情况：多维度销售数据统计
3) 签约⾦额：校区营收数据分析
4) 销售漏斗
销售及试听转化率走势图；
顾问转化率数据及关单周期、销售能力、关单数据⼀目了然；
销售漏斗清晰展示各跟进进度潜客数
[图片: 销售数据统计]
运营数据统计
在读学生人数趋势图、老师授课课时柱状图 (点击查看详情，了解具体课时情况) 、学生消课课时柱状图(点击查看详情、了解具体课时情况) 、老师带班人数柱状图和学生出勤率百分比趋势图等。
[图片: 运营数据统计]
教学数据统计
教学统计包括：学生分析、老师分析、提分分析。
[图片: 教学数据统计]
学生分析
1) 点击查看下详情，即可看到学生作业完成率，正确率，平均练习时长走势图，快速概览学生作业数据趋势；
2) 学生提分分析，以散点图形式，清晰罗列与学生相关各大元素与其提分走势的相关性，精准把握关键变量，提高学习效率；
3) 单个学生学习数据汇总，让过程与结果更明了，让决策更精准
[图片: 教学数据统计]
老师分析
1) 老师平均提分率，作业查阅率，反馈效率数据统计；
2) 老师提分分析，以散点图形式，清晰罗列与老师工作中的变量因素对提分的影响，精准分析核心变量，提高教学效率；
3) 老师工作数据统计，让教学过程更加透明，更高效
[图片: 教学数据统计]
市场数据统计
市场数据可以查看签约人数、金额。点击查看详情即可查看校区相关签约数据。
[图片: 市场数据统计]

图片说明：销售数据统计
图片说明：运营数据统计
图片说明：教学数据统计
图片说明：教学数据统计
图片说明：教学数据统计
图片说明：市场数据统计
```

### chunk_4222479fd0cd626482383dbe39dfb870 | 入门必备-老师/教研创建机构自有题库

- source_id：helpcenter:63
- document_id：doc_helpcenter_63
- 分类：初次使用指南
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T19:55:27
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051637385332462878094871328", "alt_text": "创建试卷", "ocr_text": null, "caption": "创建试卷"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051637436982110397427731004", "alt_text": "创建试卷", "ocr_text": null, "caption": "创建试卷"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051637495841307441608563263", "alt_text": "录入题目", "ocr_text": null, "caption": "录入题目"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051637573301281138523152236", "alt_text": "编辑题目", "ocr_text": null, "caption": "编辑题目"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638031424534755456130049", "alt_text": "编辑题目", "ocr_text": null, "caption": "编辑题目"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638114916401517567482132", "alt_text": "自定义分数", "ocr_text": null, "caption": "自定义分数"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638206884343233451824482", "alt_text": "自定义分数", "ocr_text": null, "caption": "自定义分数"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638268782672076072514960", "alt_text": "自定义分数", "ocr_text": null, "caption": "自定义分数"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638363543153276722646040", "alt_text": "自定义分数", "ocr_text": null, "caption": "自定义分数"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163843762079119116428498", "alt_text": "简答题支持AI智能批改", "ocr_text": null, "caption": "简答题支持AI智能批改"}]

```text
入门必备-老师/教研创建机构自有题库
入门必备-老师/教研创建机构自有题库
系统为机构配备海量题库，并支持机构上传自有题库，一起来看看老师如何上传题库吧！
创建试卷
在导航栏中选择题库，主页中选择【机构题库】-【新建试卷】，即可创建试卷，编辑试卷名称，科目和类别，添加题目！
[图片: 创建试卷]
[图片: 创建试卷]
录入题目
新建试卷可以直接进入录题界面，也可以点击试卷卡片，点击录入
[图片: 录入题目]
编辑题目
在录题界面，老师可以录入多种【交互类型】（即多种题型），我们根据实际考试中会出现的交互类型都做了分类，以便老师可以选择更合适的显示界面。
[图片: 编辑题目]
老师也可以使用AI出题，生成需要的题目，可以选择题目类型，年级以及课程标准。
[图片: 编辑题目]
自定义分数
校区机构自有题库上传支持自定义设置分数，将试卷题目编辑好后，在题目列表页面可以点击【分数换算】即可自定义试卷分数规则，系统会根据试卷题目分类及原始分区间，设置标准分换算规则！
[图片: 自定义分数]
创建模板
如果校区机构试卷题型算分一致，可以先点击【新增模板】创建通用模板，后面的试卷也可以直接应用！
[图片: 自定义分数]
[图片: 自定义分数]
也可以为单独的试卷，设置【自定义规则】，自定义规则只使用在该套试卷，不会影响模板规则
[图片: 自定义分数]
简答题支持AI智能批改
老师录入题目时，可以上传【批改规则】，AI 会根据标准自动批改。老师在机构题库中添加简答题，填写答案框，编辑批改规则。
[图片: 简答题支持AI智能批改]

图片说明：创建试卷
图片说明：创建试卷
图片说明：录入题目
图片说明：编辑题目
图片说明：编辑题目
图片说明：自定义分数
图片说明：自定义分数
图片说明：自定义分数
图片说明：自定义分数
图片说明：简答题支持AI智能批改
```

### chunk_908b38abeaad3e1ce502e4e10e85eb57 | 如何自定义课堂反馈评分项及文字评价项？

- source_id：helpcenter:96
- document_id：doc_helpcenter_96
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T17:38:29
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061504062434552583305765538", "alt_text": "自定义评分项及文字评价项", "ocr_text": null, "caption": "自定义评分项及文字评价项"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061504103109340306123757090", "alt_text": "自定义评分项及文字评价项", "ocr_text": null, "caption": "自定义评分项及文字评价项"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061504327990533293658872265", "alt_text": "自定义评分项及文字评价项", "ocr_text": null, "caption": "自定义评分项及文字评价项"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061504562204492159664982698", "alt_text": "自定义评分项及文字评价项", "ocr_text": null, "caption": "自定义评分项及文字评价项"}]

```text
如何自定义课堂反馈评分项及文字评价项？
如何自定义课堂反馈评分项及文字评价项？
系统支持自定义课堂反馈评分项和文字评价项，机构可以根据教学特点以及机构特点设置专属于机构的课堂反馈
自定义评分项及文字评价项
1）校长/教务端可以在导航栏“设置”中，点击“教学相关”，下滑页面找到课堂反馈设置，点击自定义设置反馈
[图片: 自定义评分项及文字评价项]
[图片: 自定义评分项及文字评价项]
2）点击添加可以增加新的评分项，也可以删除旧的评分项 （注：删除旧的评分项会对之前已经评过分的学生产生影响）
[图片: 自定义评分项及文字评价项]
3）点击添加可以增加新的文字评价项，同时添加新的文字评价项可以设置为是否为必填项。也可以删除旧的文字评价项（注：删除旧的文字项不会对之前已经评过分的学生产生影响）
[图片: 自定义评分项及文字评价项]

图片说明：自定义评分项及文字评价项
图片说明：自定义评分项及文字评价项
图片说明：自定义评分项及文字评价项
图片说明：自定义评分项及文字评价项
```

### chunk_4918d979d9de19d0ca6acf4e6526707e | 快速玩转教务端小程序

- source_id：helpcenter:100
- document_id：doc_helpcenter_100
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:09:40
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061434501242055139509122288", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121806331908060984827482590", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121806253693984173352656061", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121807502106308061044424543", "alt_text": "教学数据报告", "ocr_text": null, "caption": "教学数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230412180759371295059964211741", "alt_text": "教学数据报告", "ocr_text": null, "caption": "教学数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121808461183778215356918347", "alt_text": "运营数据报告", "ocr_text": null, "caption": "运营数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121809326678302768725662576", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121809266530446046780852396", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101720342209931116036923297", "alt_text": "查看校币记录", "ocr_text": null, "caption": "查看校币记录"}]

```text
快速玩转教务端小程序
快速玩转教务端小程序
教务身份可以由机构设置可以查看数据的权限，下面展示的为所有去权限都已开通的教务账号登陆小程序。
小程序数据报告
教务在电脑上登陆系统之后，可以在右上角点击【小程序】按钮，使用微信扫码登陆小程序。
[图片: 小程序数据报告]
登陆小程序首页可以查看【教学数据报告】和【运营数据报告】。
[图片: 小程序数据报告]
[图片: 小程序数据报告]
教学数据报告
教务可以分科目查看授课课时、作业完成率、作业正确率、课堂反馈等教学数据汇总分析。
可以查看学生作业完成率、正确率、模考分数排名，实时检验教学成效。
[图片: 教学数据报告]
[图片: 教学数据报告]
运营数据报告
运营数据报告，包含学员状态、课消课时，金额等数据实时汇总更新。
[图片: 运营数据报告]
待办通知
系统会自动发送代办通知：试听待排课以及班级待排课，逾期的也可以进行查看和操作。
[图片: 待办通知]
[图片: 待办通知]
查看校币记录
点击我的，即可看到校币剩余情况，点击查看详情即可查看校币的具体消耗
[图片: 查看校币记录]

图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：教学数据报告
图片说明：教学数据报告
图片说明：运营数据报告
图片说明：待办通知
图片说明：待办通知
图片说明：查看校币记录
```

### chunk_2e726cad228fbb083d648022f1770387 | 入门必备-老师/助教添加机构教研内容

- source_id：helpcenter:64
- document_id：doc_helpcenter_64
- 分类：初次使用指南
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-11T20:00:30
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051652557116870995592834968", "alt_text": "编辑系统题库", "ocr_text": null, "caption": "编辑系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051653071628079160235719399", "alt_text": "添加知识点和名师讲解", "ocr_text": null, "caption": "添加知识点和名师讲解"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509031516307203210442324783100", "alt_text": "添加知识点和名师讲解", "ocr_text": null, "caption": "添加知识点和名师讲解"}]

```text
入门必备-老师/助教添加机构教研内容
入门必备-老师/助教添加机构教研内容
系统为机构老师提供标准化知识点切分，当老师有自己独树一帜的知识点讲解时，该如何在系统中快速操作？
编辑系统题库
在导航栏中选择【题库】，主页栏上半部分可以选择不同科目下的套题，在找到想要讲解的题目后，点击【详情】！
[图片: 编辑系统题库]
添加知识点和名师讲解
进入题目界面后，老师可以选择【名师讲解】天添加自己的讲解内容，学生做完题目就能查看。
[图片: 添加知识点和名师讲解]
老师也可以添加题目知识点，更有针对性！
[图片: 添加知识点和名师讲解]

图片说明：编辑系统题库
图片说明：添加知识点和名师讲解
图片说明：添加知识点和名师讲解
```

### chunk_acddcab1204aab9d0549cba8a5ae46c1 | 一文了解：如何使用首页功能

- source_id：helpcenter:106
- document_id：doc_helpcenter_106
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:32:00
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051452086790865238352076166", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051452298148272190191962356", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051453154907439369851535057", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051453302019224408498643349", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}]

```text
一文了解：如何使用首页功能
一文了解：如何使用首页功能
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
首页功能展示
系统销售端首页设置展示了销售个人/团队的销售目标、销售业绩和销售转化等数据情况；帮助销售实时掌握个人和团队课程销售情况。
[图片: 首页功能展示]
点击目标设置即可设置所有销售目标、试听目标、自己的目标。设置好后点击左上角切换就可以查看个人和团队的业绩完成情况。
[图片: 首页功能展示]
销售可以按周、月、季度查看目标完成情况。关键指标可以进行排序查看，也可以一键导出
[图片: 首页功能展示]
首页还可以查看业绩排名，可以按照时间筛选。关键的销售漏斗分析帮助管理员更好的管理。
[图片: 首页功能展示]

图片说明：首页功能展示
图片说明：首页功能展示
图片说明：首页功能展示
图片说明：首页功能展示
```

### chunk_ad0de806629cfa42b96d98010ab1a97b | 视图模式下如何一键排课？

- source_id：helpcenter:147
- document_id：doc_helpcenter_147
- 分类：热门文章
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T15:21:54
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061503132750298595053632855", "alt_text": "视图模式下快速排课", "ocr_text": null, "caption": "视图模式下快速排课"}]

```text
视图模式下如何一键排课？
视图模式下如何一键排课？
系统为教务老师实现了一键快速排课功能？如临时有排课需求的老师，可以试试这样操作！
视图模式下快速排课
拥有校长或教务权限的老师可以点击左侧导航栏【课表】，上方切换为【视图模式】，点击课表空白处，即可进行排课！注意：老师可以查看日历表时间，如需排周二11号的课，即可点击相应空白处！
[图片: 视图模式下快速排课]
填写排课信息
点击空白处，系统会自动弹出排课列表，老师填写排课信息即可快速完成排课！

图片说明：视图模式下快速排课
```

### chunk_c5e13f7f82cb20a4de3654629c24bf6d | 一文读懂：如何进行潜客管理

- source_id：helpcenter:107
- document_id：doc_helpcenter_107
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:33:46
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051454097281457175498455126", "alt_text": "潜客管理功能展示", "ocr_text": null, "caption": "潜客管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051454341067238835694740924", "alt_text": "潜客管理功能展示", "ocr_text": null, "caption": "潜客管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051454522156097606639676189", "alt_text": "潜客管理功能展示", "ocr_text": null, "caption": "潜客管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051455168085945863333150441", "alt_text": "潜客管理功能展示", "ocr_text": null, "caption": "潜客管理功能展示"}]

```text
一文读懂：如何进行潜客管理
一文读懂：如何进行潜客管理
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
潜客管理功能展示
销售点击左侧导航栏中的【潜客】按钮，进入潜客管理页面，这里会显示该销售人员跟进的潜客，销售可在潜客管理页面添加新的潜客（潜客名单可批量导入和导出）。
[图片: 潜客管理功能展示]
添加的潜客会区分不同的跟进进度，在对应潜客信息最后可点击【入学模测】查看潜客的入学模测结果，点击【编辑】可进行潜客信息编辑，包括潜客基础信息、学习目标、信息来源、沟通信息等，沟通过程中可以不断完善潜客信息。
[图片: 潜客管理功能展示]
[图片: 潜客管理功能展示]
沟通信息包括潜客、跟进中、已预约、已试听、已签约等，所有沟通记录累积保存。填写沟通信息时，可设置下次沟通时间，系统会进行自动跟进提醒。已预约试听的潜客信息会同步给教务进行试听排课，已签约的潜客，会进入到订单中进行查看。
[图片: 潜客管理功能展示]

图片说明：潜客管理功能展示
图片说明：潜客管理功能展示
图片说明：潜客管理功能展示
图片说明：潜客管理功能展示
```

### chunk_2492b7c382f28ad0ee8727881cb84cfa | 校长端如何实时查看运营数据

- source_id：helpcenter:127
- document_id：doc_helpcenter_127
- 分类：初次使用指南
- 适用角色库：principal(校长库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:05:46
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700201430407163935625752", "alt_text": "销售数据统计", "ocr_text": null, "caption": "销售数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700277669784506293350078", "alt_text": "运营统计", "ocr_text": null, "caption": "运营统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700351148710451704323253", "alt_text": "教学统计", "ocr_text": null, "caption": "教学统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700422554872248202314193", "alt_text": "教学统计", "ocr_text": null, "caption": "教学统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700498307712332419149084", "alt_text": "教学统计", "ocr_text": null, "caption": "教学统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700582666864689851594157", "alt_text": "财务数据统计", "ocr_text": null, "caption": "财务数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051701056955675255431858102", "alt_text": "市场数据统计", "ocr_text": null, "caption": "市场数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121902574101457698733084465", "alt_text": "销售数据报告", "ocr_text": null, "caption": "销售数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121904141509153702845732381", "alt_text": "销售数据报告", "ocr_text": null, "caption": "销售数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121904437772230531358248163", "alt_text": "教学数据报告", "ocr_text": null, "caption": "教学数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121905059089711427527420075", "alt_text": "教学数据报告", "ocr_text": null, "caption": "教学数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101708063577309040369049426", "alt_text": "运营数据报告", "ocr_text": null, "caption": "运营数据报告"}]

```text
校长端如何实时查看运营数据
校长端如何实时查看运营数据
校长端可以实时查看哪些数据？销售、运营、教学、财务、市场等数据，登陆小程序即可随时随地查看数据！
销售数据统计
1) 当日、近7天、近30天基础销售数据统计
2) 销售顾问工作情况：多维度销售数据统计
3) 签约⾦额： 校区营收数据分析
4) 销售漏斗 
销售及试听转化率走势图
顾问转化率数据及关单周期、销售能力、关单数据⼀目了然
销售漏斗清晰展示各跟进进度潜客数
[图片: 销售数据统计]
运营统计
在读学生人数趋势图、老师授课课时柱状图（点击查看详情，了解具体课时情况）、学生消课课时柱状图 （点击查看详情，了解具体课时情况）、老师带班人数柱状图和学生出勤率百分比趋势图等。
[图片: 运营统计]
教学统计
教学统计包括：学生分析、老师分析、提分分析
[图片: 教学统计]
1) 点击查看下详情，即可看到学生作业完成率、正确率、平均练习时长走势图、快速概览学生作业数据趋势
2) 学生提分分析，以散点图形式，清晰罗列与学生相关各大元素与其提分走势的相关 性， 精准把握关键变量，提高学习效率
3) 单个学生学习数据汇总，让过程与结果更明了，让决策更精准
[图片: 教学统计]
1) 老师平均提分率，作业查阅率，反馈效率数据统计
2) 老师提分分析，以散点图形式，清晰罗列与老师工作中的变量因素对提分的影响， 精准分析核心变量， 提高教学效率
3) 老师工作数据统计，让教学过程更加透明，更高效
[图片: 教学统计]
财务数据统计
财务统计包括现金流统计、消课和退费统计
[图片: 财务数据统计]
市场数据统计
市场数据可以查看签约人数、金额。点击查看详情即可查看校区相关签约数据。
[图片: 市场数据统计]
小程序数据报告
打开手机，校区运营管理全掌握！
销售数据报告
分时段销售数据汇总分析，可以查看日/周/月/季度数据
[图片: 销售数据报告]
一键查看销售业绩，试听量排名
[图片: 销售数据报告]
教学数据报告
校长可以分科目查看授课课时、作业完成率、作业正确率、课堂反馈等教学数据汇总分析
[图片: 教学数据报告]

图片说明：销售数据统计
图片说明：运营统计
图片说明：教学统计
图片说明：教学统计
图片说明：教学统计
图片说明：财务数据统计
图片说明：市场数据统计
图片说明：销售数据报告
图片说明：销售数据报告
图片说明：教学数据报告
图片说明：教学数据报告
图片说明：运营数据报告
```

### chunk_fe96f45c56f4b8ff2c8730ece0ec57a0 | 校长端如何实时查看运营数据

- source_id：helpcenter:127
- document_id：doc_helpcenter_127
- 分类：初次使用指南
- 适用角色库：principal(校长库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T19:05:46
- 图片数：12
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700201430407163935625752", "alt_text": "销售数据统计", "ocr_text": null, "caption": "销售数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700277669784506293350078", "alt_text": "运营统计", "ocr_text": null, "caption": "运营统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700351148710451704323253", "alt_text": "教学统计", "ocr_text": null, "caption": "教学统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700422554872248202314193", "alt_text": "教学统计", "ocr_text": null, "caption": "教学统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700498307712332419149084", "alt_text": "教学统计", "ocr_text": null, "caption": "教学统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051700582666864689851594157", "alt_text": "财务数据统计", "ocr_text": null, "caption": "财务数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051701056955675255431858102", "alt_text": "市场数据统计", "ocr_text": null, "caption": "市场数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121902574101457698733084465", "alt_text": "销售数据报告", "ocr_text": null, "caption": "销售数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121904141509153702845732381", "alt_text": "销售数据报告", "ocr_text": null, "caption": "销售数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121904437772230531358248163", "alt_text": "教学数据报告", "ocr_text": null, "caption": "教学数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121905059089711427527420075", "alt_text": "教学数据报告", "ocr_text": null, "caption": "教学数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101708063577309040369049426", "alt_text": "运营数据报告", "ocr_text": null, "caption": "运营数据报告"}]

```text
可以查看学生作业完成率、正确率、模考分数排名，实时检验教学成效
[图片: 教学数据报告]
运营数据报告
运营数据报告，包含学员状态、课消、课时、现金流等数据实时汇总更新，随时随地管理校区
[图片: 运营数据报告]

图片说明：销售数据统计
图片说明：运营统计
图片说明：教学统计
图片说明：教学统计
图片说明：教学统计
图片说明：财务数据统计
图片说明：市场数据统计
图片说明：销售数据报告
图片说明：销售数据报告
图片说明：教学数据报告
图片说明：教学数据报告
图片说明：运营数据报告
```

### chunk_413c19aa927f74e683443efe21a03674 | 学生账号如何续期？

- source_id：helpcenter:168
- document_id：doc_helpcenter_168
- 分类：热门文章
- 适用角色库：student(学生库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-19T14:58:51
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061502199110289673568538370", "alt_text": "续期操作流程", "ocr_text": null, "caption": "续期操作流程"}]

```text
学生账号如何续期？
学生账号如何续期？
学生账号如果到期，教务/校长可以进行续期管理
续期操作流程
教务/校长登陆系统之后，点击学员管理，可以看到学生姓名旁的圆点（蓝色为启用状态，红色为停用状态，黄色为本月内即将到期）
[图片: 续期操作流程]
找到需要续期的学生账号，点击学生姓名旁的小圆点，点击【续期】即可完成操作
注：续期一次即消耗一个学生账号，点击续期后，账号服务期从当日起计时

图片说明：续期操作流程
```

### chunk_12e12bf9fe0e7731d70834e0add35199 | 一文读懂：如何进行学员管理

- source_id：helpcenter:109
- document_id：doc_helpcenter_109
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:35:57
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051456097920004645823205870", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051456324924573905210645415", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305145659271120950742667160", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051457531419731053787921166", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051458344688179166871348671", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051458538673589524660464231", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030514591185540935979883713", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051459307028568138455141523", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051459488052248465776883226", "alt_text": "学员管理功能展示", "ocr_text": null, "caption": "学员管理功能展示"}]

```text
一文读懂：如何进行学员管理
一文读懂：如何进行学员管理
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
学员管理功能展示
销售点击左侧导航栏中的【学员】按钮，进入学员管理页面，这里可以对销售已签约的学员和机构分配的正式学员进行管理，可以查看学员的基本信息、合同、相关记录和学习情况、方便销售进行该学员的后续续费。
[图片: 学员管理功能展示]
销售点击续费即可操作给学生报课，可以选择新报、续报、扩科三中类型。选择对应的课程课时即可生成订单。
[图片: 学员管理功能展示]
课表任务：销售可以在课表查看学生目前的课程、任务安排，如果学生有多个班级，可以进行筛选查看。
[图片: 学员管理功能展示]
学习报告：这里可以查看老师给学生生成的学习报告，可以按科目、时间、生成人进行筛选。
[图片: 学员管理功能展示]
练习情况：练习统计下可以查看学生的作业练习统计、错题分析、以及笔记。
[图片: 学员管理功能展示]
老师填写的课程反馈销售也可以在这里查看，可以筛选班级查看。
[图片: 学员管理功能展示]
合同页面可以查看学生目前的所有订单，点击详情即可查看订单详情，点击单子合同可以查看已签的合同或者生成合同给学生签署。
[图片: 学员管理功能展示]
添加回访：需要回访的学生，销售可以在这里添加回访记录。
[图片: 学员管理功能展示]
考试记录：销售可以添加学生的考试记录，设置好时间可以选择考前通知。
[图片: 学员管理功能展示]

图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
图片说明：学员管理功能展示
```

### chunk_e417dec0a4a8aba05c0eae44df11ca26 | 如何开启写作口语智能评分？

- source_id：helpcenter:169
- document_id：doc_helpcenter_169
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-19T15:14:41
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061458034235161299675787809", "alt_text": "开启智能评分", "ocr_text": null, "caption": "开启智能评分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111517074033594995424803075", "alt_text": "开启智能评分", "ocr_text": null, "caption": "开启智能评分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111523172133234928276219889", "alt_text": "开启智能评分", "ocr_text": null, "caption": "开启智能评分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111523216959178266141309660", "alt_text": "开启智能评分", "ocr_text": null, "caption": "开启智能评分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111526212402459492950142893", "alt_text": "开启智能评分", "ocr_text": null, "caption": "开启智能评分"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111526328196822723856409978", "alt_text": "开启智能评分", "ocr_text": null, "caption": "开启智能评分"}]

```text
如何开启写作口语智能评分？
如何开启写作口语智能评分？
口语写作智能评分开启后系统会对口语和写作作业进行智能修改，减轻老师负担！下文将介绍如何开启写作口语智能评分。
开启智能评分
教务/校长再登陆系统之后，可以点击左侧导航栏【设置】，点击【教学相关】找到写作智能批改和口语智能批改，点击右侧开启按钮即可打开智能评分。
注：开启口语智能评分，仅对开启之后学生完成的作业有效，之前的作业仍需要老师手动批改
[图片: 开启智能评分]
写作智能批改根据官方考试评分标准，智能批改给出分项批改建议，包括整体评价、任务回应、句子连贯、词汇资源、语法等维度，并且还提供逐句批改及润色文章。
[图片: 开启智能评分]
[图片: 开启智能评分]
[图片: 开启智能评分]
口语智能评分根据学生的发音、流利度、词汇多样性、语法等多维度评分，给出精准的批改建议，同时支持根据批改建议给出润色后的口语文章。
[图片: 开启智能评分]
[图片: 开启智能评分]

图片说明：开启智能评分
图片说明：开启智能评分
图片说明：开启智能评分
图片说明：开启智能评分
图片说明：开启智能评分
图片说明：开启智能评分
```

### chunk_f9d5222403437e8f28628ff85de6e661 | 一文读懂：如何进行试听课学员管理

- source_id：helpcenter:111
- document_id：doc_helpcenter_111
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:36:46
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051507413865512318103565789", "alt_text": "试听课学员管理功能展示", "ocr_text": null, "caption": "试听课学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051507443521301523182429253", "alt_text": "试听课学员管理功能展示", "ocr_text": null, "caption": "试听课学员管理功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051508028577755956530268742", "alt_text": "试听课学员管理功能展示", "ocr_text": null, "caption": "试听课学员管理功能展示"}]

```text
一文读懂：如何进行试听课学员管理
一文读懂：如何进行试听课学员管理
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
试听课学员管理功能展示
在潜客页面，预约了课程的学生，预约记录会显示在试听页面
[图片: 试听课学员管理功能展示]
[图片: 试听课学员管理功能展示]
销售点击左侧导航栏中的【试听】按钮，进入试听学员管理页面，销售可以查看试听学生记录，所有预约过试听课的学员信息都会出现在这里。包含学员的基本信息、预约课程、上课老师、时间和地点以及试听课排课状态。
[图片: 试听课学员管理功能展示]

图片说明：试听课学员管理功能展示
图片说明：试听课学员管理功能展示
图片说明：试听课学员管理功能展示
```

### chunk_4bc240c2f08bd86dfb92abedbd95d3d4 | 添加学生时，提示号码已在公池占用如何处理？

- source_id：helpcenter:170
- document_id：doc_helpcenter_170
- 分类：热门文章
- 适用角色库：student(学生库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-19T15:21:13
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061454464030208973929278571", "alt_text": "添加学生账号", "ocr_text": null, "caption": "添加学生账号"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061455433425268108215382512", "alt_text": "修改手机号码", "ocr_text": null, "caption": "修改手机号码"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061457227804604091110050760", "alt_text": "修改手机号码", "ocr_text": null, "caption": "修改手机号码"}]

```text
添加学生时，提示号码已在公池占用如何处理？
添加学生时，提示号码已在公池占用如何处理？
教务/校长在添加学生账号或将学生账号转为vip账号时，可能会遇到系统提示：号码已在公池占用，下文将带您解决此类问题。
添加学生账号
教务/校长在添加学生账号时，系统提示：“手机号在用户池中已存在”时
可以根据提示直接将正在添加的学员转为正式学员
[图片: 添加学生账号]
修改手机号码
教务/校长在修改学生手机号码时，系统提示：“新的号码已在用户池占用” 有以下解决方法。
[图片: 修改手机号码]
可以在公池搜索该被占用的号码，然后点击编辑，修改这个号码的任意数字，
再回到学员编辑这里，填写正确的号码，即可修改手机号。
[图片: 修改手机号码]

图片说明：添加学生账号
图片说明：修改手机号码
图片说明：修改手机号码
```

### chunk_036283352626531cd5ac71345f7188db | 一文读懂：如何进行合同订单管理

- source_id：helpcenter:112
- document_id：doc_helpcenter_112
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:40:16
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051508404131792983908608941", "alt_text": "- 订单管理", "ocr_text": null, "caption": "- 订单管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305150904286629394780910176", "alt_text": "- 订单管理", "ocr_text": null, "caption": "- 订单管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305150922660576185208546332", "alt_text": "- 订单管理", "ocr_text": null, "caption": "- 订单管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051509393491416240597378689", "alt_text": "- 订单管理", "ocr_text": null, "caption": "- 订单管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051509572444383591957036394", "alt_text": "- 退费管理", "ocr_text": null, "caption": "- 退费管理"}]

```text
一文读懂：如何进行合同订单管理
一文读懂：如何进行合同订单管理
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
合同订单管理功能展示
- 订单管理
销售点击左侧导航栏中的【订单】按钮，进入合同订单管理页面，销售可以在这里查看自己签约的订单。
[图片: - 订单管理]
点击订单列表中对应学员项最后的【订单详情】可以查看订单的信息，添加学员的支付信息和订单变更记录。添加支付信息学员会同步到有审批权限的销售账号中，进行订单的审批。
[图片: - 订单管理]
点击【电子合同】即可根据选择的电子合同模版自动生成电子合同，销售可将电子合同链接发送给家⻓/学生进行签约。
[图片: - 订单管理]
点击【退费】可以发起学员订单的退费申请。
[图片: - 订单管理]
- 退费管理
在合同订单管理页面，点击上方【退费管理】选项，发起的订单退费申请会在这里同步，可以点击【详情】查看学员退费的订单信息，退费金额，类型及方式；提交的退费申请需要通过审批，通过审批后可以点击【确认退费】完成退费。
[图片: - 退费管理]

图片说明：- 订单管理
图片说明：- 订单管理
图片说明：- 订单管理
图片说明：- 订单管理
图片说明：- 退费管理
```

### chunk_c0d175a00838b7e7ec5f92788d09b58d | 学生添加生词后如何查看

- source_id：helpcenter:183
- document_id：doc_helpcenter_183
- 分类：热门文章
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-08T15:53:03
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061438514331639879488860998", "alt_text": "添加生词", "ocr_text": null, "caption": "添加生词"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061439016260395606474639353", "alt_text": "查看生词本", "ocr_text": null, "caption": "查看生词本"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061439132722198958260000374", "alt_text": "查看生词本", "ocr_text": null, "caption": "查看生词本"}]

```text
学生添加生词后如何查看
学生添加生词后如何查看
学生在练习过程中遇到新单词，加入生词本后应该如何查看？
添加生词
学生在答题解析页面可以点击单词查看释义，可以点击加入生词本
[图片: 添加生词]
查看生词本
学生在导航栏点击【错题】，在词汇分析处点击【查看详情】
[图片: 查看生词本]
学生可以点击生词本，查看已加入的生词，可以进行练习也可以导出
[图片: 查看生词本]

图片说明：添加生词
图片说明：查看生词本
图片说明：查看生词本
```

### chunk_e06984987bf70ed686f8bd62be57b84a | 一文了解：如何使用审批功能

- source_id：helpcenter:113
- document_id：doc_helpcenter_113
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:41:53
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051510267692223924834011631", "alt_text": "审批功能展示", "ocr_text": null, "caption": "审批功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030515110835628930151435658", "alt_text": "审批功能展示", "ocr_text": null, "caption": "审批功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051511253463926044598384605", "alt_text": "审批功能展示", "ocr_text": null, "caption": "审批功能展示"}]

```text
一文了解：如何使用审批功能
一文了解：如何使用审批功能
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
审批功能展示
具有审批权限的销售可以点击左侧导航栏中的【审批】按钮，进入订单审批页面，这里会显示销售的签约订单，可以对订单的支付信息等进行审核确认，点击【非正式学员】按钮可以直接将学员转为正式学员。
[图片: 审批功能展示]
点击【详情】的既可查看订单，对不合理的订单可以点击【回退】对该订单进行重新编辑处理。
[图片: 审批功能展示]
点击页面上方【退费审批】可以查看退费订单的审批列表，查看退费订单的信息，对退费订单进行 【通过】 或【驳回】的审批处理。
[图片: 审批功能展示]

图片说明：审批功能展示
图片说明：审批功能展示
图片说明：审批功能展示
```

### chunk_9c3aa85cda061ebcdb3124786b94f1da | 老师如何上传单词书

- source_id：helpcenter:188
- document_id：doc_helpcenter_188
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-18T17:11:17
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061436538976314477222815169", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061436588839375426972823806", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509081655457364851341602660751", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306143719601561861618872078", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061437228474414920645075570", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061437344236234971412834568", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061437412855856255705112363", "alt_text": "自定义单词书", "ocr_text": null, "caption": "自定义单词书"}]

```text
老师如何上传单词书
老师如何上传单词书
词汇教学是英语教学的重要组成部分，词汇的掌握和运用是增强语言知识和培养语言技能的基础。
老师可以一键导入生成单词书，帮助学生系统性学习单词
自定义单词书
老师可以根据自己的教学任务上传机构独有的单词书。
第1步，导航栏选择题库，点击单词书，点击新增词表，下载系统给出的模版Excel表格
[图片: 自定义单词书]
[图片: 自定义单词书]
第2步，按照模版格式编辑好表格内容
注：
1. 每个sheet是一个单元，每个单元最多300个单词。
2. 一个单词一行，包含单词、音标、解释、例句、例句翻译。
3. 单词例句和例句解释多条用空白换行隔开。
4. 音标、解释、例句、例句翻译，未填写系统将自动匹配。
5. 系统未匹配到相关单词信息内容，可以手动对单词进行编辑。
[图片: 自定义单词书]
第3步，点击上传表格即可一键快速生成单词书
上传好的单词书内容老师可以选择手动调整，可修改单词、音标、解析并添加例句。
[图片: 自定义单词书]
[图片: 自定义单词书]
修改完成后，点击输入单词本标题、并选择科目，确认即可生成单词书！
老师可根据科目、老师筛选，或者根据上传时间、单元数、单词数、使用次数及正确率进行排序筛选，也可以点击右侧一键搜索单词书，更便捷！
[图片: 自定义单词书]
[图片: 自定义单词书]

图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
图片说明：自定义单词书
```

### chunk_fc73e83d18de1e4d6a6f40455ceeaa5e | 一文了解：如何使用申请功能

- source_id：helpcenter:114
- document_id：doc_helpcenter_114
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:42:28
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305151214916316123846401569", "alt_text": "申请功能展示", "ocr_text": null, "caption": "申请功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051512458102478129953094487", "alt_text": "申请功能展示", "ocr_text": null, "caption": "申请功能展示"}]

```text
一文了解：如何使用申请功能
一文了解：如何使用申请功能
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
申请功能展示
销售可以点击左侧导航栏中的【申请】按钮，进入申请管理页面，销售可以在这里进行某个班级的排课申请，以及备注排课安排，教务老师可以同步查看。
[图片: 申请功能展示]
排课的相关处理进度可以在这里查看，可以筛选班级或者状态查看。
[图片: 申请功能展示]

图片说明：申请功能展示
图片说明：申请功能展示
```

### chunk_d8ac59a7ce487eb166ab8f1c8c3f5c94 | 老师如何布置单词书，查看单词书学习情况

- source_id：helpcenter:189
- document_id：doc_helpcenter_189
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-18T17:17:18
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061427523119664877715946035", "alt_text": "布置选项", "ocr_text": null, "caption": "布置选项"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061431002233421618779056118", "alt_text": "老师查看单词书学习情况", "ocr_text": null, "caption": "老师查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061430396817352650573173600", "alt_text": "老师查看单词书学习情况", "ocr_text": null, "caption": "老师查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061431323834445027722324208", "alt_text": "老师查看单词书学习情况", "ocr_text": null, "caption": "老师查看单词书学习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061431588361700683738570560", "alt_text": "老师查看单词书学习情况", "ocr_text": null, "caption": "老师查看单词书学习情况"}]

```text
老师如何布置单词书，查看单词书学习情况
老师如何布置单词书，查看单词书学习情况
布置单词书，可以帮助老师实时掌握学生单词学习的进度
布置选项
老师点击布置，可以自定义编辑词表名称和学习时间，多种单词测试形式可选择，可以设置该单元单词数量，还可以设置单词或测试是否限时
[图片: 布置选项]
老师查看单词书学习情况
点击单词书【详情】可查看总体参与学生人数、单词测试正确率、及完成率。
[图片: 老师查看单词书学习情况]
[图片: 老师查看单词书学习情况]
老师可以点击学生详情，查看学生每单元的具体测试详情，实时掌握班级学生的单词学习进度！
[图片: 老师查看单词书学习情况]
老师查看学生学习情况之后可以进行抽查。
点击展开列表-选中某一单元，可以点击抽查
抽查可以选择班级、学生、测试形式、抽查个数，还可以限制时间，开启实时作业。
[图片: 老师查看单词书学习情况]

图片说明：布置选项
图片说明：老师查看单词书学习情况
图片说明：老师查看单词书学习情况
图片说明：老师查看单词书学习情况
图片说明：老师查看单词书学习情况
```

### chunk_a04f85cd310e74bcc94cb42861955db5 | 一文了解：如何使用公池功能

- source_id：helpcenter:115
- document_id：doc_helpcenter_115
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:43:48
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051513308549476815594713129", "alt_text": "公池功能展示", "ocr_text": null, "caption": "公池功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051514065334183190934328621", "alt_text": "公池功能展示", "ocr_text": null, "caption": "公池功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051515113718415646413397014", "alt_text": "公池功能展示", "ocr_text": null, "caption": "公池功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051515158533574693661212197", "alt_text": "公池功能展示", "ocr_text": null, "caption": "公池功能展示"}]

```text
一文了解：如何使用公池功能
一文了解：如何使用公池功能
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
公池功能展示
销售可以点击左侧导航栏中的【公池】按钮，进入公共学员池页面，销售可以在这里看到所有的跟进学员信息，包括已分配和未分配的学员；包含学员的基本信息、跟进进度、沟通内容等；可以添加新的潜客信息（可批量导入或导出学员信息）对学员的信息进行修改或删除；也可以将已签约的学员转为正式学员。
[图片: 公池功能展示]
销售可以在公池进行学员信息的添加、修改和删除，可以对未分配销售跟进的学员进行分配。
[图片: 公池功能展示]
销售点击入学模考可以查看学生已作答的入学模考，未交卷的学生也可以点击生测试报告二维码一键交卷，加快跟进进度！
[图片: 公池功能展示]
[图片: 公池功能展示]

图片说明：公池功能展示
图片说明：公池功能展示
图片说明：公池功能展示
图片说明：公池功能展示
```

### chunk_dbf3e7c8702a91f23ce6602e1a1183a1 | 如何使用单词书学习词汇

- source_id：helpcenter:190
- document_id：doc_helpcenter_190
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-18T17:20:35
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061420415100386225979734935", "alt_text": "单词学习测试", "ocr_text": null, "caption": "单词学习测试"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061421063361555835897042004", "alt_text": "学生查看单词测试结果", "ocr_text": null, "caption": "学生查看单词测试结果"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061424225094807350424541430", "alt_text": "学生查看单词测试结果", "ocr_text": null, "caption": "学生查看单词测试结果"}]

```text
如何使用单词书学习词汇
如何使用单词书学习词汇
单词学生是学生巩固基础的必要环节，校校单词书帮助学生全面学习单词。
单词学习测试
学生点击单词书，可以查看到老师下发的单词书，进行单元测试，也可以登录小程序，随时随地学习单词！
[图片: 单词学习测试]
学生查看单词测试结果
学生可以查看单词测试结果，点击展开列表，即可查看单元测试结果
[图片: 学生查看单词测试结果]
若测试结果不满意，学生可以点击蓝色按钮，选择重新测试！
[图片: 学生查看单词测试结果]

图片说明：单词学习测试
图片说明：学生查看单词测试结果
图片说明：学生查看单词测试结果
```

### chunk_a20e78581bb6b2713b5facdfc6e66a09 | 一文读懂：如何进行渠道管理

- source_id：helpcenter:116
- document_id：doc_helpcenter_116
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:44:22
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051515542861086347092330550", "alt_text": "渠道功能展示", "ocr_text": null, "caption": "渠道功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051516158648467424848295607", "alt_text": "渠道功能展示", "ocr_text": null, "caption": "渠道功能展示"}]

```text
一文读懂：如何进行渠道管理
一文读懂：如何进行渠道管理
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
渠道功能展示
销售管理员可以点击左侧导航栏中的【渠道】按钮，进入渠道管理页面，进行潜客学员渠道来源的管理
[图片: 渠道功能展示]
销售可以点击添加，增加新的渠道类型，也可以对已有渠道进行编辑或删除的操作。
[图片: 渠道功能展示]

图片说明：渠道功能展示
图片说明：渠道功能展示
```

### chunk_5e4dee510b6a43477255264117428e79 | 如何操作订单退费/取消

- source_id：helpcenter:191
- document_id：doc_helpcenter_191
- 分类：热门文章
- 适用角色库：sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-19T17:13:59
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061411341703846530527999762", "alt_text": "未确认订单取消/退费流程", "ocr_text": null, "caption": "未确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061411593376319895389199068", "alt_text": "未确认订单取消/退费流程", "ocr_text": null, "caption": "未确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061412376072589351415333555", "alt_text": "未确认订单取消/退费流程", "ocr_text": null, "caption": "未确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061416459210501042904766402", "alt_text": "未确认订单取消/退费流程", "ocr_text": null, "caption": "未确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061417246389292353550038559", "alt_text": "已确认订单取消/退费流程", "ocr_text": null, "caption": "已确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061418015887912357209716820", "alt_text": "已确认订单取消/退费流程", "ocr_text": null, "caption": "已确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061418258160230308807004662", "alt_text": "已确认订单取消/退费流程", "ocr_text": null, "caption": "已确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061419006518393015948713563", "alt_text": "已确认订单取消/退费流程", "ocr_text": null, "caption": "已确认订单取消/退费流程"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061419343810196524224365095", "alt_text": "已确认订单取消/退费流程", "ocr_text": null, "caption": "已确认订单取消/退费流程"}]

```text
如何操作订单退费/取消
如何操作订单退费/取消
订单分为已确认订单，和未确认订单，订单录入错误可以取消订单。
未确认订单取消/退费流程
未确认订单可以点击退费，选择好退费金额、退费类型、退回课时，点击确认即可发起退费申请。
[图片: 未确认订单取消/退费流程]
在审批-退费审批中，可以筛选待审批订单，点击通过或驳回
[图片: 未确认订单取消/退费流程]
通过退费之后，在订单-退费管理处，找到订单，点击确认退费。
[图片: 未确认订单取消/退费流程]
确认退费之后，在订单-合同订单处点击订单详情，下拉选择删除订单，即可取消订单，重新录入
[图片: 未确认订单取消/退费流程]
已确认订单取消/退费流程
已确认订单可以点击退费，选择好退费金额、退费类型、退回课时，点击确认即可发起退费申请。
[图片: 已确认订单取消/退费流程]
在审批-退费审批中，可以筛选待审批订单，点击通过或驳回。
[图片: 已确认订单取消/退费流程]
通过退费之后，在订单-退费管理处，找到订单，点击确认退费。
[图片: 已确认订单取消/退费流程]
确认退费之后，在审批-订单审批处找到点击回退
[图片: 已确认订单取消/退费流程]
回退之后，在订单-合同订单处点击订单详情，下拉选择取消订单，即可取消订单，重新录入
[图片: 已确认订单取消/退费流程]

图片说明：未确认订单取消/退费流程
图片说明：未确认订单取消/退费流程
图片说明：未确认订单取消/退费流程
图片说明：未确认订单取消/退费流程
图片说明：已确认订单取消/退费流程
图片说明：已确认订单取消/退费流程
图片说明：已确认订单取消/退费流程
图片说明：已确认订单取消/退费流程
图片说明：已确认订单取消/退费流程
```

### chunk_9fb71e763af42dc1c4760b6bdf8fa04c | 一文了解：如何查看数据统计报告

- source_id：helpcenter:117
- document_id：doc_helpcenter_117
- 分类：核心功能介绍
- 适用角色库：student(学生库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:46:23
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051517347691012277175899391", "alt_text": "数据统计报告展示", "ocr_text": null, "caption": "数据统计报告展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051517545926082178690660350", "alt_text": "数据统计报告展示", "ocr_text": null, "caption": "数据统计报告展示"}]

```text
一文了解：如何查看数据统计报告
一文了解：如何查看数据统计报告
销售能否全面了解学生和家长的需求，及时发现潜在学员，生成课程相关建议这些都同机构的发展息息相关，是机构能否形成良好的口碑，提高机构知名度的关键所在。来看看系统能够为销售提供哪些帮助吧？
数据统计报告展示
销售可以点击左侧导航栏中的【数据】按钮，进入销售数据统计页面；
销售可以在这里查看自己及其下属的工作统计数据：
- 查看当天、近7天以及近30天的基础销售数据统计
- 查看销售顾问工作情况近期间的工作情况
 - 查看机构近期签约金额统计，即校区营收数据情况分析
[图片: 数据统计报告展示]
- 查看销售漏斗，获取销售的试听转化率，帮助销售分析自己的销售能力；清晰展示各个阶段销售跟进的潜客数
[图片: 数据统计报告展示]
帮助销售从多个维度的数据统计中进行汇总分析，制定更加精准的签约计划。

图片说明：数据统计报告展示
图片说明：数据统计报告展示
```

### chunk_09eb5aac89f584c9a6495c6b9e134fc1 | 电子合同签署流程

- source_id：helpcenter:194
- document_id：doc_helpcenter_194
- 分类：热门文章
- 适用角色库：student(学生库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-06-14T15:41:25
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061405468857266843030933120", "alt_text": "创建合同模板", "ocr_text": null, "caption": "创建合同模板"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306140725660508816904464821", "alt_text": "创建合同模板", "ocr_text": null, "caption": "创建合同模板"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061407282428360565363069844", "alt_text": "创建合同模板", "ocr_text": null, "caption": "创建合同模板"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061408132741858824160972194", "alt_text": "创建合同模板", "ocr_text": null, "caption": "创建合同模板"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061408479198233676170580577", "alt_text": "订单合同编辑", "ocr_text": null, "caption": "订单合同编辑"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061409093843827895211182307", "alt_text": "订单合同编辑", "ocr_text": null, "caption": "订单合同编辑"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061409451374430035809492244", "alt_text": "订单合同编辑", "ocr_text": null, "caption": "订单合同编辑"}]

```text
电子合同签署流程
电子合同签署流程
销售端订单创建后，如何完成线上合同签署？下文将介绍电子合同签署流程
创建合同模板
合同签署的第一步，需要先创建合同模板
校长和教务可以点击左侧导航栏【设置】按钮，找到【销售相关】，即可看到电子合同，点击添加可以进行合同的创建，合同模板必须拥有合同名称和公章
[图片: 创建合同模板]
[图片: 创建合同模板]
[图片: 创建合同模板]
校校提供相应的编辑工具，可以直接插入学生姓名，课程名称，课时数，优惠金额等变量，系统会自动根据学生信息填写，需要手动编辑的地方可以点击编辑工具栏上的[...]按钮，即可生成填空格。
可以直接复制PDF或者word版本的文件，但注意要使用格式刷将合同的格式统一，或者使用清除格式，再手动编辑。
[图片: 创建合同模板]
订单合同编辑
创建合同订单之后，销售可以订单处点击电子合同，选择合同模板。
[图片: 订单合同编辑]
点击预览调整好公章和签字区域的位置。
[图片: 订单合同编辑]
点击生成链接，可以发送链接和口令给学生家长签字。
[图片: 订单合同编辑]

图片说明：创建合同模板
图片说明：创建合同模板
图片说明：创建合同模板
图片说明：创建合同模板
图片说明：订单合同编辑
图片说明：订单合同编辑
图片说明：订单合同编辑
```

### chunk_ffa74e811fe7a02f90c1cb64231f9480 | 快速玩转销售端小程序

- source_id：helpcenter:118
- document_id：doc_helpcenter_118
- 分类：核心功能介绍
- 适用角色库：sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:55:04
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061435047610434989773819186", "alt_text": "销售登录小程序", "ocr_text": null, "caption": "销售登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111534571043113848254972120", "alt_text": "销售端小程序功能", "ocr_text": null, "caption": "销售端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111535193895128048233399358", "alt_text": "销售端小程序功能", "ocr_text": null, "caption": "销售端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111535268439012890225074926", "alt_text": "销售端小程序功能", "ocr_text": null, "caption": "销售端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111535372428764256297428595", "alt_text": "销售端小程序功能", "ocr_text": null, "caption": "销售端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111535441463796148191680106", "alt_text": "销售端小程序功能", "ocr_text": null, "caption": "销售端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509111535548185474791874758584", "alt_text": "销售端小程序功能", "ocr_text": null, "caption": "销售端小程序功能"}]

```text
快速玩转销售端小程序
快速玩转销售端小程序
销售老师如何更加便捷的查看销售数据和学员跟进情况？系统为销售老师提供小程序端服务，帮助销售老师更加及时的查看待办任务，随时随地查看学员的跟进状态和销售转化情况。
销售登录小程序
销售老师进入系统首页，点击右上角菜单栏【小程序】按钮，弹出小程序二维码，销售老师扫码即可登录销售端小程序。
[图片: 销售登录小程序]
销售端小程序功能
- 首页
销售老师登录小程序端，在首页可以查看目前销售老师所有跟进阶段的用户统计，查看今日销售老师的待处理任务以及销售的目标和目前的学员转化率等等。帮助销售老师快速了解课销情况。
[图片: 销售端小程序功能]
- 潜客
销售老师点击下方导航栏中的【潜客】选项即可看到自己目前所有的客户，可以筛选跟进进度查看，点击潜客详情可以查看基本信息、入学模考和沟通记录。
[图片: 销售端小程序功能]
[图片: 销售端小程序功能]
- 学员
[图片: 销售端小程序功能]
[图片: 销售端小程序功能]
销售老师点击下方导航栏中的【学员】选项即可查看目前已转正的所有学员，可以进行班级筛选。点击学生详情可以查看学生的基础信息、报名课程、信息来源、沟通记录，也可以进行续费操作。
- 数据报告
销售老师点击下方导航栏中的【数据报告】选项即可查看目前校区的销售数据统计情况，包含当日、当周、当月及当季的销售数据报告，还可以查看销售业绩、试听量排名；帮助销售老师更好的制定和修改销售计划。
[图片: 销售端小程序功能]

图片说明：销售登录小程序
图片说明：销售端小程序功能
图片说明：销售端小程序功能
图片说明：销售端小程序功能
图片说明：销售端小程序功能
图片说明：销售端小程序功能
图片说明：销售端小程序功能
```

### chunk_386620f0d5f1ed68852eeaa3f955aa7f | 学生做作业时，如何处理口语录音未检测到录音的情况？

- source_id：helpcenter:195
- document_id：doc_helpcenter_195
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-06-14T15:52:13
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202306141547447214915823836568651", "alt_text": "麦克风声音小", "ocr_text": null, "caption": "麦克风声音小"}]

```text
学生做作业时，如何处理口语录音未检测到录音的情况？
学生做作业时，如何处理口语录音未检测到录音的情况？
当学生完成口语作业时，发现口语录音未检测到录音现象，可通过以下文档排查。
浏览器使用不正确
当学生未使用正确浏览器时，可能会出现兼容性问题或者不稳定的情况
【解决方法】：
确认一下学生是否使用的正确的浏览器，建议【电脑使用谷歌浏览器，iPad使用safari浏览器】
麦克风声音小
学生可以回听一下录音是否有声音，如果有，但是比较小的话可能与录音设备的输入音量大小有关（系统此提示是录音的音量过小）如果学生听自己的录音较小但清晰的话，可以忽略此提示
windows系统设置麦克风音量的操作过程：
[图片: 麦克风声音小]
MAC系统上，设置麦克风音量的操作过程：
打开苹果上的电脑的设置，在系统偏好设置里打开【声音】，点击的声音的【输入】
点击【内建麦克风】左右拖动调整输入音量，往右边输入音量越大，往左边输入音量越小，根据实际选择输入的音量

图片说明：麦克风声音小
```

### chunk_64b297271dbb83a6a15eb4246e68716b | 一文了解：如何使用首页功能

- source_id：helpcenter:119
- document_id：doc_helpcenter_119
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:59:33
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051521073690193415923259495", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051521371396146556225330451", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051522304141078803666529759", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051522531161082600907544569", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}]

```text
一文了解：如何使用首页功能
一文了解：如何使用首页功能
校校学生端可以为学生提供作业完成、课程学习、单词书练习等功能，助力学生高效学习！
首页功能展示
学生登录系统，在系统首页上方学生看到自己在班级中的模考分数、练习时长、完成作业数、作业完成率和错题统计、词汇量等数据，帮助学生快速了解自己的学习情况。
[图片: 首页功能展示]
学生可以进行词汇量测试，通过阅读和听力词汇测试，测算出学生目前的词汇量水平，可以查看报告。
[图片: 首页功能展示]
首页下方，系统会按日期对学生所在班级的作业、课程和任务进行展示，便于学生查看自己的待处理的作业、任务以及课程安排。
[图片: 首页功能展示]
学生可以点击【作业&任务表格】旁边的【黑板报】查看老师在黑板报中发布的作业或者通知，避免学生错过教学任务。
[图片: 首页功能展示]

图片说明：首页功能展示
图片说明：首页功能展示
图片说明：首页功能展示
图片说明：首页功能展示
```

### chunk_09ceeae30bb5a838ae3f6736d610cdac | 一文了解学生如何转班

- source_id：helpcenter:198
- document_id：doc_helpcenter_198
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-07-06T13:46:28
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061403571630648200110875073", "alt_text": "如何操作转班", "ocr_text": null, "caption": "如何操作转班"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061404136885963861024994431", "alt_text": "如何操作转班", "ocr_text": null, "caption": "如何操作转班"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030614043768545367780785119", "alt_text": "如何操作转班", "ocr_text": null, "caption": "如何操作转班"}]

```text
一文了解学生如何转班
一文了解学生如何转班
学生完成课程学习后需要转入下个班级或者课程中需要更换班级应该如何操作？校校提供一键转班操作！
如何操作转班
教务、校长可以在班级管理页面找到需要转班的学生所在的班级，点击学生人数或班级学生，点击转班
[图片: 如何操作转班]
可以选择学生需要转入的班级，通过课程和班级名称筛选，选择勾选后，即可完成转班
[图片: 如何操作转班]
如果将学生移除了班级，学生将无法再看到之前班级的作业和课程
[图片: 如何操作转班]

图片说明：如何操作转班
图片说明：如何操作转班
图片说明：如何操作转班
```

### chunk_097e2f75eb01b98f9f06f10a353ca6c1 | 一文了解：如何使用作业功能

- source_id：helpcenter:120
- document_id：doc_helpcenter_120
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:00:46
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051523324487008618970395645", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051523574802689867013730211", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051524261855313480782549515", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}]

```text
一文了解：如何使用作业功能
一文了解：如何使用作业功能
机构除了要重视教学环节以外，也要重视学生课后的体验。课后的服务无论是对机构招生，口碑还是机构的发展都有着十分重要的作用。那么系统学生端能够为学生带来哪些服务体验呢？
作业功能展示
学生点击右侧导航栏中的【作业】选项进入作业页面；在作业页面，系统会根据作业的状态进行分类，学生可以根据作业状态了解作业的完成进度；
[图片: 作业功能展示]
学生还可以根据所在班级和作业的类型（包含单词作业、模考作业、打卡作业和课件作业等）搜索自己的作业；
[图片: 作业功能展示]
找到作业，点击右下方【进入作业】即可开始完成作业或查看作业的结果报告。
[图片: 作业功能展示]

图片说明：作业功能展示
图片说明：作业功能展示
图片说明：作业功能展示
```

### chunk_543c04d4147446ce782fa53d4fb0a583 | 学生模考时出现内存不足的提示，如何解决

- source_id：helpcenter:199
- document_id：doc_helpcenter_199
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-07-27T18:15:43
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202307271815381165064482467789457", "alt_text": "浏览器相关排查", "ocr_text": null, "caption": "浏览器相关排查"}]

```text
学生模考时出现内存不足的提示，如何解决
学生模考时出现内存不足的提示，如何解决
如果出现内存不足的提示，可以按以下方式排查：
浏览器相关排查
1：检查下浏览器是否是最新版本，是否有打开多个网页
可以关闭其他网页，更新下浏览器版本
2：关闭谷歌浏览器，再重新打开进入系统，看是否能正常答题
3：如果关闭浏览器重新进入，还是显示内存不足，就需要清理一下缓存
清理浏览器缓存，步骤如下： 
1：打开浏览器设置，选择隐私设置和安全性 
2：选择清除浏览数据，将时间范围选为不限
3：清理缓存后重新登陆系统
[图片: 浏览器相关排查]

图片说明：浏览器相关排查
```

### chunk_d966a0efdb54250b4ffc0913ffddc8d6 | 一文了解：如何使用课表功能

- source_id：helpcenter:122
- document_id：doc_helpcenter_122
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:02:23
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051538271661733242262825388", "alt_text": "课表功能展示", "ocr_text": null, "caption": "课表功能展示"}]

```text
一文了解：如何使用课表功能
一文了解：如何使用课表功能
机构除了要重视教学环节以外，也要重视学生课后的体验。课后的服务无论是对机构招生，口碑还是机构的发展都有着十分重要的作用。那么系统学生端能够为学生带来哪些服务体验呢？
课表功能展示
学生点击右侧导航栏中的【课表】选项进入课表管理训练页面；在这里学生可以查阅自己的课表，即学生的课程安排，将鼠标悬浮在课程上方即可看到课程详情：上课时间、上课内容、上课时长、上课老师以及上课方式等。
[图片: 课表功能展示]

图片说明：课表功能展示
```

### chunk_f156d87e1c26da4c9442efc1f5b85b41 | 数据统计——学生老师分析字段说明

- source_id：helpcenter:242
- document_id：doc_helpcenter_242
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2025-11-11T14:17:04
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306140113909471508037368158", "alt_text": "学生分析", "ocr_text": null, "caption": "学生分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061402163953851011480000402", "alt_text": "老师分析", "ocr_text": null, "caption": "老师分析"}]

```text
数据统计——学生老师分析字段说明
数据统计——学生老师分析字段说明
校校系统通过“学生分析”和“老师分析”两大模块，从分数、课程、作业、词汇等维度对教学全过程进行量化评估。学生分析帮助机构了解个体学习进度、学习行为与提分效果；老师分析则用于评估教学执行质量、反馈及时性和作业管理情况。二者结合可实现精准教学与过程优化，解决以往“数据分散、难以评估成效”的问题，为教学决策提供科学依据。
学生分析
1.入学分数：取值顺序为“学生学习目标中的入学分数 --> 潜客入学模考的分数 --> 首次模考作业的分数”，第一位有值就取第一位的值，没有值就会取后一位的值，以此类推
2.模考分数：学生所有已完成模考作业的平均数，公式：(模考作业A分数+模考作业B分数+....)/模考作业总数
3.实考分数：考试记录中最后一次录入的考试成绩
4.分数提升：（模考平均分 - 入学分数）或者（最近手动添加考试分数 - 入学分数）
5.提分率：分数提升/入学分数
6.已上课时：学生所有已上课时总数
7.剩余课时： 学生报名课时（未报名的就是班级总课时数）- 学生已上课课时
8.反馈次数：时间范围内，该学生所有班级所有老师添加反馈的总数
9.回访次数：老师给学生添加的回访总次数
10.作业完成率：时间范围内，学生所做作业的平均完成率，公式：（作业A的完成率+作业B的完成率+...)/作业总数
11.作业正确率：时间范围内，学生所做作业的平均正确率，公式：（作业A的正确率+作业B的正确率+...)/作业总数
12.作业数：时间范围内，学生收到布置作业的数量
13.完成作业数：时间范围内，学生完成的作业数量
14.开放题库练习数：时间范围内，学生所有已完成的开放题库数量
15.最近一次完成作业时间：学生最后一次提交作业的时间
16.日均练习时长(分钟)：学生总的做作业时长 / 学生有做作业的总天数

图片说明：学生分析
图片说明：老师分析
```

### chunk_048f55cb20f0d3528e319eb5338426ab | 数据统计——学生老师分析字段说明

- source_id：helpcenter:242
- document_id：doc_helpcenter_242
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2025-11-11T14:17:04
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306140113909471508037368158", "alt_text": "学生分析", "ocr_text": null, "caption": "学生分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061402163953851011480000402", "alt_text": "老师分析", "ocr_text": null, "caption": "老师分析"}]

```text
17.听力词汇量：学生最新词汇量测试结果中听力词汇量的值
18.阅读词汇量：学生最新词汇量测试结果中阅读词汇量的值
19.词汇测试正确率：时间范围内，学生所有单词作业和单词书作业的平均正确率，公式：（单词作业A正确率+单词作业B正确率+...+单词书作业A 正确率+单词书作业B正确率+...)/单词作业总数+单词书作业总数
20.词汇测试数量：时间范围内，学生所有单词作业和单词书作业总共测试的单词数量，公式：（单词作业A测试数+单词作业B测试数+...+单词书作业A测试数+单词书作业B测试数+...）
[图片: 学生分析]
老师分析
1.提分率： ( 模考平均分or最近手动添加考试分数 - 入学分数) / 入学分数 ， 所有学生的提分率加起来除以学生数
2.实考平均分：时间范围内最近一次，老师所授科目下所有学生的平均实考分(手动录入的考试分)，公式：(学生A实考分+学生B实考分+...)/学生人数
3.模考平均分：时间范围内，该老师所授班级下所有学生的模考平均模考分，公式：(学生A平均模考分+学生B学生模考分+...)/学生人数
4.在授学生数：老师在授班级中，在读学生人数
5.累计学生数：老师所授科目下累计教授的学生总人数
6.授课课时数：时间范围内，老师已经授课的总课时数
7.总授课课时：老师累计授课的总课时数
8.反馈数：时间范围内，老师填写反馈的次数
9.未反馈数：时间范围内，已上完的课，未填写反馈的次数
10.反馈效率：时间范围内，所有已结束的课程，在多长时间内进行填写反馈，公式：
 1）反馈时长（分钟） = 添加反馈时间 - 上课结束时间
 注：如果某节课老师未添加反馈则反馈时长默认为10081分钟（一周+1分钟，会被算作一周后）
 2）应反馈次数 = 课节A*上课学生数 + 课节B*上课学生数 + ...
 3）反馈平均时长 = sum(每节课每个学生反馈时长) / 应反馈次数
 4）最终通过平均反馈时长将反馈效率转换为：1小时内、6小时内、12小时内、24小时内、48小时内、一周以内、 一周后

图片说明：学生分析
图片说明：老师分析
```

### chunk_54fa655c84ef693159182397444f00b6 | 数据统计——学生老师分析字段说明

- source_id：helpcenter:242
- document_id：doc_helpcenter_242
- 分类：热门文章
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：2
- 状态：active
- 更新时间：2025-11-11T14:17:04
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260306140113909471508037368158", "alt_text": "学生分析", "ocr_text": null, "caption": "学生分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061402163953851011480000402", "alt_text": "老师分析", "ocr_text": null, "caption": "老师分析"}]

```text
11.平均作业完成率：时间范围内，该老师布置的所有作业，所有学生完成率的平均数，公式：(学生A作业完成率+学生B作业完成率+...)/学生人数
12.布置作业数：时间范围内，布置的作业数量
13.平均班级作业数：时间范围内，该老师所授班级布置作业的平均数，公式：(班级A布置作业数+班级B布置作业数+...)/班级数
14.查阅作业数：时间范围内，该老师查阅作业的数据
15.批改作业数：时间范围内，批改的作业数量
16.查阅率：对于老师自己布置的且学生完成了的作业，查阅的比例， 公式：已查阅的作业数量 / 已完成的作业数量 
17.查阅效率：时间范围内，学生所有已完成的作业，在多长时间内进行查阅，公式：平均查阅时间 = 每个作业完成时间到查阅时间的时间差之和 / 完成的作业数， 通过平均查阅时长换算成 1小时内、6小时内、12小时内、24小时内、48小时内、一周以内、 一周后
18.批改效率：时间范围内，学生所有已完成的作业，在多长时间内进行批改，公式：平均批改时间 = 每个作业完成时间到批改时间的时间差之和 / 完成的作业数， 通过平均批改时长换算成 1小时内、6小时内、12小时内、24小时内、48小时内、一周以内、 一周后
19.课后未布置作业班级数：上过课的班级其中未布置作业的班级数量
20.未布置作业班级数：时间范围内，老师布置作业数为0的班级数
21.最近一次布置作业：老师最后一次提交布置作业的时间
22.题目讲解数：老师总共进行题目讲解的数量
[图片: 老师分析]

图片说明：学生分析
图片说明：老师分析
```

### chunk_d928b172cd39d0a64cb36eefda262662 | 一文了解：如何使用题库功能

- source_id：helpcenter:234
- document_id：doc_helpcenter_234
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2025-09-08T16:33:37
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051540287509535584948531178", "alt_text": "题库功能展示", "ocr_text": null, "caption": "题库功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051541371893442299427393366", "alt_text": "题库功能展示", "ocr_text": null, "caption": "题库功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509081633145261182271036792009", "alt_text": "题库功能展示", "ocr_text": null, "caption": "题库功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051542021163744034282857093", "alt_text": "题库功能展示", "ocr_text": null, "caption": "题库功能展示"}]

```text
一文了解：如何使用题库功能
一文了解：如何使用题库功能
校校学生端可以为学生提供作业完成、课程学习、单词书练习等功能，助力学生高效学习！
题库功能展示
学生点击题库，可以看到老师已经开放的各科目题目，可以进行科目、类别、来源的筛选，也可以搜索题目，方便快速查找题目。
[图片: 题库功能展示]
学生可以选择模考模式或者学练模式答题，模考模式和实际考试一致，学练模式学生可以使用AI助教，实时讲解问题。
[图片: 题库功能展示]
[图片: 题库功能展示]
学生点击已完成题目，可以查看已经作答完成的题目，点击即可查看作答结果页详情。
[图片: 题库功能展示]

图片说明：题库功能展示
图片说明：题库功能展示
图片说明：题库功能展示
图片说明：题库功能展示
```

### chunk_7b6fa1cf67cfab74f18cd74a3465f044 | 学生添加生词后如何查看

- source_id：helpcenter:184
- document_id：doc_helpcenter_184
- 分类：核心功能介绍
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-05-08T15:54:56
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051543321841900757500999761", "alt_text": "添加生词", "ocr_text": null, "caption": "添加生词"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030515435455072484866227019", "alt_text": "查看生词本", "ocr_text": null, "caption": "查看生词本"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051544258375224129040894895", "alt_text": "查看生词本", "ocr_text": null, "caption": "查看生词本"}]

```text
学生添加生词后如何查看
学生添加生词后如何查看
学生在练习过程中遇到新单词，加入生词本后应该如何查看？
添加生词
添加生词学生在答题解析页面可以点击单词查看释义，可以点击加入生词本
[图片: 添加生词]
查看生词本
学生在导航栏点击【错题】，在词汇分析处点击【查看详情】
[图片: 查看生词本]
学生可以点击生词本，查看已加入的生词，可以进行练习也可以导出
[图片: 查看生词本]

图片说明：添加生词
图片说明：查看生词本
图片说明：查看生词本
```

### chunk_127a7858bc98a40181044afee999ff12 | 一文了解：如何使用单词书功能

- source_id：helpcenter:233
- document_id：doc_helpcenter_233
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2025-09-08T16:31:37
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051547198360389465025998102", "alt_text": "单词书功能展示", "ocr_text": null, "caption": "单词书功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051548322438064057118190816", "alt_text": "单词书功能展示", "ocr_text": null, "caption": "单词书功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051547441553890469722672731", "alt_text": "单词书功能展示", "ocr_text": null, "caption": "单词书功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305154839440004781272534838", "alt_text": "单词书功能展示", "ocr_text": null, "caption": "单词书功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051549117703174692702911674", "alt_text": "单词书功能展示", "ocr_text": null, "caption": "单词书功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051549253193580866936340506", "alt_text": "错词本功能展示", "ocr_text": null, "caption": "错词本功能展示"}]

```text
一文了解：如何使用单词书功能
一文了解：如何使用单词书功能
校校学生端可以为学生提供作业完成、课程学习、单词书练习等功能，助力学生高效学习！
单词书功能展示
学生点击单词书，即可查看老师下发的单词书。可以看到累计已学单词和错词。每本单词书可以查看正确率和完成度。
[图片: 单词书功能展示]
点击查看详情，可以查看每单元的单词。点击开始学习即可开始练习。
[图片: 单词书功能展示]
[图片: 单词书功能展示]
展开列表，学生可以查看每个单元单词数、正确率和学习状态，点击开始学习即可开始练习。
[图片: 单词书功能展示]
点击进小程序学习，扫小程序二维码可以在小程序随时随地练习单词。
[图片: 单词书功能展示]
错词本功能展示
学生点击错词本，可以查看错词、生词的具体详情。可以秀安泽单词练习数量以及布置范围，进行再次测试。同时学生可以导出错词或者生词。
[图片: 错词本功能展示]

图片说明：单词书功能展示
图片说明：单词书功能展示
图片说明：单词书功能展示
图片说明：单词书功能展示
图片说明：单词书功能展示
图片说明：错词本功能展示
```

### chunk_1f9976b54c70714835cb800b2d3ffac7 | 一文了解：如何查看反馈

- source_id：helpcenter:123
- document_id：doc_helpcenter_123
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:02:56
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051556417686374788109487816", "alt_text": "反馈功能展示", "ocr_text": null, "caption": "反馈功能展示"}]

```text
一文了解：如何查看反馈
一文了解：如何查看反馈
校校学生端可以为学生提供作业完成、课程学习、单词书练习等功能，助力学生高效学习！
反馈功能展示
学生点击右侧导航栏中的【反馈】选项进入课表管理训练页面；在这里学生查看老师给予的课堂反馈，查阅老师对学生的课堂相关项的评分以及老师给学生的学习建议；帮助学生更好的把握自己的优势和缺点。
[图片: 反馈功能展示]

图片说明：反馈功能展示
```

### chunk_de4425a079c4a154f45b16ca9e405051 | 一文读懂：如何进行自适应训练

- source_id：helpcenter:121
- document_id：doc_helpcenter_121
- 分类：核心功能介绍
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:01:49
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559077765681151040838052", "alt_text": "自适应训练功能展示", "ocr_text": null, "caption": "自适应训练功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559116300983569051175709", "alt_text": "自适应训练功能展示", "ocr_text": null, "caption": "自适应训练功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051559595895207623980116821", "alt_text": "自适应训练功能展示", "ocr_text": null, "caption": "自适应训练功能展示"}]

```text
一文读懂：如何进行自适应训练
一文读懂：如何进行自适应训练
机构除了要重视教学环节以外，也要重视学生课后的体验。课后的服务无论是对机构招生，口碑还是机构的发展都有着十分重要的作用。那么系统学生端能够为学生带来哪些服务体验呢？
首页
自适应训练功能展示
学生点击右侧导航栏中的【自适应】选项进入自适应训练页面；学生可以选择考试的科目（目前自适应训练仅支持雅思和托福两个科目）设定目标分数，然后进行摸底测试。
[图片: 自适应训练功能展示]
[图片: 自适应训练功能展示]
学生完成摸底测试后，系统会对学生相关能力进行评估，然后根据学生的能力提供学习计划，下发题目给学生练习，并且会记录学生训练情况，学生的能力评估会根据学生的自适应训练的进度更新。
[图片: 自适应训练功能展示]

图片说明：自适应训练功能展示
图片说明：自适应训练功能展示
图片说明：自适应训练功能展示
```

### chunk_a5773de1a7872a9bb57c93d57490deb9 | 一文读懂：如何使用笔记功能

- source_id：helpcenter:124
- document_id：doc_helpcenter_124
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:03:29
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051600423379208811223069327", "alt_text": "笔记功能展示", "ocr_text": null, "caption": "笔记功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051601055635521704635001061", "alt_text": "AI笔记分析", "ocr_text": null, "caption": "AI笔记分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509081603586979512449068448999", "alt_text": "笔记添加方式", "ocr_text": null, "caption": "笔记添加方式"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305160212670204567125895984", "alt_text": "笔记添加方式", "ocr_text": null, "caption": "笔记添加方式"}]

```text
一文读懂：如何使用笔记功能
一文读懂：如何使用笔记功能
校校学生端可以为学生提供作业完成、课程学习、单词书练习等功能，助力学生高效学习！
笔记功能展示
学生点击右侧导航栏中的【笔记】选项进入课表管理训练页面；在这里学生可以看到自己在作业里的笔记；笔记可以按类型，时间和笔记内容进行笔记的搜索。方便学生回顾自己练习中遇到的问题。
[图片: 笔记功能展示]
AI笔记分析
学生可以对笔记进行重点标记，点击AI笔记分析即可分析笔记，快速看懂——你的笔记到底有没有在帮你进步！
[图片: AI笔记分析]
笔记添加方式
学生在答题过程中可引用原文高亮。在阅读文章时，学生可以选中原文任意句子进行高亮，并添加批注或笔记，用以记录理解、做题依据或不懂的单词。
[图片: 笔记添加方式]
完成作业练习后，自主回顾题目思路。在完成一次完整的机考作业（如雅思阅读、托福听力）后，学生可前往“作业结果页”查看答案与讲解。选中题干或原文段落内容进行高亮，比如定位关键词、出题干扰信息，点击添加笔记，输入本题的解题逻辑与思考！
[图片: 笔记添加方式]

图片说明：笔记功能展示
图片说明：AI笔记分析
图片说明：笔记添加方式
图片说明：笔记添加方式
```

### chunk_9eecde9fcc62c1353ab47e5b404ab7bf | 一文了解：如何查看学习报告

- source_id：helpcenter:125
- document_id：doc_helpcenter_125
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:04:22
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051603425340838748212302438", "alt_text": "学习报告展示", "ocr_text": null, "caption": "学习报告展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051604449065401540192892321", "alt_text": "学习报告展示", "ocr_text": null, "caption": "学习报告展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/2026030516044841750719107337060", "alt_text": "学习报告展示", "ocr_text": null, "caption": "学习报告展示"}]

```text
一文了解：如何查看学习报告
一文了解：如何查看学习报告
校校学生端可以为学生提供作业完成、课程学习、单词书练习等功能，助力学生高效学习！
学习报告展示
学生点击右侧导航栏中的【学习报告】选项进入学习报告页面，可以查看到老师发布的学习报告，可以筛选科目、报告时间和生成老师。
[图片: 学习报告展示]
学生可以预览和分享学习报告，点击预览即可查看老师发布的学习报告内容！
[图片: 学习报告展示]
[图片: 学习报告展示]

图片说明：学习报告展示
图片说明：学习报告展示
图片说明：学习报告展示
```

### chunk_a0f9e7f0f03a12e1442fd16b4dbdd688 | 一文了解：如何使用错题功能

- source_id：helpcenter:126
- document_id：doc_helpcenter_126
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:04:53
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305160739506930271122070417", "alt_text": "错题功能展示", "ocr_text": null, "caption": "错题功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051608243452619971853408624", "alt_text": "错题功能展示", "ocr_text": null, "caption": "错题功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051608287794324820739075627", "alt_text": "错题功能展示", "ocr_text": null, "caption": "错题功能展示"}]

```text
一文了解：如何使用错题功能
一文了解：如何使用错题功能
机构除了要重视教学环节以外，也要重视学生课后的体验。课后的服务无论是对机构招生，口碑还是机构的发展都有着十分重要的作用。那么系统学生端能够为学生带来哪些服务体验呢？
错题功能展示
学生点击右侧导航栏中的【错题】选项进入错题页面；在这里学生可以查看自己在班级课程中的错题分析，系统会按照题型对学生的错题进行分类，统计学生练习题目数、错误次数及正确率；学生可以快速查看自己的错题和错误原因。
[图片: 错题功能展示]
查看错题详情可以进行练习。
[图片: 错题功能展示]
[图片: 错题功能展示]

图片说明：错题功能展示
图片说明：错题功能展示
图片说明：错题功能展示
```

### chunk_4e9ef97619d4e14b964eaf3493516b8c | 快速玩转学生端小程序

- source_id：helpcenter:128
- document_id：doc_helpcenter_128
- 分类：核心功能介绍
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:09:57
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051609234420605228517699450", "alt_text": "学生登录小程序", "ocr_text": null, "caption": "学生登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101701271996094520537593847", "alt_text": "课表查看", "ocr_text": null, "caption": "课表查看"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101701408905969722780187115", "alt_text": "课堂反馈查看", "ocr_text": null, "caption": "课堂反馈查看"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20250910170152779419982219167112", "alt_text": "完成作业", "ocr_text": null, "caption": "完成作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101702035930132555739827096", "alt_text": "单词书学习", "ocr_text": null, "caption": "单词书学习"}]

```text
快速玩转学生端小程序
快速玩转学生端小程序
学生如何快速完成作业，查看课表，课堂反馈和通知；系统为学生提供更加便捷的小程序端服务，助力学生更好的了解课程计划，完成学习任务。
学生登录小程序
学生进入系统首页，点击右上角菜单栏【小程序】按钮，弹出小程序二维码，学生扫码即可登录小程序。
[图片: 学生登录小程序]
学生端小程序功能
学生登录小程序，可以快速查看课表、课堂反馈以及老师发布的黑板报，同时学生也能通过小程序查看并完成除模考作业外的其他作业以及单词书学习。
课表查看
学生在小程序首页，点击上方菜单栏的【课表】按钮，可以根据日历查看对应日期的相关课程，包括课程名称、上课时间、上课地点、对应班级及考勤状态等。
[图片: 课表查看]
课堂反馈查看
学生在小程序首页，点击上方菜单栏的【反馈】按钮，可以查看老师给学生的课堂反馈，其中包含对学生课堂相关项的评分以及给学生的学生建议。
[图片: 课堂反馈查看]
完成作业
学生登录小程序，点击下方导航栏的【作业】按钮，即可在小程序端快速查看对应班级的作业以及作业的完成状态；对未完成的作业也可以在小程序端进行快捷的作答。
[图片: 完成作业]
单词书学习
学生点击单词书即可查看目前已经学习的单词数、错词数。点击单词书可以进行单元的测试练习
[图片: 单词书学习]

图片说明：学生登录小程序
图片说明：课表查看
图片说明：课堂反馈查看
图片说明：完成作业
图片说明：单词书学习
```

### chunk_8f850b6219e3b0cd8ae34c7450d434f0 | 快速玩转家长端小程序

- source_id：helpcenter:129
- document_id：doc_helpcenter_129
- 分类：核心功能介绍
- 适用角色库：student(学生库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:14:32
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051611005156224007682647790", "alt_text": "家长登录小程序", "ocr_text": null, "caption": "家长登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101706018272859138294860511", "alt_text": "首页", "ocr_text": null, "caption": "首页"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101706133875285167691722423", "alt_text": "首页", "ocr_text": null, "caption": "首页"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20250910170625949725680108483798", "alt_text": "作业", "ocr_text": null, "caption": "作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101706337700212153997603102", "alt_text": "单词书", "ocr_text": null, "caption": "单词书"}]

```text
快速玩转家长端小程序
快速玩转家长端小程序
家长和孩子的学习成长密不可分，那家长该如何参与孩子的课程学习呢？系统为家长提供小程序端服务，帮助家长了解孩子的学习动态和学习状况；更好的提升家校链接。
家长登录小程序
家长登录系统，系统会弹出小程序和公众号的二维码（目前家长端暂不支持电脑端），家长扫码左侧的小程序二维码即可登录小程序。
[图片: 家长登录小程序]
家长端小程序功能
首页
家长登陆系统小程序，进入小程序首页家长可以在首页上方看到学员目前的学习数据，包含学员当天的作业数、剩余的课时以及学员作业的完成率；快速掌握学员的学习进度。
- 课表查看
家长点击学习数据下方菜单栏的【课表】选项，可以按日期查看学员的课表，包含学员上课的时间、上课内容和上课地点（方式）；家长也能提醒学员，避免错过课程。
[图片: 首页]
- 课堂反馈
家长点击学习数据下方菜单栏的【反馈】选项，在这里家长可以查看老师给学生的课堂表现的打分和建议；帮助家长了解学员在课上的学习状态，也能了解学员目前的优缺点，协助学员提升自我。
[图片: 首页]
作业
家长点击下方导航栏中的【作业】选项进入学生的作业管理页面，在这里家长可以查看学生待完成和已完成的作业，根据学员的班级和作业处理状态搜索学员的作业；帮助家长监管学员的学习。
[图片: 作业]
单词书
家长点击下方导航栏中的【单词书】选项进入学生的单词书管理页面，在这里家长可以查看学生的单词学习情况，以及错词情况，学习进度一目了然！
[图片: 单词书]

图片说明：家长登录小程序
图片说明：首页
图片说明：首页
图片说明：作业
图片说明：单词书
```

### chunk_3131659d97d801dce2cd5c3f7d652990 | 快速玩转校长端小程序

- source_id：helpcenter:98
- document_id：doc_helpcenter_98
- 分类：核心功能介绍
- 适用角色库：principal(校长库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:00:13
- 图片数：14
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603061435167526761182348608139", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121750492134133711662074235", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121752058033743782666094459", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121752331436385474080932570", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121753451100572475629216625", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121755537137415052467947207", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121753593759453099374501001", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121757291132000391418922402", "alt_text": "小程序数据报告", "ocr_text": null, "caption": "小程序数据报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121759019125670310701908115", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230412175915974870399930269239", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121759476420156922091608875", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121800026729306699692349597", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121759294647346474749703074", "alt_text": "待办通知", "ocr_text": null, "caption": "待办通知"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202509101718227450150783506663879", "alt_text": "查看校币记录", "ocr_text": null, "caption": "查看校币记录"}]

```text
快速玩转校长端小程序
快速玩转校长端小程序
校长端小程序助力校区运营管理全掌握，数据查看更方便。
小程序数据报告
校长在电脑上登陆系统之后，可以在右上角点击小程序按钮，使用微信扫码登陆小程序。
[图片: 小程序数据报告]
登陆小程序首页可以查看销售数据报告，教学数据报告和运营数报告。
[图片: 小程序数据报告]
【销售数据报告】
分时段销售数据汇总分析，可以查看日/周/月/季度数据。
一键查看销售业绩，试听量排名。
[图片: 小程序数据报告]
[图片: 小程序数据报告]
[图片: 小程序数据报告]
【教学数据报告】
校长可以分科目查看授课课时、作业完成率、作业正确率、课堂反馈等教学数据汇总分析。
可以查看学生作业完成率、正确率、模考分数排名，实时检验教学成效。
[图片: 小程序数据报告]
[图片: 小程序数据报告]
【运营数据报告】
运营数据报告，包含学员状态、课消、课时、现金流等数据实时汇总更新，随时随地管理校区。
[图片: 小程序数据报告]
待办通知
每天系统会自动发送日报，已逾期的也可以进行查看。
校长收会收到校区运营报告，包括教学情况（学生作业完成情况、待批改作业、教学反馈），运营情况（今日课程明细），销售情况 （新增客户、潜客名单）
[图片: 待办通知]
[图片: 待办通知]
[图片: 待办通知]
[图片: 待办通知]
[图片: 待办通知]
查看校币记录
点击我的，即可看到校币剩余情况，点击查看详情即可查看校币的具体消耗。
[图片: 查看校币记录]

图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：小程序数据报告
图片说明：待办通知
图片说明：待办通知
图片说明：待办通知
图片说明：待办通知
图片说明：待办通知
图片说明：查看校币记录
```

### chunk_b799506d64ec0b31049a74a9fdaf8177 | 一文读懂：如何使用首页功能

- source_id：helpcenter:130
- document_id：doc_helpcenter_130
- 分类：核心功能介绍
- 适用角色库：principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:15:48
- 图片数：1
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051623554223898779028114620", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}]

```text
一文读懂：如何使用首页功能
一文读懂：如何使用首页功能
校长端默认拥有教务和财务的所有权限，带动校区整体运营
首页功能展示
浏览器建议： 电脑端 ( Mac&Windows)使用Google Chrome浏览器
iPad 请使用Safari浏览器
首页显示了机构的⼀些基本运营数据汇总；可以在销售目标处设置本周、本月、 季度 、年度销售目标和本周、本月、 季度 、年度试听目标；可以进行订单审批、退费审批
[图片: 首页功能展示]

图片说明：首页功能展示
```

### chunk_e6e049c170188a06b2aaa595d3f89218 | 一文读懂：如何进行员工管理

- source_id：helpcenter:131
- document_id：doc_helpcenter_131
- 分类：核心功能介绍
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:19:55
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051624434512784971029097981", "alt_text": "员工管理", "ocr_text": null, "caption": "员工管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051625449159963162327823621", "alt_text": "员工管理", "ocr_text": null, "caption": "员工管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051625567825903083999265041", "alt_text": "员工管理", "ocr_text": null, "caption": "员工管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305162616309477624080562135", "alt_text": "员工管理", "ocr_text": null, "caption": "员工管理"}]

```text
一文读懂：如何进行员工管理
一文读懂：如何进行员工管理
校长可以创建员工账号，分配不同的操作权限。
员工管理
创建员工账号时需要按要求填写员工姓名手机号基础信息，登录密码可以设置为任意密码， 不输入则默认为手机号后六位。
填写完信息后可以勾选对应角色及权限设置， ⼀个账号可以同时勾选多个角色身份 ， 但权限冲突的角色（如：销售管理员和销售、校长和教务、老师和助教）不可同时勾选。
[图片: 员工管理]
账号“停用”功能， 用于老师离职后的操作： 账号停用后将不可登录系统，但账号相关联数 据 ( 已上课程/已布置作业等) 依然保留。
[图片: 员工管理]
可以操作给销售和老师添加下属，点击添加下属，选择好老师，点击箭头移动到左边，点击确定即可完成下属添加。
[图片: 员工管理]
[图片: 员工管理]

图片说明：员工管理
图片说明：员工管理
图片说明：员工管理
图片说明：员工管理
```

### chunk_8cb39562eae0df2a44be91a25f9ed06a | 一文读懂：如何进行学员管理

- source_id：helpcenter:132
- document_id：doc_helpcenter_132
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:24:17
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626481669360787648769722", "alt_text": "学员管理", "ocr_text": null, "caption": "学员管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163036922837145069514449", "alt_text": "学员管理", "ocr_text": null, "caption": "学员管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051631247895784575917955782", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051632111913642779232161605", "alt_text": "学习报告", "ocr_text": null, "caption": "学习报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051632292563638706185979318", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051633168739999758050028542", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051633326580665831673558020", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051634058306769721027733430", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051634203611211754034736897", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051634425400543269951777419", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051635008610492000935745970", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051635253681599673356143767", "alt_text": "课程反馈", "ocr_text": null, "caption": "课程反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163542696102019556255141", "alt_text": "合同", "ocr_text": null, "caption": "合同"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163556566149667891860884", "alt_text": "回访记录", "ocr_text": null, "caption": "回访记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051636118234894180181699570", "alt_text": "考试记录", "ocr_text": null, "caption": "考试记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051636329204317760906452497", "alt_text": "学生续期", "ocr_text": null, "caption": "学生续期"}]

```text
一文读懂：如何进行学员管理
一文读懂：如何进行学员管理
这里是管理正式学生的地方，可以添加学生账号或修改学生信息，也可以查看学生的学习数据。
学员管理
老师可以点击新增，添加学生或者直接导入名单。学生的信息有学生姓名、学生性别、学生登录手机号、学生登陆密码 (可不填，默认为手机 号后六位) 、学习目标 (可添加多个) ，可以填写家长手机号码。
[图片: 学员管理]
如果学生有报名课程，会显示在这里，也可以手动给学生添加报名课程以及支付信息。
添加报名课程时，如果学生报名的是⼀对⼀班级，系统会自动生成⼀个⼀对⼀班级在“班级管理”中。
[图片: 学员管理]
课表&任务
这里可以查看学生的课表和任务安排，点击导出清单可以选择时间，导出列表样式或者试图样式。
[图片: 课表&任务]
学习报告
学生在各个科目的表现都会展示在学习报告。可以查看学生的成绩、课程、作业、知识点等详情，也可以点生成一键生成学习报告。
[图片: 学习报告]
练习情况
可以查看学生的作业练习情况，包含老师的批改情况，点击详情即可查看作业结果报告。可以使用ai 数据分析，一键分析学生的作业完成情况。
[图片: 练习情况]
自适应统计可以查看学生自主练习的情况，从单词、阅读、听力、口语、写作等全方位记录学生的练习情况，点击查看详情可以查看具体的学习记录。
[图片: 练习情况]
点击单词书进度可查看学生的单词书学习情况，包括学习进度和完成率，点击详情查看具体的单词词汇。
[图片: 练习情况]
点击开放题库，可以查看老师开放给学生自主练习的题目作答情况，包括正确率、分数及批改老师，点击查看详情可查看作业练习结果报告。
[图片: 练习情况]
点击词汇量测试，可以查看学生当前的词汇量水平，对应的能力等级，点击详情查看具体的词汇量测试报告结果。
[图片: 练习情况]
点击错题分析，可查看学生词汇分析、基础训练分析、真题训练、机构题库等练习情况。
[图片: 练习情况]
点击笔记可查看学生在练习过程中添加的笔记，包括重点笔记、来源、作业名称、笔记类型，点击查看详情即可查看具体的题目内容。
[图片: 练习情况]
课程反馈

图片说明：学员管理
图片说明：学员管理
图片说明：课表&任务
图片说明：学习报告
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：课程反馈
图片说明：合同
图片说明：回访记录
图片说明：考试记录
图片说明：学生续期
```

### chunk_d6958fac328d542806929bd520311a88 | 一文读懂：如何进行学员管理

- source_id：helpcenter:132
- document_id：doc_helpcenter_132
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-12T19:24:17
- 图片数：16
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051626481669360787648769722", "alt_text": "学员管理", "ocr_text": null, "caption": "学员管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163036922837145069514449", "alt_text": "学员管理", "ocr_text": null, "caption": "学员管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051631247895784575917955782", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051632111913642779232161605", "alt_text": "学习报告", "ocr_text": null, "caption": "学习报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051632292563638706185979318", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051633168739999758050028542", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051633326580665831673558020", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051634058306769721027733430", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051634203611211754034736897", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051634425400543269951777419", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051635008610492000935745970", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051635253681599673356143767", "alt_text": "课程反馈", "ocr_text": null, "caption": "课程反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163542696102019556255141", "alt_text": "合同", "ocr_text": null, "caption": "合同"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163556566149667891860884", "alt_text": "回访记录", "ocr_text": null, "caption": "回访记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051636118234894180181699570", "alt_text": "考试记录", "ocr_text": null, "caption": "考试记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051636329204317760906452497", "alt_text": "学生续期", "ocr_text": null, "caption": "学生续期"}]

```text
课程反馈可以查看学生所在班级，老师发布的反馈，包括作业完成情况、课程要点、学习建议等。
[图片: 课程反馈]
合同
可以查看学生的签约课程以及合同，点击即可查看详情。
[图片: 合同]
回访记录
这里可以查看该学生的回访记录，也可以添加回访记录。
[图片: 回访记录]
考试记录
考试记录可以添加学生的考试信息，可以选择考试通知。
[图片: 考试记录]
学生续期
点击学生姓名旁边的小圆点，点击续期，即可操作账号续期。
[图片: 学生续期]

图片说明：学员管理
图片说明：学员管理
图片说明：课表&任务
图片说明：学习报告
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：课程反馈
图片说明：合同
图片说明：回访记录
图片说明：考试记录
图片说明：学生续期
```

### chunk_1e048e93ea4e36ef774da71d83420da6 | 一文读懂：如何进行课程管理

- source_id：helpcenter:133
- document_id：doc_helpcenter_133
- 分类：核心功能介绍
- 适用角色库：teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:29:01
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051637288076748720807397843", "alt_text": "课程管理", "ocr_text": null, "caption": "课程管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051637483880608464421067349", "alt_text": "课程管理", "ocr_text": null, "caption": "课程管理"}]

```text
一文读懂：如何进行课程管理
一文读懂：如何进行课程管理
校长可以在这里添加机构所开设的课程，可以在学杂处添加相应费用
课程管理
添加课程需要填写课程名称，课程类别，关联对应科目题库，可以设置上课内容，填写课程介绍。
课程类别： 即托福、雅思、ACT等。
上课内容： 即听力、阅读、口语等具体上课内容。
注：课程下有班级的课程，不允许删除。
[图片: 课程管理]
点击编辑，即可修改课程详情，包括名称、关联题库、课程类型、课程价格、课时、单价、上课内容及课程介绍等。
可以在学杂处添加相应费用，点击学杂管理、编辑名称，选择类型。点击编辑即可修改。
[图片: 课程管理]

图片说明：课程管理
图片说明：课程管理
```

### chunk_006d29d24a52d211799a6775cf5e81a3 | 一文读懂：如何进行班级管理

- source_id：helpcenter:134
- document_id：doc_helpcenter_134
- 分类：核心功能介绍
- 适用角色库：academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:35:09
- 图片数：8
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638114769167581697751070", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051638222679166526208946126", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305163943918262652815588031", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051639467932146854933115128", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051639594344295233799781205", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051640053854343529224985460", "alt_text": "创建班级", "ocr_text": null, "caption": "创建班级"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051640161721862384380289357", "alt_text": "班级内排课", "ocr_text": null, "caption": "班级内排课"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051640236328831071067045924", "alt_text": "班级内排课", "ocr_text": null, "caption": "班级内排课"}]

```text
一文读懂：如何进行班级管理
一文读懂：如何进行班级管理
校长可以创建班级、管理班级，添加班级学员和负责老师等，掌握班级所有开班教学信息。
创建班级
添加好课程后，可以在班级管理里创建班级
添加班级：班级信息包括所属课程、班级类型、班级名称、班级老师助教、开班日期、班级课时等
[图片: 创建班级]
[图片: 创建班级]
选择一对一班级需要手动填写班级名称，添加一对多班级系统会自动匹配学期和班级名称
[图片: 创建班级]
[图片: 创建班级]
班级里选择学生，点击添加，可以将相应学员添加至班级内。
[图片: 创建班级]
[图片: 创建班级]
班级内排课
班级创建好并完成分班后，可以给班级排课(需提前在员工管理中添加好老师，并且在创 建班级时选定老师)。
排课的方式有三种，智能排课、传统排课、常用时间段排课.
[图片: 班级内排课]
[图片: 班级内排课]

图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：创建班级
图片说明：班级内排课
图片说明：班级内排课
```

### chunk_7d896a81aa151f57db92354869adc606 | 一文读懂：如何进行课表管理

- source_id：helpcenter:135
- document_id：doc_helpcenter_135
- 分类：核心功能介绍
- 适用角色库：teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:37:25
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051647582864320885640914792", "alt_text": "课表管理", "ocr_text": null, "caption": "课表管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305164837587476131516751228", "alt_text": "课表管理", "ocr_text": null, "caption": "课表管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051648547257767230881015656", "alt_text": "课表管理", "ocr_text": null, "caption": "课表管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051649123346241020939409897", "alt_text": "课表管理", "ocr_text": null, "caption": "课表管理"}]

```text
一文读懂：如何进行课表管理
一文读懂：如何进行课表管理
所有班级已排的课表都会显示在课表页面，可以筛选数据，查看课程调整记录，新增排课或导出课表。
课表管理
机构班级已排的课表都会显示在这里，可以根据课程、班级、老师、助教、课程状态，时间等 多个维度筛选数据或导出课表
[图片: 课表管理]
老师点击记录即可查看该节课的排课记录以及变更记录。
[图片: 课表管理]
也可切换视图模式，以老师视图、班级视图、时间视图去查 看课表，视图模式也支持一键导出
[图片: 课表管理]
视图模式下老师点击空白部分即可新增排课。
[图片: 课表管理]

图片说明：课表管理
图片说明：课表管理
图片说明：课表管理
图片说明：课表管理
```

### chunk_6a938eda1d761cd7927262f353f8007d | 一文了解：如何使用考勤功能

- source_id：helpcenter:136
- document_id：doc_helpcenter_136
- 分类：核心功能介绍
- 适用角色库：student(学生库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:38:38
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051650378463712135058599019", "alt_text": "考勤管理", "ocr_text": null, "caption": "考勤管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051651195457598593752391004", "alt_text": "调课功能", "ocr_text": null, "caption": "调课功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051651247412417797254184243", "alt_text": "调课功能", "ocr_text": null, "caption": "调课功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051652016309764400428257582", "alt_text": "调课功能", "ocr_text": null, "caption": "调课功能"}]

```text
一文了解：如何使用考勤功能
一文了解：如何使用考勤功能
考勤页面可以查看、修改学生的课堂考勤情况，对请假学生进行调课操作，管理课堂考勤更轻松！
考勤管理
已过时间的课程默认为未出勤，计算课消。校长可以通过筛选上课时间，考勤状态，搜索班级或学生查看考勤记录，支持手动修改考勤。
[图片: 考勤管理]
调课功能
考勤状态为已请假的学生可以进行调课。
注：班课学生请假调课只能调到本班以外的班级，一对一班级可以不需要调课可以直接在班级重排。
[图片: 调课功能]
[图片: 调课功能]
调课后的班级课表出勤会显示有学生插课。
[图片: 调课功能]

图片说明：考勤管理
图片说明：调课功能
图片说明：调课功能
图片说明：调课功能
```

### chunk_b81dfe7fad4a8efe89f0e03bb9e6d596 | 一文了解：如何使用申请功能

- source_id：helpcenter:137
- document_id：doc_helpcenter_137
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:42:08
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305165400279837697958158364", "alt_text": "排课申请", "ocr_text": null, "caption": "排课申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051654213076150008791184726", "alt_text": "预占申请", "ocr_text": null, "caption": "预占申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051654384094333028100136743", "alt_text": "试听申请", "ocr_text": null, "caption": "试听申请"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051654463769133462894864239", "alt_text": "调课申请", "ocr_text": null, "caption": "调课申请"}]

```text
一文了解：如何使用申请功能
一文了解：如何使用申请功能
申请页面可以查看排课申请，预占请假，试听排课申请， 调课申请
排课申请
销售发起的排课申请，可以在这里查看，排课的备注信息会同步显示，方便老师合理安排课程。已排课的课程可以点击调整状为已处理。
[图片: 排课申请]
预占申请
校长可以在这里主动给老师添加预占或请假时间，添加之后本时间段不可排课，系统在排课时会自动避开该时间段，老师在自己端口请假的时间也会同步到该表格中。
可同时预占/请假多个老师的多个时间段。
[图片: 预占申请]
试听申请
销售人员通过销售端给客户预约试听课信息会显示在这里，校长可以点击排课设置试听课上课老师和时间等信息进行试听排课，也可点击“忽略”，将不需要排课的信息忽略掉。
[图片: 试听申请]
调课申请
老师或⼀对⼀班级的学生可以在自己端口“我的课表”中发起调课申请，申请调课信息会显示在调课申请这里，管理员或教务可以重新修改上课时间。
[图片: 调课申请]

图片说明：排课申请
图片说明：预占申请
图片说明：试听申请
图片说明：调课申请
```

### chunk_2bd3f2aaadd84d9a7cb0c026e7375c88 | 一文了解：如何使用公池功能

- source_id：helpcenter:138
- document_id：doc_helpcenter_138
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:44:22
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051655147876316186110735274", "alt_text": "线索管理", "ocr_text": null, "caption": "线索管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051655553540582020995057642", "alt_text": "潜客分配", "ocr_text": null, "caption": "潜客分配"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051656151467536012365791209", "alt_text": "潜客管理", "ocr_text": null, "caption": "潜客管理"}]

```text
一文了解：如何使用公池功能
一文了解：如何使用公池功能
公池是显示所有销售跟进的客户信息的客户池，可以查看潜客信息，进行潜客管理，包括名单导入导出、分配以及潜客转正。
线索管理
潜客支持名单批量导入，方便机构管理数据。公池会展示所有跟进进度下的客户信息，可以根据有效性、跟进进度、负责销售等信息进行潜筛选，查找数据。
[图片: 线索管理]
潜客分配
未分配的潜客，可以批量勾选潜客指定分配给某个销售进行跟进，可以查看潜客变更记录，线索跟进进度更透明。
[图片: 潜客分配]
潜客管理
可以查看潜客的入学模考，也可以直接转为正式学员。
[图片: 潜客管理]

图片说明：线索管理
图片说明：潜客分配
图片说明：潜客管理
```

### chunk_49a913aa737210f0ffe11d4a3cc3133a | 一文了解：如何使用订单功能

- source_id：helpcenter:139
- document_id：doc_helpcenter_139
- 分类：核心功能介绍
- 适用角色库：student(学生库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:49:42
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051657522386204822562966657", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051658157067721277529563879", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051658222937009199511089749", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051658314151257254288706894", "alt_text": "合同订单", "ocr_text": null, "caption": "合同订单"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051658552143474488352837469", "alt_text": "退费管理", "ocr_text": null, "caption": "退费管理"}]

```text
一文了解：如何使用订单功能
一文了解：如何使用订单功能
订单页面分为合同订单和退费管理，可以进行合同的查看和管理
合同订单
这里是所有的签约合同订单，可以查看合同详情、订单状态、⾦额、时间、实收⾦额、订单余额、课时余额等。
[图片: 合同订单]
点击订单详情，可查看学生报课的具体信息，包括课程信息和支付信息。
[图片: 合同订单]
点击退费，即可编辑退费信息，包括退费金额、退费类型、退回课时、退费方式等等。
[图片: 合同订单]
点击电子合同，即可查看合同细则，同时也可以更新合同模板内容。
[图片: 合同订单]
退费管理
销售发起的订单退费申请，都会同步在这里，拥有审批权限的员工可以通过或驳回退费申请， 
退费的类型包括课时费、资料费等；退费方式包括支付宝、微信、退到账户余额等。
[图片: 退费管理]

图片说明：合同订单
图片说明：合同订单
图片说明：合同订单
图片说明：合同订单
图片说明：退费管理
```

### chunk_95d9824dbb5a59fe6bc514458d504be4 | 一文了解：如何使用审批功能

- source_id：helpcenter:141
- document_id：doc_helpcenter_141
- 分类：核心功能介绍
- 适用角色库：student(学生库);principal(校长库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T19:54:44
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305170218431663197868999031", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305170300175762659606380037", "alt_text": "订单审批", "ocr_text": null, "caption": "订单审批"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051703155060069175612901380", "alt_text": "退费审批", "ocr_text": null, "caption": "退费审批"}]

```text
一文了解：如何使用审批功能
一文了解：如何使用审批功能
审批页面有订单审批和退费审批的功能
订单审批
待付款、待确认的订单会订单审批中显示，可以点击查看详情确认订单。已经确认的订单也可以点击回退回到待确认状态。
[图片: 订单审批]
已确认的订单，点击“非正式学员”，可以直接将客户转为正式学员。
[图片: 订单审批]
退费审批
校长可以在退费审批处通过或驳回退费申请
[图片: 退费审批]

图片说明：订单审批
图片说明：订单审批
图片说明：退费审批
```

### chunk_050b11fbb94f7ff6b29ad6e2c8a48614 | 一文了解：如何使用财务功能

- source_id：helpcenter:144
- document_id：doc_helpcenter_144
- 分类：核心功能介绍
- 适用角色库：principal(校长库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T20:01:03
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051706306035613526686710317", "alt_text": "财务管理", "ocr_text": null, "caption": "财务管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305170643753344293897241341", "alt_text": "财务管理", "ocr_text": null, "caption": "财务管理"}]

```text
一文了解：如何使用财务功能
一文了解：如何使用财务功能
财务收支明细都会统计在财务管理页面
财务管理
财务收支明细都会统计在这里，也可点击“新增”手动添加收支项目，清晰记录每⼀笔缴费情况，实时筛选数据查看，也可以导出数据。
[图片: 财务管理]
[图片: 财务管理]

图片说明：财务管理
图片说明：财务管理
```

### chunk_b3ce7e5e5386ba5b4244eecaff0a434c | 一文了解：如何查看数据分析

- source_id：helpcenter:145
- document_id：doc_helpcenter_145
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T20:07:02
- 图片数：10
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051707306154848220498672502", "alt_text": "销售数据统计", "ocr_text": null, "caption": "销售数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305170814490766855667305562", "alt_text": "运营数据统计", "ocr_text": null, "caption": "运营数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051708173226010331476810468", "alt_text": "运营数据统计", "ocr_text": null, "caption": "运营数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051708215536834565335546863", "alt_text": "运营数据统计", "ocr_text": null, "caption": "运营数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051717378042966751550861467", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051717484583216753202869275", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051724568232963042401169609", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051725198959486096351897173", "alt_text": "教学数据统计", "ocr_text": null, "caption": "教学数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051725467559419085131383721", "alt_text": "财务数据统计", "ocr_text": null, "caption": "财务数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051726195048322406068608155", "alt_text": "市场数据统计", "ocr_text": null, "caption": "市场数据统计"}]

```text
一文了解：如何查看数据分析
一文了解：如何查看数据分析
校长端统计分析部分分为销售、运营、教学、财务、市场数据统计五个部分，校区管理者可以查看校区关键数据，及时调整运营计划。
销售数据统计
1) 当日、近7天、近30天基础销售数据统计
2) 销售顾问工作情况：多维度销售数据统计
3) 签约⾦额： 校区营收数据分析
4) 销售漏斗 
销售及试听转化率走势图
顾问转化率数据及关单周期、销售能力、关单数据⼀目了然
销售漏斗清晰展示各跟进进度潜客数
[图片: 销售数据统计]
运营数据统计
在读学生人数趋势图、老师授课课时柱状图 (点击查看详情了解具体课时情况)、学生消课课时柱状图(点击查看详情了解具体课时情况)、老师带班人数柱状图和学生出勤率百分比趋势图等。
[图片: 运营数据统计]
[图片: 运营数据统计]
[图片: 运营数据统计]
教学数据统计
学生分析
1) 点击查看下详情，即可看到学生作业完成率、正确率、平均练习时长走势图，快速概览学生作业数据趋势；
2) 学生提分分析，以散点图形式，清晰罗列与学生相关各大元素与其提分走势的相关性，精准把握关键变量，提高学习效率；
3) 单个学生学习数据汇总，让过程与结果更明了，让决策更精准
[图片: 教学数据统计]
[图片: 教学数据统计]
老师分析
1) 老师平均提分率，作业查阅率，反馈效率数据统计
2) 老师工作数据统计，让教学过程更加透明，更高效
[图片: 教学数据统计]
[图片: 教学数据统计]
财务数据统计
财务统计包括现金流统计、消课和退费统计。
[图片: 财务数据统计]
市场数据统计
市场数据可以查看签约人数、金额。点击查看详情即可查看校区相关签约数据。
[图片: 市场数据统计]

图片说明：销售数据统计
图片说明：运营数据统计
图片说明：运营数据统计
图片说明：运营数据统计
图片说明：教学数据统计
图片说明：教学数据统计
图片说明：教学数据统计
图片说明：教学数据统计
图片说明：财务数据统计
图片说明：市场数据统计
```

### chunk_500e71e177f5f17d7de1a40ff2d9db63 | 一文了解：如何进行系统设置

- source_id：helpcenter:146
- document_id：doc_helpcenter_146
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T20:12:27
- 图片数：9
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051727495468755618606821777", "alt_text": "基本信息设置", "ocr_text": null, "caption": "基本信息设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051728373128082636235129106", "alt_text": "销售相关设置", "ocr_text": null, "caption": "销售相关设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051728404174455914946649206", "alt_text": "销售相关设置", "ocr_text": null, "caption": "销售相关设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051729422399744057358473036", "alt_text": "教学相关设置", "ocr_text": null, "caption": "教学相关设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305173014812517225504280993", "alt_text": "教学相关设置", "ocr_text": null, "caption": "教学相关设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051731204456959141712452469", "alt_text": "待办与通知设置", "ocr_text": null, "caption": "待办与通知设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051731258267697498294917434", "alt_text": "待办与通知设置", "ocr_text": null, "caption": "待办与通知设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051731288304075328353972619", "alt_text": "待办与通知设置", "ocr_text": null, "caption": "待办与通知设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051731328499636310699467060", "alt_text": "待办与通知设置", "ocr_text": null, "caption": "待办与通知设置"}]

```text
一文了解：如何进行系统设置
一文了解：如何进行系统设置
系统设置包括基本信息设置、销售相关设置、教学相关设置、待办与通知设置
基本信息设置
基本信息会显示账户余额、系统服务有效期、可添加学生数量、校币数量。机构可以自定义登录页的背景图、机构logo和网站图标。
[图片: 基本信息设置]
销售相关设置
销售相关设置可以设置订单相关内容，课时分钟数，潜客相关内容以及电子合同模版。支持创建多个电子合同模版。
[图片: 销售相关设置]
[图片: 销售相关设置]
教学相关设置
教学相关设置可以查看云盘容量；
设置老师是否可以请假；
模考成绩审核发布按钮(开启后学生模考结束，需老师点击发布成绩，学生才能看到自己的模考成绩)；
AI助教；校币充值按钮；智能批改写作按钮；
预设上课地点以及常用上课时间段以供排课的时候选择；
课堂反馈相关设置。
[图片: 教学相关设置]
[图片: 教学相关设置]
待办与通知设置
待办与通知设置，可以设置是否开启教学、课程、销售、教务等相关规则触发的通知。
[图片: 待办与通知设置]
[图片: 待办与通知设置]
[图片: 待办与通知设置]
[图片: 待办与通知设置]

图片说明：基本信息设置
图片说明：销售相关设置
图片说明：销售相关设置
图片说明：教学相关设置
图片说明：教学相关设置
图片说明：待办与通知设置
图片说明：待办与通知设置
图片说明：待办与通知设置
图片说明：待办与通知设置
```

### chunk_2bbc80f578c526c7cf99e7041c2cae6b | 快速玩转老师端小程序

- source_id：helpcenter:103
- document_id：doc_helpcenter_103
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-12T18:21:35
- 图片数：7
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051732599082342759028986675", "alt_text": "老师登录小程序", "ocr_text": null, "caption": "老师登录小程序"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121820058551739971391042381", "alt_text": "老师端小程序功能", "ocr_text": null, "caption": "老师端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230412182018398868507875906421", "alt_text": "老师端小程序功能", "ocr_text": null, "caption": "老师端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121820316238537878440462632", "alt_text": "老师端小程序功能", "ocr_text": null, "caption": "老师端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121820462848419792363716633", "alt_text": "老师端小程序功能", "ocr_text": null, "caption": "老师端小程序功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121821038875875035791308453", "alt_text": "班级管理", "ocr_text": null, "caption": "班级管理"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304121821327998770338735466454", "alt_text": "数据报告", "ocr_text": null, "caption": "数据报告"}]

```text
快速玩转老师端小程序
快速玩转老师端小程序
不用登录电脑端就能轻松完成教学任务？系统为老师们提供专门的小程序端服务，助力老师应对多种场景下的教学管理，提高教学效率。
老师登录小程序
老师进入系统首页，点击右上角菜单栏-小程序按钮，弹出小程序二维码，老师扫码即可登录小程序。
[图片: 老师登录小程序]
老师端小程序功能
工作台
老师登录小程序，在首页-工作台中，老师可以快速完成作业管理、课堂反馈、课表查看、黑板报发布等功能。
- 作业管理：在工作台上方菜单栏中点击【作业】按钮，可对班级作业进行筛选、查看作业的完成情况、提高作业管理效率。
[图片: 老师端小程序功能]
- 课堂反馈：在工作台上方菜单栏中点击【反馈】按钮，可对课堂反馈进行筛选，快捷添加课堂反馈。
[图片: 老师端小程序功能]
- 查看课表：在工作台上方菜单栏中点击【课表】按钮，可按日期筛选查看老师当日排课；查看上课时间、地点；手动设置学生考勤。
[图片: 老师端小程序功能]
- 查看黑板报：在工作台上方菜单栏中点击【黑板报】按钮，可快捷发布黑板报，筛选黑板报类型，查看黑板报内容。
[图片: 老师端小程序功能]
班级管理
老师点击下方导航中的【班级】按钮，在小程序端进行班级管理，查看班级的相关信息和状态；点击对应班级可在小程序端进行班级的作业管理。
[图片: 班级管理]
数据报告
老师点击下方导航中的【数据报告】按钮，在小程序端查看相关的教学数据报告；包含周作业正确率统计；当日、当周、当月和当季对应的教学数据报告；以及学生的作业完成率和正确率的排行榜。
[图片: 数据报告]

图片说明：老师登录小程序
图片说明：老师端小程序功能
图片说明：老师端小程序功能
图片说明：老师端小程序功能
图片说明：老师端小程序功能
图片说明：班级管理
图片说明：数据报告
```

### chunk_c86e71190185abc888550473f7eaaad9 | 一文读懂：如何使用首页功能

- source_id：helpcenter:148
- document_id：doc_helpcenter_148
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T15:49:50
- 图片数：5
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051754252700954820112896019", "alt_text": "首页功能展示", "ocr_text": null, "caption": "首页功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051756354228560134364281769", "alt_text": "待办事项", "ocr_text": null, "caption": "待办事项"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051755033897566329673439139", "alt_text": "黑板报功能", "ocr_text": null, "caption": "黑板报功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051755215032352274074613532", "alt_text": "黑板报功能", "ocr_text": null, "caption": "黑板报功能"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051755401135134163641682323", "alt_text": "数据看板", "ocr_text": null, "caption": "数据看板"}]

```text
一文读懂：如何使用首页功能
一文读懂：如何使用首页功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
首页功能展示
首页显示了AI 助手，老师的待办事项，黑板报以及数据看板。
老师可以通过ai 助手快速分析学生学习情况，及时检测异常数据。
[图片: 首页功能展示]
待办事项
老师可以在待办里查看今日的课程安排，待批改作业和待反馈课程。
[图片: 待办事项]
黑板报功能
老师可以编辑黑板报内容，包括：标题、正文内容、支持上传多张图片等，编辑完成后可以选择发布类型，包含： 通知、作业、活动、课程、考试等多种类型！
[图片: 黑板报功能]
[图片: 黑板报功能]
数据看板
老师可以点击数据看板，查看课时数、学生数、班级数、以及作业相关数据
[图片: 数据看板]

图片说明：首页功能展示
图片说明：待办事项
图片说明：黑板报功能
图片说明：黑板报功能
图片说明：数据看板
```

### chunk_1ac7c04f4026c432ccf3a50c35ac4375 | 一文读懂：如何进行学员管理

- source_id：helpcenter:149
- document_id：doc_helpcenter_149
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T15:55:49
- 图片数：13
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051757137998395588612701352", "alt_text": "基本信息", "ocr_text": null, "caption": "基本信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051757565177798613560564337", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051757594725401554972361200", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051758296121670251791819439", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305175902615635182549470568", "alt_text": "学习报告", "ocr_text": null, "caption": "学习报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051759564034639807068304159", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051800274595302184901289291", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051800584139731392864010110", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051801293329493034630714961", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051802042216361674533486878", "alt_text": "课程反馈", "ocr_text": null, "caption": "课程反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051803175194626484279580223", "alt_text": "课程反馈", "ocr_text": null, "caption": "课程反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305180522309813652673703059", "alt_text": "回访记录", "ocr_text": null, "caption": "回访记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051803391350459136374833149", "alt_text": "考试记录", "ocr_text": null, "caption": "考试记录"}]

```text
一文读懂：如何进行学员管理
一文读懂：如何进行学员管理
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
学员功能展示
学员管理显示老师所带所有学生，老师可以查看学生的基本信息、课表任务、学习报告、练习情况、课堂反馈、回访记录和考试记录。
基本信息
学生的基本信息会在这里显示。
[图片: 基本信息]
课表&任务
课表&任务里以月日历形式展示学生的课程，作业，及考试安排。老师还可点击日历左上角的添加任务，手动添加个性化任务。
[图片: 课表&任务]
[图片: 课表&任务]
老师可以通过筛选时间段，导出学生的课程和作业安排及完成情况，并且可生成图片分享给家长等。
[图片: 课表&任务]
学习报告
学习报告从学生成绩、课程、作业、知识点全面统计学生的学习成长轨迹。点击左上角即可一键生成学习报告。
[图片: 学习报告]
练习情况
练习情况可以看到学生的错题分析、练习统计、笔记。
学生练习统计包括作业完成情况、自适应统计、单词书进度、开放题库、词汇量测试五个板块，点击可查看学生的完成情况及详情。
[图片: 练习情况]
错题分析分模块和分题型统计学生练习模考中的所有错题。点击查看详情，即可看到对应题型下的错题，老师还可将错题二次布置给学生进行错题练习。
[图片: 练习情况]
学生在做题过程中留下的笔记都会记录下来，老师可点击此处的“笔记”查看。
[图片: 练习情况]
老师可以点击AI一键分析学生的学习进度以及薄弱知识点，帮助老师更好制定学习计划
[图片: 练习情况]
课程反馈
老师可以在这里给学生添加课堂反馈。
点击“添加评分建议”，进入下图课堂反馈界面 。
[图片: 课程反馈]
选择课堂、选择发送对象、填写学习建议、课堂表现、上次作业完成情况等进行学生上课表现反馈，反馈标准支持机构自定义设置。
[图片: 课程反馈]
回访记录
老师可以查看学生的沟通记录，可以添加回访记录
[图片: 回访记录]
考试记录
考试记录页面可以添加学生线下纸笔考试的成绩。

图片说明：基本信息
图片说明：课表&任务
图片说明：课表&任务
图片说明：课表&任务
图片说明：学习报告
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：课程反馈
图片说明：课程反馈
图片说明：回访记录
图片说明：考试记录
```

### chunk_6638ebaf7856325c1513e824bdba4bf0 | 一文读懂：如何进行学员管理

- source_id：helpcenter:149
- document_id：doc_helpcenter_149
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-13T15:55:49
- 图片数：13
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051757137998395588612701352", "alt_text": "基本信息", "ocr_text": null, "caption": "基本信息"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051757565177798613560564337", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051757594725401554972361200", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051758296121670251791819439", "alt_text": "课表&任务", "ocr_text": null, "caption": "课表&任务"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305175902615635182549470568", "alt_text": "学习报告", "ocr_text": null, "caption": "学习报告"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051759564034639807068304159", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051800274595302184901289291", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051800584139731392864010110", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051801293329493034630714961", "alt_text": "练习情况", "ocr_text": null, "caption": "练习情况"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051802042216361674533486878", "alt_text": "课程反馈", "ocr_text": null, "caption": "课程反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051803175194626484279580223", "alt_text": "课程反馈", "ocr_text": null, "caption": "课程反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305180522309813652673703059", "alt_text": "回访记录", "ocr_text": null, "caption": "回访记录"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051803391350459136374833149", "alt_text": "考试记录", "ocr_text": null, "caption": "考试记录"}]

```text
[图片: 考试记录]

图片说明：基本信息
图片说明：课表&任务
图片说明：课表&任务
图片说明：课表&任务
图片说明：学习报告
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：练习情况
图片说明：课程反馈
图片说明：课程反馈
图片说明：回访记录
图片说明：考试记录
```

### chunk_b4a8f1b3a1592cb271bf4590f1207256 | 一文了解：如何使用题库功能

- source_id：helpcenter:153
- document_id：doc_helpcenter_153
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T17:31:17
- 图片数：11
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051823574193627718900312052", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051806147833170238948148162", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051807143404848657620993474", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304131731064737286822695484006", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305181006691504249728537066", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051810103901865445681943868", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051811298133070870509563286", "alt_text": "系统题库", "ocr_text": null, "caption": "系统题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051813026986591990506599601", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051813304788762229863490415", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051814023500223760072332784", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051814368382869882278251124", "alt_text": "单词书", "ocr_text": null, "caption": "单词书"}]

```text
一文了解：如何使用题库功能
一文了解：如何使用题库功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
题库功能功能展示
老师可以在题库看到目前系统所有的科目题库、机构自有题库以及单词书。
系统题库
题库展示参与数、正确率、中位数、题目数、中位分、方差、中位用时、区分度。帮助老师更好的选择题目
[图片: 系统题库]
老师可以选择需要教研的题目，点击详情，可以添加名师讲解。
[图片: 系统题库]
[图片: 系统题库]
老师可以对所有题目的知识点进行自定义(这里所有机构知识点需要在知识点大纲中预设好，这里只做知识点的选择 )。
[图片: 系统题库]
老师可以点击答题预览，查看学生答题界面，点击打开白板，老师可以使用画笔、文字、激光笔等内容，方便老师进行题目讲解。
[图片: 系统题库]
[图片: 系统题库]
老师可以勾选题目，开放题目给学生自主答题。可以在已开放题目中查看。
[图片: 系统题库]
机构题库
老师可以上传机构专属题目到机构题库，形成校区专属题目库。点击新建试卷，即可创建试卷，编辑试卷名称，科目和类别，添加题目！
[图片: 机构题库]
[图片: 机构题库]
老师上传机构题库保存试卷，进行答题预览。
[图片: 机构题库]
单词书
老师可以根据自己的教学任务上传机构独有的单词书，下发给学生进行单词学习
[图片: 单词书]

图片说明：系统题库
图片说明：系统题库
图片说明：系统题库
图片说明：系统题库
图片说明：系统题库
图片说明：系统题库
图片说明：系统题库
图片说明：机构题库
图片说明：机构题库
图片说明：机构题库
图片说明：单词书
```

### chunk_1328fe713f9abfb674f41d2e08d69a5b | 一文读懂：如何进行班级管理

- source_id：helpcenter:150
- document_id：doc_helpcenter_150
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T16:20:17
- 图片数：13
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051815137173883001254397617", "alt_text": "班级功能展示", "ocr_text": null, "caption": "班级功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051815598313362693337771273", "alt_text": "班级功能展示", "ocr_text": null, "caption": "班级功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051816417402128891309955836", "alt_text": "布置作业", "ocr_text": null, "caption": "布置作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051817137369106564564567174", "alt_text": "添加至常用作业", "ocr_text": null, "caption": "添加至常用作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051817362161816339457245938", "alt_text": "布置/预览", "ocr_text": null, "caption": "布置/预览"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051817583782785536064489086", "alt_text": "关联音视频", "ocr_text": null, "caption": "关联音视频"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818204682780468934238425", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305181856776491688313944227", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305181931939058348141051421", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051819507497648164605199153", "alt_text": "课表", "ocr_text": null, "caption": "课表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051820537372152155264016355", "alt_text": "反馈", "ocr_text": null, "caption": "反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051821266432211909337946347", "alt_text": "作业大纲", "ocr_text": null, "caption": "作业大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051821452929754137327722343", "alt_text": "概览", "ocr_text": null, "caption": "概览"}]

```text
一文读懂：如何进行班级管理
一文读懂：如何进行班级管理
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
班级功能展示
班级页面会显示老师所带的所有班级。
老师可以通过筛选班级查看班级课表、作业等基本信息。
[图片: 班级功能展示]
老师可以点击“模考作业”即可进入下图布置作业界面。
[图片: 班级功能展示]
布置作业
作业题目内容分为基础练习 、题型训练 、模考测试、机构题库、自定义作业、打卡作业、视频课件作业7项。
基础练习 、题型训练和模考测试为校校系统自带的题库供机构直接使用，而机构题库和自定义作业是提供给机构录入自己的个性化作业资料的地方 。
[图片: 布置作业]
添加至常用作业
可将选中的题目定义好标题，添加至常用作业。下次需要布置时，只需在“拷贝作业”中点击选择添加好的常用作业进行一键布置。添加好的常用作业也可通过手机小程序端布置给学生，但要注意名称要定义清楚，布置时无法查看作业中的题目详情，且老师只能看到自己的常用作业。
[图片: 添加至常用作业]
布置/预览
点击布置，即可将选中的题目布置给学生；点击预览， 即预览到看到学生端的做题界面和作业结果页预览。
[图片: 布置/预览]
关联音视频
布置作业时可从云盘中选择关联音视频，学生在做到该项作业之前和做完之后均可观看关联音视频，后台也可自动记录学生的观看时长。
[图片: 关联音视频]
自定义作业
机构可将自己的作业资料以复制粘贴、图片、超链接、音频等形式输入到文本框，也可以添加附件让学生下载查看做题。
答题方式分为两种：
1. 答题卡作答 (老师添加答题卡，将正确答案输入，学生作答结束后系统自动批改正误。)
2. 无答题卡作答 (需要学生将写在纸上的答案拍照上传或上传音频作答内容，老师进行批改处理 。)
[图片: 自定义作业]
机构题库
需要提前在“题库管理”的“机构题库”中录入需要布置的题，录入完成后，即可在这里进行题目筛选布置。
[图片: 机构题库]

图片说明：班级功能展示
图片说明：班级功能展示
图片说明：布置作业
图片说明：添加至常用作业
图片说明：布置/预览
图片说明：关联音视频
图片说明：自定义作业
图片说明：机构题库
图片说明：机构题库
图片说明：课表
图片说明：反馈
图片说明：作业大纲
图片说明：概览
```

### chunk_f046be2afcc3c3c51de019cbb4777730 | 一文读懂：如何进行班级管理

- source_id：helpcenter:150
- document_id：doc_helpcenter_150
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-13T16:20:17
- 图片数：13
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051815137173883001254397617", "alt_text": "班级功能展示", "ocr_text": null, "caption": "班级功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051815598313362693337771273", "alt_text": "班级功能展示", "ocr_text": null, "caption": "班级功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051816417402128891309955836", "alt_text": "布置作业", "ocr_text": null, "caption": "布置作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051817137369106564564567174", "alt_text": "添加至常用作业", "ocr_text": null, "caption": "添加至常用作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051817362161816339457245938", "alt_text": "布置/预览", "ocr_text": null, "caption": "布置/预览"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051817583782785536064489086", "alt_text": "关联音视频", "ocr_text": null, "caption": "关联音视频"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818204682780468934238425", "alt_text": "自定义作业", "ocr_text": null, "caption": "自定义作业"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305181856776491688313944227", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305181931939058348141051421", "alt_text": "机构题库", "ocr_text": null, "caption": "机构题库"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051819507497648164605199153", "alt_text": "课表", "ocr_text": null, "caption": "课表"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051820537372152155264016355", "alt_text": "反馈", "ocr_text": null, "caption": "反馈"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051821266432211909337946347", "alt_text": "作业大纲", "ocr_text": null, "caption": "作业大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051821452929754137327722343", "alt_text": "概览", "ocr_text": null, "caption": "概览"}]

```text
老师可以进行作业检查。如果完成即会显示分数，未完成的作业会显示“未作答”或“进行中”状态。
[图片: 机构题库]
课表
老师可以查看班级课表，可以筛选不同的班级查看，点击课程可以查看详情，线上课可以点击去上课按钮跳转到在线课堂。
[图片: 课表]
反馈
老师可以在班级页面-反馈，选择学生，点击“添加评分意见”填写课堂反馈。
[图片: 反馈]
作业大纲
老师可以将添加好的作业大纲，一键关联给班级，并且设置作业布置日期并发布，系统会在指定日期下发对应作业到班级作业中。
注：老师可点击停用，停用后无法启用；可以单独设置某个作业不发布给班级；作业大纲不可下发当日作业。
[图片: 作业大纲]
概览
老师可以在班级概览里查看学生课程、作业和模考安排。
[图片: 概览]

图片说明：班级功能展示
图片说明：班级功能展示
图片说明：布置作业
图片说明：添加至常用作业
图片说明：布置/预览
图片说明：关联音视频
图片说明：自定义作业
图片说明：机构题库
图片说明：机构题库
图片说明：课表
图片说明：反馈
图片说明：作业大纲
图片说明：概览
```

### chunk_67a9ad7bf624d2c58933516f70ca4d93 | 一文读懂：如何使用作业功能

- source_id：helpcenter:151
- document_id：doc_helpcenter_151
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T16:51:15
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818215154760883133214462", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818325380495312960665597", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818485072533874617545678", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818523721222171517724482", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051818575726785756988239032", "alt_text": "作业功能展示", "ocr_text": null, "caption": "作业功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051819048381670445678097910", "alt_text": "AI作业分析", "ocr_text": null, "caption": "AI作业分析"}]

```text
一文读懂：如何使用作业功能
一文读懂：如何使用作业功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
作业功能展示
老师布置的作业都会在这里显示，可以筛选班级以及作业状态查看作业。
老师可以点击布置作业，选择班级、作业类型、学生；进入布置作业页面。
[图片: 作业功能展示]
基础练习 、题型训练和模考测试为校校系统自带的题库供机构直接使用，而机构题库、自定义作业打卡作业、视频课件作业是提供给机构录入自己的个性化作业资料的地方 。
[图片: 作业功能展示]
老师可以点击某个已完成的作业详情查看学生作答情况以及批改作业，也可以给学生填写评语，评语可以上传图片、音频、录音。
[图片: 作业功能展示]
[图片: 作业功能展示]
[图片: 作业功能展示]
AI作业分析
老师可以点击AI作业分析，点击一键分析学生作业完成情况、答题情况。
[图片: AI作业分析]

图片说明：作业功能展示
图片说明：作业功能展示
图片说明：作业功能展示
图片说明：作业功能展示
图片说明：作业功能展示
图片说明：AI作业分析
```

### chunk_1def20601944fe0dae614c861cff18fc | 一文了解：如何使用课表功能

- source_id：helpcenter:152
- document_id：doc_helpcenter_152
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T16:52:47
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051807101311736677760343084", "alt_text": "课表功能展示", "ocr_text": null, "caption": "课表功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051807186347471320724897558", "alt_text": "课表功能展示", "ocr_text": null, "caption": "课表功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051807257428829584071097210", "alt_text": "课表功能展示", "ocr_text": null, "caption": "课表功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051807323027463347957271205", "alt_text": "课表功能展示", "ocr_text": null, "caption": "课表功能展示"}]

```text
一文了解：如何使用课表功能
一文了解：如何使用课表功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
课表功能展示
老师可以查看自己的课表，以及课时详情，申请请假。
[图片: 课表功能展示]
老师可以在课时详情里，筛选时间，查看自己的课时统计及详情。
[图片: 课表功能展示]
老师可以在课表给学生进行考勤操作，以及布置作业
[图片: 课表功能展示]
老师可以在课表右上方申请请假，可以填写日期、时间以及原因。
[图片: 课表功能展示]

图片说明：课表功能展示
图片说明：课表功能展示
图片说明：课表功能展示
图片说明：课表功能展示
```

### chunk_9a47a0c52d00c8cd20ef6424cda81d34 | 一文了解：如何使用教研功能

- source_id：helpcenter:154
- document_id：doc_helpcenter_154
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T17:42:50
- 图片数：3
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305175903513834707031308868", "alt_text": "作业大纲", "ocr_text": null, "caption": "作业大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051759103960552219962697492", "alt_text": "知识点大纲", "ocr_text": null, "caption": "知识点大纲"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051759176923953390412798034", "alt_text": "知识点大纲", "ocr_text": null, "caption": "知识点大纲"}]

```text
一文了解：如何使用教研功能
一文了解：如何使用教研功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
教研功能展示
教研页面可以添加作业大纲和知识点。
作业大纲
老师可以创建作业大纲，预设好作业包 (单词、作业、音视频)，便可在我的班级界面直接关联给班级，下发作业。
[图片: 作业大纲]
知识点大纲
知识点大纲，包括我的大纲(只有添加的老师自己可以看到)和机构共享大纲(共享给的老师都可以看到) 。
[图片: 知识点大纲]
老师可以添加大纲，包括知识点类型 (可自由输入) 、知识点 、是否机构共享 、共享老师的选择 、知识点详情、视频音频讲解和附件【知识点下如果添加了音频讲解和视频讲解，学生在作业结果页，即可点击看到对应音视频】。
[图片: 知识点大纲]

图片说明：作业大纲
图片说明：知识点大纲
图片说明：知识点大纲
```

### chunk_e22985d13178cf7b76f8566aa818147f | 一文了解：如何使用云盘功能

- source_id：helpcenter:155
- document_id：doc_helpcenter_155
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T17:54:36
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051756396091746978275899688", "alt_text": "云盘功能展示", "ocr_text": null, "caption": "云盘功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051756468800221199963554868", "alt_text": "云盘功能展示", "ocr_text": null, "caption": "云盘功能展示"}]

```text
一文了解：如何使用云盘功能
一文了解：如何使用云盘功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
云盘功能展示
云盘分为我的云盘和共享云盘。
老师可以看到共享云盘里其他老师上传的文件，可以进行下载，点击上传即可添加文件。
[图片: 云盘功能展示]
老师可以选择上传到我的云盘或者共享云盘，点击选择文件，再进保存即可。
[图片: 云盘功能展示]

图片说明：云盘功能展示
图片说明：云盘功能展示
```

### chunk_8e346b38c1b380063fa404e56386efee | 一文了解：如何使用申请功能

- source_id：helpcenter:156
- document_id：doc_helpcenter_156
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T17:55:20
- 图片数：2
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051753166472359706687918255", "alt_text": "申请功能展示", "ocr_text": null, "caption": "申请功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051754008846747382802917997", "alt_text": "申请功能展示", "ocr_text": null, "caption": "申请功能展示"}]

```text
一文了解：如何使用申请功能
一文了解：如何使用申请功能
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
申请功能展示
老师可以在申请页面点击申请排课，选择班级，添加备注，点击确认，教务端会收到申请消息，老师也可以查看自己的申请是否通过。
[图片: 申请功能展示]
[图片: 申请功能展示]

图片说明：申请功能展示
图片说明：申请功能展示
```

### chunk_26b1d06e270e4a191fe366d075d31d7d | 一文了解：如何使用报课功能

- source_id：helpcenter:235
- document_id：doc_helpcenter_235
- 分类：核心功能介绍
- 适用角色库：student(学生库);principal(校长库);academic(教务库);sales(销售库)
- 分块序号：0
- 状态：active
- 更新时间：2025-09-11T11:47:42
- 图片数：4
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051748548403835864212499119", "alt_text": "数据统计", "ocr_text": null, "caption": "数据统计"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051749044680697480260779643", "alt_text": "班级上架", "ocr_text": null, "caption": "班级上架"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051749116890695513850685995", "alt_text": "报课设置", "ocr_text": null, "caption": "报课设置"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20260305174919725433189262736750", "alt_text": "优惠券设置", "ocr_text": null, "caption": "优惠券设置"}]

```text
一文了解：如何使用报课功能
一文了解：如何使用报课功能
校校系统提供小程序报课功能，可以在这里进行班级、报课、优惠券设置。
数据统计
报课数据统计会在这里显示，可以查看注册用户数、付费用户数、成交额、转化率等关键数据。
[图片: 数据统计]
班级上架
这里可以提前创建好需要报课的班级，设置班级相关信息，多选可以批量上架班级。
[图片: 班级上架]
报课设置
这里可以添加报课相关的信息，包括标题、是否允许未注册的学生报名、订单是否需要审核以及填写报名须知。
[图片: 报课设置]
优惠券设置
这里可以添加报课优惠券，包括无门槛券和叠加券。可以查看优惠券领取详情。
[图片: 优惠券设置]

图片说明：数据统计
图片说明：班级上架
图片说明：报课设置
图片说明：优惠券设置
```

### chunk_7231addda5eae69d63b6c841c232eb67 | 一文了解：如何查看数据

- source_id：helpcenter:157
- document_id：doc_helpcenter_157
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);principal(校长库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-13T17:57:34
- 图片数：6
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051726408923258509347145843", "alt_text": "数据功能展示", "ocr_text": null, "caption": "数据功能展示"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051726485981385245539642782", "alt_text": "学生分析", "ocr_text": null, "caption": "学生分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051726548077309565463697510", "alt_text": "学生分析", "ocr_text": null, "caption": "学生分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051728424895399335765140239", "alt_text": "学生分析", "ocr_text": null, "caption": "学生分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051729068421235111589383539", "alt_text": "老师分析", "ocr_text": null, "caption": "老师分析"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051729114387636750550425824", "alt_text": "老师分析", "ocr_text": null, "caption": "老师分析"}]

```text
一文了解：如何查看数据
一文了解：如何查看数据
教学是机构在发展中最为重要的环节之一，而老师又是教学的主体，那么老师该如何使用系统节省时间和精力，提升教学效率，帮助学生提升能力水平？快来看看系统能给老师带来哪些帮助吧。
数据功能展示
教学统计包括：学生分析 、老师分析 、提分分析。
[图片: 数据功能展示]
学生分析
老师点击查看详情，即可看到学生作业完成率、正确率、平均练习时长走势图，快速概览学生作业数据趋势。
[图片: 学生分析]
学生提分分析，以散点图形式，清晰罗列与学生相关各大元素与其提分走势的相关性，精准把握关键变量，提高学习效率，也可以看到单个学生学习数据汇总，让过程与结果更明了。
[图片: 学生分析]
老师可以点击学生作业查看详情，可以查看班级名称、作业、布置时间及作业状态等详情数据，点击操作查看一键跳转学生作业结果页
[图片: 学生分析]
老师分析
老师可以查看自己以及下属的平均提分率，作业查阅率，反馈效率数据统计。
提分分析以散点图形式清晰罗列与老师工作中的变量因素对提分的影响，精准分析核心变量，提高教学效率。
[图片: 老师分析]
老师工作数据统计让教学过程更加透明，更高效，可查看在授学生数、反馈次数、未反馈次数、班级作业数、作业查阅率
[图片: 老师分析]

图片说明：数据功能展示
图片说明：学生分析
图片说明：学生分析
图片说明：学生分析
图片说明：老师分析
图片说明：老师分析
```

### chunk_3a10593974a847e50f638b3d2b9fa7fb | 如何玩转在线课堂

- source_id：helpcenter:171
- document_id：doc_helpcenter_171
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：0
- 状态：active
- 更新时间：2023-04-19T15:36:48
- 图片数：15
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051707051424263575651022816", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191528506694607131027269651", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191528541494299273781082826", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191529354090727024877454784", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191530006620731532572068210", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230419153035251825693450553618", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191530588577326946132528191", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191531179172351272366222997", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191532323740138595422841554", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191533554612218465447659233", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191534314563945252918463457", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191535073134329008580792801", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191535128990909584237564614", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191536094945855690339943609", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191536154467465912927689867", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}]

```text
如何玩转在线课堂
如何玩转在线课堂
老师第一次使用在线课堂时，有什么注意事项？在线课堂有哪些功能可以让老师上课更轻松？下文将带您了解！
软件安装
使用在线课堂前，需要先进行软件的安装。
一：在课表找到对应的课程点击“去上课”按钮
[图片: 软件安装]
二：跳转后，首次进入课堂需要下载启动器，需要根据图中提示下载客户端/启动器，下载完整之后需要确保安装成功。
PC端页面和MAC端页面分别如下图所示：
Tips: 使用 iPad 操作一样，启动器根据浏览器提示跳转下载，如无法下载，可在 app store搜索“G 直播”，下载后，通过网页再次点击去上课，直接跳转进入课堂即可（如无法进入，需要查看safari浏览器是否设置为了电脑模式，如果是，需要取消）
[图片: 软件安装]
[图片: 软件安装]
三：安装成功之后，点击“点击启动”，会有弹窗显示，点击打开，即可以进入在线课堂
[图片: 软件安装]
课堂内使用说明
老师进入课堂后可以预览摄像头画面和进行麦克风测试，保证直播质量
[图片: 课堂内使用说明]
老师点击上讲台开始上课之后，可以使用不同的功能
[图片: 课堂内使用说明]
老师点击【开始上课】之后，可以进行录制（注：录制上课内容才会生成课堂回放）
注：在线课堂生成的回放不支持删除，回放不占用云盘空间
[图片: 课堂内使用说明]
老师点击“新建”可以【新建白板】
[图片: 课堂内使用说明]
老师可以添加【本地插播】（即音视频文件），添加之后可以在多媒体中心打开播放
（注：播放音频视频时，老师会暂时离开讲台，对上课无影响）
[图片: 课堂内使用说明]
老师可以打开【桌面共享】（注：桌面共享和本地插播不能同时使用）
如桌面共享时，学生不能看到全屏，老师需要将系统文本大小调至100%
操作方法：
win10操作路径：电脑桌面上点击鼠标右键---选择显示设置---设置更改文本、应用等项目的大小为100%
win7系统：鼠标右键点击桌面------选择屏幕分辨率---点击下方的“放大或缩小文本和其它项目”，设置为100%
[图片: 课堂内使用说明]

图片说明：软件安装
图片说明：软件安装
图片说明：软件安装
图片说明：软件安装
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
```

### chunk_4f432e5f8834cb3f6ccbf2574dc5df7a | 如何玩转在线课堂

- source_id：helpcenter:171
- document_id：doc_helpcenter_171
- 分类：核心功能介绍
- 适用角色库：student(学生库);teacher(老师库);academic(教务库)
- 分块序号：1
- 状态：active
- 更新时间：2023-04-19T15:36:48
- 图片数：15
- 图片引用：[{"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202603051707051424263575651022816", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191528506694607131027269651", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191528541494299273781082826", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191529354090727024877454784", "alt_text": "软件安装", "ocr_text": null, "caption": "软件安装"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191530006620731532572068210", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/20230419153035251825693450553618", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191530588577326946132528191", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191531179172351272366222997", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191532323740138595422841554", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191533554612218465447659233", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191534314563945252918463457", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191535073134329008580792801", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191535128990909584237564614", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191536094945855690339943609", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}, {"url": "https://xiaosaas.oss-cn-beijing.aliyuncs.com/202304191536154467465912927689867", "alt_text": "课堂内使用说明", "ocr_text": null, "caption": "课堂内使用说明"}]

```text
老师可以导入或新建试卷，并设置答题卡
[图片: 课堂内使用说明]
老师可以开启【虚拟背景】
操作方法：
第一步：点击右上角图标，打开硬件加速设置
第二部：点击虚拟抠像
[图片: 课堂内使用说明]
[图片: 课堂内使用说明]
老师可以将【举手学生】设置上【提问席】
注：学生需要先进行举手，最多可以让4位学生上提问席
[图片: 课堂内使用说明]
[图片: 课堂内使用说明]

图片说明：软件安装
图片说明：软件安装
图片说明：软件安装
图片说明：软件安装
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
图片说明：课堂内使用说明
```
