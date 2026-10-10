# MathPalette 视觉变体审核工作台

本项目实现 `REQUIREMENTS.md` 中的 A1～A4、B1～B5、本地审核流程与确定性重绘。目标是每题人工收录 A=5、B=5，共 80 题、800 张变体。**正式初始通过数为 0；测试数据仅在独立临时目录中生成。800 张正式通过图需要用户逐张审核。**

## 启动

Windows 双击本目录中的 **`start_workbench.cmd`**。它检查固定版本的绘图依赖，必要时在本目录建立 `.venv` 并安装 `requirements.txt`，随后打开 `http://127.0.0.1:8765`。已安装依赖后，工作台运行不需要网络、前端构建工具或外部服务。

也可以在本目录执行：

```powershell
python -m pip install -r requirements.txt
python -B server.py --open-browser
```

需要 Python 3.12 或更新版本；本次验证环境为 Python 3.13.9、Matplotlib 3.11.2、NumPy 2.5.3、Pillow 12.3.0。为了像素复现，继续审核和重绘应使用同一 Python 与绘图依赖版本。推荐保留当前已能一致重绘原图的环境。

启动时先核对全部输入文件的 SHA-256，再检查 80 题的原场景与操作可用性，首次检查约需十几秒。后续启动复用同基线、配置和依赖环境的检查缓存。若原代码无操作重绘与原图不同，服务会明确报错并停止，不覆盖原图或更换基线。

保持服务窗口打开。在窗口按 Ctrl+C 可停止，重新启动会恢复位置、阶段、通过结果与尚未审核的同一候选。一个状态目录同时只允许一个写入服务。

端口被占用时可运行 `python -B server.py --port 8767`，然后打开提示地址。停止服务后，可用 `python -B server.py --check` 检查输入与可用性，不生成候选。已经启动服务时，直接使用该服务窗口，不重复启动。

## 审核

1. 首次从 Ana01 / A 类型覆盖 / A1 开始。原图与候选并排显示，点击“原始尺寸”查看 768×768 图片；题目全文、可折叠答案和冻结参数均在页面中。
2. **Pass** 直接保存当前展示的候选 PNG，不重新采样或重绘。图像、参数、函数、索引与进度持久保存后才计入通过数。
3. **No Pass** 删除当前候选 PNG，保留轻量拒绝记录以避免重复。覆盖阶段继续当前类型；有限结果已用尽时进入下一类型。
4. **跳过此类型** 记录本题此操作的跳过状态和可选原因，不计为通过。“类型覆盖与可用性”中可点击“恢复尝试”。不可用、耗尽和跳过原因均可查看。
5. 覆盖阶段按 A1～A4 / B1～B5 顺序尝试。能通过的操作尽量先收录一张，随后从同组仍有新候选的操作随机补足。A 满 5 后才进入 B；两组均满 5 后自动进入下一题。
6. A01～A05、B01～B05 按本组实际通过顺序分配，不绑定操作类型。具体操作和 `coverage` / `fill` 阶段写在各图的方案中。
7. 一个组没有剩余可用类型且仍不足 5 时，显示待处理和缺口。可以恢复跳过的类型，也可以通过列表或上一题/下一题离开，已有结果会保留。

所有变体都从原始场景独立构建，只做一次指定操作。候选与原图、已通过图、被拒绝图按**解码像素哈希**去重。A1 只有两种网格，A2 只有一个结果，A4 只有两种颜色，用尽后不再重复展示。随机构造默认最多尝试 32 次，失败会显示原因并提供重试和跳过。

审核按钮在生成、保存与图片载入期间禁用。只有当前 `candidate_id` 的图片成功载入后才允许提交，避免把尚未显示的新图当作当前图审核。旧候选请求无法操作新候选；相同决定的重复请求不会重复计数。

左侧和顶部显示全局通过数、完成题数、待审核槽位、实际操作使用次数及尚未补足的大类。下方展示本题 10 个槽位，点击通过图缩略图可查看完整冻结方案。

## 输入与整数点验证

`../first_process/` 是只读输入。本工作台不调用原批量生成入口、不重新采样题目参数、不写入原图目录。80 个原题类仍保留在原来的四个源文件中；类按 `dataset.jsonl` 的 Ana 题号通用加载，不使用逐题插件或题号分支。

原题 `finalize()` 仅在一次受锁保护的绘制中被截获，原图坐标锁定后才应用操作。截获绑定通过 `finally` 恢复。变体保存不再次调用原 `finalize()`，因此 A2 的刻度数字和 A4 的背景不会被恢复。

对于 `y=f(x)`，适配器重放原 `draw()` 的相同数学计算，把定义域中的输入换为整数 x，再用 `1e-8` 容差验证 y 是否为整数。圆、椭圆和多边形轮廓使用实际几何定义验证。不会从图片猜点、插值取整或把曲线采样点当作显式原有点。整数点身份、对应曲线和验证方式记录在检查数据与方案中。

当前已审核输入的预检查结果：

| 操作 | 可生成的题目数 |
| --- | ---: |
| A1～A4、B1、B2 | 各 80 |
| B3 | 20 |
| B4 | 64 |
| B5 | 62 |

