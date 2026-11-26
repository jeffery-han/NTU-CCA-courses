# EE6221 final · Mock C · key and marking rubric

Unofficial practice paper (prep protocol step 5). 5 questions × 20 = **100 marks**, 3 hours, closed book, handwritten.
The paper is `final-mock-c.html`; it contains no answers. Every number below is recomputed by `final-mock-c-check.py`.
The split of marks inside each part is ours; only the 20 per question follows the official papers.

**Weighting**, taken from the open items in `final-mistakes.md` after Mock B:
- #6: offset angles inside the link matrices. T₁² carries θ2 + 90°.
- #7: resonances given in Hz.
- #8: the servo v written out in full.
- #9: hybrid force control, plus a disturbance on the force joint.
- #10–#13: wheel l, α, β and the constraint rows. Wheel C is off the X_R axis.
- #14: the arm (w, V, IK), the homography equations and the Kalman derivation.

Sources: Lec 1 pp. 53–71, 91–108, 133–141; Lec 2 pp. 6–13, 20–31, 38–54; Lec 3 pp. 20–40; HGQ Lec 3 pp. 28–32; HGQ Lec 4 pp. 25–44.

---

## Q1 · D-H (20 = 11 + 9)

The figure is drawn at q = 0, so the θ offsets are fixed by the drawing. Axis directions: → right, ↑ up, ⊙ out of the page, ⊗ into the page.

### Model frames

| k | origin (out, up) cm | x_k | y_k = z_k × x_k | z_k |
|---|---|---|---|---|
| 0 | (0, 0), floor | → | ⊗ | ↑ |
| 1 | (0, 40), shoulder | → | ↑ | ⊙ |
| 2 | (0, 70), elbow | ↑ | ← | ⊙ |
| 3 | (0, 70), elbow | ↑ | ⊙ | → (forearm) |
| 4 | (20, 70), wrist | ↑ | ← | ⊙ |
| 5 | (20, 70), wrist | → | ⊙ | ↓ (tool) |
| 6 | (20, 58), tip T | → | ⊙ | ↓ |

The tip at q = 0 is **(20, 58)** cm: 20 out, and 40 + 30 − 12 up. The checker multiplies the table below and reproduces every axis and every origin listed above.

### Table

| k | θ | d (cm) | a (cm) | α |
|---|---|---|---|---|
| 1 | θ1 | 40 | 0 | +90° |
| 2 | **θ2 + 90°** | 0 | 30 | 0 |
| 3 | θ3 | 0 | 0 | +90° |
| 4 | θ4 | 20 | 0 | −90° |
| 5 | **θ5 − 90°** | 0 | 0 | +90° |
| 6 | θ6 | 12 | 0 | 0 |

Why each cell:
- **40 cm** lies along z0, so it is d1.
- **30 cm** is the common normal between the parallel axes z1 and z2, so it is a2. x2 points up along the upper arm while x1 points →, which gives the **+90° offset**.
- **20 cm** lies along z3, the forearm axis, so it is d4. It is not a3: z2 and z3 intersect at the elbow, so a3 = 0.
- **12 cm** lies along z5, the tool axis, so it is d6.
- **θ5 − 90°**: x4 ↑ turns to x5 → about z4 ⊙.

### Matrices (mistake #6 is the T₁² line)

\[T^1_0=\begin{bmatrix}C_1&0&S_1&0\\S_1&0&-C_1&0\\0&1&0&40\\0&0&0&1\end{bmatrix}\quad
T^2_1=\begin{bmatrix}-S_2&-C_2&0&-30S_2\\C_2&-S_2&0&30C_2\\0&0&1&0\\0&0&0&1\end{bmatrix}\quad
T^3_2=\begin{bmatrix}C_3&0&S_3&0\\S_3&0&-C_3&0\\0&1&0&0\\0&0&0&1\end{bmatrix}\]

The offset identities are cos(θ2 + 90°) = −S2 and sin(θ2 + 90°) = C2. To check them, set q2 = 0: the first column must be x2 = (0, 1, 0) in frame 1, which is ↑. Written in the matrix's own notation, the (1,4) entry is **−30S_2** and the (2,4) entry is **30C_2**.

### Rubric
- (a) 11:
  - z axes, 6
  - x axes and origins, 2 (frames 2 and 3 share the elbow; frames 4 and 5 share the wrist)
  - all seven y axes, right-handed, 2
  - tool frame at T, 1
