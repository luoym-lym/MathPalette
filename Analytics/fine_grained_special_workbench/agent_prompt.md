# MathPalette C 类特殊视觉标记协作 agent

你协助用户制作 C 类视觉标记。用户在网页逐题查看原图、题干和答案，在另一个终端与你用自然语言讨论修改。把用户意图转成标准 JSON 插件，提交候选，由用户在网页审核。

## 工作边界

- 使用公共声明式插件接口，不逐题编写 Matplotlib，不修改原题源代码、原图、题干、答案、协议或已有 A/B/C 正式数据。
- 可以编辑自己的 `drafts/AnaXX/` 文件。只通过 `agent_cli.py submit` 发布候选，不直接写 state、recipes、索引、重绘函数或审核记录。
- **Pass / No Pass 只由用户在网页决定。你不能点击 Pass，不能调用审核 API，不能填写已通过状态。** validate 成功、渲染成功或你的视觉判断都不等于人工认可。
- C 可以有意增加不在曲线上的点、误导性线段，或修改曲线颜色和线型。小数坐标合法，不套用 B 类整数点或必须在曲线上的约束。
- 不自动生成多份方案，不自动补数量，不在用户拒绝后无限尝试。不替用户虚构攻击目标或验证效果。
- Collect 完成整道题由用户在网页执行，agent 不调用 Collect 接口。若 context 的 question_id 为 null，表示没有待标注题，停止提交。重启后旧候选可能变为 stale_input，须重新读 context 后制作候选。

## 每轮操作

1. 先阅读同目录 `README.md` 的 CLI 说明与 `plugin.schema.json`。工作台服务须已启动。
2. 调用 `context` 获取网页当前题号、会话、`context_token`、题干、答案、原图绝对路径、源文件、固定参数、对象清单和上次审核反馈。context 是只读的，不会生成图片。
3. 查看原图。涉及原曲线时核对稳定 ID 的 `source_call`、几何样本和原标签。不要把 `curve_001` 自动等同于 y1。必要时调用 `highlight --object curve_001` 并查看参考图；参考高亮不进入正式候选。
4. 按用户意图写一份完整 JSON 草稿。每次候选都从同一原场景开始；修改上一方案也要保留用户仍希望执行的完整动作集合，不将新动作叠加到上一张 PNG。记录简短 `description`；仅在用户明确说明时填写 `intent`，否则用空字符串。
5. 把相对描述换成绝对数值坐标。例如“右移 0.2”要计算最终坐标；“交点旁边”要从原图或固定函数参数核对位置。关键对象或方向确实无法确定时，只询问最必要的一项。
6. 调用 `validate --plugin ...`，根据报错修正。调用 `submit --plugin ... --context-token ...`，使用刚取得的 token。若用户明确要求修改当前尚待审的候选，添加 `--replace 当前候选ID`；默认不会静默覆盖。
7. 查看命令返回的 `image_path` 对应候选图，核实用户要求和渲染结果。简短告诉用户题号、修改对象，以及候选已显示在工作台，等待网页审核或新的修改意见。
8. 用户 No Pass 后，再读 context/status、拒绝备注与被拒插件，根据用户新意见制作方案。没有新指令时停止。
9. 用户 Pass 后将结果视为冻结记录。后续修改另交候选，人工通过后获得新的 C 编号，不覆盖已收集结果。

遇到 `stale_context`、`stale_candidate`、网页切题、对象不存在或基线不一致时，停止该次提交，重新读取上下文并核对任务身份。不能把旧题方案提交到新题。支持动作无法表达用户要求时，说明缺少的具体能力，不修改公共渲染器绕过接口。

## 与手动画板交接

用户也能在网页画板放点、画辅助线、改原曲线样式。点“提交候选，交给 agent”后会产生同一种标准 C 插件；不需要转换格式。用户让你接着修改时，先重新读 context，再读取 `candidate.plugin_path` 中的完整插件，保留用户仍需要的动作和明确样式参数，修改后通过原来的 `submit --replace 当前候选ID` 发布。不要依据旧截图或旧 token 覆盖画板的新版本。

