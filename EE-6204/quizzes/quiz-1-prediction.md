# EE6204 Quiz 1 — prediction & practice paper (answer key + marking rubric)

**Status: unofficial.** Written 2026-09-02 from `quiz-1-intel.md` (小红书 recollections of the
Feb 2026 / Sep 2025 sittings), `../notes/beginner-notes.tex`, `../notes/notes.tex`, and the
Week 1–2 lecture transcripts. It is **not** a real paper and **not** an official marking scheme.
Every number below was derived and checked here.

- **Interactive version:** `quiz-1-prediction.html` — deliberately contains **no answers**. Sit it
  closed-book, on paper, in 30 minutes, then either read this file or paste the exported answer
  sheet into Claude Code for per-mistake grading. Reading this file first wastes the exercise.
- **Format mirrored (current run, Prof. Su Rong):** Q1 = LP formulation, Q2 = simplex on the same
  LP. **16 marks, 30 minutes**, handwritten. Maximization, all `≤` constraints, slack variables
  only. Objective row written as `z − cᵀx = 0`; optimal when every bottom-row entry is `≥ 0`.
- **Predicted unseen item** (Section S, *not* part of the 16): a sensitivity/duality extension on
  the same LP. In-scope, lecturer-flagged, absent from the circulating recollection.
- **Legacy block** (Section L): transportation + constrained NLP — the *previous* lecturer's
  format through Sep 2025. Lower probability for the current run; included so a format reversion
  does not catch you cold.

---

## The problem (Q1 + Q2 share it)

> A workshop assembles two loudspeaker models, **Standard** and **Premium**. Each Standard sold
> earns **\$40** profit, each Premium **\$30**. Every unit of either model needs **1 hour** at the
> shared **assembly** bench; **12** assembly-hours are available this week. **Testing** takes
> **2 hours** per Standard and **1 hour** per Premium; the test rig has **16** hours available.
> All output is sold. How many of each model should be built this week to maximise profit, and
> what is that profit?

---

## Q1 — Formulation (5 marks)

**Decision variables.** Let `x₁` = number of Standard units built this week, `x₂` = number of
Premium units built this week (`x₁, x₂ ≥ 0`; treat as continuous unless integrality is asked).

**Model.**
```
maximise    z = 40 x₁ + 30 x₂            (profit, $)
subject to      x₁ +   x₂ ≤ 12           (assembly hours)
              2 x₁ +   x₂ ≤ 16           (test-rig hours)
                x₁ ,     x₂ ≥ 0
```

**Standard form for the simplex method** (add one slack per `≤` row; RHS already `≥ 0`):
```
maximise z ;   z − 40 x₁ − 30 x₂ = 0
    x₁ +   x₂ + s₁       = 12
  2 x₁ +   x₂       + s₂ = 16
    x₁, x₂, s₁, s₂ ≥ 0
```
`s₁` = unused assembly hours, `s₂` = unused test-rig hours.

### Q1 rubric — 5 marks

| # | Checkpoint | Marks |
|---|---|---:|
| 1a | Both variables defined **with units / meaning** ("number of … per week"), not just "let x, y be the speakers" | 1 |
| 1b | Objective `= 40x₁ + 30x₂` **and** "maximise" stated explicitly | 1 |
| 1c | Assembly constraint `x₁ + x₂ ≤ 12` | 1 |
| 1d | Testing constraint `2x₁ + x₂ ≤ 16` | 1 |
| 1e | Non-negativity **and** conversion to standard form (slacks added, objective row `z − cᵀx = 0`) | 1 |

**Common wrong paths.**
- *Objective swapped with a constraint* ("maximise `x₁ + x₂` s.t. `40x₁ + 30x₂ ≤ …`") — the value
  being maximised is profit; hours are the limits. −2 (1b + one constraint).
