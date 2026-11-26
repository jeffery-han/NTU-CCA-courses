# EE6221 final · Mock B · key and marking rubric

Unofficial practice paper (prep protocol step 3). 5 questions × 20 = **100 marks**, 3 hours, closed book, handwritten.
The paper is `final-mock-b.html`, which has no answers in it. Every number below is recomputed by `final-mock-b-check.py`.
Conventions are the ones in `final-intel.md`, "Conventions to use". The split of marks inside each part is ours; only the 20 per question follows the official papers.

Weighting: Q1 retests the Mock A D-H items (offsets ticked into one cell each, α sign, θ marked as a variable). Part (a) now asks explicitly for **x, y and z** of every frame, because y = z × x is the one item still open in `final-mistakes.md`.
**Prediction (unseen):** Q2(c) puts the unknown disturbance inside the *force* subspace. Circulating papers place disturbances only in the motion subspace or leave them out.

Sources: Lec 1 pp. 53–71 (D-H), pp. 91–108 and 133–141 (tool configuration, IK, tool-configuration Jacobian); Lec 2 pp. 6–13, 20–31, 38–54; Lec 3 pp. 20–40; HGQ Lec 3 pp. 28–32; HGQ Lec 4 pp. 25–44.

---

## Q1 · D-H (20 = 11 + 9)

Figure 1 is a floor-mounted arm. θ1 is a waist about the vertical column. θ2 (shoulder) and θ3 (elbow) have axes perpendicular to the page, 25 cm apart, with the shoulder 30 cm above the floor. The forearm carries a prismatic slide d4 along it. At the end of the slide, θ5 turns about a vertical axis. The tool-roll axis θ6 is 5 cm above the slide line, and the tool tip T is 12 cm along it from the θ5 axis. Frame 0 is at the base, on the θ1 axis, at floor level.

### Model frames (one valid set; page directions: right, up, ⊙ out of page)

| k | origin | z_k | x_k | y_k = z_k × x_k |
|---|---|---|---|---|
| 0 | base, floor | ↑ | → | ⊗ |
| 1 | shoulder centre | ⊙ | → | ↑ |
| 2 | elbow centre | ⊙ | → | ↑ |
| 3 | elbow centre | → (slide) | ↑ | ⊙ |
| 4 | on the θ5 axis, on the slide line | ↑ | ⊙ | → |
| 5 | on the θ5 axis, 5 cm up (roll axis) | → | ⊙ | ↓ |
| 6 | tool tip T | → | ⊙ | ↓ |

With d4 = 20 cm, the tip is at **(57, 35)** cm (out, up), that is 25 + 20 + 12 and 30 + 5. Every origin and axis above is reproduced by multiplying the table below.

### Table

| k | θ | d (cm) | a (cm) | α |
|---|---|---|---|---|
| 1 | \(\theta_1\) | 30 | 0 | \(+90^\circ\) |
| 2 | \(\theta_2\) | 0 | 25 | 0 |
| 3 | \(\theta_3+90^\circ\) | 0 | 0 | \(+90^\circ\) |
| 4 | \(90^\circ\) (fixed) | \(d_4\) | 0 | \(+90^\circ\) |
| 5 | \(\theta_5\) | 5 | 0 | \(-90^\circ\) |
| 6 | \(\theta_6\) | 12 | 0 | 0 |

Why each cell:
- 30 cm runs along z0, so it is d1.
- 25 cm is the common normal between the parallel axes z1 and z2, so it is a2. Because z1 ∥ z2, α2 = 0 and x2 points away from z1.
- Row 3 has θ3 + 90° because x2 → (along the upper arm) turns to x3 ↑ about z2 ⊙.
- Row 4 is prismatic. θ4 is a fixed 90° (x3 ↑ → x4 ⊙ about z3 →), **not 0**, and d4 is the variable.
- 5 cm runs along z4 (the vertical θ5 axis), so it is d5.
- 12 cm runs along z5, so it is d6.

Matrices:

