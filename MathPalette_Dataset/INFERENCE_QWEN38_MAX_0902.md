# Qwen3.8-Max-0902 推理

入口为 `infer_qwen38_max_0902.py`，固定使用模型 ID `qwen3.8-max-0902`，默认平台为用户指定的 `https://maas.qianwenaiapi.com/compatible-mode/v1`。最终请求地址为 `https://maas.qianwenaiapi.com/compatible-mode/v1/chat/completions`。

每个新模型使用新的独立脚本。本入口不依赖、不改写 DeepSeek 脚本，使用独立 API Key 和运行目录。仅做推理，不计算正确率。

## API Key

需要 Python 3.9 或更新版本，仅使用标准库。

项目根目录现有且由 Git 跟踪的 `.env` 中使用以下独立变量，保留其他配置：

```text
QWEN_38_MAX_0902_API_KEY=该平台的APIKey
```

本次用户通过密钥输入框提供的 Key 已保存到这个变量。脚本优先读取同名环境变量，其次读取 `.env`。不会把 Key 放到命令行、请求记录或结果中。DeepSeek 的 Key 仍使用 `DEEPSEEK_API_KEY`。

## 运行

在项目根目录执行。先离线核验全部冻结数据，不联网、不需要 Key：

```sh
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py --dry-run
```

运行三个分支各一题的原图与第一张 Special，共6个输入；此命令会实际调用模型并计费：

```sh
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py --smoke
```

全量运行1,463个输入，自动跳过同一目录中已经完整成功的请求：

```sh
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py
```

也可以选择 `--limit 10` 或 `--sample-id Ana01_original`；它们不能与 `--smoke` 同时使用。并发可通过 `--concurrency` 调整，速率通过 `--rpm` 调整。修改实验的题目、代码或推理预设时，需要新的 `--output-dir`，避免把不同设置的结果混在一起。

## 固定请求与默认参数

| 项目 | 默认值 / 行为 |
| --- | --- |
| 模型 | `qwen3.8-max-0902` |
| 开启思考 | 请求顶层 `enable_thinking=true` |
| 思考力度 | `reasoning_effort=xhigh`；可选 `--reasoning-effort low/medium/xhigh` |
| 思考预算 | 不发送 `thinking_budget`，避免与 effort 冲突 |
| 输出 Token 上限 | 不发送 `max_tokens`、`max_completion_tokens`、`max_output_tokens`，由服务端采用默认值 |
| 采样 | 不发送 `temperature` 或 `top_p`，采用平台默认值 |
| 流式 | `stream=true`、`stream_options.include_usage=true` |
| 图片 | 本地冻结 PNG 原字节 Base64，不发送 `detail`，服务端按自身策略处理 |
| 并发 | `--concurrency 4` |
| 请求速率 | `--rpm 60`，包含重试 |
| 请求总时限 | `--timeout 240` 秒，可调低；持续 keep-alive 不会延长总时限 |
| 独立次数 | `--trials 1`，原图与 Special 相同 |
| 每个输入每轮尝试上限 | `--max-attempts 3`，含首次和续跑前已消耗的尝试 |
| 输出目录 | `.runtime/inference/qwen3_8_max_0902/` |

HTTP 请求直接发送顶层 `enable_thinking` 和 `reasoning_effort`，不发送 SDK 的 `extra_body` 包装，也不发送 DeepSeek 的 `thinking` 对象。

2026-11-12 核对的千问官方参数文档中，Qwen3.8-Max-0902 支持 `low`、`medium`、`xhigh`；显式 `xhigh` 对应思考预算262,144 tokens。`reasoning_effort` 与 `thinking_budget` 不能同时设置。本脚本按用户要求只传 `xhigh`。不传输出上限不代表无限输出，平台的默认值、上下文和模型固有限制仍适用。

上述参数格式根据千问官方文档实现；指定网关的参数透传、实际后端版本与是否返回思考内容尚未通过真实调用验证。脚本记录请求模型、返回模型及 `system_fingerprint`（如有）；配置中 `gateway_model_mapping_verified=false`，不把请求快照名称当作已验证的后端身份。

## 数据、思考内容与续跑

运行前核验正式快照的核心文件指纹、普通 Collect 条件、原图/变体映射及全部1,456个 PNG；每次请求前再次核验该图指纹。直接读取冻结 PNG，不重绘、缩放或压缩；服务端的图像预处理由平台决定。

每个请求是独立新对话，仅发送统一解题提示、原题题干和一张图。同题原图与 Special 使用相同题干和设置。标准答案及变体操作不进入请求，标准答案只作为本地 `reference_answer` 保存。

分别保存接口提供的 `reasoning_content` 与最终 `content`，以及用量、返回模型、请求 ID、原始 SSE 和所有尝试。只有正常结束、两个字段都非空才算完整成功；不将最终回答中的解题说明冒充接口思考字段。`reasoning_content` 表示接口提供的推理文本，不额外声称它完整反映模型内部计算。

输出结构与 [DeepSeek 输出文件说明](INFERENCE.md#输出文件)一致，但位于独立的 `.runtime/inference/qwen3_8_max_0902/`：

- `run.json`：代码、数据、推理预设签名和各次启动信息。
- `results.jsonl`：每个输入每轮一行，保留思考、回答、用量、状态及尝试记录。
- `summary.json`：进度与尝试次数，不计算正确率。
- `samples/<样本ID>/trial_01/`：持久化结果及各次请求的原始流、起止时间、传输状态。

超时从 HTTP 实际发出时计时，通过独立子进程控制总时长。超时、网络失败、暂时性 HTTP 错误或未结束的流可在剩余预算内重试，沿用完全相同的请求与图像。每次尝试单独保存，续跑不清零；已完成的另一轮不重测。

Ctrl+C 会关闭本地连接并保留已收到的片段；重新执行相同命令即可续跑。关闭本地连接不代表服务端已停止计算或计费。缺少思考或回答、认证错误等会明确失败并停止后续调用；数学错答和输出截断不会触发重测或自动改参。

## 离线验证

```sh
python3 -B -m unittest dataset_tools.test_qwen38_max_0902_inference -v
```

测试仅访问本机模拟 HTTP/SSE 服务，使用测试 Key，覆盖指定路径、Qwen 请求字段、无输出上限、思考与回答保存、超时重试、续跑、Ctrl+C、Key 隔离和冻结图像核验。离线测试通过不代表指定网关已完成联调。

官方参考：[模型与快照](https://help.aliyun.com/zh/model-studio/qwen3-8-max)、[思考模式](https://help.aliyun.com/zh/model-studio/deep-thinking)、[OpenAI 兼容参数](https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions/)。