- *`2x₂` instead of `x₂` in the test row* — misreading "2 hours per **Standard**". −1 (1d).
- *`≥` instead of `≤`* — "available" is an upper bound. −1 per row.
- *Forgetting `s₁, s₂` or writing `z + cᵀx`* — the sign of the objective row drives every entering
  decision in Q2. −1 (1e), and it usually propagates into Q2.
- *Adding `x₁, x₂ ∈ ℤ`* unprompted — not wrong as a remark, but then it is an integer LP and the
  simplex tableau no longer gives the final answer directly. No penalty if flagged; note it.

---

## Q2 — Simplex method (11 marks)

Convention (Prof. Su Rong, from `week-02-transcript.txt`): bottom row holds `z − cᵀx`, i.e. the
**negatives** of the objective coefficients; a maximization is optimal when **every bottom-row
entry is `≥ 0`**; entering variable = any negative bottom-row entry (most negative is a convenient
default, not required); leaving variable = **minimum non-negative ratio** `bᵢ / aᵢⱼ` over rows with
`aᵢⱼ > 0` (this keeps the RHS column `≥ 0`).

### Tableau 0 — initial BFS `x₁ = x₂ = 0`, `s₁ = 12`, `s₂ = 16`, `z = 0`

| basis | x₁ | x₂ | s₁ | s₂ | RHS |
|---|---:|---:|---:|---:|---:|
| s₁ | 1 | 1 | 1 | 0 | 12 |
| s₂ | **2** | 1 | 0 | 1 | 16 |
| z  | −40 | −30 | 0 | 0 | 0 |

Entering: `x₁` (bottom row −40 is negative). Ratios: `12/1 = 12`, `16/2 = 8` → **min is 8**, row
`s₂` leaves. Pivot on the `2`.

### Tableau 1 — `x₁` enters, `s₂` leaves

Pivot row ÷ 2, then eliminate the `x₁` column elsewhere (`R_{s₁} ← R_{s₁} − R_{x₁}`,
`R_z ← R_z + 40·R_{x₁}`):

| basis | x₁ | x₂ | s₁ | s₂ | RHS |
|---|---:|---:|---:|---:|---:|
| s₁ | 0 | **0.5** | 1 | −0.5 | 4 |
| x₁ | 1 | 0.5 | 0 | 0.5 | 8 |
| z  | 0 | −10 | 0 | 20 | 320 |

BFS: `x₁ = 8`, `x₂ = 0`, `z = 320`. Bottom row still has `−10` under `x₂` → not optimal.
Entering: `x₂`. Ratios: `4 / 0.5 = 8`, `8 / 0.5 = 16` → **min is 8**, row `s₁` leaves. Pivot on `0.5`.

### Tableau 2 — `x₂` enters, `s₁` leaves

Pivot row ÷ 0.5, then eliminate the `x₂` column (`R_{x₁} ← R_{x₁} − 0.5·R_{x₂}`,
`R_z ← R_z + 10·R_{x₂}`):

| basis | x₁ | x₂ | s₁ | s₂ | RHS |
|---|---:|---:|---:|---:|---:|
| x₂ | 0 | 1 | 2 | −1 | 8 |
| x₁ | 1 | 0 | −1 | 1 | 4 |
| z  | 0 | 0 | **20** | **10** | **400** |

Every bottom-row entry is `≥ 0` → **optimal**.

### Answer

- **`x₁* = 4` Standard, `x₂* = 8` Premium, `z* = $400`.**
- `s₁* = 0`, `s₂* = 0` → **both** constraints binding (all 12 assembly hours and all 16 test-rig
  hours are used).
- Two pivot iterations, as the recollection ("matrix transformed twice") predicts.

### Graphical check (the recollection says you can verify this way)

Corners of the feasible region: `(0,0) → 0`, `(8,0) → 320`, `(0,12) → 360`, and the intersection
of `x₁ + x₂ = 12` with `2x₁ + x₂ = 16`, which is `(4,8) → 40·4 + 30·8 = 400`. Maximum at `(4,8)`,
confirming the tableau.

### Q2 rubric — 11 marks