Ana01 没有显式点，B3 不可用；原正弦曲线的整数点 (0, 0) 可用于 B5，但没有非退化投影可用于 B4。仅通过辅助线绘制、适配层未能验证数学定义的曲线会显示“不支持该几何验证”，例如当前 Ana48 的 B5，不宣称数学上不存在整数点。该题仍可用其他 B 操作补足。

“是否无关、是否仍可解答、答案是否不变”由人工判断，服务只检查几何与渲染有效性。

## 保存、备份与恢复

首次运行按需建立下列输出，全部在工作台目录内：

```text
state/baseline_manifest.json     原始输入文件哈希及基线指纹
state/availability.json          原场景预检查、各操作状态、覆盖和缺口
state/progress.json              当前位置、候选、审核历史与通过记录
candidates/<candidate_id>.png    尚未审核的候选
accepted/AnaXX/recipes.json      该题完整通过方案
accepted/AnaXX/draw_variants.py  已通过槽位的真实函数入口
accepted/AnaXX/images/A01.png    按组内通过顺序保存的 PNG
accepted_index.jsonl             全部正式通过方案索引
reproduced/                      默认重绘输出
```

每张方案包括题号、槽位、类别、操作、阶段、候选 ID、追溯种子、完整实际构造参数、图片像素哈希、审核时间、版本、环境与基线指纹。种子不参与重绘。

每次审核立即落盘。保存使用同目录原子替换，并通过 `state/pending_transaction.json` 记录可恢复事务；服务重启或点击重试会继续完成尚未完成的保存/删除。若磁盘写入或文件删除失败，界面会提示，不把失败当成通过。不要手动删除待恢复事务或进度文件。

No Pass 只会删除经过路径解析和边界验证的**单个当前候选 PNG**，不会删除原图、通过图或整个目录。已审核拒绝图不永久保留 PNG。尚未审核的候选随导航保留，以便返回时恢复同一张图。

备份时先停止服务，然后复制整个工作台目录，至少包含 `state/`、`accepted/`、`accepted_index.jsonl` 和尚未审核的 `candidates/`；同时保留对应的 `first_process/` 与依赖环境。恢复时放回相同目录关系再启动。运行产生的审核文件在本目录 `.gitignore` 中忽略，**Git 提交不替代审核数据备份**。

审核开始后不要更改影响生成的 `config.json` 设置、原始输入或绘图依赖；服务会检测不一致，避免混入不同环境下的结果。正式输出图片丢失或被修改时会报错，应从备份恢复。

## 确定性重绘

通过一个槽位后，该题 `draw_variants.py` 增加对应函数；未通过的槽位没有占位函数。该题完成时恰好有 `draw_A01`～`draw_A05` 和 `draw_B01`～`draw_B05` 十个入口。

在工作台目录执行：

```powershell
python -B accepted/Ana01/draw_variants.py A01
python -B accepted/Ana01/draw_variants.py A01 --output reproduced/Ana01/custom.png
python -B generate_variants.py redraw accepted/Ana01/recipes.json A01 --output reproduced/Ana01/another.png
```

Python 调用示例：

```python
import importlib.util
from pathlib import Path

path = Path("accepted/Ana01/draw_variants.py").resolve()
spec = importlib.util.spec_from_file_location("ana01_variants", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.draw_A01()                         # 默认写入 reproduced/Ana01/A01.png
module.draw_A01("reproduced/custom.png")   # 自定义输出路径
```

这些入口读取 `recipes.json` 的冻结参数，调用与候选相同的绘制实现。重绘过程中不选择新操作、不采样位置、不随机颜色或布局。重绘先验证像素哈希，只有与通过图相同才写入输出；禁止覆盖原始输入和正式通过 PNG。

也可独立生成一张**未审核**候选供检查，不计入正式配额：

```powershell
python -B generate_variants.py candidate Ana09 B5 --seed 123 --output reproduced/unreviewed-demo.png
```

相邻 JSON 保存完整参数、候选身份、哈希及 `unreviewed` 状态。正常收集请使用工作台的 Pass / No Pass。

## 功能验证

```powershell
python -B -m unittest -v test_workbench
```

测试使用单独的系统临时目录，覆盖有限操作拒绝后耗尽、候选删除、精确保存、重复和过期请求、并发双击、跳过/恢复、导航/重启、缺失候选的冻结重建、失败后的事务恢复、整数点来源、网格与刻度、独立原点 0、浅色背景及遮罩、所有三种形状，以及原文件哈希不变。

完整收集测试在隔离目录中模拟 80 题共 800 次通过，验证每题 A=5/B=5、800 条索引和 800 张图片，实际调用全部 **800 个**交付函数并核对重绘像素。测试结束删除模拟结果；这些结果不代表人工审核通过，不写入正式目录。测试运行可能需要几分钟。

浏览器功能验证也使用独立的 `--data-dir`。该选项用于隔离输出，例如 `python -B server.py --data-dir C:/Temp/mathpalette-review-test --port 8766`；页面逻辑与正式工作台相同。
