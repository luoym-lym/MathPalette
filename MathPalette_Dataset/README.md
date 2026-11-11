# MathPalette 正式评测数据集

本目录是可独立复用的数据快照。仅纳入用户已 Collect、且当前没有特殊标识的题目；保留原题号。题干、答案、选项和图像来自当前正式分支数据，不使用 Collect 历史记录中的旧题干，也不重新绘图。

每个模型使用独立推理脚本：DeepSeek V4.1 Flash 使用 [`infer_deepseek.py`](infer_deepseek.py)（[说明](INFERENCE.md)），Qwen3.8-Max-0902 使用 [`infer_qwen38_max_0902.py`](infer_qwen38_max_0902.py)（[说明](INFERENCE_QWEN38_MAX_0902.md)）。两者分别保存接口提供的思考内容和最终回答；默认思考强度分别为 `max` 和 `xhigh`，请求总时限均为240秒，不显式发送输出 Token 上限。此前的 Batch 请求材料已清理。

## 本次范围

快照整理日期：2026-11-11。精确生成时间、源文件指纹和数据文件指纹见 `metadata.json`。

| 分支 | 题目 / 原图 | Special | 图文样本 |
| --- | ---: | ---: | ---: |
| Analytics | 84 | 216 | 300 |
| PlaneGeometry | 178 | 727 | 905 |
| SolidGeometry | 61 | 197 | 258 |
| 合计 | 323 | 1,140 | 1,463 |

筛选同时要求 `collection.json` 的顶层 `status` 和 `current.status` 都为 `collected`，`current.special_case` 缺省或为 `false`，且不是 `review_status=pending`。仅复制这些题的已 Pass 变体，并核对变体槽位与当前 Collect 的 `slots`、`accepted_count` 完全一致。本次排除 510 道带特殊标识的题及 683 道未 Collect 的题。

“原图”指分支 `dataset.jsonl` 的 `image`，即统一渲染的题目基准图；上游截图字段 `original_image` 没有被当作评测输入。本目录不收录 Base、待审候选、快测记录或历史评测分数。Special Pass 记录仅用于证明变体已保存，不构成新原题批准或有效诱导效果的声明。

## 文件与字段

- `dataset.jsonl`：每题一行，共 323 行；包含题干、答案、选项、基准图及 `special_variants` 列表。适合按题目配对分析。
- `samples.jsonl`：每个图文输入一行，共 1,463 行；适合模型推理和通用数据加载。
- `images/`：768×768 PNG，逐字节复制已冻结的图像。文件以 SHA256 命名，所有数据路径相对于本目录。
- `image_manifest.jsonl`：每个物理图像文件一行，包含文件大小、尺寸、SHA256 和对应样本 ID。
- `metadata.json`：筛选规则、统计、来源分布、生成时间和核心文件指纹。
- `provenance/`：仅包含入选题目的批准、Collect、recipes 和来源说明快照，及源路径/指纹映射。
- `attribution/`、`ATTRIBUTION.md`：保留的题源署名和许可通知。
- `infer_deepseek.py`、`INFERENCE.md`：DeepSeek V4.1 Flash 推理脚本与使用说明，运行结果写入项目 `.runtime/`。
- `infer_qwen38_max_0902.py`、`INFERENCE_QWEN38_MAX_0902.md`：Qwen3.8-Max-0902 独立推理入口与指定平台说明，使用独立的 Key 和运行目录。
- `SHA256SUMS`：发布数据、图像、推理脚本和说明文件的 SHA256 清单。

`dataset.jsonl` 的主要字段：

| 字段 | 含义 |
| --- | --- |
| `id` | 原正式题号，如 `Ana01`；不重新编号 |
| `branch` | `Analytics`、`PlaneGeometry` 或 `SolidGeometry` |
| `source_dataset` / `source_key` | 原题源名称及已有来源键 |
| `question` | 当前已批准的完整题干，逐字保留 |
| `answer` / `answer_type` | 当前标准答案及 `choice` / `number` / `expression` / `text` 类型 |
| `choices` | 仅选择题保留，字母到选项内容的原映射 |
| `image` / `image_sha256` | 基准图的本目录相对路径及文件指纹 |
| `special_variants` | 本题已 Collect 的 Special，包含样本 ID、`slot_id`、图片路径及指纹 |
| `collection` | 当前普通 Collect 的状态、时间及 `special_case=false` |

`samples.jsonl` 中的 `id` 是输入样本 ID，例如 `Ana01_original` 或 `Ana01_C01`；`question_id` 始终指向原题号。`variant_type` 为 `original` 或 `special`，`variant_id` 为 `null` 或 `C01` 等槽位。其余题干、答案、选项、图像字段与题目记录一致。同题原图和变体使用完全相同的题干及答案。

1,463 个样本对应 1,456 个不同 PNG。相同文件内容共享存储路径，但样本记录、题号和原图/变体身份全部保留。按样本 ID 匹配推理结果，不能按图片哈希合并样本。

## 读取

```python
import json
from pathlib import Path

root = Path("MathPalette_Dataset")
samples = [json.loads(line) for line in (root / "samples.jsonl").read_text(encoding="utf-8").splitlines()]
sample = samples[0]
image_path = root / sample["image"]
print(sample["id"], sample["question"], image_path)
```

## 复用与核验

本快照脱离原仓库也可以加载题干、答案和图片。`provenance/source_manifest.jsonl` 中的源路径以及原批准记录中的路径用于回到源仓库追溯，不是本快照的加载依赖；原批准指纹保持历史值，不因导出重算或冒称重新审核。

将本目录移动到其他位置时保持内部结构即可。快照不会自动跟随工作台状态变化；未来增加、重新 Collect、重新标记或改题后，应重新筛选生成新快照，不手工把未 Collect 或有特殊标识的题追加进来。不要仅凭相同题号混用不同快照的结果。

可在本目录内执行 `shasum -a 256 -c SHA256SUMS` 核验发布文件。题干、答案与 PNG 的源文件一致性、筛选范围及 PNG 完整解码已在导出时核验；推理脚本的 `--dry-run` 会重新检查冻结数据、Collect 状态、样本映射和全部图片指纹。