| # | Checkpoint | Marks |
|---|---|---:|
| 2a | Tableau 0 correct: slack basis, RHS = (12, 16), objective row = `(−40, −30, 0, 0 \| 0)` | 2 |
| 2b | Iteration 1: names a **negative** bottom-row entry to enter **and** uses the **minimum-ratio** test to pick the leaving row (8, not 12) | 2 |
| 2c | Iteration 1 pivot arithmetic gives Tableau 1 (or an equivalent correct tableau) | 2 |
| 2d | Iteration 2: entering `x₂`, leaving `s₁` by minimum ratio; pivot arithmetic gives Tableau 2 | 3 |
| 2e | States the optimality test ("all bottom-row entries `≥ 0`") and reads off `x* = (4, 8)`, `z* = 400` | 1 |
| 2f | Reports `s₁ = s₂ = 0` / both constraints binding, **or** a correct graphical verification | 1 |

Method marks: award 2b–2d for the right procedure even if one arithmetic slip carries through, as
long as the entering/leaving **rules** are applied correctly. Note which checkpoint the marks came
from.

**Common wrong paths and what each implies.**

| Symptom | Likely cause | Fix |
|---|---|---|
| Enters the variable with the **most positive** bottom-row entry | Confusing the `z − cᵀx` row (negatives) with a `cⱼ − zⱼ` row (positives) | With `z − cᵀx = 0`, improvement is signalled by a **negative** entry; stop at all `≥ 0` |
| Picks the leaving row by the **largest** ratio, or ignores the ratio test | Forgot the ratio test's job — keeping RHS `≥ 0` | Always the **minimum non-negative** ratio, over `aᵢⱼ > 0` only |
| Divides by a negative or zero pivot-column entry in the ratio test | Included ineligible rows | Only rows with `aᵢⱼ > 0` take part |
| Gets `z*` = 360 at `(0, 12)` and stops | Stopped after one pivot / read the wrong corner | Check the bottom row: `−10` under `x₂` still allows improvement |
| Optimal `z` but wrong slacks (e.g. `s₁ = 4`) | Read slack values from Tableau 1 instead of Tableau 2 | Slacks are nonbasic (`= 0`) in the final tableau here |
| "Unbounded" | Ratio test found no eligible row because of a sign error in the pivot | Re-check the pivot arithmetic; this LP is bounded |
| Runs Big-M / two-phase | Treated `≤` rows as needing artificials | `≤` with RHS `≥ 0` in a maximization needs slack only |

---

## Section S — predicted unseen item: sensitivity & duality (8 marks practice, *not* in the 16)

Same LP, same optimal tableau. The Week 2 transcript shows Prof. Su Rong perturbing a cost
coefficient (`c₁ → c₁ + θ`) and an `A` entry while saying this is how you "operate … in a quiz or
in the final exam." Treat this as the most likely add-on.

### S1 — Shadow prices (2 marks)

Read directly off the **final** bottom row: the coefficient under `sᵢ` is the shadow price of
constraint `i`.
- Assembly (`s₁`): **\$20 per hour**.
- Test rig (`s₂`): **\$10 per hour**.
Meaning: within an allowable range, one extra assembly-hour raises optimal profit by \$20; one
extra test-rig hour by \$10.

### S2 — One more unit, and the dual check (2 marks)

- If assembly capacity rose from 12 to 13 hours, predicted new `z* = 400 + 20 = $420` (basis
  unchanged — see S3).
- **Dual:** `min 12 w₁ + 16 w₂` s.t. `w₁ + 2 w₂ ≥ 40`, `w₁ + w₂ ≥ 30`, `w ≥ 0`. At
  `(w₁, w₂) = (20, 10)` both dual constraints are **tight** (`40`, `30`) and
  `12·20 + 16·10 = 400` = primal optimum → strong duality confirmed. Complementary slackness:
  `x₁, x₂ > 0` forces both dual constraints tight; `s₁ = s₂ = 0` allows both `wᵢ > 0`.

