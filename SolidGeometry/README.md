# SolidGeometry

正式通过题共 25 道：Solid01～Solid25，其中 MathVerse 16 道、SOLIDGEO 9 道。`dataset.jsonl` 仅含正式题；重绘 PNG 在 `image/`，来源截图在 `originals/`，冻结场景和逐题绘图程序在 `dataset_generator/`。

公共绘图器和机器协议保持原样。场景可重新导出 PNG 或 SVG；不保留重复的 SVG 成品。Base 尚未启用；Special 标注使用独立工作台，由用户逐份 Pass、整题 Collect。

双击 `start_special_workbench.cmd` 打开立体工作台（端口 `8769`）。支持四色点、四色辅助虚线、原对象颜色与实虚线、Ctrl 几何点吸附、精确两点连接和 MiniMax-M3 Quick Test。运行数据在项目 `.runtime/solid_special/`，人工通过的结果保存在本分支 `special_variant/`。详细流程见 [工作台说明](workbench/README.md) 与 [已确认需求](../GEOMETRY_WORKBENCH_REQUIREMENTS.md)。

在项目根目录重绘：

```powershell
python -X utf8 -B dataset_tools/geometry_dataset.py SolidGeometry Solid01
python -X utf8 -B SolidGeometry/dataset_generator/test_renderer.py
```

具体几何规则见 [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)。统一收集规则见 [项目协议](../MATHPALETTE_PROTOCOL.md)。

## SOLIDGEO 已收集原题

本批只保留用户已 Pass 的 Solid17～Solid25，来源题号依次为 1766、1807、1878、1892、1932、2024、2046、2072、2135。正式数据、图片、冻结绘图依赖及原审核记录完整保留。

剩余 86 道待审候选、重复暂存文件、本批原题审核工具和缓存已删除，当前没有待审队列。保留清单与文件指纹核验见 [清理记录](../provenance/solidgeo_cleanup.json)，来源署名及许可见 [SOLIDGEO_ATTRIBUTION.md](../provenance/SOLIDGEO_ATTRIBUTION.md)。已入库题仍可在 Special 工作台制作变体；变体 Pass / Collect 与原题审核独立。

Solid17～Solid25 的题干已按用户再次确认的版本清理：移除图片占位符、残留标题及填空占位，统一英文表述，正式清单与逐题脚本保持一致。数学条件、答案、选项、图片和冻结场景保持原样；前后文本、原 Pass 和本次确认见 [题干修订记录](../provenance/solidgeo_wording_cleanup.json)。
