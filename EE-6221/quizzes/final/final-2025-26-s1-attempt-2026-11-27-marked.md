# EE-6221 · Official 2025–26 S1 final · attempt 2026-11-27 · marked

Scans: `attempts/final-2025-26-s1-q{2,3,4,5}-2026-11-27.jpg` (Q1 not sat / not uploaded; Q3 photo uploaded twice).
Key: `ntu-only/final-2025-26-s1.md`.

## Marks summary (Q2–Q5 attempted)

| Q | Part | Marks | Status | Confidence |
|---|---|---:|---|---|
| Q1 | (a)–(b) | — / 20 | not attempted | — |
| Q2 | (a) Computed torque (`ζ = 1.25`) | 8 / 9 | minor slip (`β_1` sign) | derivable |
| Q2 | (b) Hybrid control + disturbances | 7 / 11 | `d_1, d_2` in `β'`; `d/m` instead of `α_m⁻¹ d` | derivable |
| Q3 | (a) Mobile robot constraints | 4 / 8 | `cos α` sign, swapped `x/y` in cols 3, cm vs m | derivable |
| Q3 | (b)(i) Forward kinematics | 4 / 4 | full marks | derivable |
| Q3 | (b)(ii) Analytic IK | 3.5 / 4 | `cos C_2` slip | derivable |
| Q3 | (b)(iii) Numerical IK | 0 / 4 | blank (skipped) | derivable |
| Q4 | (a) `G_n` count + derivation | 4 / 10 | count 20 (not 18); `{1,2,8,9}` invalid; row cols 7–8 swapped | derivable |
| Q4 | (b) `H_n` count | 1 / 4 | count 4 (not 6) | derivable |
| Q4 | (c) `M_n` via chaining | 5.5 / 6 | `F_p F_q` typo for `F_p F_d` | derivable |
| Q5 | (a) Group 1 Kalman gains | 2 / 6 | `−Σ L_i² σ_i²` sign; dropped `p_k` in `∂p/∂L_i`; unfinished | derivable |
| Q5 | (b) Group 2 Kalman gains | 0 / 8 | blank | derivable |
| Q5 | (c) Comparison | 0 / 6 | blank | derivable |
| **Total (Q2–Q5)** | | **39 / 80** | **18 marks blank** (`Q3(b)(iii)`, `Q5(b),(c)`) | |

---

## Transcription and verdicts

