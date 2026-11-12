# MathPalette 绘图协议 2.0

所有 1516 道正式题均由自己的 Python 类构图。解析、平面、立体分别使用 `ANALYTICS`、`PLANE`、`SOLID` 配置，共用一个实现：[dataset_tools/drawing.py](dataset_tools/drawing.py)。来源名称只表示题源，不再选择绘图器。

## 每题接口

`dataset.jsonl` 的 `script` 指向唯一题目类。题号、来源、题干、答案、答案类型和选择题选项保存在类属性中，与正式清单一致。`draw()` 内直接调用协议工具构图；不读取来源图片，不执行旧 renderer，也不再通过 JSON 场景转发绘图。

```python
from dataset_tools.drawing import Canvas, PLANE

class Example:
    def draw(self, output_path):
        points = {"A": (0, 0), "B": (4, 0), "C": (1, 3)}
        with Canvas(PLANE, xlim=(-2, 6), ylim=(-2, 6)) as c:
            c.line([points[n] for n in ("A", "B", "C", "A")], id="triangle")
            for name, xy in points.items():
                c.text(name, xy, offset_pt=(0, 12), vertex=True)
            return c.save(output_path)
```

正式类使用 `draw(output_path=None, *, variant=None)`：省略路径时写 `.runtime/reproduced/<分支>/<题号>.png`；`variant="C01"` 重放当前已 Pass 槽位。`_canvas=True` 及 `build_scene()` 是工作台捕获接口，普通使用只需 `draw()`。

已有完整浮点坐标、曲线采样和矢量路径保留在各类中，避免统一协议时重新拟合。几何题的原冻结场景继续保留，用于审计几何条件；`get_scene()` 仅提供读取接口，绘图本身不依赖该文件。立体仍分别冻结三维几何、投影及显隐区间；涉及三维构图时在同一个 `Canvas` 上用 `project()` 投影，不能从二维外观反推空间条件。

## 公共工具

| 工具 | 用途 |
| --- | --- |
| `Canvas(协议, xlim=..., ylim=...)` | 固定画布、视窗和默认样式；用 `with` 隔离绘图设置 |
| `line(points, id=..., **style)` | 折线、线段或线段集合；曲线由题目给出冻结采样 |
| `point(points, filled=True, **style)` | 实心或空心点 |
| `path(vertices, codes, **style)` | Bézier 等矢量路径；少量历史箭头保留固定页面坐标 |
| `circle(center, radius)` / `arc(center, radius, start, end)` | 圆及角度制圆弧 |
| `fill(points, **style)` | 多边形或区域填充 |
| `text(text, xy, offset_pt=..., vertex=False)` | 文本、点名和以 pt 冻结的页面偏移 |
| `project(xyz)` | 使用已冻结的 2×3 平行投影；不做自动消隐 |
| `save(path)` | 生成 PNG；同时保留 SVG 导出能力 |

样式参数沿用 Matplotlib 的常用参数，不另设样式语言、来源适配层或插件注册系统。`id` 绑定实际矢量对象，供工作台选择及覆盖外观；同一对象分成显隐片段时可重复使用同一 ID。数学构造、关系标记和采样规则写在题目类中，不继续往公共工具里叠加题型特例。

固定输出为 768×768、100 dpi、不透明白底，禁止紧裁切和自动缩放；视窗须为方形，等比例坐标。解析配置默认显示坐标网格和坐标轴；平面与立体默认隐藏坐标轴。历史题保留其冻结样式覆盖，新题沿用对应分支的几何语义与审核要求。环境依赖继续固定于根目录 `requirements.txt`。

## 入口和验证

在项目根目录执行：

```sh
.venv/bin/python -B dataset_tools/draw_question.py Analytics Ana01
.venv/bin/python -B dataset_tools/draw_question.py PlaneGeometry Plane01 --output .runtime/Plane01.png
.venv/bin/python -B dataset_tools/draw_question.py SolidGeometry Solid249 --variant C01
.venv/bin/python -B dataset_tools/catalog.py check
.venv/bin/python -B dataset_tools/test_drawing.py
```

原逐题脚本可直接执行；`dataset_tools/geometry_dataset.py`、`author_redraw.py` 和分支 `common_renderer.draw()` 保留为统一入口的薄封装。带场景路径的旧接口只接受正式冻结场景，防止忽略传入的改图内容。输出写项目 `.runtime/` 或项目外的指定目录，不能覆盖正式输入。

工作台也从同一个类捕获实际对象。`dataset_generator/contexts/<题号>.json` 只保存对象别名、吸附点及重绘校验指纹，不是另一套绘图场景。原对象整体和局部样式修改继续在实际矢量路径上进行；外观覆盖不更改冻结的三维几何、投影或可见性。

历史 Special 的冻结矢量构图位于各题 `special_variant/<题号>/unified_drawings.py`，使用相同协议。原插件、recipes、PNG、Pass 和 Collect 记录保留。新 Pass 仍冻结插件和输入清单后严格验证像素；删除槽位后的重排按不可变内容匹配历史构图，不重新制造 Pass。

## 本轮迁移

本轮按用户明确要求整合，保留全部现存原图、来源图及 Special PNG 字节。1516 张原图加 1297 张 Special 中，2754 张重绘与原 PNG 的 RGBA 完全一致；19 张原图和 40 张 Special 有最多 2/255 的通道差异。迁移核验冻结这些具体重绘指纹，不对后续任意差异放宽容差；`matches_accepted` 始终表示严格像素一致，`migration_verified` 单独表示命中已核验迁移。

原批准原话、时间、题干、答案及所有 Pass/Collect 状态保留，表示迁移保留新旧内容指纹，不产生新的数学审核。凭据及逐样本差异见 [迁移记录](provenance/drawing_protocol_integration_20261112.json)。旧绘图源码、校验器及旧测试完整归档于 [v1 源码归档](provenance/drawing_protocol_v1.tar.gz)，逐文件 SHA-256 见 [归档清单](provenance/drawing_protocol_v1.json)。它们退出运行依赖。

正式评测快照 `MathPalette_Dataset/` 及两份模型推理脚本不随本轮重绘协议迁移更新，继续使用原冻结 PNG。
