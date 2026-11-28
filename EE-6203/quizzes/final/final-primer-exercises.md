# EE6203 final primer — part exercises E1–E4: key and marking rubric (unofficial)

The questions are in `final-primer.html`, one exercise at the end of each part (no answers on the page).  Each is one exam-style question: 25 marks, 45 min, handwritten, closed book, z-transform table assumed given.
Every number below is recomputed by `final-check.py`.  The numbers are new: none repeats Mock B (`final-mock-b.md`), so Mock B stays cold.
Pass rule (study rule, not an NTU rule): **≥ 20/25 and no part blank** → next part.  Otherwise each lost mark goes into `final-mistakes.md` and a fresh variant is set before moving on.

Conventions as in `final-intel.md`: Wen e = r − y; Lee u = −Kx, K = [0 … 0 1] W_C⁻¹ α_c(A), L_O = α_O(A) W_O⁻¹ [0 … 1]ᵀ; LQR cost with a ½.

---

## E1 — Question 1 slot, Wen Ch 1–3 (25)

### (a) 6 marks

**(i) 2.**  x(t) is a **continuous-time signal**: defined for every t (here it is even a continuous function).  [1]
x(kT) is **not digital**: it is discrete in time but its amplitude is not quantised → a **sampled-data signal** (Wen notes pp. 12–15).  [1]

**(ii) 4.**  T = 0.25: x(kT) = 0, 0.25, 0.5, 0.75, 1, 1, 1, …  (x(1) = 1: the t ≥ 1 branch holds at t = 1; here both branches agree anyway).  [1]
X(z) = 0.25z⁻¹ + 0.5z⁻² + 0.75z⁻³ + Σ_{k≥4} z⁻ᵏ = 0.25z⁻¹ + 0.5z⁻² + 0.75z⁻³ + z⁻³/(z − 1).  [2]
  **X(z) = 0.25(z³ + z² + z + 1) / (z³(z − 1)) = 0.25(z + 1)(z² + 1) / (z³(z − 1)).**  [1]

Wrong paths: starting the step tail at z⁻³ (counting k = 3 as t = 1); using the ramp table entry Tz/(z−1)² for all k (forgets the ramp stops at t = 1).

### (b) 5 marks

FVT needs every pole of (1 − z⁻¹)Y(z) strictly inside |z| = 1 (Wen notes pp. 44–47).
- Y₁: (1 − z⁻¹)Y₁ = 0.5/(z − 0.6), pole 0.6 inside → **y₁(∞) = 0.5/0.4 = 1.25.**  [2]
- Y₂: (1 − z⁻¹)Y₂ = 1/(z − 1), pole at z = 1 → **FVT not applicable**; y₂(k) = k, grows without bound.  [1½]
- Y₃: pole 1.2 outside the circle → **FVT not applicable**; **y₃(k) = 5(1.2)ᵏ − 5** diverges.  [1½]

Wrong path: plugging z = 1 into (z − 1)Y₃/z gives −5, a "final value" for a signal that blows up.

### (c) 8 marks

**(i) 2.**  k = −2: y(0) − 0.7y(−1) + 0.1y(−2) = 2x(−1) = 0 → **y(0) = 0**.  k = −1: y(1) − 0.7y(0) + 0.1y(−1) = 2x(0) = 2 → **y(1) = 2**.  [2]
(Not zero: the right-hand side is x(k+1), which is already 1 at k = −1.)

**(ii) 5.**  Shift theorem: z²Y − z²y(0) − zy(1) − 0.7(zY − zy(0)) + 0.1Y = 2(zX − zx(0)).  [1]
(z² − 0.7z + 0.1)Y − 2z = 2z/(z − 1)  →  **Y(z) = 2z² / ((z − 1)(z − 0.5)(z − 0.2)).**  [2]
Y/z = 2z/((z−1)(z−0.5)(z−0.2)): residues 5 at z = 1, −20/3 at 0.5, 5/3 at 0.2.  [1]
  **y(k) = 5 − (20/3)(0.5)ᵏ + (5/3)(0.2)ᵏ, k ≥ 0.**  [1]

**(iii) 1.**  Recursion: y(2) = 0.7·2 − 0 + 2x(1) = 3.4; formula: 5 − 5/3 + 1/15 = 3.4 ✓.  (Final value 5 = 2/(1 − 0.7 + 0.1).)

Wrong paths: y(1) = 0 (assumed, not computed) → Y has 2z/(z−1) only and the answer is off by a shifted copy; PFE on Y(z) instead of Y(z)/z.

