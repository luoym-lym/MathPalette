# 立体几何 Special 工作台

在项目根目录双击或运行 `SolidGeometry/start_special_workbench.cmd`，打开 `http://127.0.0.1:8769`。也可运行：

```powershell
python -X utf8 -B SolidGeometry/workbench/launch_workbench.py
```

启动器复用既有工作台的冻结依赖检查、解释器选择、端口与重启处理；可用 `MATHPALETTE_PYTHON` 指定解释器。`requirements.txt` 和已通过 recipes 的依赖必须匹配。工作台读取 `SolidGeometry/dataset.jsonl` 中的 16 道正式题；选题、候选、浏览器草稿和审核令牌独立于平面与解析工作台。

侧栏题号搜索下方的「来源」可按正式清单中的数据集筛选，默认「全部来源」；与题号搜索及已完成列表的特殊情况筛选组合生效，「上一题／下一题」遵循当前筛选。

打开画板可添加四色实心点、四色辅助线（实线或虚线），以及选择原棱线、圆弧、曲面轮廓或原辅助线修改颜色与实虚线。原对象使用场景稳定 ID，重叠时从下拉列表选择；一个圆弧的多个显隐片段一起高亮和改色。单纯改色保留各片段原线型，点“改为实线/虚线”才覆盖线型；“恢复原对象样式”移除该对象的所有覆盖。原文字、面填充、尺寸与关系标记的位置不变。

新点固定 50 pt²、边宽 1 pt；新线固定 1 pt，默认虚线，间隔 `[3.7,1.6]`；选择“辅助线 → 实线 / 虚线”后，可点选两个位置、拖动或选择两个点连接，吸附方式不变。红 `#DC2626`、蓝 `#2563EB`、绿 `#16A34A`、橙 `#EA580C` 四色可用于新增标记，原对象还允许黑色。服务端与 Agent 使用同一严格白名单。

按住 Ctrl 或启用“始终吸附几何点”时，鼠标按屏幕距离吸附到已有顶点、命名点或本画板新增点，并保存精确二维投影坐标。松开 Ctrl 可自由定位。辅助线支持两次点击、拖动，或选择起点/终点后点“连接所选两点”；同一投影位置的不同空间点仍分别列出原 ID。Shift 仅限制画面水平/竖直，不覆盖吸附端点，也不表示空间垂直关系。不会自动添加中点、圆心、整数格点或投影交点。

画板预览由原冻结公共 renderer 和受限插件渲染器生成。未标注的 16 题须逐题与正式原图像素一致；保持 768×768、不透明白底、原视窗和标签。鼠标高亮、吸附提示和控制点不进入 PNG。撤销/重做、删除标记、取消线段、清空、提交候选和 Pass 均沿用原流程。

Pass 保存一份 C 变体；No Pass 拒绝本候选；Collect 结束整题，已完成列表可重新打开。删除已通过图使用可恢复事务。通过图仅在用户 Pass 后创建于 `SolidGeometry/special_variant/`；Collect 和特殊标记另存整题完成记录，每题包含 `images/`、`plugins/`、`recipes.json`、`draw_variants.py`，完成题另有 `collection.json`。保存原场景、原 PNG、绘图入口、公共 renderer、协议、插件执行器、schema 和依赖的指纹；显式线型覆盖另外记录为 `appearance_changes.rendered_visibility_style_overrides`。原三维几何、投影和冻结可见性区间保持只读。

运行状态、草稿、未通过图、预览、删除备份和 Quick Test 回答只写 `.runtime/solid_special/`。清理运行缓存后，已 Pass 的 recipes 和 Collect 记录可恢复收集状态；未通过草稿仍属于临时数据。修改已审核题目须另行获得用户批准，不能用 Special 审核替代原题批准。

**Quick Test 1** 调用 MiniMax-M3（nonthinking），**Quick Test 2** 调用 MiniMax-M3.1-Flash-Preview（low）。每次点击仅调用所选模型一次；两种模式的回答、思考（如有）、用时和 token 数分别显示并保存，互不覆盖。仅发送本题正式题干和当前候选 PNG；标准答案、原图、意图与参数不发送。不增加判分器，不自动重试、Pass 或 Collect。服务端读取项目现有环境配置；页面与记录不保存密钥。结果绑定本分支、题号、候选、PNG 与像素指纹，替换候选不会错用旧回答。

