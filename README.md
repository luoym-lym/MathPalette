# MathPalette

MathPalette 研究统一渲染条件下，视觉标记如何影响视觉语言模型的数学推理。原题经用户确认后收集，Special 从原图独立派生、经用户审核后保存，冻结操作以便重绘。标记方法与后续探索见 [Conclusion.md](Conclusion.md)（2026-10-17 的历史盘点）。[paper.tex](paper.tex) 是研究设计草稿，包含尚未启用的 BaseVar 设计；当前可用数据与功能以本说明和数据协议为准。编译论文还需准备 ICML 2026 模板及其参考文献文件。

截至 2026-10-27，正式数据为 **265 题、335 张 Special**：Analytics 51 题 / 116 张，PlaneGeometry 136 题 / 189 张，SolidGeometry 78 题 / 30 张。Special 覆盖 80 道原题。题源为 DynaMath 20 题、MathVerse 125 题、MathVista 56 题、SOLIDGEO 9 题、Author designed 55 题；最新数量以 `catalog.py check` 为准。

| 内容 | 数量 / 入口 |
| --- | --- |
| 正式原题 | [question_bank.jsonl](question_bank.jsonl)，265 条 |
| Base | 三个分支均未启用，汇总索引中的 `base_plugins` 为空列表 |
| 已审核 Special | 共 335 张，保留原 Pass / Collect 时间；只有完成标记、没有已通过图片的题不计入变体数 |
| 来源截图 | MathVerse 125 张、MathVista 56 张、SOLIDGEO 9 张，另有 9 张作者提供的参考图；DynaMath 20 题的来源截图在原库中缺失 |
| 解析几何 Special 工作台 | 双击 [Analytics/start_special_workbench.cmd](Analytics/start_special_workbench.cmd)，端口 8767 |
| 平面几何 Special 工作台 | 双击 [PlaneGeometry/start_special_workbench.cmd](PlaneGeometry/start_special_workbench.cmd)，端口 8768 |
| 立体几何 Special 工作台 | 双击 [SolidGeometry/start_special_workbench.cmd](SolidGeometry/start_special_workbench.cmd)，端口 8769 |
| 工作台使用与标注范围 | [解析](Analytics/workbench/README.md)、[平面](PlaneGeometry/workbench/README.md)、[立体](SolidGeometry/workbench/README.md)；Agent 说明和插件 schema 在各工作台目录 |
| 审核凭据 | [provenance/approvals.json](provenance/approvals.json) |
| Author designed 变体审核 | [本轮用户审核确认](provenance/author_designed_variant_review_20261023.json)、[初次批量 Pass 授权](provenance/author_designed_variant_pass_20261023.json)、[Plane122 改色记录](provenance/plane122_axis_black_20261023.json)、[网格与扇形变体通过及 Collect 记录](provenance/grid_spinner_variant_pass_collect_20261026.json)；初次授权记录中的槽位属于当时快照，当前保留内容以正式 recipes 为准 |
| MathVista 来源与署名 | [provenance/mathvista/README.md](provenance/mathvista/README.md)，含完整源记录与入库核验 |
| SOLIDGEO 来源与清理记录 | [来源署名](provenance/SOLIDGEO_ATTRIBUTION.md)、[保留题目与清理核验](provenance/solidgeo_cleanup.json) |

当前题号为 Ana01～Ana51、Plane01～Plane136、Solid01～Solid78。Ana01～Ana20 来自 DynaMath，Ana21～Ana45 与 Ana47～Ana51 来自 MathVerse，Ana46 来自 MathVista。Plane01～Plane16 与 Plane72～Plane93 来自 MathVerse，Plane17～Plane71 来自 MathVista，Plane94～Plane136 为 Author designed；Solid01～Solid16 与 Solid26～Solid66 来自 MathVerse，Solid17～Solid25 来自 SOLIDGEO，Solid67～Solid78 为 Author designed。图片、绘图类、Special 插件和工作台使用相同题号。清理前编号仅保存在 [迁移记录](provenance/cleanup.json) 中。

Author designed 平面题包括 Plane94～Plane99 曲线追踪、Plane100～Plane102 最短路径、Plane103～Plane108 图形比较、Plane109～Plane114 交点计数、Plane115 直线延长判断，Plane116～Plane118 平行、垂直和等角判断，Plane119 多边形边数判断，Plane120～Plane121 折线转折与平面分区计数，以及 Plane122 轴对称点判断。最短路径三题分别使用等半径双圆、单圆偏置端点、不等半径双圆；正式图保留黑色几何和尺寸标注，精确答案以 `dataset.jsonl` 为准。

