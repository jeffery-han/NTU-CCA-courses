# EE6221 final exam — scope and format evidence

Compiled 2026-11-20.  The primary evidence is the **five official past papers** from the NTU Library
repository (Graduates folder).  They are stored locally in `tests/` and **git-ignored**: they are
NTU-only, copyright-marked, and this backup repo is public.  This file summarises topics only.
**This sitting's date, time and venue are NOT verified.**  NTULearn had no final-exam announcement on
2026-11-20; check the exam timetable / StudentLink.

## Sources consulted

| Source | What it gives | Trust |
|---|---|---|
| `tests/test-final-2023-24-s2.pdf`, `-2024-25-s1.pdf`, `-2024-25-s2.pdf`, `-2025-26-s1.pdf`, `-2025-26-s2.pdf` | Five complete official papers | **Official** |
| `resources/lecture-02-robot-control.pdf` pp. 8–13, 32–54 | Partitioned control, gain rule, disturbance + integral, force and hybrid control | Official |
| `resources/lecture-03-mobile-robot-kinematics.pdf` pp. 21–39 | Wheel constraints (fixed, steered, castor), Examples 2 and 4 | Official |
| `resources/additional-materials/review-week-06-control.pdf`, `review-week-07-mobile-robot-kinematics.pdf`, `robot-control-examples-additional-info.pdf` | Lecturer's review sheets (uploaded after Weeks 6–7) | Official |
| `resources/exercises-robot-control-not-for-submission.pdf` + `-solutions.pdf` | α/β design, 3-link PD computed torque, kv = 90, kp = 2025 | Official |
| `resources/transcripts-raw/week-06-transcript.txt` | "Remember these two specifications" (ζ and the resonance limit) | High (ASR text) |
| `resources/transcripts-raw/week-11-transcript.txt` | Kalman: two-sensor gains K1, K2 are the key point, three sensors the same way; sequential processing is "reference reading, not required" | High (ASR text) |
| `resources/transcripts-raw/week-12-transcript.txt` | Hybrid 2.5D visual servoing "not covered in this class" | High (ASR text) |
| `quizzes/quiz-02/quiz-02-intel.md` | Part 2 final = HGQ Lec 2–4 (Lec 1 "not covered in the final exam"); Lec 3 slides 18, 33–36 not tested | High (Week 8 transcript) |
| `resources/transcripts-raw/week-05…07`, `week-13-transcript.txt` | No exam remarks found | — |

## Format (official, constant over all five papers)

- **3 hours, closed book, 5 questions, answer all, 20 marks each.**  Each question has 2–3 parts.
- The slot of each topic never changed in five sittings:

| Q | Topic | Lecture | Typical split |
|---|---|---|---|
| 1 | D-H: link-coordinate diagram (11–12) + kinematic-parameter table and the first 3 link transforms (8–9) | Part 1 Lec 1 | 12 + 8 or 11 + 9 |
| 2 | Robot control: computed torque with ζ and the resonance limit; hybrid position/force control; error equations with disturbances or model error | Part 1 Lec 2 | 9–14 + 6–11 (+3) |
| 3 | (a) mobile-robot rolling + sliding constraints of a drawn platform (8–10); (b) manipulator on the platform: tool-configuration vector / Jacobian / analytic IK at a given point (10–12) | Part 1 Lec 3 + Lec 1 | 8–10 + 10–12 |
| 4 | Homography: count valid four-point groups (no three collinear), derive G_n / H_n, chain to the third pose | HGQ Lec 3 | 7 + 6 + 7 style |
| 5 | Multi-sensor Kalman, x_{k+1} = x_k: one gain per sensor vs one gain for all, or group A vs group B; which gives smaller error | HGQ Lec 4 | 10 + 10 or 6 + 8 + 6 |

## Topic map (official papers)

| Sitting | Q2 robot control | Q3(a) mobile platform | Q3(b) arm | Q4 homography | Q5 Kalman |
|---|---|---|---|---|---|
| 23-24 S2 | Cartesian xy robot, stiffness 50 N/m; hybrid, motion ζ = 1 / force ζ = 1.25, "gains as high as possible", resonances 7, 15 rad/s (13); integral action; **stiffness misjudged as 49** (7) | steered + 2 standard + castor (10) | IK of a 3-joint arm (10) | 9 points, 7 collinear groups; which groups, derive H_n | 2 sensors a², 9a²: one shared gain vs separate gains |
| 24-25 S1 | 3-DOF, f = 22(q3 − 0.2); hybrid, motion ζ = 1.05 / force ζ = 1; resonances 5, 10, 15 (14); error equations with disturbances (6) | steered + 2 standard, r = 10 cm (8) | tool-config Jacobian, IK at (0.2, 0.2, 0), approach vector (12) | 12-point grid, G, H, J = chain | 3 sensors a², 4a², 9a²: separate gains (10); one gain + compare (10) |
| 24-25 S2 | 3-DOF Cartesian, computed torque ζ = 1, resonances 6, 12, 18 (9); 2×2 stiffness matrix, hybrid (8); unknown constant force along z (3) | circular, 2 standard + castor (8) | T01, T12, T23 (prismatic): FK, IK at a point (12) | circle + 3 lines, 8 points; G_n, H_n, can J_n be found? | 4 sensors: pair 1&4 vs pair 2&3 |
| 25-26 S1 | 2-link coupled + prismatic, computed torque ζ = 1.25, resonances 8, 16, 24 (9); f = 25(q3 − 0.2), constant d1, d2, hybrid, error equations (11) | 2 standard + steered, 45° geometry (8) | T_wrist and T_tool: FK, IK at a point (12) | 9 points on 3 parallel lines; G, H, M | Group {1,2} vs group {3,4,5} |
| 25-26 S2 | 4-DOF, f = 12(q1 − 0.20), **no force sensor**; hybrid, motion ζ = 1 / force ζ = 1.2, resonances 10–25; **q_e drifts to 0.19** unnoticed (b) | circular, standard r = 0.10 + steered r = 0.08 | T04 and tool-config vector, then IK | 9 points on 3 lines through O3; H, J, K | 5 sensors, S1–S2 vs S3–S5 |

