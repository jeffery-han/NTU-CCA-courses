# EE6407 Quiz 1 — RedNote (小红书) intelligence

Gathered 2026-09-01 by searching 小红书 for `EE6407` (logged-in session, `type=51` notes search).
This file is **unofficial student recollection**, not an official paper or marking scheme. Treat
every "answer" below as a study hypothesis to re-derive, not as ground truth. Verify quiz
logistics on NTULearn.

## Sources consulted

| Note title | Author | Posted | Likes | What it contains |
|---|---|---|---:|---|
| `EE6407 Quiz 1 复习` | 头没那么大 | 2026-08-31 | 79 | Typed transcript of **two** past papers (25-26 S1, 24-25 S2) + T/F answers + handwritten worked solutions for the calculation questions. Most current. |
| `🇸🇬NTU EE6407 Quiz 1（两学期完整版）` | 梵高先生不姓梵 | 2026-07 | 217 | Clean typed版 of the same two papers (25-26 S1, 24-25 S2). No answers. Author comment clarifies the bold PMX substring in 25-26 S1 Q2. |
| `EE6407 Quiz 1（2026.2）` | 新叶猫 | 2026-02-19 | 42 | Reconstruction of the **Feb 2026 sitting (24-25 S2 makeup / 25-26 S2)** — a *different* structure: trinary + knight-move T/F, a 4×5 three-colouring construction, an Ackley-style fitness-and-sort question, and a "what is evolutionary creativity" short answer. |
| `NTU EEE 6407＆6204 quiz1回顾` | 今天可以去哪玩 | 2025-09-19 | 37 | Format + strategy notes (see below). |
| `6407你真是🐶` | TH | 2026-08-21 | 7 | Screenshot of GSLink: **EE6407 AY2026 Sem 1 commenced 11-Aug-2026**, two class groups (A, and B under Assoc Prof Mao Kezhi in LT19A). |

## Confirmed format (from `6407＆6204 quiz1回顾`, matches the two circulated papers)

- **Week 4**, closed-book, answers written on the question paper, submitted and signed in person.
- **10 True/False + 3 application (calculation) questions + 1 short-answer.**
- Scope = **Weeks 1–3 only** ("树 之前内容 / 前三周内容"); the Week 4 lecture is **not** examined.
- The paper is assembled by **recombining questions from the two circulating past papers** — but
  the lecturer **adds one new twist each year that is not in the old papers**:
  - AY2025-26 S1: added a **number-base conversion** question (the trinary→real decode, Q3).
  - Feb 2026 sitting: added the **graph three-colouring construction** and **"evolutionary creativity"**.
  - **Expectation for your sitting: everything below is fair game, plus one unseen item.**

## Recalled paper A — EE6407 Quiz 1 (24-25 S2)

### Q1. True/False (10)
| # | Statement | Student consensus |
|---|---|---|
| a | Finding a feasible path between two points in a complicated map is a class NP problem. | **F** (BFS/DFS is polynomial ⇒ in P; disputed, some say the phrasing is ambiguous) |
| b | During initialization of a GA, the population diversity tends to be the highest. | **T** (random init, selection has not yet removed anything) |
| c | Selection of parents reduces population diversity while recombination increases diversity. | **T** |
| d | A GA used to solve for the weight matrix of an ANN is a *simulation* problem per the black-box characterization. | **F** (it is *modelling* — unknown `M`, given `x,y`) |
| e | An example of a class P problem is finding a solution to an N-queens problem. | **T** (ordinary, non-predefined N-queens has a polynomial constructive method) |
| f | For a GA using a binary-tree representation, the Boolean expression `F = abcdef` should have 12 edges. | **F** (a 6-leaf binary expression tree has 5 internal nodes ⇒ 10 edges; "12" only if you also count an `=`/root node) |
| g | It is still possible for an evolutionary algorithm to work with only recombination. | **F** (crossover cannot introduce a lost allele; only mutation can) |
| h | NP stands for "non-distinguishable polynomial". | **F** (nondeterministic polynomial time) |
| i | Recombination increases population diversity while mutation reduces diversity. | **F** (both create variation; mutation is the one that can *introduce* new alleles) |
| j | It is possible to show that P = NP if we have enough computing resources. | **F** (hardware/time cannot settle a complexity-class question) |

### Q2. Order-1 crossover
Parents `<a b c d e f g h i j>` and `<j a i h b c g d f e>`, segment = positions 4–8.
```
P1: a b c [d e f g h] i j
P2: j a i [b h c g d] f e
```
### Q3. Partially matched crossover (PMX) — same parents, same segment.
### Q4. Cycle crossover — same parents, same segment.
### Q5. Short answer
"A common approach to select parents for crossover is fitness-proportional selection. Discuss its
effectiveness at different stages of a GA search." (early: a few super-individuals dominate ⇒
premature convergence; late: fitnesses bunch up ⇒ selection pressure collapses ⇒ stagnation;
remedy = scaling / rank / tournament.)

## Recalled paper B — EE6407 Quiz 1 (25-26 S1)

