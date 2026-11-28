# E1 (final primer, Question 1 slot) — marked attempt, 2026-11-28

Script: `attempts/final-primer-e1-2026-11-28.pdf` (3 pp., pp. 1 and 3 scanned sideways).  Key: `final-primer-exercises.md` § E1.  Unofficial practice marking.

**Total 16.5 / 25 — below the 20/25 pass line: retry E1-1 … E1-4, then move on to Q2.**

| Part | Item | Max | Got | Note |
|---|---|---|---|---|
| (a)(i) | continuous-time; sampled, not digital (not quantised) | 2 | 2 | |
| (a)(ii) | sequence 0, 0.25, 0.5, 0.75, 1, 1, … | 1 | 1 | |
| | series with step tail | 2 | 1 | tail written z⁻⁴/(1 − z); correct z⁻⁴/(1 − z⁻¹) = z⁻³/(z − 1) — **E1-3** |
| | single rational function | 1 | 0 | not combined — **E1-3** |
| (b) | Y₁: FVT yes, 1.25 | 2 | 2 | |
| | Y₂: FVT no (double pole at 1), y = k | 1½ | ½ | wrote y₂(k) = k·1^(k−1), then "lim y₂(k) = 1"; y₂ = k → ∞ — **E1-4** |
| | Y₃: FVT no, y₃ = 5(1.2ᵏ − 1) → ∞ | 1½ | 1½ | |
| (c)(i) | y(0) = 0, y(1) = 2 | 2 | 2 | |
| (c)(ii) | shift theorem with initial conditions | 1 | 0 | wrote (z² − 0.7z + 0.1)Y = 2(zX − z): subtracted z·x(0) on the right, dropped −z·y(1) = −2z on the left — **E1-1** |
| | Y(z) = 2z²/((z−1)(z−0.5)(z−0.2)) | 2 | 0 | got 2z/((z−1)(z−0.5)(z−0.2)) |
| | PFE on Y/z | 1 | 1 | follow-through: 5, 25/3, −40/3 correct for that Y |
| | y(k) | 1 | ½ | 5 + (25/3)0.2ᵏ − (40/3)0.5ᵏ: the true answer delayed one step |
| (c)(iii) | check y(2) | 1 | ½ | recursion y(2) = 3.4 right; formula gave y(1) = 0 ≠ 2 and the mismatch was not acted on — **E1-1** |
| (d)(i) | PFE ½/s − 1/(s+1) + ½/(s+2) | 1 | 1 | |
| | z-transform, e^{−T} = ½, e^{−2T} = ¼ | 1 | 1 | |
| | combine to 0.125(z+0.5)/((z−0.5)(z−0.25)) | 2 | 1 | three numerator expansions right (2z² − 1.5z + ¼, −(4z² − 5z + 1), 2z² − 3z + 1); sum written ½z, constant ¼ dropped → G = ½z/(2(z−½)(2z−½)) — **E1-2** |
| (d)(ii) | Y/R and poles, stable | 2 | 1½ | method right: z/(4z² − 2z + ½), poles 0.25 ± j0.25, \|z\| = 0.354, stable.  True: 0.25(z+0.5)/(z² − 0.5z + 0.25), poles 0.25 ± j0.433, \|z\| = 0.5 |

By part: (a) 4/6, (b) 4/5, (c) 4/8, (d) 4.5/6.

Your y(k) for k = 0…4 (with the k = 3 arithmetic fixed: 5 + 1/15 − 5/3 = 51/15 = 3.4, not 10/3): 0, 0, 2, 3.4, 4.18.  True: 0, 2, 3.4, 4.18, 4.586.  Exactly one step late, which is the fingerprint of the missing −2z.
