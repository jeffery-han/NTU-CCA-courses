# EE6203 Final Mock B — key and marking rubric (unofficial)

Paper: `final-mock-b.html`.  4 questions × 25 marks, 3 h, closed book, own calculator, z-transform table supplied.
Every number below is recomputed by `final-mock-b-check.py`.
Format basis: lecturer statement (Week 1–2 transcripts: 4 questions × 25 marks, 3 h) and the 2022–23 student walkthroughs (`final-intel.md`).  The paper is a prediction, not a recollection.

Conventions used (from the slides; see `final-intel.md` § Conventions): Wen's error `e = r − y`; LPH `u = −Kx`, Ackermann `K = [0 … 0 1] W_C⁻¹ α_c(A)`; LQR cost `J = ½xᵀ(N)Sx(N) + ½Σ(xᵀQx + uᵀRu)`.

---

## Question 1 (25)

### (a) 7 marks

**(i) 2 marks.**  x(t) is a **continuous-time signal**: it is defined for every t, a jump at t = 1 does not change that (Wen Lecture notes p. 12).  [1]
x(kT) is **not digital**: it is discrete-time with continuous amplitude (e.g. e^{−0.5} = 0.60653…), i.e. a **sampled-data signal**; a digital signal also needs quantised amplitude (p. 15).  [1]

**(ii) 5 marks.**  Samples (T = 0.5): x(0) = 2, x(0.5) = 2, x(1) = e⁰ = 1, x(1.5) = e^{−0.5}, and in general x(kT) = e^{−(k−2)/2} for k ≥ 2.  [2: must take the t ≥ 1 branch at t = 1]

X(z) = 2 + 2z⁻¹ + Σ_{k≥2} (e^{−0.5})^{k−2} z^{−k} = 2 + 2z⁻¹ + z⁻² · 1/(1 − e^{−0.5}z⁻¹)  [2: definition + geometric series]

  **X(z) = 2 + 2z⁻¹ + z⁻¹/(z − 0.60653)** = (2z² + 0.78694 z − 0.21306) / (z(z − 0.60653)).  [1]

Common wrong paths: x(1) = 2 (left limit) → every later term shifts; using the table entry for e^{−at} without the two-sample delay.

### (b) 5 marks

FVT needs all poles of (1 − z⁻¹)Y(z) strictly inside the unit circle (Lecture notes pp. 44–47).
- Y₁: (1 − z⁻¹)Y₁ = 0.6z/(z − 0.4), pole 0.4 inside → applies.  **y₁(∞) = 0.6/(1 − 0.4) = 1.**  [2]
- Y₂: (1 − z⁻¹)Y₂ = 1/(z + 1), pole at z = −1 on the unit circle → **FVT does not apply**.  [2]  y₂(k) = 0, 1, 0, 1, … oscillates for ever, no limit.  [1]

Wrong path: plugging z = 1 into (z−1)Y₂/z gives ½, a wrong "final value" (the average, not a limit).

### (c) 8 marks

Initial values from k < 0: k = −2: y(0) − 0.9y(−1) + 0.2y(−2) = x(−2) = 0 → **y(0) = 0**; k = −1: y(1) − 0.9y(0) + 0.2y(−1) = x(−1) = 0 → **y(1) = 0**.  [2]

z-transform with the shift theorem (initial terms vanish): (z² − 0.9z + 0.2) Y(z) = z/(z − 1), so
  Y(z) = z / ((z − 1)(z − 0.5)(z − 0.4)).  [2]

PFE on Y(z)/z: residues 1/(0.5·0.6) = 10/3 at z = 1; 1/((−0.5)(0.1)) = −20 at z = 0.5; 1/((−0.6)(−0.1)) = 50/3 at z = 0.4.  [2]

  **y(k) = 10/3 − 20(0.5)^k + (50/3)(0.4)^k,  k ≥ 0.**  [1]

Check: y(2) = 10/3 − 5 + 8/3 = 1, and the recursion gives y(2) = x(0) = 1.  Final value 10/3 = 1/(1 − 0.9 + 0.2).  [1]