Agent 使用 [agent_prompt.md](agent_prompt.md)、[plugin.schema.json](plugin.schema.json) 和 `agent_cli.py`；绘图输入与候选冲突保护同画板一致。

```powershell
python -X utf8 -B SolidGeometry/workbench/agent_cli.py context
python -X utf8 -B SolidGeometry/special_variant/Solid01/draw_variants.py C01
```

离线重绘默认写 `.runtime/solid_special/reproduced/`，核对通过时环境、执行器、该题冻结依赖与最终像素，拒绝覆盖正式输入或已通过 PNG。

软件回归只产生可识别的临时测试夹具，使用模拟 API，不调用付费模型：

```powershell
python -X utf8 -B SolidGeometry/workbench/test_workbench.py
python -X utf8 -B SolidGeometry/workbench/test_quick_test.py
node SolidGeometry/workbench/test_board_geometry.js
```

需要隔离启动时，同时指定 `--data-dir` 与 `--output-dir`，例如将两者设在项目 `.runtime/solid_workbench_tests/` 中两个独立子目录。相对路径以调用命令时的目录为准，支持 `--flag value` 和 `--flag=value`。测试程序自动清理自身夹具；浏览器验收后应停止测试服务并删除对应预览、日志、缓存，不删除用户既有状态。需求见 [GEOMETRY_WORKBENCH_REQUIREMENTS.md](../../GEOMETRY_WORKBENCH_REQUIREMENTS.md)。

## 特殊情况与后期复审

点击题目顶部「特殊标记」，将当前题计入 Collect 完成并切换到下一道未完成题。无需先 Pass 变体；已有通过图保持原样，当前待审候选留在运行状态中，不会自动 Pass 或 No Pass。画板打开或正在生成候选时，先返回工作台并等待生成结束。

侧栏「已完成」显示「特殊情况 · 待复审」，可勾选「只看特殊情况 · 待复审」，点击「复审」重新打开。复审完成后照常 Pass / Collect；再次特殊标记则继续留待后审。重新打开和再次完成会保留历史记录。

标记保存在 `special_variant/<题号>/collection.json` 的 `current.special_case=true`、`current.review_status="pending"`，并同步 `collected_index.jsonl`；完成时间使用 `collected_at`。普通重启及清理运行缓存后仍能恢复特殊完成状态。未通过候选与浏览器草稿仍属于运行数据，清理对应缓存后不保证保留。特殊标记只记录整题的工作进度，不创建变体通过记录，也不改变原题审核。


## 局部区间样式（2026-10-14）

选择原对象后，将「修改范围」切换到「局部区间」，在线上点选起点、终点；靠近已有几何点、显式交点或路径端点时自动吸附。青色高亮表示将要修改的区间，拖动两端圆点可以调整范围。交叉处锁定原对象，多个不相连的路径不能跨空隙连接。圆或其他闭合路径可用「选择另一段」切换两点之间的另一侧。

颜色、实虚线和线宽仅影响所选区间；线宽允许 0.5、1、1.5、2、3 pt。只改颜色时保留原有实虚线，包括立体图的显隐片段。点击「重新选区间」可继续添加另一处修改；在「编辑标记」列表点击「编辑区间」可重选、拖动或删除已有局部修改。重叠操作按列表顺序逐属性应用，后面的同属性操作优先。删除局部修改会显露下面的样式；「整个对象 → 恢复原对象样式」移除该对象的全部覆盖。支持撤销、重做和浏览器草稿恢复。

插件仍使用 `set_object_style`，新增可选 `linewidth_pt` 和 `interval`。区间字段为 `path_id`、`path_sha256`、`start`、`end`、`wrap`，满足 `0 ≤ start < end ≤ 1`；`wrap=true` 仅用于闭合路径另一侧。路径来自画板 `targets[].partial_paths`，参数按原矢量路径的有序段编号归一化；样本第三列是参数。保存完整参数和路径指纹，不保存鼠标像素位置。后端精确切分贝塞尔/折线路径，保留原填充、投影和可见性输入。预览、提交与离线重绘使用同一实现。

升级只兼容 `style_compatibility.json` 记录的旧整对象执行器与 schema 组合，旧 recipe 不改写；仍核验环境、题目输入、参数及最终像素。未知执行器继续拒绝。测试命令：

```powershell
python -X utf8 -B SolidGeometry/workbench/test_partial_style.py
node SolidGeometry/workbench/test_partial_selection.js
node SolidGeometry/workbench/test_partial_board.js
```
