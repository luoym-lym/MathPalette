# Analytics 制作与变体协议

版本：3.0.0。当前仅保留 45 道正式题。DynaMath 使用 Ana01～Ana20，MathVerse 使用 Ana21～Ana45；所有文件与插件使用同一题号。

## 原题

原题必须经用户明确确认。正式清单为本目录 `dataset.jsonl`，根目录清单为自动汇总。未通过新题在独立暂存区制作。每题 class 记录真实 `source_dataset`、题干、答案和答案类型，绘图参数冻结，不在导入或重绘时随机。

原图沿用 `dataset_generator/protocol.json`：768×768、不透明白底、等比例坐标 `[-8,8]²`。题目脚本在 `dataset_generator/questions/function_plotNN.py`，公共绘图器在上一级。使用 `draw(num=0, output_path=None)`；正式输入不得被临时重绘覆盖。

`provenance/approvals.json`（项目根目录）保存用户通过原话、时间及内容指纹。内容改变须重新审核。来源截图在 `originals/`；旧 DynaMath 来源截图缺失，不使用重绘图冒充。

## Base


每题抽取四种不同操作，按抽取顺序编号 `base_1`～`base_4`。**每张从原图独立生成，只做一个操作，不叠加前一张改变。** 离散选项等概率抽样；连续区间均匀抽样。

| 操作 | 规则与参数 |
| --- | --- |
| Base1 修改网格 | 二选一：`off` 关闭全部网格；`half_density` 仅保留 `-8,-6,-4,-2,0,2,4,6,8` 网格线。刻度短线和数字保持原样。 |
| Base2 隐藏刻度数字 | 隐藏 x/y 两轴刻度数字和单独原点 `0`；保留坐标轴、刻度短线、网格、轴名和原有数学标签。内部无随机参数。 |
| Base3 标准蓝背景 | 画布、绘图区、刻度数字及原点背景遮罩改成 **`#0000FF`**。原数学对象颜色、白底空心点保持原样。不是浅蓝色；内部无随机参数。 |
| Base4 随机虚线 | 每张 1 条；水平/竖直/斜线三选一；绿 **`#00FF00`**、红 **`#FF0000`**、黄 **`#FFFF00`** 三选一。线宽 1 pt，虚线 `[4,3]` pt。在 `[-8,8]²` 随机取锚点；斜线角度绝对值 `5～85°`、正负等概率；直线裁剪到视窗边界，保存实际端点。 |
| Base5 随机形状 | 每张 1 个椭圆/矩形/三角形。**中心 x、y 各在 `[-6,6]`**；宽高各在 **`[0.8,2.5]`** 坐标单位；旋转角度 **`[0,360)`**。黑色 `#000000`、1 pt 实线、无填充。宽高是旋转前外接框全长。椭圆保存中心/宽高/角度；多边形保存最终顶点。三角形底边位于局部框下边、顶点在上边，顶点横向偏移取 `[-width/3,width/3]`。这些范围保证任意旋转后完整位于 `[-8,8]²`。 |
| Base6 游离点 | 点数从 1、2、3 抽一个；从 `{-8,…,8}²` 不放回抽整数位置，各点独立二选一实心/空心。圆点面积 36 pt²、黑色边框 1 pt；实心填黑、空心填白。边界点允许被绘图区裁剪。 |

不按题型、答案、曲线、坐标轴、文字或关键点避让；允许相交与重叠。只检查可渲染、尺寸正确、参数有效、图像有变化且本题四张不重复；不根据模型是否答对筛选。无变化时仅重抽同一操作参数，最多 32 次，失败明确报错，不换操作补数。

Base 沿用原题题干和标准答案。实验观察到的歧义或语义变化单独记录，不反向改写原题真值。


## 重绘与校验

在项目根目录运行：

```powershell
python -X utf8 -B Analytics/dataset_generator/generate_base_variants.py check --redraw
python -X utf8 -B Analytics/base_variant/Ana21/draw_variants.py base_1
python -X utf8 -B dataset_tools/catalog.py check
```

Base 包保留 images、plugins、recipes、draw_variants.py 和可重建全局索引。冻结实际参数；重绘不重新抽样。recipes 保存输入、执行器、协议、图片哈希和依赖版本，使用 `status="generated"`，不冒充人工通过。

## Special

工作台在 `Analytics/workbench/`，启动入口为 `Analytics/start_special_workbench.cmd`，端口 8767。用户制作、预览、Pass 单张、Collect 整题；数量由用户决定。保存 `special_variant/<id>/` 的图片、插件、recipes、重绘入口和 collection，原 Pass/Collect 时间保留。

运行状态、草稿、候选和预览位于项目 `.runtime/analytics_special/`，不混入正式清单。服务停止后可清理不需要的运行状态；工作台从正式 recipes 与 collection 恢复已收集进度。原题批准和 Special Pass/Collect 独立。
