# MathPalette

本仓库仅保留 **已 Collect、没有特殊标识且不处于待复审状态**的正式题目，以及绘图和评测所需的代码。题号沿用原编号。

| 分支 | 题目 | Special | 图文样本 |
| --- | ---: | ---: | ---: |
| Analytics | 84 | 216 | 300 |
| PlaneGeometry | 178 | 727 | 905 |
| SolidGeometry | 61 | 197 | 258 |
| 合计 | **323** | **1140** | **1463** |

所有 PNG 均以当前题目类重新绘制的结果为准。每题一个 Python 类，`draw()` 绘制原图，`draw(variant="C01")` 绘制该题 Special。三个分支分别使用 `ANALYTICS`、`PLANE`、`SOLID` 配置，共用简单的基础图元工具。

## 目录

```text
MathPalette_Dataset/
  dataset.jsonl                  每题一行：题干、答案、图片、Special 和 Collect
  samples.jsonl                  每张图一行：直接用于模型推理
  images/                        按 SHA-256 去重保存的正式 PNG
  questions/                     323 个题目类，包含原图和 Special 的构图
  drawing.py                     公共画布、图元、文字、投影、导出
  draw.py                        单题绘图、全量重建和校验
  infer_deepseek.py               DeepSeek 独立推理入口
  infer_qwen38_max_0902.py        Qwen 独立推理入口
  image_manifest.jsonl           图像与样本的映射、尺寸和指纹
  metadata.json / SHA256SUMS      数据和可运行代码的完整性核验
  attribution/                   保留的来源许可通知
  README.md / INFERENCE*.md       数据字段与运行说明
DRAWING_PROTOCOL.md               绘图协议
requirements.txt                  固定绘图依赖
tests/                           数据与本地模拟接口测试
```

未 Collect 或带特殊标识的题、旧分支目录、工作台、历史绘图器、迁移归档、重复索引、来源截图、论文草稿、旧实验材料与运行缓存已清理。历史用户批准文字与时间、普通 Collect 时间和已 Pass 槽位的信息保留在正式题目记录中；它们不代表本轮重新进行人工审核。

## 环境与校验

绘图环境为 Python 3.13.9，NumPy 2.5.3、Matplotlib 3.11.2、Pillow 12.3.0，FreeType 2.14.3。

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B MathPalette_Dataset/draw.py check
.venv/bin/python -B MathPalette_Dataset/draw.py check --redraw
```

`check --redraw` 会对全部 1463 张图重新绘制，要求与正式 PNG 的字节指纹一致。若修改绘图代码并明确要更新正式图像，执行：

```sh
.venv/bin/python -B MathPalette_Dataset/draw.py rebuild
```

重建同步图片、索引、元数据和校验清单，清理不再引用的 PNG。题干、答案、题号和 Collect 信息不会由重建推断或批准。

## 绘图

```sh
.venv/bin/python -B MathPalette_Dataset/draw.py draw Ana01
.venv/bin/python -B MathPalette_Dataset/draw.py draw Plane25 --variant C01
.venv/bin/python -B MathPalette_Dataset/draw.py draw Solid67 --output .runtime/Solid67.png
```

默认输出写 `.runtime/reproduced/`。题目脚本也可直接执行。详细工具接口见 [绘图协议](DRAWING_PROTOCOL.md)，数据读取见 [数据集说明](MathPalette_Dataset/README.md)。

## 评测推理

每个模型使用独立脚本。先执行不联网的全量预检：

```sh
python3 -B MathPalette_Dataset/infer_deepseek.py --dry-run
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py --dry-run
```

去掉 `--dry-run` 后才发送模型请求。两者直接读取本地正式 PNG，使用相同的题干前缀，分别保存接口返回的 `reasoning_content`、最终回答、用量和原始流；不自动判分或因数学错答重测。结果写 `.runtime/inference/`，数据或代码变化后应使用新的运行目录。

默认 DeepSeek 为 `max`，Qwen 为 `xhigh`；请求总时限 240 秒，每个样本每轮最多 3 次尝试，续跑不清零，不发送输出 Token 上限。API Key 继续从根目录现有 `.env` 或对应环境变量读取。配置与命令见 [DeepSeek](MathPalette_Dataset/INFERENCE.md)、[Qwen](MathPalette_Dataset/INFERENCE_QWEN38_MAX_0902.md)。

运行不调用外部模型的回归测试：

```sh
.venv/bin/python -B -m unittest discover -s tests
```

来源与许可见 [署名说明](MathPalette_Dataset/ATTRIBUTION.md)。
