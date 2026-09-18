# EE6221 Quiz 1 — Mock 2, marked attempt (2026-09-18)

**Script:** `attempts/quiz-01-mock-02-2026-09-18.pdf` (2 pages, handwritten, scanned).
**Marked against:** `quiz-01-mock-02.md` (rubric, 20 core + 5 predicted = 25).
**Previous attempt for comparison:** `quiz-01-mock-01-attempt-2026-09-17-marked.md` (12/20 core).

## Result

| Part | Marks | Score | vs. Mock 1 |
|---|---:|---:|---|
| Q1(a) frame assignment | 4 | **4** | 3 → **4** |
| Q1(b) D–H parameter table | 3 | **3** | 1 → **3** |
| Q1(c) link transforms | 3 | **0** | 2 → 0 *(blank)* |
| Q1(d) arm matrix + check | 2 | **0** | 0 → 0 *(blank)* |
| **Q1 subtotal** | **12** | **7** | 6 → 7 |
| Q2(a) pick pose | 4 | **3** | 3 → 3 |
| Q2(b) place pose | 3 | **1** | 3 → 1 |
| Q2(c) checks + connecting rotation | 1 | **1** | 0 → **1** |
| **Q2 subtotal** | **8** | **5** | 6 → 5 |
| **Core total** | **20** | **12** | 12 → 12 |
| C1 multi-branch inverse kinematics | 3 | **0** | — *(blank)* |
| C2 cubic trajectory segment | 2 | **0** | — *(blank)* |
| **Grand total** | **25** | **12** | 15 → 12 |

Core is 12/20 again, but the composition moved substantially: the D–H modelling half went from
7/12 to 10/12 on the parts that were attempted, while **8 of the 13 lost marks are blank, not
wrong** — Q1(c), Q1(d) and the whole of Section C were never started.

## The fold-back worked

Mock 1's headline error was a D–H table that gave the rigid tool a joint row and lost the revolute
joint. That is fixed, and fixed properly:

| $k$ | $\theta_k$ | $d_k$ | $a_k$ | $\alpha_k$ |
|---|---|---|---|---|
| 1 | $\theta_1$ | $d_1$ | $0$ | $\pi/2$ |
| 2 | $\theta_2$ | $0$ | $a_2$ | $0$ |
| 3 | $\theta_3$ | $0$ | $a_3+L_t$ | $0$ |

with `joint var` arrowed at the $\theta$ column. Every checkpoint earned:

- Three joints, three rows, all three variables are $\theta$'s. **No tool row.**
- The tool is folded into row 3 as $a_3+L_t$ — which is exactly the handling the key permits, and
  the right one for this arm, since $x_3$ runs along link 3.
- The twist $\alpha_1=\pi/2$ is in **row 1**, the crux checkpoint, and rows 2 and 3 correctly carry
  $\alpha=0$ because the shoulder and elbow axes are parallel.
- No contradiction anywhere between the table and the diagram — the mock 1 failure mode
  ($\alpha_2=+90^\circ$ in the table vs. $R_x(-90^\circ)$ in the transform) does not recur.

That is the row-per-joint rule applied, not recited. 3/3.

## Q1(a) — 4/4, and it caught an error in my key

The third (final) diagram is correct on every checkpoint: $z_0$ vertical with $\theta_{01}$ arrowed
about it; frame 1 at the shoulder with $z_1$ into the page, so the $z_0\to z_1$ twist is explicit;
$z_2$ parallel to $z_1$; $x_2$ along link 2 and $x_3$ along link 3; $y$ drawn at every frame. Only
the final diagram was marked — the two earlier attempts are struck through.

**Your frame 2 sits at the elbow. My key's prose said the shoulder. You are right and the key was
wrong.** With $a_2$ in row 2, the link transform ${}^{1}T_2$ has translation column
$(a_2c_2,\ a_2s_2,\ 0)$ — non-zero — so frame 2's origin is displaced from frame 1's by exactly
$a_2$. Verified numerically at the part-(d) configuration:

| frame | origin | landmark |
|---|---|---|
| 0 | $(0,0,0)$ | base |
| 1 | $(0,0,4)$ | shoulder — $d_1$ up the column |
| 2 | $(0,\ 2.598,\ 5.5)$ | **elbow** — $\lvert o_2-o_1\rvert = 3 = a_2$ |
| 3 | $(0,\ 2.598,\ 8.5)$ | tool tip — $\lvert o_3-o_2\rvert = 3 = a_3+L_t$ |

