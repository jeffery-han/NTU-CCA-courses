# EE6221 Quiz 1 — Mock 2: answer key, rubric, and diagnosis guide

**Companion exam page:** `quiz-01-mock-02.html` (answer-free — sit it before reading this file).
**Intel basis:** `quiz-01-intel.md`. **Mock 1 and its marked attempt:** `quiz-01-mock-01.md`,
`quiz-01-mock-01-attempt-2026-09-17-marked.md`.
**Conventions:** Schilling standard D–H, matching `notes/notes.tex`,
`resources/additional-materials/review-week-02-dh-algorithm-summary.pdf`, and
`resources/additional-materials/review-week-03-tool-configuration-vector.pdf`.

Link transform template (fill order $\theta,d,a,\alpha$; operations
Rot$(z,\theta)\to$Trans$(z,d)\to$Trans$(x,a)\to$Rot$(x,\alpha)$):
$$
{}^{k-1}T_k=\begin{bmatrix}
c_k & -s_k c_{\alpha k} & s_k s_{\alpha k} & a_k c_k\\
s_k & c_k c_{\alpha k} & -c_k s_{\alpha k} & a_k s_k\\
0 & s_{\alpha k} & c_{\alpha k} & d_k\\
0 & 0 & 0 & 1
\end{bmatrix}
$$

**Total: 20 core marks + 5 predicted = 25.** Same allocation as Mock 1 (Q1 = 12, Q2 = 8, Section
C = 5), because the format evidence for that shape is the high-confidence part of the intel.

## How this paper was chosen (and what it is *not*)

Mock 2 covers the same syllabus as Mock 1 from a different angle. The changes are architectural,
not remedial:

| | Mock 1 | Mock 2 | Why |
|---|---|---|---|
| Q1 arm | cylindrical **RPP** | articulated **RRR** | Both are named architectures in `notes/notes.tex`; RRR is the one the lecture's own five-axis worked example is built on, and it puts the twist at $\alpha_1$ instead of $\alpha_2$ so the table cannot be pattern-matched. |
| Q1 tool | along $z_3$ | along $x_3$ | Consequence of the geometry, not a trap: in an articulated arm the links run along $x$, so the tool offset does too. |
| Q1(d) | symbolic | symbolic **+ numeric evaluation** | The recalled papers are symbolic, but a numeric check is the only way to catch a sign error, and $\theta_2+\theta_3=90^\circ$ makes it hand-computable. |
| Q2 orientation | both long axes $\parallel x_0$; place reuses pick $R$ | long axes **perpendicular**; place needs a real $90^\circ$ rotation | Copying $R$ from pick to place earns a mark in Mock 1. Here it cannot. |
| Section C | tool-configuration vector + **unique-solution** IK | **multi-branch** IK + **cubic trajectory** | Cubic interpolation is in scope and was untested by Mock 1. Across the two mocks the predicted set is now fully covered. |

Deliberately *not* included: the tool-configuration vector (examined in Mock 1, and now written into
`notes/beginner-notes.tex`), and the Jacobian (out of scope — see `STATUS.md`).

---

## Question 1 — D–H modelling of an articulated robot (12 marks)

### Setup given to the student

Articulated RRR arm: joint 1 revolute about the vertical column ($\theta_1$); joint 2 revolute
(shoulder), horizontal axis intersecting the column at height $d_1$; joint 3 revolute (elbow),
horizontal axis parallel to the shoulder's, a distance $a_2$ along link 2. Link 3 spans $a_3$ to the
wrist, then a rigid tool of length $L_t$ continues in the same direction.

Numeric values for part (d): $d_1=4$, $a_2=3$, $a_3=2$, $L_t=1$, $(\theta_1,\theta_2,\theta_3)=
(90^\circ,30^\circ,60^\circ)$.

### (a) Frame assignment — 4 marks

One valid assignment (frame 0 at the base, $z_0$ up the column, $x_0$ a fixed horizontal reference):