### (d) 6 marks

**(i) 4.**  G_ZAS = (1 − z⁻¹) Z{1/(s(s+1)(s+2))}.  1/(s(s+1)(s+2)) = 0.5/s − 1/(s+1) + 0.5/(s+2).  [1]
Z: 0.5z/(z−1) − z/(z − e^{−T}) + 0.5z/(z − e^{−2T}), with e^{−T} = 0.5, e^{−2T} = 0.25.  [1]
× (z − 1)/z and combine over (z − 0.5)(z − 0.25):
  **G_ZAS(z) = (0.125z + 0.0625)/((z − 0.5)(z − 0.25)) = 0.125(z + 0.5)/((z − 0.5)(z − 0.25)).**  [2]
Checks: G_ZAS(1) = 0.5 = G(0); first sample of the step response 0.5 − e^{−T} + 0.5e^{−2T} = 0.125 = leading coefficient.

**(ii) 2.**  Y/R = 2G/(1 + 2G) = **0.25(z + 0.5)/(z² − 0.5z + 0.25)**.  [1]
Poles **z = 0.25 ± j0.4330**, |z| = 0.5 < 1 → **stable**.  [1]

Wrong paths: Z{G(s)} without the hold (gives (z−1)-free answer with wrong numerator); forgetting the ×(z−1)/z.

### E1 retries (2026-11-28, after E1 = 16.5/25)

- **R1 (E1-1).**  y(k+2) − 0.6y(k+1) + 0.08y(k) = 3x(k+1), x = unit step, at rest.  Y = 3z²/((z−1)(z−0.4)(z−0.2)); Y/z residues 25/4, −10, 15/4 → **y(k) = 6.25 − 10(0.4)ᵏ + 3.75(0.2)ᵏ**; y = 0, 3, 4.8, 5.64, 6 (matches the recursion).
- **R1′ (E1-1, after R1 failed 2026-11-29).**  y(k+2) − 0.75y(k+1) + 0.125y(k) = x(k+1), unit step, at rest.  Y = z²/((z−1)(z−0.5)(z−0.25)); Y/z residues 8/3, −4, 4/3 → **y(k) = 8/3 − 4(0.5)ᵏ + (4/3)(0.25)ᵏ**; y = 0, 1, 7/4, 35/16 (matches the recursion).
- **R2 (E1-3).**  x(t) = t for 0 ≤ t < 1.5, 1.5 for t ≥ 1.5, T = 0.5: samples 0, 0.5, 1, 1.5, 1.5, …  X = 0.5z⁻¹ + z⁻² + 1.5z⁻²/(z − 1) = **0.5(z² + z + 1)/(z²(z − 1))**; FVT → 1.5 ✓.
- **R3 (E1-4).**  Yₐ = 3z/(z−1)²: FVT not allowed, yₐ = 3k → ∞.  Y_b = z²/((z−1)(z+1)): FVT not allowed (pole at −1), y_b = 0.5 + 0.5(−1)ᵏ = 1, 0, 1, 0, … no limit.
- **R4 (E1-2).**  G(s) = 2/((s+1)(s+3)), ZOH, T = ln 2: G/s = (2/3)/s − 1/(s+1) + (1/3)/(s+3); **G_ZAS = (5/24)(z + 0.4)/((z − 0.5)(z − 0.125))**; checks G_ZAS(1) = 2/3 = G(0), leading 5/24 = 2/3 − 1/2 + 1/24.

---

## E2 — Question 2 slot, Wen Ch 4–6 (25)

G(z) = 0.1(z + 0.8)/((z − 1)(z − 0.7)), T = 0.1 s.

### (a) 8 marks

**(i) 5.**  CE: (z − 1)(z − 0.7) + 0.1K(z + 0.8) = **z² + (0.1K − 1.7)z + (0.7 + 0.08K) = 0.**  [1]
Jury: |0.7 + 0.08K| < 1 → −21.25 < K < 3.75;  P(1) = 0.18K > 0 → K > 0;  P(−1) = 3.4 − 0.02K > 0 → K < 170.  [3]
  **0 < K < 3.75** (strict).  [1]

**(ii) 1.**  K = 3.75: z² − 1.325z + 1 = 0, poles on the circle at e^{±jθ}, cos θ = 0.6625, θ = 0.8466 rad/sample → **ω = θ/T = 8.466 rad/s.**

