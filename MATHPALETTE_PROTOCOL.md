# MathPalette 协议入口

版本：2026-10-10。创建或修改题目、重绘图及变体前，先按题型阅读下列分支协议。

| 题型 | 协议与机器配置 | 当前流程 |
| --- | --- | --- |
| 函数与解析几何 | [Analytics 制作协议](Analytics/MATHPALETTE_PROTOCOL.md) | 冻结候选，用户逐题通过后正式入库；自动 Base；Special 另由用户 Pass / Collect。 |
| 平面几何 | [重绘协议](PlaneGeometry/REDRAW_PROTOCOL.md)、[机器配置](PlaneGeometry/dataset_generator/protocol.json) | 独立重绘，用户逐题通过后正式入库；Base / Special 尚未启用。 |
| 立体几何 | [重绘协议](SolidGeometry/REDRAW_PROTOCOL.md)、[机器配置](SolidGeometry/dataset_generator/protocol.json) | 冻结三维几何、投影和显隐，用户逐题通过后正式入库；Base / Special 尚未启用。 |

各分支的坐标、几何语义和渲染器分别维护；不能把函数图的网格、刻度操作直接套入几何图。只有图片的材料可以制作 `redraw_example`，不推测题干、答案或真实来源数据集，也不占用正式题号。

函数、解析几何、平面和立体几何均须用户明确通过对应题号后，才加入根目录正式 `question_bank.jsonl`。所有候选保存在 `question_candidates.jsonl`，待审题在 `pending_questions.jsonl`。平面、立体分支 `dataset.jsonl` 仅包含已通过题目；Analytics 保留原 `fine_grained_dataset/dataset.jsonl` 作为 Base/Special 的冻结候选输入，正式题使用 `approved_dataset.jsonl`，待审题使用 `pending_dataset.jsonl`。用户审核记录在 `imports/mathverse_vision_dominant/question_user_reviews.json`，绑定当前题干、答案及绘图内容；内容改变后待重新审核。Agent 检查、答案核验、原题用户通过和 Special Pass/Collect 分别记录，不能相互代替。

函数数据与当前工作台分别在 `Analytics/fine_grained_dataset/`、`Analytics/fine_grained_special_workbench/`。旧 A/B 人工工作台仅用于历史回放。分支说明见 [Analytics](Analytics/README.md)、[PlaneGeometry](PlaneGeometry/README.md)、[SolidGeometry](SolidGeometry/README.md)。