| Frame | origin | $z$ axis | $x$ axis |
|---|---|---|---|
| 0 | base, on the column axis | up the column (waist axis) | fixed horizontal reference |
| 1 | on the column axis at height $d_1$ (the shoulder) | **horizontal**, along the shoulder axis | common normal of $z_0,z_1$ — horizontal, perpendicular to $z_1$ |
| 2 | shoulder | along $z_1$ (elbow axis $\parallel$ shoulder axis) | along link 2, from shoulder toward elbow |
| 3 | wrist point | along $z_2$ | along link 3, from elbow toward wrist |

Mark scheme:
- 1 — $z_0$ vertical along the waist axis; origin of frame 1 lifted to the shoulder so that
  $d_1$ is the offset **along $z_0$**.
- 1 — $z_1$ **horizontal** (shoulder axis), i.e. the $z_0\to z_1$ change identified as a
  $\pm90^\circ$ twist; $z_2\parallel z_1$ (elbow axis parallel), so $\alpha_2=0$.
- 1 — every $x_k$ along the common normal / $z_{k-1}\times z_k$: in particular $x_2$ **along link 2**
  and $x_3$ **along link 3**, which is what makes $a_2,a_3$ the link lengths. Right-handed
  $y_k=z_k\times x_k$ shown or implied.
- 1 — all three joints identified as revolute with $\theta_k$ starred; origins on the correct axes
  (frame 1 and 2 origins coincide at the shoulder, since the shoulder axis intersects the column:
  $a_1=0$).

*Non-uniqueness:* $\alpha_1=-90^\circ$, a different $x_0$, or putting $d_1$ in row 1 vs. a fixed
base offset are all acceptable. Mark against the student's own diagram; the invariants are in (d).

### (b) D–H parameter table — 3 marks

With $\alpha_1=+90^\circ$ and the tool folded into link 3 ($L_3 \equiv a_3+L_t$):

| $k$ | $\theta_k$ | $d_k$ | $a_k$ | $\alpha_k$ | variable |
|---|---|---|---|---|---|
| 1 | $\theta_1^\ast$ | $d_1$ | $0$ | $+90^\circ$ | $\theta_1$ (revolute) |
| 2 | $\theta_2^\ast$ | $0$ | $a_2$ | $0$ | $\theta_2$ (revolute) |
| 3 | $\theta_3^\ast$ | $0$ | $a_3$ | $0$ | $\theta_3$ (revolute) |

- 1 — row 1: $\theta_1$ variable, $d_1$ present, $a_1=0$ (axes intersect), and
  $\alpha_1=\pm90^\circ$. **The twist in row 1 is the crux of this question** — a table with
  $\alpha_1=0$ gets 0 for this row, because then the whole arm stays in a horizontal plane.
- 1 — row 2: $\theta_2$ variable, $a_2$ = link-2 length, $d_2=0$, $\alpha_2=0$ (parallel axes).
- 1 — row 3: $\theta_3$ variable, $a_3$ = link-3 length, $d_3=0$, $\alpha_3=0$; all three variables
  starred.

**Three joints $\Rightarrow$ three rows, and all three variables are $\theta$'s.** The tool is
handled as a post-multiplied $\mathrm{Trans}(x,L_t)$ or by writing $a_3+L_t$ in row 3 — stating
which. Accept either; a *fourth row* for the tool is acceptable **only** if it is explicitly marked
fixed (no starred variable) and the three joint rows are all still present.

### (c) Link transforms — 3 marks

$$
{}^{0}T_1=\begin{bmatrix}c_1&0&s_1&0\\ s_1&0&-c_1&0\\ 0&1&0&d_1\\ 0&0&0&1\end{bmatrix},\quad
{}^{1}T_2=\begin{bmatrix}c_2&-s_2&0&a_2c_2\\ s_2&c_2&0&a_2s_2\\ 0&0&1&0\\ 0&0&0&1\end{bmatrix},\quad
{}^{2}T_3=\begin{bmatrix}c_3&-s_3&0&a_3c_3\\ s_3&c_3&0&a_3s_3\\ 0&0&1&0\\ 0&0&0&1\end{bmatrix}
$$