**(iii) 2.**  Type 1 (one pole at z = 1) → **step error 0.**  K_v = lim (z − 1)·2G(z)/(Tz) = 2·0.1·1.8/(0.3·0.1) = 12 → **ramp error 1/12 = 0.0833.**  [2]

Wrong paths: closed interval; K_v without 1/T (1.2 → error 0.833); taking |a₂| < a₀ only.

### (b) 10 marks — Quiz 3 open mistake C1

**(i) 4.**  C = G_cl/[G(1 − G_cl)] with G_cl = z⁻¹ → **C(z) = (z − 0.7)/(0.1(z + 0.8)) = 10(z − 0.7)/(z + 0.8)**: cancels the plant zero at −0.8.  [2]
U = G_cl R/G = 10(z − 0.7)/(z + 0.8): **u = 10, −15, 12, −9.6, …** (u(k) = −15(−0.8)ᵏ⁻¹, k ≥ 1).  [1]
u never settles, so y(kT) = 1 from k = 1 but **y(t) ripples between samples** (the integrating plant is pushed back and forth).  [1]

**(ii) 6.**  Conditions: G_cl causal (relative degree ≥ 1); G_cl contains the plant zero (do not cancel it, here −0.8); 1 − G_cl contains the plant pole at z = 1; G_cl(1) = 1.  [2]
G_cl = K(z + 0.8)/z², G_cl(1) = 1 → **K = 1/1.8 = 5/9 = 0.5556.**  [1]
1 − G_cl = (z − 1)(z + 4/9)/z² → **C(z) = (50/9)(z − 0.7)/(z + 4/9) = 5.556(z − 0.7)/(z + 0.4444).**  [1]
U = (50/9)(1 − 0.7z⁻¹) → **u = 5.556, −3.889, 0, 0, …**;  **y = 0, 0.5556, 1, 1, …**  [1]
Settles in **2 samples = 0.2 s** (one more than (i)), u constant afterwards → no ripple.  [1]

Wrong paths: G_cl = K(z + 0.8)/z (relative degree 0, not causal); K = 1/0.8; final u ≠ 0 (the plant has an integrator, so holding y = 1 needs u = 0).

### (c) 7 marks — Quiz 3 open mistakes C4, C6

**(i) 4.**  s = (2/T)(z − 1)/(z + 1) = 20(z − 1)/(z + 1):
D(z) = (20(z − 1) + 2(z + 1)) / (20(z − 1) + 10(z + 1)) = (22z − 18)/(30z − 10)  [2]
  **D(z) = 0.7333(z − 0.8182)/(z − 0.3333) = 0.7333(1 − 0.8182z⁻¹)/(1 − 0.3333z⁻¹).**  [1]
DC: D(1) = 4/20 = 0.2 = D(s = 0) = 2/10 ✓ (bilinear keeps DC gain).  [1]

**(ii) 3.**  **m(k) = e(k) + 0.3333 m(k − 1),  u(k) = 0.7333 m(k) − 0.6 m(k − 1).**  [2]
**One delay** (standard: n = 1); direct programming needs n + m = **2**.  [1]

Wrong paths: not dividing by 30 (leading coefficient) before reading the difference equation; sign of the 0.3333 term flipped; 2 delays for standard.

---

## E3 — Question 3 slot, Lee Lect 1–3 (25)

### (a) 3 marks

ẋ₁ = x₂, ẋ₂ = −2x₂ + u:  **A = [0 1; 0 −2], B = [0; 1], C = [1 0].**  [3]

### (b) 8 marks

(sI − A)⁻¹ = [1/s, 1/(s(s+2)); 0, 1/(s+2)]  [2]  →  **e^{At} = [1, (1 − e^{−2t})/2; 0, e^{−2t}].**  [1]
T = 0.2, e^{−0.4} = 0.67032:  **Φ = [1 0.1648; 0 0.6703].**  [2]
Θ = ∫₀ᵀ e^{Aτ}B dτ = [T/2 − (1 − e^{−2T})/4; (1 − e^{−2T})/2]  [2]  →  **Θ = [0.01758; 0.1648].**  [1]

Wrong paths: Θ = TB = [0; 0.2] (Euler); Θ = A⁻¹(Φ − I)B (A is singular here); stopping at e^{−0.4}.

### (c) 6 marks

G(z) = [θ₁(z − φ₂₂) + φ₁₂θ₂] / ((z − 1)(z − φ₂₂))  [2]
  **G(z) = (0.01758z + 0.01539)/((z − 1)(z − 0.6703)) = 0.01758(z + 0.8753)/((z − 1)(z − 0.6703)).**  [2]