\[T^1_0=\begin{bmatrix}C_1&0&S_1&0\\S_1&0&-C_1&0\\0&1&0&30\\0&0&0&1\end{bmatrix}\quad
T^2_1=\begin{bmatrix}C_2&-S_2&0&25C_2\\S_2&C_2&0&25S_2\\0&0&1&0\\0&0&0&1\end{bmatrix}\quad
T^3_2=\begin{bmatrix}-S_3&0&C_3&0\\C_3&0&S_3&0\\0&1&0&0\\0&0&0&1\end{bmatrix}\]

(\(\cos(\theta_3+90^\circ)=-S_3\), \(\sin(\theta_3+90^\circ)=C_3\).)

### Rubric
- **(a) 11 marks.**
  - z0–z6, 6 marks: z0 ↑; z1 and z2 ⊥ page; z3 along the slide; z4 vertical at the end of the slide; z5 on the roll axis; z6 the approach direction.
  - x axes and origins, 2 marks: frames 2 and 3 share the elbow origin; frame 4 is on the slide line; frame 5 is 5 cm up.
  - y axes, 2 marks: all seven drawn and right-handed. Missing y axes cost 1; any one wrong costs 1.
  - Tool frame at T, 1 mark.
- **(b) 9 marks.** One per row (6). The rows must match *your own* frames, and signs are judged against your drawing. One per matrix (3).

### Common wrong paths
- **25 cm written as d2.** The axes are parallel, so the offset is a common normal, which makes it a2. Writing d2 means the common normal was not drawn.
- **Row 4 written as θ4 = 0 or θ4 = q4.** For a prismatic joint the angle is fixed but read from the frames, and d4 is the variable.
- **α2 = ±90°.** z1 ∥ z2 means α2 = 0. Writing ±90° means z2 was drawn along the arm, not on the elbow axis.
- **The 5 cm forgotten, or written as a5.** It lies along z4, so it is d5. This is the Mock A item 2 slip again.
- **Frame 4 placed at the elbow.** That collapses d4 to 0 and makes the prismatic joint vanish.
- **y omitted.** This is the open item in the mistakes log.

---

## Q2 · Robot control (20 = 9 + 8 + 3)

Dynamics:
\(u_1=(5+2C_2)\ddot q_1+(1+C_2)\ddot q_2-S_2(2\dot q_1\dot q_2+\dot q_2^2)+3\dot q_1+d_1\)
\(u_2=(1+C_2)\ddot q_1+\ddot q_2+S_2\dot q_1^2+9.8C_{12}+d_2\)
\(u_3=4\ddot q_3+2\dot q_3+39.2+f+d_3\)

The unmodelled resonances are 2 Hz, 3.5 Hz and 5 Hz.

### (a) Computed torque, f = 0, d = 0, ζ = 1.1 (9)

\[\alpha=\begin{bmatrix}5+2C_2&1+C_2&0\\1+C_2&1&0\\0&0&4\end{bmatrix},\quad
\beta=\begin{bmatrix}-S_2(2\dot q_1\dot q_2+\dot q_2^2)+3\dot q_1\\S_2\dot q_1^2+9.8C_{12}\\2\dot q_3+39.2\end{bmatrix}\]

\(u=\alpha v+\beta\), \(v=\ddot q_d+k_v\dot e+k_p e\), so \(\ddot e+k_v\dot e+k_pe=0\) on each joint. The mass matrix is positive definite for every q2, because det = 4 − C2² > 0.

Lowest resonance: 2 Hz = 4π = 12.566 rad/s. So ω_n ≤ 0.5 × 12.566, giving **ω_n = 6.2832**. Then **k_v = 2(1.1)(6.2832) = 13.823** and **k_p = 39.478**.

At \(q_2=\pi/3\), \(\dot q_1=1\), \(\dot q_2=-1\), with \(\ddot q_{1d}=0\), \(e_1=0.05\), \(\dot e_1=-0.1\), \(\ddot q_{2d}=0.2\), \(e_2=-0.02\), \(\dot e_2=0.05\):

- \(v_1=13.823(-0.1)+39.478(0.05)=\) **0.5916**
- \(v_2=0.2+13.823(0.05)-39.478(0.02)=\) **0.1016**
- \(u_1=6(0.5916)+1.5(0.1016)-0.8660(-2+1)+3=\) **7.568**

Rubric (9):
- α with the off-diagonal coupling terms, 2.
- β, 2.
- Hz → rad/s, the 0.5 factor and the lowest resonance, 2.
- k_v and k_p, 1.
- The error equation, 1.
- The value of u1, 1.