1 mark each.
- ${}^{0}T_1$: with $\theta_1$ free, $d_1$ along $z_0$, $a_1=0$, $\alpha_1=+90^\circ$
  ($c_\alpha=0,\ s_\alpha=1$). Note the translation column is $(0,0,d_1)$ — $d_1$ sits in the
  **third** slot because $\mathrm{Trans}(z,d)$ always does. The rotation block's third column is
  $(s_1,-c_1,0)$; a sign flip there costs the mark.
- ${}^{1}T_2$, ${}^{2}T_3$: the standard planar form, $\alpha=0$ so the third row/column is
  $(0,0,1)$. Award the mark for either $a_3$ or $a_3+L_t$ in ${}^{2}T_3$ provided the tool is
  accounted for exactly once overall.

### (d) Arm matrix, numeric evaluation, check — 2 marks

Writing $L_3=a_3+L_t$, $c_{23}=\cos(\theta_2+\theta_3)$, $s_{23}=\sin(\theta_2+\theta_3)$:

$$
{}^{0}T_{\text{tool}}=\begin{bmatrix}
c_1c_{23} & -c_1s_{23} & s_1 & c_1\,(a_2c_2+L_3c_{23})\\
s_1c_{23} & -s_1s_{23} & -c_1 & s_1\,(a_2c_2+L_3c_{23})\\
s_{23} & c_{23} & 0 & d_1+a_2s_2+L_3s_{23}\\
0&0&0&1
\end{bmatrix}
$$

This is the classic articulated-arm result: the **radial** reach is $r=a_2c_2+L_3c_{23}$, the
**height** is $z=d_1+a_2s_2+L_3s_{23}$, and $\theta_1$ simply swings $(r,z)$ around the column —
hence the $c_1,s_1$ factors on $x$ and $y$.

Numerically, $L_3=2+1=3$; $\theta_2+\theta_3=90^\circ$ so $c_{23}=0,\ s_{23}=1$; $\theta_1=90^\circ$
so $c_1=0,\ s_1=1$; $c_2=\sqrt3/2,\ s_2=1/2$:

$$
r=3\cdot\tfrac{\sqrt3}{2}+3\cdot 0=\tfrac{3\sqrt3}{2},\qquad
z=4+3\cdot\tfrac12+3\cdot 1=\tfrac{17}{2},
$$
$$
{}^{0}T_{\text{tool}}=\begin{bmatrix}
0&0&1&0\\ 0&-1&0&\tfrac{3\sqrt3}{2}\\ 1&0&0&\tfrac{17}{2}\\ 0&0&0&1
\end{bmatrix},\qquad
p=\Big(0,\ \tfrac{3\sqrt3}{2},\ \tfrac{17}{2}\Big).
$$

- 1 — correct symbolic product **or** correct numeric matrix with $p$ and $R$ identified.
- 1 — the orthonormality check: columns $(0,0,1),(0,-1,0),(1,0,0)$ are mutually orthogonal unit
  vectors, $R^{\mathsf T}R=I$, and $\det R=+1$ (not $-1$ — check the handedness, not just the norms).
  Physical sanity: $\sqrt{x^2+y^2}=3\sqrt3/2=r$ ✓ and $z=17/2$ ✓.

*Verification used to build this key:* the closed form above was checked against the numeric product
of the three link matrices at 2000 random $(\theta_1,\theta_2,\theta_3)$ — exact agreement in both
$R$ and $p$.

### Q1 — common wrong paths and what each implies

