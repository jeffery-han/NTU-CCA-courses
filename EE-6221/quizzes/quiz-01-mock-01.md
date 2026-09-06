# EE6221 Quiz 1 — Mock 1: answer key, rubric, and diagnosis guide

**Companion exam page:** `quiz-01-mock-01.html` (answer-free — sit it before reading this file).
**Intel basis:** `quiz-01-intel.md`.
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

Paper shape mirrors the recalled real quiz: **2 core questions, ~30 min, closed book, handwritten.**
Section C is a **prediction** (in stated scope, absent from every recalled paper) — labelled as such
on the exam page.

**Total: 20 core marks + 5 predicted = 25.**

---

## Question 1 — D–H modelling of a cylindrical robot (12 marks)

### Setup given to the student

A cylindrical-configuration robot (see the figure on the exam page):

- **Joint 1** — revolute: rotates the arm about the fixed vertical column axis; angle $\theta_1$.
- **Joint 2** — prismatic: a carriage slides vertically along the column; displacement $d_2$.
- **Joint 3** — prismatic: the horizontal arm telescopes radially outward; displacement $d_3$.
- A rigid tool of length $L_t$ is fixed to the end of link 3, pointing along the extension direction.

Tasks: (a) assign link frames and draw the link-coordinate diagram; (b) tabulate the four D–H
parameters for every joint; (c) write the three link transforms; (d) form the arm matrix
${}^{0}T_{\text{tool}}$ to the tool tip, read off $R$ and $p$, and verify $R$ is orthonormal.

### (a) Frame assignment — 4 marks

One valid assignment (frame 0 at the column base, $z_0$ up along the column, $x_0$ a fixed
horizontal reference):

| Frame | origin | $z$ axis | $x$ axis |
|---|---|---|---|
| 0 | column base | up the column | fixed horizontal reference |
| 1 | on $z_0$, at joint 1 | along $z_0$ (revolute axis) | $x_0$ rotated by $\theta_1$ |
| 2 | carriage | **horizontal**, along the arm's radial direction | vertical, $= z_1$ direction after the $-90^\circ$ twist |
| 3 | end of the telescoping section | along $z_2$ (radial slide axis) | $= x_2$ |

Mark scheme:
- 1 — $z_0,z_1$ vertical along the column; $z_1\parallel z_0$.
- 1 — $z_2$ (and $z_3$) horizontal along the radial reach; the $z_1\to z_2$ change of direction
  identified as a $\pm90^\circ$ twist.
- 1 — every $x_k$ along the common normal / $z_{k-1}\times z_k$; right-handed $y_k=z_k\times x_k$
  shown or implied.
- 1 — variable joints correctly identified (1 revolute, 2 prismatic) and origins on the correct
  axes.

*Non-uniqueness:* choosing $\alpha_2=+90^\circ$ instead of $-90^\circ$, or a different $x_0$, is
equally correct. Award full marks for any internally consistent assignment whose part-(d) tool
position has radial distance $d_3+L_t$ and height $d_2$.

### (b) D–H parameter table — 3 marks

With $\alpha_2=-90^\circ$:

| $k$ | $\theta_k$ | $d_k$ | $a_k$ | $\alpha_k$ | variable |
|---|---|---|---|---|---|
| 1 | $\theta_1^\ast$ | $0$ | $0$ | $0$ | $\theta_1$ (revolute) |
| 2 | $0$ | $d_2^\ast$ | $0$ | $-90^\circ$ | $d_2$ (prismatic) |
| 3 | $0$ | $d_3^\ast$ | $0$ | $0$ | $d_3$ (prismatic) |

- 1 — row 1 (only $\theta_1$ variable; $d_1=a_1=\alpha_1=0$).
- 1 — row 2 ($\theta_2=0$ constant, $d_2$ variable, $\alpha_2=\pm90^\circ$). **The twist here is the
  crux of the question** — a table with $\alpha_2=0$ gets 0 for this row.
- 1 — row 3 (all zero except $d_3$ variable); variables circled/starred.

If the student's frame choice legitimately places the twist at $\alpha_1$ or splits it, mark their
table against their own diagram.

### (c) Link transforms — 3 marks

