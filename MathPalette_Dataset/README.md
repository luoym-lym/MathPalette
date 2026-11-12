# MathPalette 正式数据集

共 323 题、1140 张 Special、1463 个图文样本，使用 1456 个不同 PNG 文件。同图可被多个样本引用，不能按图片哈希合并样本身份。

只保留当前普通 Collect：`collection.status="collected"`、`special_case=false`、不处于待复审状态。每题的 Special 槽位与该次 Collect 的 `slots`、`accepted_count` 完全一致，题号保留原样，不重新连续编号。

## 数据

- `dataset.jsonl`：每题一行。`id`、`branch`、`source_dataset`、`source_key`（如有）、`question`、`answer`、`answer_type`、`choices`（仅选择题）；`script` 指向唯一题目类；`image` 和 `image_sha256` 指向原图；`special_variants` 保存各槽位、图片及原 Pass 时间。
- `collection`：当前普通 Collect 状态、原 Collect 时间、数量和槽位。
- `approval`：原题历史批准者、用户原话及批准时间；不重新制造审核记录。
- `samples.jsonl`：每个输入一行。`id` 如 `Ana01_original`、`Ana01_C01`，`question_id` 始终指向原题；`variant_type` 为 `original` 或 `special`，`variant_id` 为 `null` 或 `C01`。同题原图和 Special 的题干、答案及选项相同。
- `image_manifest.jsonl`：每个 PNG 的字节 SHA-256、RGBA 指纹、尺寸、字节数和引用样本 ID。
- `metadata.json`：数量、来源分布、绘图环境及数据和绘图代码指纹。
- `SHA256SUMS`：本目录全部发布文件的校验和，不包含清单自身。

答案类型为 `choice`、`number`、`expression` 或 `text`。选择题答案只保存一个选项字母，其他答案保留原有精确值与单位。

```python
import json
from pathlib import Path

root = Path("MathPalette_Dataset")
samples = [json.loads(line) for line in (root / "samples.jsonl").read_text(encoding="utf-8").splitlines()]
sample = samples[0]
print(sample["id"], sample["question"], root / sample["image"])
```

## 绘图与推理

`questions/<题号>.py` 包含每题全部构图，使用 `drawing.py` 的共享工具，不依赖旧分支、JSON 场景、工作台或历史 recipes。所有正式图像已用这些代码重建。绘图及全量校验入口为 `draw.py`，接口见根目录 [绘图协议](../DRAWING_PROTOCOL.md)。

推理读取这里保存的 PNG，不在请求时重绘、缩放或压缩。`infer_deepseek.py` 与 `infer_qwen38_max_0902.py` 各自独立，只有标准库依赖；数据目录连同脚本和图片复制到其他位置后仍可推理。恢复绘图时保留目录名 `MathPalette_Dataset` 及其父目录的 Python 导入路径，或直接执行 `draw.py`。

详见 [DeepSeek 说明](INFERENCE.md)、[Qwen 说明](INFERENCE_QWEN38_MAX_0902.md)、[来源与许可](ATTRIBUTION.md)。
