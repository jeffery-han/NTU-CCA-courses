# EE-6204 Quiz 1 - Mock Paper 2: answer key, reasons, and traps

**Companion to `quiz.html` (built from `question-bank.json`).** 27 items, 1 mark each,
**total 27**. Sit `quiz.html` cold first - it is answer-free until you press *Finish and
score*, and this file spoils it.

This paper is **unofficial and not a prediction**. It matches the official Quiz 1 shape - MCQ;
scope = graphical method + simplex method + sensitivity analysis for the simplex method; no
calculator (`quizzes/quiz-1-official-announcement.pdf`) - but every LP and number was written
from scratch. Rationale for the item mix is in `evidence-report.md`. This is the **second** MCQ
mock; the first is `quizzes/quiz-1-mcq-practice.*` (18 items, different LPs). Do both.

The `quiz.html` marks every item in the browser and the `explanation` text (also embedded in
the page) is the full worked reason. This file adds the single-line key, the trap behind each
distractor, and the part-by-part marking table.

**No countdown timer** in this template. Give yourself ~45 min.

---

## Answer key (single line)

```
A1 33   A2 b   A3 c   A4 a,b,d   A5 c   A6 a   A7 d   A8 b   A9 c
B1 b   B2 d   B3 a   B4 b   B5 c   B6 a   B7 c   B8 b   B9 d   B10 a
C1 3   C2 c   C3 b   C4 d   C5 d   C6 a   C7 c   C8 a,c,d
```

CLI cross-check: `assessment_cli.py score question-bank.json attempt-selfcheck.json` -> 27/27.

---

## Spine LP (Parts A, B, C share it)

    maximize   z = 6 x1 + 5 x2
    s.t.           x1 +   x2 <= 6      (R1)
                 3 x1 + 2 x2 <= 15     (R2)
                   x1 , x2 >= 0

- Vertices: (0,0) 0 | (5,0) 30 | (3,3) **33** | (0,6) 30.  Optimum **(3, 3), z = 33**, both
  constraints binding.
- Simplex (z - c^T x row): T0 basis (s1,s2) -> enter x1 (-6), leave s2 (15/3 = 5) ->
  T1 basis (s1,x1), z row [0,-1,0,2 | 30] -> enter x2 (-1), leave s1 (1 / (1/3) = 3) ->
  **T2** basis (x2,x1):

      x2 | 0  1   3  -1 | 3
      x1 | 1  0  -2   1 | 3
      z  | 0  0   3   1 | 33     <- all >= 0, optimal

- Shadow prices: **R1 = 3, R2 = 1** (z-row under s1, s2). Dual check b^T w = 6(3)+15(1) = 33. OK
- Allowable ranges: **b1 in [5, 7.5]**, **b2 in [12, 18]**, **c1 in [5, 7.5]**, **c2 in [4, 6]**.

---

## Part A - graphical method (A1-A9)

| # | Ans | One-line reason | Distractor traps |
|---|---|---|---|
| A1 | **33** | Highest z over the 4 vertices, at (3,3). | 30 = value at (5,0) or (0,6). |
| A2 | **b** (3,3) | Only vertex that beats 30. | (5,0)/(0,6) stop at a first-hit axis vertex; (4,2) is infeasible - 3(4)+2(2)=16 > 15 (checked only R1). |
| A3 | **c** both | Sub (3,3): both lines tight, both slacks 0. | "Only R1/only R2" name one edge; "interior" ignores that a max sits on the boundary. |
| A4 | **a,b,d** | Region bounded; (5,0) is the x2=0 / R2 vertex; unique optimum => single contact point. | c is false: z(0,6) = 30 < 33. Miss = wrong tick set (exact-set scoring). |
| A5 | **c** [5, 7.5] | Iso-profit slope -c1/5 must lie between edge slopes -3/2 and -1. | [4,6] is the c2 range; [5,6] truncates one side; "any c1>0" ignores the rotation limit. |
| A6 | **a** (3,1), z=9 | Min over vertices (0,4),(3,1),(6,0) of a >=-constrained region. | (0,4)/(6,0) give 12; "unbounded" confuses an unbounded region with an unbounded objective (a min is fine). |
| A7 | **d** degenerate | Three lines x1+x2=4, x1=2, x2=2 all pass through (2,2); a 2-D vertex needs only 2. | "unbounded/infeasible/interior" - the point is feasible, bounded, and a corner. |
| A8 | **b** x1+x2<=10 | Every feasible point already has x1+x2 <= 6. | x1<=4 cuts (5,0); x2<=2 and 2x1+x2<=6 each cut (3,3). |
| A9 | **c** infinitely many | Objective 4x1+6x2 = 2(2x1+3x2) is parallel to the binding edge 2x1+3x2=12; whole edge gives z=24. | The two "unique optimum" options each pick one endpoint of that edge. |

## Part B - simplex method (B1-B10)

