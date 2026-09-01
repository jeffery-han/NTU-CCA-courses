# EE6407 Quiz 1 — Prediction & Practice Paper

**Purpose.** A source-grounded mock built from (a) the local canonical notes
(`../notes/beginner-notes.tex`, `../notes/notes.tex`), (b) the local public archive, and
(c) student recollections gathered from 小红书 on 2026-09-01 (`rednote-quiz1-intel.md`).
Not an official paper. Attempt Part 1 closed-book before reading Part 2.

**Format assumed** (observed in the 25-26 S1 sitting; *verify on NTULearn*):
Week 4, closed-book, on the question paper — **10 True/False + 3 application questions +
1 short answer**. Scope = **Weeks 1–3 only** (the Week 4 lecture is not examined).

**Why markdown, not LaTeX.** The two canonical notes and their PDFs, plus
`../notes/quiz1-prep-learning.html`, remain the printable/interactive prep. This file is a
screen-study mock kept with the other quiz material in `quizzes/`.

---

## PART 1 — QUESTIONS (attempt first)

### Section A — True / False (10 marks, 1 each)
State T or F. (A one-line reason is given in Part 2; on the real quiz, only T/F is required.)

1. The offspring pool in an EA generally has higher diversity than the parent population it was produced from.
2. "NP" stands for *nondeterministic polynomial time*, not *non-polynomial*.
3. Branch-and-bound is one of the standard metaheuristic search methods.
4. Fitness-proportionate (roulette-wheel) selection probabilities are unchanged if the same positive constant is added to every individual's fitness.
5. Applying ordinary one-point crossover to two permutation chromosomes always produces two valid permutations.
6. In a binary-coded GA, the effect of a single bit flip on the decoded value does not depend on which bit is flipped.
7. In self-adaptive mutation of a real vector, the strategy parameter σ should be mutated *before* the object variables.
8. Whole arithmetic crossover with α = 0.5 yields two identical offspring, and no arithmetic-crossover offspring can fall outside the box spanned by the two parents.
9. Creep mutation on an integer genome can drive premature convergence, whereas random resetting does not have that tendency.
10. Recombination alone can restore an allele value that has been lost from the entire population.

*Disputed item seen in both circulated papers — be ready to argue it either way:*
"Finding a feasible path between two points in a complicated map is a class NP problem."

### Section B — Application (3 questions)

**B1. Permutation crossover (10 marks).**
For a permutation-coded GA the selected parents are
```
P1 = 1 2 3 [4 5 6 7] 8 9      (shaded = positions 4–7)
P2 = 4 5 2 [1 8 7 6] 9 3
```
(i) Perform **partially matched crossover (PMX)** on the shaded substrings and write both offspring.
(ii) Show the mapping you used and verify each offspring is a valid permutation.
(iii) State one legal **mutation** operator for this representation and apply it once to offspring 1.

**B2. Binary encoding, decoding, selection, variation (10 marks).**
A GA maximises `f(x) = x²` for integer `x ∈ [0, 31]`, using 5-bit chromosomes, MSB first.
Population (size 4): `s1 = 11010`, `s2 = 00101`, `s3 = 10011`, `s4 = 01110`.
(i) Decode each chromosome and give its fitness.
(ii) Compute the roulette-wheel selection probability of each chromosome; verify they sum to 1.
(iii) Cross `s1 × s3` with a one-point cut after bit 2 (between positions 2 and 3). Decode both children and give their fitness.
(iv) With per-bit mutation probability `p_m = 0.01`, give the **expected** number of flipped bits in the 20-bit population and `Pr(no bit flips at all)`. Explain why the expected value is not the number you will actually see.

**B3. Integer encoding — graph colouring (10 marks).**
A map has 6 regions. Adjacent pairs (sharing a border) are
`R1–R2, R1–R3, R2–R3, R2–R4, R3–R5, R4–R5, R4–R6, R5–R6`.
Colours are `{1, 2, 3}`, chromosome `c ∈ {1,2,3}⁶` with `c_k` the colour of region `k`.
(i) Write the constraint-violation function `V(c)` and a fitness `f(c)` to be maximised.
(ii) Give a chromosome with `V(c) = 0`, or explain why none exists.
(iii) Would 2 colours suffice for this map? Justify from the adjacency structure.
(iv) State one legal mutation and one legal crossover for this representation.