Plane109～Plane114 为用户确认收集的六道原创交点计数题，来源统一为 `Author designed`，按当时暂存图1～图6的顺序入库，答案依次为 6、4、5、6、6、8。正式数据保留黑白原图、冻结场景和逐题绘图程序；构造、独立求交和像素复现核验见 [来源记录](provenance/source_notes.json)。没有外部来源图片，`original_image` 为 `null`；后续通过工作台收集的诱导变体保存在各题的 `special_variant/` 目录中。

Plane115 为用户确认收集的原创直线延长判断题，答案为 A（Point A）。重绘图保留线段 PO 与 C、A、B 三个候选点，相邻候选点间距从参考图约 78 px 增至约 125 px；P、O、A 共线且 O 位于 P 与 A 之间。作者提供的参考图原样保存在 `PlaneGeometry/originals/Plane115.png`。

Plane116～Plane118 分别为平行、垂直、等角判断题，答案依次为 A、C、C；对应用户审阅时的暂存编号 Plane117、Plane118、Plane120。按连续题号迁入时保留题干、选项、答案和原图像素，编号对应关系及内容哈希见 [来源记录](provenance/source_notes.json)。原题入库时清理了未收集的配套标注和旧稿；后续 Special 及整题完成记录以各题工作台目录为准。

Plane119 为用户确认的原创多边形边数判断题，答案为 6。正式图为六条边组成的闭合不规则六边形，作者上传的参考图原样保存在 `PlaneGeometry/originals/Plane119.png`。

Plane120、Plane121 为用户确认收集的折线转折与矩形分区计数题，答案分别为 5、7；对应审阅时的暂存编号 Plane120、Plane124。Plane121 使用三条内部直线累计上移约 107 px 的最终确认版；三个交点互异，仍将矩形分成 7 个区域。两题均无外部来源图片，原题图像像素原样保留；编号映射、冻结几何及复现核验见 [来源记录](provenance/source_notes.json)。

Plane122 为用户确认的原创轴对称点判断题，答案为 A（Point A）。直线 l 垂直平分 PA；图中仅保留参考图已有的四个点、点名与直线 l，不添加垂足或辅助线。上传参考图原样保存在 `PlaneGeometry/originals/Plane122.png`，构造和复现核验见 [来源记录](provenance/source_notes.json)。

Plane123～Plane129 为用户确认收录的七道单位方格阴影多边形面积题，来源统一为 `Author designed`。顺序为参照凹箭头、偏置箭头、双凹口箭头、不等削角、沙漏、非45度斜带、凹阶梯，答案依次为 10、13.5、14、33/2、18、7、18。Plane123 保留用户上传的参考图，其余六题 `original_image` 为 `null`；六道新题使用各自调整后的英文措辞。独立面积验算、冻结场景及像素复现证据见 [来源记录](provenance/source_notes.json)，用户确认原话和当前内容指纹见 [审核记录](provenance/approvals.json)。这七题共保存 41 张 Special：Plane123 有 5 张，其余各 6 张，均已 Collect；用户手工图和本轮新增图的原通过记录分别保留。

Plane130～Plane136 为用户确认收录的七道圆盘阴影扇形概率题，来源统一为 `Author designed`，均使用已审核的精简英文题干。顺序为参照题、上半圆内侧灰区、上半圆端部灰区、下半圆内侧灰区、上半圆五扇区、竖直直径、倾斜直径五扇区，答案依次为 1/6、7/36、5/36、1/8、11/72、13/72、1/9。样本空间均为整个圆盘，按面积均匀取点。Plane130 保留用户上传的参考图，其余六题 `original_image` 为 `null`；题干、答案及重绘像素与审核版一致，角度和面积比核验见 [来源记录](provenance/source_notes.json)。这七题各保存 6 张 Special，均已 Collect；Plane130 原有的 2 张手工图与本轮追加的 4 张、其余六题各新增的 6 张均保留冻结插件、图片和离线重绘入口。