Poles **1 = e^{0·T}** and **0.6703 = e^{−2T}** ✓ (s-poles 0, −2).  [1]
lim (z − 1)G/(Tz) = (0.01758 + 0.01539)/(0.3297 · 0.2) = **0.5** = lim sG(s) = 1/2 ✓.  [1]

### (d) 8 marks

**(i) 3.**  ΦΘ = [0.04475; 0.1105];  **det W_C = det[Θ ΦΘ] = −0.005434 ≠ 0 → controllable.**  [3]

**(ii) 3.**  y(0) = x₁(0) = 0;  y(1) = CΦx(0) = x₁(0) + 0.1648 x₂(0) = 0.1  →  **x(0) = [0; 0.6066].**  [3]  (Possible because W_O = [1 0; 1 0.1648], det = 0.1648 ≠ 0.)

**(iii) 2.**  C = [0 1]: W_O = [0 1; 0 0.6703], **det = 0 → not observable.**  [1]  Velocity readings never reveal where the motor started: a constant position offset leaves every velocity sample unchanged.  [1]

---

## E4 — Question 4 slot, Lee Lect 3–5 (25)

A = [1 0.4; 0 0.6], B = [0.2; 1], C = [1 0].  A² = [1 0.64; 0 0.36].

### (a) 7 marks

W_C = [B AB] = [0.2 0.6; 1 0.6], **det = −0.48 ≠ 0 → controllable.**  [1]
α_c(z) = (z − 0.4)² + 0.09 = **z² − 0.8z + 0.25.**  [1]
α_c(A) = A² − 0.8A + 0.25I = [0.45 0.32; 0 0.13].  [1]
W_C⁻¹ = [−1.25 1.25; 2.0833 −0.4167];  [0 1]W_C⁻¹ = [2.0833 −0.4167].  [2]
  **K = [0.9375 0.6125].**  [1]
Verify: A − BK = [0.8125 0.2775; −0.9375 −0.0125], trace 0.8, det 0.25 → z² − 0.8z + 0.25 ✓.  [1]

### (b) 7 marks

**(i) 4.**  Deadbeat error: α_O = z², α_O(A) = A².  W_O = [1 0; 1 0.4], W_O⁻¹[0; 1] = [0; 2.5].  [2]
  **L_O = A²[0; 2.5] = [1.6; 0.9].**  [1]
A − L_O C = [−0.6 0.4; −0.9 0.6]: trace 0, det 0 → (A − L_O C)² = 0, error zero after 2 steps.  [1]

**(ii) 3.**  x_a = x₁ = y: A_aa = 1, A_ab = 0.4, A_ba = 0, A_bb = 0.6, B_a = 0.2, B_b = 1.
0.6 − 0.4L_r = 0.2 → **L_r = 1.**  [1]
  **x̂₂(k+1) = 0.2 x̂₂(k) + y(k+1) − y(k) + 0.8 u(k).**  [2]

### (c) 5 marks

**(i) 2.**  **(z² − 0.8z + 0.25) z²** — **separation principle** (controller poles ∪ observer poles).  [2]

**(ii) 3.**  Y/R = k_r C(zI − A + BK)⁻¹B; at z = 1: C(I − A + BK)⁻¹B = 1/0.9375.  [2]  **k_r = 0.9375** (= k₁, because the plant has a pole at z = 1 and y = x₁).  [1]

### (d) 6 marks

**(i) 1.**  J = Σ(x² + u²) = ½Σ(2x² + 2u²) → **Q = R = 2.**
**(ii) 3.**  Scalar ARE: S = A²SR/(B²S + R) + Q → S(S + 2) = 4.5S + 2S + 4 → **S² − 4.5S − 4 = 0**, positive root **S = 5.2604.**  [2]
**K = ASB/(B²S + R) = 1.5·5.2604/7.2604 = 1.0868.**  [1]
**(iii) 2.**  Closed-loop pole **1.5 − 1.0868 = 0.4132** (stable; open loop 1.5 was not).  x(1) = **0.4132**, x(2) = **0.1707**.  [1]  **J* = ½Sx(0)² = 2.6302.**  [1]

Wrong paths: Q = R = 1 (same K, S = 2.6302, J* = 1.3151); negative Riccati root (−0.7604 → unstable gain); J* = S x(0)² without the ½.

---

Totals: E1 6 + 5 + 8 + 6 = 25; E2 8 + 10 + 7 = 25; E3 3 + 8 + 6 + 8 = 25; E4 7 + 7 + 5 + 6 = 25.
