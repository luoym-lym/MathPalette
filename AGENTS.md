# MathPalette 工作说明

修改前阅读根目录 README.md 和 DRAWING_PROTOCOL.md。

- 唯一正式数据目录为 MathPalette_Dataset/。仅保留普通 Collect：collected、special_case=false、不待复审；Special 必须与当前 Collect 槽位完全匹配。当前323题、1140张Special、1463个图文样本。
- 保留原题号，不为补齐编号恢复已删除题目。不得把未 Collect、特殊标记、候选或普通 Special Pass 当成正式题。
- 每题一个 Python 类，draw() 和 draw_C01() 等方法直接调用 drawing.py 的共享工具。不要恢复来源 renderer、工作台、迁移归档或旧分支。
- 题干、答案、选项或数学构造的内容修改仍须用户确认；保留已有批准文字、时间、Collect 和 Pass 信息，不伪造审核。
- 用户已明确本次以新代码绘制的图片为准。用 draw.py rebuild 同步图像、索引、metadata.json、SHA256SUMS，用 check --redraw 检查全量复现；不能只修改图片或一份索引。
- 新增模型使用独立脚本。当前 DeepSeek 默认 max、Qwen 默认 xhigh，总时限240秒，每个样本每轮最多3次尝试，续跑不清零，不设输出 Token 上限。直接发送本地 PNG，保存接口 reasoning_content、最终 content、用量、原始流和每次尝试。没有返回推理内容时如实标记，不用最终回答冒充。
- 所有输入统一前缀：Please solve the problem step by step and put your answer in one "\boxed{}".，接一个换行和正式题干，不加 system 消息或选择题特例。
- 根目录 .env 按用户要求继续由 Git 跟踪，不迁移、不修改跟踪状态、不泄露密钥。不修改 .git 历史。
- 临时图、测试及推理结果写 .runtime/，不纳入正式数据。不要恢复旧实验日志、分数或历史候选。
- 完成改动后执行正式数据校验和适用测试；离线预检或本机模拟接口测试不能描述成真实模型调用。
