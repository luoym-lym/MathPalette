# MathPalette 绘图协议 2.1

每题一个 `MathPalette_Dataset/questions/<题号>.py`，类名为正式题号。题干、答案及选项与 `dataset.jsonl` 保持一致，几何坐标、曲线采样、投影、显隐片段和标注偏移直接冻结在类中。导入模块不生成图片。

```python
from MathPalette_Dataset.drawing import Canvas, PLANE

class Example:
    def draw(self, output_path):
        with Canvas(PLANE, xlim=(-2, 6), ylim=(-2, 6)) as c:
            points = [(0, 0), (4, 0), (1, 3)]
            c.line([*points, points[0]], id="triangle")
            c.text("A", points[0], offset_pt=(0, -12), vertex=True)
            return c.save(output_path)
```

正式类使用 `draw(output_path=None, *, variant=None)`。`variant=None` 画原图，`variant="C01"` 调用同一类的 `draw_C01()`。只有该题已收录的 Special 才能调用。默认写入项目 `.runtime/reproduced/`，单题绘图禁止覆盖正式数据目录；通过显式 `draw.py rebuild` 更新正式图片及清单。

## 最小公共工具

实现集中于 `MathPalette_Dataset/drawing.py`，三个配置分别为 `ANALYTICS`、`PLANE`、`SOLID`，不按题源选择绘图器。

| 接口 | 用途 |
| --- | --- |
| `Canvas(协议, xlim=..., ylim=...)` | 固定画布、方形视窗和样式，用 `with` 隔离状态 |
| `line(points, **style)` | 线段、折线、冻结采样曲线和线段集合 |
| `point(points, filled=True, **style)` | 实心或空心点 |
| `path(vertices, codes, **style)` | Bézier 等矢量路径 |
| `circle(center, radius)` / `arc(center, radius, start, end)` | 圆和角度制圆弧 |
| `fill(points, **style)` | 多边形和区域填充 |
| `text(text, xy, offset_pt=..., vertex=False)` | 文本、点名及 pt 偏移 |
| `project(xyz)` | 冻结的 2×3 平行投影 |
| `save(path)` | 不透明 PNG，亦支持 SVG 导出 |

图元可设 `id`，样式使用 Matplotlib 的常用参数。数学构造和题型特例放在题目类中，公共工具不增加来源适配器或新的样式语言。长坐标序列只表示冻结矢量几何，不使用图片回放。

## 固定约定

输出 PNG 为 768×768、100 dpi、不透明白底；保持等比例坐标，不自动缩放或紧裁切。解析配置默认有坐标网格，平面和立体默认隐藏坐标轴。历史题保留已冻结的样式参数，Special 的文字、颜色、实虚线和局部片段也由类内代码明确表达。

平面构图保持点、线、角、圆、区域和标签的明确数学关系，不从视觉比例推测并添加条件。立体分别保留真实几何、投影及可见/隐藏片段；`project()` 只做投影，不进行自动消隐。页面偏移和二维投影长度不能代替真实空间长度。

本次剪枝按用户确认，以新代码绘制的 PNG 为准，已同步刷新所有图像指纹。后续全量复现要求与这些新 PNG 完全一致，不再保留旧图灰阶容差或旧 renderer 兼容层。题干、答案或数学构造的内容修改仍需用户确认，重建不等于批准新题或 Pass/Collect。

```sh
.venv/bin/python -B MathPalette_Dataset/draw.py check --redraw
.venv/bin/python -B MathPalette_Dataset/draw.py rebuild
```

依赖固定于根目录 `requirements.txt`，运行环境见 `metadata.json`。正式评测直接使用冻结 PNG；只在显式重建时绘图。
