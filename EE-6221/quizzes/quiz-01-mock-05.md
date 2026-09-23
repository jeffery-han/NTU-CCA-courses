# EE6221 Quiz 1 scope — Mock 5: tutor past-paper set, answer key

**Paper:** `quiz-01-mock-05.html`. The questions are the Quiz-1-scope (kinematics) items from the
unofficial tutor review slides `resources/ee6221-tutor-exam-review-2026.pdf`, pp. 4–26. Year labels
are the tutor's. They refer to past **final-exam** questions, not to past Quiz 1 papers. The
dynamics and control half (pp. 27–58) is outside Quiz 1 scope.

**Verification:** `quiz-01-mock-05-check.py` builds every D–H table below. For each table it finds
a pose where each $z_{k-1}$ lies on joint $k$'s physical axis and the tool tip equals the figure's
dimension sums. It also checks the Q5 Jacobian against finite differences, both Q5 IK branches, and
the Q6 numbers. Run it with `python3 quiz-01-mock-05-check.py`.

The tutor's handwritten keys were **not** adopted blindly. Two errors and one typo were found:

1. **Q2, row 6 sign (a real error).** The tutor's table puts the 0.05 m gripper offset on the
   wrong side, so it describes a mirror image of the drawn robot.
2. **Q1, row 2 label (a typo).** p. 10 labels row 2 "q1"; it should be q2.
3. **Q5, part (ii) (a typo).** p. 23 writes "y = 0.2 − C₁q₂…"; the "−" should be "=".

**Total:** 80 source marks for Q1–Q4 (20 each) plus 20 practice-weighted marks for Q5–Q6 (10 each). The Q5–Q6 source marks are not shown, so the set totals 100.

D–H tables are not unique. Grade an answer against **its own drawn frames**. A table is right when
each row reproduces the drawn $x_{k-1}\to x_k$ and $z_{k-1}\to z_k$ steps.

---

## Q1 — six-joint arm (tutor p. 9–10, "23-24 S2 Q1"), 20 marks

