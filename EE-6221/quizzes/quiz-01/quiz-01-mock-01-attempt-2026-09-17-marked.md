# EE6221 Quiz 1 — Mock 1, marked attempt (2026-09-17)

**Script:** `attempts/quiz-01-mock-01-2026-09-17.pdf` (2 pages, handwritten, scanned).
**Marked against:** `quiz-01-mock-01.md` (rubric, 20 core + 5 predicted = 25).

## Result

| Part | Marks | Score |
|---|---:|---:|
| Q1(a) frame assignment | 4 | **3** |
| Q1(b) D–H parameter table | 3 | **1** |
| Q1(c) link transforms | 3 | **2** |
| Q1(d) arm matrix + check | 2 | **0** |
| **Q1 subtotal** | **12** | **6** |
| Q2(a) pick pose | 4 | **3** |
| Q2(b) place pose | 3 | **3** |
| Q2 orthonormality check | 1 | **0** |
| **Q2 subtotal** | **8** | **6** |
| **Core total** | **20** | **12** |
| C1 tool configuration vector | 2 | **1** |
| C2 inverse kinematics | 3 | **2** |
| **Grand total** | **25** | **15** |

Core 12/20 (60%). Two of the three marks lost in Q1(d) are **blank, not wrong** — the part
was started (`⁰T_tool = ⁰T₁ ¹T₂ ²T₃`) and abandoned before multiplying out.

## The headline finding: a joint went missing from the table

The submitted D–H table is

| k | θ_k | d_k | a_k | α_k |
|---|---|---|---|---|
| 1 | 0 | d₂ | 0 | 0 |
| 2 | π/2 | d₃ | 0 | π/2 |
| 3 | 0 | L_t | 0 | 0 |

Three rows, but the wrong three. The arm has **three joints** — revolute θ₁ about the column,
prismatic d₂ up the column, prismatic d₃ radially out — plus a **rigid tool** of length L_t.
The table models d₂, d₃ and L_t, and the revolute θ₁ appears nowhere.

This is not a gap in understanding the arm. The diagram *does* mark θ₀₁ as a rotation about z₀,
and Section C uses θ₁ correctly throughout. The error is in the table-construction rule: rows were
allocated **one per visible offset** rather than **one per joint**, and the fixed tool offset was
promoted into a joint row, displacing joint 1.

The rule: a D–H table has exactly one row per **joint**. A rigid tool is not a joint — it is either
a post-multiplied `Trans(z, L_t)` (what the key does) or an explicitly labelled extra *fixed* frame
appended after the last joint row. Never a substitute for one.

Consequence: the chain has two variables where the arm has three, so it cannot reach a general
cylindrical point — yet Section C's own answer needs θ₁. That internal contradiction is the cheapest
possible self-check: **count the starred variables and compare with the number of joints in the
figure** before going on.

## Part-by-part

### Q1(a) frame assignment — 3/4

Earned:
- z₀ and z₁ vertical along the column with z₁ ∥ z₀. ✓
- z₂ and z₃ horizontal along the radial reach, with the z₁→z₂ change carried as a ±90° twist. ✓
- All three axes drawn at every frame, so y_k = z_k × x_k is at least implied. ✓

Lost: the joint variables are never starred or circled, and the diagram's own labels (d₁ vertical,
d₂ horizontal) contradict the table's (d₂, d₃). Frame 3 is drawn over several times and its axis
directions can't be read with confidence. In a 30-minute paper the diagram is what the table gets
marked against — keep it legible and label it once, consistently.

### Q1(b) D–H parameter table — 1/3

- Row for the missing revolute: **0**. See above.
- Twist row: **1**. The ±90° twist is present and correct — this is the checkpoint the rubric calls
  "the crux of the question", and it was not missed.
- Tool/last row: **0**. `L_t` occupies a joint row; variables unmarked.

### Q1(c) link transforms — 2/3

- `⁰T₁ = [I | (0, d₂, 0)ᵀ]`: **0**. Under the submitted row 1 (θ=0, d=d₂, α=0) the template gives
  translation `(0, 0, d₂)` — along **z**, not y. `Trans(z, d)` puts d in the third slot of p, always.
- `¹T₂ = R_z(π/2) · Trans_z(d₃) · [Trans_x(0)] · R_x(−π/2)`: **1 method mark**, for reproducing the
  Schilling operator order Rot(z,θ)→Trans(z,d)→Trans(x,a)→Rot(x,α) exactly. But the table says
  α₂ = **+**π/2 while this line writes R_x(**−**π/2). One of the two is wrong and the script doesn't
  say which. A contradiction between the table and the transform is worth more marks than either
  error alone, because the examiner cannot award the benefit of the doubt.
- `²T₃ = Trans_z(L_t)`: **1**. Correct for the submitted row 3.

### Q1(d) arm matrix and check — 0/2

`⁰T_tool = ⁰T₁ ¹T₂ ²T₃` is the **correct order** — base-to-tool reads left to right, and reversing
it is the classic error. But the product was never formed, so there is no p, no R, and no
orthonormality check. Both marks are unearned; treat this as *ran out of time*, not *didn't know*.

### Q2(a) pick pose — 3/4

Submitted:

```
⁰T_pick = [ 0  1  0 | 4 ]
          [ 1  0  0 | 8 ]
          [ 0  0 -1 | ? ]
          [ 0  0  0 | 1 ]
```

