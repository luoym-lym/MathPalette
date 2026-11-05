# Solution — extension_04

The answer is **B (Board B)**.

Number rows from the top and columns from the left, starting at 1. Write 1 for a dark square and 0 for a white square. The displayed upper board is:

```
1 1 0 0
0 1 0 1
1 0 1 0
0 0 1 1
```

For a turn of 90 degrees in either direction, each square moves according to `clockwise: (r, c) -> (c, 5 - r); counterclockwise: (r, c) -> (5 - c, r)`. Applying this rule to every square gives:

```
0 1 0 1
0 0 1 1
1 1 0 0
1 0 1 0
```

These rows are exactly Board B; this is the actual content of the selected answer.

The upper pattern has half-turn symmetry: reversing both its row order and its column order leaves it unchanged. The clockwise and counterclockwise quarter-turns differ by a half-turn, so they give the same matrix shown above. Both permitted directions have been checked separately, and each selects the same option.

For the other options, a single disagreeing square is already enough to rule them out. Full matrix comparison gives the following certificates:

| Option | Disagreeing squares | One visible discrepancy |
| --- | ---: | --- |
| A | 8 | Row 1, column 1: expected white, but shown dark. |
| B | 0 | Every square agrees. |
| C | 8 | Row 1, column 2: expected dark, but shown white. |
| D | 16 | Row 1, column 1: expected white, but shown dark. |
| E | 2 | Row 1, column 1: expected white, but shown dark. |

Each allowed turn is a bijection of the grid squares, so the displayed source fixes every destination square. The five options are distinct, and exactly one equals the complete destination matrix. All options have the same number of dark squares; counting alone does not identify the answer. Flipping, mirroring and changing colours are excluded by the written conditions. Row and column numbering is only a way to describe the visible diagram; no hidden scene coordinates are needed.

相对父题的实质变化：8个深色格的半周对称配置，两个三格分量和两个孤立格；顺逆90度得到同一目标，显式核对全部允许方向。

独立核验：math_check.py 不导入 renderer，先使用整数笛卡尔格心坐标重新计算所有允许旋转，再读取并比较 question.json 中的答案。逐格映射、全部选项差异及跨题去重证据见 math_check.json。
