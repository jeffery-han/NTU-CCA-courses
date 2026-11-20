# EE6221 Quiz #2 — Mock 1: key, rubric and wrong paths

**UNOFFICIAL prediction.** Format from `quiz-02-intel.md` (official: short questions on Lec 1–4, 60 min, closed book, no calculator; unofficial: ~10 T/F with justification + one short answer). **Mark split is estimated** (40 marks: A = 10 × 2, B = 20). All numeric keys are asserted by `quiz-02-mock-01-check.py`.

Section A rubric (every item): **1 mark** correct True/False; **1 mark** a justification that names the governing fact or shows the one-line calculation. A correct verdict with a wrong or missing reason earns 1. A wrong verdict earns 0 even with relevant text, unless the reasoning is correct and only the final word is flipped (then 1, record as a slip).

---

## Section A

**A1 — "Calibrating a sensor removes its random error."** — **FALSE.**
Calibration corrects *systematic* (deterministic) error, which can be modelled and predicted (e.g. lens distortion). Random error cannot be predicted, only described probabilistically and reduced by filtering/averaging (Lec 1 p. 26; lecturer: "calibration may improve accuracy when the systematic error can be modelled").
*Wrong paths:* "True — calibration improves accuracy" (mixes accuracy with removing noise; shows precision/accuracy confusion, Lec 1 p. 25).