### S3 — Right-hand-side ranging (3 marks)

From the final tableau, `B⁻¹` (columns of `s₁, s₂` in rows `x₂, x₁`) is
`[[2, −1], [−1, 1]]`, and `x_B = B⁻¹ b = (8, 4)` = `(x₂, x₁)`.

- **Assembly** `b₁ = 12 + Δ`: `x_B = (8 + 2Δ, 4 − Δ) ≥ 0` ⇒ `−4 ≤ Δ ≤ 4` ⇒
  **`b₁ ∈ [8, 16]`**. Over this range the basis stays optimal and each hour is worth \$20.
  Endpoints: `b₁ = 16 → (x₂, x₁) = (16, 0)`, `z = 480`; `b₁ = 8 → (0, 8)`, `z = 320`.
- **Test rig** `b₂ = 16 + Δ`: `x_B = (8 − Δ, 4 + Δ) ≥ 0` ⇒ `−4 ≤ Δ ≤ 8` ⇒ **`b₂ ∈ [12, 24]`**,
  each hour worth \$10.

### S4 — Objective-coefficient ranging (1 mark)

`c₁ = 40 + δ` with `x₁` basic (final `x₁` row `(1, 0, −1, 1 | 4)`). Adding `δ · (x₁ row)` to the
bottom row: `s₁` coefficient `→ 20 − δ`, `s₂` coefficient `→ 10 + δ`. Both `≥ 0` ⇒
**`−10 ≤ δ ≤ 20` ⇒ `c₁ ∈ [30, 60]`**. In this range the optimal basis and `x* = (4, 8)` are
unchanged; `z* = 400 + 4δ`. Outside it, re-optimise (pivot) rather than extrapolate.

### Section S rubric — 8 marks

| # | Checkpoint | Marks |
|---|---|---:|
| S1 | Both shadow prices read off the final bottom row (20, 10) with the correct constraint attached | 2 |
| S2 | Correct "+\$20" statement **and** a dual formed and value-checked to 400 | 2 |
| S3 | `B⁻¹` or the tableau columns used to get at least one RHS range with the `x_B ≥ 0` argument | 3 |
| S4 | `c₁` range `[30, 60]` by the "add `δ ·` basic row to the bottom row, keep `≥ 0`" argument | 1 |

**Wrong paths.** Quoting shadow prices with the constraints swapped (S1); extrapolating
`z = 400 + 20 Δ` for `Δ = 10` when the range only reaches `Δ = 4` (S3 — outside the range the
basis changes); using the *initial* tableau's `s`-columns for `B⁻¹` instead of the final one.

---

## Section L — legacy block (previous lecturer, through Sep 2025 — lower probability)

Do these only after the core paper. They are the transportation + NLP questions Prof. Su Rong
**removed**; they return only if the coordinator reverts the format.

### L1 — Balanced transportation (VAM + one optimality step)

> Three plants supply four depots. Supplies `(20, 30, 25)`; demands `(15, 20, 20, 20)`. Unit
> costs:
> ```
>        D1  D2  D3  D4
>  P1     8   6  10   9
>  P2     9  12  13   7
>  P3    14   9  16   5
> ```
> Balance the problem, build an initial BFS by **Vogel's Approximation Method**, then test
> optimality with `uᵢ + vⱼ = cᵢⱼ` / `cᵢⱼ − uᵢ − vⱼ` and, if needed, do one stepping-stone loop.

**Worked answer.** `Σsupply = 75`, `Σdemand = 75` → already balanced; no dummy.

VAM — each round: penalty of a line = (2nd-smallest cost) − (smallest cost) over its still-active
cells; pick the line with the **largest** penalty; allocate as much as possible to its
**cheapest** cell; cross out the exhausted row or column; repeat.