Wrong paths:
- **Using 2 rad/s.** This forgets the 2π. It gives ω_n = 1, so the design is far too slow.
- **ω_n = 0.5 × 5 Hz.** This uses the highest resonance instead of the lowest.
- **Putting (1 + C2) q̈2 into β.** That term multiplies an acceleration, so it belongs in α.
- **Forgetting 9.8 C12 or 39.2 in β.** Gravity is computable, so β must cancel it.

### (b) Hybrid control, f = 40(q3 − 0.3) measured, d = 0 (8)

- **Subspaces.** q3 is force-controlled, because f depends only on q3. q1 and q2 are position-controlled with ζ = 1.1 and the gains from (a).
- **Force servo**, critically damped with the same ω_n:
  - k_vf = 2(1)(6.2832) = **12.566**
  - k_pf = 39.478
  - \(v_3=\frac{1}{40}\big(\ddot f_d+k_{vf}\dot e_f+k_{pf}e_f\big)\), with \(e_f=f_d-f\)
- **Control law:** \(u=\alpha v+\beta\), where β₃ now includes f: \(u_3=4v_3+2\dot q_3+39.2+f\).
- **Error equations:** \(\ddot e_i+13.823\dot e_i+39.478e_i=0\) for i = 1, 2, and \(\ddot e_f+12.566\dot e_f+39.478e_f=0\).
- **Steady state** for f_d = 10 N: \(q_3=0.3+10/40=\) **0.55** m.

Rubric (8):
- Subspace choice, 1.
- Motion and force servo laws, 3.
- u3 with f in β, 2.
- Error equations, 1.
- q3 at steady state, 1.

Wrong paths:
- **Leaving f out of β₃.** The contact force then acts as a disturbance on the joint.
- **v3 without the factor 1/k_e.** The units are wrong: v3 must be an acceleration, and f̈ = k_e q̈3.
- **e_f = f − f_d.** Every sign in the force servo then flips.

### (c) Unknown constant d3 = 2 N with the controller of (b) (3) · *prediction*

With d3 left out of the model, \(4\ddot q_3=4v_3-d_3\). So

\[\ddot f=40\ddot q_3=\ddot f_d+k_{vf}\dot e_f+k_{pf}e_f-10d_3\]

which gives

\[\ddot e_f+k_{vf}\dot e_f+k_{pf}e_f=\frac{k_e d_3}{m_3}=20\]

The steady-state force error is **e_f = 20/39.478 = 0.5066 N**: the force falls short of f_d. Fix it by adding \(k_{if}\int e_f\,dt\) to the force servo, which drives e_f to 0, with gains kept inside the resonance limit.

Rubric (3):
- Error equation with the right-hand side k_e d3/m3, 1.
- Value of e_ss, 1.
- Integral fix, 1.

Wrong path: "**put d3 in β**." It is unknown, so it cannot be cancelled. That is exactly why it shows up as a steady error (Lec 2 pp. 11–13).

---

## Q3 · Mobile platform and arm (20 = 10 + 10)

### (a) Platform (10)

The platform has:
- two rear fixed standard wheels, A at (−0.2, 0.15) m and B at (−0.2, −0.15) m, radius 0.05, with positive spin driving +X_R;
- a front steered standard wheel C at (0.3, 0) m, radius 0.04, with steering angle β_C(t).

(i) α, β and l (3):

| Wheel | l | α | β |
|---|---|---|---|
| A | 0.25 | 143.13° | −53.13° |
| B | 0.25 | −143.13° | 233.13° (≡ −126.87°) |
| C | 0.3 | 0 | β_C(t) |

For A and B, α + β = 90°, because the rolling direction is +X_R.

(ii) Constraints (4):

\[\begin{bmatrix}1&0&-0.15\\1&0&0.15\\\sin\beta_C&-\cos\beta_C&-0.3\cos\beta_C\end{bmatrix}R(\theta)\dot\xi_I-\begin{bmatrix}0.05&0&0\\0&0.05&0\\0&0&0.04\end{bmatrix}\begin{bmatrix}\dot\varphi_A\\\dot\varphi_B\\\dot\varphi_C\end{bmatrix}=0\]