Wrong paths: assuming y(1) given / non-zero; forgetting x(k) is a step (Y = 1/(z²−…)); PFE on Y(z) instead of Y(z)/z.

### (d) 5 marks

G_ZAS(z) = (1 − z⁻¹) Z{G(s)/s} = (1 − z⁻¹) Z{1/(s²(s+1))}.  [1]
1/(s²(s+1)) = 1/s² − 1/s + 1/(s+1) → Z = Tz/(z−1)² − z/(z−1) + z/(z − e^{−T}).  [2]
Multiply by (z−1)/z and combine with e^{−T} = 0.5, T = ln 2:

  **G_ZAS(z) = [(T − 1 + e^{−T}) z + (1 − e^{−T} − T e^{−T})] / ((z − 1)(z − 0.5)) = (0.19315 z + 0.15343) / ((z − 1)(z − 0.5)).**  [2]

Check: DC behaviour — step response of the plant is t − 1 + e^{−t}; at t = T it is 0.19315 = b₁. ✓

---

## Question 2 (25)

### (a) 8 marks

CE: (z − 1)(z − 0.6) + 0.4K(z + 0.5) = **z² + (0.4K − 1.6) z + (0.6 + 0.2K) = 0.**  [2]
Jury, n = 2:  |a₂| < a₀: |0.6 + 0.2K| < 1 → −8 < K < 2;  P(1) = 0.6K > 0 → K > 0;  P(−1) = 3.2 − 0.2K > 0 → K < 16.  [3]
  **0 < K < 2** (strict).  [1]

K = 1: type 1 (one pole at z = 1).  Step: **e_ss = 0.**  Ramp: K_v = lim_{z→1} (z − 1)G(z)/(Tz) = 0.4·1.5/(0.4·0.1) = 15 → **e_ss = 1/K_v = 0.0667.**  [2]

Wrong paths: closed interval [0, 2]; forgetting 1/T in K_v (gives 1.5 and e_ss = 0.667).

### (b) 10 marks — carries Quiz 3 mistakes #1 and D1

**(i) 4 marks.**  C = G_cl / [G(1 − G_cl)] = z⁻¹ / [G · (1 − z⁻¹)] = **(z − 0.6) / (0.4(z + 0.5))**.  [2]  It cancels the plant zero at −0.5.
U(z) = G_cl R / G = 2.5(z − 0.6)/(z + 0.5): **u = 2.5, −2.75, 1.375, −0.6875, …** (u(k) = −2.75(−0.5)^{k−1}, k ≥ 1).  [1]
u(k) never becomes constant, so the plant (which has an integrator) keeps being pushed back and forth: y(kT) = 1 at every sample from k = 1, but **y(t) ripples between samples**.  [1]

**(ii) 6 marks.**  Keep the plant zero in G_cl so it is not cancelled: G_cl = K z⁻¹(1 + 0.5z⁻¹) = K(z + 0.5)/z².  [2]
G_cl(1) = 1 → 1.5K = 1 → **K = 2/3, G_cl = (2/3)(z + 0.5)/z².**  [1]
1 − G_cl = (z − 1)(z + 1/3)/z², so **C(z) = (5/3)(z − 0.6)/(z + 1/3).**  [1]
U(z) = (5/3)(1 − 0.6z⁻¹) → **u = 5/3, −1, 0, 0, …**  Y(z) = G_cl/(1 − z⁻¹) → **y = 0, 2/3, 1, 1, …**  [1]
Settles in **2 sampling periods** (one more than (i)), with u constant (zero) afterwards → no intersample ripple.  [1]

Conditions to quote: G_cl realisable (relative degree ≥ 1), contains G's zeros you must not cancel, 1 − G_cl contains G's unstable/marginal poles (z = 1 here, automatic from G_cl(1) = 1), G_cl(1) = 1 (Lecture notes Ch 5 pp. 55–57, 73–82).

