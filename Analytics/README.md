# Analytics：函数与解析几何

现有 Ana01～Ana20 的数据、自动 Base、人工 Special、评测脚本及评测结果统一放在此目录。完整流程见 [MATHPALETTE_PROTOCOL.md](MATHPALETTE_PROTOCOL.md)。

原题统一采用用户逐题明确通过后入库，函数与解析几何也适用。`fine_grained_dataset/dataset.jsonl` 保留为冻结候选和 Base/Special 输入；正式原题在同目录 `approved_dataset.jsonl` 及项目根目录 `question_bank.jsonl`，待审题在 `pending_dataset.jsonl`。所有原图、Base 和既有 Special 人工记录保留；Agent 检查与 Special Pass/Collect 不代替原题通过。见 [审核进度](../imports/mathverse_vision_dominant/question_review_progress.json)。

## 目录

| 目录 | 用途 |
| --- | --- |
| `fine_grained_dataset/` | 原图、题目脚本、Base / Special、重绘与历史归档 |
| `fine_grained_special_workbench/` | 当前人工 Special 工作台，默认端口 8767 |
| `special_variant_workbench/` | 历史工作台；其 `construct_dataset` 输入已不在当前项目，保留供历史参考 |
| `val_script/` | 原图 / Base / Special 评测脚本和既有 trace、报告 |
| `migration/` | 2026-10-09 搬迁前文件哈希与搬迁核对记录 |

## 使用

在 **MathPalette 目录**执行：

```powershell
python -B Analytics/fine_grained_dataset/dataset_generator/prepare_question.py --pending
python -B Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py check --redraw
python -B Analytics/val_script/evaluate.py --help
python -B Analytics/val_script/evaluate_variants.py --help
python -B Analytics/val_script/evaluate_special.py --help
```

双击 `fine_grained_dataset/start_special_workbench.cmd` 启动当前工作台。备份时将数据集与当前工作台一起保留。

评测默认读取 **MathPalette 根目录的 `.env`**，仍支持 `--env-file`。旧 trace 文件原样保留；只有数据集从旧目录搬到当前目录且数据、图片、recipes 和评测配置均不变时，续跑才接受路径变化，并记录路径迁移历史。实际评测会调用模型 API；本次搬迁核对仅加载数据、重绘和测试，不发起模型请求。
