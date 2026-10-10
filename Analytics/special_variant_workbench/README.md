# C 类特殊标记协作工作台

独立的本地 Python HTTP 服务与原生网页。用户可以直接用画板标注，也可以在另一个终端用自然语言指挥标记 agent；无需模型 API。两种方式使用相同的插件、审核和输出格式。每道题的 C 数量不限，审核后停留在当前题。

## 启动

双击 `start_workbench.cmd`，或从 Research 目录运行：

```powershell
python -B MathPalette/Analytics/special_variant_workbench/server.py --open-browser
```

默认地址 **http://127.0.0.1:8766**。更换端口可用 `--port 8776`，CLI 自动读取服务登记的实际端口。首次启动逐像素检查 80 道原题，之后使用与输入和渲染器签名绑定的缓存；原数据发生变化时停止并报告。验证环境：Python 3.13.9、Matplotlib 3.11.2、NumPy 2.5.3、Pillow 12.3.0；实际使用的 Python 版本记录在每个候选/recipe 中。

缺少依赖时，在本目录执行 `python -m pip install -r requirements.txt`。`--check` 校验全部原题并退出，不生成候选、不写正式 C 成果。Ctrl+C 停止服务，刷新/重启恢复选择的题目、未审候选和已收集图片。同一状态目录只允许一个服务。

配置分别指定 dataset、原图、公共渲染器、协议、嵌套题目类目录和 C 输出目录。所有相对路径基于配置文件位置，运行不依赖当前工作目录、`first_process` 或旧 A/B 工作台。当前原渲染器要求 `protocol.json` 与它自身同目录。

## 手动画板

选题后点击右上角 **打开画板**。如果本题已有 agent 候选，画板会载入它的完整插件，继续编辑时保留未修改的动作（包括 agent 添加的文字）。

- **红色点**（快捷键 `1`）：单击放点，实心 `#DC2626`，面积 50 pt²、边宽 1 pt。
- **辅助虚线**（`2`）：点击起点、终点，或从起点拖到终点。使用 `#2563EB`、线宽 1 pt、虚线间距 `[3.7, 1.6]` pt。
- **选择原曲线**（`3`）：点击曲线，选红 / 蓝 / 黑或实线 / 虚线。改颜色会保留当前线型，改线型会保留当前颜色。重叠曲线可通过下拉列表选择稳定 ID，青色轮廓用来核对目标。“恢复原曲线样式”移除该曲线的样式动作。
- **按住 Ctrl**：点和线端点吸附整数格点；松开恢复自由坐标。也可勾选“始终吸附整数格点”。坐标实时显示，小数保留至 6 位。
- **按住 Shift**：正在绘制的辅助线约束为水平或竖直，可与 Ctrl 同用。
- **Esc**：取消未完成线段或选中曲线；再次按可返回工作台。**Ctrl+Z / Ctrl+Shift+Z** 撤销 / 重做。也可展开“编辑标记”单独删除动作，清空后仍能撤销。

每次修改会自动调用原有 Matplotlib 执行器生成 **768×768 精确预览**。预览加载完成后点击 **Pass · 收集这张图**，自动提交相同插件、核对预览与候选的像素和参数哈希，并通过原有审核事务收集。绘制中的辅助线、青色选中轮廓和指针仅供操作参考，不进入保存图片。未完成线段和正在渲染时禁止 Pass。

点 **提交候选，交给 agent** 可把当前画板结果发布为正常待审候选，继续在终端要求 agent 修改；这一步不会判定通过。agent 读取 context 中的 `candidate.plugin_path` 即可取得完整标准插件，沿用现有 `submit --replace` 接口。工作台仍支持原来的 Pass / No Pass。

**返回工作台**会暂存画板草稿；同一浏览器、同一地址再次打开时，若题目和基础候选仍匹配，就恢复草稿。草稿仅在浏览器 localStorage 中，不是正式数据，也不属于 agent 可读取的候选。清除浏览器数据会清除该草稿；需要交接时先提交候选。如果其他页面或 agent 改变题目 / 候选，画板停止保存并提示载入最新候选，不自动覆盖别人的更改。

