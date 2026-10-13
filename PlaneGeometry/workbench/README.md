# 平面几何 Special 标注工作台

读取正式 `PlaneGeometry/dataset.jsonl` 的 Plane01～Plane71。工作台复制自 Analytics，使用独立端口、状态、浏览器草稿和 Agent 插件。通过图只在用户点击 Pass 后写入 `PlaneGeometry/special_variant/`，Collect 和特殊标记另存整题完成记录；不修改原题、原图、冻结场景或审核凭据。

从项目根目录运行：

```powershell
python -X utf8 -B PlaneGeometry/workbench/launch_workbench.py
```

也可双击 `PlaneGeometry/start_special_workbench.cmd` 或本目录 `start_workbench.cmd`，访问 `http://127.0.0.1:8768`。启动器检查根 `requirements.txt` 和已通过 recipes 的环境版本，自动寻找匹配 Python；可用 `MATHPALETTE_PYTHON` 指定解释器。再次启动会正常停止同一状态目录的旧服务，再读取最新输入。

## 画板与审核

1. 选择题目，核对原图、题干、答案，点击「打开画板」。
2. 标记点默认红色、实心、50 pt²、边宽 1 pt；辅助线默认蓝色、虚线、1 pt；选择“辅助线 → 实线 / 虚线”后，两次点选或拖动即可画线，吸附方式不变。虚线间隔固定 `[3.7,1.6]` pt。新增标记可选红 `#DC2626`、蓝 `#2563EB`、绿 `#16A34A`、橙 `#EA580C`。
3. 选择原对象工具点击线段、圆、弧、多边形轮廓或关系标记；重叠时使用对象列表。原对象可选上述四色或黑色，并切换实线/虚线。仅改颜色时保留原线型；恢复原样会删除该对象的样式覆盖。多边形填充与文字不随轮廓样式改变。
4. Ctrl 或「始终吸附」吸附已有顶点、图中命名/标出的点和画板新增点。没有附近目标时自由定位。辅助线靠近这些点时可两次点选精确连接，也可拖动。提示显示目标 ID；保存完整坐标精度。不会生成整数格点、中点、未显示圆心或交点。Shift 只约束画面水平/竖直，已吸附端点优先。
5. Esc 取消未完成线段/选择；支持撤销、重做、按项删除、清空。等待服务器实际 PNG 预览后，点击「提交到当前候选」或画板 Pass。青色高亮、鼠标指针和吸附提示不保存。
6. 每次 Pass 保存一张 C 图，同题可有 C01、C02……。No Pass 保留反馈并解除待审候选。Collect 在至少一张已通过、没有待审候选时完成整题。已完成题可从侧栏重新打开。
7. 已通过图可以删除，二次确认后剩余槽位顺序重排；删除备份在运行目录 `deleted_variants/`。Pass、删除和 Collect 事务意外中断后由重启恢复。

画板中未提交的草稿按平面题号和本题输入指纹保存在本浏览器。Agent 提交新候选或切题会使旧画板提交失效，须载入最新候选。界面中的构造坐标仅用于绘图，不是题设条件。

## Agent 与 CLI

先阅读 [agent_prompt.md](agent_prompt.md) 与 [plugin.schema.json](plugin.schema.json)。只支持 `add_point`、`add_line`、`set_object_style`。固定颜色、尺寸、虚线间隔、视窗坐标和对象 ID 均由服务端核对；不支持文字、任意代码或改动原几何。

```powershell
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py context
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py highlight --object AB
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py validate --plugin .runtime/plane_special/drafts/Plane01/plugin.json
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py submit --plugin .runtime/plane_special/drafts/Plane01/plugin.json --context-token TOKEN
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py status --candidate ID
```

使用 context 返回的真实题号、对象、`draft_directory`、token 和 candidate ID。用户要求替换待审候选时给 submit 加 `--replace ID`。自定义配置用 `--config`，测试服务用 `--url http://127.0.0.1:端口`。CLI 不提供人工审核命令。context 包含冻结 scene ID、吸附点、实际画板双向坐标映射、本题输入指纹与当前候选令牌。

