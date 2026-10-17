# 二次收集 special_variant 工作台

此工作台读取 `..`，人工 Pass 后保存到 `../special_variant`。Collect 保存整道题的完成状态并从待标注列表隐藏。备份或移动时，将这两个文件夹一起保留。

## 启动与手动标注

双击本目录的 `start_workbench.cmd`，或数据集目录的 `start_special_workbench.cmd`。打开 http://127.0.0.1:8767 。也可以从项目根目录执行：

```powershell
python -X utf8 -B Analytics/workbench/launch_workbench.py
```

启动器会检查 `requirements.txt` 和已通过 recipes 中冻结的环境版本，自动寻找匹配的 Python，并打印实际使用的路径与版本。它会检查当前 Python、项目虚拟环境、本机 Miniconda/Anaconda 和 PATH；也可用 `MATHPALETTE_PYTHON` 指定解释器完整路径。当前正式环境为 Python 3.13.9、Matplotlib 3.11.2、NumPy 2.5.3、Pillow 12.3.0。没有匹配环境时会在渲染前停止并列出版本差异，保留原图和收集记录。

1. 在左侧选择题目，核对原图、题干、答案，点击“打开画板”。题号搜索下方的「来源」可按正式清单中的数据集筛选，默认「全部来源」；与题号搜索及已完成列表的特殊情况筛选组合生效，「上一题／下一题」遵循当前筛选。
2. 选择红点工具并点击放点；辅助线工具点击两个端点或拖动；曲线样式工具点击原曲线，再选择颜色或实线/虚线。
3. 按住 Ctrl 吸附整数格点；勾选吸附可持续启用。画线时 Shift 约束水平/竖直方向。支持撤销、重做、删除、清空。
4. 等待服务器渲染预览，检查实际图片，满意后点画板 Pass。一次 Pass 保存一份 C 变体，同一题可继续收集 C02、C03 等。
5. 整道题完成后，回到工作台点「Collect · 完成收集」。题目从待标注列表隐藏，自动切换到下一题。必须先处理当前待审候选，且至少已有一张通过的 C 图。误 Collect 时展开侧栏「已完成」，在题目旁点「重新打开」即可继续。
6. 误 Pass 的变体可在「本题已收集的 C 图」中点「删除」，再点「确认删除」。已 Collect 的题先重新打开。删除会移除该变体的正式记录，剩余 C 图按原顺序重新编号，并同步图片、插件、recipes、重绘函数和索引。删到零张后可重新 Pass 收集 C01。

删除前的图片、插件和完整 recipes 会保存在工作台的 `deleted_variants/题号/删除记录ID/` 中，`deletion.json` 记录被删除的变体和删除时间。该备份不计入正式数据集。删除途中若服务退出，重启会自动恢复并完成同一事务。

默认红点 `#DC2626`、面积 50 pt²、边宽 1 pt；蓝色辅助虚线 `#2563EB`、宽 1 pt、虚线间隔 `[3.7,1.6]` pt。沿用既有标注标准。

正式结果包括：

```text
Analytics/special_variant/
  accepted_index.jsonl
  Ana01/
    images/C01.png
    plugins/C01.json
    recipes.json
    draw_variants.py
    collection.json
  collected_index.jsonl
  _baselines/
```

插件和 recipes 格式沿用原工作台，保存精确坐标、对象 ID、颜色、线型、参数/图片哈希、人工审核时间。未 Pass 的画板预览不会成为正式数据。C 数量由人工决定，不自动补齐。

## Quick Test

提交候选后，手动点击候选图右上角的测试按钮：

| 按钮 | 模型 | 思考模式 | 服务端凭据 |
| --- | --- | --- | --- |
| Quick Test 1 | MiniMax-M3 | nonthinking | `MINIMAX_API_KEY` |
| Quick Test 2 | MiniMax-M3.1-Flash-Preview | adaptive · low | `MINIMAX_API_KEY` |
| Quick Test 3 | MiMo-V2.6-Flash | nonthinking（`disabled`） | `MIMO_API_KEY` |
| Quick Test 4 | MiMo-V2.6-Flash | thinking（`enabled`） | `MIMO_API_KEY` |

