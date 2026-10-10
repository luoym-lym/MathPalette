# MathVerse 本批收录与核验

从项目根目录的 `wrong_review_vision_dominant.html` 收录全部 107 题。三个 GPT-6-Luna 子代理分别处理函数与解析几何、平面几何、立体几何，主代理逐页对照原图与重绘图并复核答案。原始题干、来源 GT、来源图片均保留；核验候选单独记录，没有删除问题题目或用候选结果覆盖 GT。

| 分支 | 新题号 | 题数 | 需复核 |
| --- | --- | ---: | ---: |
| 函数与解析几何 | Ana21～Ana66 | 46 | 14 |
| 平面几何 | Plane01～Plane40 | 40 | 19 |
| 立体几何 | Solid01～Solid21 | 21 | 13 |
| 合计 | | 107 | 46 |

打开 [原图与重绘对照页](redraw_review.html)，可按题型、核验状态、入库状态和题号筛选，点击图片查看完整尺寸。全部疑点及推导见 [issues.md](issues.md)。`needs_review` 包括来源答案冲突、条件缺失、单位、公式格式、精度和读图歧义，并不都代表已经证实的数学错误。`verified` 表示本次数学核验相符；所有原题（包括函数与解析几何）的 `user_pass` 仅在用户明确通过且当前内容指纹相符时为 `true`。

2026-10-10 平面几何已迁移至重绘协议 1.1.0，数字、字母和编号角标配一条弧，同角多标识共用弧；无角标的直角保留方框。详情见 [平面几何更新记录](../../PlaneGeometry/README.md)。

随后平面协议更新为 1.2.0、立体协议更新为 1.1.0：61 道几何题按完整图示包围盒居中并放大，最长边约占画布 86%；点名 18 pt、数值及单位 16 pt，线宽 1 pt。三个 GPT-6-Luna 子代理以 medium 档位分批重绘并检查标注。几何、投影、显隐关系、题干与来源答案保留，调整前文件另存备份。见 [构图调整前后](layout_upgrade_20261010/layout_review.html) 与 [检查记录](layout_upgrade_20261010/validation.json)。

正式题库 [question_bank.jsonl](../../question_bank.jsonl) 仅包含用户明确通过的原题，函数与解析几何也适用。全部候选见根目录 [question_candidates.jsonl](../../question_candidates.jsonl)，未通过题在 [pending_questions.jsonl](../../pending_questions.jsonl)。平面、立体分支 `dataset.jsonl` 仅存已通过题；Analytics 原 `dataset.jsonl` 保留为 Base/Special 的冻结候选输入，正式原题另用 `approved_dataset.jsonl`。各分支还有 `pending_dataset.jsonl`，保留所有原题和图片。[imported_questions.jsonl](imported_questions.jsonl) 仍保存本批全部 107 题的来源、重绘、核验及入库状态。当前数量见 [审核进度](question_review_progress.json)，用户原话与通过版本见 [用户审核记录](question_user_reviews.json)。既有 Special Pass/Collect 记录保留，不代替原题审核。

函数与解析几何新生成 184 张 Base，每题不放回抽取四种并通过插件重绘核对；46 题进入 Special 待办。平面与立体分支提供 PNG/SVG 和冻结场景，尚未启用 Base/Special。平面场景冻结几何关系；立体场景分别冻结三维几何、投影和可见性。所有重绘使用项目的 Matplotlib 渲染流程。

核验记录：

- [收录报告](import_report.json)：题数、来源保留、旧文件核对及分支疑点数量。
- [浏览器检查](browser_validation.json)：214 张图片、状态筛选、题型筛选和题号搜索。
- `source_manifest.json` / `assignments.json`：原始抽取内容与正式题号映射。
- `root_verification.json`：主代理独立复核及中文疑点，独立于来源 GT。
- `base_check.log` / `analytic_dependencies_check.log` / `arrow_check.log`：Base 重绘核对。
- `line_endings_restoration.json`：7 个旧脚本仅恢复到既有冻结哈希的 LF 换行，原字节备份在 `line_endings_before/`。旧题数学内容未修改，433 个受保护的旧图片、Base 与 Special 文件字节一致，原 Base 引擎未修改。

在项目根目录重新核对索引并生成对照页：

```powershell
python -X utf8 -B imports/mathverse_vision_dominant/build_catalog.py
```

需要重新渲染某道几何题时，使用对应冻结场景：

```powershell
python -X utf8 -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
```

实际查看更新后的来源图和重绘图之后，再用 `--reviewed` 记录视觉检查。输入或输出变化会使原视觉检查失效，汇总程序会拒绝未检查或哈希过期的结果。
