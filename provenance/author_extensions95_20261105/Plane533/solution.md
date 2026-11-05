# Solution

B = black, G = grey, W = white; a dot means that no square exists.
Read rows from top to bottom and positions within each row from left to right.

The initial pattern and each complete step are:

Initial state

```text
BWGG
G..W
W..B
GBWG
```

After step 1: First, in the whole pattern, replace every white square with a black square.

```text
BBGG
G..B
B..B
GBBG
```

After step 2: Then, in the leftmost column only, replace every black square with a grey square.

```text
GBGG
G..B
G..B
GBBG
```

After step 3: Finally, in the whole pattern, replace every grey square with a white square.

```text
WBWW
W..B
W..B
WBBW
```

Therefore the answer is **A**. Its actual pattern is:

```text
WBWW
W..B
W..B
WBBW
```

Why the other options fail:

- B: Applies each colour test to the original pattern instead of the current pattern. It disagrees at 2 square(s); for example, row 1, column 1 is G instead of W.
- C: Executes the three instructions in reverse order. It disagrees at 7 square(s); for example, row 1, column 1 is G instead of W.
- D: Stops after the second step. It disagrees at 7 square(s); for example, row 1, column 1 is G instead of W.
- E: Omits the first instruction. It disagrees at 3 square(s); for example, row 1, column 2 is W instead of B.

Uniqueness and interpretation:

Every rule is a total, deterministic operation on the current colours of a precisely specified set of squares. Unmentioned colours and positions stay unchanged. The position of every square is fixed; no rotation or reflection is allowed. Starting from the displayed pattern, each step therefore has exactly one result. Only the stated answer matches every square; the other four options are pairwise distinct and each has a mismatch.

Independent verification uses whole-pattern state simulation and, separately, composition of the three possible colour inputs at each position. Each position is independent, so checking all three inputs there covers all possible starting patterns under these rules. The checker also reconstructs all five option patterns from the frozen scene and checks every option.

Substantive change from the parent:

12格4×4空心方框；中间2×2区域不属于图案。第二步仅改最左列，第一步新生成的黑格会继续被改色。
