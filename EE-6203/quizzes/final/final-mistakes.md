# EE6203 final — mistakes log (unofficial practice)

One entry per lost mark, most marks first.  An entry closes only when its retry is right.

## Carried forward from Quiz 3 (`../quiz-03/quiz-03-mistakes.md`, still open on 2026-11-27)

| # | Topic | What went wrong | Rule | Where it is retried |
|---|---|---|---|---|
| C1 | Ripple-free deadbeat (Q3 #1, D1) | Blank in Mock A and Mock D | G_cl = K z⁻¹(1 + b z⁻¹) keeps the plant zero; K from G_cl(1) = 1; C = G_cl/[G(1 − G_cl)]; give u(k), y(k) | Primer D1; E2(b); Mock B Q2(b) |
| C2 | ZOH discretisation (Q3 #2) | Wrong order, no derivation | G_ZAS = (1 − z⁻¹)Z{G(s)/s}; order = denominator degree | Primer Z3; Mock B Q1(d) |
| C3 | Pole-zero matching (Q3 #4, D4) | Dropped the mapped zero; α not divided through | Map every pole and zero by z = e^{sT}; α from D(z=1) = D(s=0) | Primer P1; Mock B Q2(c) |
| C4 | Standard vs direct programming (Q3 #5, #8) | Used the direct count | Standard: n delays; direct: n + m | Primer P1; E2(c)(ii); Mock B Q2(c)(ii) |
| C5 | Jury: strict range; 3rd-order b-row (Q3 #6, D2) | Closed interval; skipped the b-row | Strict inequalities; n = 3 needs \|b₂\| > \|b₀\| | Primer J1; Mock B Q2(a) |
| C6 | Bilinear normalisation, difference equation (D3, D5) | Leading coefficients not divided out; signs | Divide by the leading z coefficient; denominator signs flip | Primer P1; E2(c) |
| C7 | Type and step error (D6) | Assumed type 1 | Type = number of poles at z = 1 | Primer J1; Mock B Q2(a) |

## Part exercises E1–E4 (`final-primer-exercises.md`)

E1 sat 2026-11-28: 16.5/25 (`final-primer-e1-attempt-2026-11-28-marked.md`).  Retry variants R1–R4 are in the chat of that day; their key is under "E1 retries" in `final-primer-exercises.md`.

| # | Marks lost | Item | What was written | Why wrong | Rule | Retry |
|---|---|---|---|---|---|---|
| E1-1 | 4 | E1(c) difference equation by z-transform (concept gap) | (z² − 0.7z + 0.1)Y = 2(zX − z) → Y = 2z/((z−1)(z−0.5)(z−0.2)); y(k) one step late; failed y(1) check ignored | Initial-condition terms subtracted on the right only; the left needs −z²y(0) − zy(1) = −2z, which cancels the right's −2z | At rest before k = 0: Y = [b(z)/a(z)]·X with no IC terms at all; otherwise subtract ICs on **both** sides.  If the formula misses y(0) or y(1), stop and fix | R1 open |
| E1-2 | 1½ | E1(d)(i) ZOH combine (slip) | numerator sum ½z (constant ¼ lost) | ¼ − 1 + 1 = ¼ | After combining, test G_ZAS(1) = G(0) and leading coefficient = first step-response sample | R4 open |
| E1-3 | 2 | E1(a)(ii) step tail (slip) | Σ_{k≥4} z⁻ᵏ = z⁻⁴/(1 − z); not combined | Ratio is z⁻¹: Σ_{k≥n} z⁻ᵏ = z⁻ⁿ/(1 − z⁻¹) = z^{−(n−1)}/(z − 1); "single rational function" means one fraction | Tail from k = n: z^{−(n−1)}/(z − 1); then put all over zⁿ⁻¹(z − 1) and check the FVT gives the final level | R2 open |
| E1-4 | 1 | E1(b) Y₂ = z/(z−1)² behaviour | y₂ = k·1^(k−1), "lim = 1" | 1^(k−1) = 1 but the factor k grows: y₂ = k → ∞ | A double pole at z = 1 is a ramp; a pole at −1 is a non-decaying ±1 oscillation; neither has a limit | R3 open |

## Mock B

Not yet sat.
