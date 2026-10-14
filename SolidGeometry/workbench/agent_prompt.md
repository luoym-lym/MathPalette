# 立体几何 Special 标注 Agent

先阅读根目录 `MATHPALETTE_PROTOCOL.md`、`GEOMETRY_WORKBENCH_REQUIREMENTS.md` 和 `SolidGeometry/REDRAW_PROTOCOL.md`。本工作台只对正式 Solid 题增加二维标注或覆盖原线条外观；不改变题干、答案、三维坐标、投影、可见性区间、尺寸绑定或原图。原题审核与 Special Pass / Collect 相互独立。

从项目根目录运行：

```powershell
python -X utf8 -B SolidGeometry/workbench/agent_cli.py context
python -X utf8 -B SolidGeometry/workbench/agent_cli.py highlight --object AB
```

context 提供当前 Solid 题号、正式题干/答案、输入指纹、`objects` 稳定 ID、`snap_points` 和 `canvas` 坐标变换、`projection`、候选以及 `context_token`。所有新增坐标都是冻结投影后的二维绘图坐标。可用 `snap_points[].xy` 精确连接已有顶点或命名点，不要通过测图或舍入替代该坐标。同一投影位置的空间点仍各有独立 ID 和 `world_xyz`；投影交叉不是新空间交点。不自动生成中点、圆心、整数格点或未显示的内部构造点。

仅允许 `plugin.schema.json` 中的三种声明式动作：

- `add_point`：`id`、`xy`；实心、50 pt²、边宽 1 pt。颜色限红 `#DC2626`（默认）、蓝 `#2563EB`、绿 `#16A34A`、橙 `#EA580C`。
- `add_line`：`id`、两个二维 `endpoints`；固定 1 pt，可选 `linestyle="solid"` 或 `"dashed"`（默认虚线）；仅虚线可带 `dash_pattern_pt=[3.7,1.6]`，实线须省略；默认蓝色，可用相同四色。用 context 提供的精确 `xy` 连接已有点，或连接此前新增点的 `xy`。标注不自动成为题设条件。
- `set_object_style`：`target` 是可选原对象的稳定 ID；`color` 可用上述四色或黑 `#000000`，`linestyle` 仅 `solid` / `dashed`；也可设置白名单线宽，三种属性至少提供一种。只改颜色时省略 `linestyle`，保留每个可见/隐藏片段的原线型。明确设置线型时覆盖指定范围；省略 interval 时覆盖全部实际片段，包括原隐藏线。这是成图外观改变，保存记录会声明 rendered visibility style override；原冻结可见性仍不改动。恢复原样应删除该对象的样式动作。

不支持额外颜色、白名单外线宽/点大小/虚线密度、文字、移动对象或执行绘图代码。标签、尺寸文字、面填充不作为可编辑目标。所有规则由服务端再次验证；不得修改程序或冻结输入绕过白名单。不要把高亮参考图、鼠标覆盖层或控制点用于提交。

插件示例（Solid01 中的 A、B 坐标应从本次 context 获取，不复制其他题坐标）：

```json
{
  "plugin_schema_version": "1.0.0",
  "question_id": "Solid01",
  "category": "C",
  "operation": "C_manual",
  "description": "将 AB 改为红色，保留原线型",
  "intent": "突出指定棱",
  "params": {"actions": [{"type": "set_object_style", "target": "AB", "color": "#DC2626"}]}
}
```

草稿只写到 context 返回的 `draft_directory`，例如 `.runtime/solid_special/drafts/Solid01/plugin.json`。提交前验证：

```powershell
python -X utf8 -B SolidGeometry/workbench/agent_cli.py validate --plugin .runtime/solid_special/drafts/Solid01/plugin.json
python -X utf8 -B SolidGeometry/workbench/agent_cli.py submit --plugin .runtime/solid_special/drafts/Solid01/plugin.json --context-token TOKEN
python -X utf8 -B SolidGeometry/workbench/agent_cli.py status --candidate ID
```

若当前已有待审候选，仅在用户明确要求替换时读取最新 context，附 `--replace ID`。切题、替换或审核会使旧 token 失效；重新读取 context 后再操作。不要直接写 state、recipes、索引或收集记录；CLI 不提供 Pass / Collect。最终必须由用户在网页查看实际 PNG 后审核。Quick Test 仅由用户手动发起，使用正式题干与当前候选图，不发送答案、原图、标注意图或绘图参数，不自动判分、重试或通过。


局部样式：`set_object_style` 可带 `interval={path_id,path_sha256,start,end,wrap}` 和 `linewidth_pt`（0.5、1、1.5、2、3）。从 `/api/drawing-scene/<题号>` 的 `targets[].partial_paths` 取得路径 ID、sha256 及参数样本；参数是原矢量路径有序段编号归一化值，不是像素比例或空间距离。`0 ≤ start < end ≤ 1`，仅闭合路径允许 `wrap=true` 选择补区间。省略 interval 仍改整个对象。仅改颜色应省略 linestyle 和 linewidth_pt。重叠动作按数组顺序逐属性覆盖；删除指定动作即撤回该次修改。局部切分只用于变体渲染，原场景及审核指纹保持冻结。
