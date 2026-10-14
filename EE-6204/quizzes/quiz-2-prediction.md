# EE6204 Quiz 2 — prediction paper: questions, key, rubric

**Unofficial practice paper.** Built 2026-10-14 to the *official* Quiz 2 shape (4 questions,
keyed answers in an exact format, calculator allowed, appendix provided, 50 min — see
`quiz-2-intel.md`). The **topics per question are a prediction** from the lecturer's own sample
questions and final-exam history; the actual quiz may differ.

- Interface (answer-free): `quiz-2-prediction.html`
- Every key is derived in `quiz-2-prediction-check.py` (exact fractions; floats only for `e^x`;
  half-up rounding applied once at the end). Run it to re-verify.
- All numbers are fresh: none match the lecture examples (Eg 3.1 λ=8/µ=10, Eg 9.1
  s=20/p=4/f=0.05/r=1, the PC shop with Poisson(1) demand) or `notes/quiz2-prep-learning.html`.

**Marking:** 1 mark per input box, **25 marks**. A box is right only if the string matches the key
in the stated format (the real system works this way — "no backend intervention"). When grading,
also record *format-only* misses (right value, wrong format) separately from value errors.

---

## Q1 — Random variables, Poisson processes, classification (7 marks)

A help desk receives calls on two independent lines. Line A calls form a Poisson process with
rate 3 per hour; line B calls form a Poisson process with rate 2 per hour.

| Part | Question | Format | Key |
|---|---|---|---|
| (a) | P(exactly 2 calls in total in a 30-minute interval) | 4 d.p. | **0.2565** |
| (b) | P(the next call comes from line A) | simplest fraction | **3/5** |
| (c) | No call arrived in the last 10 minutes. P(no call in the next 15 minutes) | 4 d.p. | **0.2865** |
| (d) | A cutting tool breaks on any operation with probability 0.02, independently. It has survived 25 operations. P(it survives at least 50 more operations) | 4 d.p. | **0.3642** |
| (e) | Mean number of operations up to and including the breakdown, for a new tool | integer | **50** |
| (f) | Number of customers in a bank, observed continuously: classify (A DT-DS, B DT-CS, C CT-DS, D CT-CS) | one letter | **C** |
| (g) | Distribution of the number of steps a DTMC spends in state i per visit (A Poisson, B exponential, C geometric, D uniform) | one letter | **C** |

**Derivations.**
(a) Superposition → Poisson rate 5/h; in 0.5 h the mean is 2.5; `e^{-2.5}·2.5²/2! = 0.25652`.
(b) Decomposition / competing exponentials: `λ_A/(λ_A+λ_B) = 3/5`.
(c) Memoryless — the 10 quiet minutes are irrelevant: `P(T>15 min) = e^{-5·0.25} = e^{-1.25} = 0.28650`.
(d) Geometric memoryless: `P(X>75 | X>25) = P(X>50) = 0.98^{50} = 0.36417`.
(e) `E(X) = 1/p = 50`.
(f) Time is continuous (observed at every t ≥ 0); the count takes values in {0, 1, 2, …}, a countable set → continuous-time, discrete-state (a continuous-time chain), like lecture Eg 3.3.
(g) `P(Tᵢ > n) = pᵢᵢⁿ` ⇒ `P(Tᵢ = n) = pᵢᵢ^{n−1}(1−pᵢᵢ)`: geometric with success probability `1 − pᵢᵢ` (lecture-01 p23–24). The CTMC analogue is exponential.

Added 2026-10-14 after merging the RedNote evidence: the Oct-2025 recollection (S1 in `quiz-2-intel.md`) says the first page tested exactly these two concepts.

**Common wrong paths.**
- (a) using a rate of 3 or 2 instead of the sum (forgetting superposition), or `λt = 5` (forgot to
  convert 30 min) → 0.0842.
- (b) `0.6` — right value, **wrong format** (the box asked for a fraction).
- (f) D — confusing a continuous *time* index with a continuous *state*; A — if you imagined hourly snapshots, but the question says continuous observation.
- (g) B — exponential is the CTMC holding time; Poisson counts events, it is not a holding time.
- (c) using 25 minutes (`e^{-25/12} = 0.1245`) → the memoryless property was not applied.
- (d) `0.98^{75}` or `0.98^{49}` → off-by-one / no memoryless. "At least 50 more" means
  `X > 75` given `X > 25`.

## Q2 — Inventory DTMC (6 marks)

A shop sells a spare part. Weekly demands `D₁, D₂, …` are i.i.d. Poisson with mean 0.5. Let `Xₙ`
be the stock at the **end** of week n, `0 ≤ X₀ ≤ 2`. Policy: if the stock at the end of a week is
0, the shop orders 2 parts that arrive before the next week opens; otherwise no order. Unmet
demand is lost. State space `S = {0, 1, 2}`.