Wrong paths: G_cl = K z⁻¹(z + 0.5) (not realisable: relative degree 0); K = 1/0.5; forgetting that u(k) must settle to the value that holds y = 1 (zero here, because the plant has an integrator).

### (c) 7 marks

**(i) 4 marks.**  Zero s = −1 → z = e^{−0.2} = 0.81873; pole s = −5 → z = e^{−1} = 0.36788.  [2]  Equal numbers of finite poles and zeros, so no (z + 1) factor.
DC gain: D(0) = 1 = α(1 − 0.81873)/(1 − 0.36788) → **α = 3.4871, D(z) = 3.4871(z − 0.81873)/(z − 0.36788).**  [2]

**(ii) 3 marks.**  D(z) = 3.4871(1 − 0.81873z⁻¹)/(1 − 0.36788z⁻¹):
  m(k) = e(k) + 0.36788 m(k − 1),  u(k) = 3.4871 [m(k) − 0.81873 m(k − 1)].  [2]
**One delay element** (standard programming needs n = 1; direct programming would need n + m = 2).  [1]

Wrong paths: α = 1 (no DC match); α from 1 − e^{−0.2} alone; two delays (that is direct programming).

---

## Question 3 (25)

### (a) 9 marks

ẋ₁ = x₂, ẋ₂ = −3x₁ − 4x₂ + u:  **A = [0 1; −3 −4], B = [0; 1], C = [1 0].**  [2]

(sI − A)⁻¹ = [s+4 1; −3 s] / ((s+1)(s+3)); partial fractions give
e^{At} = [1.5e^{−t} − 0.5e^{−3t}, 0.5e^{−t} − 0.5e^{−3t}; −1.5e^{−t} + 1.5e^{−3t}, −0.5e^{−t} + 1.5e^{−3t}].  [3]
At T = ln 2 (e^{−T} = 1/2, e^{−3T} = 1/8):

  **Φ = [11/16 3/16; −9/16 −1/16].**  [1]

Θ = ∫₀ᵀ e^{Aτ}B dτ = [∫(0.5e^{−τ} − 0.5e^{−3τ}); ∫(−0.5e^{−τ} + 1.5e^{−3τ})] = [0.5(1/2) − (1/6)(7/8); −0.5(1/2) + 0.5(7/8)]

  **Θ = [5/48; 3/16] = [0.10417; 0.1875].**  [3]

Wrong paths: Θ = A⁻¹(Φ − I)B is valid here (A invertible) and gives the same answer; Θ = TB (Euler) is wrong.

### (b) 6 marks

det(zI − Φ) = z² − 0.625z + 0.0625 = (z − 0.5)(z − 0.125).  [2]
G(z) = C(zI − Φ)⁻¹Θ = [(z + 1/16)(5/48) + (3/16)(3/16)] / det = (5/48)z + 1/24 over det:

  **G(z) = (5/48)(z + 0.4) / ((z − 0.5)(z − 0.125)).**  [2]

Poles **0.5 = e^{−T} and 0.125 = e^{−3T}** (s-poles −1, −3 mapped by z = e^{sT}).  [1]
DC check: G(1) = (5/48)(1.4)/(0.5·0.875) = 1/3 = continuous DC gain 1/3. ✓  [1]

### (c) 5 marks

ΦΘ = [41/384; −9/128];  W_C = [Θ ΦΘ], **det W_C = −7/256 ≠ 0 → controllable.**  [2½]
W_O = [C; CΦ] = [1 0; 11/16 3/16], **det W_O = 3/16 ≠ 0 → observable.**  [2½]

### (d) 5 marks

x(2) = Φ²x(0) + ΦΘ u(0) + Θ u(1) = 0, with Φ²x(0) = [47/128; −45/128].  [2]
Solve [ΦΘ Θ][u(0); u(1)] = −Φ²x(0):  **u(0) = −27/7 = −3.857,  u(1) = 3/7 = 0.4286.**  [3]
(Possible in two steps because W_C is non-singular, n = 2.)