**Reference frames (tutor's choice, verified).**

- Frame 0 is at the base on the waist axis, with $z_0$ up and $x_0$ to the right.
- $z_1$ lies along the q2 pipe (horizontal, pointing right), and $y_1$ points up.
- Frame 2 is at the q3 centre. $x_2$ points down the 0.15 m drop, and $z_2$ is along the q3 axis
  (into or out of the page).
- $z_3 \parallel z_2$, at q4.
- $z_4$ is vertical (the q5 axis), with its origin on q5, 0.17 m from q4.
- $z_5$ is horizontal (the q6 roll axis), raised 0.05 m.
- Frame 6 is at the tool tip, with $z_6$ as the approach direction.

| k | θ | d (m) | a (m) | α |
|---|---|---|---|---|
| 1 | q1 | 0.47 | 0 | π/2 |
| 2 | q2 | 0.16 | 0.15 | π/2 |
| 3 | q3 | 0 | 0.18 | 0 |
| 4 | q4 | 0 | 0.17 | −π/2 |
| 5 | q5 | 0.05 | 0 | π/2 |
| 6 | q6 | 0.20 | 0 | 0 |

Verified pose: $(90°, −90°, 90°, 0, 90°, 0)$. At that pose the tip is at $(0.71, 0, 0.37)$ m, which
equals $(0.16+0.18+0.17+0.20,\;0,\;0.47−0.15+0.05)$.

**Rubric.**

- (a) 12 marks:
  - 6 marks: one per $z_{k-1}$ on joint $k$'s axis.
  - 3 marks: $x$ axes along the common normals, with origins at the axis intersections.
  - 1 mark: $y$ axes right-handed.
  - 1 mark: base frame.
  - 1 mark: tool frame, with $z_6$ as the approach.
- (b) 8 marks:
  - 6 marks: one per row.
  - 1 mark: the variables identified (all six joints are revolute).
  - 1 mark: $\alpha$ signs consistent with the drawn frames.

**Common wrong paths.**

- **Putting $z_1$ vertical.** The q2 arrow circles the horizontal pipe, so q2 is a roll about that
  pipe. Misreading it points to reading the curl arrows too quickly.
- **Placing $d_2 = 0.15$ and $a_2 = 0.16$.** The 0.16 m run lies *along* $z_1$, so it is a $d$.
  The 0.15 m drop lies along $x_2$, so it is an $a$.
- **Using $a_5 = 0.05$.** The offset lies along $z_4$ (vertical), so it is $d_5$.

## Q2 — seven-joint arm (tutor p. 11–12, "22-23 S2 Q1"), 20 marks

**Reference frames (tutor's choice).**

- Frame 1 sits on the θ2 axis. The 0.22 m offset is $a_1$ and the 0.65 m height is $d_1$.
- $z_1$ is horizontal (the θ2 axis). $z_2$ lies along the 0.20 m link (the θ3 roll axis).
- $z_3$ is the θ4 axis, reached 0.20 m along $z_2$ ($d_3$) and 0.15 m along $x_3$ ($a_3$).
- $z_4$ lies along the prismatic direction.
- $z_5$ is vertical (the θ6 axis), and $z_6$ is horizontal (the θ7 roll axis).

| k | θ | d (m) | a (m) | α |
|---|---|---|---|---|
| 1 | θ1 | 0.65 | 0.22 | −π/2 |
| 2 | θ2 | 0 | 0 | −π/2 |
| 3 | θ3 | 0.20 | 0.15 | π/2 |
| 4 | θ4 | 0 | 0 | −π/2 |
| 5 | π/2 (fixed) | **d5 (variable)** | 0 | π/2 |
| 6 | θ6 | **−0.05** (tutor wrote +0.05) | 0 | −π/2 |
| 7 | θ7 | 0.12 | 0 | 0 |

**Correction.** With the tutor's rows 1–5, the pose that points the 0.15 m link down, as drawn, gives
$\theta_3 = 180°$. At that pose $z_5$ points **down**, so $d_6 = +0.05$ would put the gripper
0.05 m *below* the prismatic line. The figure shows the gripper 0.05 m *above* it.

No joint angles can fix this, and the reason does not depend on the checker's search. θ3 rolls
about link 2's own axis. A 180° roll therefore carries the 0.15 m link and the 0.05 m offset across
*together*, while the prismatic stage still points outward. θ4, θ6 and θ7 cannot separate them
either. So the tutor's rows always put the link and the offset on the **same** side of the arm. The
figure has them on **opposite** sides: the link goes down and the gripper sits up. A cross-product
sign test gives −1 for the tutor's rows and +1 for the figure. Two equivalent fixes exist:

- Keep $\theta_5 = \pi/2$ and set $d_6 = −0.05$.
- Set $\theta_5 = −\pi/2$ and keep $d_6 = +0.05$. This flips $x_5$ and therefore $z_5$.

Both pass the check, with the tip at $(0.22+0.20+d_5+0.12,\;0,\;0.65−0.15+0.05)$. An answer whose
own drawing has $z_5$ pointing up and $d_6 = +0.05$ is also correct.

**Rubric.**

- (a) 12 marks:
  - 7 marks: one per $z$ axis.
  - 3 marks: $x$ axes and origins, including frames 1–2 sharing an origin.
  - 1 mark: right-handed $y$.
  - 1 mark: tool frame.
- (b) 8 marks:
  - 7 marks: one per row.
  - 1 mark: row 5 written with θ fixed and d variable.

**Common wrong paths.**

- **Making θ3 a pitch joint.** The θ3 arrow circles the 0.20 m link, so θ3 is a roll about it.
- **Writing row 5 with $\theta_5$ variable.** Joint 5 is prismatic, so $d_5$ is the variable and
  $\theta_5$ is a constant.
- **Placing the 0.05 m offset on the wrong side** (the tutor's own slip). Check the offset's
  direction at a drawn pose.

## Q3 — wall-mounted arm (tutor p. 13–16, "24-25 S2 Q1"), 20 marks, cm

**Reference frames (tutor's choice, verified).**

- Frame 0 is at the wall on the θ1 axis. $z_0$ points out of the wall (to the right), $y_0$ points
  down, and $x_0$ points out of the page.
- $z_1$ points up (the θ2 axis), 25 cm from the wall.
- $z_2$ points along the prismatic direction, raised 11 cm.
- $z_3$ is the θ4 axis (along $x_0$), at the end of $d_3$.
- $z_4$ is the θ5 axis, perpendicular to the link, at 15 cm.
- $z_5$ lies along the gripper (the θ6 roll axis), offset 4 cm toward the upper side of the link.
  The gripper centreline in the figure is on that side.
- Frame 6 is at the tool tip.

| k | θ | d (cm) | a (cm) | α |
|---|---|---|---|---|
| 1 | θ1 | 25 | 0 | π/2 |
| 2 | θ2 | 11 | 0 | −π/2 |
| 3 | −π/2 (fixed) | **d3** | 0 | −π/2 |
| 4 | θ4 | 0 | 15 | −π/2 |
| 5 | θ5 | 4 | 0 | π/2 |
| 6 | θ6 | 20 | 0 | 0 |

Verified with $d_3 = 20$: the tip is at $(0, −15, 80)$ cm, which is 11 + 4 cm up and
25 + 20 + 15 + 20 cm out from the wall.

**First three link matrices:**

$$
{}^0T_1=\begin{bmatrix}C_1&0&S_1&0\\S_1&0&-C_1&0\\0&1&0&25\\0&0&0&1\end{bmatrix},\quad
{}^1T_2=\begin{bmatrix}C_2&0&-S_2&0\\S_2&0&C_2&0\\0&-1&0&11\\0&0&0&1\end{bmatrix},\quad
{}^2T_3=\begin{bmatrix}0&0&1&0\\-1&0&0&0\\0&-1&0&d_3\\0&0&0&1\end{bmatrix}
$$

The tutor's matrices on p. 16 match these. For ${}^2T_3$, use $\cos\theta = 0$,
$\sin\theta = −1$ and $\sin\alpha = −1$.

**Rubric.**

- (a) 11 marks:
  - 6 marks: one per $z$ axis.
  - 3 marks: $x$ axes and origins.
  - 1 mark: $y$ axes.
  - 1 mark: tool frame.
- (b) 9 marks:
  - 6 marks: one per row.
  - 3 marks: one per matrix.

**Common wrong paths.**

- **Setting $z_0$ vertical.** The base is on a wall, and θ1 rolls about the horizontal axis that
  comes out of the wall.
- **Keeping θ3 = 0 in row 3.** $x_2 \to x_3$ still involves a fixed rotation. Read it from your own
  frames.
- **Writing the matrices in degrees, or leaving $\cos(-\pi/2)$ unevaluated** in ${}^2T_3$.

## Q4 — prismatic-column arm (tutor p. 4, year label uncertain, **no tutor solution**), 20 marks

**Reference frames (derived here).**

- Frame 0 is at the column base, with $z_0$ up (the q1 slide axis) and $x_0$ to the right.
- Frame 1 is on the q2 axis at beam height. $z_1$ points **down** along the q2 axis and $x_1$
  points to the right. $z_0 \parallel z_1$, so $a_1 = 0.15$ and $d_1 = q_1$, which is variable.
- Frame 2 is at the q3 centre, 0.20 m down $z_1$. $z_2$ points into the page and $x_2$ points to
  the right.
- Frame 3 is at the q4 centre, with $x_3$ along the 0.19 m link.
- Frame 4 is at the q5 centre, with $z_4$ into the page.
- Frame 5 is at the q5 centre, with $z_5$ along the gripper (the q6 roll axis).
- Frame 6 is at the tool tip, 0.25 m along $z_5$.

| k | θ | d (m) | a (m) | α |
|---|---|---|---|---|
| 1 | 0 (fixed) | **q1** | 0.15 | π |
| 2 | q2 | 0.20 | 0 | π/2 |
| 3 | q3 | 0 | 0.19 | 0 |
| 4 | q4 | 0 | **√(0.18² + 0.10²) ≈ 0.206** | 0 |
| 5 | q5 | 0 | 0 | π/2 |
| 6 | q6 | 0.25 | 0 | 0 |

**The key trap (row 4).** The q4 and q5 axes are **parallel**; both point into the page. D–H
therefore forces $x_4$ along their common normal: 0.18 m across and 0.10 m down, a single diagonal
of length 0.206 m. You cannot write $a_4 = 0.18$ with a "$d = 0.10$", because any $d$ is measured
along $z$ (into the page), not downward. The drawn L-shape is absorbed into a constant offset in
$\theta_4$ and $\theta_5$: the angle is $\operatorname{atan2}(0.10, 0.18) = 29.05°$. At the verified
pose $(\theta_4, \theta_5) = (29.05°, 60.95°)$ with q1 = 0.80, the tip is at
$(0.15+0.19+0.18+0.25,\;0,\;0.80−0.20−0.10) = (0.77, 0, 0.50)$.

Accepted alternatives:

- $z_1$ **up** with $\alpha_1 = 0$ and $d_2 = −0.20$. The other signs then follow the drawn frames.
- Treating q1 as measured to a different height, as long as $d_1$ is marked variable.

**Rubric.**

- (a) 12 marks:
  - 6 marks: one per $z$ axis. $z_0$ and $z_1$ are both vertical; $z_2$, $z_3$ and $z_4$ are
    parallel.
  - 3 marks: $x$ axes and origins, with $x_4$ along the diagonal common normal.
  - 1 mark: $y$ axes.
  - 1 mark: base frame.
  - 1 mark: tool frame.
- (b) 8 marks:
  - 6 marks: one per row.
  - 1 mark: q1 identified as the prismatic $d_1$.
  - 1 mark: $a_4 = 0.206$ m, justified.

**Common wrong paths.**

- **$a_4 = 0.18$ plus a phantom vertical offset.** This comes from reading drawn link shapes
  instead of joint axes.
- **Making q2 a horizontal axis.** Its arrows circle the vertical pipe.
- **Forgetting that parallel $z_0 \parallel z_1$ still needs $a_1 = 0.15$.**

## Q5 — four-variable mobile-platform arm (tutor p. 17–24)

**(i) Tool-configuration vector and Jacobian.** The vector is
$w = (p,\; e^{q_4/\pi} r^3)$, where $r^3$ is the third column of $R$ (the approach vector):

$$
w=\begin{bmatrix}S_1q_2+0.25S_1C_3\\ C_1q_2+0.25C_1C_3\\ -0.25S_3+0.25\\ -e^{q_4/\pi}S_1C_3\\ e^{q_4/\pi}C_1C_3\\ -e^{q_4/\pi}S_3\end{bmatrix},
\qquad
V(q)=\frac{\partial w}{\partial q}=
\begin{bmatrix}
C_1q_2+0.25C_1C_3 & S_1 & -0.25S_1S_3 & 0\\
-S_1q_2-0.25S_1C_3 & C_1 & -0.25C_1S_3 & 0\\
0&0&-0.25C_3&0\\
-e^{q_4/\pi}C_1C_3 & 0 & e^{q_4/\pi}S_1S_3 & -e^{q_4/\pi}S_1C_3/\pi\\
-e^{q_4/\pi}S_1C_3 & 0 & -e^{q_4/\pi}C_1S_3 & e^{q_4/\pi}C_1C_3/\pi\\
0&0&-e^{q_4/\pi}C_3 & -e^{q_4/\pi}S_3/\pi
\end{bmatrix}
$$

This is a 6×4 matrix. The tutor's p. 20–21 Jacobian matches it, and the checker confirms it against
finite differences.

**(ii) Inverse kinematics.**

- From $z = 0$: $0.25(1 − S_3) = 0$, so $S_3 = 1$ and $q_3 = \pi/2$. This is unique on $(−\pi, \pi]$.
- Then $C_3 = 0$, so $x = S_1q_2$ and $y = C_1q_2$.
- This gives $q_1 = \operatorname{atan2}(x, y) = \pi/4$ and $q_2 = \sqrt{x^2 + y^2} = 0.2\sqrt2 = \sqrt2/5 \approx 0.283$.

A second branch is $q_1 = −3\pi/4$ with $q_2 = −\sqrt2/5$. It is valid only if the prismatic $q_2$
may be negative, which a real slide usually does not allow.

**(iii) Approach vector.** $r^3 = (−S_1C_3,\; C_1C_3,\; −S_3) = (0, 0, −1)$. The tool points
straight down on both branches.

**Rubric (practice weights; the source marks are not shown).**

- (i): 4 marks: 1 for $w$, 3 for the columns.
- (ii): 4 marks: $q_3$ (1), the collapse to $x = S_1q_2$ and $y = C_1q_2$ (1), $q_1$ (1), $q_2$ (1).
- (iii): 2 marks.

**Common wrong paths.**

- **$q_1 = \operatorname{atan2}(y, x)$.** Here $x = S_1(\cdot)$, so the correct form is
  $\operatorname{atan2}(x, y)$. It happens to give the same π/4 only because x = y, which is a
  trap on any other numbers.
- **Building $w_{4..6}$ from the first column of $R$ instead of the third.**
- **Dropping the $1/\pi$ in column 4.**

## Q6 — spherical RRP arm (tutor p. 25–26, "22-23 S2 Q3(b)")

**(i) Analytic IK.** Set $\rho = q_3 + 0.1 \ge 0$, so that $p = \rho\,(C_1S_2,\; S_1S_2,\; C_2)$.

$$
q_1=\operatorname{atan2}(y,x),\qquad q_2=\operatorname{atan2}\!\big(\sqrt{x^2+y^2},\,z\big),\qquad q_3=\sqrt{x^2+y^2+z^2}-0.1
$$

A second branch is $(q_1 + \pi,\; −q_2,\; q_3)$.

**(ii) Numbers for (0.15, 0.25, 0.025):**

- $q_1 = 59.04°$ (1.030 rad).
- $q_2 = 85.10°$ (1.485 rad).
- $q_3 = \sqrt{0.085625} − 0.1 = 0.1926$ units.
- Alternate branch: $q_1 = −120.96°$ and $q_2 = −85.10°$.

**Problems with the task.** This is supplementary reasoning; the tutor slides give no answer.

- **Radial approach only.** The approach vector $r^3 = (C_1S_2, S_1S_2, C_2)$ is the unit vector
  from the base origin to the tip. The gripper always points straight out from the base, so it
  cannot come down onto the object from above.
- **Near-horizontal reach at low height.** With $C_2 = 0.085$, the tool arrives almost sideways at
  z = 0.025. The fingers and link travel close to the supporting surface, which risks collision.
  Putting the tool tip exactly at the centroid also needs jaw clearance.
- **No orientation freedom.** With 3 DOF, the position fixes all the joints. The jaw roll and the
  approach direction cannot be chosen to match the object's grasp faces.
- **Mobile base.** The target must be known in the arm's base frame. Any error in localising the
  mobile robot goes straight into tip error.
- **Limits and branches.** Check the stroke of $q_3$ and the limit of $q_2$ near 90°, and choose one
  of the two branches.

**Rubric (practice weights).**

- (i): 4 marks: $q_1$ (1), $q_2$ with quadrant-safe atan2 (1.5), $q_3$ (1.5).
- (ii): 6 marks: numbers (3), discussion (3, any three valid points).

**Common wrong paths.**

- **Using $q_2 = \arccos(z)$ without dividing by $\rho$.**
- **$q_3 = \rho$, forgetting the 0.1 offset.**
- **$q_1 = \arctan(y/x)$, losing the quadrant.**