\[\begin{bmatrix}0&1&-0.2\\0&1&-0.2\\\cos\beta_C&\sin\beta_C&0.3\sin\beta_C\end{bmatrix}R(\theta)\dot\xi_I=0\]

The cells follow from \(l\cos\beta\) and \(l\sin\beta\):
- A: \(-l\cos\beta=-0.25(0.6)=-0.15\) and \(l\sin\beta=0.25(-0.8)=-0.2\).
- B: \(-l\cos\beta=+0.15\) and \(l\sin\beta=-0.2\).

Physical check: the wheel's sideways velocity is \(\dot y_r+\dot\theta x_w=\dot y_r-0.2\dot\theta\).

(iii) With \(\dot x_r=0.4\) m/s and \(\dot\theta=0.5\) rad/s (3):
- The rear sliding rows force \(\dot y_r=0.2\dot\theta=\) **0.1** m/s. The rear axle is behind P, so P slides sideways when the robot turns.
- \(\dot\varphi_A=(0.4-0.075)/0.05=\) **6.5** rad/s.
- \(\dot\varphi_B=(0.4+0.075)/0.05=\) **9.5** rad/s.
- C sliding: \(0.4\cos\beta_C+0.25\sin\beta_C=0\), so \(\beta_C=\pi-\tan^{-1}1.6=\) **2.1294** rad.
- \(\dot\varphi_C=(0.4\sin\beta_C-0.25\cos\beta_C)/0.04=\) **11.792** rad/s.

Check: C moves at (0.4, 0.25) m/s, speed 0.4717 = 0.04 × 11.792.

Rubric (10):
- α, β, l for A and B, 3.
- One rolling row and one sliding row per wheel, with β_C kept symbolic, 3.
- J2 with the right radii, 1.
- ẏ_r, 1.
- φ̇A and φ̇B, 1.
- β_C and φ̇C, 1.

Wrong paths:
- **Taking α = 90° because "the wheel is on the left".** α is the polar angle of the wheel position measured from X_R, and that is 143.13°.
- **Taking ẏ_r = 0.** That is true only when the fixed axle passes through P, as in Mock A. Here it does not.
- **Writing −0.25 in the rolling row.** That is l itself, not l cos β.

### (b) Arm on the platform (10)

\[T^4_0=\begin{bmatrix}C_{124}&S_{124}&0&0.3C_1+0.2C_{12}\\S_{124}&-C_{124}&0&0.3S_1+0.2S_{12}\\0&0&-1&0.45-q_3\\0&0&0&1\end{bmatrix}\]

q3 is prismatic and q4 is the tool roll.

(i) Tool-configuration vector (2):

\[w=\big[0.3C_1+0.2C_{12},\ 0.3S_1+0.2S_{12},\ 0.45-q_3,\ 0,\ 0,\ -e^{q_4/\pi}\big]^T\]

(ii) Tool-configuration Jacobian (3):

\[V=\begin{bmatrix}-0.3S_1-0.2S_{12}&-0.2S_{12}&0&0\\0.3C_1+0.2C_{12}&0.2C_{12}&0&0\\0&0&-1&0\\0&0&0&0\\0&0&0&0\\0&0&0&-\tfrac1\pi e^{q_4/\pi}\end{bmatrix}\]

(iii) IK for \(w=[0.1,\ 0.4,\ 0.2,\ 0,\ 0,\ -e^{0.25}]^T\) (5):
- \(q_4=\pi\ln e^{0.25}=\pi/4=\) **0.7854** rad
- \(q_3=0.45-0.2=\) **0.25** m
- \(C_2=(0.17-0.09-0.04)/0.12=1/3\), so \(q_2=\pm\) **1.2310** rad
- \(q_1=\operatorname{atan2}(0.4,0.1)\mp\operatorname{atan2}(0.2S_2,\,0.3+0.2C_2)\):
  - **0.8508** rad, with q2 = +1.2310
  - **1.8008** rad, with q2 = −1.2310

Both solutions substituted back give (0.1, 0.4, 0.2).

Rubric (10):
- w, 2.
- V: the chain rule on q4 and the −1 for q3, 3.
- q4 and q3, 2.
- q2 with both signs, 1.
- q1 for each solution, 2.

