# MathPalette

本目录只收集用户确认的正式题目。当前 **77 题**：Analytics 45、PlaneGeometry 16、SolidGeometry 16。Analytics 包含 DynaMath 20 题与 MathVerse 25 题；平面、立体均来自 MathVerse。

| 内容 | 数量 / 入口 |
| --- | --- |
| 正式原题 | [question_bank.jsonl](question_bank.jsonl)，77 条 |
| 自动 Base | Analytics 每题 4 张，共 180 张及对应插件 |
| 人工 Special | Ana01～Ana20 共 72 张，保留原 Pass / Collect 时间 |
| 来源截图 | MathVerse 57 张；DynaMath 20 题的来源截图在原库中缺失 |
| Special 工作台 | 双击 [Analytics/start_special_workbench.cmd](Analytics/start_special_workbench.cmd) |
| 审核凭据 | [provenance/approvals.json](provenance/approvals.json) |

Ana01～Ana20 保留 DynaMath 编号，Ana21～Ana45 为 MathVerse；图片、绘图类、Base 插件和工作台使用相同题号。平面、立体分别使用 Plane01～Plane16、Solid01～Solid16。清理前编号仅保存在 [迁移记录](provenance/cleanup.json) 中。

## 数据内容

三个分支的 `dataset.jsonl` 均表示正式题，路径相对于所在分支。根目录 `question_bank.jsonl` 是自动汇总，路径相对于项目根目录，不手工编辑。

| 字段 | 含义 |
| --- | --- |
| `id` | 唯一题号 |
| `source_dataset` / `source_key` | 真实来源；已有来源键时保留 |
| `question` / `answer` / `answer_type` | 当前正式题干、答案、答案类型 |
| `image` | 正式统一重绘 PNG |
| `original_image` | 来源截图；没有时为 `null` |
| `script` | 本题绘图程序 |
| `scene` | 几何题的冻结场景，含坐标、标签、约束；立体还含投影与显隐 |
| `base_plugins` / `special_plugins` | 根目录汇总清单中的插件路径；尚未收集时为空列表 |

每份变体保留图片、插件、`recipes.json` 与 `draw_variants.py`。recipes 保存冻结参数、哈希、环境及生成/人工通过时间；公共绘图器和机器协议也是重绘依赖，不能只留下逐题脚本。源题与当前题干或答案不同的说明保存在 `provenance/source_notes.json`。

## 目录

```text
Analytics/       正式清单、图片、绘图器、Base、Special、工作台、评测程序
PlaneGeometry/   正式清单、图片、冻结二维场景、绘图器
SolidGeometry/   正式清单、图片、冻结三维场景、绘图器
dataset_tools/   正式索引、内容校验和几何重绘
provenance/      用户通过记录、必要来源说明、一次清理核验记录
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
python -X utf8 -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
python -X utf8 -B Analytics/special_variant/Ana01/draw_variants.py C01
```

工作台仅展示正式 Analytics 题。Ana01～Ana20 的 Collect 状态保留，新 MathVerse 25 题等待人工制作 Special。平面、立体的 Base / Special 尚未启用。

双击 CMD 时，工作台启动器会自动寻找与正式数据冻结版本匹配的 Python，避免系统 Python 与 Conda 环境混用导致像素校验失败。启动窗口会显示实际解释器路径和依赖版本；也可通过 `MATHPALETTE_PYTHON` 指定匹配的解释器。

候选图右上角提供 **Quick Test**：使用 `.env` 中的 `MINIMAX_API_KEY` 调用中国区 MiniMax-M3，关闭思考后直接回答候选图对应的题目，不设置本地输出上限。画板标注后先点击「提交到当前候选」即可测试；不接入 judge，不自动收集，结果只保存在 `.runtime/analytics_special/quick_tests/`。

评测程序在 `Analytics/evaluation/`，默认读取项目根目录 `.env`。评测会调用模型 API；本次清理只检查数据加载与本地重绘，没有运行模型评测。新增结果默认写入 `.runtime/evaluation/`。

新增题目或修改内容前阅读 [MATHPALETTE_PROTOCOL.md](MATHPALETTE_PROTOCOL.md)。原题通过与 Special Pass / Collect 独立，不能相互代替。
