# Analytics 制作与变体协议

版本：3.1.0。当前仅保留 51 道正式题，题号为 Ana01～Ana51；来源与题干以 `dataset.jsonl` 为准，所有文件与插件使用同一题号。

## 原题

原题必须经用户明确确认。正式清单为本目录 `dataset.jsonl`，根目录清单为自动汇总。未通过新题在独立暂存区制作。每题 class 记录真实 `source_dataset`、题干、答案和答案类型，绘图参数冻结，不在导入或重绘时随机。

原图沿用 `dataset_generator/protocol.json`：768×768、不透明白底、等比例坐标 `[-8,8]²`。题目脚本在 `dataset_generator/questions/function_plotNN.py`，公共绘图器在上一级。使用 `draw(num=0, output_path=None)`；正式输入不得被临时重绘覆盖。

`provenance/approvals.json`（项目根目录）保存用户通过原话、时间及内容指纹。内容改变须重新审核。来源截图在 `originals/`；旧 DynaMath 来源截图缺失，不使用重绘图冒充。

## Base

与平面、立体分支一致，Base 尚未启用。当前通过 Special 工作台制作和收集变体。

## 重绘与校验

在项目根目录运行：

```powershell
python -X utf8 -B dataset_tools/catalog.py check
```

## Special

工作台在 `Analytics/workbench/`，启动入口为 `Analytics/start_special_workbench.cmd`，端口 8767。用户制作、预览、Pass 单张、Collect 整题；数量由用户决定。保存 `special_variant/<id>/` 的图片、插件、recipes、重绘入口和 collection，原 Pass/Collect 时间保留。

运行状态、草稿、候选和预览位于项目 `.runtime/analytics_special/`，不混入正式清单。服务停止后可清理不需要的运行状态；工作台从正式 recipes 与 collection 恢复已收集进度。原题批准和 Special Pass/Collect 独立。
