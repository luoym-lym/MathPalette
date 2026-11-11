# MathPalette 工作说明

创建或修改题目、变体和数据流程前，阅读根目录 `MATHPALETTE_PROTOCOL.md` 以及对应分支协议。

仅用户明确确认的原题进入正式数据。三个分支 `dataset.jsonl` 都只包含正式题；根目录 `question_bank.jsonl` 是 `dataset_tools/catalog.py build` 生成的汇总。不得恢复旧候选清单或把 Special Pass/Collect 当成原题通过。

正式题号统一：当前为 Ana01～Ana590、Plane01～Plane599、Solid01～Solid327（共 1516 题，均连续无空缺）。Analytics 的 DynaMath 使用 Ana01～Ana20，MathVerse 使用 Ana21～Ana45 与 Ana47～Ana70（原 Ana53～Ana71 已按用户要求前移为 Ana52～Ana70 以消除空缺），MathVista 使用 Ana46 与 Ana71～Ana131（2026-11-08 合入 61 道新增 MathVista 题，保留既有 Ana46，详见 `provenance/analytics_renumber_and_mathvista61_20261108.json`）；Solid17～Solid25 来自 SOLIDGEO。Plane140～Plane490 与 Solid79～Solid248 来自 MathVision。Plane491～Plane511 与 Solid249～Solid257 为 Author Designed。Plane512～Plane529 与 Solid258～Solid263 为用户授权直接入库的24道拓展题。Plane530～Plane599 与 Solid264～Solid288 为用户于2026-11-05批准入库的95道同题型拓展原题，父题映射见 `provenance/author_extensions95_20261105.json`；本轮未创建 Specialvar 或 Collect。所有原创题来源按用户最新要求统一为 `Author Designed`，历史原话保留。本次 We-Math2.0-Standard 为 Ana132～Ana546 与 Solid289～Solid327，共454题，15道排除题保留不入库。批量授权与来源说明恢复见 `provenance/wemath/README.md`，不代表逐题人工批准或 Special Pass/Collect。题源以各分支 `dataset.jsonl` 为准。新增题号继续递增，不建立另一套 formal/candidate 编号。

2026-11-11 用户明确批量授权新增 Analytics 原创原题 Ana547～Ana566（Author Designed）及每题 C01；由主代理执行原题入库与 Special Pass，不代表逐题人工审核，不执行 Collect。设计、批量授权与执行凭据见 `provenance/analytics_author_special20_20261111.json`。

2026-11-11 用户以“放进去吧”明确批准将已交付的 6 道 Analytics 新原创题 Ana567～Ana572 加入 Author Designed，沿用“设计的变体直接pass就好”的指令保存 7 份 Special（Ana567 为 C01、C02，其余每题 C01）。Pass 仅代表授权保存；本轮视觉实测只有 Ana567/C02 达到预设双样本条件，不代表其他变体有效或逐题人工审核。未执行 Collect。授权、设计与事务凭据见 `provenance/analytics_author_visual6_20261111.json`。

2026-11-11 用户要求“再进行一轮”，继续此前 Author Designed 入库与“设计的变体直接pass就好”的授权，新增 Ana573～Ana578 六道原题及七份 Special（Ana577 为 C01、C02，其余每题 C01）。本轮参考已 Collect 题目；Ana576/C01、Ana578/C01 达到预设双样本视觉误读条件，Ana577 两份变体均一对一错，Ana573～Ana575 对照因连接失败未完整，效果未验证。Pass 不代表逐题人工审核或稳定诱导效果；未执行 Collect。凭据见 `provenance/analytics_author_collect6_20261111.json`。

2026-11-11 用户要求“你从已经收录的题目里面进行扩展就好”“可以多做一些”，继续 Author Designed 入库和直接 Pass 授权，新增 Ana579～Ana590 共12道母题扩展，每题C01，母题为Ana576、Ana578、Ana548、Ana567。Ana579、Ana581、Ana582、Ana588、Ana590 的C01达到本轮双样本条件（Ana581有附带FINAL矛盾，已保留说明）；Ana580原图对照失误，变体未测，其余未达条件。未执行Collect，不冒称逐题人工审核或稳定有效。母题映射、授权与实测凭据见 `provenance/analytics_author_extensions12_20261111.json`。

用户通过原话、时间及当前内容指纹在 `provenance/approvals.json`。改题干、答案、绘图输入或原图时，须用户重新确认后更新记录。迁移仅在题干、答案及像素一致的核验通过后更新路径/编号指纹，保留旧指纹和原审核时间。

使用 `dataset_tools/question_review.py 分支 题号 --instruction "用户明确通过原话"` 保存审核并同步索引；不得用修改指令、数学检查或本工具执行成功代替用户批准。

