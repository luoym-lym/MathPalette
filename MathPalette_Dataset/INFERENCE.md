# DeepSeek V4.1 Flash 推理

入口为 `infer_deepseek.py`，目前只适配 DeepSeek 官方 Chat Completions 实时接口。读取本目录的正式数据快照，默认每张图请求一次，保存接口提供的思考文本和最终回答，不执行答案判分。

2026-11-12 核对的官方模型 ID 为 **`deepseek-flash`**，当时对应 **DeepSeek-V4.1-Flash-1017**，支持图片和思考模式。`deepseek-flash` 是服务别名，不能把它当作永久冻结的检查点；脚本同时保存请求模型 ID、响应中的模型名称和服务提供的 `system_fingerprint`（如有）。

每个模型使用独立脚本。Qwen3.8-Max-0902 的指定平台入口见 [`INFERENCE_QWEN38_MAX_0902.md`](INFERENCE_QWEN38_MAX_0902.md)，使用独立的 Key 和输出目录。

## 准备 API Key

需要 Python 3.9 或更新版本，仅使用标准库，不需要安装 OpenAI SDK 或其他推理依赖。

在 DeepSeek 开放平台创建 API Key，在项目根目录现有 `.env` 中新增一行，保留其他内容：

```text
DEEPSEEK_API_KEY=你的DeepSeek官方APIKey
```

也可以通过环境变量 `DEEPSEEK_API_KEY` 提供。环境变量优先；脚本只读取 `.env`，不会修改文件，也不会把 Key 写进命令行参数、请求记录或结果。

## 运行顺序

在 MathPalette 项目根目录执行。

先校验全量数据，不联网、不需要 Key：

```sh
python3 -B MathPalette_Dataset/infer_deepseek.py --dry-run
```

先运行 6 个图文输入（每个分支一题的原图与第一张 Special），这一步会实际调用并计费：

```sh
python3 -B MathPalette_Dataset/infer_deepseek.py --smoke
```

确认输出后，运行全量：

```sh
python3 -B MathPalette_Dataset/infer_deepseek.py
```

全量运行会复用同一输出目录，跳过已经完整成功的 6 个输入，继续其余样本。运行中按 Ctrl+C 会关闭本地请求、保存已有部分响应；之后执行相同命令即可续跑。已完成的请求不重测，已使用的尝试次数不清零。

也可以用 `--limit 10` 选择前 10 个输入，或用 `--sample-id Ana01_original` 选择一个输入。`--smoke` 与这两个筛选选项不能同时使用。筛选只控制本次处理哪些样本，不改变整个实验的数据和推理设置。

## 图片与请求内容

脚本逐字节读取 `images/` 中的 PNG，以 Base64 形式直接传入 API，`image_url.detail` 固定为 `original`。运行前核验核心数据文件、Collect 状态、原图/变体映射和全部图片指纹；每次请求前再次核对该图指纹。不会重新绘图、缩放、压缩或转格式。

模型接收统一解题提示、正式题干和该输入的一张图片。标准答案、题源、Collect 状态、变体操作及诱导意图不进入请求正文。同题原图与 Special 使用相同题干和推理设置，每个请求都是独立的新对话。

请求记录保留题干、设置、本地图像路径、图片指纹及完整请求体指纹，不在记录中重复保存 Base64 图像。标准答案以 `reference_answer` 保存在本地推理结果中，方便后续另行判分。

## 预设与重试

默认预设如下，启动前即可查看或通过参数明确设置：

| 项目 | 默认值 / 参数 |
| --- | --- |
| API | `https://api.deepseek.com/chat/completions` |
| 模型 ID | `deepseek-flash` |
| 思考 | `thinking.type=enabled`，要求响应中有非空 `reasoning_content` |
| 思考强度 | `max`；`--reasoning-effort low/high/max` |
| 输出上限 | 不发送 `max_tokens`、`max_completion_tokens` 等上限参数，使用服务端默认值 |
| 流式 | `stream=true`，`stream_options.include_usage=true` |
| 图像细节 | `original` |
| top_p | `1.0`；不发送思考模式下无效的 temperature |
| 独立次数 | `--trials 1`，原图与 Special 相同 |
| 并发请求 | `--concurrency 4` |
| 请求速率 | `--rpm 60`，重试也计入 |
| 单次总时长 | `--timeout 240` 秒，可调低；包括持续收到 keep-alive 的情况 |
| 每个样本每轮的尝试上限 | `--max-attempts 3`，包含首次、超时、失败和续跑前已消耗的次数 |

