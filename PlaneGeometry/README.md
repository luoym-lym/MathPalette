# PlaneGeometry

正式通过题共 102 道：MathVerse 38 道、MathVista 55 道、Author designed 9 道。`dataset.jsonl` 仅含正式题；重绘 PNG 在 `image/`，来源图片在 `originals/`（没有来源图时记录为 `null`），冻结场景和逐题绘图程序在 `dataset_generator/`。

Plane100～Plane102 是 Author designed 最短路径题，依次为等半径双圆、单圆偏置端点、不等半径双圆。正式图保留黑色几何、半径和距离标注；本次仅收录原题。精确答案见 `dataset.jsonl`，构造、推导和重绘核验见根目录 `provenance/source_notes.json`。

公共绘图器和机器协议保持原样。场景可重新导出 PNG 或 SVG。Base 尚未启用；Special 标注工作台已提供，原题审核与变体 Pass/Collect 分开保存。

双击 `start_special_workbench.cmd`，在 `http://127.0.0.1:8768` 标注平面题。工作台支持已有对象颜色/实虚线、四色实心点、四色辅助虚线，以及已有几何点与新增点的精确吸附连接。运行状态在项目 `.runtime/plane_special/`，用户 Pass 后才保存到 `special_variant/`。使用、Agent CLI 与测试说明见 [workbench/README.md](workbench/README.md)。

在项目根目录重绘：

```powershell
python -X utf8 -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01
python -X utf8 -B PlaneGeometry/dataset_generator/test_renderer.py
```

具体几何规则见 [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)。统一收集规则见 [项目协议](../MATHPALETTE_PROTOCOL.md)。
