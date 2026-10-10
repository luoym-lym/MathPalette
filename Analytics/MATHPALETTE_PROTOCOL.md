# MathPalette Analytics 新题制作与变体协议

版本：2.0.0。适用于 `MathPalette/Analytics/fine_grained_dataset/`。2026-10-09 目录迁入 `Analytics/`；本次迁移不改变冻结绘图输入、Base 参数或既有人工审核记录。本协议替代旧 A1～A4 / B1～B5 的人工 Base 收集流程，是后续创建题目的 agent 应阅读的入口。

## 1. 每道新题的流程

1. 创建冻结题目脚本，核对数学答案。
2. 生成原图并实际查看，登记冻结候选 `dataset.jsonl`，等待用户明确通过原题后正式入库。
3. 从 Base1～Base6 **等概率、不放回地抽取四种操作**，各自从原图生成一张变体。
4. 保存四张 PNG、四份冻结插件、recipes、全局索引及重绘函数，验证可重绘。
5. 新题作为 Special 待办，等待用户制作并 Pass；用户完成整题后 Collect。

Base 自动生成，不要求用户逐张审核。Special 的 Pass、No Pass、Collect 由用户操作；不为新题伪造 C 插件、通过记录或完成状态。

原题正式入库须用户逐题明确通过，函数与解析几何也适用。`fine_grained_dataset/dataset.jsonl` 保留为原图、Base/Special 的冻结候选输入，不代表用户审核通过；正式原题列表为同目录 `approved_dataset.jsonl` 和根目录 `question_bank.jsonl`，未通过题在 `pending_dataset.jsonl`。原题通过记录由 `dataset_tools/question_review.py` 保存到 `imports/mathverse_vision_dominant/question_user_reviews.json`，绑定题干、答案、原图、冻结脚本、坐标适配与机器协议；内容变化后待重新审核。原题通过和 Special Pass/Collect 互不替代，已有 Base、Special 及人工记录保留。

## 2. 文件布局

```text
Research/
  MATHPALETTE_PROTOCOL.md                  项目入口的兼容跳转
  MathPalette/
    MATHPALETTE_PROTOCOL.md                题型与流程入口
    Analytics/
      MATHPALETTE_PROTOCOL.md              本协议
      fine_grained_dataset/
        dataset.jsonl
        image/Ana21.png
        dataset_generator/
          common_renderer.py               原图公共渲染器
          protocol.json                    原图样式协议
          base_protocol.json               Base 参数与版本
          base_support.py                  数据加载、原图重绘、哈希
          prepare_question.py              新题完整准备入口
          generate_base_variants.py         Base 生成、校验、重绘
          dataset_generator/
            function_plot21.py              class Ana21
            generate_dataset.py             原图重绘校验
        base_variant/
          generated_index.jsonl
          Ana21/
            images/Ana21_base_variant_1.png ... _4.png
            plugins/Ana21_base_variant_1.json ... _4.json
            recipes.json
            draw_variants.py
        special_variant/
          accepted_index.jsonl
          collected_index.jsonl
          Ana21/                            用户 Pass 后才出现正式结果
            images/C01.png
            plugins/C01.json
            recipes.json
            draw_variants.py
            collection.json                 用户 Collect 后记录完成
          _baselines/
        reproduced/                         重绘输出
        archive/                            旧 Base 包与迁移备份
      fine_grained_special_workbench/        本批 Special 工作台
      val_script/                           实验评测
```

- 题号取现有最大编号加一，按 `Ana01`、`Ana02`……连续排列；20 题后的下一题是 `Ana21`，不限制为 80 题。
- 推荐每题一个 `function_plotNN.py`，避免追加新题时改变旧题源码指纹。
- 文件名 `_base_variant_1` 中的 `1` 是本题抽样槽位，不表示 Base1；真正操作在插件 `operation` 中。
- 数据路径相对于 `fine_grained_dataset/`，不写个人机器绝对路径。
- `variant_workbench/` 已由自动脚本替代。`special_variant_workbench/` 是旧数据工作台；本批使用 **`fine_grained_special_workbench/`**。

## 3. 编写冻结题目

参照现有 `function_plot*.py` 的相对路径与公共绘图辅助函数。新文件包含唯一的 `class AnaNN`，定义 `self.id`、`self.source_dataset`、`self.query`、`self.answer`、`self.answer_type`、`self.subject`、`self.level`。