$$
{}^{0}T_1=\begin{bmatrix}c_1&-s_1&0&0\\ s_1&c_1&0&0\\ 0&0&1&0\\ 0&0&0&1\end{bmatrix},\quad
{}^{1}T_2=\begin{bmatrix}1&0&0&0\\ 0&0&1&0\\ 0&-1&0&d_2\\ 0&0&0&1\end{bmatrix},\quad
{}^{2}T_3=\begin{bmatrix}1&0&0&0\\ 0&1&0&0\\ 0&0&1&d_3\\ 0&0&0&1\end{bmatrix}
$$

1 mark each. For ${}^{1}T_2$: with $\theta_2=0,\ \alpha_2=-90^\circ$ the template gives
$c_{\alpha}=0,\ s_{\alpha}=-1$, so column 2 $=(0,0,-1)$ wait — check entries:
row 2 col 3 is $-c_2 s_{\alpha 2}=-(1)(-1)=+1$; row 3 col 2 is $s_{\alpha 2}=-1$. A sign flip in
${}^{1}T_2$'s rotation block costs the mark.

### (d) Arm matrix, read-off, check — 2 marks

$$
{}^{0}T_{\text{tool}}
={}^{0}T_1\,{}^{1}T_2\,{}^{2}T_3\cdot\mathrm{Trans}(z,L_t)
=\begin{bmatrix}
c_1 & 0 & -s_1 & -(d_3+L_t)s_1\\
s_1 & 0 & c_1 & (d_3+L_t)c_1\\
0 & -1 & 0 & d_2\\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- 1 — correct product; $p=\big(-(d_3+L_t)s_1,\ (d_3+L_t)c_1,\ d_2\big)$,
  $R=\big[\,(c_1,s_1,0)\ \ (0,0,-1)\ \ (-s_1,c_1,0)\,\big]$.
- 1 — states $R$ is the orientation block / $p$ the position, and checks
  $R^{\mathsf T}R=I$, $\det R=+1$ (columns orthonormal). Physical sanity: radial distance
  $\sqrt{x^2+y^2}=d_3+L_t$, height $z=d_2$ — a cylinder, as the name promises.

*Equally correct:* a frame choice with $\alpha_2=+90^\circ$ or a different $x_0$ gives e.g.
$p=\big((d_3+L_t)c_1,\ (d_3+L_t)s_1,\ d_2\big)$ with the $R$ columns permuted/signed to match. Mark
against the student's own diagram; the invariants are radial distance $d_3+L_t$ and height $d_2$.

### Q1 — common wrong paths and what each implies

