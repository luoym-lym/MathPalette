# Qwen3.8-Max-0902 推理

独立入口 `infer_qwen38_max_0902.py`，模型 ID `qwen3.8-max-0902`，默认平台 `https://maas.qianwenaiapi.com/compatible-mode/v1`。请求地址追加 `/chat/completions`，顶层发送 `enable_thinking=true`、`reasoning_effort=xhigh` 和流式参数，不发送 temperature、top_p 或图像 detail。

网关是否透传参数、实际后端版本及思考字段以真实响应为准；保留 `gateway_model_mapping_verified=false`，不将请求的模型名冒充已验证的后端身份。

根目录现有 .env 使用独立的 `QWEN_38_MAX_0902_API_KEY`，同名环境变量优先。默认输出 `.runtime/inference/qwen3_8_max_0902/`。

```sh
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py --dry-run
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py --smoke
python3 -B MathPalette_Dataset/infer_qwen38_max_0902.py
```

## 请求与结果

先运行 `--dry-run` 做全量离线校验，不需要 Key、不发送请求。去掉该参数才执行付费模型调用；也可用 `--smoke` 选三个分支各一对原图和 Special，共6个输入。`--limit` 和 `--sample-id` 可选择输入。

脚本发送正式 PNG 原字节与题干，不在请求时重绘、缩放或压缩，不发送标准答案、题源、批准信息或变体意图。同题原图和 Special 使用相同指令、相同设置，每个请求是独立对话。唯一 user 文本为：

```text
Please solve the problem step by step and put your answer in one "\boxed{}".
{question}
```

这是用户确认的 lmms-eval MathVision 通用指令，来源固定为提交 `c26b6b2713c3ec155962ff990f956bf78e0efe45` 的 `lmms_eval/tasks/mathvision/utils.py`；不加 system 消息或选择题特例。

默认总时限240秒、每个输入每轮最多3次尝试、独立次数1、并发4、RPM 60。不发送输出 Token 上限或显式 thinking_budget。超时从实际发出 HTTP 请求计算，持续 keep-alive 不延长时限。重试沿用相同图片、题干与设置，保存各次 ID、起止时间、状态和部分响应，续跑不会清零预算。

`reasoning_content`、最终 `content`、用量、返回模型、请求 ID、原始 SSE 和各次尝试分别保存。仅正常结束且推理和回答字段非空才算完整成功；缺失推理、截断或错误会如实标记。模型数学错答不触发重试；不自动判分，不更改预设追求正确答案。

输出包含 `run.json`、`results.jsonl`、`summary.json` 和 `samples/<样本ID>/trial_01/attempts/`。成功输入在续跑时跳过，其他输入沿用剩余尝试预算。数据、代码或固定预设变化后需要新的运行目录，避免混用结果。

Ctrl+C 会保存已有内容并关闭本地请求；本地取消不表示服务端已撤销计算或计费。API Key 仅从环境变量或现有 .env 读取，不写入请求记录、结果或命令行。

推理只依赖 Python 3.9+ 标准库。脚本、JSON 与图片可独立复制使用；无需绘图依赖或旧工作台。离线验证不代表真实接口已验证。默认入口和参数按用户已确认设置保留，不在整理数据时调用外部模型。
