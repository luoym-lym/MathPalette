# MathPalette 协议入口

版本：2026-10-10。创建或修改题目、重绘图及变体前，先按题型阅读下列分支协议。

| 题型 | 协议与机器配置 | 当前流程 |
| --- | --- | --- |
| 函数与解析几何 | [Analytics 制作协议](Analytics/MATHPALETTE_PROTOCOL.md) | 冻结原题；自动抽取四种 Base；Special 由用户 Pass / Collect。 |
| 平面几何 | [重绘协议](PlaneGeometry/REDRAW_PROTOCOL.md)、[机器配置](PlaneGeometry/dataset_generator/protocol.json) | 独立几何构造与统一重绘；Base / Special 尚未启用。 |
| 立体几何 | [重绘协议](SolidGeometry/REDRAW_PROTOCOL.md)、[机器配置](SolidGeometry/dataset_generator/protocol.json) | 冻结三维几何、投影和可见性，生成 PNG / SVG；Base / Special 尚未启用。 |

各分支的坐标、几何语义和渲染器分别维护；不能把函数图的网格、刻度操作直接套入几何图。只有图片的材料可以制作 `redraw_example`，不推测题干、答案或真实来源数据集，也不占用正式题号。

函数数据与当前工作台分别在 `Analytics/fine_grained_dataset/`、`Analytics/fine_grained_special_workbench/`。旧 A/B 人工工作台仅用于历史回放。分支说明见 [Analytics](Analytics/README.md)、[PlaneGeometry](PlaneGeometry/README.md)、[SolidGeometry](SolidGeometry/README.md)。