## Quick Test

对已提交候选手动点击 **Quick Test 1**（MiniMax-M3，nonthinking）或 **Quick Test 2**（MiniMax-M3.1-Flash-Preview，low），沿用现有服务端环境配置。两种模式的回答、思考（如有）、用时和 token 数分别显示并保存，互不覆盖。每次手动操作仅一次调用，不自动重试或判分。请求只含正式题干和当前候选 PNG；标准答案、原图、说明、标注意图和绘图参数不发送。Key 只在服务端从项目 `.env` 或环境变量读取。

结果绑定 PlaneGeometry、题号、候选 ID、参数和实际 PNG 指纹，保存在 `.runtime/plane_special/quick_tests/`；切题、替换或审核后不会显示为另一份候选的结果。软件测试使用 mock API，不发送付费模型请求。

## 保存、重绘与测试

```text
PlaneGeometry/special_variant/
  accepted_index.jsonl
  collected_index.jsonl
  _baselines/<指纹>.json
  Plane01/
    images/C01.png
    plugins/C01.json
    recipes.json
    draw_variants.py
    collection.json
```

Pass 冻结实际操作、原图/场景/协议/原脚本/geometry_dataset.py 输入哈希、插件执行器、schema、依赖版本、题目记录指纹、PNG 指纹及人工审核时间。它不替代原题审核。清理运行缓存后，可由 recipes 和 collection 恢复收集状态。

在保留完整项目输入和工作台代码的环境中离线重绘：

```powershell
python -X utf8 -B PlaneGeometry/special_variant/Plane01/draw_variants.py C01
```

默认写 `.runtime/plane_special/reproduced/`，不覆盖正式图。其他题更新后可查历史基线继续重放；本题场景、题目记录、绘图输入、执行器或依赖变化则停止，不能自动更新旧通过记录。

从项目根目录运行离线软件验收：

```powershell
python -X utf8 -B PlaneGeometry/workbench/test_geometry.py
node PlaneGeometry/workbench/test_geometry_input.js
python -X utf8 -B PlaneGeometry/workbench/test_quick_test.py
python -X utf8 -B PlaneGeometry/workbench/launch_workbench.py --check --data-dir .runtime/plane_workbench_tests/check_state --output-dir .runtime/plane_workbench_tests/check_output
```

测试涵盖 16 题逐像素基线、每个可选对象的全部真实路径/片段、样式与填充/标签隔离、参数拒绝、精确吸附、候选冲突、临时 Pass/Collect 事务、冷启动恢复、离线入口、删除恢复及 Quick Test mock。所有审核夹具明确标记为 `TEMPORARY SOFTWARE TEST FIXTURE`，仅写 `.runtime/plane_workbench_tests/`，不进入真实 Special 或根索引。浏览器联调同样同时指定 `--data-dir` 和 `--output-dir`。

实现依据：[已确认需求](../../GEOMETRY_WORKBENCH_REQUIREMENTS.md)、[平面重绘协议](../REDRAW_PROTOCOL.md)。Base 仍未启用。

## 特殊情况与后期复审

点击题目顶部「特殊标记」，将当前题计入 Collect 完成并切换到下一道未完成题。无需先 Pass 变体；已有通过图保持原样，当前待审候选留在运行状态中，不会自动 Pass 或 No Pass。画板打开或正在生成候选时，先返回工作台并等待生成结束。

侧栏「已完成」显示「特殊情况 · 待复审」，可勾选「只看特殊情况 · 待复审」，点击「复审」重新打开。复审完成后照常 Pass / Collect；再次特殊标记则继续留待后审。重新打开和再次完成会保留历史记录。

标记保存在 `special_variant/<题号>/collection.json` 的 `current.special_case=true`、`current.review_status="pending"`，并同步 `collected_index.jsonl`；完成时间使用 `collected_at`。普通重启及清理运行缓存后仍能恢复特殊完成状态。未通过候选与浏览器草稿仍属于运行数据，清理对应缓存后不保证保留。特殊标记只记录整题的工作进度，不创建变体通过记录，也不改变原题审核。