The key's claim that "frame 1 and 2 origins coincide at the shoulder, since $a_1=0$" conflated two
different things. $a_1=0$ says frame 1's **origin lies on the column axis** — the shoulder axis
intersects it, so there is no common-normal offset in row 1. It says nothing about frames 1 and 2.
`quiz-01-mock-02.md` has been corrected; see the note at the end of this file.

None of this touches the marks or the arm matrix: the closed form was verified from the product of
the three link matrices, which never depended on that prose.

## Q1(c), Q1(d) — 0/5, blank

`⁰T₁`, `¹T₂`, `²T₃` and the arm matrix were not attempted. Nothing to mark and nothing wrong.

**This is now a confirmed pacing problem, not a one-off.** Mock 1 ended with Q1(d) blank; mock 2
ended with Q1(c), Q1(d) *and* all of Section C blank. Both times the table and diagram were strong
and the matrices ran out of clock. The visible cause on this script is three separate drawings of
the link-coordinate diagram — the first two struck through. On a 30-minute paper where (c) and (d)
are worth 5 of Q1's 12 marks, a redraw is expensive.

What to do about it, in order:

1. **Draw the frames once, in pencil, small.** Sketch the $z$ axes first and confirm the twist
   before inking any $x$ or $y$. The diagram is worth 4 marks; it is not worth 3 attempts.
2. **Write the three link matrices straight off the table.** Once the table is right, each matrix is
   a template substitution — roughly a minute each, and worth 3 marks. Never leave (c) blank when
   (b) is already correct: it is the cheapest mark on the paper.
3. **Budget by marks.** 12 + 8 marks in 30 min is about 1 min 20 s per mark: Q1 ≈ 18 min, Q2 ≈ 12
   min. If the diagram has eaten 10 minutes, move on and come back.

## Q2(a) pick pose — 3/4

Submitted:

$$
{}^{0}T_{\text{pick}}=\begin{bmatrix}-1&0&0&8\\ 0&1&0&3\\ 0&0&-1&1\\ 0&0&0&1\end{bmatrix}
$$

- Approach $r_3=(0,0,-1)$, descending onto the part: **1** ✓
- Closing direction $r_2=(0,1,0)$: **0**. Part E's long axis is along $y_0$, so its two long faces
  are the $6\times 2$ faces whose normals point along $\pm x_0$ — they are separated **along
  $x_0$**, so the jaws must close along $x_0$: $r_2=(1,0,0)$. As submitted the jaws would close along
  the part's 6-length and strike its short end faces.
- Right-handed orthonormal set: **1**. $r_1=r_2\times r_3=(0,1,0)\times(0,0,-1)=(-1,0,0)$ ✓,
  $r_1\times r_2=r_3$ ✓, $\det R=+1$ ✓. The frame is genuine — just assigned to the wrong pose.
- Translation $(8,3,1)$ = E's centroid: **1** ✓

## Q2(b) place pose — 1/3

Submitted:

$$
{}^{0}T_{\text{place}}=\begin{bmatrix}0&1&0&3\\ 1&0&0&8\\ 0&0&-1&4\\ 0&0&0&1\end{bmatrix}
$$

- Orientation: **0**. See below — it is the *pick* orientation.
- $x,y=(3,8)$ = F's centroid: **1** ✓
- $z=4$: **0**. F's top surface is at $2+\tfrac42=4$, and E's centroid must then rise its own
  half-height above that: $z=4+\tfrac22=5$. The answer stops at the supporting surface.

**On the $z$ regression.** You got this exact checkpoint *right* on mock 1 ($1+1+2=4$) and wrong
here. Mock 1's answer was also the number 4, which is suspicious — the two papers deliberately use
different block heights (mock 1: F-analogue height 2, moving part height 4; mock 2: F height 4,
moving part height 2). The formula is $z = z_{\text{support}} + \tfrac12 h_{\text{support}} +
\tfrac12 h_{\text{moving}}$ and it has **three** terms every time. Recompute it from the table on
the paper in front of you; do not carry a remembered number across papers.

## The real finding: your two rotations are exactly swapped

Both matrices you wrote are correct answers to this question — you just attached each to the wrong
pose:

| | correct | you wrote |
|---|---|---|
| $R_{\text{pick}}$ | $\begin{bmatrix}0&1&0\\1&0&0\\0&0&-1\end{bmatrix}$ | $\begin{bmatrix}-1&0&0\\0&1&0\\0&0&-1\end{bmatrix}$ ← the *place* answer |
| $R_{\text{place}}$ | $\begin{bmatrix}-1&0&0\\0&1&0\\0&0&-1\end{bmatrix}$ | $\begin{bmatrix}0&1&0\\1&0&0\\0&0&-1\end{bmatrix}$ ← the *pick* answer |

Verified: the swap is exact, and both are right-handed with $\det=+1$.

So this is **not** a failure to construct a gripper frame — you can do that, and Q2(c) proves you
can compose them. It is reading *which part orientation is in force at which moment*:

- **At the pick**, E is where it started: long axis along $y_0$. → jaws along $x_0$.
- **At the place**, E has been turned so its long axis lines up with F's: long axis along $x_0$.
  → jaws along $y_0$.

The habit that prevents it: before writing either matrix, write down the part's long-axis direction
*for that pose* on its own line. Two words — "long ∥ y₀" then "long ∥ x₀" — and the jaw direction
follows mechanically as the perpendicular one.

There is a second, sharper reason this matters. On mock 1 you wrote $r_2=(1,0,0)$ for the pick and it
was **wrong**; on mock 2 the pick needs exactly that $r_2$ and would have been **right**. You wrote
$(0,1,0)$ instead — the value that was correct last time. The two papers are built so that the
remembered answer fails and only the derivation succeeds, which is why the key carries a grader's
note about it. Derive $r_2$ from the part, every single time.

## Q2(c) checks and connecting rotation — 1/1

`RᵀR = I`, `det R = +1` stated, **and** the connecting rotation identified as

$$
R_z(-90^\circ)=\begin{bmatrix}0&1&0\\-1&0&0\\0&0&1\end{bmatrix},
$$

shown by explicit multiplication against your own pick matrix. Verified: $R_z(-90^\circ)$ does carry
*your* pick to *your* place. Full marks — the checkpoint is the check plus naming the rotation, both
done and done consistently.

For the record, with the poses the right way round the connector is $R_z(+90^\circ)$: the part turns
from long-axis-$y_0$ to long-axis-$x_0$. Your sign is the mirror of that because your pair is
mirrored. Marked against your own answers, per the rubric.

This is a clear gain over mock 1, where the orthonormality mark was lost to an illegible `3 yeah.`

## Section C — 0/5, blank

Neither the multi-branch inverse kinematics nor the cubic trajectory was attempted. Section C was
meant to be done **untimed, after stopping the clock** — so unlike Q1(c)/(d), this one wasn't a
pacing failure, it just wasn't started. Both topics are in scope and untested so far; worth doing
before the real quiz even without a timer. The key has full worked solutions.

## Slips vs. inverted concepts

**Inverted concept** — one, and it is a reading habit rather than a method gap:
1. Which part orientation applies at which pose. Both gripper frames were constructed correctly and
   composed correctly; they were assigned to the wrong poses.

**Slip:**
2. Place height stopped at the supporting surface, dropping the moving part's half-height — a
   checkpoint passed on mock 1, so this is execution, not understanding.

**Blank, not wrong:** Q1(c), Q1(d), C1, C2 — 10 marks unattempted out of the 13 lost.

**Fixed since mock 1:** the D–H table (1/3 → 3/3), the frame diagram (3/4 → 4/4), and the
orthonormality check (0/1 → 1/1).

## Correction to the mock itself

`quiz-01-mock-02.md` Q1(a) described the frame-2 and frame-3 origins wrongly and asserted that
frames 1 and 2 coincide at the shoulder. They do not: frame 2 is at the elbow, frame 3 at the tool
tip. The key has been corrected and the checkpoint reworded. Stated here rather than edited
quietly, because the student's diagram was right and the key was wrong.

## Confidence

All marks **derivable** — every answer re-derived independently and checked numerically (frame
origins from the link-matrix product; both rotation blocks for orthonormality, handedness and
determinant; the swap and the connecting rotation by explicit multiplication). No convention-
dependent or disputed items on this paper. The script is fully legible throughout — no repeat of
mock 1's unreadable cells.