| Part | Question | Format | Key |
|---|---|---|---|
| (a) | `p₀₁` | 4 d.p. | **0.3033** |
| (b) | `p₁₀` | 4 d.p. | **0.3935** |
| (c) | Mean sojourn time in state 1 (weeks) | 4 d.p. | **2.5415** |
| (d) | `P(X₂ = 0 \| X₀ = 2)` | 6 d.p. | **0.182174** |
| (e) | Steady-state probability of state 0 | 6 d.p. | **0.222205** |
| (f) | Long-run mean end-of-week stock | 4 d.p. | **1.1203** |

**Derivation.** Relation: `X_{n+1} = max(2 − D_{n+1}, 0)` if `Xₙ = 0`; `max(Xₙ − D_{n+1}, 0)` if
`Xₙ ≥ 1`. With `d₀ = e^{-0.5} = 0.60653`, `d₁ = 0.5e^{-0.5} = 0.30327`, `P(D≥2) = 0.09020`:

```
          to 0       to 1    to 2
from 0  [ 0.09020   0.30327  0.60653 ]   (restocked to 2, so same row as state 2)
from 1  [ 0.39347   0.60653  0       ]
from 2  [ 0.09020   0.30327  0.60653 ]
```

(c) `1/(1 − p₁₁) = 1/0.39347 = 2.54149`.
(d) `p₂₀(2) = Σₖ p₂ₖ pₖ₀ = P(D≥2)² + d₁(1−d₀) + d₀P(D≥2) = 0.0081365 + 0.1193273 + 0.0547098 = 0.182174`.
(e) Rows 0 and 2 coincide, so with `T = y₀ + y₂`: `y₂ = T d₀`, `y₀ = T(1 − d₀)`,
`y₁ = T d₁/(1 − d₀)`, and `T = (1 − d₀)/(1 − d₀ + d₁) = 0.56473` → `y₀ = 0.222205`,
`y₁ = 0.43527`, `y₂ = 0.34253` (sum 1 ✓).
(f) `0·y₀ + 1·y₁ + 2·y₂ = 1.12033`.

**Common wrong paths.**
- Treating state 0 as "stays at 0 until demand" — forgetting the restock, so row 0 becomes
  `[1, 0, 0]` (absorbing). The policy check is the first thing to read.
- `p₁₀ = d₁` (exactly one demand) instead of `P(D ≥ 1) = 1 − d₀` — the stock cannot go negative,
  so *all* demand ≥ 1 empties it.
- (c) `1/p₁₁` or `p₁₁/(1−p₁₁)`. Lecture formula: `E(Tᵢ) = 1/(1 − pᵢᵢ)` time steps.
- (d) reading `p₂₀` (one step) instead of the two-step entry, or computing `(P²)₀₂`.
- Rounding `d₀` to 0.6065 (or the TPM entries to 4 d.p.) early, then compounding: the 6-d.p. answers in (d)/(e) drift in the last digits — round only at the end. Four boxes in this paper ask for 6 d.p. on purpose (2d, 2e, 3d, 4e): the only recorded format evidence (S3 in `quiz-2-intel.md`) shows six-decimal probabilities.

## Q3 — Machine CTMC (5 marks)

A machine cycles: **setup** (state 0, duration EXP(s)), then **processing** one part (state 1,
EXP(p)), then back to setup. The machine can fail **both during setup and during processing**,
time to failure EXP(f) in either state; a failed machine (state 2) is repaired in EXP(r) and,
after repair, the unfinished part is **discarded** and a fresh setup starts. All times
independent. Rates per hour: `s = 6, p = 3, f = 0.5, r = 2`.

| Part | Question | Format | Key |
|---|---|---|---|
| (a) | Diagonal entry `q₀₀` of the generator Q | 1 d.p. | **-6.5** |
| (b) | Mean sojourn time in state 1, in **minutes** | 2 d.p. | **17.14** |
| (c) | Steady-state probability π₀ | simplest fraction | **28/95** |
| (d) | Production rate R (parts per hour) | 6 d.p. | **1.515789** |
| (e) | Long-run fraction of time the machine is under repair | simplest fraction | **1/5** |

**Derivation.**

```
Q = [ -(s+f)    s        f  ]   = [ -6.5   6    0.5 ]
    [   p     -(p+f)     f  ]     [  3    -3.5  0.5 ]
    [   r       0       -r  ]     [  2     0   -2   ]
```

Rate balance: state 1 `(p+f)π₁ = sπ₀` → `π₁ = (12/7)π₀`; state 2 `rπ₂ = f(π₀+π₁)` →
`π₂ = (19/28)π₀`; normalise: `π₀(28+48+19)/28 = 1` → `π₀ = 28/95`, `π₁ = 48/95`, `π₂ = 19/95 = 1/5`.
Check state 0: `6.5·28/95 = 182/95 = 3·48/95 + 2·19/95` ✓.
(b) Sojourn in state 1 is `EXP(p+f) = EXP(3.5)` → `60/3.5 = 17.142857` min.
(d) `R = pπ₁ = 144/95 = 1.515789`.

**Common wrong paths.**
- (a) `-6` (forgot that failure is also possible during setup) or `+6.5` (sign: diagonal of a
  generator is **minus** the total out-rate; rows sum to 0).