### Q1. True/False (10)
| # | Statement | Student consensus |
|---|---|---|
| 1 | In the EA framework (population, parents, offspring), diversity is probably highest in the offspring pool. | **F** (offspring pool has already been through selection; parent generation was more diverse) |
| 2 | GA is a metaheuristic that can usually find the optimum solution in P time. | **F** |
| 3 | It is possible to show P = NP if we have enough computing resources. | **F** |
| 4 | Metaheuristics are a non-deterministic approach for solving NP problems in reasonable computational time. | **T** (course phrasing) |
| 5 | Saying a problem is class NP means it is a "non-polynomial deterministic" / "non-polynomial nondeterminism". | **F** (nondeterministic *polynomial* time) |
| 6 | An example of a class P problem is finding a solution to an N-queens problem. | **T** |
| 7 | For even `n > 10`, the permutation string `[1,3,5,…,n-1, 2,4,6,…,n]` is a valid N-queens configuration with no attacking queens. | **F** (queen at (1,1) and queen at (n,n) sit on the main diagonal: `|1−n| = |1−n|`) |
| 8 | NP-complete problems require a polynomial algorithm to verify a solution. | **T** (NP-complete ⊆ NP) |
| 9 | Finding a feasible path between two points in a complicated map is a class NP problem. | disputed; poster leans **F** |
| 10 | Branch-and-bound is one of the many metaheuristic approaches. | **F** (it is an *exact* search framework) |

### Q2. Partially matched crossover (PMX), permutation length 16 (hex alphabet `0-9 A-F`)
```
P1: F E D C [B A 9 8 7 6 5 4] 3 2 1 0      (bold/shaded = positions 5–12, "B … 4")
P2: B A 8 1 [D 9 7 C 2 E 6 0] 3 F 4 5      (bold/shaded = positions 5–12, "D … 0")
```
(Author of the 梵高 note confirms in a pinned comment: "加粗部分是 B–4, D–0".)
Re-derived independently (the 头没那么大 handwritten `offspring1` was garbled — it had two `A`s and no `0`):
`offspring 1 = D 2 C 1 B A 9 8 7 6 5 4 3 F 0 E`  ( = `D2C1BA9876543F0E` )
`offspring 2 = F 5 B 8 D 9 7 C 2 E 6 0 3 A 1 4`  ( = `F5B8D97C2E603A14` )
Both contain `0-9 A-F` exactly once. Mapping used: `B↔D, A↔9, 9↔7, 8↔C, 7↔2, 6↔E, 5↔6, 4↔0`.

### Q3. Number-base decode
"Consider a 10-digit trinary (base-3) coding system representing real values in `[0, 100]`.
Find the equivalent real value for the trinary string `<0221021121>`."
(String digits vary between the two transcripts: `0221021121` / `0221021112` / 9-digit `022102112`
— re-read the actual paper. Method is unambiguous: `x = a + (b−a)/(3^L − 1) · Σ dᵢ 3^{L−i}`.)
Worked with `<0221021121>`, `L=10`, `[a,b]=[0,100]`:
`Σ = 2·3⁸+2·3⁷+3⁶+2·3⁴+3³+3²+2·3¹+1 = 13122+4374+729+162+27+9+6+1 = 18430`;
`3¹⁰−1 = 59048`; value `= 18430/59048 · 100 ≈ 31.212`.

### Q4. Short answer
"Discuss the implications of the No Free Lunch theorem of optimization on problem-solving."

## Recalled paper C — Feb 2026 sitting (the "new structure")

- **T/F**: included a knight's-move item ("how many moves / which direction"), a base-3 item, an
  item made by adding a *"not"* to a known past-paper statement, and the offspring-pool-diversity item.
- **B1 — three-colouring construction (10):** a 4×5 grid (20 cells), colours `{1,2,3}` = red/blue/green.
  A diagonal-adjacency rule forbids a colour on the horizontal neighbours of a matched diagonal pair.
  Produce **two** valid colourings: one with colour 2 (blue) used on exactly 10 cells, one with
  colour 3 (green) on exactly 10 cells. Answer = a length-20 string, row by row.
- **B2 — fitness compute + sort (10):** roughly `f(x) = exp(… Σ xᵢ²) + exp(… Σ xᵢ) + exp(Σ cos xᵢ)`
  (a modified Ackley, *larger is better*), `n = 4`. Candidates `A=(0,0,0,0)`, `B=(1,0,0,0)`,
  `C=(0,1,1,0)`, `D=(1,1,0,0)`. Compute each `f` (3 dp), then sort ascending.
  **The recalled data is internally inconsistent:** the exact scaling inside the first exp was not
  legible (`exp(1/√n · Σxᵢ²)` vs `exp(√(1/n · Σxᵢ²))`), *and* `C` and `D` are permutations of each
  other (`{0,0,1,1}`), so any symmetric fitness gives `f(C) = f(D)` and a strict 1–4 ranking is
  impossible. Treat this as a **method drill** (evaluate the three exp terms separately, show the
  arithmetic), not a question with a unique ranking. Under either formula reading the order is
  `A > B > C = D` (larger-is-better), i.e. ascending `C = D < B < A`.
- **C1 — short answer (10):** "Explain, in your own words, what evolutionary *creativity* means."

## Cross-check against the local public archive

`../resources/public-archive-2026-08-24/exam-summary/6407考试原题.docx` (a Chinese exam-question
compilation) independently confirms the recurring **Q1 = genetic-algorithm scenario question**
pattern in the older EE6227 papers and its drift toward long applied scenarios: build an objective
function; normalise a fitness function to `[0,1]`; classify the task as optimisation / modelling /
simulation; compare real vs binary encoding; apply arithmetic recombination by formula; write the
N-bit binary string of the optimum. These older items are *pattern evidence only* — the current
Quiz 1 is the Weeks 1–3 slice above.
