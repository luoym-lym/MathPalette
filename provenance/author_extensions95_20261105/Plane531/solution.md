# Solution

B = black, G = grey, W = white; a dot means that no square exists.
Read rows from top to bottom and positions within each row from left to right.

The initial pattern and each complete step are:

Initial state

```text
G...
WB..
BGW.
WGGB
```

After step 1: First, replace every grey square with a black square.

```text
B...
WB..
BBW.
WBBB
```

After step 2: Then replace every white square with a grey square.

```text
B...
GB..
BBG.
GBBB
```

After step 3: Finally, replace every black square with a white square.

```text
W...
GW..
WWG.
GWWW
```

Therefore the answer is **E**. Its actual pattern is:

```text
W...
GW..
WWG.
GWWW
```

Why the other options fail:

- A: Applies each colour test to the original pattern instead of the current pattern. It disagrees at 4 square(s); for example, row 1, column 1 is B instead of W.
- B: Executes the three instructions in reverse order. It disagrees at 10 square(s); for example, row 1, column 1 is B instead of W.
- C: Stops after the second step. It disagrees at 7 square(s); for example, row 1, column 1 is B instead of W.
- D: Omits the first instruction. It disagrees at 4 square(s); for example, row 1, column 1 is G instead of W.

Uniqueness and interpretation:

Every rule is a total, deterministic operation on the current colours of a precisely specified set of squares. Unmentioned colours and positions stay unchanged. The position of every square is fixed; no rotation or reflection is allowed. Starting from the displayed pattern, each step therefore has exactly one result. Only the stated answer matches every square; the other four options are pairwise distinct and each has a mismatch.

Independent verification uses whole-pattern state simulation and, separately, composition of the three possible colour inputs at each position. Each position is independent, so checking all three inputs there covers all possible starting patterns under these rules. The checker also reconstructs all five option patterns from the frozen scene and checks every option.

Substantive change from the parent:

10格左对齐四层阶梯；灰先并入黑，白再变灰，黑最后变白。阶梯轮廓与各层颜色分布均新建。
