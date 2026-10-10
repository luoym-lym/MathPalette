# PlaneGeometry：平面几何

本分支提供平面几何重绘协议、机器样式配置与公共绘图器。它与 Analytics 的函数图流程分别维护。

- [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)：制作和验收规则。
- [dataset_generator/protocol.json](dataset_generator/protocol.json)：画布、线宽、字体、标记与数值容差。
- [dataset_generator/common_renderer.py](dataset_generator/common_renderer.py)：从冻结场景生成 PNG / SVG，检查支持的几何约束和标注。
- [dataset_generator/test_renderer.py](dataset_generator/test_renderer.py)：使用独立构造的几何场景核对重绘器。

在 MathPalette 目录执行：

```powershell
python -B PlaneGeometry/dataset_generator/test_renderer.py
```

公共绘图器提供 `draw(scene_path, output_path=None)`，从冻结场景生成 PNG 或 SVG。现已收录 MathVerse 的 40 道题（Plane01～Plane40）：四字段记录在 `dataset.jsonl`，原始来源图在 `originals/`，重绘 PNG / SVG 在 `image/`，冻结场景、逐题类和核对报告在 `dataset_generator/`。

在项目根目录执行 `python -B dataset_tools/geometry_dataset.py PlaneGeometry Plane01` 可重新生成指定题目并核对确定性。每题类也提供 `draw(output_path=None)`。来源题干和 GT 原样保留；答案冲突、缺少条件或解释歧义另存 `answer_verification`，不因疑点删题。全批见 [原图 / 重绘对照页](../imports/mathverse_vision_dominant/redraw_review.html) 与 [核验疑点](../imports/mathverse_vision_dominant/issues.md)。

Base 操作、人工 Special 工作台和评测接入尚未制定。现有 Analytics 工作台只服务 Ana 系列。
