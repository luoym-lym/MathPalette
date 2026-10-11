# SolidGeometry

正式通过题共 16 道：Solid01～Solid16。`dataset.jsonl` 仅含正式题；重绘 PNG 在 `image/`，来源截图在 `originals/`，冻结场景和逐题绘图程序在 `dataset_generator/`。

公共绘图器和机器协议保持原样。场景可重新导出 PNG 或 SVG；不保留重复的 SVG 成品。Base 尚未启用；Special 标注使用独立工作台，由用户逐份 Pass、整题 Collect。

双击 `start_special_workbench.cmd` 打开立体工作台（端口 `8769`）。支持四色点、四色辅助虚线、原对象颜色与实虚线、Ctrl 几何点吸附、精确两点连接和 MiniMax-M3 Quick Test。运行数据在项目 `.runtime/solid_special/`，人工通过的结果保存在本分支 `special_variant/`。详细流程见 [工作台说明](workbench/README.md) 与 [已确认需求](../GEOMETRY_WORKBENCH_REQUIREMENTS.md)。

在项目根目录重绘：

```powershell
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
python -X utf8 -B SolidGeometry/dataset_generator/test_renderer.py
```

具体几何规则见 [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)。统一收集规则见 [项目协议](../MATHPALETTE_PROTOCOL.md)。
