# 原题审核工作台验证

本分支以本地 `master` 为正式数据和公共工作台基线。旧文档中的 142 道正式题、731 道待审核题和 Base 兼容检查不再作为当前状态或验收条件。

## 验证范围

- 正式数据、原图、绘图输入、审核指纹和 Special 包与 `master` 比较；不新建真实批准记录。
- 三个 Special 工作台的公共文件恢复为 `master` 版本，移除旧 Base 和旧绘图器兼容桥。
- 原题 Pass/Delete 的列表、详情、内容变化拒绝、幂等性、事务回滚、进程中断恢复、并发编号和 HTTP 检查在独立临时副本执行。
- 候选转正式记录的 schema、来源、编号和独立重绘使用当前仍在待审核清单中的代表题。
- 测试按当前正式清单推导下一题号，按当前候选清单选择绘图家族，不恢复历史候选来凑固定测试数量。
- 当前已无待审核立体题；依赖立体候选的测试明确跳过，不记为执行通过。

## 运行命令

本轮验证（2026-10-20，正式基线 `master`：`fdcecc96`）：正式目录和审核指纹检查通过，251 道原题、144 张 Special、0 Base；启动环境匹配。Python 共 16 项，14 项通过、2 项因无待审核立体题而跳过；前端 7 项通过，两份前端脚本语法检查通过。

```powershell
python -X utf8 -B dataset_tools/catalog.py check
python -X utf8 -B review_workbench/launch_workbench.py --check
python -X utf8 -B -m unittest discover -s review_workbench/tests -v
node --test review_workbench/tests/test_review_core.cjs
node --check review_workbench/static/app.js
node --check review_workbench/static/review-core.js
```

以上软件测试不能代替用户原题审核。合成测试批准仅存在于临时副本中，不进入正式数据。浏览器交互未在本轮重新验证；合成浏览器测试的运行条件见 `tests/FRONTEND_TESTING.md`。