| # | Ans | One-line reason | Distractor traps |
|---|---|---|---|
| B1 | **b** +s2 = 15 | A <= row takes a non-negative slack. | a = surplus (>= rows); c = free slack breaks non-negativity; d = needless artificial. |
| B2 | **d** x1 (-6) | Most-negative bottom-row entry is the standard entering pick. | "x2 smaller coef" / "s1 largest ratio" are not the rule; "already optimal" - negatives remain. |
| B3 | **a** s2, 15/3 = 5 | Minimum non-negative ratio over positive column entries. | "s1 larger ratio" drives s2 negative; "larger obj coef" is not the test; not unbounded (both entries > 0). |
| B4 | **b** the 3 (s2 row, x1 col) | Pivot = entering column intersect leaving row. | Never the z-row entry or an RHS number; the s1-row 1 is the wrong row. |
| B5 | **c** x1=5, x2=0, s1=1, s2=0, z=30 | Basic vars = their RHS; non-basic (x2,s2) = 0; z = obj-row RHS. | (3,3,z=33) is the FINAL answer two pivots on, not this tableau. |
| B6 | **a** not optimal, x2 enters | The -1 under x2 is a remaining improvement direction. | +2 under s2 is not; x1 is already basic; "optimal" ignores the -1. |
| B7 | **c** all z-row entries >= 0 | That is exactly the stopping rule for a z - c^T x maximization. | "both vars basic" / "RHS >= 0" are true here but not the criterion; "sum of RHS" is a coincidence. |
| B8 | **b** unbounded | x2 should enter but its column (-1,-3) has no positive entry - no ratio test row. | "optimal" ignores the -2; can't pivot on a negative; a non-basic var can't "leave". |
| B9 | **d** alternative optima | Non-basic x2 with reduced cost 0 => can enter without changing z. | "degenerate" = a BASIC var at 0 (different); the 0 under basic s2 is normal, the one under non-basic x2 is not. |
| B10 | **a** -e3 + a3 = 8 | A >= row needs a surplus to equalise AND an artificial for the start basis. | +s3 is the <= rule; -e3 alone has no starting basic var; negating makes RHS < 0. |

## Part C - sensitivity analysis for the simplex method (C1-C8)

| # | Ans | One-line reason | Distractor traps |
|---|---|---|---|
| C1 | **3** | z-row coefficient under s1 in the final tableau. | 1 is R2's price (wrong slack column). |
| C2 | **c** up to 1, within range | R2 shadow price = 1; and only over its allowable b2 range. | "up to 5" = an objective coef; "any price" / "0" mis-state a binding resource's value. |
| C3 | **b** 36 | 33 + (shadow price 3)(+1); new x-values 6 and 1 are >= 0, so the rate is valid. | 33 ignores it; 39/42 use the wrong rate. |
| C4 | **d** [12, 18] | x2 = 3 - D >= 0 and x1 = 3 + D >= 0 => D in [-3, 3]. | [10,20]/[13,17] are wrong widths; "always" forgets the basis can change. |
| C5 | **d** No - 25 is outside [12,18] | A shadow price is a LOCAL rate; past the range the basis (and rate) change. | "Yes" answers extrapolate a local rate globally; "rate is 3" is R1's, not R2's. |
| C6 | **a** Yes - 7 > 3(1)+1(2) = 5 | Reduced cost of the new column is +2 > 0, so it would enter. | "below 33" compares the wrong things; "no room" forgets you'd substitute, not just add; "can't tell" - the pricing test IS the tool. |
| C7 | **c** [4, 6] | c2 = 5 + d: keep 3 + 3d >= 0 and 1 - d >= 0 => d in [-1, 1]. | [0,10]/[3,7] are wrong widths; "exactly 5" forgets a whole interval keeps the basis. |
| C8 | **a,c,d** | Binding constraint => price may be > 0 (a); x1 > 0 => its dual constraint tight (c); w = (3,1) are the z-row prices (d). | b is false: it reverses complementary slackness (binding => price CAN be positive, not forced to 0). |

---

## Marking table

| Part | Items | Marks | What it tests |
|---|---|--:|---|
| A - graphical method | A1-A9 | 9 | vertex enumeration, binding set, iso-profit gradient / objective-coef range, graphical minimisation, degeneracy, redundancy, alternative optima |
| B - simplex method | B1-B10 | 10 | standard form (<= and >=), entering / leaving / ratio test, pivot element, reading a mid-run BFS, optimality criterion, unboundedness and alternative optima from a tableau |
| C - sensitivity for the simplex method | C1-C8 | 8 | shadow prices off the z-row, willingness-to-pay, RHS delta-z, RHS and objective-coefficient ranges, the extrapolation trap, pricing a new variable, complementary slackness |
| **Total** | **27** | **27** | |

Pass target on the page: 70% (19/27). Below ~60% -> re-read `notes/beginner-notes.tex` sec 3-6
before the quiz.

## After grading - fold misses back in

For each wrong item decide **slip** (misread a tableau, arithmetic) vs **inverted concept**
(wrong rule). Only the second kind needs a note edit.

- Concept miss on **B1 / B7 / B8 / B10 / C1 / C8** -> the rule is already in
  `notes/beginner-notes.tex` (sec 4 standard form, sec 5 stopping rule / unboundedness, sec 6
  shadow prices / complementary slackness). Re-read; thicken via `/update` if the note is thin.
- Miss on **C4 / C5 / C7** (RHS / objective ranging and its validity limit) is the most likely
  real gap - `beginner-notes.tex` sec 6 has the `B^-1 (b + db) >= 0` condition but no fully
  worked range. The spine LP here is a clean candidate for a worked example (`/update`).
- Miss on **A5 / A9 / B9** (objective-coef range from the graph; alternative optima from the
  graph vs from a tableau) -> `notes/notes.tex` sec 2-3: check the "special cases" coverage.
- Slips on **A1 / A2 / B5 / C3** (wrong vertex, wrong tableau, arithmetic) are "slow down and
  check" items, not note gaps.

Record durable misses in `assessment/weakness-log.json`.