默认输出路径为项目 `.runtime/inference/deepseek_v4_1_flash/`。可用 `--output-dir` 指定另一个运行目录。

2026-11-12 按用户最新要求改为 `max`、240秒总时限，并移除输出 Token 上限参数及 `--max-tokens` 选项。不设置参数不代表服务端无限输出；DeepSeek 官方文档规定，在 `max` 模式下未设置 `max_tokens` 时默认输出上限为128K。脚本不另设 `thinking_budget`。

推理预设、代码或冻结数据发生改变时，脚本拒绝混入同一运行目录。运行目录保存这些内容的签名。并发和 RPM 可在续跑时调整；重复次数、最大尝试数、超时和推理参数不能在原实验中悄悄变更。

网络失败、HTTP 408/409/425/429/5xx、未完整结束的流以及总时长超时可以在剩余预算内重试；每次都沿用完全相同的请求体与图像，保留独立尝试 ID、起止时间和已收到的内容。通过独立 HTTP 子进程和实际请求发出时间控制总时长，不只依赖 socket 读取间隔超时。

本地取消仅表示关闭本地连接，不能确认服务端已取消计算或停止计费。重复调用仍可能产生费用。达到尝试上限即停止该输入，续跑不会绕过上限。

模型数学答案错误不会触发重试。`finish_reason=length` 保存为 `truncated`，不会自动增加 token 上限后重跑。思考内容缺失、最终回答缺失或非暂时性 HTTP 错误会明确标记，并停止后续请求，避免把不符合接口要求的回复当作成功。已成功的其他输入保留。

## 输出文件

```text
.runtime/inference/deepseek_v4_1_flash/
├── run.json                         数据、代码、预设签名和本次/历次运行信息
├── results.jsonl                    已处理输入的汇总结果，每个样本每轮一行
├── summary.json                     进度、状态及尝试次数统计，不含正确率
└── samples/
    └── Ana01_original/
        └── trial_01/
            ├── result.json          此输入的持久化结果
            └── attempts/
                └── attempt_001_<唯一ID>/
                    ├── attempt.json         本次状态、请求、输出、用量和错误
                    ├── response.sse         原始流或超时前收到的部分流
                    ├── request_started.json 实际 HTTP 开始时间
                    ├── http_headers.json    状态码、请求ID等有限响应头
                    └── transport.json       已结束请求的传输状态
```

每次请求结束立即保存其 `attempt.json` 和 `result.json`。`results.jsonl` 与 `summary.json` 在本次运行结束或正常 Ctrl+C 后汇总生成；运行中也可直接查看各输入目录。意外中断后，会优先恢复已经下载完整的响应，不为已经收到的完整结果额外发请求。

`results.jsonl` 包含 `id`、`question_id`、`trial`、分支、原图/变体身份、图片指纹、`reasoning_content`、`content`、`usage`、`finish_reason`、响应模型、请求/响应 ID，以及各次尝试的状态和路径。失败输入同样有记录，已有的思考或回答片段保留，并以 `response_complete=false` 标识。请求中是否返回了思考和回答，与其数学答案是否正确是独立概念；本脚本不计算正确率。

这里的 `reasoning_content` 指 DeepSeek 对外提供的推理文本，不对它是否完整反映模型内部计算作额外声明。后续接其他模型时须另行区分推理文本、思考摘要和不返回推理的接口。

## 本地验证

```sh
python3 -B -m unittest dataset_tools.test_deepseek_inference -v
```

测试只启动本机 HTTP 模拟服务，使用测试 Key；覆盖流式思考/回答/用量保存、图片与答案隔离、持续 keep-alive 下的总超时、预算内重试、断点恢复、Ctrl+C、截断、缺少思考和错误响应等情况，不调用真实模型。

官方资料：[模型与当前版本](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)、[图像输入](https://api-docs.deepseek.com/zh-cn/guides/vision/)、[思考模式](https://api-docs.deepseek.com/zh-cn/guides/thinking_mode/)、[Chat Completions 参数与流式格式](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion/)。
