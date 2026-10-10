# 历史协议：已由 Research/MATHPALETTE_PROTOCOL.md 的 2.0.0 流程替代

以下内容仅解释旧人工 A/B 归档，不约束当前 Base1～Base6 自动生成。

# MathPalette 数据整理协议

组织协议版本：`1.0`  
核对日期：`2026-10-08`  
参照数据：`MathPalette/construct_dataset/`  
新数据根目录：`MathPalette/fine_grained_dataset/`

## 1. 目的与适用范围

本文件规定种子题、原图、固定绘图程序、A/B 变体、C 变体以及重绘记录的组织方式，供后续 agent 整理数据时遵循。用户所说的 `dataset_construct` 在当前仓库中的实际目录名是 **`construct_dataset`**。

核心单位是：**一道固定参数的种子题 + 一张原图 + 5 张 A 变体 + 5 张 B 变体 + 人工决定数量的 C 变体**。从同一个例题扩展出的不同数学实例分别是不同种子题；对同一道种子题只改变视觉标记，才是该种子题的 A/B/C 变体。

当前收集按用户要求使用新的独立题号，不保留新旧题号 mapping 或旧数据追溯副本。下文来源映射和研究元数据均为可选项；不得仅为符合示例目录树而补造这些文件。新数据的读取和重绘必须能够脱离旧数据目录运行。

本协议保留现有核心字段、插件动作和目录结构；同时明确历史迁移遗留的路径问题。文中“新数据必须”约束此后整理的数据，不表示本次已经修复或迁移旧数据。不要为了符合新目录写法而直接改动旧数据或其审核状态。

截至核对日期，旧目录包含：

| 数据 | 实际数量与形式 |
| --- | --- |
| 种子题 | 80 条，`Ana01`～`Ana80` |
| 原图 | 80 张，位于 `image/` |
| A/B | 每题 10 条 recipe、10 张图，共 800 张 |
| C | 75 道题有正式记录，共 184 条 recipe、184 张图、184 份插件 |
| C 数量 | 每道有 C 记录的题为 1～4 张；不要求每题数量一致 |

以上是旧数据的快照，**不是新数据必须达到的题量**。没有 C 记录不能被 agent 擅自解释为遗漏，更不能自动补造已通过记录。

## 2. 目录与命名

以下树中的 `Ana01` 为示例；用各题的实际 ID 替换。

```text
fine_grained_dataset/
├── protocol.md
├── dataset.jsonl
├── image/
│   └── Ana01.png
├── dataset_generator/
│   ├── common_renderer.py
│   ├── protocol.json
│   ├── requirements.txt
│   └── dataset_generator/
│       ├── function_plot*.py
│       ├── generate_dataset.py
│       └── id_map.json           # 可选来源映射；当前收集不保留
├── base_variant/
│   └── Ana01/
│       ├── images/
│       │   ├── A01.png ... A05.png
│       │   └── B01.png ... B05.png
│       ├── recipes.json
│       └── draw_variants.py
├── special_variant/
│   ├── accepted_index.jsonl
│   └── Ana01/
│       ├── images/
│       │   └── C01.png ...
│       ├── plugins/
│       │   └── C01.json ...
│       ├── recipes.json
│       └── draw_variants.py
└── val_script/                   # 可选：评测脚本与结果，不属于题目真值
```

- 本协议中的“数据根目录”指 `fine_grained_dataset/`，不是工作台目录、当前终端目录或内层 `dataset_generator/`。
- 保留现有双层 `dataset_generator/` 布局：外层放公共渲染器和绘图协议，内层放题目类。文件分组不必继续限定每文件 20 题，但原始题目类必须可定位。
- 继续采用 `Ana01`、`Ana02` 等稳定 ID。新数据集可以从 `Ana01` 重新编号；跨数据集引用时必须同时携带数据集名称或版本，不能只用题号区分新旧数据。
- ID 在题目记录、类名、类的 `self.id`、原图文件名、变体目录和 `question_id` 中必须一致。已有正式变体的种子题不得随意重编号。
- 图片使用小写扩展名 `.png`。JSON 路径统一使用 `/`，不得保存个人机器的绝对路径或含 `..` 的越界路径。
- **新数据**的 `image`、`image_path`、`plugin_path` 一律相对于数据根目录。例：`image/Ana01.png`、`base_variant/Ana01/images/A01.png`、`special_variant/Ana01/plugins/C01.json`。
- 草稿、候选、拒绝记录、工作台会话和锁文件留在独立工作台运行目录；不混入正式 `images/`、`plugins/` 或 `recipes.json`。
- `A01` 是 A 类第一个通过的**槽位**，`A1` 是修改网格的**操作类型**，二者不能混淆。例如 `A02.png` 完全可以对应 `operation="A3"`。
- 一张变体的唯一业务标识为 `(数据集版本, question_id, slot_id)`；`candidate_id` 是候选提交标识，不能代替上述标识。