画板的坐标映射和点击选择取自 Matplotlib 的实际变换及完整曲线路径，适应网页缩放，支持普通函数、几何轮廓与原有辅助线对象；不把坐标轴、网格作为可修改曲线。只编辑图中可见区域的点和线段；超出视窗的坐标、文字或更多复杂操作仍可交给 agent。

实现新增 `drawing_board.py` 与 `web/drawing-board.js`，复用原有 renderer / schema / recipe / draw_Cxx，不改动受版本签名保护的三个渲染文件及插件 schema。画板仅添加三个接口：只读场景 `GET /api/drawing-scene/AnaXX`、无持久化预览 `POST /api/drawing-preview`、普通候选发布 `POST /api/drawing-submit`；两个 POST 均要求网页会话令牌。预览不会替换已有候选。发布前和发布后均校验题号、上下文以及显示的图片 / 参数哈希；最终 Pass 仍使用 `/api/review`。

更新代码后须重启已运行的 Python 服务，再刷新网页；只刷新网页不会让旧服务加载新增接口。

## 与标记 agent 协作

1. 在网页选题、查看原图、题干和答案。
2. 在另一个终端让 agent 阅读 `MathPalette/Analytics/special_variant_workbench/agent_prompt.md`，描述希望添加的点、线或曲线样式。
3. agent 读取 context、查看原图、在 drafts 中写 JSON，然后 validate/submit。
4. 网页每秒轮询完成发布的候选，图片完成载入后启用 **Pass / No Pass**。
5. Pass 冻结收集当前 PNG 原始字节与对应插件，不重新绘图。No Pass 保存可选拒绝备注、删除该候选 PNG，然后等待新的指令和提交。切题保留待审候选。

“原图对象定位”展示稳定 ID、原绘图调用和高亮入口。原曲线编号不是 y1/y2 的语义标签；必须结合原标签、几何样本、源代码或高亮确认。参考图明确标注 REFERENCE ONLY，不写入正式数据。

## CLI

工作台须先启动。所有成功结果与错误都为 JSON；失败退出码为 1。submit 同步等待候选 PNG、插件快照、清单与状态完成持久化，成功表示网页已可展示该图。

```powershell
# Research 目录
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py context
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py validate --plugin MathPalette/Analytics/special_variant_workbench/examples/Ana04_combined.json
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py highlight --object curve_001
# 用 context 返回的当前题号、context_token 和草稿目录
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py submit --plugin MathPalette/Analytics/special_variant_workbench/drafts/Ana04/plugin.json --context-token TOKEN
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py status --candidate ID
# 仅当用户明确要求修改仍待审的 ID
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py submit --plugin MathPalette/Analytics/special_variant_workbench/drafts/Ana04/plugin.json --context-token TOKEN --replace ID
```

在其他工作目录用入口和插件的绝对路径（含空格时加引号）。`--config 路径` 或 `--url http://127.0.0.1:端口` 可置于子命令前后。`context.commands` 给出绝对入口，`context.config_path` 给出配置路径。CLI 没有 Pass / No Pass 命令；agent 不得调用网页审核接口。

切题（含离开再返回）、审核、提交、替换或服务重启会使旧 context_token 过期。默认不覆盖待审候选；`--replace` 必须匹配当前 ID。渲染失败或渲染期间切题时，原待审候选仍可用。status 返回 pending / passed / rejected / superseded；被拒图片的路径返回 null，不伪装为仍存在。

## 插件格式

`plugin.schema.json` 是草稿格式规范。执行器只解释四种声明式动作，不执行插件代码：

| 动作 | 几何 | 样式 |
| --- | --- | --- |
| add_point | 新 id、xy | filled、color、size_pt2、edge_linewidth_pt |
| add_line | 新 id、endpoints | color、linestyle、linewidth_pt、可选 dash_pattern_pt |
| set_curve_style | 原 target | color、linestyle、linewidth_pt |
| add_text | 新 id、xy、text | color、fontsize_pt、ha、va |

