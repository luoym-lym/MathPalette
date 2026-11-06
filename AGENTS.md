# MathPalette 工作说明

创建或修改题目、变体和数据流程前，阅读根目录 `MATHPALETTE_PROTOCOL.md` 以及对应分支协议。

仅用户明确确认的原题进入正式数据。三个分支 `dataset.jsonl` 都只包含正式题；根目录 `question_bank.jsonl` 是 `dataset_tools/catalog.py build` 生成的汇总。不得恢复旧候选清单或把 Special Pass/Collect 当成原题通过。

正式题号统一：当前为 Ana01～Ana51、Ana53～Ana71、Plane01～Plane599、Solid01～Solid288；Ana52 已按用户要求删除，不复用。Analytics 的 DynaMath 使用 Ana01～Ana20，MathVerse 使用 Ana21～Ana45、Ana47～Ana51 与 Ana53～Ana71，MathVista 使用 Ana46；Solid17～Solid25 来自 SOLIDGEO。Plane140～Plane490 与 Solid79～Solid248 来自 MathVision。Plane491～Plane511 与 Solid249～Solid257 为 Author Designed。Plane512～Plane529 与 Solid258～Solid263 为用户授权直接入库的24道拓展题。Plane530～Plane599 与 Solid264～Solid288 为用户于2026-11-05批准入库的95道同题型拓展原题，父题映射见 `provenance/author_extensions95_20261105.json`；本轮未创建 Specialvar 或 Collect。所有原创题来源按用户最新要求统一为 `Author Designed`，历史原话保留。题源以各分支 `dataset.jsonl` 为准。新增题号继续递增，不复用、不建立另一套 formal/candidate 编号。

用户通过原话、时间及当前内容指纹在 `provenance/approvals.json`。改题干、答案、绘图输入或原图时，须用户重新确认后更新记录。迁移仅在题干、答案及像素一致的核验通过后更新路径/编号指纹，保留旧指纹和原审核时间。

使用 `dataset_tools/question_review.py 分支 题号 --instruction "用户明确通过原话"` 保存审核并同步索引；不得用修改指令、数学检查或本工具执行成功代替用户批准。

三个分支的 Base 均未启用。Special 分别使用各自 `workbench/`，由用户 Pass / Collect。不得伪造通过记录。

平面、立体分别使用分支 `REDRAW_PROTOCOL.md` 和 `dataset_generator/protocol.json`；立体须分别冻结三维几何、投影和可见性。Special 操作范围见各分支 `workbench/README.md`、`workbench/agent_prompt.md` 与 `workbench/plugin.schema.json`。原对象实虚线覆盖属于变体外观操作，不改写原冻结场景。

未通过的新题在独立暂存区制作，不写进正式目录或清单。临时输出放 `.runtime/`；运行时缓存、日志和预览不作为正式数据。来源图片缺失时如实记录，不用重绘图冒充。

用户已明确要求删除旧评测日志和分数，不从旧实验报告恢复这些文件。清理不修改 `.git` 历史或 `.env`。

## Quick Test 请求超时与重试（2026-11-06 用户更新）

单次测试 HTTP 请求从实际发出起等待超过 120 秒，取消该次本地请求并重新请求同一次测试；覆盖旧的“不取消、不重试慢请求”规则。使用总时长限制，不能只依赖 socket 读取间隔超时。每次取消及重试均保存独立尝试 ID、时间、状态与已有部分响应，并计入每题调用上限。保留已经完整返回的另一轮结果，只重试超时的那一轮；两轮仍须独立。预算耗尽就停止，不能绕过上限。超时重试沿用同一冻结图片、题干与测试前预设，不修改预设、不因答案不理想重测。该规则允许超时后的同像素重试，其他历史像素去重约束保持有效。本地取消仅表示关闭本地请求，不能声称服务端已撤销计算或计费。