| Round | Largest penalty | Cell | Allocation | Exhausted |
|---|---|---|---:|---|
| 1 | P3 → 9 − 5 = 4 | P3–D4 (5) | 20 | D4; P3 left 5 |
| 2 | P3 → 14 − 9 = 5 | P3–D2 (9) | 5 | P3; D2 left 15 |
| 3 | D2 → 12 − 6 = 6 | P1–D2 (6) | 15 | D2; P1 left 5 |
| 4 | P2 → 13 − 9 = 4 | P2–D1 (9) | 15 | D1; P2 left 15 |
| 5 | (only D3 left) | P1–D3 (10), P2–D3 (13) | 5, 15 | P1, P2, D3 |

Initial BFS: `x₁₂ = 15, x₁₃ = 5, x₂₁ = 15, x₂₃ = 15, x₃₂ = 5, x₃₄ = 20` — **6 cells**
`= m + n − 1 = 3 + 4 − 1` ✓ (non-degenerate). Cost
`= 15·6 + 5·10 + 15·9 + 15·13 + 5·9 + 20·5 = 90 + 50 + 135 + 195 + 45 + 100 = 615`.

Optimality (MODI): set `u₁ = 0`; solve `uᵢ + vⱼ = cᵢⱼ` on the six basic cells →
`v₂ = 6, v₃ = 10, u₃ = 3, v₄ = 2, u₂ = 3, v₁ = 6`.
Reduced costs `cᵢⱼ − uᵢ − vⱼ` on the six non-basic cells:
`x₁₁ = 2, x₁₄ = 7, x₂₂ = 3, x₂₄ = 2, x₃₁ = 5, x₃₃ = 3` — all `≥ 0` ⇒ **the VAM solution is
already optimal, cost = 615**. (No stepping-stone loop needed; if any reduced cost were negative,
you would trace the closed `+/−` loop from that cell and shift the minimum `−`-cell amount.)

*(VAM tie-breaks can produce a different initial BFS. Check that yours also reaches cost 615 after
the optimality test — method marks matter more than matching this allocation.)*

**L1 rubric — 10 marks.** Balance check + no dummy (1); VAM penalties computed at least twice
correctly (2); complete initial BFS with `m + n − 1` basic cells (2); cost of initial BFS (1);
potentials `uᵢ + vⱼ = cᵢⱼ` set up with one `uᵢ` fixed (2); reduced-cost scan and correct
optimality verdict / improving cell (2).

**Wrong paths.** Using the north-west corner rule when VAM is asked (−2); fewer than `m + n − 1`
basic cells and not spotting the degeneracy (−2); sign error in `cᵢⱼ − uᵢ − vⱼ` (a negative that
should be positive sends you pivoting forever).

### L2 — Constrained NLP: a closed box of fixed volume

> Design a **closed** rectangular box (a lid on all six faces) of volume **`V = 32` (units³)** that
> uses the least sheet material. Let the base be `x × y` and the height `z`. Minimise surface area
> subject to the volume constraint. Solve with a Lagrange multiplier and confirm it is a minimum.

**Worked answer.** Minimise `S = 2(xy + yz + zx)` s.t. `h(x,y,z) = xyz − 32 = 0`.
`L = 2(xy + yz + zx) − λ(xyz − 32)`.
Stationarity:
`∂L/∂x = 2(y + z) − λ yz = 0`
`∂L/∂y = 2(x + z) − λ xz = 0`
`∂L/∂z = 2(y + x) − λ xy = 0`
Subtract the first two equations: `2(y − x) − λz(y − x) = 0 ⇒ (y − x)(2 − λz) = 0`. At a positive
optimum `λ, z > 0`; if `2 − λz = 0` the third equation forces a contradiction with `x, y > 0`, so
`y = x`. By the same argument on the other pairs, `z = x`. The stationary point is a **cube**:
`x = y = z`, and `V = x³ = 32 ⇒ x = 32^{1/3} ≈ 3.175`.
Surface area `S = 6x² = 6·32^{2/3} ≈ 60.48`; multiplier `λ = 2(y + z)/(yz) = 4x/x² = 4/x ≈ 1.260`.

