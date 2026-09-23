# Mock 5 Q1 attempt — 2026-09-23, marked

Scan: `quizzes/attempts/quiz-01-mock-05-q1-2026-09-23.jpg`. Key: `quiz-01-mock-05.md` Q1.

**Score: 18/20.** Part (a) 11/12, part (b) 7/8. Both deductions are convention slips; there is no
inverted concept.

The learner's table uses the learner's own frames, with every joint zero set to the drawn pose.

| k | θ | d | a | α |
|---|---|---|---|---|
| 1 | q1+π/2 | 0.47 | 0 | π/2 |
| 2 | q2+π/2 | 0.16 | −0.15 | π/2 |
| 3 | q3+π/2 | 0 | 0.18 | 0 |
| 4 | q4 | 0 | 0.17 | π/2 |
| 5 | q5+π/2 | 0.05 | 0 | π/2 |
| 6 | q6 | 0.20 | 0 | 0 |

**Numerical check at q = 0.** Every drawn axis is reproduced:

- $z_0$ up, $z_1$ along the q2 pipe, $z_2$ and $z_3$ into the page, $z_4$ up, $z_5$ and $z_6$ along
  the tool.
- $x_2$ up, $x_5$ and $x_6$ into the page.
- Tool tip at (0.71, 0, 0.37) m, which matches the figure.

The +π/2 offsets are valid: they make the drawn pose q = 0. Writing α4 = +π/2 where the tutor has
−π/2 is also valid, because the learner's $z_4$ direction differs from the tutor's.

## Deductions

- **(b) −1: a2 = −0.15.** The learner drew $x_2$ pointing up, but joint 3 hangs 0.15 m below
  joint 2. D–H takes $a_k$ as a distance along $x_k$ with $x_k$ pointing from $z_{k-1}$ toward
  $z_k$, so the fix is to point $x_2$ down and write a2 = +0.15. The row-3 offset then changes from
  q3+π/2 to q3−π/2. The learner's result is mathematically consistent, but the length is
  nonstandard.
- **(a) −1: legibility.** The wrist region (frames 5–6) contains a second, overdrawn set of axes.
  A marker cannot tell which one is final. In the exam, cross out the abandoned attempt cleanly.

## Folded into notes

The $x_k$ direction rule and why it gives $a_k \ge 0$ were added to `notes/beginner-notes.tex`
(D–H construction order) and `notes/notes.tex` (practical workflow).