### Section C — Short answer (10 marks)
**Predicted:** "Discuss the implications of the No Free Lunch theorem of optimization on problem-solving."
*(Alternates that have appeared: "A common approach to select parents is fitness-proportionate
selection — discuss its effectiveness at different stages of a GA search"; "Explain in your own
words what evolutionary *creativity* means." Model answers to all three are in Part 2.)*

---

## PART 2 — WORKED SOLUTIONS

### Section A

| # | Ans | Reason |
|---|:--:|---|
| 1 | **F** | The offspring pool has already passed through parent selection and survivor selection; low-fitness variety is culled. Diversity is normally *highest at random initialisation* and decays. |
| 2 | **T** | NP = problems whose "yes" certificates are checkable in polynomial time by a nondeterministic machine. `P ⊆ NP`. "Non-polynomial" is the classic wrong expansion. |
| 3 | **F** | Branch-and-bound is an **exact** tree-search framework: run to completion it certifies the optimum. Metaheuristics (GA, ACO, PSO, SA) are stochastic and certify nothing. |
| 4 | **F** | `p_i = f_i / Σ f_j`. Adding `c` to every `f_i` changes `p_i` to `(f_i + c)/(Σ f_j + nc)` — the ranking is preserved but the probabilities flatten toward uniform. Rank / tournament selection avoid this. |
| 5 | **F** | One-point crossover on permutations duplicates some symbols and drops others. Valid permutation operators: order-1, PMX, cycle, edge recombination; valid mutations: swap, insert, scramble, inversion. |
| 6 | **F** | Flipping the MSB changes the decoded integer by `2^{L-1}`; the LSB by 1. The *application* of mutation is uniform but its *effect* is biased toward significant bits. **Gray coding** is the standard remedy (numerically adjacent values differ by one bit). |
| 7 | **T** | Fitness is measured on `x` only, so a new `σ'` can only be judged through the `x'` it produced. Mutating `σ` first, then using it to mutate `x`, creates that dependency. |
| 8 | **T** | `z^{(1)} = αx + (1−α)y`, `z^{(2)} = (1−α)x + αy`; at α = 0.5 both equal `(x+y)/2`. Every arithmetic offspring is a convex combination of the parents ⇒ inside their box. **Blend crossover** is the operator that can reach outside it. |
| 9 | **T** | Creep adds small ± steps; they accumulate, individuals drift together ⇒ premature convergence. Random resetting draws a fresh value (the true analogue of a bit flip) and does not have this drift. |
| 10 | **F** | Crossover only *redistributes* alleles already present. Starting from a 1:1 zero/one ratio, crossover leaves the population-wide ratio at 1:1 forever; a lost allele is unrecoverable without **mutation**. |

**Disputed item.** `notes.tex` states `P ⊆ NP`. Finding a feasible path in a graph is solvable by
BFS/DFS in polynomial time, so it is in **P**, and therefore *also* in **NP** by containment.
- Under the strict definition ("in NP") the statement is **True**.
- Under the colloquial exam reading ("NP means hard / in NP but not in P") it is **False**.
Name the ambiguity in your answer; that is the point the item tests. The course slides use the
strict containment definition, so if forced, answer **True** and justify by `P ⊆ NP`.

### Section B1 — PMX

Segment (positions 4–7): `P1 = [4 5 6 7]`, `P2 = [1 8 7 6]`.
Position-wise mapping: `4↔1, 5↔8, 6↔7, 7↔6`.

**Offspring 1** — copy P1's segment, fill the rest from P2 (positions 1,2,3,8,9 → P2 values 4,5,2,9,3):
- pos 1: P2 = 4, already in segment → follow `4→1`; 1 is free → **1**
- pos 2: P2 = 5, in segment → `5→8`; 8 is free → **8**
- pos 3: P2 = 2, free → **2**
- pos 8: P2 = 9, free → **9**
- pos 9: P2 = 3, free → **3**

`Offspring 1 = 1 8 2 | 4 5 6 7 | 9 3`  → digits {1..9} once each ✓

**Offspring 2** — copy P2's segment, fill from P1 (positions 1,2,3,8,9 → P1 values 1,2,3,8,9), mapping reversed `1↔4, 8↔5, 7↔6, 6↔7`:
- pos 1: P1 = 1, in segment → `1→4`; 4 free → **4**
- pos 2: P1 = 2, free → **2**
- pos 3: P1 = 3, free → **3**
- pos 8: P1 = 8, in segment → `8→5`; 5 free → **5**
- pos 9: P1 = 9, free → **9**

`Offspring 2 = 4 2 3 | 1 8 7 6 | 5 9`  → digits {1..9} once each ✓

(iii) **Swap mutation** on offspring 1, swap positions 2 and 7:
`1 8 2 4 5 6 7 9 3` → `1 7 2 4 5 6 8 9 3` — still a permutation ✓.

### Section B2 — Binary SGA step

(i) Decode (MSB first) and fitness `x²`:

| chrom | bits | `x` | `f = x²` |
|---|---|---:|---:|
| s1 | 11010 | 26 | 676 |
| s2 | 00101 | 5  | 25 |
| s3 | 10011 | 19 | 361 |
| s4 | 01110 | 14 | 196 |
| **Σ** | | | **1258** |

(ii) `p_i = f_i / 1258`:
`p1 = 676/1258 = 0.5374`, `p2 = 25/1258 = 0.0199`,
`p3 = 361/1258 = 0.2870`, `p4 = 196/1258 = 0.1558`.
Sum `= 1.0001` (rounding) ✓.

(iii) `s1 = 11|010`, `s3 = 10|011`, cut after bit 2:
- child A = `11|011` = `11011` → `x = 27` → `f = 729`
- child B = `10|010` = `10010` → `x = 18` → `f = 324`

(iv) 20 bits, `p_m = 0.01`:
- `E[flips] = 20 × 0.01 = 0.2`
- `Pr(no flips) = (1 − 0.01)^20 = 0.99^20 ≈ 0.8179`
- `0.2` is an average over many generations. In any single generation the realised count is a
  non-negative integer drawn from `Binomial(20, 0.01)`; the most probable value is **0** (≈ 82 %),
  then 1 (≈ 17 %). You never literally see "0.2 bits" mutate.

### Section B3 — Graph colouring

Edges: `E = {R1R2, R1R3, R2R3, R2R4, R3R5, R4R5, R4R6, R5R6}`, `|E| = 8`.

(i) `V(c) = Σ_{(u,v) ∈ E} 1[c_u = c_v]`  (number of edges whose endpoints share a colour).
`f(c) = |E| − V(c) = 8 − V(c)`, maximised; `f = 8 ⇔ V = 0 ⇔ proper colouring`.
Unlike the N-queens permutation, this encoding **cannot** make the constraint unviolatable, so
constraint handling is paid for in the objective.

(ii) `c = (1, 2, 3, 1, 2, 3)`:
`R1R2` 1≠2 ✓ · `R1R3` 1≠3 ✓ · `R2R3` 2≠3 ✓ · `R2R4` 2≠1 ✓ · `R3R5` 3≠2 ✓ ·
`R4R5` 1≠2 ✓ · `R4R6` 1≠3 ✓ · `R5R6` 2≠3 ✓ → `V = 0`. Valid.

(iii) **No.** `R1, R2, R3` are mutually adjacent (a triangle / `K₃`), which needs 3 distinct
colours. 2 colours can only properly colour bipartite (odd-cycle-free) graphs.

(iv) Mutation: **random resetting** (draw a fresh colour in `{1,2,3}`) or **creep** (±1 mod 3).
Crossover: one-point / multi-point / uniform, as for binary strings.

### Section C — model answers

**No Free Lunch (predicted).**
Plot an algorithm's performance over *all* possible objective functions. NFL (Wolpert & Macready,
1997) says that, averaged uniformly over that set, **every algorithm has the same mean
performance** — even random search. Adding domain knowledge (a tailored representation, repair
rules, seeded solutions, specialised operators) *deforms* the performance curve: a higher peak on
the targeted problem class bought with a lower value elsewhere; the enclosed area is unchanged.
Implications for problem-solving:
1. There is **no universal optimiser**; "best algorithm" is only meaningful relative to a problem class.
2. Real engineering problems are a **structured, non-uniform subset** of all functions, so exploiting
   their structure (bias) is exactly the right move — NFL does *not* say algorithm choice is irrelevant here.