## 3. 原题记录：`dataset.jsonl`

UTF-8 JSON Lines；每行一个 JSON 对象，不使用外围数组，不写注释。每道种子题恰好一行，按题号的数字部分排序。保持以下四个核心字段：

| 字段 | 类型 | 约束 |
| --- | --- | --- |
| `id` | string | 稳定且唯一的种子题 ID |
| `question` | string | 完整题干，选择题包含选项；与绘图实例匹配 |
| `answer` | number 或 string | 标准答案；保留真实类型和数值精度 |
| `image` | string | 原图相对路径，固定为 `image/<id>.png` |

旧数据的真实格式示例：

```json
{"id":"Ana01","question":"What is the period of this function y = a*sin(b*x), where both a and b are integers? Answer the question with a floating-point number. ","answer":3.141592653589793,"image":"image/Ana01.png"}
```

要求：

1. 不把数值 `3.141592653589793` 改成字符串或截断为 `3.14`。当前旧数据包含整数、浮点数和字符串答案；选择题答案如 `"A"`，表达式答案如 `"y = 0"`。不要自行把它们统一转换为其他类型。
2. 不接受 NaN、Infinity、重复 JSON 键或空题干。需要新答案类型时先明确消费者如何读取，不直接把 `answer` 改成任意嵌套对象。
3. **一个种子题的所有 A/B/C 变体共用该行题干与标准答案**。变体记录不重复存一套可独立漂移的题干、答案。
4. 数学参数改变形成新实例时，重新计算并人工核对答案，分配新种子 ID。不能把改变函数、定义域或标准答案的实例伪装成视觉变体。
5. 不把错误模式、难度、来源等研究字段塞进 C 插件；需要时按第 10 节增加独立元数据。

## 4. 种子绘图程序与原图

### 4.1 固定实例的程序约定

当前题目类形如 `class Ana01`，具有 `self.id`、`self.source_id`、固定数学参数、`self.query`、`self.answer`，并保存 `answer_type`、`subject`、`level` 等属性。对外绘图入口为 `draw(self, num)`；现有 `num` 是兼容参数，不代表重新采样。

新数据必须遵循：

- 一类对应一个已经冻结的实例。采样或从例题扩展的工作发生在冻结之前；`__init__` 和 `draw()` 不再重新随机选择数学参数或视觉参数。
- 参数数组、分段区间、采样点数量等同样属于冻结内容。只保存一个随机种子而不保存具体实例不够。
- `self.query == dataset.jsonl.question`，`self.answer` 与 `dataset.jsonl.answer` 的值和类型一致。
- 原图通过公共 `common_renderer.py` 绘制，避免逐题建立另一套默认颜色、字号、画幅或坐标轴。
- 原题类只负责原图；A/B/C 动作通过通用执行器作用于原场景，不把人工变体代码改写进原题 `draw()`。
- 导入模块不得自动批量生成、覆盖数据。批量入口只能在明确执行时运行；必须明确数据根目录，输出到根目录的 `image/` 与 `dataset.jsonl`。
- 对一个冻结实例重复重绘，原图像素必须一致；已有变体后不得静默修改原题、原图或绘图协议。

旧 `id_map.json` 是来源映射数组，每项具有 `ana_id`、`source_id`、`source_file`、`source_class`。其中 `source_class="Q01"` 等描述**上游来源类**，不代表本地冻结类仍叫 `Q01`。新题来自其他来源时如实记录，不编造 DynaMath 的 Q 题号；本地冻结类仍按种子 ID 定位。

### 4.2 当前原图渲染标准

机器可读的完整规则以本批次归档的 `dataset_generator/protocol.json` 为准；以下为现有解析几何协议的关键值：