| Observed | Diagnosis | Fix |
|---|---|---|
| $\alpha_1=0$ | Did not see that the shoulder axis is perpendicular to the waist axis; the arm can then only move in a horizontal plane | Draw $z_0$ and $z_1$ first, *then* read $\alpha_1$ as the angle from $z_0$ to $z_1$ about $x_1$ |
| $\alpha_2=\pm90^\circ$ | Assumed every row needs a twist | Parallel axes $\Rightarrow \alpha=0$. Shoulder and elbow are parallel, so rows 2 and 3 are the planar case |
| $a_2$ or $a_3$ placed in $d_k$ | Confused "along $x_k$" with "along $z_{k-1}$" | Link lengths live in $a$ when $x_k$ runs along the link; $d$ is the offset along the *previous* $z$ |
| Tool added along $z_3$ | Imported Mock 1's geometry, where the tool did run along $z$ | The tool continues **link 3**, and $x_3$ is along link 3, so it is $\mathrm{Trans}(x,L_t)$ here. The direction follows from the frame, never from memory |
| Four rows, one of them the tool with a starred variable | Row-per-offset instead of row-per-joint | A rigid tool has no DOF; three joints means three starred variables |
| $\det R=-1$ accepted | Checked norms but not handedness | $R^{\mathsf T}R=I$ admits reflections; also check $\det=+1$ |
| Reversed product ${}^{2}T_3\,{}^{1}T_2\,{}^{0}T_1$ | Order rule not internalised | Base-to-tool = left-to-right |

*Confidence:* **derivable.** Frame choice is non-unique; the invariants to mark against are
$r=a_2c_2+L_3c_{23}$, $z=d_1+a_2s_2+L_3s_{23}$, and the numeric $p$ above.

---

## Question 2 — pick-and-place arm matrix (8 marks)

### Setup given to the student

Top view, base frame $\{0\}$, $z_0$ up, centimetres. Both blocks rest flat.

- **Part E**: centroid ${}^{0}p_E=[8,3,1]^{\mathsf T}$; long side $6$ **along $y_0$**, short side $3$
  along $x_0$, height $2$.
- **Part F**: centroid ${}^{0}p_F=[3,8,2]^{\mathsf T}$; long side $6$ **along $x_0$**, short side $3$
  along $y_0$, height $4$.

Tool frame: $R=[\,r_1\ r_2\ r_3\,]$ = [normal, sliding, approach].

### (a) Pick pose — 4 marks

- Approach from above: $r_3=-z_0=[0,0,-1]^{\mathsf T}$. — 1
- E's long axis is along $y_0$, so its two long faces are separated **along $x_0$**; the jaws close
  along $x_0$: $r_2=[1,0,0]^{\mathsf T}$. — 1
- $r_1=r_2\times r_3=[1,0,0]\times[0,0,-1]=[0,1,0]^{\mathsf T}$; handedness check
  $r_1\times r_2=[0,1,0]\times[1,0,0]=[0,0,-1]=r_3$ ✓. — 1
- Translation column = E's centroid $[8,3,1]^{\mathsf T}$. — 1

$$
{}^{0}T_{\text{pick}}=\begin{bmatrix}
0&1&0&8\\ 1&0&0&3\\ 0&0&-1&1\\ 0&0&0&1
\end{bmatrix},\qquad \det R=+1\ \checkmark
$$