- Approach `r₃ = (0,0,−1)`, down onto the part: **1**. ✓
- Closing direction `r₂ = (1,0,0)`: **0**. Part C's long axis lies along x₀, so its two long faces
  are separated along **y₀** — the jaws must close along y₀, giving `r₂ = (0,1,0)`. "Grasp the long
  sides" names the faces the jaws touch, not the direction they move. The gripper as submitted would
  close along the part's length and hit its short ends.
- Right-handed orthonormal set: **1**. `r₁ × r₂ = (0,1,0) × (1,0,0) = (0,0,−1) = r₃` ✓ and
  det R = +1, so this is a genuine rotation, not a reflection — just the wrong one for the task.
- Translation: **1**, conditionally. x,y = (4,8) is correct. The z entry is overwritten several times
  and I cannot read it; the correct value is **2** (part C's centroid height). Awarded on the
  assumption it resolves to 2 — say if it doesn't.

### Q2(b) place pose — 3/3

```
⁰T_place = [ 0  1  0 | 9 ]
           [ 1  0  0 | 3 ]
           [ 0  0 -1 | 4 ]
           [ 0  0  0 | 1 ]
```

All three checkpoints: orientation carried over from the pick, (x,y) = D's centroid (9,3), and
z = **4**. The height is the trap the rubric flags — D's top surface sits at 1 + 1 = 2, and C's own
half-height adds another 2. Both half-heights were added. Full marks.

### Q2 orthonormality check — 0/1

The script has `3   yeah.` (reading uncertain) where the explicit check belongs. The mark needs
`RᵀR = I` and `det R = +1` written down. One line, and it catches most sign errors for free.

### C1 tool configuration vector — 1/2

Submitted `w = [ (d₃+L_t)cosθ₁, (d₃+L_t)sinθ₁, d₂, e^{θ₁/π}cosθ₁, e^{θ₁/π}sinθ₁, 0 ]ᵀ`.

- Structure `[p ; e^{·}r₃]` with the correct p and the correct approach vector
  `r₃ = (cosθ₁, sinθ₁, 0)` for the chosen frames: **1**. ✓
- The exponent: **0**. The scale factor is `e^{q_n/π}` where `q_n` is the **tool roll angle** — the
  rotation *about the approach vector* (`lecture-01-manipulator-kinematics.pdf`, pp. 92–93: "the roll
  angle represents a rotation about the approach vector"). It is not θ₁, which rotates the whole arm
  about the base column and changes the approach *direction* rather than rolling about it. This arm
  has no roll degree of freedom at all, so `q_n = 0`,
  `e^{q_n/π} = 1`, and the lower half is just `r₃` with unit norm. The consistency check is built in:
  `q_n = π ln‖w₄₋₆‖`, so `‖w₄₋₆‖` must come out as `e^{q_n/π}`. As submitted `‖w₄₋₆‖ = e^{θ₁/π}`,
  which would decode to a tool roll of θ₁ that the arm physically cannot produce.

Note: the p written here is consistent with the α₂ = **+**π/2 frame choice, which the key explicitly
allows as equally correct. Section C is marked against that choice throughout, not against the key's
α₂ = −π/2 variant.

### C2 inverse kinematics — 2/3

`θ₁ = atan2(y, x)`, `d₂ = z`, `d₃ = √(x²+y²) − L_t`.

- Radial equation and `d₂ = z`: **1** ✓
- **atan2, not arctan**: **1** ✓ — quadrant preserved, and it survives y = 0. This is the checkpoint
  most people lose.
- Feasibility and uniqueness: **0**. Nothing stated. The answer needs `d₃ ≥ 0`
  (i.e. `√(x²+y²) ≥ L_t`), z within the column stroke, and the observation that the solution is
  **unique** — one revolute joint, no 2R sub-chain, so no elbow-up/elbow-down branch.

Algebraically the three expressions are exactly right for the chosen frames. Verified by
substitution: L_t = 1, target (0, 3, 5) → θ₁ = atan2(3,0) = 90°, d₂ = 5, d₃ = 3 − 1 = 2; forward
gives x = (2+1)cos90° = 0 ✓, y = (2+1)sin90° = 3 ✓, z = 5 ✓.

## Slips vs. inverted concepts

**Inverted concepts** (these need the notes, and are folded in at stage 6):
1. A D–H row belongs to a **joint**, not to an offset; a rigid tool is appended, never substituted.
2. `r₂` is perpendicular to the faces being grasped, not along them.
3. The tool-configuration exponent carries the **tool roll angle** (rotation about the approach
   vector), not the base joint angle.
4. An IK answer is unfinished without a feasibility and uniqueness statement.

**Slips** (execution, not understanding):
5. `Trans(z, d₂)` written into the y slot of p.
6. Table α₂ = +π/2 vs transform R_x(−π/2) — pick one and keep it.

**Blank, not wrong:** Q1(d)'s product and read-off, and the Q2 orthonormality line.

## Unmatched item

Page 1 opens with a line numbered `1.` reading approximately *"path is then a straight or curved
line in-between 2 pos, no time involved b..."* — a correct statement of path vs trajectory (a path
is the geometric locus; a trajectory adds the timing), but it answers no question on this mock.
Recorded here rather than graded; confirm whether it was a pre-exam memory dump or an answer to
something else.

## Confidence

All marks above are **derivable** — every answer was re-derived independently from the arm
definition and checked numerically. Two readability caveats, both flagged in place: the z entry of
`⁰T_pick` and the `3 yeah.` line.
