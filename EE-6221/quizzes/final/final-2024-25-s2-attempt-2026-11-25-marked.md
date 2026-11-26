# EE6221 final · official 2024-25 S2 Q1 (D-H), marked attempt (2026-11-25)

**Script:** `attempts/final-2024-25-s2-q1-2026-11-25.jpg` (handwritten, scanned).
**Marked against:** the rubric in `final-relearn-q1-q2.html` Part 6 (the item split is ours, not NTU's).  Full grading: the "Your attempt" box there.

## Result: 19 / 20 (up from 12 / 20 on Mock A Q1)

| Item | Marks | Score |
|---|---:|---:|
| (a) z on joint axes | 6 | **6** |
| (a) x and origins | 3 | **3** |
| (a) y axes | 1 | **0** |
| (a) tool frame | 1 | **1** |
| (b) table rows | 6 | **6** |
| (b) matrices | 3 | **3** |
| **Total** | **20** | **19** |

## What was written

Arrows: ↗ = into page, ↙ = out of page.  The arm is drawn straightened with the link level; the θ offsets record that pose, which is allowed.

| k | θ | d (cm) | a (cm) | α |
|---|---|---|---|---|
| 1 | θ1 + 90° | 25 | 0 | 90° |
| 2 | θ2 | 11 | 0 | −90° |
| 3 | 90° | d3 | 0 | −90° |
| 4 | 90° + θ4 | 0 | −15 | −90° |
| 5 | 90° + θ5 | 4 | 0 | −90° |
| 6 | 180° + θ6 | 20 | 0 | 0 |

```
T01 = [ −S1  0  C1   0 ]   T12 = [ C2  0 −S2   0 ]   T23 = [ 0  0 −1  0  ]
      [  C1  0  S1   0 ]         [ S2  0  C2   0 ]         [ 1  0  0  0  ]
      [   0  1   0  25 ]         [  0 −1   0  11 ]         [ 0 −1  0  d3 ]
      [   0  0   0   1 ]         [  0  0   0   1 ]         [ 0  0  0  1  ]
```

Checked: these rows at q = 0, d3 = 20 put every frame exactly where it is drawn; the tip is at 80 cm out, 15 cm up.  All three matrices match the general link matrix entry for entry.

## Verdicts

- **Lost mark, y axes:** only y6 is drawn (correct: → × ⊗ = ↑).  y0–y5 are missing.  Draw at least y0 and check each with y = z × x (frame 0: → × ↑ = ⊙).
- a4 = −15 is valid (x4 points back toward z3) but a4 = +15 with x4 along the link means fewer signs to get wrong.
- Mock A items #1, #2, #3, #5 and the blank matrices are closed by this attempt.  #4 (y axes) stayed open until Mock B Q1.
