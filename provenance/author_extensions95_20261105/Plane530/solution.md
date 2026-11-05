# Solution

B = black, G = grey, W = white; a dot means that no square exists.
Read rows from top to bottom and positions within each row from left to right.

The initial pattern and each complete step are:

Initial state

```text
BGWW
WGBG
```

After step 1: First, replace every white square with a grey square.

```text
BGGG
GGBG
```

After step 2: Then replace every black square with a white square.

```text
WGGG
GGWG
```

After step 3: Finally, replace every grey square with a black square.

```text
WBBB
BBWB
```

Therefore the answer is **C**. Its actual pattern is:

```text
WBBB
BBWB
```

Why the other options fail:

- A: Applies each colour test to the original pattern instead of the current pattern. It disagrees at 3 square(s); for example, row 1, column 3 is G instead of B.
- B: Executes the three instructions in reverse order. It disagrees at 8 square(s); for example, row 1, column 1 is G instead of W.
- D: Stops after the second step. It disagrees at 6 square(s); for example, row 1, column 2 is G instead of B.
- E: Omits the first instruction. It disagrees at 3 square(s); for example, row 1, column 3 is W instead of B.

Uniqueness and interpretation:

Every rule is a total, deterministic operation on the current colours of a precisely specified set of squares. Unmentioned colours and positions stay unchanged. The position of every square is fixed; no rotation or reflection is allowed. Starting from the displayed pattern, each step therefore has exactly one result. Only the stated answer matches every square; the other four options are pairwise distinct and each has a mismatch.

Independent verification uses whole-pattern state simulation and, separately, composition of the three possible colour inputs at each position. Each position is independent, so checking all three inputs there covers all possible starting patterns under these rules. The checker also reconstructs all five option patterns from the frozen scene and checks every option.

Substantive change from the parent:

8格2×4矩形代替9格单行；先白变灰，再黑变白，最后灰变黑，产生白/黑而非父题灰/黑终态。
