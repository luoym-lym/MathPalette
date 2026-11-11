# Qwen3.8-Max Batch 文件

这些文件仅从 `../samples.jsonl` 转换请求格式，不执行推理、上传、重试、判分或其他正式评测流程。

## 本轮不使用 Batch

2026-11-11 用户明确本次评测需要思考过程。百炼官方说明，Batch 即使设置 `enable_thinking=true`，结果仍不包含 `reasoning_content`。因此以下文件虽然格式与图片地址已经核验，**不适用于本轮需要思考过程的正式评测，请勿据此继续提交本轮任务**。

Qwen 应改用普通按量实时 API，启用思考模式，分别保存服务返回的 `reasoning_content` 和 `content`。通过程序并发处理全部样本仍然可行，不需要逐题人工操作。最终回复中的解题说明与接口单独返回的思考内容应区分保存。数据快照、样本 ID 和 OSS 图片均可复用；本轮暂不修改评测脚本。

来源：[Batch 返回字段限制](https://help.aliyun.com/zh/model-studio/batch-inference)、[实时 API 思考内容字段](https://help.aliyun.com/zh/model-studio/deep-thinking)。

## 此前准备的格式文件

2026-11-11 已将图片地址替换为 `https://mathpalette-eval.oss-cn-beijing.aliyuncs.com/mathpalette/images/<SHA256>.png`，逐张以不带签名的公网 GET 下载全部 1,456 个 PNG，并确认 SHA256 与本快照一致。文件不依赖临时签名，后续仍需保持图片访问权限至批任务结束。

- `ready/all.jsonl`：全部 1,463 条图文请求，仅保留此前准备的 Batch 格式。
- `ready/smoke.jsonl`：此前准备的 6 条 Batch 接口检查请求。
- `ready/originals.jsonl`、`ready/specials.jsonl`：分别为 323 条原图与 1,140 条 Special 的 Batch 格式。
- `ready/manifest.json`、`ready/SHA256SUMS`：本轮地址、核验时间、文件数量及指纹。

这些文件已经完成 URL 替换，暂不提交本轮评测。全量文件与分开文件、6 条检查文件存在重叠。完整图片下载核验及超时重试记录在源仓库 `.runtime/qwen_oss_image_verification_20261111*.json`；本代理尚未向模型发送任何请求。

## 已准备的文件

| 文件 | 请求数 | 内容 |
| --- | ---: | --- |
| `templates/all.template.jsonl` | 1,463 | 本正式数据集的全部图文输入 |
| `templates/originals.template.jsonl` | 323 | 基准图输入 |
| `templates/specials.template.jsonl` | 1,140 | Special 输入 |
| `templates/smoke.template.jsonl` | 6 | 每分支一题的原图与第一张 Special，供上传后检查接口 |
| `images.zip` | 1,456 个 PNG | 仅图片，解压后是 `images/` 目录 |
| `prepare_urls.py` | — | 将占位图片地址替换为真实 HTTPS 前缀 |
| `manifest.json` | — | 模型、请求参数、模板数量与指纹 |

**模板中的域名是 `replace-image-host.invalid`，目前不能直接提交。** 正式数据文件 `../dataset.jsonl`、`../samples.jsonl` 带有标准答案，用于本地加载与后续判分，不要把它们当作模型请求文件上传。

每个样本对应一条请求，`custom_id` 与 `../samples.jsonl` 的 `id` 一致。模型仅收到统一解题提示、正式题干和该样本的一张图片；标准答案、来源、Collect 状态、变体操作和诱导意图均不进入请求正文。题目已有的选择题选项保留在原题干内。

统一参数为 `model="qwen3.8-max"`、`enable_thinking=true`，后者直接位于 `body` 内，与 `model` 同级。采样参数和 token 上限未指定，使用服务端默认值；本轮只做数据整理，未决定正式评测的重复次数、预算或判分策略。Batch 结果不返回 `reasoning_content`。

`all` 恰好由 `originals` 和 `specials` 合成，`smoke` 是其中 6 条的子集。正式提交可选 `all`，也可分别提交 `originals` 与 `specials`；同一轮不要重复提交这些相互重叠的文件。

## 图片怎样处理

1. 使用阿里云 OSS 或能从公网直接访问的 HTTPS 图片存储。推荐与本次 Batch 使用同一北京地域。按文件原样上传 `../images/`，或者先解压 `images.zip` 再上传其中的 `images/` 目录。不要把 ZIP 压缩包本身当作模型图片 URL。
2. 假设选择的图片根前缀为 `https://YOUR-BUCKET.oss-cn-beijing.aliyuncs.com/mathpalette`，对象路径应为 `mathpalette/images/<SHA256>.png`。保留 `images/` 这一层；下方命令的前缀不包含最后的 `/images`。
3. 图片链接须能直接获取 PNG，不需要登录、Cookie 或额外请求头；保持可访问状态直至批任务全部结束。只需提供图片访问路径，不必公开整个桶。当前替换工具按统一 URL 前缀工作；若使用私有桶逐图签名 URL，应另行生成 URL 映射，且有效期须覆盖任务执行窗口。
4. 保留 PNG 原始字节、768×768 尺寸、颜色、线型和透明度设置。上传和 CDN 服务不要自动缩放、转 JPEG/WebP 或应用图片处理参数。应返回 PNG 内容，建议 `Content-Type: image/png`。上传后下载核对 SHA256，预期值在 `../image_manifest.jsonl`。
5. 仅上传图片目录即可。标准答案和本地批准/Collect/recipes 文件不需要放到图片存储。

## 替换 URL，生成可提交的文件

在 MathPalette 项目根目录运行，将下方地址替换为自己的真实图片根前缀：

```sh
python3 MathPalette_Dataset/qwen_batch/prepare_urls.py \
  --image-base-url 'https://YOUR-BUCKET.oss-cn-beijing.aliyuncs.com/mathpalette'
```

Windows 可将 `python3` 换为 `python`，并把命令写成一行。

工具在 `qwen_batch/ready/` 生成 `all.jsonl`、`originals.jsonl`、`specials.jsonl`、`smoke.jsonl`。原模板保持不变。若输出目录已存在且非空，使用 `--output-dir` 指向一个新的目录，避免混用先前的 URL。脚本只执行本地替换与格式校验，不验证远程对象已经上传，也不会向模型提交请求。

## Batch 控制台操作参考（不适用于本轮）

使用**华北2（北京）**地域的百炼 Batch 文件任务。官方批量总览与模型专页对新加坡支持情况存在不一致，本包按双方均明确支持的北京地域准备。使用 `qwen3.8-max`；模型专页把 `qwen3.8-max-0902` 快照列为不支持 Batch，暂不替换为该快照 ID。

图片上传并确认可读取后，可先提交 `ready/smoke.jsonl` 检查接口、图片读取和返回格式，再选择全量或分开的文件。每个 Batch 文件是 UTF-8 JSONL，单行一个请求；`method="POST"`、`url="/v1/chat/completions"`。这些模板均低于官方文件上限（50,000 请求、500 MB），并按更保守的每行 1 MB 上限校验。

批任务结束后及时下载成功结果与错误文件，用 `custom_id` 关联 `../samples.jsonl`。模型回答、失败情况和服务端截断的实际处理规则留待正式评测流程确定；本轮尚未创建任何批任务。

官方资料（2026-11-11 核查）：[Batch 文件格式与图片 URL 要求](https://help.aliyun.com/zh/model-studio/batch-inference)、[Qwen3.8-Max 模型能力与快照](https://help.aliyun.com/zh/model-studio/qwen3-8-max)。