### 来源标注（2026-10-09 补充）

- **每道题必须在自身 class 的 `__init__` 中显式填写 `self.source_dataset`**，记录真实的来源数据集或题源名称；不能只在文件注释或外部说明中标注。重绘、冻结参数或改编为共同协议下的题目后，仍须保留来源。
- **只记录来源名称，不要求记录或核对来源中的原始题号；题目类无需定义 `source_id`。** 本项目题号仍由 `self.id` 标识。只有真正自建的题目才能将来源写为 `Custom`。
- **Ana01～Ana20 的来源均为 DynaMath，已统一标注 `self.source_dataset = 'DynaMath'`。**

示例：

```python
class Ana01:
    def __init__(self):
        self.id = 'Ana01'
        self.source_dataset = 'DynaMath'
        # 其余题干、答案和绘图参数字段按本协议定义。
```

对已冻结题目补录来源时，须处理源码哈希与既有 Base / Special 重绘基线的兼容性，核对题干、答案和绘图结果一致，并保留已有人工 Pass / Collect 记录。Ana01～Ana20 本次来源补录的旧文件、哈希对应关系和核对记录保存在 `fine_grained_dataset/provenance/source_metadata_20261009/`。

### 绘图与冻结要求

- `draw(self, num=0, output_path=None)` 使用 `open_canvas()`、`plot_curve()`、`scatter_points()`、`label()` 等辅助函数，通过模块中的 `finalize(fig, destination)` 保存。执行器会捕获该函数取得原场景。
- 数学参数、分段区间、采样数量和标签位置均冻结；构造函数和 `draw()` 中不重新随机。
- 导入模块不生成文件。题干、答案、图像一致；Agent 独立核对数学答案，实际查看原图中的端点、分段、尺度、标签和目标对象。
- 原图沿用 `dataset_generator/protocol.json`：768×768、不透明白底、等比例坐标 `[-8,8]²`、统一网格/曲线/字体。空实心点和函数标签保留数学含义。
- 数学实例变化应作为新题，不借生成 Base 静默修改已有题干、答案或原图。

## 4. 登记、原图生成与 Base 生成

命令从 **Research 目录**执行。依赖版本见 `MathPalette/Analytics/fine_grained_dataset/dataset_generator/requirements.txt`。

写好新题脚本后执行：

```powershell
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/prepare_question.py Ana21
```

此命令读取题目类，检查题号/字段，两次绘制原图核对像素，保存缺失原图，向 JSONL 登记 `id/question/answer/image`，生成并重绘核对四份 Base，更新 Base 索引，输出 Special 待办状态。无需预先手工写 JSONL。答案保留真实数值或字符串类型。

重复执行会校验并复用已有产物。已有原图或已登记题干/答案与脚本不一致时停止；不自动覆盖基线。中途失败可修正后重跑，确认四份 Base 齐全后再交给 Special。运行中不要由另一进程编辑题目输入。

```powershell
# 批量准备连续新题
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/prepare_question.py Ana21 Ana22 Ana23

# 只生成全部现有题目的 Base；已有且一致的结果会跳过
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py generate

# 只生成一题
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py generate Ana21

# 明确重新抽样；旧的整题 Base 包先移入 archive/base_variant/
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py generate Ana21 --seed 20261009 --replace
```

默认 master seed 为 `20261008`，可通过 `--seed` 指定。各题的操作选择种子和参数种子由 master seed、题号、用途稳定派生，新增其他题不改变既有题目的抽样。重绘使用冻结参数，不重新使用种子抽样。

## 5. 六种 Base 操作

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

## 6. 插件、recipes 与重绘

插件示例：

```json
{
  "plugin_schema_version": "1.0.0",
  "protocol_version": "2.0.0",
  "question_id": "Ana21",
  "category": "Base",
  "operation": "Base3",
  "params": {"background_color": "#0000FF"}
}
```

Base 和 Special 均采用 `images/ + plugins/ + recipes.json + draw_variants.py + 全局索引`。Base 的 `params` 保存单一操作参数；Special 的 `params.actions` 保存多项人工动作，两者由各自执行器读取。

