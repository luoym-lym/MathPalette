# SolidGeometry：立体几何

本分支提供立体几何重绘协议、机器样式、冻结三维场景和可复现绘图器。三维尺寸、二维投影、可见/隐藏关系分别记录，与 Analytics 和 PlaneGeometry 分开维护。

当前协议为 1.1.0：完整图示居中，最长边约占 768×768 画布的 86%，至少保留 5% 外边距；点名 18 pt，数值与单位 16 pt，线宽保持 1 pt。Solid01～Solid21 已统一重绘，三维几何、投影与显隐区间保持冻结。调整前后见 [构图对照页](../imports/mathverse_vision_dominant/layout_upgrade_20261010/layout_review.html)，逐题核对见 [构图检查](../imports/mathverse_vision_dominant/layout_upgrade_20261010/validation.json)。

- [REDRAW_PROTOCOL.md](REDRAW_PROTOCOL.md)：构造、投影、遮挡、尺寸标注及验收规则。
- [机器配置](dataset_generator/protocol.json)：768×768 白底、1 pt 黑线、18 pt 点名、16 pt 数值与单位，以及数值容差。
- [公共重绘器](dataset_generator/common_renderer.py)：正交/斜投影、冻结可见区间、圆弧、棱线、面与尺寸标注。
- [通用重绘器检查](dataset_generator/test_renderer.py)：使用独立构造的三维场景，不依赖题目或示例图片。

在 **MathPalette 目录**执行：

```powershell
# 检查三维尺寸、投影、可见区间、错误输入及确定性
python -B SolidGeometry/dataset_generator/test_renderer.py
```

依赖见 [requirements.txt](dataset_generator/requirements.txt)。公共接口为 `draw(scene_path, output_path=None)`；指定 `.svg` 路径导出矢量图，默认写 `reproduced/`。导入不写文件。新增题目时须按协议保存冻结场景及核对报告，分别记录自动核对和图像检查；输入或输出改变时，重新核对。

v1 支持平行投影与显式可见性，不含通用自动消隐、透视或空间关系标记生成器。各类实体需要对应的几何构造和核对。

现已重绘 MathVerse 的 21 道候选（Solid01～Solid21）：用户明确通过的题目写入正式 `dataset.jsonl`，其余保留在 `pending_dataset.jsonl`；原始来源图在 `originals/`，PNG/SVG 在 `image/`，逐题类、三维场景与报告在 `dataset_generator/`。审核进度见 [逐题审核记录](../imports/mathverse_vision_dominant/geometry_review_progress.json)。Agent 检查不代表用户通过，改图后当前版本待重新审核。每道场景分别冻结三维点、投影矩阵和显隐区间，尺寸或标签绑定对应对象；不把解答画入待求量。

在项目根目录执行 `python -B dataset_tools/geometry_dataset.py SolidGeometry Solid01` 可重新生成指定题目并核对确定性。来源题干和 GT 保留；单位、计算、舍入和图示含义疑点另存 `answer_verification`。全批见 [原图 / 重绘对照页](../imports/mathverse_vision_dominant/redraw_review.html) 与 [核验疑点](../imports/mathverse_vision_dominant/issues.md)。

Base / Special 工作台和评测接入尚未启用，现有 Analytics 工作台仍只服务 Ana 系列。此前只有图片的半圆柱样例已按用户要求移除；本批 Solid03 是带完整 MathVerse 题干和来源答案的正式题目。
