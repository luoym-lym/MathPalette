# MathPalette 工作说明

创建或修改本项目题目、Base 变体和数据流程前，阅读项目根目录的 [MATHPALETTE_PROTOCOL.md](MATHPALETTE_PROTOCOL.md)，并按题型阅读对应分支协议。

函数与解析几何数据在 `Analytics/fine_grained_dataset/`。Base 使用该数据集的 `dataset_generator/generate_base_variants.py` 自动生成，每题从 Base1～Base6 不放回抽取四种。Special 使用 `Analytics/fine_grained_special_workbench/`，等待用户 Pass / Collect。旧 A/B 人工工作台规范仅供历史回放。

平面几何使用 `PlaneGeometry/REDRAW_PROTOCOL.md` 和 `PlaneGeometry/dataset_generator/protocol.json`。立体几何使用 `SolidGeometry/REDRAW_PROTOCOL.md` 和 `SolidGeometry/dataset_generator/protocol.json`，须分别冻结三维几何、投影与可见性。两个几何分支均提供重绘器，尚未启用 Base / Special 流程；只有图片的重绘样例不占正式题号。

所有分支（包括函数与解析几何）均按用户逐题审核，只有明确通过题号后才加入根目录正式 `question_bank.jsonl`。平面、立体正式题写入分支 `dataset.jsonl`；Analytics 的原 `fine_grained_dataset/dataset.jsonl` 保持冻结候选输入，正式题另用 `approved_dataset.jsonl`。未通过题保留在分支 `pending_dataset.jsonl` 和根目录 `pending_questions.jsonl`，全部候选在 `question_candidates.jsonl`。不能把 Agent 检查、数学核验或 Special 变体 Pass/Collect 当成原题通过。使用 `dataset_tools/question_review.py` 记录用户原话和当前内容指纹，再运行导入目录 `build_catalog.py` 同步索引。已通过内容改变时待重新审核。