| 项目 | 原图标准 |
| --- | --- |
| 输出 | PNG，768×768，RGB 或不透明 RGBA，不把题干和答案嵌进图片 |
| 画幅 | `figsize=(7.68, 7.68)`，`dpi=100`；不使用 `bbox_inches="tight"` |
| 背景 | `#FFFFFF`，不透明 |
| 坐标视窗 | x、y 都为 `[-8, 8]`，等比例，关闭自动缩放 |
| 坐标区位置 | `[0.12, 0.12, 0.80, 0.80]` |
| 坐标轴 | 左、下轴穿过原点，上、右边框隐藏；轴线黑色 1 pt |
| 主刻度 | -8 至 8，间隔 1；原点数字 0 只画一次 |
| 网格 | `#E0E0E0` 实线，0.5 pt |
| 函数曲线与数学轮廓 | `#000000` 实线，1 pt，无额外曲线 marker |
| 字体 | DejaVu Sans，通常 12 pt，mathtext 为 dejavusans |
| 原有数学点 | 36 pt²；实心黑点或保留数学意义的白底黑边空心点 |

注意：线宽单位 **pt，不是 px**；点大小单位 **pt²**。原题必要的空心端点、区域、几何轮廓和文字不应被误删成“装饰”。完整协议还包含极点断线、区域填充、局部定义域、复平面与极坐标题适配，不能仅凭本表重新猜测实现。

A/B/C 可以按各自操作改变指定样式，例如 A4 改背景、C 改曲线颜色；画幅大小和原数学实例保持冻结。

## 5. A/B 变体：`base_variant/`

### 5.1 数量与收集规则

- 一道完成 A/B 收集的种子题包含 `A01`～`A05`、`B01`～`B05`，共 10 个槽位。A、B 分开按人工通过顺序编号。
- 优先尝试 A1～A4 各一张、B1～B5 各一张，然后分别补足 5 张。
- 某操作不可构造、有限方案耗尽或被人工拒绝时，先收集其他可通过的类型，再从该大类其他可行操作补足；不得强造 B3/B4/B5 的来源点。
- `phase="coverage"` 表示类型覆盖阶段，`phase="fill"` 表示补足阶段。因此不能要求每个种子都一定包含 A1～A4 或 B1～B5 的全部操作。
- 每张 A/B recipe 表达一种 `operation`；A/B 不是 C 的 `params.actions` 结构。每次从原图场景出发，不依次把 A1、A2 等累积到上一张变体上。
- 同一种子题的正式 A/B 图片不得用重复像素凑数。尚未收满时保留真实通过记录，不把临时缺额写成已完成。

### 5.2 `recipes.json` 字段

每题一个 JSON **数组**，数组元素是完整的通过记录。当前所有 A/B recipe 都包含以下 17 个字段：

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `question_id` | string | 所属种子题 ID |
| `category` | string | `A` 或 `B` |
| `operation` | string | `A1`～`A4` 或 `B1`～`B5`，须属于对应 category |
| `phase` | string | `coverage` 或 `fill` |
| `candidate_id` | string | 实际候选 UUID，当前使用 32 位十六进制字符串 |
| `seed` | integer | 候选采样时的随机种子；仅用于追踪，不替代 params |
| `params` | object | 本次构造已冻结的完整参数，见下一节 |
| `parameter_key` | string | 操作与参数的规范化 JSON SHA256，见第 8 节 |
| `image_path` | string | 新数据写 `base_variant/<question_id>/images/<slot_id>.png` |
| `pixel_sha256` | string | PNG 解码像素哈希，不是 PNG 文件字节哈希 |
| `status` | string | 正式记录只能为 `passed` |
| `created_at` | string | 实际候选生成时间，带时区 ISO 8601 |
| `generator_version` | string | 对应生成器版本；旧数据为 `1.0.0` |
| `environment` | object | `python`、`matplotlib`、`numpy`、`pillow` 四个版本字符串 |
| `baseline_fingerprint` | string | 该生成器实际计算的原题基线指纹 |
| `slot_id` | string | `A01`～`A05` 或 `B01`～`B05` |
| `reviewed_at` | string | 实际人工通过时间，带时区 ISO 8601 |

`seed` 的现有取值可能大于 JavaScript 的安全整数上限 `2^53-1`。整理时使用 Python 等能无损处理该整数的方式，不通过有损的浏览器 JSON 往返改写，也不擅自改成字符串。

### 5.3 各操作的 `params`

A3、B1～B5 使用以下公共样式字段：`color`、`linewidth_pt`、`linestyle`、`dash_pattern_pt`。现有 A/B 通常为黑色 `#000000`、1 pt；实线是 `"solid"` 和 `[]`，虚线是 `"dashed"` 和 `[4.0, 3.0]`。它们与 C 的蓝色虚线预设不同，不要统一替换。