三个分支的 Base 均未启用。Special 分别使用各自 `workbench/`，由用户 Pass / Collect。不得伪造通过记录。

2026-11-11 用户明确要求将可复用的正式评测数据集放入独立目录，并规定“正式的数据集仅包含collect且没有特殊标识的题目”。发布快照位于 `MathPalette_Dataset/`：筛选 `collection.json` 顶层及 `current.status` 均为 `collected`、`current.special_case` 缺省或为 false，排除待复审题；只附带与该次普通 Collect 的槽位完全匹配的已 Pass Special。当前快照为323题、1140张Special、1463个图文样本。保留原正式题号及已批准内容；三个分支源库与原批准记录继续作为追溯依据。更新发布集须重新按当前状态筛选，不把未 Collect 或特殊标记题追加进来。

2026-11-11 用户进一步明确评测需要思考过程（“因为我要思考过程啊”）。后续模型接入须核实图像输入和对应接口实际返回的推理字段，并保存接口提供的思考内容与最终回答；须区分推理文本、思考摘要和未返回思考内容，不能把开启 thinking 参数当作已获取思考过程。2026-11-12 用户明确要求编写推理脚本、清理此前 Batch 材料，并指定先适配 DeepSeek V4.1 Flash，后续再拓展。入口为 `MathPalette_Dataset/infer_deepseek.py`，官方 API 模型 ID 为 `deepseek-flash`（当时文档版本 DeepSeek-V4.1-Flash-1017，别名不视为永久固定快照）。直接发送本地冻结 PNG，保存 `reasoning_content`、`content`、用量、原始流和各次尝试；结果写 `.runtime/`。正式推理每次请求按最新指令默认240秒总时长、每个样本每轮最多3次尝试，续跑不清零；重试不改题干、图像或推理预设，不因数学错答或截断改参重测。旧 Batch 文件及辅助材料已清理，仅进行离线预检和本机模拟接口测试不代表已调用付费模型。

2026-11-12 用户要求“新的模型用新的脚本”。Qwen3.8-Max-0902 使用独立入口 `MathPalette_Dataset/infer_qwen38_max_0902.py`，模型 ID `qwen3.8-max-0902`，平台 `https://maas.qianwenaiapi.com/compatible-mode/v1`。用户随后明确“Deepseek用max，Qwen用xhigh，然后把请求总时限改成240，输出token上限不要设置”：两份正式推理脚本默认分别为 `max` / `xhigh`，总时限240秒，不发送 `max_tokens`、`max_completion_tokens` 或显式 `thinking_budget`。服务端默认输出限制仍适用。此处240秒覆盖正式推理脚本此前的120秒设定，不改动下方工作台 Quick Test 的120秒规则。API Key 保存在用户明确要求继续由 Git 跟踪的根目录 `.env`，DeepSeek 和 Qwen 分别读取 `DEEPSEEK_API_KEY` 与 `QWEN_38_MAX_0902_API_KEY`；不得自行迁移到 `.env.local` 或修改跟踪状态。

平面、立体分别使用分支 `REDRAW_PROTOCOL.md` 和 `dataset_generator/protocol.json`；立体须分别冻结三维几何、投影和可见性。Special 操作范围见各分支 `workbench/README.md`、`workbench/agent_prompt.md` 与 `workbench/plugin.schema.json`。原对象实虚线覆盖属于变体外观操作，不改写原冻结场景。

未通过的新题在独立暂存区制作，不写进正式目录或清单。临时输出放 `.runtime/`；运行时缓存、日志和预览不作为正式数据。来源图片缺失时如实记录，不用重绘图冒充。

用户已明确要求删除旧评测日志和分数，不从旧实验报告恢复这些文件。清理不修改 `.git` 历史或 `.env`。

## Quick Test 请求超时与重试（2026-11-06 用户更新）

单次测试 HTTP 请求从实际发出起等待超过 120 秒，取消该次本地请求并重新请求同一次测试；覆盖旧的“不取消、不重试慢请求”规则。使用总时长限制，不能只依赖 socket 读取间隔超时。每次取消及重试均保存独立尝试 ID、时间、状态与已有部分响应，并计入每题调用上限。保留已经完整返回的另一轮结果，只重试超时的那一轮；两轮仍须独立。预算耗尽就停止，不能绕过上限。超时重试沿用同一冻结图片、题干与测试前预设，不修改预设、不因答案不理想重测。该规则允许超时后的同像素重试，其他历史像素去重约束保持有效。本地取消仅表示关闭本地请求，不能声称服务端已撤销计算或计费。
