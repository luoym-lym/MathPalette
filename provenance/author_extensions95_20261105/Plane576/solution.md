# Solution — extension_02

The answer is **A (Board A)**.

Number rows from the top and columns from the left, starting at 1. Write 1 for a dark square and 0 for a white square. The displayed upper board is:

```
1 1 0 0
1 0 0 1
0 0 1 1
0 0 0 1
```

For a turn of 90 degrees counterclockwise, each square moves according to `(r, c) -> (5 - c, r)`. Applying this rule to every square gives:

```
0 1 1 1
0 0 1 0
1 0 0 0
1 1 0 0
```

These rows are exactly Board A; this is the actual content of the selected answer.

For the other options, a single disagreeing square is already enough to rule them out. Full matrix comparison gives the following certificates:

| Option | Disagreeing squares | One visible discrepancy |
| --- | ---: | --- |
| A | 0 | Every square agrees. |
| B | 6 | Row 1, column 2: expected dark, but shown white. |
| C | 12 | Row 1, column 1: expected white, but shown dark. |
| D | 6 | Row 1, column 2: expected dark, but shown white. |
| E | 2 | Row 1, column 1: expected white, but shown dark. |

Each allowed turn is a bijection of the grid squares, so the displayed source fixes every destination square. The five options are distinct, and exactly one equals the complete destination matrix. All options have the same number of dark squares; counting alone does not identify the answer. Flipping, mirroring and changing colours are excluded by the written conditions. Row and column numbering is only a way to describe the visible diagram; no hidden scene coordinates are needed.

相对父题的实质变化：保留4×4但改为7个深色格，形成大小分别为3与4的两个连通分量；明确逆时针旋转。

独立核验：math_check.py 不导入 renderer，先使用整数笛卡尔格心坐标重新计算所有允许旋转，再读取并比较 question.json 中的答案。逐格映射、全部选项差异及跨题去重证据见 math_check.json。