> **Grader's note — read this before marking.** This $R$ is *numerically identical* to the one the
> learner wrote for Mock 1 Q2(a), where it was **wrong**. It is **right here**, because part E's long
> axis is along $y_0$ whereas part C's was along $x_0$. Do not mark it wrong out of consistency with
> the previous paper, and do not credit it as "learned" without checking the reasoning: the whole
> point is that $r_2$ is *derived from the part's orientation* every time, not remembered. If the
> script shows the derivation ("long axis $\parallel y_0$ $\Rightarrow$ long faces split along $x_0$
> $\Rightarrow$ jaws close along $x_0$"), award it fully and say why it was right this time.

### (b) Place pose — 3 marks

Part E must end up on top of F with the long axes aligned. F's long axis is along $x_0$ and E's is
currently along $y_0$, so **the part turns $90^\circ$ about $z_0$** — and the gripper turns with it.
The jaws still grip the same two long faces, which after the turn are separated along $y_0$:

- $r_2=[0,1,0]^{\mathsf T}$, $r_3=[0,0,-1]^{\mathsf T}$ unchanged (still descending), and
  $r_1=r_2\times r_3=[0,1,0]\times[0,0,-1]=[-1,0,0]^{\mathsf T}$. Equivalently
  $R_{\text{place}}=R_z(90^\circ)\,R_{\text{pick}}$. — 1
- $x,y$ of the translation = F's centroid $x,y=(3,8)$. — 1
- $z$: F's top surface is at (F centroid $z$) + (F half-height) $=2+2=4$; E's centroid then sits its
  own half-height above that, $+1$, so $z=5$. **Both half-heights**, and note F's half-height is $2$
  here, not $1$ — the two blocks have different heights on purpose. — 1

$$
{}^{0}T_{\text{place}}=\begin{bmatrix}
-1&0&0&3\\ 0&1&0&8\\ 0&0&-1&5\\ 0&0&0&1
\end{bmatrix}
$$

### (c) Checks and the connecting rotation — 1 mark

States $R^{\mathsf T}R=I$ and $\det R=+1$ for both matrices, **and** identifies the pick-to-place
rotation as $R_z(+90^\circ)$ (or $-90^\circ$ with a consistently mirrored $r_2$; either sign is
acceptable if the jaws still straddle E's long faces and the part's long axis ends up along $x_0$).

Verified: $R_z(90^\circ)\,R_{\text{pick}}=R_{\text{place}}$ exactly.

### Q2 — common wrong paths and what each implies

| Observed | Diagnosis | Fix |
|---|---|---|
| $r_2=[0,1,0]$ in part (a) | Applied Mock 1's *answer* rather than Mock 1's *method* | Re-read the part's orientation each time: E's long axis is along $y_0$, so the jaws close along $x_0$ |
| $R_{\text{place}}=R_{\text{pick}}$ | Copied the pick orientation, as Mock 1 allowed | The long axes here are perpendicular, so aligning them *requires* a $90^\circ$ turn about $z_0$ |
| $(3,3)$ entry $=+1$ | Approach taken as "toward $+z$" instead of "toward the part" | $r_3$ points from the tool into the workpiece — downward |
| Place $z=4$ | Stopped at F's top surface and forgot E's own half-height | $z=z_F+\tfrac12 h_F+\tfrac12 h_E=2+2+1=5$ |
| Place $z=3$ | Used $\tfrac12 h_F=1$, i.e. read F's height as $2$ (Mock 1's value) | F's height is $4$ on this paper. Re-read the table |
| Place translation $=[8,3,\cdot]$ | Used E's current centroid rather than its destination | The part is *moving* to F |
| $\det R=-1$ | Guessed a column instead of using the cross product | $r_1=r_2\times r_3$, computed |

*Confidence:* **derivable**, given the stated tool-frame convention. A different but self-consistent
gripper convention should be marked against the student's stated convention.

---

## Section C — PREDICTED extension (5 marks)

### C1 — inverse kinematics of the Q1 arm, position only — 3 marks

**General solution.** With $L_3=a_3+L_t$ and target $(x,y,z)$:

$$
\theta_1=\operatorname{atan2}(y,x),\qquad r=\sqrt{x^2+y^2},\qquad s=z-d_1 .
$$

$\theta_1$ swings the arm into the vertical plane containing the target; inside that plane the
problem is a **planar 2R chain** with links $a_2$ and $L_3$ reaching the point $(r,s)$:

$$
r=a_2c_2+L_3c_{23},\qquad s=a_2s_2+L_3s_{23}.
$$