| 操作 | 必须冻结的具体内容 |
| --- | --- |
| A1 修改网格 | `mode="off"` 时 `grid_positions=[]`；`mode="half_density"` 时为 `[-8,-6,-4,-2,0,2,4,6,8]` |
| A2 隐藏刻度数字 | `hidden=["x_tick_labels","y_tick_labels","origin_zero"]`；保留轴线、刻度位置和轴名 |
| A3 独立形状 | `shape` 为 `ellipse/rectangle/triangle`；`center`、`angle_deg`、`width`、`height`、`fill=false` 和公共样式。矩形/三角形保存最终 `vertices`；椭圆另存 `major_axis`、`minor_axis`，width/height 为轴全长 |
| A4 背景色 | `background_color` 为 `#FFF9DB`（浅黄）或 `#EAF4FF`（浅蓝） |
| B1 游离点 | `points` 为 1～3 项；每项保存 `xy`、`filled`、`size_pt2`、`color`。xy 均为整数，不与原有点完全重合；外层保存公共样式 |
| B2 随机线 | `orientation` 为 `horizontal/vertical/oblique`；保存实际 `endpoints=[[x1,y1],[x2,y2]]` 和公共样式。端点可为小数 |
| B3 原有点连原点 | `source` 记录原已绘制点的 `kind="original_point"`、`id`、`xy`、`filled`；`endpoints=[source.xy,[0,0]]`；加公共样式 |
| B4 坐标投影 | `source`、`projection_axis="x"/"y"`、实际 `endpoints` 和公共样式。投影到 x 轴为 `[x,0]`，到 y 轴为 `[0,y]` |
| B5 曲线上整数点 | 1～3 个不同整数坐标点；每项保存普通点字段及 `curve_id`、`verification`、`tolerance`；外层保存公共样式 |

B4 的来源可以是原来绘制的点，也可以是原曲线上经验证的整数点；**原有点本身不强制整数**。曲线整数点来源示例：

```json
{"kind":"verified_curve_integer","xy":[-5,-2],"curve_id":"curve_001","verification":"original_draw_integer_evaluation","tolerance":1e-8}
```

B5 中每个点的结构示例：

```json
{"xy":[-6,-3],"filled":true,"size_pt2":36,"color":"#000000","curve_id":"curve_001","verification":"original_draw_integer_evaluation","tolerance":1e-8}
```

`verification` 必须记录实际验证方式；旧数据也存在 `analytic_Ellipse`，不能一律填相同文字。当前整数点验证容差为 `1e-8`。不能仅从 PNG 肉眼估计“似乎过格点”就伪造通过验证的元数据。

B3/B4 必须保存实际来源，禁止把后添加的游离点冒充原有点。新增线段不得退化或与原轴线、原线条完全重合。B1 的旧实现排除与原有点完全重合，并不保证它绝不落在任何曲线上；无关性、可解性仍由人工审核，不应在元数据中声称已经自动证明。

### 5.4 图片与重绘函数

每个槽位有一张 `images/<slot_id>.png`，并在 `draw_variants.py` 提供同名接口：

```python
def draw_A01(output_path=None): ...
def draw_B01(output_path=None): ...
```

这些函数读取本题 `recipes.json`，调用共享 A/B 执行器按冻结参数重绘；不是保存另一份会再次随机采样的代码。只为已通过槽位生成函数。

当前整理后的 `base_variant/` **没有**每槽位 `plugins/*.json`，也没有根级 `accepted_index.jsonl`。A/B 的 `params` 已在 recipes 中完整保存，不需要为兼容而补造 C 式插件文件。新数据如额外导出 A/B 全局索引，只能是各题 recipes 的可重建汇总，不可成为不同步的第二套真值。

## 6. C 变体：`special_variant/`

### 6.1 数量与文件关系

C 的数量由人工决定，记为每题 `K`，不自动补到 5 张。按人工通过顺序连续编号 `C01`、`C02`……；没有通过记录的题可以暂不创建该题目录，不写空壳图片或伪造 recipe。

每个通过槽位必须同时具备：

1. `images/C01.png`：审核时的图片。
2. `plugins/C01.json`：已补齐默认值、冻结的完整声明式插件。
3. `recipes.json` 中的对应完整记录。
4. `draw_variants.py` 中的 `draw_C01(output_path=None)`。
5. 根级 `special_variant/accepted_index.jsonl` 中相同的完整 recipe。

手动画板、agent 协作和直接写标准 JSON 都产生这一种格式；不另设 `C_board` 类别，也不把浏览器画布截图当成可重绘参数。

### 6.2 `plugins/Cxx.json`

插件只有以下顶层字段，不能加入审核字段或任意研究字段：