- (b) `20.00` (used `1/p`) — leaving state 1 happens at the *first* of completion or failure,
  `min(EXP(p), EXP(f)) = EXP(p+f)`.
- (c) `56/190` → not simplest form, marked wrong. `0.2947` → wrong format.
- (d) `R = p` or `R = sπ₀`: the latter counts setups completed, and some setups are interrupted
  later by failures in processing — it overstates output (`6·28/95 = 1.768`).
- Copying the Eg 9.1 / Problem 9.2 discard formula: that model has no failure during setup, so
  its π₀ differs.

## Q4 — Queue design comparison (7 marks)

Jobs arrive at a print room as a Poisson process, λ = 9 per hour. Use the exam appendix.

- **System A:** one fast printer, exponential service with mean 5 min (µ = 12/h) — M/M/1.
- **System B:** two slow printers sharing one queue, each with mean 10 min (µ = 6/h) — M/M/2.
- **System C:** the fast printer of A, but at most 3 jobs fit in the room (in service + waiting);
  arrivals finding it full are turned away — M/M/1/3.
- **System D:** the fast printer of A, but jobs arrive in batches of 3, at 3 batches per hour —
  Mᵇ/M/1 with b = 3.

| Part | Question | Format | Key |
|---|---|---|---|
| (a) | A: mean time in system W (minutes) | 2 d.p. | **20.00** |
| (b) | B: probability the system is empty π₀ | simplest fraction | **1/7** |
| (c) | B: mean number in system L | 4 d.p. | **3.4286** |
| (d) | C: probability an arriving job is turned away | simplest fraction | **27/175** |
| (e) | C: mean number in system L | 6 d.p. | **1.148571** |
| (f) | D: mean time in system W (minutes) | 2 d.p. | **40.00** |
| (g) | A (FIFO): P(a job waits in the queue more than 10 minutes) | 4 d.p. | **0.4549** |

**Derivations.**
(a) `W = 1/(µ−λ) = 1/3 h = 20 min`.
(b) `ρ = λ/(mµ) = 3/4`, `mρ = 3/2`: `π₀ = [ (3/2)²/(2!·(1/4)) + 1 + 3/2 ]^{-1} = [9/2 + 5/2]^{-1} = 1/7`.
(c) `Q = ρ(mρ)^m π₀/(m!(1−ρ)²) = (3/4)(9/4)(1/7)/(2·1/16) = 27/14`; `L = Q + λ/µ = 27/14 + 3/2 = 24/7 = 3.428571`.
(d) PASTA: an arrival is blocked with probability `π₃ = ρ³(1−ρ)/(1−ρ⁴) = (27/256)/(175/256) = 27/175`.
(e) Appendix `L = ρ[1−ρᴺ−Nρᴺ(1−ρ)]/((1−ρ)(1−ρᴺ⁺¹))` with ρ=3/4, N=3 → `201/175 = 1.148571`
(cross-checked as `Σ kπₖ`).
(f) `ρ = bλ/µ = 9/12 = 3/4`; `W = (1+b)/(2µ(1−ρ)) = 4/(24·1/4) = 2/3 h = 40 min`.
(g) **Not on the appendix** — M/M/1 waiting-time distribution (lecture-02 p13–14, taught Week 8): `P(d > t) = ρ e^{−µ(1−ρ)t} = 0.75·e^{−12·0.25·(1/6)} = 0.75 e^{−0.5} = 0.454898`. Added 2026-10-14 after the Week 8 transcript showed this was derived in class.

**Comparison (for discussion, not keyed):** A beats B on W (20 vs `L/λ = 24/63 h = 22.86` min),
the same pooling lesson as lecture slide p27 (M/M/1 with 2µ beats M/M/2). C has a short queue
but loses 15.4 % of jobs. D doubles A's W because every job waits for its batch-mates.

**Common wrong paths.**
- (a) answering in hours (`0.33`) when the box asked for minutes.
- (b) using `ρ = λ/µ = 1.5` in the M/M/m formula (the appendix defines `ρ = λ/(mµ)`), or
  summing `Σ_{k=0}^{m}` instead of `Σ_{k=0}^{m-1}`.
- (c) reporting Q (1.9286) instead of L — the question asks for the number in **system**.
- (d) `π₀` instead of `π_N`, or `ρ^N(1−ρ)` without the `1−ρ^{N+1}` normaliser.
- (f) using `ρ = λ/µ = 0.25` (forgot ×b), or `W = L/λ` with λ = batches only → 120 min.
- (g) `e^{−0.5} = 0.6065` (dropped the leading ρ — that is P(time in *system* > 10 min)), or `1 − 0.75e^{−0.5} = 0.5451` (the cdf, not the tail).

---

## Grading checklist (for the grader)

1. Score each box: exact string match = 1; else 0. Report `/25`.
2. Re-mark each miss as **format-only** (value right, form wrong), **slip** (method right,
   arithmetic/rounding wrong), or **concept** (wrong model/formula). Concept misses go to the
   notes (Stage 6); format-only misses go to the quiz-day checklist.
3. Blank ≠ wrong: list blanks separately with elapsed time.