Squaring and adding kills $\theta_2$ and leaves the law of cosines:
$$
\cos\theta_3=\frac{r^2+s^2-a_2^2-L_3^2}{2\,a_2L_3}\equiv D,
\qquad
\theta_3=\operatorname{atan2}\!\big(\pm\sqrt{1-D^2},\ D\big),
$$
$$
\theta_2=\operatorname{atan2}(s,r)-\operatorname{atan2}\!\big(L_3\sin\theta_3,\ a_2+L_3\cos\theta_3\big).
$$

- 1 — reduces to the planar 2R sub-problem: $\theta_1$ by atan2, then $r,s$ with $s=z-d_1$ (the
  shoulder height **must** be subtracted before the 2R geometry is applied).
- 1 — $\cos\theta_3$ by the law of cosines and **two branches** $\theta_3=\pm|\theta_3|$
  (elbow-down / elbow-up), with $\theta_2$ following from the atan2 difference. The arm has a genuine
  2R sub-chain (shoulder + elbow, parallel axes), so **two** position solutions exist for a
  reachable interior target — unlike the Mock 1 cylindrical arm, which had exactly one.
- 1 — reachability: $|a_2-L_3|\le\sqrt{r^2+s^2}\le a_2+L_3$, plus $|D|\le 1$ as the algebraic form of
  the same statement. (A second family exists from $\theta_1\to\theta_1+180^\circ$ with the arm
  reaching backwards; mention it for credit, do not require it.)

**Numeric case.** $a_2=3$, $L_3=3$, $d_1=4$, target $\big(0,\ \tfrac{3\sqrt3}{2},\ \tfrac{17}{2}\big)$:

$$
\theta_1=\operatorname{atan2}\!\Big(\tfrac{3\sqrt3}{2},0\Big)=90^\circ,\qquad
r=\tfrac{3\sqrt3}{2},\qquad s=\tfrac{17}{2}-4=\tfrac92 ,
$$
$$
r^2+s^2=\tfrac{27}{4}+\tfrac{81}{4}=27,\qquad
D=\frac{27-9-9}{2\cdot3\cdot3}=\frac{9}{18}=\frac12
\;\Longrightarrow\;\theta_3=\pm60^\circ .
$$

Then $\operatorname{atan2}(s,r)=\operatorname{atan2}\big(\tfrac92,\tfrac{3\sqrt3}{2}\big)=60^\circ$
(since $\tan=\tfrac{9/2}{3\sqrt3/2}=\tfrac{3}{\sqrt3}=\sqrt3$), and:

| branch | $\theta_1$ | $\theta_2$ | $\theta_3$ |
|---|---|---|---|
| elbow-down | $90^\circ$ | $60^\circ-30^\circ=30^\circ$ | $+60^\circ$ |
| elbow-up | $90^\circ$ | $60^\circ-(-30^\circ)=90^\circ$ | $-60^\circ$ |

because $\operatorname{atan2}(3\sin(\pm60^\circ),\,3+3\cos(\pm60^\circ))
=\operatorname{atan2}(\pm\tfrac{3\sqrt3}{2},\tfrac92)=\pm30^\circ$.

The first branch recovers the Q1 configuration $(90^\circ,30^\circ,60^\circ)$ — that is the built-in
consistency check. Both branches were forward-substituted into the Q1 arm matrix and reproduce the
target exactly. Equal effective links ($a_2=L_3=3$) make every intermediate angle exact here, and
also collapse the inner reach bound to $|a_2-L_3|=0$: this arm can fold right back to the shoulder,
so it has no inner dead zone. Students should still state the general bound.

### C2 — cubic trajectory segment — 2 marks

With $q(t)=at^3+bt^2+ct+d$, endpoints $q(0)=q_0$, $q(T)=q_1$, $\dot q(0)=\dot q(T)=0$, and
$\Delta=q_1-q_0$:
$$
d=q_0,\qquad c=0,\qquad b=\frac{3\Delta}{T^2},\qquad a=-\frac{2\Delta}{T^3}.
$$

