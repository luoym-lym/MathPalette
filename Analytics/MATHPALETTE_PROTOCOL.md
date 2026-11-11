# Analytics 制作与变体协议

版本：3.1.0。当前保留 590 道正式题，题号为连续的 Ana01～Ana590；来源与题干以 `dataset.jsonl` 为准，所有文件与插件使用同一题号。

Ana547～Ana566 为 2026-11-11 用户明确批量授权的 Author Designed 原题，每题包含一份同步设计并授权直接 Pass 的 C01。记录见 [`analytics_author_special20_20261111.json`](../provenance/analytics_author_special20_20261111.json)，不冒称逐题人工审核。

2026-11-11 用户以“放进去吧”明确批准将已交付的 6 道 Analytics 新原创题 Ana567～Ana572 加入 Author Designed，沿用“设计的变体直接pass就好”的指令保存 7 份 Special（Ana567 为 C01、C02，其余每题 C01）。Pass 仅代表授权保存；本轮视觉实测只有 Ana567/C02 达到预设双样本条件，不代表其他变体有效或逐题人工审核。未执行 Collect。授权、设计与事务凭据见 [`analytics_author_visual6_20261111.json`](../provenance/analytics_author_visual6_20261111.json)。

2026-11-11 用户要求“再进行一轮”，继续此前 Author Designed 入库与“设计的变体直接pass就好”的授权，新增 Ana573～Ana578 六道原题及七份 Special（Ana577 为 C01、C02，其余每题 C01）。本轮参考已 Collect 题目；Ana576/C01、Ana578/C01 达到预设双样本视觉误读条件，Ana577 两份变体均一对一错，Ana573～Ana575 对照因连接失败未完整，效果未验证。Pass 不代表逐题人工审核或稳定诱导效果；未执行 Collect。凭据见 [`analytics_author_collect6_20261111.json`](../provenance/analytics_author_collect6_20261111.json)。

2026-11-11 用户要求“你从已经收录的题目里面进行扩展就好”“可以多做一些”，继续 Author Designed 入库和直接 Pass 授权，新增 Ana579～Ana590 共12道母题扩展，每题C01，母题为Ana576、Ana578、Ana548、Ana567。Ana579、Ana581、Ana582、Ana588、Ana590 的C01达到本轮双样本条件（Ana581有附带FINAL矛盾，已保留说明）；Ana580原图对照失误，变体未测，其余未达条件。未执行Collect，不冒称逐题人工审核或稳定有效。母题映射、授权与实测凭据见 [`analytics_author_extensions12_20261111.json`](../provenance/analytics_author_extensions12_20261111.json)。

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