| 字段 | 固定值 / 含义 |
| --- | --- |
| `plugin_schema_version` | 当前为 `"1.0.0"` |
| `question_id` | 所属种子题 ID |
| `category` | `"C"` |
| `operation` | `"C_manual"` |
| `description` | 具体修改说明，string；冻结文件包含此字段，旧数据允许空字符串 |
| `intent` | 用户确认的意图，string；没有确认时用空字符串，不编造效果结论 |
| `params` | `{"actions": [...]}`，保存有序的完整动作列表 |

可解析的草稿格式示例（**仅示例，不是已审核数据**）：

```json
{
  "plugin_schema_version": "1.0.0",
  "question_id": "Ana01",
  "category": "C",
  "operation": "C_manual",
  "description": "在 (2,3) 添加红点，添加一条蓝色辅助虚线",
  "intent": "",
  "params": {
    "actions": [
      {
        "type": "add_point",
        "id": "point_decoy_1",
        "xy": [2,3],
        "filled": true,
        "color": "#DC2626",
        "size_pt2": 50,
        "edge_linewidth_pt": 1.0
      },
      {
        "type": "add_line",
        "id": "line_aux_1",
        "endpoints": [[-2,2],[3,2]],
        "color": "#2563EB",
        "linestyle": "dashed",
        "linewidth_pt": 1.0,
        "dash_pattern_pt": [3.7,1.6]
      }
    ]
  }
}
```

### 6.3 四种动作

| 动作 | 几何或目标字段 | 冻结后的样式字段 |
| --- | --- | --- |
| `add_point` | 新 `id`、`xy=[x,y]` | `filled`、`color`、`size_pt2`、`edge_linewidth_pt` |
| `add_line` | 新 `id`、`endpoints=[[x1,y1],[x2,y2]]` | `color`、`linestyle`、`linewidth_pt`；虚线保存 `dash_pattern_pt` |
| `set_curve_style` | `target` 为原图可修改对象的稳定 ID | `color`、`linestyle`、`linewidth_pt` |
| `add_text` | 新 `id`、`xy`、`text` | `color`、`fontsize_pt`、`ha`、`va` |

- 所有坐标都是数学数据坐标，不是画布像素；C 允许小数。Ctrl 吸附只是画板输入方式，不是 C 数据必须为整数的约束。
- 每次从原始冻结场景执行完整动作列表。不能只保存“再向右移一点”“继续改红”等依赖上一个候选的增量指令。
- 数组顺序具有含义，不能为了排序或去重任意调整。多个样式动作可能作用于同一原对象，最终按顺序执行。
- `target` 必须对应本种子场景的 `styleable=true` 对象；不要把 `curve_001` 自动当成语义上的 y1，也不能猜测另一道题的 ID 映射。
- 新对象 ID 以英文字母开头，后接字母、数字、下划线或连字符，最长 64 字符；不能与原对象或其他新动作 ID 冲突。`set_curve_style` 使用 `target`，不需要新增 `id`。
- 颜色为 `#RRGGBB`，冻结时沿用执行器的大写规范；线型仅 `solid/dashed`。线宽大于 0 且不超过 30 pt，点面积不超过 2500 pt²。
- `add_line` 端点不同。自定义虚线参数只能用于虚线，为 2～12 个正的 pt 长度、个数为偶数，每项不超过 100；实线不添加虚线参数。
- 当前 schema 的 `set_curve_style` **不接受** `dash_pattern_pt`；曲线改虚线由执行器使用其固定线型规则，不能把 `add_line` 的字段搬过去。
- `add_text.text` 为 1～120 字符，字号大于 0 且不超过 96 pt；`ha` 为 `left/center/right`，`va` 为 `top/center/bottom/baseline/center_baseline`。使用原渲染器字体，注意其字符覆盖范围。
- 每份插件为 1～100 个动作；`description`、`intent` 各不超过 1000 字符。拒绝未知字段、未知动作、重复键和非有限数值，不执行任意 Python 或表达式。

默认视觉约定延续人工标注：红点 `#DC2626`、实心、50 pt²、边宽 1 pt；蓝色辅助虚线 `#2563EB`、1 pt、`[3.7,1.6]`。注意工作台配置中的 `add_line` 默认仍是实线，所以希望生成辅助虚线时必须明确填写 `linestyle` 和虚线参数。既有标注使用其他合法样式时保留其真实冻结值，不在整理时统一覆盖。

### 6.4 C 的 `recipes.json`