For $q_0=20^\circ$, $q_1=80^\circ$, $T=3\,$s $\Rightarrow \Delta=60^\circ$:
$$
d=20^\circ,\quad c=0,\quad b=\frac{180}{9}=20\ \mathrm{deg/s^2},\quad
a=-\frac{120}{27}=-\frac{40}{9}\approx-4.44\ \mathrm{deg/s^3}.
$$

- 1 — all four coefficients, with $c=0$ justified by $\dot q(0)=0$ and $d=q_0$ by $q(0)=q_0$.
- 1 — $q(T/2)=q(1.5)=20+20(2.25)-\tfrac{40}{9}(3.375)=20+45-15=50^\circ$, i.e. exactly the
  **midpoint** $q_0+\Delta/2$ — a property of the zero-endpoint-velocity cubic, and a free check.
  Maximum rate at $t=T/2$: $\dot q_{\max}=\dfrac{3\Delta}{2T}=\dfrac{180}{6}=30\ \mathrm{deg/s}$
  (from $\dot q=2bt+3at^2=40t-\tfrac{40}{3}t^2$, giving $60-30=30$ at $t=1.5$).

Sanity checks used on this key: $q(0)=20$, $q(3)=80$, $\dot q(0)=\dot q(3)=0$, $q(1.5)=50$,
$\dot q(1.5)=30$ — all exact.

### Section C — common wrong paths

| Observed | Diagnosis |
|---|---|
| Only one $\theta_3$ reported | Missed that $\cos\theta_3=D$ has two solutions $\pm$; a 2R sub-chain always gives elbow-up/elbow-down for an interior target |
| $s=z$ instead of $z-d_1$ | Forgot to drop to the shoulder before applying the planar geometry — every later angle is then wrong |
| $\theta_2=\operatorname{atan2}(s,r)$ alone | Forgot the second term: $\operatorname{atan2}(s,r)$ points at the *target*, not along *link 2* |
| $\theta_3=\arccos D$ only | Loses the sign branch; also blows up numerically near $|D|=1$ — prefer $\operatorname{atan2}(\pm\sqrt{1-D^2},D)$ |
| No reachability statement | IK without a workspace check |
| Cubic with $c\neq0$ | Did not impose $\dot q(0)=0$ |
| $q(T/2)\neq$ midpoint | Arithmetic slip — the zero-endpoint-velocity cubic *always* passes through the midpoint at $T/2$, so this is a free self-check |
| Max rate taken at $t=0$ or $t=T$ | Rate is zero at both ends by construction; the extremum is at $t=T/2$ |

*Confidence:* **derivable** throughout. C1's branch count is derivable from the geometry, not a
convention question.

---

## Marking summary

| Part | Marks | Confidence |
|---|---:|---|
| Q1(a) frame assignment | 4 | derivable (mark vs. own diagram) |
| Q1(b) D–H table | 3 | derivable |
| Q1(c) link transforms | 3 | derivable |
| Q1(d) arm matrix + numeric + check | 2 | derivable |
| Q2(a) pick pose | 4 | derivable (given convention) |
| Q2(b) place pose | 3 | derivable |
| Q2(c) checks + connecting rotation | 1 | derivable |
| **Core total** | **20** | |
| C1 multi-branch inverse kinematics | 3 | derivable — *predicted topic* |
| C2 cubic trajectory segment | 2 | derivable — *predicted topic* |
| **Grand total** | **25** | |

**Grading protocol:** mark part by part against the checkpoints above. Separate arithmetic slips
(award method marks, name the checkpoint that earned them) from inverted concepts — on this paper the
diagnostic ones are the row-1 twist $\alpha_1$, the tool direction following $x_3$ rather than $z_3$,
$r_2$ derived from *this* part's orientation, the $90^\circ$ place rotation, and the two elbow
branches. An unattempted part is **blank, not wrong**. After grading, fold every non-slip error into
`notes/beginner-notes.tex` / `notes/notes.tex` and log it in `STATUS.md` (loop stage 6).