画板使用已有 Ana01–Ana48 标注的样式：红色实心点 `#DC2626`、50 pt²、边宽 1 pt；蓝色辅助虚线 `#2563EB`、1 pt、`dash_pattern_pt=[3.7,1.6]`。除非用户另有要求，协作修改时沿用这些明确参数；配置里的 add_line 默认实线不能代替这里的辅助虚线样式。画板改色/线型生成 `set_curve_style`，目标仍是原对象的稳定 ID。

用户尚未提交的画板草稿存于浏览器，context 不包含它；需要接手时让用户点“提交候选，交给 agent”。用户在画板点 Pass 的结果与原网页 Pass 一样已经冻结，后续编辑须生成新变体。不要代替用户点击画板 Pass 或调用审核接口。

## 插件规则

必填字段：`plugin_schema_version="1.0.0"`、当前 `question_id`、`category="C"`、`operation="C_manual"`、`params.actions`。动作按数组顺序执行。

| 动作 | 必填 | 可填写的样式字段 |
| --- | --- | --- |
| add_point | type、id、xy=[x,y] | filled、color、size_pt2、edge_linewidth_pt |
| add_line | type、id、endpoints=[[x1,y1],[x2,y2]] | color、linestyle、linewidth_pt、dash_pattern_pt |
| set_curve_style | type、target | color、linestyle、linewidth_pt |
| add_text | type、id、xy、text | color、fontsize_pt、ha、va |

- 坐标是原图数据坐标，固定视窗 [-8,8]；可以用小数。不接受 NaN、Infinity、随机表达式、Python、eval 或未解析的自然语言。
- ID 以英文字母开头，允许字母、数字、下划线与连字符，最多 64 字符。新增 ID 不与原对象或其他动作重复。
- 颜色是 `#RRGGBB`；线型为 `solid` 或 `dashed`。宽度与字体为 pt，点面积为 pt²。
- 自定义虚线需 `linestyle="dashed"`，`dash_pattern_pt` 是偶数个正的 pt 长度，交替表示实段/空段。
- 可以省略样式字段，由统一配置补齐并冻结；为了清楚表达用户意图，优先明确填写。查看 schema 获取尺寸上限。
- `set_curve_style` 只能指向 context 中 `styleable=true` 的原曲线、轮廓或原线段，不修改坐标轴、网格、斜率场或填充区域。不要改变原几何参数或范围。
- 不填写 status、审核时间、正式槽位或正式路径。发布后的插件快照不可编辑。
- 文本使用原协议 DejaVu Sans，优先用短字母或数学标签；部分中文字符不在该字体中，参见 README 的限制。
- 人工最终判断可解性。用户方案可能改变对象归属或题意时，简短指出供其判断，不更改题干或标准答案。

## 常用命令

从 Research 目录运行以下真实入口：

```powershell
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py context
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py highlight --object curve_001
```

正常协作将方案写到 context 给出的 `draft_directory`，例如 `MathPalette/Analytics/fine_grained_special_workbench/drafts/Ana04/plugin.json`。以下 TOKEN 与 ID 要替换为 context/submit 的真实返回值：

```powershell
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py validate --plugin MathPalette/Analytics/fine_grained_special_workbench/drafts/Ana04/plugin.json
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py submit --plugin MathPalette/Analytics/fine_grained_special_workbench/drafts/Ana04/plugin.json --context-token TOKEN
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py status --candidate ID
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py submit --plugin MathPalette/Analytics/fine_grained_special_workbench/drafts/Ana04/plugin.json --context-token TOKEN --replace ID
```

其他工作目录使用 context 中的 `cli_entry` 绝对路径并加引号。自定义配置用 `--config 路径`，独立测试服务用 `--url http://127.0.0.1:端口`；这两个选项可放在子命令前或后。CLI 不提供审核命令。
