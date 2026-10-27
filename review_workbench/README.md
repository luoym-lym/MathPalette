# MathVerse 原题审核工作台

这是独立的本地原题审核页面。待审核候选保存在 `review_candidates/mathverse/`，数量以当前 `index.jsonl` 为准。首次启动、浏览、筛选和预取图片不会批准或删除题目。正式数据、审核协议和三个 Special 工作台以本地 `master` 为准。

## Windows 启动

在项目根目录双击 **start_mathverse_review.cmd**。默认地址为 http://127.0.0.1:8770/ 。保持命令窗口开启，关闭时按 Ctrl+C。

启动器会检查现有 Python、项目 `.venv` / `venv` 和已登记的 Conda 环境。它不联网、不自动安装软件。严格重绘参考环境：

- CPython 3.13.9
- NumPy 2.5.3、Matplotlib 3.11.2、Pillow 12.3.0
- Matplotlib 随附 FreeType 2.14.3

缺少环境时，先安装 CPython 3.13.9，再在项目根目录自行运行：

```bat
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r review_candidates\mathverse\requirements.txt
start_mathverse_review.cmd
```

`py -3.13` 指向的实际补丁版本也必须为 3.13.9。使用其他已有环境时：

```bat
set MATHPALETTE_PYTHON=C:\path\to\python.exe
start_mathverse_review.cmd
```

只检查环境、不启动服务：`start_mathverse_review.cmd --check`。
端口被占用时：`start_mathverse_review.cmd --port 8771`。
不要把服务暴露到局域网或公网；它只允许绑定 127.0.0.1。

## 审核内容与按钮

页面并排显示来源原图与代码重绘图，并区分来源题干/答案、当前改编题干/答案、独立核验推导及核验限制。自动数学检查和像素检查都不等于用户批准。`needs_manual_confirmation` 明确表示仍需人工判断，不能当作已独立证明。

- **Pass**：你明确批准当前画面所绑定的原题内容。后端重新核对该题内容指纹，在独立临时目录只重绘一次并逐像素比对，然后分配下一个 Ana / Plane / Solid 题号，复制独立运行依赖，记录 `instruction="Pass"` 的用户批准，调用正式审核工具完整核验和更新索引。成功后才进入下一题。
- **Delete**：二次确认后直接删除当前候选的逐题目录及候选清单条目。它不删除正式题，也不影响其他候选。这个按钮不能撤销；历史中仅保留必要决定记录。
- 正在提交时按钮禁用。错误会留在当前题。网络返回不确定时显式重试同一操作会复用 request_id，不会重复入库或重复分配题号。
- 原题、答案、图片、场景、证据或实际绘图依赖在显示后被修改时，旧指纹会被拒绝，需重新打开此题。

通过后，正式图片、原图、脚本、场景及分族依赖位于对应正式分支。正式脚本不依赖候选目录；源题定位和原始证据保留于正式来源记录。已通过/已删除历史可刷新查看，但删除后的原图不会被另行保留。

## 性能与事务

候选列表只读一份轻量 JSONL 和决定状态，不读全部候选图片、不全量重绘。详情只散列当前题和其实际依赖；图片按内容哈希缓存。Delete 不调用 Git、不扫描全仓库 AST、不重绘。Pass 保留完整正式题库校验，不以性能为由跳过批准指纹。

所有修改使用与三个 Special 工作台相同的跨进程 catalog 锁；内层审核函数明确复用已持有的锁，不重入。正式编号、批准记录、两级清单、来源记录和候选移除构成一个持久事务。每次写入前记录准确的前后哈希和备份，重启会回滚未提交操作或保留已经提交的成功结果。恢复发现外部修改时会停止并报告 `recovery_required`，不会覆盖这些修改。

完整校验在每轮读取一次来源记录快照，并在结束时检查快照是否被外部修改；每道题的批准指纹仍逐一验证。审核工作台等待 catalog 锁最多 120 秒，页面为提交操作保留更长等待时间，避免题库增长或并发审核时过早超时。

`review_candidates/mathverse/review_state.json` 是实际操作后的持久历史/幂等状态，不是审核批准的替代来源；正式批准仍以 `provenance/approvals.json` 为准。进行中的恢复数据在 `.runtime/review_workbench/transactions/`。若程序异常退出，请先重新启动恢复，不能在恢复前手动清空 `.runtime/`。

## 验证和独立复现

```bat
.venv\Scripts\python.exe -B -m unittest discover -s review_workbench/tests -v
.venv\Scripts\python.exe -B dataset_tools/catalog.py check
```

测试会创建独立临时副本，绝不对实际待审核题目或正式题库执行 Pass/Delete。测试按当前候选家族和正式编号选择夹具；已无待审核题目的分支会明确跳过。更完整的测试记录见 `VALIDATION.md`。

高级启动（用你已验证匹配的 Python）：

```bat
python -X utf8 -B review_workbench/server.py --no-browser --port 8770
```

`--root <另一份完整项目目录>` 用于隔离测试；此参数决定全部候选、正式数据、静态页面和事务路径。

### 新题正式脚本与旧几何辅助入口

新题通过后，请使用对应正式 `dataset.jsonl` 中的 `script` 入口，并传入临时输出 PNG 路径。脚本会读取正式场景及随题记录的分族绘图依赖；不需要保留候选目录。三个 Special 工作台同样使用原生场景，支持这些分族对象。题号以实际通过后分配的 Ana / Plane / Solid 编号为准，不能使用 MV 候选号。

例如，仅在 `Plane72` 已正式通过且该记录的 `script` 为下列路径时：

```bat
python -B PlaneGeometry/dataset_generator/plane_plot72.py .runtime/reproduced/Plane72.png
```

旧 `dataset_tools/geometry_dataset.py` 及其命令行入口仅支持原 stock 绘图器的对象，不能用它重绘新增的 region、curved_region、ellipse 等扩展。保留该旧文件是为了不改变现有 96 道几何题的已批准依赖指纹。新题独立复现请始终调用正式记录指定的脚本，不要改用这个旧辅助入口，也不要将输出指向正式原图、来源图或冻结场景。

## 分支边界

本分支增加原题审核工作台、待审核候选及 Pass/Delete 的事务支持。三个 Special 工作台与 `master` 保持相同；不保留旧 Base 生成器或旧绘图器兼容注册表。公共审核工具增加可选事务发布接口，并在每轮校验中复用来源记录快照；原有命令行、内容指纹和完整题库校验规则沿用 `master`。

不要从历史打包清单恢复已通过或已删除的候选。审核进度以当前 `index.jsonl` 和 `review_state.json` 为准，正式通过凭据仍只来自 `provenance/approvals.json`。
