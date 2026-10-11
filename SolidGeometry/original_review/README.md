# SOLIDGEO 原题审核工作台

这是本机运行的逐题原题审核页面。它与端口 8769 的 Special 标注工作台分开，不把数学验算、重绘检查或 Special Pass 当作原题通过。

## Windows 启动

通过 Git 拉取包含本工作台的分支（需要可读取当前提交的 Git 仓库，不要只解压 ZIP），再在项目根目录双击：

```text
SolidGeometry\start_original_review.cmd
```

默认打开 `http://127.0.0.1:8770/`。保持命令窗口打开；关闭窗口或按 Ctrl+C 停止服务。页面、数学排版和图片均由本机提供，不使用 CDN、在线题库、模型 API 或付费调用。无需 Node、npm 或前端构建步骤。

### 一次性准备 Python 环境

候选重绘冻结环境是 Python **3.13.9**、Matplotlib **3.11.2**、NumPy **2.5.3**、Pillow **12.3.0**。启动器核对 Python 补丁版本及根目录 `requirements.txt` 中的精确版本，不会自动安装或升级软件。

先安装 Python 3.13.9，然后在项目根目录执行：

```powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
SolidGeometry\start_original_review.cmd --check
SolidGeometry\start_original_review.cmd
```

`py -3.13` 选择本机已安装的 3.13；`--check` 会核对它是否恰为 3.13.9。若电脑装有多个补丁版本，也可用 Python 3.13.9 的完整路径代替 `py -3.13` 创建环境。

已有匹配环境时，启动器会检查当前 Python、项目 `.venv` / `venv`、已知 Conda 环境、PATH 和 Windows Python Launcher 的解释器。也可明确指定：

```powershell
$env:MATHPALETTE_PYTHON = 'C:\path with spaces\python.exe'
SolidGeometry\start_original_review.cmd
```

此设置只影响当前终端。若双击启动，请使用项目 `.venv`，或在 Windows 环境变量中配置该完整路径。CMD 启动入口处理 UTF-8 和带空格的路径。

可用参数：

```powershell
python -X utf8 -B SolidGeometry/original_review/launch_workbench.py --check
python -X utf8 -B SolidGeometry/original_review/launch_workbench.py --no-browser
python -X utf8 -B SolidGeometry/original_review/launch_workbench.py --port 8771
```

`--check` 只检查环境，不启动服务、不写入审核。端口占用时关闭之前的启动窗口，或指定另一端口。服务只绑定 `127.0.0.1`，不接受局域网或公网绑定。

## 审核流程

1. 页面一次显示一个候选。上一题、下一题、下拉跳转和键盘 ← / → 都会把当前位置保存到本机服务。输入控件、弹窗和提交操作期间不触发快捷切题。
2. 原图和规范重绘并排展示；点击任意图片可放大，在弹窗内切换两张图、缩放或恢复适应窗口，Esc 关闭。完整英文题干与所有选项显示在图片下方。
3. 分开查看来源原始答案、拟收录标准答案、独立验算答案，以及完整推导。原始答案可能含上游分析正文，长内容保留在可滚动区域。仅有 `verified` 状态不会被界面自动解释为答案一致；一致、不一致和未确定由明确的核验比较记录决定。
4. 若来源、数学核验、场景协议或图片加载不满足要求，Pass 被禁用，下方显示具体原因。两张图片均完整显示后才能提交。未知或不支持的对象不会被静默忽略。
5. 点击 **Pass · 原题通过**，表示用户确认**当前显示的原图、重绘、完整题干与标准答案**。服务端再次检查内容指纹与重绘，事务性分配 `SolidNN`、写入正式原题、审核记录与汇总索引。当前候选清理后移到逻辑下一题；上方可查看已通过的正式题号。当前显示图可能是在冻结环境中重新生成的图；这不宣称与旧环境的历史 PNG 像素一致。技术详情保留可用的迁移与环境记录。
6. **删除候选**会先确认，再移除该候选的清单和独占暂存文件。它不会删除已有正式题、共享文件、未跟踪文件或 Git 历史。含未提交候选行元数据或专属文件更改的候选会被拒绝删除，须先自行保存这些更改。已提交的候选内容仍可从 Git 历史恢复；页面不提供一键撤销删除。

通过和删除只在服务端返回对应操作回执后显示成功；不会乐观地显示“已保存”。连续点击只发送一笔操作。网络中断时页面保留原请求编号并锁住新操作；点击“核对并重试”沿用同一请求编号，服务端去重。刷新或重新打开同一浏览器标签页也不会自动替用户提交。内容过期时重新读取后由用户重新检查，不自动 Pass。

## 数据归属和持久化

- 候选：`staging/solidgeo/candidates.jsonl` 及对应候选目录，和正式题隔离
- 正式题：`SolidGeometry/dataset.jsonl`、`image/`、`originals/`、`dataset_generator/`
- 原题用户通过记录：项目 `provenance/approvals.json`，随正式数据保存
- 来源说明与核验依据：`provenance/source_notes.json`
- 派生汇总：根目录 `question_bank.jsonl`
- 本机当前位置、完成回执、请求去重和事务恢复状态：`.runtime/solidgeo-original-review/`

请保留本机审核状态目录；不要在审核过程中把它当作可随意删除的预览缓存。服务重启后恢复已有状态，未确认事务按日志恢复。审核产生的正式数据和候选变更仍是本地 Git 工作区变更；工作台不执行提交或推送。不要混用回退后的正式清单和较新的审核状态：编号不一致会阻止入库，不会跳号或复用旧号。若要从 Git 恢复一批数据重新审核，可使用独立干净的 Git checkout。

## 数学排版

页面自带 MIT 许可的 KaTeX 0.19.0，仅生成原生 MathML，适用于现代 Edge / Chrome / Firefox。不下载字体、脚本或样式。`$…$`、`$$…$$`、`\(…\)`、`\[…\]` 数学源码本机排版，解析失败保留原始文本；不允许可信 HTML 命令，限制宏展开次数和尺寸。第三方文件及许可证在 `static/vendor/`。

## 验证

[本次交付核验范围与剩余限制](VALIDATION.md)。

在项目根目录、匹配的冻结 Python 环境运行：

```powershell
python -X utf8 -B -m unittest discover -s SolidGeometry/original_review -p "test_*.py"
node SolidGeometry/original_review/test_ui.cjs
python -X utf8 -B dataset_tools/catalog.py check
```

Node 只用于可选的前端开发回归测试，普通用户启动不需要。Python 测试使用可识别的独立临时仓库，不向真实候选或正式数据写入自动审核记录。前端测试执行真正的 `static/app.js`，覆盖图片加载失败、Pass 双击、导航竞态、内容冲突、网络结果不明后的同编号重试、删除取消、弹窗、键盘和空队列。

本次执行环境无法启动可用的 Chromium，云浏览器也无法访问执行器本机服务；因此前端已完成真实脚本事件/状态回归和静态检查，但**没有完成真实浏览器视觉验收**。数学排版的 MathML 输出单独检查；其浏览器内排版仍属于上述未完成的视觉验收范围。

Windows CMD 入口和路径/解释器选择逻辑有自动化回归覆盖，但本次测试在 Linux 执行器中运行，未在真实 Windows 桌面上双击验收。若本机系统渲染与冻结 PNG 不一致，工作台会阻止 Pass 并报告差异，不会静默重新批准另一张图。
