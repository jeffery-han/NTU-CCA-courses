# EE-6221 final: mistakes log

One row per lost mark.  An item stays open until a fresh-variant retry is right.  Full grading: the "Your attempt" box under Q1 in `final-mock-a-guided.html`.

| # | Paper, Q | What was written | Why wrong | Rule | Retry |
|---|---|---|---|---|---|
| 1 | Mock A Q1(b) row 4 | a4 = 0; frame 4 placed at q4 | z4 must lie on the q5 axis; the 0.17 m common normal q4→q5 is a4 | Tick each figure dimension into exactly one d/a cell (count before finishing) | closed 2026-11-25 (2024-25 S2 Q1 right) |
| 2 | Mock A Q1(b) rows 5–6 | d5 = 0.2, row 6 blank | 0.05 m raise along z4 is d5; 0.20 m along z5 is d6 | Same rule; 6 joints = 6 rows | closed 2026-11-25 (2024-25 S2 Q1 right) |
| 3 | Mock A Q1(b) α4, α5 | α4 = −90°, α5 = 0 | z4 ⟂ z5 forces ±90°; signs must reproduce the drawn z (α4 = +90°, α5 = −90° on own frames) | Perpendicular consecutive z ⇒ α = ±90°, never 0 | closed 2026-11-25 (2024-25 S2 Q1 right) |
| 4 | Mock A Q1(a) y axes | y0, y1, y2, y4 reversed (↗ read as into page) | y = z × x; drawing and table disagree on which way is out of page | Check y = z × x on every frame | closed 2026-11-26 (Mock B Q1: all seven y drawn, all right-handed) |
| 5 | Mock A Q1(b) θ column | numbers only (90°, −90°…) | θ must be marked as the joint variable | Write θk = qk | closed 2026-11-25 (2024-25 S2 Q1 right) |
| — | Mock A Q1(b) T01, T12, T23 | blank | not attempted (blank, not wrong) | — | closed 2026-11-25 (2024-25 S2 Q1 right) |
| 6 | Mock B Q1(b) T23 | first column (−S3, −C3), third column (C3, −S3) | θ = θ3 − 90° gives cos = +S3, sin = −C3, so T23 = [S3 0 C3; −C3 0 S3; 0 −1 0] | Shift identities: cos(θ−90°) = sin θ, sin(θ−90°) = −cos θ; check one entry at θ3 = 90° | open |
| 7 | Mock B Q2(a) gains | ωn = 0.5 × 2 = 1 "Hz", kp = 1, kv = 2.2 | 2 Hz = 2·2π = 12.566 rad/s; ωn = 6.2832, kp = 39.478, kv = 13.823 | Resonance in Hz → multiply by 2π before halving | open |
| 8 | Mock B Q2(a) v, u1 | v = q̈; u1 not computed | v = q̈d + kv ė + kp e is the servo; u1 = 7.568 | Write v in full, then plug numbers into αv + β | open |
| 9 | Mock B Q2(b), (c) | blank (not wrong) | hybrid force/position control and force-subspace disturbance not yet understood | Relearn: subspaces, force servo with 1/ke, disturbance → e_ss = ke d/(m kpf) | open |
| 10 | Mock B Q3(a) l | l = √(0.2² − 0.15²) = 0.132 | distance from P is Pythagoras with a plus: √(0.04 + 0.0225) = 0.25 | l = √(x² + y²) | open |
| 11 | Mock B Q3(a) α | α = atan2(2, −1.5) = 4.428 rad | α = atan2(y, x) of the wheel position = atan2(0.15, −0.2) = 143.13° | atan2(y, x), y first; check the quadrant | open |
| 12 | Mock B Q3(a) β | β = 2.857 rad | rolling direction α + β − 90° = 0 (along +X_R), so β = 90° − α = −53.13° | Set the rolling direction, then solve for β | open |
| 13 | Mock B Q3(a) rows | rolling [cos, −sin, l cosβ], sliding [sin, −cos, l sinβ]; no R(θ) | rolling [sin(α+β), −cos(α+β), −l cosβ], sliding [cos(α+β), sin(α+β), l sinβ], acting on R(θ)ξ̇_I | Sliding = axle (cos, sin, +l sin); rolling = turned −90° (sin, −cos, −l cos); sanity check fixed wheel: [1, 0, −y], [0, 1, x] | open |
| 14 | Mock B Q3(a)(iii), Q3(b), Q4, Q5 | blank (not wrong) | equations not held in memory: speeds from rows, w/V/IK, homography rows and group count, Kalman derivation | Rebuild each from its picture (relearn Q2–Q5 Parts 6–10), then Mock C | open |