每题仍为 JSON 数组。每条记录先包含插件的全部 7 个顶层字段，再追加以下字段；因此它与独立插件不是同一份 JSON：

| 追加字段 | 类型 / 规则 |
| --- | --- |
| `phase` | `"manual"` |
| `slot_id` | `"C01"` 等连续正式槽位 |
| `candidate_id` | 实际发布候选的 UUID |
| `parameter_key` | 完整冻结插件的规范化 JSON 哈希 |
| `pixel_sha256` | 解码像素哈希 |
| `png_sha256` | 审核 PNG 原始文件字节的 SHA256 |
| `plugin_sha256` | `plugins/Cxx.json` 原始文件字节的 SHA256 |
| `generator_version` | 对应执行器版本；旧数据为 `"C-1.0.0"` |
| `environment` | 四个环境版本字段，与 A/B 字段名一致 |
| `baseline_fingerprint` | C 执行器实际生成的基线指纹 |
| `schema_sha256` | 该批使用的 `plugin.schema.json` 文件哈希 |
| `renderer_sha256` | C 渲染核心文件指纹，见第 8 节 |
| `created_at`、`reviewed_at` | 实际生成、人工通过时间，带时区 ISO 8601 |
| `status` | `"passed"` |
| `image_path` | `special_variant/<question_id>/images/<slot_id>.png` |
| `plugin_path` | `special_variant/<question_id>/plugins/<slot_id>.json` |

`accepted_index.jsonl` 每行是一条上述**完整 recipe**，不是只有 ID、路径的摘要。按种子题号与槽位数字排序，其内容必须与各题 recipes 的汇总一致。

## 7. 审核与保存边界

1. 种子题先完成数学正确性和原图审核，再冻结并生成视觉变体。渲染成功不代表题意或答案正确。
2. 候选可以被人工拒绝、重做；只有人工 Pass 后才能写入正式槽位和 `status="passed"`。agent 不根据自己的判断补填通过状态、审核时间或不存在的历史。
3. 保存审核时看到的具体 PNG 和完整构造参数。不能在 Pass 后再次随机抽样、换一组默认值或重新解释自然语言。
4. 保存图片、插件、recipe、索引与重绘函数必须保持一致，使用工作台已有事务或等价的原子提交方式，避免只有图没有参数、只有 recipe 没有图。
5. 未通过的候选不进入正式 recipes。当前 No Pass 流程可以删除候选图片，反馈和历史属于工作台运行记录。
6. 已通过结果冻结；后续想改图应作为新候选，重新审核并分配新槽位，不静默覆盖旧图。
7. 每个变体都必须仍能使用原题的标准答案。如果修改实际改变了数学事实、必需指代或题意，应修正标注或作为新种子处理，不能借“对抗”名义沿用失效答案。
8. C 表示构造意图类别，不代表已经证明模型必错。实际是否诱导特定错误另存实验记录，不从颜色、红点或人工 Pass 推断攻击成功。

## 8. 哈希、环境和确定性重绘

### 8.1 参数哈希

当前通用规范化哈希：

```python
import hashlib
import json

def canonical_hash(value):
    payload = json.dumps(
        value, sort_keys=True, ensure_ascii=False,
        allow_nan=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
```

- A/B：`parameter_key = canonical_hash({"operation": operation, "params": params})`。
- C：`parameter_key = canonical_hash(完整的冻结插件)`，包含题号、description、intent 等插件字段；**不包含** recipe 的审核字段、路径或哈希字段。
- 不把“同样的浮点数显示得更短”视为无影响修改；数值精度、数值类型和动作数组顺序都应保持。不同操作或不同基线之间不能仅凭同一个参数哈希判定为同一数据。

### 8.2 图片哈希与插件文件哈希

`pixel_sha256` 的算法不是 `sha256(PNG字节)`，而是：

```python
from PIL import Image

with Image.open(image_path) as source:
    rgba = source.convert("RGBA")
    prefix = f"{rgba.width}x{rgba.height}:RGBA:".encode("ascii")
    pixel_sha256 = hashlib.sha256(prefix + rgba.tobytes()).hexdigest()
```

C 的 `png_sha256` 与 `plugin_sha256` 分别是对应文件原始字节的 SHA256。冻结插件即使只改缩进或换行，也会改变文件哈希，所以不要“格式化”已经通过的插件文件。

### 8.3 版本与基线