Solid67～Solid72 为用户确认的六道中点截面体积题，答案依次为 30、108、144、60、42、40。Solid67 保留用户提供的参考图，其余五题 `original_image` 为 `null`；当前 Solid67 已有 3 张 Special。构造、原题修订和来源答案争议统一保存在 [source_notes.json](provenance/source_notes.json)，原题审核见 [approvals.json](provenance/approvals.json)。

Solid73 为用户确认的原创三棱柱展开图题，题干和选项均为英文，答案为 B（Point R）。上传参考图原样保存在 `SolidGeometry/originals/Solid73.png`；三维折叠对应、边界粘合与像素复现核验见 [来源记录](provenance/source_notes.json)。

Solid74、Solid75 为用户确认的立方体顶点重合与正四面体相对棱题，答案依次为 B（Point R）、B（Edge BC）；对应审阅时的 75、77。按用户允许修改编号的要求连续收录，题干、选项、答案和原题图像像素保持不变。两题均无外部来源图，编号映射、三维折叠及复现核验见 [来源记录](provenance/source_notes.json)。后续通过的 Special 保存在正式工作台输出目录，零变体的完成题仅保留整题完成记录。

Solid76～Solid78 为用户确认的立方体、直三棱柱和四棱锥展开图共端点判断题，对应审阅时的 80、81、82，答案依次为 C（Edge DF）、B（Edge DE）、A（Edge DE）。按连续题号收录时，英文题干、选项、答案和原题图像像素保持不变；三题均无外部来源图片。编号映射、独立折叠核验和复现记录见 [来源记录](provenance/source_notes.json)。

## 数据内容

三个分支的 `dataset.jsonl` 均表示正式题，路径相对于所在分支。根目录 `question_bank.jsonl` 是自动汇总，路径相对于项目根目录，不手工编辑。

| 字段 | 含义 |
| --- | --- |
| `id` | 唯一题号 |
| `source_dataset` / `source_key` | 数据集名称，如 DynaMath、MathVerse、MathVista、SOLIDGEO；已有来源键时保留 |
| `question` / `answer` / `answer_type` | 当前正式题干、答案、答案类型 |
| `choices` | 仅选择题包含，保存选项字母与内容的对应关系；`answer` 只保存字母 |
| `image` | 正式统一重绘 PNG |
| `original_image` | 来源截图；没有时为 `null` |
| `script` | 本题绘图程序 |
| `scene` | 几何题的冻结场景，含坐标、标签、约束；立体还含投影与显隐 |
| `base_plugins` / `special_plugins` | 根目录汇总清单中的插件路径；尚未收集时为空列表 |

每份变体保留图片、插件、`recipes.json` 与 `draw_variants.py`。recipes 保存冻结参数、哈希、环境及生成/用户通过时间；公共绘图器和机器协议也是重绘依赖，不能只留下逐题脚本。插件中的 `description`、`intent` 保留生成时的说明，正式收集状态以 recipes 的 `status="passed"` 为准，模型测试结果另属于临时实验记录。源题与当前题干或答案不同的说明保存在 `provenance/source_notes.json`。

答案类型统一为 `choice`、`number`、`expression`、`text`，含义见 [数据协议](MATHPALETTE_PROTOCOL.md)。正式清单保存题干、答案、选项和数据集来源；场景只保留绘图、约束及必要解释。表示迁移记录见 [schema_normalization.json](provenance/schema_normalization.json)，原用户通过时间和变体 Pass / Collect 时间保留。

## 目录

```text
Analytics/       正式清单、图片、绘图器、Special 工作台、评测程序
PlaneGeometry/   正式清单、图片、冻结二维场景、绘图器、Special 工作台
SolidGeometry/   正式清单、图片、冻结三维场景、绘图器、Special 工作台
dataset_tools/   正式索引、内容校验和几何重绘
provenance/      用户通过记录、必要来源说明、署名与迁移核验记录
.runtime/        启动后生成的工作台状态、预览和临时重绘
```

SOLIDGEO 本批审核已结束，只保留用户已 Pass 的 9 道正式题。剩余 86 道待审候选、重复暂存资源、本批原题审核工具及其运行缓存已按用户要求删除；当前没有待审候选清单。

`.runtime/` 不属于正式数据，存放 Special 工作台草稿、预览及本地校验输出。服务停止且没有需要保留的未提交草稿时可以清理；工作台会从正式 recipes 和 collection 记录恢复已收集状态。旧候选、历史工作台、重复备份、旧评测日志及分数已按用户要求清理。

## 使用

在项目根目录执行：

