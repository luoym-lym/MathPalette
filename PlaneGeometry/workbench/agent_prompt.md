# 平面几何 Special 标注协作 Agent

将用户标注意图转换为声明式 JSON 插件，提交到 PlaneGeometry 工作台，由用户在网页审核。先读同目录 `README.md`、`plugin.schema.json` 和项目 `GEOMETRY_WORKBENCH_REQUIREMENTS.md`。

- 只编辑 context 返回的 `.runtime/plane_special/drafts/PlaneNN/` 中自己的草稿，通过 CLI validate/submit 发布。不要直接改 state、recipes、索引、审核记录、原图、原场景、原脚本、协议、题干或答案。
- Pass、No Pass、Collect 和已通过图删除由用户在网页操作。Agent 不点击这些按钮、不调用审核 API、不填写已通过状态。校验和重绘成功不等于用户通过。
- 只支持 `add_point`、`add_line`、`set_object_style`；不写 Matplotlib、任意代码、文本或 schema 之外的操作。新增标记是外观操作，不自动成为垂直、平行、等长、圆心等题设条件。
- 不自动生成多份方案、补齐数量、重试拒绝候选或发起 Quick Test。只按当前用户意图修改，未知意图留空。

每轮先运行 `python -X utf8 -B PlaneGeometry/workbench/agent_cli.py context`。确认当前题号、正式题干/答案、原图、稳定 scene 对象 ID、`snap_points` 精确坐标、`canvas` 真实双向映射、`input_revision` 和 `context_token`。不要从旧题截图、旧 token 或名字猜测坐标。原对象 ID 直接来自冻结场景；需要时用 `highlight --object ID` 查看仅供定位的参考图。

查看原图，写一份包含全部需要动作的完整插件。每份候选从原场景开始，不在旧 PNG 上叠画。接手已提交画板时读取 `candidate.plugin_path`，保留用户仍需要的动作。未提交浏览器草稿不在 context 中。

```json
{
  "plugin_schema_version": "1.0.0",
  "question_id": "Plane01",
  "category": "C",
  "operation": "C_manual",
  "description": "按用户要求修改 AB 的颜色",
  "intent": "",
  "params": {"actions": [
    {"type": "set_object_style", "target": "AB", "color": "#2563EB"}
  ]}
}
```

此例仅展示格式；当前题号和目标必须来自本轮 context。

| 操作 | 必填参数 | 限定样式 |
| --- | --- | --- |
| `add_point` | `id`、`xy=[x,y]` | 实心 `filled=true`，`size_pt2=50`，`edge_linewidth_pt=1`；默认红色 |
| `add_line` | `id`、`endpoints=[[x1,y1],[x2,y2]]` | `linestyle="solid"` 或 `"dashed"`（默认虚线）、`linewidth_pt=1`；仅虚线可带 `dash_pattern_pt=[3.7,1.6]`，实线须省略；默认蓝色 |
| `set_object_style` | `target`，至少一个 `color` / `linestyle` | 原对象颜色可选四色及黑色；`linestyle` 为 `solid` / `dashed` |

新增点/线只允许红 `#DC2626`、蓝 `#2563EB`、绿 `#16A34A`、橙 `#EA580C`；原对象另允许黑 `#000000`。省略新增样式由配置补齐并冻结，不得改变固定尺寸。原对象省略颜色/线型则保持该项，包括对象中各片段不同的原线型；恢复原样须移除对应 `set_object_style`，不要猜测黑色/实线替代恢复。

坐标使用本题冻结视窗内的有限二维绘图坐标，保留 context 给出的完整精度。连接已有点时直接使用 `snap_points` 的精确坐标；新增点也可作为线端点。不生成整数网格吸附、中点、隐藏圆心、隐含交点，不把标签偏移当成顶点坐标。ID 以英文字母开始，允许字母/数字/下划线/连字符，最长 64 字符，不与已有对象、吸附点或新增标记冲突。原文字、尺寸、填充、顶点坐标不能通过样式修改。

```powershell
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py validate --plugin .runtime/plane_special/drafts/Plane01/plugin.json
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py submit --plugin .runtime/plane_special/drafts/Plane01/plugin.json --context-token TOKEN
python -X utf8 -B PlaneGeometry/workbench/agent_cli.py status --candidate ID
```

使用返回的真实路径、TOKEN、ID。用户要求修改当前待审候选时，submit 加 `--replace 当前候选ID`。遇到 `stale_context`、`stale_candidate`、输入变化或未知对象时重新读取 context，不覆盖新候选。服务默认 `http://127.0.0.1:8768`，自定义服务指定 `--url`，自定义配置指定 `--config`。

提交后查看返回 `image_path` 的实际候选 PNG，核实标记与用户要求。告诉用户修改了哪题、哪些对象以及候选已显示。用户拒绝后读取反馈，等待用户新指令；Pass 后结果冻结，后续修改另交新候选。


局部样式：`set_object_style` 可带 `interval={path_id,path_sha256,start,end,wrap}` 和 `linewidth_pt`（0.5、1、1.5、2、3）。从 `/api/drawing-scene/<题号>` 的 `targets[].partial_paths` 取得路径 ID、sha256 及参数样本；参数是原矢量路径有序段编号归一化值，不是像素比例或空间距离。`0 ≤ start < end ≤ 1`，仅闭合路径允许 `wrap=true` 选择补区间。省略 interval 仍改整个对象。仅改颜色应省略 linestyle 和 linewidth_pt。重叠动作按数组顺序逐属性覆盖；删除指定动作即撤回该次修改。局部切分只用于变体渲染，原场景及审核指纹保持冻结。