坐标允许小数，以原 [-8,8] 数据坐标解释。颜色为 #RRGGBB；线型 solid / dashed；宽度/字号单位 pt，点面积 pt²。ID 不可重复或与原对象冲突。不接受额外字段、任意 Python、重复 JSON 键、NaN/Infinity 或无限数值。单个插件最多 100 动作，文本最多 120 字符，点面积上限 2500 pt²，线宽上限 30 pt，字体上限 96 pt。

样式默认值来自 config，发布前全部填入插件快照；重绘不读取后来的默认值。actions 按顺序执行，每次从原场景重建，不叠加此前候选修改。视窗外、遮挡或原样式不变造成的完全无像素变化会报错。C 允许误导性点线，不检查是否位于原曲线上。最终可解性由用户判断。

`examples/Ana04_combined.json` 展示四种动作组合。示例未经人工收集，不包含 passed 字段。validate 只检查格式、对象和参数，submit 才检查实际渲染变化。

## 输出与重绘

- 草稿：`special_variant_workbench/drafts/AnaXX/`，可编辑。
- 候选：`special_variant_workbench/candidates/<candidate_id>/`，插件和清单是不可变快照；No Pass 仅删除同包内 image.png。
- 状态与事务：`special_variant_workbench/state/`。
- **正式结果**：`construct_dataset/special_variant/AnaXX/images/C01.png`、`plugins/C01.json`、`recipes.json`、`draw_variants.py`；全局 `accepted_index.jsonl`。只在人工作出 Pass 后创建。
- 重绘：`special_variant_workbench/reproduced/AnaXX/C01.png`，默认不覆盖输入或正式文件。

正式 recipe 的 image_path/plugin_path 相对于 `construct_dataset/`。每题只有已通过的 `draw_C01(output_path=None)`、`draw_C02(...)` 等入口。

```powershell
python -B MathPalette/construct_dataset/special_variant/Ana04/draw_variants.py C01
```

也可 import 该模块后调用函数。重绘无需网络或 agent，不读 drafts，先核对版本、依赖、基线与参数哈希，再核对解码像素，匹配才写出。可用 `--output` 指定其他输出位置，禁止覆盖原图、A/B、正式 C 或基线输入。搬迁时保持 MathPalette 相对目录结构，并一起保留配置、state 和正式 C 数据。

Pass 的写前事务日志依次保存图片、插件、recipe、函数和索引，最后提交状态；失败重试或重启时向前恢复。重复请求不增加记录。审核绑定题号、上下文、实际显示的候选 ID 与图像/参数哈希；替换后的旧 ID 不能审核。候选 PNG 与插件文件变动会阻止 Pass。

## 验证

```powershell
python -B MathPalette/Analytics/special_variant_workbench/server.py --check
python -B MathPalette/Analytics/special_variant_workbench/test_workbench.py
```

测试使用系统临时目录，模拟 Pass 只落到临时 `construct_dataset/special_variant/`。浏览器验证也必须同时指定独立状态和输出：

```powershell
python -B MathPalette/Analytics/special_variant_workbench/server.py --port 8876 --data-dir 临时目录/runtime --output-dir 临时目录/construct_dataset/special_variant
python -B MathPalette/Analytics/special_variant_workbench/agent_cli.py --url http://127.0.0.1:8876 context
```

不要只更换状态目录而仍使用正式输出。`verification/validation_report.json` 记录开发验收结果。

## 实际限制

服务为单机协作设计，渲染串行。稳定对象 ID 与输入指纹绑定；修改源代码、渲染器/schema 或依赖版本时拒绝静默沿用旧结果。不要删除 state 来绕过检查；恢复原环境和备份。

可改样式的对象包括函数曲线、几何轮廓和原始线段；斜率场、区域填充、坐标轴与网格不可用 set_curve_style 修改。几何样本用于定位，不是自动求解器；复杂交点由 agent 根据固定参数核对。

新增文字沿用协议 DejaVu Sans，支持短字母和 Matplotlib 数学标签；该字体不覆盖全部中文字符，中文标记可能缺字。网页描述与备注完整支持中文。原图/答案采用纯文本显示，保留原题全文。

原题/A/B 全部只读。正式收集结果及其 state 应一同备份；删除/损坏正式 PNG、插件、recipe 或索引时会报告，不从未冻结草稿猜测恢复。
