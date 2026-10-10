# SolidGeometry

正式通过题共 16 道：Solid01～Solid16。`dataset.jsonl` 仅含正式题；重绘 PNG 在 `image/`，来源截图在 `originals/`，冻结场景和逐题绘图程序在 `dataset_generator/`。

公共绘图器和机器协议保持原样。场景可重新导出 PNG 或 SVG；本次移除重复的 SVG 成品。Base/Special 尚未启用。

在项目根目录重绘：

```powershell
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
python -X utf8 -B SolidGeometry/dataset_generator/test_renderer.py
```

具体几何规则见 [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)。统一收集规则见 [项目协议](../MATHPALETTE_PROTOCOL.md)。
