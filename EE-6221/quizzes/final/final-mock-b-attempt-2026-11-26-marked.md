# EE6221 final · Mock B, marked attempt (2026-11-26)

**Scripts:** `attempts/final-mock-b-q1-2026-11-26.jpg`, `-q2-…`, `-q3-…` (handwritten, photographed).
**Marked against:** `final-mock-b.md` (rubric per question).  Q4–Q5 not attempted (the picture understood, the equations not held).

## Result

| Part | Marks | Score |
|---|---:|---:|
| Q1(a) frames: z 6, x/origins 2, y 2, tool 1 | 11 | **11** |
| Q1(b) rows | 6 | **6** |
| Q1(b) matrices | 3 | **2** |
| **Q1** | **20** | **19** |
| Q2(a) α 2, β 2, resonance 1/2, gains 1, error eq 1, u1 0 | 9 | **7** |
| Q2(b) hybrid force/position | 8 | **0** (blank) |
| Q2(c) disturbance in force subspace | 3 | **0** (blank) |
| **Q2** | **20** | **7** |
| Q3(a)(i) α, β, l | 3 | **0** |
| Q3(a)(ii) rows: structure 3, J2 1 | 4 | **2** (structure 1, J2 1) |
| Q3(a)(iii) speeds | 3 | **0** (blank) |
| Q3(b) arm w, V, IK | 10 | **0** (blank) |
| **Q3** | **20** | **2** |
| Q4, Q5 | 40 | not attempted |
| **Running total (Q1–Q3)** | **60** | **28** |

## Q1 · what was written

Arrows: ↗ = into page, ↙ = out of page.  z1, z2 drawn into the page (opposite to the key, allowed), so α1, α3, α4 = −90° and the θ3 offset is −90°.  All seven y axes drawn, all right-handed.  Frame 3 drawn displaced along a dashed line; the table (d3 = a3 = 0) puts it at the elbow, so accepted; write "O3 = O2" in the exam.

| k | θ | d (cm) | a (cm) | α |
|---|---|---|---|---|
| 1 | θ1 | 30 | 0 | −90° |
| 2 | θ2 | 0 | 25 | 0 |
| 3 | θ3 − 90° | 0 | 0 | −90° |
| 4 | −90° (fixed) | d4 | 0 | −90° |
| 5 | θ5 + 180° | 5 | 0 | −90° |
| 6 | θ6 | 12 | 0 | 0 |

Checked: forward kinematics of these rows at q = 0, d4 = 20 reproduces every drawn x, y, z and the tip (57, 35) cm.

```
T01 = [ C1  0 −S1  0 ]   T12 = [ C2 −S2  0  25C2 ]   T23 written = [ −S3  0  C3  0 ]
      [ S1  0  C1  0 ]         [ S2  C2  0  25S2 ]                 [ −C3  0 −S3  0 ]
      [  0 −1   0 30 ]         [  0   0  1   0   ]                 [   0 −1   0  0 ]
      [  0  0   0  1 ]         [  0   0  0   1   ]                 [   0  0   0  1 ]
```

**Lost mark: T23.**  θ = θ3 − 90° gives cos θ = +S3, sin θ = −C3, so

```
T23 = [  S3  0  C3  0 ]
      [ −C3  0  S3  0 ]
      [   0 −1   0  0 ]
      [   0  0   0  1 ]
```

Wrong signs at (1,1) and (2,3): a sign slip in the shift identity, not a concept gap.  Mistakes log #6.

(Top of the sheet also has scratch work for a block with a disturbance: m(ë + kv ė + kp e) = d.  Not graded.)

## Q2 · what was written

- α = [5+2C2, 1+C2, 0; 1+C2, 1, 0; 0, 0, 4]: right (2/2).
- β = [−S2(2q̇1q̇2 + q̇2²) + 3q̇1; S2 q̇1² + 9.8C12; 2q̇3 + 39.2]: right (2/2).
- u = αv + β, with **v = q̈**.  This should be the servo v = q̈d + kv ė + kp e.  Mistakes log #8.
- m(ë + kv ė + kp e) = d, e_ss = d/(m kp): error equation right (1/1).
- ω = 2/2 = 1 "Hz", kp = ω² = 1, kv = 2ωζ = 2.2.  The lowest resonance and the 0.5 factor are right, but the 2π is missing (resonance 1/2).  Correct: 2 Hz = 12.566 rad/s, ωn = 6.2832, kp = 39.478, kv = 13.823.  Gains get 1/1 as follow-through.  Mistakes log #7.
- u1 not computed (0/1).  Correct: v1 = 0.5916, v2 = 0.1016, u1 = 7.568.
- (b), (c): blank.  Out of knowledge, not out of time: hybrid force/position control had not been learned yet.  Mistakes log #9.

## Q3 · what was written

(a)(i), wheels A and B (C not done):
- l = √(0.2² − 0.15²) = 0.132.  Should be √(0.2² + 0.15²) = 0.25.  Mistakes log #10.
- α_A = atan2(2, −1.5) = 4.428 rad, α_B = −4.428 rad.  The arguments are swapped and the lengths are wrong; should be atan2(0.15, −0.2) = 143.13°.  Mistakes log #11.
- β = α − π/2 = 2.857 rad, β_B = −2.857.  Should be β = 90° − α = −53.13°, because the rolling direction is +X_R.  Mistakes log #12.

(a)(ii), rows written per wheel (β_C kept symbolic, rφ̇ on the right: structure 1, J2 1):
- rolling: [cos(α+β), −sin(α+β), l cos β] ξ̇ = rφ̇
- sliding: [sin(α+β), −cos(α+β), l sin β] ξ̇ = 0
- No R(θ).  Correct: rolling [sin(α+β), −cos(α+β), −l cos β], sliding [cos(α+β), sin(α+β), l sin β], both acting on R(θ)ξ̇_I.  Sanity check: a fixed wheel gives [1, 0, −y] and [0, 1, x].  Mistakes log #13.

(a)(iii) and (b): blank, out of knowledge.  Mistakes log #14.

## What to retry

Open items #6–14 in `final-mistakes.md`.  Relearn page: `final-relearn-q2-q5.html`, then `final-mock-c.html` cold.