- (b) 9:
  - one per row, 6 (judged on the learner's own frames)
  - one per matrix, 3. **T₁² must use −S₂ and C₂.** Writing cos(θ2 + 90) without simplifying gets no mark.

### Wrong paths
- **θ2 written as q2.** The drawing has the upper arm vertical, so x2 ↑ ≠ x1 →.
- **20 cm written as a3.** It runs along the forearm axis z3, so it is d4.
- **12 cm written as d5.** The tool axis is z5, so the length is d6.
- **cos(θ+90°) = +S.** It is −S.

---

## Q2 · Robot control (20 = 9 + 8 + 3)

### (a) (9)

\[\alpha=\begin{bmatrix}4+C_2&0.5+0.5C_2&0\\0.5+0.5C_2&0.5&0\\0&0&6\end{bmatrix},\quad
\beta=\begin{bmatrix}-0.5S_2(2\dot q_1\dot q_2+\dot q_2^2)+2\dot q_1+14.7C_1+4.9C_{12}\\0.5S_2\dot q_1^2+4.9C_{12}\\3\dot q_3+58.8\end{bmatrix}\]

- Law: u = αv + β.
- Servo: v = q̈_d + k_v ė + k_p e.
- Error equation: ë + k_v ė + k_p e = 0.
- Lowest resonance: 3 Hz = 6π rad/s, so ω_n = 0.5 × 6π = **9.4248** rad/s.
- Gains: k_p = **88.8264**, k_v = 2(1.2)(9.4248) = **22.6195**.

At the given instant, C2 = 1, S2 = 0 and C12 = cos 60° = 0.5:
- v1 = 88.8264(0.02) = **1.7765**
- v2 = 0.4 + 22.6195(−0.05) + 88.8264(0.01) = **0.1573**
- u2 = (0.5 + 0.5)(1.7765) + 0.5(0.1573) + 0 + 4.9(0.5) = **4.3052**

Rubric (9):
- α, 2
- β with both gravity terms, 2
- Hz → rad/s and the lowest resonance, 2
- gains, 1
- v written out in full, plus the error equation, 1
- u2, 1

Wrong paths:
- ω_n = 1.5 (Hz used directly).
- Using 4.5 Hz because it is listed first; the lowest is 3 Hz.
- Leaving 14.7C1 out of β1.

### (b) (8)
- **Subspaces:** q1 and q2 are position-controlled; q3 is force-controlled.
- **Force servo:** v3 = (1/60)(f̈_d + k_vf ė_f + k_pf e_f), with k_vf = 2ω_n = **18.8496**, k_pf = 88.8264, and e_f = f_d − f.
- **u3** = 6v3 + 3q̇3 + 58.8 + f.
- **Error equations:** ë_i + k_v ė_i + k_p e_i = 0 for i = 1, 2, and ë_f + k_vf ė_f + k_pf e_f = 0.
- **At the instant:**
  - e_f = 18 − 12 = 6
  - ė_f = −ḟ = −60(0.1) = −6
  - v3 = (18.8496(−6) + 88.8264(6))/60 = **6.9977**
  - u3 = 6(6.9977) + 0.3 + 58.8 + 12 = **113.0861**
- **Steady state:** 60(q3 − 0.15) = 18, so q3 = **0.45 m**.

Rubric (8):
- subspaces, 1
- force servo with 1/k_e, 2
- u3 with f in β, 1
- error equations, 1
- ė_f from q̇3, 1
- u3 value, 1
- steady q3, 1

Wrong paths:
- No 1/60 in v3.
- ė_f taken as 0 (the force is changing, because q̇3 ≠ 0).
- f left out of β3.

### (c) (3)
Since 6q̈3 = 6v3 − d3, the force equation becomes

\[\ddot e_f+k_{vf}\dot e_f+k_{pf}e_f=\frac{k_e d_3}{m_3}=\frac{60\cdot3}{6}=30.\]

So e_f,ss = 30/88.8264 = **0.3377** N, short of f_d. The fix is to add k_if ∫e_f dt to the force servo. In shorthand, the right-hand side is **= 30**.

Rubric (3):
- equation with k_e d/m, 1
- value, 1
- integral fix, 1

---

## Q3 · Mobile platform and arm (20 = 10 + 10)

### (a) (10)

| Wheel | l | α | β |
|---|---|---|---|
| A | 0.25 | 163.74° | −73.74° |
| B | 0.25 | −163.74° | 253.74° ≡ −106.26° |
| C | 0.3162 | 18.43° | β_C(t) |

For A and B, α + β = 90°, so the rolling direction is 0°, along +X_R.

**Rolling** (J1 R(θ) ξ̇_I − J2 φ̇ = 0, with J2 = diag(0.05, 0.05, 0.04)):

\[J_1=\begin{bmatrix}1&0&-0.07\\1&0&0.07\\\sin(18.43^\circ+\beta_C)&-\cos(18.43^\circ+\beta_C)&-0.3162\cos\beta_C\end{bmatrix}\]

**Sliding** (C1 R(θ) ξ̇_I = 0):

\[C_1=\begin{bmatrix}0&1&-0.24\\0&1&-0.24\\\cos(18.43^\circ+\beta_C)&\sin(18.43^\circ+\beta_C)&0.3162\sin\beta_C\end{bmatrix}\]

Check: A's rolling row gives −l cos β = −0.25 cos(−73.74°) = −0.07 = −y_A, and its sliding row gives l sin β = −0.24 = x_A. The checker projects each hub velocity and confirms every row.

**Speeds**, with ẋ_r = 0.6 m/s and θ̇ = −0.5 rad/s:
- The A and B sliding rows give ẏ_r = 0.24 θ̇ = **−0.12** m/s.
- φ̇_A = (0.6 − 0.07θ̇)/0.05 = **12.7** rad/s.
- φ̇_B = (0.6 + 0.07θ̇)/0.05 = **11.3** rad/s.
- C's hub velocity is (ẋ − 0.1θ̇, ẏ + 0.3θ̇) = (0.65, −0.27).
  - Its rolling direction is atan2(−0.27, 0.65) = −22.55°, so 18.43° + β_C − 90° = −22.55°.
  - That gives β_C = **49.01°** = **0.8553** rad.
  - φ̇_C = |(0.65, −0.27)|/0.04 = **17.5962** rad/s.

Rubric (10):
- l, α, β for A, B and C, 3
- rows, with C symbolic, 3
- J2 and R(θ), 1
- ẏ_r, 1
- φ̇_A and φ̇_B, 1
- β_C and φ̇_C, 1

Wrong paths:
- **α_C = 0.** C is off the axis, so α_C = atan2(0.1, 0.3).
- **ẏ_r = 0.**
- **l = √(0.24² − 0.07²).**
- **C's hub velocity without the −θ̇ y_C term.**

### (b) (10)

\[w=\big[0.35C_1+0.25C_{12},\ 0.35S_1+0.25S_{12},\ 0.5-q_3,\ 0,\ 0,\ -e^{q_4/\pi}\big]^T\]

\[V=\begin{bmatrix}-0.35S_1-0.25S_{12}&-0.25S_{12}&0&0\\0.35C_1+0.25C_{12}&0.25C_{12}&0&0\\0&0&-1&0\\0&0&0&0\\0&0&0&0\\0&0&0&-\tfrac1\pi e^{q_4/\pi}\end{bmatrix}\]

IK:
- q4 = π ln e^{0.75} = **2.3562** rad.
- q3 = 0.5 − 0.18 = **0.32 m**.
- C2 = (0.09 + 0.1225 − 0.1225 − 0.0625)/(2·0.35·0.25) = **11/70** = **0.1571**.
- So q2 = ±**1.4130** rad.
- q1 = atan2(0.35, 0.3) − atan2(0.25S2, 0.35 + 0.25C2):
  - **0.2970** rad with q2 = +1.4130;
  - **1.4274** rad with q2 = −1.4130.
- Both solutions substituted back give (0.3, 0.35).

Rubric (10):
- w, 2
- V, 3
- q4 and q3, 2
- q2 with both signs, 1
- q1 for each solution, 2

---

## Q4 · Homography (20 = 10 + 4 + 6)

There are five collinear triples:
- the bottom side {O1, O6, O2}
- the top side {O4, O7, O3}
- the middle vertical {O6, O5, O7}
- the diagonals {O1, O5, O3} and {O2, O5, O4}

### (a) (10)
F_a ∩ F_b = {O1, O2, O4, O6, O7}. The only triple inside it is {O1, O2, O6}. That gives C(5,4) − 2 = **3 groups**:
- **{O1, O2, O4, O7}**
- **{O1, O4, O6, O7}**
- **{O2, O4, O6, O7}**

The two groups that fail contain O1, O2 and O6. Those three points are collinear, which makes the 8 × 8 system singular. The checker confirms det M ≠ 0 exactly for the three groups listed.

System: λ_i m_ib = G m_ia. Normalise so that g33 = 1, and eliminate λ_i using row 3. Each point then gives two rows, [a_x, a_y, 1, 0, 0, 0, −a_x b_x, −a_y b_x] g = b_x and [0, 0, 0, a_x, a_y, 1, −a_x b_y, −a_y b_y] g = b_y. Stack four points into M g = b, and solve g = M⁻¹b.

O7, with a = (1.5, 2.2) and b = (2.1, 1.8):
- [1.5, 2.2, 1, 0, 0, 0, **−3.15**, **−4.62**] g = 2.1
- [0, 0, 0, 1.5, 2.2, 1, **−2.70**, **−3.96**] g = 1.8

Rubric (10):
- count with the triple identified, 3
- list, 1
- why the others fail, 1
- derivation and stacked system, 3
- O7's rows, 2

### (b) (4)
F_b ∩ F_c = {O3, O4, O5, O6, O7}. Its triples are {O3, O4, O7} and {O5, O6, O7}, so there is 5 − 2 − 2 = 1 group: **{O3, O4, O5, O6}**.

Rubric (4):
- both triples, 2. The middle line through the centre is the trap.
- the group, 2

### (c) (6)
F_a ∩ F_c = {O4, O6, O7} has only 3 points, so K cannot be found directly. Through F_b it can: K ∝ HG, so K_n = H_nG_n/(H_nG_n)₃₃.

**Twist:** without O6 in F_b, F_b ∩ F_c = {O3, O4, O5, O7}. That set contains the line {O3, O4, O7}, so H cannot be found. The chain is broken, and **K_n cannot be obtained**.

Rubric (6):
- direct route impossible, 1
- chain in the right order with normalisation, 3
- twist answered "no" with the reason, 2

---

## Q5 · Sensor integration (20 = 8 + 6 + 6)

Variances are written in units of a². S1 = 3, S2 = 6, S3 = 1.

### (a) (8)
The full derivation: x̃_{k+1} = (1 − ΣL_i) x̃_k − Σ L_i v_i. So p_{k+1} = (1 − ΣL_i)² p_k + Σ L_i² σ_i². Setting ∂/∂L_i = 0 gives L_i σ_i² = (1 − ΣL_j) p_k. Then L_i = p_k / (σ_i² (1 + p_k Σ 1/σ_j²)), and 1/p_{k+1} = 1/p_k + Σ 1/σ_i².

At p_k = 2a²:
- 1/p_{k+1} = 1/2 + 1/3 + 1/6 + 1 = 2/a², so p_{k+1} = **a²/2**.
- L1 = **1/6**, L2 = **1/12**, L3 = **1/2** (L_i = p_{k+1}/σ_i²).

Rubric (8):
- error recursion, 2
- p_{k+1}, 2
- gain derivation, 2
- numbers, 2

### (b) (6)
- Group A adds 1/a² of information. Group B adds 1/(3a²) + 1/(6a²) = 1/(2a²).
- **A (S3 alone) is better.**
- From p_k = 2a²: A gives **2/3** a² and B gives a².

Rubric (6):
- information for each group, 2 each
- conclusion, 2

### (c) (6)
- p_{k+1} = (1 − 3L)² p_k + L² (3 + 6 + 1) a².
- L = 3p_k/(9p_k + 10a²) = **3/14**.
- 1/p_{k+1} = 1/2 + 9/10 = 14/10, so p_{k+1} = **5/7** a² ≈ 0.714 a².
- This is **worse** than S3 alone (2/3 a² ≈ 0.667 a²). One shared gain must weight the noisy S1 and S2 as heavily as S3, and that costs more than their extra information is worth: 9/10 < 1.

Rubric (6):
- derivation, 3
- values, 1
- comparison with the reason, 2

Wrong path: answering "three sensors are always better than one". That holds only with separate gains.