---

## Question 4 (25)

A = [1 1; 0 0.5], B = [0; 1], C = [1 0].  A² = [1 1.5; 0 0.25].

### (a) 7 marks

α_c(z) = (z − 0.5)² + 0.09 = **z² − z + 0.34.**  [1]
W_C = [B AB] = [0 1; 1 0.5], W_C⁻¹ = [−0.5 1; 1 0].  [2]
α_c(A) = A² − A + 0.34I = [0.34 0.5; 0 0.09].  [2]
K = [0 1]W_C⁻¹α_c(A) = [1 0]α_c(A) = **[0.34 0.5].**  [1]
Verify: A − BK = [1 1; −0.34 0]: trace 1, det 0.34 → z² − z + 0.34. ✓  [1]

### (b) 7 marks

**(i) 4 marks.**  Deadbeat error: α_O(z) = z², α_O(A) = A².  W_O = [C; CA] = [1 0; 1 1], W_O⁻¹[0; 1] = [0; 1].
  **L_O = A²[0; 1] = [1.5; 0.25].**  [2]
Observer: x̂(k+1) = (A − L_O C)x̂(k) + Bu(k) + L_O y(k), with A − L_O C = [−0.5 1; −0.25 0.5].  [1]
(A − L_O C)² = 0, so e(2) = (A − L_O C)²e(0) = 0 for every e(0).  [1]

**(ii) 3 marks — prediction item (current observers have not appeared in the past finals mapped in `final-intel.md`).**
L_C = α_O(A)[CA; CA²]⁻¹[0; 1], CA = [1 1], CA² = [1 1.5] → [CA; CA²]⁻¹[0; 1] = [−2; 2].
  **L_C = A²[−2; 2] = [1; 0.5].**  [2]  Error matrix A − L_C CA = [0 0; −0.5 0], nilpotent → deadbeat. ✓  [1]

### (c) 5 marks

(i) **(z² − z + 0.34) · z²** — the closed-loop poles are the controller poles plus the observer poles: the **separation principle**.  [2]
(ii) Y(z)/R(z) = k_r C(zI − A + BK)⁻¹B = k_r / (z² − z + 0.34).  DC gain at z = 1: k_r/0.34 = 1 → **k_r = 0.34.**  [3]

### (d) 6 marks

The lecture's cost has a ½: J = ½Σ(Qx² + Ru²).  So J = Σ(x² + u²) means **Q = R = 2** (Lect 5 Ex 5.2).  [1]
Recursion: K(k) = BS(k+1)A / (B²S(k+1) + R), S(k) = (A − BK)²S(k+1) + RK² + Q, with A = 1, B = 2.

**(i)** S(2) = 0 → K(1) = 0, S(1) = 2; K(0) = 2·2/(4·2 + 2) = **0.4**, S(0) = 0.2²·2 + 0.16·2 + 2 = **2.4**.
u*(0) = −0.4·2 = −0.8, u*(1) = 0.  **J* = ½S(0)x(0)² = 4.8.**  [2]

**(ii)** Steady state S = (1 − 2K)²S + 2K² + 2 with K = 2S/(4S + 2) → S² − 2S − 1 = 0 → **S = 1 + √2 = 2.4142** (positive root).  [1]
**K = √2 − 1 = 0.41421**, closed-loop pole **1 − 2K = 3 − 2√2 = 0.17157** (stable).  [1]
u*(0) = −0.82843, x(1) = 0.34315, **J* = ½Sx(0)² = 2 + 2√2 = 4.8284.**  [1]
(Infinite horizon costs more than the 2-step cost because it also pays for k ≥ 2.)

Wrong paths: Q = R = 1 gives the same K but S and J* half as large; dropping the ½ in J*; picking the negative Riccati root.

---

Total: 100 marks (Q1 7 + 5 + 8 + 5, Q2 8 + 10 + 7, Q3 9 + 6 + 5 + 5, Q4 7 + 7 + 5 + 6).