- `environment` 记录实际环境，不照抄示例。旧记录使用 Python `3.13.9`、Matplotlib `3.11.2`、NumPy `2.5.3`、Pillow `12.3.0`。
- 原图渲染协议版本、C 插件 schema 版本、A/B 生成器版本、C 生成器版本和本 Markdown 的组织协议版本是不同概念，不因都包含 `1.0.0` 就混为一项。
- A/B 与 C 的基线 manifest 结构不同，所以同一批原题的两个 `baseline_fingerprint` 也可以不同。必须让对应执行器真实计算，不能互相复制或用固定假哈希填充。
- 当前 C 的 `renderer_sha256` 是 `renderer_adapter.py`、`render_plugins.py`、`workbench_io.py` 三个文件各自 SHA256 所组成字典的 `canonical_hash`；`schema_sha256` 为 schema 文件字节哈希。
- 新批次须保存匹配的源程序、绘图协议、依赖版本、生成器实现、配置及必要的 baseline manifest。正式数据目录存成果；工作台运行状态另行配套备份。
- 当前基线绑定整批源文件。先完成本批种子冻结再收集变体；追加种子或修改源文件时按新批次/版本处理，不能删除指纹检查来强行接续旧状态。

重绘必须从原场景和冻结参数出发，不访问模型、不读取可变草稿、不重新采样。输出先写到独立验证目录，对比保存时的 `pixel_sha256`；不同则检查环境、源码和协议，不能把新图覆盖旧图来“让校验通过”。

## 9. 旧目录中的迁移问题与兼容边界

**保持数据格式不等于复制旧脚本后可以直接运行。** 目前已核实以下差异，后续执行 agent 必须先做相应适配：

| 旧实现的实际情况 | 新数据的处理要求 |
| --- | --- |
| 800 条 A/B recipe 的 `image_path` 仍为 `accepted/AnaXX/images/...`；实际文件在 `base_variant/AnaXX/images/` | 读取旧数据时显式识别此历史映射；新导出写数据根目录相对的 `base_variant/...`，不能在新根目录创建一个假的 `accepted/` 来掩盖问题 |
| 旧 A/B 工作台配置 `source_dir` 仍为 `../first_process` | 为新数据提供真实根目录和源文件定位，不照搬失效配置 |
| A/B `draw_variants.py` 带个人机器的绝对工作台路径回退 | 新生成的函数使用项目相对路径或明确配置的运行环境，不写 `C:\Users\...` |
| 原始生成脚本和题目类用 `parents[1]` 推断 ROOT；现在嵌套位置会把普通批量输出指向外层 `dataset_generator/` 内 | 新入口必须显式定位数据根目录，保证图和题目记录落到根目录的 `image/`、`dataset.jsonl`；不要未经检查直接运行旧批量入口 |
| 原生成脚本、工作台适配器、C schema 以及部分评测代码限制 `Ana01`～`Ana80` | 新题量不受 80 限制，但实现 agent 须先适配枚举、ID 校验和 UI；只增加文件不会自动支持第 81 题或少于 80 题的批次 |
| C 重绘函数能找到同级 `special_variant_workbench`，但其默认配置仍指向旧 `construct_dataset` | 新数据必须绑定自己的输入、输出、配置与状态；不能因成功 import 就认为重绘了新数据 |
| 原评测脚本含旧题量、旧路径和特定评分设置 | 保留题干/答案复用关系，按新数据清单适配；评分容差、模型与调用次数是实验配置，不是本数据格式的固定要求 |

新工作台需要使用独立 runtime、输出目录和 manifest，不能拿旧 `state/progress.json` 启动新数据。同样，复制 C 原始 recipe 或修改 schema / 渲染器后，不能继续冒用旧版本指纹。

本节仅记录兼容问题；**本次整理协议不授权 agent 自动修复、重算或覆盖旧数据**。

## 10. 二次收集的可选研究元数据

本节是为“错误模式 → 例题 → 扩展种子 → 视觉变体”建议的**独立扩展**，不是旧 `construct_dataset` 已经具有的字段。核心四字段原题记录、A/B recipes、C 插件结构保持不变。

推荐在新数据根目录增加 `seed_metadata.jsonl`，每题一行，用 `question_id` 关联种子题。字段约定可采用：

| 字段 | 类型 | 用途 |
| --- | --- | --- |
| `question_id` | string | 与 dataset 中的 id 连接 |
| `error_pattern_id` | string 或 null | 用户确认的目标错误模式 ID；不是模型失败事实 |
| `example_id` | string 或 null | 原始例题标识 |
| `family_id` | string 或 null | 同一例题/模板扩展出的种子家族 |
| `source` | object | 真实来源，如数据集名、原题号、URL 或本地相对文件路径；未知内容留空 |
| `derivation` | object | 相对例题的实际参数变换、固定数学参数，以及生成方法说明 |
| `difficulty` | object 或 null | 难度标签、判定依据及已知测量；未标注用 null，不由 agent 伪造统一难度 |