**A2 — Ultrasonic echo after 30 ms, c = 340 m/s → object 5.1 m away.** — **TRUE.**
d = c·t/2 = 340 × 0.030 / 2 = 5.1 m (Lec 1 p. 38). c·t = 10.2 m is the round trip. (Numbers deliberately differ from the in-class 10 ms → 1.7 m example.)
*Wrong paths:* answering False because 10.2 m (used p. 36's round-trip d = c·t as range: forgot the factor 2); 0.51 m / 51 m (unit slip in ms).

**A3 — "Fusing complementary sensors mainly reduces uncertainty about one feature that each sensor can already perceive."** — **FALSE.**
That describes **redundant** information (several sensors see the same feature → lower uncertainty, higher reliability, Lec 1 p. 14). **Complementary** sensors let the system perceive features that no single sensor can perceive alone (p. 15).
*Wrong paths:* True → redundant/complementary swapped; revise the four advantages: redundancy, complementarity, timeliness, cost (p. 13).

**A4 — Pinhole: fσx = fσy = 500 px, α = 0, (u0, v0) = (320, 240); m̄ = [0.2, −0.1, 2]ᵀ m → pixel (370, 215).** — **TRUE.**
m = [x/z, y/z, 1]ᵀ = [0.1, −0.05, 1]ᵀ; u = 500(0.1) + 320 = 370; v = 500(−0.05) + 240 = 215 (Lec 2 p. 30, p = A m).
*Wrong paths:* (420, 190) → forgot to divide by z; (320 ± …) sign slip on v; adding u0 before scaling.

**A5 — "Knowing p and A, the point's Euclidean coordinates are m̄ = A⁻¹p."** — **FALSE.**
A⁻¹p gives the **normalised** coordinates m = [x/z, y/z, 1]ᵀ only; the depth z is lost in projection, so m̄ = z·m is unrecoverable without extra information (Lec 2 p. 32 "depth ambiguity is a consequence of imaging"; p. 17). Every point on the ray z·m has the same p.
*Wrong paths:* True → treats A as invertible map of 3D points; review p. 17 loss of size and depth.

**A6 — "From ≥ 8 matched points, E = [x]×R recovers R and the translation x including its magnitude."** — **FALSE.**
The epipolar constraint mⱼᵀ E mⱼ* = 0 is homogeneous, so E — and therefore x — is recovered only **up to scale**: x′ = λx (Lec 3 p. 15 "loss of scale information", p. 17, p. 19). Magnitude needs extra knowledge (a known distance).
*Wrong paths:* True; or "False because 8-point needs coplanar points" (wrong reason: it needs points **not** all coplanar).

**A7 — "Any essential matrix E = [x]×R (x ≠ 0) has two equal non-zero singular values and one zero."** — **TRUE.**
That is why the noisy estimate is projected to the nearest essential matrix by replacing Σ with diag{σ, σ, 0} (Lec 3 p. 17). The zero singular value comes from [x]× being rank 2 ([x]× x = 0). (Check script: x = [1,2,2], R = R_y(60°) gives singular values 3, 3, 0.)
*Wrong paths:* "False, a rotation is full rank" (forgets the skew factor is rank 2).

**A8 — "The 4-point (homography) method cannot be used when all feature points lie on one plane."** — **FALSE.**
The homography method *requires* ≥ 4 **coplanar**, non-collinear points (Lec 3 p. 29, p. 43). It is the 8-point/essential method that cannot have all points coplanar.
*Wrong paths:* True → E and H requirements swapped. Comparison list, p. 43: E ≥ 8 points / not all coplanar / needs x ≠ 0; H ≥ 4 / all coplanar / needs extra view or knowledge to pick between solutions.

**A9 — "For uncorrelated X, Y: V(X − Y) = V(X) − V(Y)."** — **FALSE.**
V(X − Y) = V(X) + V(−Y) = V(X) + (−1)²V(Y) = **V(X) + V(Y)** (Lec 4 p. 15 with Y → −Y; variance scales by the square of a constant). Variances of uncorrelated terms always add.
*Wrong paths:* True (sign carried through linearly — misses the square); "True if means are zero" (means do not matter).

**A10 — "Scalar KF, A = H = 1: as R → ∞, K → 0 and the update ignores the measurement."** — **TRUE.**
K = AHP/(H²P + R) = P/(P + R) → 0 as R → ∞ (Lec 4 p. 29/31), so x̂ ← x̂ + 0·(z − x̂). An infinitely noisy sensor carries no information. (Conversely R → 0 gives K → 1: trust the measurement.)
*Wrong paths:* "K → 1" (inverted the ratio); "False, the gain depends only on P" (forgot R in the denominator).

---

## Section B — two-sensor fusion (20)

Model (given in the paper): x_{k+1} = x_k (constant state, Lec 4 p. 33), z₁ = x + v₁, z₂ = x + v₂, vᵢ zero-mean, variances σ₁², σ₂², independent of each other and of the estimation error x̃_k = x − x̂_k, E[x̃_k] = 0, P_k = E[x̃_k²].

**B(a) [4] Error variance of the batch estimator x̂_{k+1} = x̂_k + K₁(z₁ − x̂_k) + K₂(z₂ − x̂_k).**
x̃_{k+1} = x − x̂_{k+1} = x̃_k − K₁(x̃_k + v₁) − K₂(x̃_k + v₂) = (1 − K₁ − K₂)x̃_k − K₁v₁ − K₂v₂. (2: substitute zᵢ − x̂_k = x̃_k + vᵢ and collect)
Square and take expectations; cross terms vanish by the uncorrelatedness assumption (1):
**P_{k+1} = (1 − K₁ − K₂)² P_k + K₁²σ₁² + K₂²σ₂²** (1) (Lec 4 p. 37–38).

**B(b) [6] Optimal gains.** ∂P_{k+1}/∂K₁ = −2(1 − K₁ − K₂)P_k + 2K₁σ₁² = 0 and ∂/∂K₂ similarly (2). So (1 − K₁ − K₂)P_k = K₁σ₁² = K₂σ₂² (1). Solving (2):
**K₁ = P_k σ₂² / (σ₁²σ₂² + P_k(σ₁² + σ₂²)), K₂ = P_k σ₁² / (σ₁²σ₂² + P_k(σ₁² + σ₂²))** (Lec 4 p. 40). Interpretation (1): the gain on sensor 1 is proportional to the *other* sensor's variance — the noisier sensor gets the smaller gain.
(Bonus check, not required: P_min = P_kσ₁²σ₂²/(σ₁²σ₂² + P_k(σ₁²+σ₂²)), and with no prior, P_k → ∞, the weights tend to σ₂²/(σ₁²+σ₂²), σ₁²/(σ₁²+σ₂²), matching (12).)

**B(c) [6] Sequential numbers: z₁ = 10 (σ₁² = 1), then z₂ = 15 (σ₂² = 4).**
Prior from sensor 1: x̂₀ = z₁ = 10, P₀ = σ₁² = 1 (Lec 4 p. 41) (1).
K = P₀/(P₀ + σ₂²) = 1/5 (2 — scalar KF gain with A = H = 1, R = σ₂²).
x̂ = 10 + (1/5)(15 − 10) = **11** (1); equivalently (4/5)·10 + (1/5)·15 (eq. 12).
P = (1 − K)P₀ = σ₁²σ₂²/(σ₁²+σ₂²) = **4/5** (2).
Note: slide p. 42 labels R = diag(σ₁², σ₂²); in this scalar sequential step R is σ₂² alone. Either route gives the same numbers; do not use a 2×2 R here.

**B(d) [4]** Third sensor, variance 4, reading fused after the first two: 1/P = 1/1 + 1/4 + 1/4 = 3/2 → **P = 2/3** (2). (Sequentially: K = (4/5)/(4/5 + 4) = 1/6, P = (5/6)(4/5) = 2/3.)
Why fusion helps / when it fails (2, any two): fused variance is below every individual variance because independent errors partly cancel (redundancy, Lec 1 p. 14; Lec 4 p. 43); the most accurate sensor gets the largest weight; it **fails** if the noises are correlated or biased (systematic error is not averaged out), or if the model/linear-Gaussian assumptions do not hold (Lec 4 p. 45).

**Section B wrong paths**
- Keeping cross terms like 2K₁K₂E[v₁v₂] — fine only if you then use independence to drop them; leaving them in signals the assumption wasn't used.
- Gain on sensor 1 ∝ σ₁² (swapped) → the noisy sensor is trusted more; check with σ₁² → ∞ (K₁ must → 0).
- x̂ = 12.5 (plain average) — ignored the variances. x̂ = 14 — weights swapped.
- P = 5 or 3 (variances added or subtracted) instead of combined in parallel.
- Using p. 42's diag(σ₁², σ₂²) as a matrix R in a scalar update.

## Confidence classes
All Section A items and B(a)–(d) are **derivable** from the slides cited. Only A3's wording ("mainly") is mildly **convention-dependent** — the slide definitions (pp. 14–15) decide it.