Wrong paths:
- **q4 = 0.25.** This forgets the factor π.
- **The sign of w6 is +.** But r³ = (0, 0, −1): the tool points down.
- **Using tan⁻¹(y/x).** Only atan2 gives the right quadrant.
- **Giving one elbow solution only.**

---

## Q4 · Homography (20 = 10 + 4 + 6)

Seven coplanar points:
- the triangle corners O1 (0, 0), O3 (6, 0) and O5 (0, 6);
- the side midpoints O2 (3, 0), O4 (3, 3) and O6 (0, 3);
- the centroid O7 (2, 2).

The camera poses see these points:
- F_a: O1, O2, O3, O6, O7
- F_b: all seven
- F_c: O3 to O7

There are 6 collinear triples:
- the 3 sides: {O1,O2,O3}, {O3,O4,O5}, {O5,O6,O1};
- the 3 medians through the centroid: {O1,O7,O4}, {O3,O7,O6}, {O5,O7,O2}.

Over all seven points there are 35 − 6 × 4 = 11 valid four-point groups. No four-point group can contain two collinear triples, because two lines share at most one point.

### (a) G_n (10)
F_a ∩ F_b = {O1, O2, O3, O6, O7}. The collinear triples inside it are {O1,O2,O3} (a side) and {O3,O6,O7} (a median). Of the C(5,4) = 5 groups, 2 contain the first triple and 2 contain the second. That leaves **exactly one valid group: \{O_1,O_2,O_6,O_7\}**.

Derivation: \(m_{ib}=\alpha_iG\,m_{ia}\). Divide by g33 and eliminate α_i with row 3. That gives two rows per point:

\[\begin{bmatrix}a_{ix}&a_{iy}&1&0&0&0&-a_{ix}b_{ix}&-a_{iy}b_{ix}\\0&0&0&a_{ix}&a_{iy}&1&-a_{ix}b_{iy}&-a_{iy}b_{iy}\end{bmatrix}g=\begin{bmatrix}b_{ix}\\b_{iy}\end{bmatrix}\]

Stack the four points into Mg = b (8 × 8). Then g = M⁻¹b, and G_n has g33 = 1. M is invertible because no three of the points are collinear. The checker confirms det M ≠ 0 for this group and det M = 0 for {O1,O2,O3,O6}.

Rubric (10):
- Find both triples inside F_a ∩ F_b, especially the median, 3.
- The count of 1, 2.
- The equations and the stacked system, 4.
- The reason M is invertible, 1.

### (b) H_n (4)
F_b ∩ F_c = {O3, O4, O5, O6, O7}. The triples inside it are {O3,O4,O5} and {O3,O6,O7}. That gives 5 − 2 − 2 = **1 group: \{O_4,O_5,O_6,O_7\}**.

### (c) K_n (6)
F_a ∩ F_c = {O3, O6, O7}: only three points, and they are collinear. So K cannot be found directly. Through F_b it can: \(m_c\propto HG\,m_a\), so \(K\propto HG\) and \(K_n=H_nG_n/(H_nG_n)_{33}\). G acts first.

Twist: if F_c saw only {O3, O4, O5, O7}, then F_b ∩ F_c would have one group, and it contains the side {O3,O4,O5}. So H cannot be found, and the direct route has only O3 and O7. **K_n cannot be obtained.**

Rubric (6):
- Direct route impossible, 1.
- Chaining in the right order, 3.
- The twist case answered "no" with the reason, 2.

### Wrong paths
- **Missing the medians.** Students check the sides and stop, then count 3 groups in (a) instead of 1.
- **Answering "yes" in the twist** because "chaining always works". A chain needs every link in it to exist.

---

## Q5 · Grouped sensors (20 = 8 + 6 + 6)

Model: \(x_{k+1}=x_k\), \(y_{ik}=x_k+v_{ik}\), with variances a², 2a², 4a² and 4a² for S1 to S4. The noises are independent of each other and of \(\tilde x_k\).

### (a) Separate gains (8)

\(\tilde x_{k+1}=(1-\sum L_i)\tilde x_k-\sum L_iv_i\), so

\[p_{k+1}=(1-\textstyle\sum L_i)^2p_k+\sum L_i^2\sigma_i^2\]