| Observed | Diagnosis | Fix |
|---|---|---|
| $\alpha_2=0$, whole arm stays "vertical" | Did not see that a prismatic joint's *direction* can differ from the previous $z$; treated D–H as "one row per link length" | Re-do the axis step first: draw $z_1$ and $z_2$, *then* read $\alpha$ as the angle between them about $x_2$ |
| Rotation block of ${}^{1}T_2$ has wrong signs | Template memorised with $+s_\alpha/-s_\alpha$ swapped | Re-derive ${}^{1}T_2$ from Rot$(z,0)$Trans$(z,d_2)$Trans$(x,0)$Rot$(x,-90^\circ)$ once, by hand |
| $d_2$ placed in the wrong column of $p$ | Confused "along $z_1$" (vertical) with "along $z_2$" (radial) | Track which frame each parameter lives in — $d_2$ is along $z_1$, before the twist |
| Multiplied ${}^{0}T_3={}^{2}T_3\,{}^{1}T_2\,{}^{0}T_1$ (reversed) | Order rule not internalised | Base-to-tool = left-to-right, ${}^{0}T_1$ first |
| No orthonormality check | Skipped verification | Cheap insurance — one line, catches most sign errors |
| Origins drifting off the joint axes; $y$ arrows reversed | (matches RedNote 新叶猫's own correction #ii) sloppy right-hand rule | $y_k=z_k\times x_k$, computed not guessed |

*Confidence:* **derivable.** The frame choice is non-unique but every valid choice yields the same
physical tool pose; mark against the student's own diagram.

---

## Question 2 — pick-and-place arm matrix (8 marks)

### Setup given to the student

Top view of a workstation, base frame $\{0\}$ with $z_0$ vertically up, all coordinates in cm.

- **Part C**: a rectangular block, centroid ${}^{0}p_C=[4,\ 8,\ 2]^{\mathsf T}$, resting flat on the
  table, its **long axis along $x_0$**, short axis along $y_0$, total height $4$.
- **Part D**: a rectangular block, centroid ${}^{0}p_D=[9,\ 3,\ 1]^{\mathsf T}$, long axis along
  $x_0$, total height $2$.

(a) Find ${}^{0}T_{\text{pick}}$ to pick part C from above by grasping its **long sides**.
(b) Find ${}^{0}T_{\text{place}}$ to set part C on top of part D with centroids and long axes aligned.

Tool frame convention (course): $R=[\,r_1\ r_2\ r_3\,]$ = [normal, sliding, approach];
$r_3$ points the way the tool advances toward the part, $r_2$ along the gripper's closing direction.

### (a) Pick pose — 4 marks

- Approach from above: $r_3=-z_0=[0,0,-1]^{\mathsf T}$. — 1
- Grasping the long sides ⇒ jaws close along the **short** axis: $r_2=[0,1,0]^{\mathsf T}$. — 1
- $r_1=r_2\times r_3=[0,1,0]\times[0,0,-1]=[-1,0,0]^{\mathsf T}$; right-handed check
  $r_1\times r_2=r_3$. — 1
- Translation column = part-C centroid $[4,8,2]^{\mathsf T}$. — 1

$$
{}^{0}T_{\text{pick}}=\begin{bmatrix}
-1&0&0&4\\ 0&1&0&8\\ 0&0&-1&2\\ 0&0&0&1
\end{bmatrix},\qquad \det R=(-1)(1)(-1)=+1\ \checkmark
$$

### (b) Place pose — 3 marks

- Same orientation as the pick (top-down approach, long axes still aligned): $R$ unchanged. — 1
- $x,y$ of the translation = part-D centroid $x,y$: $(9,\ 3)$. — 1
- $z$: D's top surface is at (D centroid $z$) + (D half-height) $= 1 + 1 = 2$; the place pose lifts
  C's centroid another (C half-height) $= 2$ above that, so $z = 2 + 2 = 4$. **Both half-heights
  must be added** — not left at D's centroid $z=1$, nor at D's top $z=2$. — 1

$$
{}^{0}T_{\text{place}}=\begin{bmatrix}
-1&0&0&9\\ 0&1&0&3\\ 0&0&-1&4\\ 0&0&0&1
\end{bmatrix}
$$

### Orthonormality / handedness check — 1 mark

Explicitly states $R^{\mathsf T}R=I$ and $\det R=+1$ for the final matrix (not a reflection).

### Q2 — common wrong paths and what each implies

| Observed | Diagnosis | Fix |
|---|---|---|
| $(3,3)$ entry is $+1$ (i.e. $r_3=+z_0$) | Approach direction taken as "toward $+z$" instead of "toward the part" | $r_3$ points *from the tool into the workpiece* — downward here |
| $R=\mathrm{diag\text{-}like}\ [1,0,0;0,1,0;0,0,-1]$, $\det R=-1$ | Wrote a reflection, not a rotation — never checked $\det$ | $r_1$ must be $r_2\times r_3$, computed; then $\det R=+1$ by construction (matches KuRRe8 p.4: "$R$ must be an orthogonal matrix") |
| $r_2=[1,0,0]$ | "Grasp the long sides" misread as "jaws along the long axis" | Jaws close *across* the sides they touch — perpendicular to the long sides = short axis |
| Place $z=1$ or $z=2$ | Forgot the stacked part's own half-height | Place height = (surface the part lands on) + (half the moving part) |
| Place translation $=[4,8,\cdot]$ | Used C's current centroid instead of the target | The part is *moving* to D's location |
| $r_1,r_2,r_3$ not mutually perpendicular | Guessed columns instead of using the cross product | Pick two axes from the physical task, get the third from $r_i\times r_j$ |

*Confidence:* **derivable**, given the stated tool-frame convention. If the student uses a different
but self-consistent gripper convention (e.g. $r_2$ as the approach), mark their matrix against their
stated convention — the course convention is normal/sliding/approach $= r_1/r_2/r_3$.

---

## Section C — PREDICTED extension (5 marks) — not from any recalled paper

In the stated Quiz 1 scope, present in the official practice handout (Problem 1c), but absent from
every circulating Quiz 1 recollection. Include for completeness; do not treat a low score here as a
core-topic failure.

### C1 — tool configuration vector for the Q1 arm — 2 marks

$$
w=\begin{bmatrix} p \\[2pt] e^{q_n/\pi}\,r_3 \end{bmatrix}\in\mathbb{R}^6,\qquad
p=\text{tool-tip position},\ \ r_3=\text{approach vector},\ \ q_n=\text{net tool-roll angle}.
$$

The cylindrical arm has **no roll joint**, so $q_n=0$, $e^{q_n/\pi}=1$, and with
$r_3=(-s_1,\ c_1,\ 0)$ from Q1(d):
$$
w=\big[\,-(d_3+L_t)s_1,\ \ (d_3+L_t)c_1,\ \ d_2,\ \ -s_1,\ \ c_1,\ \ 0\,\big]^{\mathsf T}.
$$

- 1 — correct definition, including that the lower half is the approach vector *scaled by*
  $e^{q_n/\pi}$ (magnitude encodes roll).
- 1 — correct substitution; note $\lVert w_{4:6}\rVert=1=e^0$, consistent with
  $q_n=\pi\ln\lVert w_{4:6}\rVert=0$.

### C2 — inverse kinematics for the Q1 arm — 3 marks

Given a target tool-tip position $(x,y,z)$:

$$
d_2=z,\qquad
\theta_1=\operatorname{atan2}(-x,\ y),\qquad
d_3=\sqrt{x^2+y^2}-L_t.
$$

Derivation: $z=d_2$ directly. From $x=-(d_3+L_t)s_1$, $y=(d_3+L_t)c_1$ with the common **positive**
factor $(d_3+L_t)$: $\ -x=(d_3+L_t)s_1$ and $y=(d_3+L_t)c_1$, so
$\theta_1=\operatorname{atan2}(-x,y)$ and $d_3+L_t=\sqrt{x^2+y^2}$.

- 1 — $d_2=z$ and the radial equation $d_3+L_t=\sqrt{x^2+y^2}$.
- 1 — $\theta_1$ via **atan2** (not $\arctan$): $\theta_1$ can be in any quadrant and $y$ can be $0$
  when the arm points along $\pm x_0$.
- 1 — feasibility: $d_3\ge 0$ (i.e. $\sqrt{x^2+y^2}\ge L_t$) and $z$ within the column stroke;
  states the solution is **unique** (no elbow-up/down branch — one revolute joint, no 2R sub-chain).

Numeric self-check (used to validate this key): $L_t=1$, target $(-3,0,5)$
$\Rightarrow d_2=5$, $\theta_1=\operatorname{atan2}(3,0)=+90^\circ$, $d_3=\sqrt9-1=2$.
Forward-substitute into Q1(d): $-(2+1)\sin90^\circ=-3$ ✓, $(3)\cos90^\circ=0$ ✓, $z=5$ ✓.

### Section C — common wrong paths

| Observed | Diagnosis |
|---|---|
| $w$ lower half is $r_3$ unscaled | Missed the $e^{q_n/\pi}$ factor — the whole point of the representation is that magnitude carries roll |
| $w\in\mathbb{R}^7$ or includes all of $R$ | Confused the tool configuration vector with the full arm matrix |
| $\theta_1=\arctan(-x/y)$ | Quadrant lost; blows up along $\pm x_0$ |
| Reports $\pm$ branch for $d_3$ | Imported the 2R elbow pattern where there is no 2R sub-chain |
| No feasibility statement | IK without a workspace check — flagged in `notes/beginner-notes.tex` §6 |

---

## Marking summary

| Part | Marks | Confidence |
|---|---:|---|
| Q1(a) frame assignment | 4 | derivable (mark vs. own diagram) |
| Q1(b) D–H table | 3 | derivable |
| Q1(c) link transforms | 3 | derivable |
| Q1(d) arm matrix + check | 2 | derivable |
| Q2(a) pick pose | 4 | derivable (given convention) |
| Q2(b) place pose | 3 | derivable |
| Q2 orthonormality check | 1 | derivable |
| **Core total** | **20** | |
| C1 tool configuration vector | 2 | derivable — *predicted topic* |
| C2 inverse kinematics | 3 | derivable — *predicted topic* |
| **Grand total** | **25** | |

**Grading protocol:** mark part by part against the checkpoints above. Separate arithmetic slips
(award method marks, note the slip) from inverted concepts (the $\alpha_2$ twist, the approach-vector
sign, atan2 vs arctan — these are the diagnostic ones). An unattempted part is **blank, not wrong** —
record separately so the learner knows if they ran out of time or knowledge. After grading, fold
every non-slip error into `notes/beginner-notes.tex` / `notes/notes.tex` and log it in `STATUS.md`
(loop stage 6).