推荐对 C 变体另建可选的 `variant_metadata.jsonl`，以 `question_id + slot_id` 连接正式 recipe，记录目标 `error_pattern_id`、用户确认的 `intended_mechanism` 和真实证据位置 `evidence_refs`。未验证的机制写成假设，证据列表允许为空；不把这些字段写入禁止额外属性的 C 插件。

模式定义可以单独文档化。模式 ID、例题 ID、家族 ID 与数学题号职责不同，不用目录名称或槽位编号隐式编码所有含义。同一家族的难度控制、同一种子各变体的配对比较，都应据此元数据完成；`subject/level` 不能直接代替经确认的题目难度。

后续 agent 创建这些扩展前应沿用用户已经确认的模式定义和字段值；缺少信息时保留未标注状态，不自动发明错误模式、来源或实验结果。

## 11. 整理与交付核对清单

### 种子题冻结时

- [ ] `dataset.jsonl` 为合法 UTF-8 JSONL，ID 无重复，四个核心字段完整，答案类型正确。
- [ ] 每行恰好对应一张根目录原图和一个可定位的固定题目类；题干、答案、固定数学实例一致。
- [ ] 图片尺寸、不透明性、坐标范围和样式符合本批绘图协议。
- [ ] 重绘不重新随机，重复输出像素一致；数学与视觉正确性已由人工确认。
- [ ] 源程序、配置、依赖、来源映射和绘图协议与本批数据一起冻结；不存在个人绝对路径依赖。

### 变体入库时

- [ ] 只有人工通过的候选进入正式目录，时间、UUID 和哈希均来自实际过程。
- [ ] 完成 A/B 收集的题恰有 A=5、B=5；缺少某操作有实际不可用或审核原因，没有伪造 coverage。
- [ ] C 数量和实际人工决定一致；槽位连续，无自动补造记录。
- [ ] 每个 recipe 的题号、类别、操作、槽位、文件路径和文件名相互匹配；路径在本数据根目录内且文件存在。
- [ ] A/B 每槽位有图片、完整 params 和重绘函数；C 额外有独立冻结插件与全局索引对应行。
- [ ] C 插件与 recipe 的插件部分一致，索引与每题 recipes 一致；没有孤立图片、孤立插件或重复槽位。
- [ ] 重新计算参数哈希、图片像素哈希及 C 文件哈希，全部匹配；没有沿用其他题目或其他环境的伪指纹。
- [ ] 用本批匹配的执行器离线重绘每个通过槽位，在独立目录验证像素一致，不覆盖正式图片。
- [ ] 评测时每个视觉变体复用其种子的题干与答案；实验输出和研究标签不反向改写题目真值。
- [ ] 工作台状态、schema 和 baseline manifest 与该批数据对应；新批次不会读写旧数据集。

分阶段交付可以只有已冻结种子或部分通过变体，但必须如实说明完成范围。不得为了满足数量检查复制图片、填占位哈希或伪造人工审核记录。

## 12. 核对来源

需要进一步检查实现时，优先阅读以下实际文件；文档中的相对链接以本文件所在目录为起点：

- [原题清单](../construct_dataset/dataset.jsonl)
- [原图完整渲染协议](../construct_dataset/dataset_generator/protocol.json)
- [原题类样例](../construct_dataset/dataset_generator/dataset_generator/function_plot1-20.py)
- [原题批量入口](../construct_dataset/dataset_generator/dataset_generator/generate_dataset.py)
- [A/B recipe 样例](../construct_dataset/base_variant/Ana01/recipes.json)
- [A/B 生成与重绘](../variant_workbench/generate_variants.py)
- [A/B 哈希与持久化](../variant_workbench/workbench_io.py)
- [C recipe 样例](../construct_dataset/special_variant/Ana80/recipes.json)
- [C 全局通过索引](../construct_dataset/special_variant/accepted_index.jsonl)
- [C 插件 schema](../special_variant_workbench/plugin.schema.json)
- [C 标准插件执行器](../special_variant_workbench/render_plugins.py)
- [C 哈希与版本规则](../special_variant_workbench/workbench_io.py)
- [C 人工审核与保存](../special_variant_workbench/review_store.py)

发生冲突时先核实对应批次的冻结代码、schema、文件与审核记录，报告差异，不通过修改正式数据来掩盖冲突。