3. The working question is **which bias matches this problem**, answered empirically on representative instances.
4. Benchmark/leaderboard results transfer only to problems that share structure with the benchmark.

**Fitness-proportionate selection over the search (alternate).**
`p_i = f_i / Σ f_j`.
- *Early:* the initial population often contains a few chromosomes with far higher fitness than the
  rest. Their selection probability dominates, they flood the mating pool, diversity crashes ⇒
  **premature convergence** to a local optimum.
- *Late:* as the population converges, all fitness values become similar. Ratios `f_i / Σ f_j`
  approach uniform, so selection pressure **vanishes** and the search stops making directed progress
  (drifts randomly).
- It is also unusable with negative fitness and sensitive to additive scaling.
- Remedies: fitness scaling (sigma / linear / power), or switch to **rank** or **tournament**
  selection, which depend only on order and keep pressure roughly constant throughout the run.

**Evolutionary "creativity" (alternate).**
The ability of an EA to produce solutions the designer did not anticipate and did not build in.
Because selection acts only on the fitness score and variation (mutation, recombination) is
undirected, the algorithm explores regions of the search space that human intuition would skip. It
can therefore exploit loopholes in the fitness function, combine partial structures from different
lineages into novel wholes, or find unconventional designs (e.g. odd antenna geometries, unexpected
circuit topologies). The flip side: the same undirected search will "creatively" exploit any
mis-specification in the fitness function, so creativity is only as useful as the objective is
honest.

