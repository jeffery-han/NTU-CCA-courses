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

---

# Mock 5 Q2 attempt — 2026-09-23, marked

Scan: `quizzes/attempts/quiz-01-mock-05-q2-2026-09-23.jpg`. Key: `quiz-01-mock-05.md` Q2.

**Score: 13/20.** Part (a) 9/12, part (b) 4/8. All seven z axes are correct. The losses come from
one concept error (d versus a) and from two slips seen again: the x direction, and a missing row.

The learner's table (six rows only):

| k | θ | d | a | α |
|---|---|---|---|---|
| 1 | θ1 | 0.65 | 0.22 | −π/2 |
| 2 | θ2+π/2 | 0 | 0.2 | π/2 |
| 3 | θ3+π | 0 | 0.15 | π/2 |
| 4 | θ4 | 0 | 0 | −π/2 |
| 5 | π/2 | d5 | 0 | π/2 |
| 6 | θ6+π | 0.05 | 0 | −π/2 |

**Numerical check with all joints at 0 and d5 = 0.3, plus the missing row 7 appended:**

- Origin 2 lands at z = 0.45. The 0.2 goes 0.2 m *down* along $x_2$, not along link 2.
- Origin 3 lands *above* frame 2. With θ3 + π, $x_3$ points up, but the link hangs down.
- $z_6$ points back toward the base, because of θ6 + π.
- The tip is at (0.40, 0, 0.65), not the figure's (0.84, 0, 0.55).

**Minimal corrected version of the learner's own table:**

| k | θ | d | a | α |
|---|---|---|---|---|
| 1 | θ1 | 0.65 | 0.22 | −π/2 |
| 2 | θ2+π/2 | 0 | **0** | π/2 |
| 3 | **θ3** | **0.20** | 0.15 | π/2 |
| 4 | θ4 | 0 | 0 | −π/2 |
| 5 | π/2 | d5 | 0 | π/2 |
| 6 | **θ6** | **−0.05** | 0 | −π/2 |
| 7 | **θ7** | **0.12** | **0** | **0** |

This version was verified numerically: the tip is at (0.84, 0, 0.55). The sign of d6 is the same
chirality issue as in the tutor's key. As an alternative, set θ5 = −π/2 and keep d6 = +0.05.

## Deductions

- **Concept: the 0.20 m is a d, not an a (−1 in a, −2 in b).** θ3 rolls about link 2's own axis, so
  $z_2$ lies along that link and the 0.20 m is measured along $z_2$. That makes it $d_3 = 0.20$.
  Also, $z_1$ and $z_2$ intersect, so $a_2 = 0$ and frames 1 and 2 share an origin. Writing
  $a_2 = 0.2$ moves the arm 0.2 m perpendicular to the link. This is a genuine gap, and it has been
  folded into the notes.
- **Slip (repeat of Q1): x₃ direction (−1 in b).** θ3 + π points $x_3$ up while the 0.15 m link
  hangs down. Point $x_3$ from $z_2$ toward $z_3$.
- **Missing joint (−1 in a, −1 in b).** The arm has seven joints, but the table has six rows and
  there is no frame 7 or tool frame. The row-count check in the notes (count the variable entries,
  count the joints) catches this.
- **Frame 6 (−1 in a, −1 in b).** The drawn $y_6$ (into the page) and $z_6$ (to the right) force
  $x_6$ to be vertical, which is parallel to $z_5$. That breaks $x_6 \perp z_5$. The θ6 + π offset
  also reverses $z_6$. The 0.05 sign has the same chirality problem as the tutor's key.

Credited: all $z$ axes, including the θ3 roll axis along link 2; row 1; row 4; and row 5 written
correctly as θ fixed with d5 variable.

## Folded into notes

"A length along a joint axis is a d, not an a", together with the $x_k \perp z_{k-1}$ check and the
tip-walk check, was added to `notes/beginner-notes.tex` (a new pitfall paragraph) and to
`notes/notes.tex` (practical workflow).