每题 `recipes.json` 是四项数组，包含完整插件以及槽位、UUID、master/selection/parameter seed、采样次数、参数/PNG/像素/插件哈希、本题记录与源码/原图/公共渲染器/原图协议基线、Base 协议和执行器哈希、实际依赖版本、生成时间、相对路径。

Base 使用 `status="generated"`、`review_mode="automatic"`，不伪造 `reviewed_at` 或人工 `passed`。`generated_index.jsonl` 是各题 recipes 的可重建汇总，不是独立真值。

```powershell
# 全部文件校验及逐张插件重绘
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py check --redraw

# 单图重绘，默认输出 reproduced/base_variant/Ana21/
python -B MathPalette/Analytics/fine_grained_dataset/base_variant/Ana21/draw_variants.py base_1

# 原图重绘校验，默认输出 reproduced/originals/
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/dataset_generator/generate_dataset.py --question Ana21
```

也可调用 `draw_base_1(output_path=None)`～`draw_base_4(output_path=None)`。重绘不重新采样、不覆盖正式图片。Base 基线按题独立绑定，追加其他题不使旧题失效。修改 Base 协议/执行器时应更新版本，用明确的 `--replace` 生成新包。

## 7. Special 待办与收集

**现有工作台没有需要 agent 手工添加的待办文件。** 启动时读取 `dataset.jsonl`，自动为新题初始化未 Collect 状态；未 Collect 的题组成待办列表。完成原图、登记和四份 Base 后，重启工作台即可。

```powershell
# 从正式 collection.json 派生待办题号
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/prepare_question.py --pending

# 双击此入口重启并打开本批工作台
MathPalette\Analytics\fine_grained_dataset\start_special_workbench.cmd
```

不要手工修改或清空 `fine_grained_special_workbench/state/progress.json`，不要重置已 Collect 的题。没有人工 C 结果时不创建空 C recipes、伪造插件或 collection 记录。用户通过画板 Pass 后保存 C01、C02……，数量由用户决定；Collect 后从待办隐藏，需要继续时由用户重新打开。

备份时同时保留 `fine_grained_dataset/` 和 `fine_grained_special_workbench/`。C 回放依赖匹配的工作台和基线记录，详情见 `MathPalette/Analytics/fine_grained_special_workbench/README.md`。

## 8. Agent 交付检查

- 每道题的 class 已显式填写真实的 `source_dataset`，无需记录来源中的原始题号。
- 数学答案已核对，题目脚本/题干/原图一致，实际查看过原图。
- ID 连续且唯一，原图 768×768，重复重绘像素一致。
- 每题四张 Base、四份插件、四条 recipe、四个重绘函数，四种操作不同。
- Base 参数、路径、版本、哈希和索引一致，冻结插件能重绘。
- 新题可进入 Special 待办，既有 Special 人工产物和完成状态保留。
- 交付说明列出新题号、文件位置、核对范围和待办状态，不把自动生成称为人工审核通过。

旧 A/B 规范在 `fine_grained_dataset/provenance/protocol_v1_legacy.md`，旧产物在 `archive/`，不属于当前四变体数据集。旧 `render_variants.py` / `baseline_manifest.json` 仅供历史 A/B 回放，新题使用本文的新入口。

## 9. MathVerse 本批收录补充

Ana21～Ana66 的来源坐标范围不同，使用 `dataset_generator/mathverse_renderer.py` 和逐题冻结的平移、比例映射到标准展示画布 `[-8,8]²`。刻度位置和数学对象采用同一映射，数字保留来源单位；圆与解析几何采用等比例映射，含大幅值、时间或数量单位的函数图分别冻结两轴比例。端点、空实心状态、方向箭头、渐近线、给定点标签和对象名称必须保留。

新题模块绑定坐标适配器与逐题 provenance 的 SHA256；场景捕获后恢复冻结映射。既有 Base 执行器不变，四种操作仍按原规则抽取；Base1 只调整展示网格，不改变来源刻度或数学对象。

按用户本批要求，题源疑点不阻止保留收录。`self.query` 和 `self.answer` 保存原题与来源 GT；`provenance/MathVerse/` 保存独立推导、核验候选和疑点。不得用候选答案覆盖来源 GT，也不得用历史模型回答作为真值。`needs_review` 不等于已证明错误。全批索引和原图 / 重绘对照位于 `imports/mathverse_vision_dominant/`。