---

## PART 3 — THE "ONE UNSEEN ITEM" PREDICTION

Every recalled sitting added one item **not** in the two circulated past papers:
25-26 S1 added the number-base decode; the Feb-2026 sitting added the grid three-colouring
construction and "evolutionary creativity". So expect one fresh item drawn from the Weeks 1–3
material that the circulated papers never touched. Ranked by likelihood, with a 60-second drill each:

1. **Edge recombination crossover.** The only permutation operator not yet examined (order-1, PMX,
   cycle all have). *Drill:* build the neighbour table from two 6-city tours, mark common edges with
   `+`, then construct the child by the rule order — common edge → shortest remaining list → random
   tie-break → jump to a random unused city on an empty list. Always end by checking every city
   appears once. See `../notes/notes.tex` §"Permutation".
2. **Roulette-wheel arithmetic with a scaling trap.** Give fitnesses including a 0 or a negative
   value, or ask what adding a constant does. *Drill:* `A,B,C` with fitness `3,1,2` → `p = 1/2, 1/6, 1/3`;
   now add 10 to each → `p = 13/36, 11/36, 12/36` — ranking kept, probabilities flattened.
3. **Gray coding.** Why plain binary mutation is biased and how Gray code fixes it (adjacent values
   differ in one bit). Possibly: convert a 4-bit binary value to Gray or back.
4. **Self-adaptive mutation order.** State and justify: mutate `σ` before `x`.
5. **Arithmetic vs blend crossover — the bounding box.** Show arithmetic offspring stay inside
   `[x_i, y_i]`; blend with `α = 0.5`, `x_i = 0.3`, `y_i = 0.7` samples from `[0.1, 0.9]`.
6. **Creep vs random resetting** on integers — which converges prematurely and why.
7. **GP tree node/edge counting.** For an expression with `L` leaves built from binary operators:
   `L − 1` internal nodes, `2(L − 1)` edges. Reading order = operator precedence, root applied last.
8. **`y = M(x)` classification with `S`, `F`, `f`.** Classify a described task as optimisation /
   modelling / simulation and identify search space, feasible set, objective.
9. **Binary → bounded real decode.** `Γ(a) = x + (y−x)/(2^L − 1) · Σ a_i 2^{L−i}` — divide by
   `2^L − 1`, **not** `2^L`. (Trinary analogue uses `3^L − 1`.)

### Quick-reference formulas (reproduce from memory)

```
classify:   x unknown → optimisation ;  M unknown → modelling ;  y unknown → simulation
roulette:   p_i = f_i / Σ_j f_j
N-queens:   attack iff |q_i − q_j| = |i − j| ;  max fitness = C(N,2)
binary→int: z = Σ_{k=0}^{L-1} 2^k b_k
b→real:     Γ(a) = a_lo + (a_hi − a_lo)/(2^L − 1) · Σ_{i=1}^{L} a_i 2^{L−i}
trinary→real: same with base 3 and (3^L − 1)
mutation:   E[flips] = N·L·p_m ;  Pr(no flip) = (1 − p_m)^{N·L} ;  guide  1/μ ≲ p_m ≲ 1/L
arithmetic xover: z_i = α x_i + (1−α) y_i  (α = 0.5 ⇒ identical children, stays in parent box)
blend xover:      d_i = y_i − x_i ,  z_i ~ U[x_i − α d_i ,  y_i + α d_i]
graph colouring:  V(c) = Σ_{(u,v)∈E} 1[c_u = c_v] ,  f = |E| − V
GP tree:  L leaves ⇒ L−1 internal nodes ⇒ 2(L−1) edges
```

### Likely traps (from `notes.tex` §"Likely traps")
NP ≠ non-polynomial · selection favours but never guarantees · parent vs survivor selection answer
different questions · convergence ≠ global-optimality proof · "local optimum" is undefined without a
neighbourhood · NFL does **not** say algorithm choice is irrelevant on a given problem · creep
converges prematurely, random resetting does not · arithmetic crossover cannot explore outside the
parents' interval · crossover never changes population-wide allele frequencies · a binary mutation
is uniform in application but biased in effect toward significant bits.