### Q2 (15 / 20)
- **(a) (8/9)**: `α = [[2,1,0],[1,1,0],[0,0,10]]`, `β = [(2q̇_1²+q̇_1q̇_2)sin q_2 + 7 cos q_1 + 20 cos(q_1+q_2); q̇_1² sin q_2 + 10 cos(q_1+q_2); 3 q̇_3 + 100]`, `u = αv + β`, `v = q̈_d + k_v ė + k_p e`, `ω_n = 4 rad/s`, `k_p = 16`, `k_v = 10`.
  - Verdict: Right method, gains, and servo (closes Mistake #8). Lost 1 mark for missing leading minus sign on `β_1` and not stating diagonal `K_p, K_v` / error equation.
- **(b) (7/11)**: `α' = α`, `β' = β + [d_1, d_2, 25(q_3 - 0.2)]^T`; motion `u_1, u_2`: `ω_n = 4, k_p = 16, k_v = 8.4`; force `u_3`: `v_f = (1/25)(f̈_d + k_vf ė_f + k_pf e_f)`, `k_pf = 16, k_vf = 8`; error equations: `ë_i + k_v ė + k_p e = d/m` and `ë_f + k_vf ė_f + k_pf e_f = 0`.
  - Verdict: Subspace split, `1/25` force servo, separate gains, and force error `= 0` are all right (closes Mistake #9). Lost 1 mark for putting unknown `d_1, d_2` inside `β'` (new Mistake #16) and 3 marks for writing `d/m` instead of keeping `α_m = [[2,1],[1,1]]` and inverting to `ë_1 + 8.4 ė_1 + 16 e_1 = d_1 - d_2` and `ë_2 + 8.4 ė_2 + 16 e_2 = -d_1 + 2 d_2` (Mistake #15 remains open).

### Q3 (11.5 / 20)
- **(a) (4/8)**: `y_1 = 25, y_2 = -25, x_1 = x_2 = -10`; `sin α_1 = 0.928, sin α_2 = -0.928, cos α_2 = cos α_1 = 0.371`; `α_3 = 0`, `β_1 = 90° - α_1, β_2 = 90° - α_2`; `J = [[1,0,10],[1,0,10],[sin β_3,-cos β_3,-22 cos β_3]]`, `C = [[0,1,25],[0,1,25],[cos β_3,sin β_3,22 sin β_3]]`; `J R_θ ξ - r φ̇ = 0`, `C R_θ ξ = 0`.
  - Verdict: Coordinates and `(l, α, β)` setup close Mistakes #10–#12, and row trigonometric forms are right. Lost 4 marks for: `cos α = +0.371` instead of `-0.371` (quadrants II/III), swapping `x` and `y` in the 3rd columns of `J` (`[-0.25, +0.25]`) and `C` (`[-0.10, -0.10]`), leaving lengths in cm instead of m, scalar `r` instead of `J_2 = diag(0.04, 0.04, 0.03)`, and omitting `R(θ)` (Mistake #13 remains open).
- **(b) (7.5/12)**:
  - (i) 4/4: `T^tool_base` multiplied completely and accurately.
  - (ii) 3.5/4: `q_1 = atan2(y-0.05, x-0.05)`, `q_2 = atan2(√((y-0.05)²+(x-0.05)²), z)`, `q_3 = z / cos C_2 - 0.3` (minor slip `cos C_2` for `cos q_2`).
  - (iii) 0/4: blank (`Skipped calcu`). Correct values: `q_3 = 0.4071 m`, `q_1 = 0.9273 rad`, `q_2 = 0.7854 rad (45°)`.

### Q4 (10.5 / 20)
- **(a) (4/10)**: `C^7_4 - 4(7-3) + 1 = 20`; chose `{1, 2, 8, 9}`; matrix rows `[a_xi, a_yi, 1, 0, 0, 0, -a_xi b_xi, -a_xi b_yi]` and `[0, 0, 0, a_xi, a_yi, 1, -a_yi b_xi, -a_yi b_yi]`.
  - Verdict: Correct count is `C(3,2)×C(4,2) = 18` (missed Line 1 `{O_1,O_2,O_3}`); `{O_8, O_9}` are not in `F_p`; entries (1,8) and (2,7) are swapped (`-a_yi b_xi` in row 1, `-a_xi b_yi` in row 2). New Mistake #17 & #18.
- **(b) (1/4)**: `C^6_4 - 4(6-3) + 1 = 4`. Correct count is `C(4,2)×C(2,2) = 6` (`4(6-3)` over-subtracted the 4-on-L2 group 4 times).
- **(c) (5.5/6)**: Direct impossible (`4–7` collinear), chain `H_n G_n / (H_n G_n)_33` works. Tiny slip `F_p F_q` instead of `F_p F_d`.

### Q5 (2 / 20)
- **(a) (2/6)**: Correct error recursion `x̃_{k+1} = (1 - L_1 - L_2) x̃_k - L_1 v_1 - L_2 v_2`. Then wrote `p_{k+1} = C² p_k - Σ L_i² σ_i²` (wrong minus sign) and `∂p_{k+1}/∂L_i = -2(1 - Σ L_i) - 2 σ_i² L_i = 0` (dropped `p_k`), stalled before solving. New Mistake #19.
- **(b) (0/8)**, **(c) (0/6)**: blank.

## Mistakes log updates
- Closed: **#8**, **#9**, **#10**, **#11**, **#12**.
- Still open: **#6**, **#7**, **#13**, **#14**, **#15**.
- Opened: **#16** (`d` put inside `β`), **#17** (homography counting by inclusion-exclusion instead of line-split), **#18** (homography row entries `-a_y b_x` / `-a_x b_y` swapped), **#19** (Kalman variance `+ Σ L_i² σ_i²` and keeping `p_k` in `∂p/∂L_i`).