Setting \(\partial/\partial L_i=0\) gives

\[L_i=\frac{p_k}{\sigma_i^2(1+p_k\sum1/\sigma_j^2)},\qquad \frac1{p_{k+1}}=\frac1{p_k}+\sum\frac1{\sigma_i^2}=\frac1{p_k}+\frac2{a^2}\]

At \(p_k=a^2\): L = **1/3, 1/6, 1/12, 1/12**, and \(p_{k+1}=\) **a²/3**.

Rubric (8):
- Error recursion, 2.
- p_{k+1} expression, 2.
- Gains, 2.
- 1/p form and the numbers, 2.

### (b) S1 alone vs S2–S4 with separate gains (6)

Group A adds 1/a² of information. Group B adds 1/(2a²) + 1/(4a²) + 1/(4a²) = 1/a². **They are equal.** From p_k = a², both give p_{k+1} = a²/2.

Rubric (6):
- Information form for each group, 2 each.
- The conclusion "equal", 2.

A student who answers "B, because it has more sensors" earns 2 at most.

### (c) S2–S4 with one shared gain (6)

\(p_{k+1}=(1-3L)^2p_k+L^2(2+4+4)a^2\). Minimising gives \(L=3p_k/(9p_k+10a^2)\) and \(1/p_{k+1}=1/p_k+\) **9/10**·(1/a²). That is less than 1/a², so S1 alone (with any gain design) now beats group B.

At p_k = a²: L = **3/19** and p_{k+1} = **10/19** a² (0.526 a², against 0.5 a²).

Rubric (6):
- Derivation, 3.
- The value 9/10 (from n²/Σσ²), 1.
- The comparison and the reason, 2. One shared gain cannot weight the better sensor more heavily.

Wrong paths:
- **Averaging the variances.**
- **Writing 1/p₊ = 1/p + 3/(10a²).** This drops the n² factor.

---

## Your attempt, graded 2026-11-26 (Q1–Q3; Q4–Q5 not attempted)

Scans: `attempts/final-mock-b-q1-2026-11-26.jpg`, `attempts/final-mock-b-q2-2026-11-26.jpg`.

**Q1: 19 / 20.** (a) 11/11, (b) rows 6/6, matrices 2/3. The arrow ↗ means into the page and ↙ means out of it. Your z1 and z2 point into the page, the opposite of the model, which is allowed; that is why your α1, α3, α4 are −90° and your θ3 offset is −90°. Forward kinematics of your six rows at q = 0, d4 = 20 reproduces every drawn x, y, z and the tip (57, 35) cm. All seven y axes are drawn and right-handed, which closes mistakes-log item 4. Frame 3 is drawn displaced along a dashed line; the table (d3 = a3 = 0) puts it at the elbow, so it is accepted, but write "O3 = O2" next to it in the exam. Lost mark: T23. With θ = θ3 − 90°, cos = +S3 and sin = −C3, so T23 = [S3 0 C3 0; −C3 0 S3 0; 0 −1 0 0]. You wrote −S3 in (1,1) and −S3 in (2,3).

**Q2: 7 / 20.** (a) 7/9: α 2, β 2, resonance 1/2 (lowest one and the 0.5 factor right, the 2π missing), gains 1 (follow-through), error equation 1, u1 0. (b) 0/8 and (c) 0/3: blank. Note that "v = q̈" should be written as the servo v = q̈d + kv ė + kp e.

**Q3: 2 / 20** (scan `attempts/final-mock-b-q3-2026-11-26.jpg`). (a) 2/10: one rolling and one sliding row per wheel, β_C kept symbolic and rφ̇ on the right (structure 1, J2 1). Lost: l = √(0.2² − 0.15²) = 0.132 (should be +, giving 0.25); α = atan2(2, −1.5) (arguments swapped; should be atan2(0.15, −0.2) = 143.13°); β = 2.857 (should be 90° − α = −53.13°); the row entries have sin and cos swapped between rolling and sliding and the wrong sign on l cos β; R(θ) is missing; (iii) not done. (b) 0/10, blank.

**Q4, Q5:** not attempted (the learner understands the picture but not the equations).

Running total: 28 / 60 on Q1–Q3. Retraining: `final-relearn-q2-q5.html`, then `final-mock-c.html`.
