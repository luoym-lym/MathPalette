# MathPalette

本目录只收集用户确认的正式题目。当前 **133 题**：Analytics 46、PlaneGeometry 71、SolidGeometry 16。来源为 DynaMath 20 题、MathVerse 57 题、MathVista 56 题。

| 内容 | 数量 / 入口 |
| --- | --- |
| 正式原题 | [question_bank.jsonl](question_bank.jsonl)，133 条 |
| 自动 Base | Analytics 每题 4 张，共 184 张及对应插件 |
| 人工 Special | 当前 Analytics 共 95 张，保留原 Pass / Collect 时间 |
| 来源截图 | MathVerse 57 张、MathVista 56 张；DynaMath 20 题的来源截图在原库中缺失 |
| 解析几何 Special 工作台 | 双击 [Analytics/start_special_workbench.cmd](Analytics/start_special_workbench.cmd)，端口 8767 |
| 平面几何 Special 工作台 | 双击 [PlaneGeometry/start_special_workbench.cmd](PlaneGeometry/start_special_workbench.cmd)，端口 8768 |
| 立体几何 Special 工作台 | 双击 [SolidGeometry/start_special_workbench.cmd](SolidGeometry/start_special_workbench.cmd)，端口 8769 |
| 几何工作台需求 | [GEOMETRY_WORKBENCH_REQUIREMENTS.md](GEOMETRY_WORKBENCH_REQUIREMENTS.md) |
| 审核凭据 | [provenance/approvals.json](provenance/approvals.json) |
| MathVista 来源与署名 | [provenance/mathvista/README.md](provenance/mathvista/README.md)，含完整源记录与入库核验 |

Ana01～Ana20 来自 DynaMath，Ana21～Ana45 来自 MathVerse，Ana46 来自 MathVista。Plane01～Plane16 来自 MathVerse，Plane17～Plane71 来自 MathVista；Solid01～Solid16 来自 MathVerse。图片、绘图类、Base 插件和工作台使用相同题号。清理前编号仅保存在 [迁移记录](provenance/cleanup.json) 中。

## 数据内容

三个分支的 `dataset.jsonl` 均表示正式题，路径相对于所在分支。根目录 `question_bank.jsonl` 是自动汇总，路径相对于项目根目录，不手工编辑。

| 字段 | 含义 |
| --- | --- |
| `id` | 唯一题号 |
| `source_dataset` / `source_key` | 数据集名称，如 DynaMath、MathVerse、MathVista；已有来源键时保留 |
| `question` / `answer` / `answer_type` | 当前正式题干、答案、答案类型 |
| `choices` | 仅选择题包含，保存选项字母与内容的对应关系；`answer` 只保存字母 |
| `image` | 正式统一重绘 PNG |
| `original_image` | 来源截图；没有时为 `null` |
| `script` | 本题绘图程序 |
| `scene` | 几何题的冻结场景，含坐标、标签、约束；立体还含投影与显隐 |
| `base_plugins` / `special_plugins` | 根目录汇总清单中的插件路径；尚未收集时为空列表 |

每份变体保留图片、插件、`recipes.json` 与 `draw_variants.py`。recipes 保存冻结参数、哈希、环境及生成/人工通过时间；公共绘图器和机器协议也是重绘依赖，不能只留下逐题脚本。源题与当前题干或答案不同的说明保存在 `provenance/source_notes.json`。

答案类型统一为 `choice`、`number`、`expression`、`text`，含义见 [数据协议](MATHPALETTE_PROTOCOL.md)。正式清单保存题干、答案、选项和数据集来源；场景只保留绘图、约束及必要解释。表示迁移记录见 [schema_normalization.json](provenance/schema_normalization.json)，原用户通过时间和变体 Pass / Collect 时间保留。

## 目录

```text
Analytics/       正式清单、图片、绘图器、Base、Special、工作台、评测程序
PlaneGeometry/   正式清单、图片、冻结二维场景、绘图器、Special 工作台
SolidGeometry/   正式清单、图片、冻结三维场景、绘图器、Special 工作台
dataset_tools/   正式索引、内容校验和几何重绘
provenance/      用户通过记录、必要来源说明、署名与迁移核验记录
.runtime/        启动后生成的工作台状态、预览和临时重绘
```

`.runtime` 不属于正式数据。服务停止且没有需要保留的未提交草稿时可以清理；工作台会从正式 recipes 和 collection 记录恢复已收集状态。旧候选、历史工作台、重复备份、旧评测日志及分数已按用户要求清理。

## 使用

在项目根目录执行：

```powershell
python -m pip install -r requirements.txt
python -X utf8 -B dataset_tools/catalog.py check
python -X utf8 -B dataset_tools/catalog.py build
python -X utf8 -B Analytics/dataset_generator/generate_base_variants.py check --redraw
python -X utf8 -B Analytics/workbench/launch_workbench.py --check
python -X utf8 -B PlaneGeometry/workbench/launch_workbench.py --check
python -X utf8 -B SolidGeometry/workbench/launch_workbench.py --check
python -X utf8 -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
python -X utf8 -B Analytics/special_variant/Ana01/draw_variants.py C01
```

三套工作台分别展示各分支的正式题，保存独立草稿和收集进度，可以同时运行。平面与立体首版提供原对象改色及实虚线、四色标记点、四色辅助虚线、已有顶点和新增点吸附；画板和 Agent 使用相同插件限制。原题数据和审核记录不由标注工具修改。平面、立体的 Base 尚未启用。

双击 CMD 时，工作台启动器会自动寻找与正式数据冻结版本匹配的 Python，避免系统 Python 与 Conda 环境混用导致像素校验失败。启动窗口会显示实际解释器路径和依赖版本；也可通过 `MATHPALETTE_PYTHON` 指定匹配的解释器。

候选图右上角提供 **Quick Test**：使用 `.env` 中的 `MINIMAX_API_KEY` 调用中国区 MiniMax-M3，关闭思考后直接回答候选图对应的题目，不设置本地输出上限。画板标注后先点击「提交到当前候选」即可测试；不接入 judge，不自动收集。结果分别保存在 `.runtime/analytics_special/quick_tests/`、`.runtime/plane_special/quick_tests/` 和 `.runtime/solid_special/quick_tests/`。

评测程序在 `Analytics/evaluation/`，默认读取项目根目录 `.env`。评测会调用模型 API；本次清理只检查数据加载与本地重绘，没有运行模型评测。新增结果默认写入 `.runtime/evaluation/`。

新增题目或修改内容前阅读 [MATHPALETTE_PROTOCOL.md](MATHPALETTE_PROTOCOL.md)。原题通过与 Special Pass / Collect 独立，不能相互代替。

## MathVista 入库记录

本轮用户逐题通过的 56 题已正式入库。每题保留来源图片、完整源记录、正式题干与答案、绘图程序；55 道平面题另有冻结场景，Ana46 的冻结输入保存在绘图程序中。原始来源、署名及必要许可通知见 [来源说明](provenance/mathvista/README.md)。

审核网页、候选包、重复核验文件及运行缓存已清理。用户通过原话、时间和内容指纹仍由 `provenance/approvals.json` 保存；已入库题的解题核验及当时候选内容快照保存在 `provenance/source_notes.json`。快照中的旧路径仅供追溯，实际使用正式清单中的路径。通过按钮凭据和像素复现、来源路径迁移核验见 [imports.json](provenance/mathvista/imports.json)。