凭据仅由服务端从环境变量或项目根目录 `.env` 读取；按各自 Key 是否配置独立启用按钮。小米使用 Token Plan 专属 Key（`tp-` 或 `ttp-`），接口为 `https://token-plan-cn.xiaomimimo.com/v1`，由 `config.json` 的 `quick_test.mimo_api_base` 指定，不复用 MiniMax 的 Key 或接口。模型与思考模式在 `quick_test.py` 固定。配置变更后重新启动工作台。小米接入与思考开关见[官方 Token Plan 文档](https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/quick-access)和[Chat Completions 文档](https://mimo.mi.com/docs/en-US/api/chat)。

四种模式的回答、思考（如有）、用时和 token 数分别显示并保存，互不覆盖，刷新页面可恢复。每次手动操作仅一次调用，运行期间禁止重复调用，不自动重试或判分，不自动 Pass / Collect。请求只含正式题干和当前候选 PNG；标准答案、原图、说明、标注意图和绘图参数不发送。均不发送 `max_tokens` 或 `max_completion_tokens`，不设置本地等待超时；实际输出长度由模型服务决定，发生长度截断时页面提示。

结果绑定题号、候选 ID、参数和实际 PNG 指纹，分别保存在 `.runtime/analytics_special/quick_tests/`；每种模式保存该候选最近一次测试，切题、替换或审核后不会显示为另一份候选的结果。保留原 Quick Test 1、2 缓存兼容。这些输出属于临时工作记录，不进入正式数据。软件测试使用 mock API，不发送真实模型请求。

## 更新未完成题目与重启

编辑未完成题目的题干、答案、绘图函数或原图后，重新双击数据集目录 `start_special_workbench.cmd` 即可。启动入口会先正常停止当前服务，再启动新服务读取最新输入。原题改动须用户重新审核；既有 Special 不自动获得与新原题兼容的资格。

如果一份待审候选属于旧输入，重启后会将其置为 `stale_input`，保留候选快照，重新等待标注。浏览器草稿只在这道题的输入仍一致时恢复。运行期间继续编辑输入会提示重启；无需手动清空 state 或重设基线。新增题目保持 Ana 编号连续，提供匹配的题目类、原图和 dataset.jsonl 记录后，同样重启读取。

`collection.json` 和 `collected_index.jsonl` 保存完成时间、题目记录和已通过槽位；重新打开会留下收集历史。`_baselines/` 保留历史输入哈希，支持在其他题更新后重绘已保存 C 图；重绘仍核对该题的绘图输入和最终像素。原题类、协议和渲染器需与该题通过时匹配。

## 与 agent 协同

让 agent 先阅读本目录 `agent_prompt.md`。你也可以在画板点击“提交到当前候选”，再让 agent 修改该候选。所有方案最终由你在网页 Pass / No Pass；agent 不代替你审核。

从项目根目录运行：

```powershell
python -B Analytics/workbench/agent_cli.py context
python -B Analytics/workbench/agent_cli.py validate --plugin .runtime/analytics_special/drafts/Ana01/plugin.json
python -B Analytics/workbench/agent_cli.py submit --plugin .runtime/analytics_special/drafts/Ana01/plugin.json --context-token TOKEN
```

使用 context 返回的真实题号、对象 ID、token；修改待审候选时按提示使用 `--replace ID`。不要从旧工作台提交到新服务。

## 重绘与检查

```powershell
python -X utf8 -B Analytics/workbench/launch_workbench.py --check
python -B Analytics/special_variant/Ana01/draw_variants.py C01
```

重绘默认保存到项目 `.runtime/analytics_special/reproduced/`，不覆盖正式图片。函数提供 `draw_C01(output_path=None)`。文本使用 DejaVu Sans，部分中文字形不受支持，优先使用数学标签。


运行状态位于项目 `.runtime/analytics_special/`。正式数据与代码独立；已 Pass 的 recipes 和 Collect 记录可恢复收集状态。题目来自 `Analytics/dataset.jsonl` 的正式清单。草稿路径和删除备份均相对于该运行目录。

## 特殊情况与后期复审

点击题目顶部「特殊标记」，将当前题计入 Collect 完成并切换到下一道未完成题。无需先 Pass 变体；已有通过图保持原样，当前待审候选留在运行状态中，不会自动 Pass 或 No Pass。画板打开或正在生成候选时，先返回工作台并等待生成结束。

侧栏「已完成」显示「特殊情况 · 待复审」，可勾选「只看特殊情况 · 待复审」，点击「复审」重新打开。复审完成后照常 Pass / Collect；再次特殊标记则继续留待后审。重新打开和再次完成会保留历史记录。

标记保存在 `special_variant/<题号>/collection.json` 的 `current.special_case=true`、`current.review_status="pending"`，并同步 `collected_index.jsonl`；完成时间使用 `collected_at`。普通重启及清理运行缓存后仍能恢复特殊完成状态。未通过候选与浏览器草稿仍属于运行数据，清理对应缓存后不保证保留。特殊标记只记录整题的工作进度，不创建变体通过记录，也不改变原题审核。