Second-order check: on the constraint surface the objective `S(x) = 2(x² + 2·(32/x²)·x)`… simpler:
substitute `z = 32/(xy)` into `S`, giving `S(x,y) = 2(xy + 32/x + 32/y)`. Hessian
`∂²S/∂x² = 128/x³ > 0`, `∂²S/∂y² = 128/y³ > 0`, `∂²S/∂x∂y = 2`. At `x = y = 32^{1/3}`:
`128/x³ = 128/32 = 4`, so `H = [[4, 2], [2, 4]]`, `det = 12 > 0`, leading minor `4 > 0` →
`H ≻ 0` → **strict local minimum**. (And `S → ∞` as any edge → 0 or ∞, so it is the global
minimum.)

**Open-top variant** (the trap in the recollection): `S = xy + 2yz + 2zx` (no top). Then
`x = y = 2z`, `x²·(x/2) = 32 ⇒ x³ = 64 ⇒ x = y = 4, z = 2`, `S = 16 + 16 + 16 = 48`. Read the
problem for whether the lid is there before you start.

**L2 rubric — 10 marks.** Correct objective and constraint from the geometry (2); Lagrangian and
all stationarity equations (2); solving to `x = y = z` (cube) with justification (2); dimensions
`x = 32^{1/3}`, `S = 6·32^{2/3}`, `λ = 4/x` (2); a valid second-order argument (bordered Hessian,
reduced Hessian, or substitution) for "minimum" (2).

**Wrong paths.** Optimising `S` with no constraint (gets `x = 0`); using the open-top area when a
closed box is asked, or vice versa (−2, the recollection's exact mistake); stopping at the
stationary point with no second-order check (−2 — "stationary points are only candidates").

---

## Formula recall (blur the right-hand side and reconstruct)

| Prompt | Result |
|---|---|
| `≤ bᵢ` becomes … | `aᵢᵀx + sᵢ = bᵢ`, `sᵢ ≥ 0` (slack) |
| `≥ bᵢ` becomes … | `aᵢᵀx − eᵢ = bᵢ`, `eᵢ ≥ 0` (surplus), + artificial for the starting basis |
| free `xₖ` becomes … | `xₖ = xₖ⁺ − xₖ⁻`, both `≥ 0` |
| simplex optimal (Su Rong's `z − cᵀx` row) when … | every bottom-row entry `≥ 0` |
| leaving variable = … | row of minimum non-negative `bᵢ / aᵢⱼ` over `aᵢⱼ > 0` |
| unbounded when … | entering column has no `aᵢⱼ > 0` (no eligible ratio) |
| dual of `min cᵀx, Ax ≥ b, x ≥ 0` | `max bᵀw, Aᵀw ≤ c, w ≥ 0` |
| complementary slackness | `wᵢ((Ax)ᵢ − bᵢ) = 0`, `xⱼ(cⱼ − (Aᵀw)ⱼ) = 0` |
| shadow price of constraint `i` | bottom-row coefficient under `sᵢ` in the final tableau |
| RHS range keeps the basis while … | `B⁻¹(b + Δb) ≥ 0` |
| Hessian test at a stationary point | `H ≻ 0` min, `H ≺ 0` max, indefinite → saddle |
| KKT for `min f`, `g(x) ≥ 0` | `∇f − Σμⱼ∇gⱼ = 0`, `g ≥ 0`, `μ ≥ 0`, `μⱼgⱼ = 0` |

---

## Answer sheet (for pasting into Claude Code)

The interactive page's **Build answer sheet** button produces a self-contained plain-text block:
paper identity, the key-file path, mark allocation, elapsed time, your Q1/Q2 objective answers,
and `<blank>` markers, with the derivations marked "answered on paper". Paste it into a fresh
Claude Code conversation and ask for grading against this file — it will mark part-by-part, give
the total out of 16 (+ Section S / L separately), separate arithmetic slips from inverted
concepts, and fold anything that reflects a real gap back into the course notes.