## Conventions to use (slide pages)

- **Partitioned control** `τ = αv + β`, α = the inertia (matrix) multiplying q̈, β = everything else (Coriolis, friction, gravity, contact force).  Servo `v = q̈_d + k_v ė + k_p e`, `e = q_d − q`, giving `ë + k_v ė + k_p e = 0`.  Lec 2 pp. 8–10; review sheet p. 1.
- **Gains**: `k_v = 2ζω_n`, `k_p = ω_n²`, with ζ ≥ 1 and **ω_n ≤ 0.5 ω_res (lowest resonance)**.  Resonance in Hz → multiply by 2π first (exercise 2: 14.5 Hz → 91.1 rad/s → ω_n = 45 → kv = 90, kp = 2025).  Lec 2 pp. 10–11, 37.
- **Disturbance**: `m(ë + k_v ė + k_p e) = d`, `e_ss = d/(m k_p)`; add `k_i ∫e dt` to remove it.  Lec 2 pp. 11–13.
- **Force control**: `f = k_e(x − x_e)`, β includes f, `f̈ = k_e ẍ`, `v = k_e⁻¹(f̈_d + k_vf ė_f + k_pf e_f)`, `e_f = f_d − f`.  Lec 2 pp. 38–41.
- **Hybrid**: split into motion subspace (position servo) and force subspace (force servo), each with its own ζ.  Lec 2 pp. 42–54 (servo laws pp. 47–48, 53–54).
- **Wheel constraints** (α, l locate the wheel; β is the wheel-plane angle):
  rolling `[sin(α+β)  −cos(α+β)  −l cos β] R(θ) ξ̇_I − r φ̇ = 0`;
  sliding `[cos(α+β)  sin(α+β)  l sin β] R(θ) ξ̇_I = 0`;
  steered: β = β(t); castor: sliding gains `+ d β̇`.  Lec 3 pp. 23–30; Week 7 review sheet.
  Stack into `J1(β) R(θ) ξ̇_I − J2 φ̇ = 0` and `C1(β) R(θ) ξ̇_I = 0`.  Lec 3 pp. 37–39.
- **Homography**: four coplanar points seen in both images, **no three collinear**; scaled `H_n = H/h33`; chain `K ∝ H G`.  HGQ Lec 3 pp. 31–32.
- **Kalman (x_{k+1} = x_k)**: error recursion → `p_{k+1} = (1 − ΣL_i)² p_k + Σ L_i² σ_i²` → `L_i = p_k / (σ_i² (1 + p_k Σ 1/σ_j²))`, `1/p_{k+1} = 1/p_k + Σ 1/σ_i²`.  One shared gain for n sensors: `1/p_{k+1} = 1/p_k + n²/Σσ_i²` (never better).  HGQ Lec 4 pp. 26–29, 40–42.

Inferred, not a slide formula (mark as own derivation when used): stiffness mismatch k̂ ≠ k gives
`ë_f + ρk_vf ė_f + ρk_pf e_f = (1 − ρ) f̈_d` with ρ = k/k̂; an undetected shift of x_e biases a force
computed from position by `k_e Δx_e`.

## Prep protocol (agreed 2026-11-20, same as EE6407)

| Step | Material | Mode |
|---|---|---|
| 1 | `final-primer.html` | Light primer, one card per slot, quick checks |
| 2 | `final-mock-a-guided.html` | Full 5 × 20 paper as checked steps (Q1 reuses the 23-24 S2 arm) |
| 3 | Mock B (to build) | Cold, 3 h, handwritten; graded against a rubric |
| 4 | `final-mistakes.md` (to create) | Diagnose every lost mark, fresh variant until right |
| 5 | Mock C (to build) | Cold re-test on new numbers + the step-4 weak spots |
| 6 | Hard mock H (to build) | Cold; wider traps (no force sensor, x_e drift, stiffness matrix, castor wheels, grouped sensors) |
| 7 | Official **2025-26 S1** | Cold under exam conditions; graded, retrained |
| 8 | Official **2025-26 S2** | Dress rehearsal, then a final re-test from the mistakes log |

The 2023-24 S2 and 2024-25 papers are the spare pool for retrain drills; no mock reuses their numbers
(Q1 of mock A reuses only the 23-24 S2 arm figure already solved in `quizzes/quiz-01/quiz-01-mock-05.md`).
Shortened route if time runs out: steps 1, 3, 4, 7.

## Unresolved

- Exam date, time, venue; whether a calculator is allowed (the papers need one for √ and trig).