```powershell
python -m pip install -r requirements.txt
python -X utf8 -B dataset_tools/catalog.py check
python -X utf8 -B dataset_tools/catalog.py build
python -X utf8 -B Analytics/workbench/launch_workbench.py --check
python -X utf8 -B PlaneGeometry/workbench/launch_workbench.py --check
python -X utf8 -B SolidGeometry/workbench/launch_workbench.py --check
python -X utf8 -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
python -X utf8 -B Analytics/special_variant/Ana01/draw_variants.py C01
```

三套工作台分别展示各分支的正式题，保存独立草稿和收集进度，可以同时运行。平面与立体支持四色标记点、实线/虚线辅助线、已有点吸附，以及原对象整体或局部区间的颜色、线型和白名单线宽覆盖；画板和 Agent 使用相同插件限制。立体的三维几何、投影和原可见性分别冻结，外观覆盖只作用于变体。原题数据和审核记录不由标注工具修改。三个分支的 Base 均未启用。

双击 CMD 时，工作台启动器会自动寻找与正式数据冻结版本匹配的 Python，避免系统 Python 与 Conda 环境混用导致像素校验失败。启动窗口会显示实际解释器路径和依赖版本；也可通过 `MATHPALETTE_PYTHON` 指定匹配的解释器。

候选图右上角提供 **Quick Test**，可手动调用配置的模型模式；具体模型、密钥变量和参数见各工作台说明与 `quick_test.py`。画板标注后先点击「提交到当前候选」即可测试。请求只含正式题干与当前候选 PNG，不发送标准答案、原图或标注意图；不接入 judge，不自动收集。结果分别保存在 `.runtime/analytics_special/quick_tests/`、`.runtime/plane_special/quick_tests/` 和 `.runtime/solid_special/quick_tests/`。

评测程序在 `Analytics/evaluation/`，默认读取项目根目录 `.env`。评测会调用模型 API；本次清理只检查数据加载与本地重绘，没有运行模型评测。新增结果默认写入 `.runtime/evaluation/`。

新增题目或修改内容前阅读 [MATHPALETTE_PROTOCOL.md](MATHPALETTE_PROTOCOL.md)。原题通过与 Special Pass / Collect 独立，不能相互代替。

## MathVista 入库记录

本轮用户逐题通过的 56 题已正式入库。每题保留来源图片、完整源记录、正式题干与答案、绘图程序；55 道平面题另有冻结场景，Ana46 的冻结输入保存在绘图程序中。原始来源、署名及必要许可通知见 [来源说明](provenance/mathvista/README.md)。

审核网页、候选包、重复核验文件及运行缓存已清理。用户通过原话、时间和内容指纹仍由 `provenance/approvals.json` 保存；已入库题的解题核验及当时候选内容快照保存在 `provenance/source_notes.json`。快照中的旧路径仅供追溯，实际使用正式清单中的路径。通过按钮凭据和像素复现、来源路径迁移核验见 [imports.json](provenance/mathvista/imports.json)。

## SOLIDGEO 入库与清理记录

本批最初有 168 道来源题，最终保留用户逐题 Pass 的 9 道：

| 正式题号 | 来源题号 |
| --- | --- |
| Solid17 | 1766 |
| Solid18 | 1807 |
| Solid19 | 1878 |
| Solid20 | 1892 |
| Solid21 | 1932 |
| Solid22 | 2024 |
| Solid23 | 2046 |
| Solid24 | 2072 |
| Solid25 | 2135 |

此前已删除 73 道，本次删除剩余 86 道。保留题的正式题干、答案、来源图、重绘图、冻结场景、绘图程序和审核记录均保持不变；清理前后文件指纹及通过凭据见 [清理记录](provenance/solidgeo_cleanup.json)。[来源署名](provenance/SOLIDGEO_ATTRIBUTION.md) 中的 168 题指最初审核批次，当前正式收集数量为 9 题。`source_notes.json` 内的旧候选路径仅作历史追溯，运行依赖全部位于正式目录。

此后，用户确认了 Solid17～Solid25 的题干清理版：删除图片占位符、残留标题和填空占位，统一英文提问，并同步逐题脚本。数学条件、答案、选项和绘图输入保持原样；修改前后题干、原 Pass 凭据、本次确认及像素核验见 [题干修订记录](provenance/solidgeo_wording_cleanup.json)。当前审核指纹对应已确认的新版题干。
