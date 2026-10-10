# 二次收集 special_variant 工作台

此工作台读取 `../fine_grained_dataset`，人工 Pass 后保存到 `../fine_grained_dataset/special_variant`。Collect 保存整道题的完成状态并从待标注列表隐藏。备份或移动时，将这两个文件夹一起保留。

## 启动与手动标注

双击本目录的 `start_workbench.cmd`，或数据集目录的 `start_special_workbench.cmd`。打开 http://127.0.0.1:8767 。也可以从 Research 目录执行：

```powershell
python -B MathPalette/Analytics/fine_grained_special_workbench/server.py
```

1. 在左侧选择题目，核对原图、题干、答案，点击“打开画板”。
2. 选择红点工具并点击放点；辅助线工具点击两个端点或拖动；曲线样式工具点击原曲线，再选择颜色或实线/虚线。
3. 按住 Ctrl 吸附整数格点；勾选吸附可持续启用。画线时 Shift 约束水平/竖直方向。支持撤销、重做、删除、清空。
4. 等待服务器渲染预览，检查实际图片，满意后点画板 Pass。一次 Pass 保存一份 C 变体，同一题可继续收集 C02、C03 等。
5. 整道题完成后，回到工作台点「Collect · 完成收集」。题目从待标注列表隐藏，自动切换到下一题。必须先处理当前待审候选，且至少已有一张通过的 C 图。误 Collect 时展开侧栏「已完成」，在题目旁点「重新打开」即可继续。
6. 误 Pass 的变体可在「本题已收集的 C 图」中点「删除」，再点「确认删除」。已 Collect 的题先重新打开。删除会移除该变体的正式记录，剩余 C 图按原顺序重新编号，并同步图片、插件、recipes、重绘函数和索引。删到零张后可重新 Pass 收集 C01。

删除前的图片、插件和完整 recipes 会保存在工作台的 `deleted_variants/题号/删除记录ID/` 中，`deletion.json` 记录被删除的变体和删除时间。该备份不计入正式数据集。删除途中若服务退出，重启会自动恢复并完成同一事务。

默认红点 `#DC2626`、面积 50 pt²、边宽 1 pt；蓝色辅助虚线 `#2563EB`、宽 1 pt、虚线间隔 `[3.7,1.6]` pt。沿用既有标注标准。

正式结果包括：

```text
fine_grained_dataset/special_variant/
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

## 更新未完成题目与重启

编辑未完成题目的题干、答案、绘图函数或原图后，重新双击数据集目录 `start_special_workbench.cmd` 即可。启动入口会先正常停止当前服务，再启动新服务读取最新输入。所有已通过图片、插件和 recipes 保持保存，已 Collect 的题不会再次显示。

如果一份待审候选属于旧输入，重启后会将其置为 `stale_input`，保留候选快照，重新等待标注。浏览器草稿只在这道题的输入仍一致时恢复。运行期间继续编辑输入会提示重启；无需手动清空 state 或重设基线。新增题目保持 Ana 编号连续，提供匹配的题目类、原图和 dataset.jsonl 记录后，同样重启读取。

`collection.json` 和 `collected_index.jsonl` 保存完成时间、题目记录和已通过槽位；重新打开会留下收集历史。`_baselines/` 保留历史输入哈希，支持在其他题更新后重绘已保存 C 图；重绘仍核对该题的绘图输入和最终像素。原题类、协议和渲染器需与该题通过时匹配。

## 与 agent 协同

让 agent 先阅读本目录 `agent_prompt.md`。你也可以在画板点击“提交候选，交给 agent”，再让 agent 修改该候选。所有方案最终由你在网页 Pass / No Pass；agent 不代替你审核。

从 Research 目录运行：

```powershell
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py context
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py validate --plugin MathPalette/Analytics/fine_grained_special_workbench/drafts/Ana01/plugin.json
python -B MathPalette/Analytics/fine_grained_special_workbench/agent_cli.py submit --plugin MathPalette/Analytics/fine_grained_special_workbench/drafts/Ana01/plugin.json --context-token TOKEN
```

使用 context 返回的真实题号、对象 ID、token；修改待审候选时按提示使用 `--replace ID`。不要从旧工作台提交到新服务。

## 重绘与检查

```powershell
python -B MathPalette/Analytics/fine_grained_special_workbench/server.py --check
python -B MathPalette/Analytics/fine_grained_dataset/special_variant/Ana01/draw_variants.py C01
```

重绘默认保存到工作台 `reproduced/`，不覆盖正式图片。函数提供 `draw_C01(output_path=None)`。文本使用 DejaVu Sans，部分中文字形不受支持，优先使用数学标签。
