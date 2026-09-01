# EE6407 Quiz 1 — Mock Paper B (with answer key and marking rubric)

**Status: unofficial.** This is a practice paper written on 2026-09-01 from
`quizzes/rednote-quiz1-intel.md` (student recollections of the 24-25 S2, 25-26 S1 and
Feb-2026 papers), `notes/beginner-notes.tex`, and
`resources/lecture-01-evolutionary-computing-part-2.pdf`. It is **not** a real paper and
**not** an official marking scheme. Every answer below was derived here and checked.

- **Interactive version:** `quizzes/quiz-1-mock-b.html` — deliberately contains **no answers**.
  Sit the paper there, export the answer sheet, and paste it into Claude Code for grading and a
  per-mistake explanation. Read this file only after you have submitted, or you lose the point of it.
- **Companion paper:** `quizzes/quiz-1-prediction.md` / `.html` is Mock Paper A. Mock B shares
  **no** items with it: A uses PMX / binary+trinary decode / graph three-colouring / NFL short answer;
  B uses order-1 + cycle / base-4 decode / fitness ranking / representation short answer.
- **Format mimicked:** 10 True/False + 3 application questions + 1 short answer, closed-book,
  Weeks 1–3 scope only (up to numbered slide 60 of the representations deck = end of tree
  representation, per `resources/week-04-transcript.txt` — note that transcript is present locally
  but **untracked by git**, so this citation resolves only in the learner's own working copy).
  No calculators — B3 supplies an
  exponential table, as a real closed-book paper would.
- **Marks:** Section A 10 × 2 = 20; B1 10; B2 10; B3 10; C 10. **Total 60.** Suggested time 60 min.

---

## Section A — True/False (10 items, 2 marks each)

| # | Statement | Key |
|---:|---|:--:|
| 1 | For a problem in NP-complete, a proposed solution can be verified in polynomial time. | **T** |
| 2 | In "class NP", the "N" abbreviates "non-polynomial". | **F** |
| 3 | In a real-valued representation, whole arithmetic recombination with \(\alpha \in [0,1]\) can produce an offspring lying outside the hyper-box spanned by the two parents. | **F** |
| 4 | Parent selection tends to reduce population diversity, while mutation tends to increase it. | **T** |
| 5 | Given measured input–output pairs from a plant whose internal workings are unknown, using a GA to search for a model that reproduces them is a *modelling* problem in the black-box characterisation. | **T** |
| 6 | A binary expression tree in which every internal node is a two-argument operator, and which has 7 leaves, contains 6 internal nodes and 12 edges. | **T** |
| 7 | An EA that uses recombination but no mutation can still, in principle, recover an allele value that has disappeared from every individual in the population. | **F** |
| 8 | For \(n = 9\), the permutation \([1,3,5,7,9,2,4,6,8]\) gives an N-queens configuration with no two queens attacking each other. | **F** |
| 9 | Branch-and-bound and simulated annealing are both examples of metaheuristics. | **F** |
| 10 | The No Free Lunch theorem implies that if algorithm A outperforms algorithm B on one class of problems, there must be another class of problems on which B outperforms A. | **T** |

### Why each answer is what it is

1. **T.** NP is *defined* as the class of problems whose candidate solutions are verifiable by a
   deterministic polynomial-time checker. NP-complete ⊆ NP, so verification is polynomial. The trap
   is confusing *verifying* a given solution (polynomial) with *finding* one (not known to be).
2. **F.** "NP" = **nondeterministic polynomial** time — polynomial time on a nondeterministic
   machine. Both halves of the wrong reading are wrong: it is not "non-polynomial", and the
   polynomial part is not negated. Past papers recycle this one almost verbatim.
3. **F.** Whole arithmetic recombination forms \(z_i = \alpha x_i + (1-\alpha) y_i\) with
   \(\alpha \in [0,1]\): a **convex combination**, so every gene lies on the segment between the two
   parent values and the child is inside the parents' hyper-box. The operator that *can* escape the
   box is **blend crossover (BLX-\(\alpha\))**, which samples from
   \([x_i - \alpha d_i,\; y_i + \alpha d_i]\) with \(d_i = |x_i - y_i|\).
   *(Note: numbered slide 27 of the Part 2 deck prints the upper limit as \(x_i + \alpha d_i\);
   that is a typo — with both limits keyed to \(x_i\) the interval would not contain \(y_i\).)*
4. **T.** Both halves hold. Parent selection is the step that *copies the good and discards the rest*,
   which strictly removes genetic material; mutation is the only operator that can introduce an allele
   value not currently present. Recombination shuffles existing material — it changes *combinations*,
   not the allele pool.
5. **T.** The black-box trichotomy: given the model \(M\) and input \(x\), find output \(y\) →
   **simulation**; given \(M\) and desired \(y\), find \(x\) → **optimisation**; given \(x\) and \(y\),
   find \(M\) → **modelling**. Input–output pairs known, system unknown ⇒ modelling. This is the same
   item as the past-paper "GA for ANN weights" question, restated forwards instead of as a trap.
6. **T.** In a tree where every internal node has exactly 2 children, \(L\) leaves force \(L-1\)
   internal nodes: \(7 - 1 = 6\). Total nodes \(= 7 + 6 = 13\); a tree has (nodes − 1) edges,
   so \(13 - 1 = 12\). Equivalently \(2(L-1) = 12\). The past-paper version of this was **F**
   (6 leaves ⇒ 10 edges, not 12) — the numbers were changed so that memorising "F" fails.
   The stem says *every internal node is a two-argument operator* for a reason: a unary `NOT`
   node would break \(L-1\).
7. **F.** Recombination can only recombine allele values already present in the parents. Once a value
   is absent from every individual, no crossover can reconstruct it — the column is fixed forever.
   Only **mutation** can reintroduce it. This is the standard argument for why mutation is
   indispensable and crossover alone is not a complete search.
8. **F.** Place queen \(i\) in column \(i\), row \(p_i\): \((1,1),(2,3),(3,5),(4,7),(5,9),(6,2),(7,4),(8,6),(9,8)\).
   A permutation already rules out row and column clashes, so only the diagonal test
   \(|q_i - q_j| = |i - j|\) matters. Take columns 3 and 6: rows 5 and 2.
   \(|6-3| = 3\) and \(|2-5| = 3\) — **equal, so they attack.** Not conflict-free.
   *Background:* this "double knight's move" construction is conflict-free exactly when \(n\) is
   divisible by **neither 2 nor 3**. \(n=5\) and \(n=7\) work; \(n=9\) fails because \(3 \mid 9\), and
   every even \(n\) fails because \((1,1)\) and \((n,n)\) share the main diagonal — that is the version
   the recalled 25-26 S1 paper used.
9. **F.** **Simulated annealing is** a metaheuristic. **Branch-and-bound is not** — it is an *exact*
   (complete) search framework that provably returns the optimum by systematically pruning subtrees
   with bounds. A metaheuristic is a stochastic, generally-applicable strategy with no optimality
   guarantee. "Both" makes the statement false. Same trap as the past-paper item, made harder by
   pairing the wrong term with a genuinely correct one.
10. **T.** NFL says that averaged over *all* possible objective functions, every search algorithm has
    identical expected performance. If A beats B somewhere, the average can only be preserved by B
    beating A somewhere else by a compensating amount. Practical reading: superiority is always
    relative to a problem class, so match the algorithm to the structure of your problem —
    there is no universally best optimiser.

---

## Section B — Application questions

### B1. Permutation crossover (10 marks: 5 + 5)

Parents, length 10 over the alphabet `A…J`:

```
P1 : A  B  C  D  E  F  G  H  I  J
P2 : C  G  A  J  E  B  I  D  F  H
       positions:  1  2  3  4  5  6  7  8  9 10
```

**(a) Order-1 crossover**, crossover segment = **positions 4–7**. Produce both children.
Fill convention (as in `notes/beginner-notes.tex` §7.6): copy the segment from one parent, then take
the *other* parent's values in that parent's own order, **starting immediately after the segment**
(position 8) and **wrapping around**, skipping any value already in the child.

**(b) Cycle crossover** on the same parents. List the cycles, then produce both offspring.

#### Answer — B1(a) order-1

Child 1 keeps P1's segment `D E F G` at positions 4–7.
Reading P2 from position 8 and wrapping: `D F H C G A J E B I`.
Deleting the segment values `{D,E,F,G}` leaves **`H C A J B I`**, which fill positions 8, 9, 10, 1, 2, 3:

```
child 1 = J  B  I | D  E  F  G | H  C  A      →  JBID EFG HCA  =  J B I D E F G H C A
```

Child 2 keeps P2's segment `J E B I` at positions 4–7.
Reading P1 from position 8 and wrapping: `H I J A B C D E F G`.
Deleting `{J,E,B,I}` leaves **`H A C D F G`**, filling positions 8, 9, 10, 1, 2, 3:

```
child 2 = D  F  G | J  E  B  I | H  A  C
```

Validity check: each child contains `A`–`J` exactly once. ✔

#### Answer — B1(b) cycle crossover

Follow position → value in P2 → that value's position in P1, until the start repeats.

| Cycle | Positions | Values (from P1) |
|---|---|---|
| 1 | 1, 3 | A, C |
| 2 | 2, 7, 9, 6 | B, G, I, F |
| 3 | 4, 10, 8 | D, J, H |
| 4 | 5 | E (fixed point: `P1[5] = P2[5] = E`) |

Positions covered: 2 + 4 + 3 + 1 = 10 ✔

Offspring 1 takes odd-numbered cycles (1, 3) from P1 and even-numbered cycles (2, 4) from P2:

```
offspring 1 = A  G  C  D  E  B  I  H  F  J
```

Offspring 2 swaps the roles:

```
offspring 2 = C  B  A  J  E  F  G  D  I  H
```

Validity check: both are permutations of `A`–`J`. ✔

#### Marking — B1 (10)

| Checkpoint | Marks |
|---|---:|
| (a) Segment copied to the *same positions* in the child | 1 |
| (a) Correct fill order: other parent's order, starting after the segment, wrapping | 2 |
| (a) Both children correct and valid permutations | 2 |
| (b) Cycles correctly traced (all four, including the fixed point at position 5) | 3 |
| (b) Both offspring assembled by alternating cycles; valid permutations | 2 |

**Common wrong paths and what they mean**
- Filling from **position 1** instead of from after the segment → you have the mechanism but not the
  convention. Half credit; state the convention next to the answer in the real paper to protect yourself.
- Filling in the *first* parent's order rather than the second's → you have inverted the roles.
  Order-1's whole point is that one parent gives **values at positions**, the other gives **relative order**.
- Cycle crossover producing a non-permutation → you copied position-by-position instead of
  cycle-by-cycle. Always run the validity check; it catches this in seconds.
- **Missing the fixed point** at position 5 is the single most common cycle-crossover error.
  When `P1[i] = P2[i]`, that position is a length-1 cycle on its own — it does not join a neighbour.

---

### B2. Number-base decoding (10 marks)

An 8-digit **quaternary** (base-4) coding system represents real values on the interval
\([-5,\; 5]\). Find the real value encoded by

```
< 3 0 2 1 3 1 0 2 >
```

Give the decoded value to 3 decimal places. State the formula you use.

#### Answer — B2

The decode map for an \(L\)-digit base-\(b\) string \(d_1 d_2 \dots d_L\) onto \([a, b']\) is

\[
\Gamma(d) \;=\; a \;+\; \frac{b' - a}{b^{L} - 1}\sum_{i=1}^{L} d_i \, b^{\,L-i}.
\]

The denominator is \(b^L - 1\), **not** \(b^L\): the largest representable string is all-\((b-1)\)s,
whose weighted sum is \(b^L - 1\), and that string must map exactly to the top of the interval.

Integer value of the string, with \(b = 4\), \(L = 8\):

| \(i\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(d_i\) | 3 | 0 | 2 | 1 | 3 | 1 | 0 | 2 |
| \(4^{8-i}\) | 16384 | 4096 | 1024 | 256 | 64 | 16 | 4 | 1 |
| product | 49152 | 0 | 2048 | 256 | 192 | 16 | 0 | 2 |

\[
\textstyle\sum = 49152 + 2048 + 256 + 192 + 16 + 2 = 51666,
\qquad 4^{8} - 1 = 65536 - 1 = 65535.
\]

\[
\Gamma \;=\; -5 + \frac{5 - (-5)}{65535}\times 51666
\;=\; -5 + \frac{10 \times 51666}{65535}
\;=\; -5 + \frac{516660}{65535}
\;=\; -5 + 7.8837\ldots
\]

\[
\boxed{\Gamma \approx 2.884}
\]

**Sanity checks.** `<00000000>` → \(-5 + 0 = -5\) ✔ (bottom of range).
`<33333333>` → \(\sum = 65535\), so \(-5 + 10 = +5\) ✔ (top of range).
Our string is a bit past the middle of the range (\(51666/65535 \approx 0.788\)), and \(2.884\) sits
78.8 % of the way from \(-5\) to \(+5\) ✔.
Resolution \(= 10/65535 \approx 1.53 \times 10^{-4}\).

#### Marking — B2 (10)

| Checkpoint | Marks |
|---|---:|
| Correct formula stated, with denominator \(b^L - 1\) | 3 |
| Weighted sum \(\sum d_i 4^{8-i} = 51666\) | 3 |
| Scale factor \((b'-a) = 10\) applied, offset \(a = -5\) added | 2 |
| Final value \(\approx 2.884\), 3 dp | 2 |

**Common wrong paths and what they mean**
- **\(4^8 = 65536\) in the denominator** → \(-5 + 516660/65536 = 2.8836\). Numerically almost identical
  here, so it will *not* be caught by the answer looking wrong. Marked down on the formula line.
  The tell that you understand it: `<33333333>` must give exactly \(+5\), which \(b^L\) does not.
- **Forgetting the \(a +\) offset** → \(7.884\), outside the interval entirely. With a negative lower
  bound this is the dominant error; the range check ("is my answer inside \([-5,5]\)?") kills it.
- **Using \((b' - a) = 5\)** (taking the upper bound as the width) → \(-5 + 3.942 = -1.058\).
  The width of \([-5, 5]\) is 10, not 5.
- **Reading digit weights right-to-left as \(4^{i}\) from \(i=0\)** is fine *provided* you reverse the
  string; mixing the two conventions is the usual source of a wildly wrong \(\sum\).

---

### B3. Fitness evaluation and ranking (10 marks)

A modified Ackley-type fitness, **larger is better**, on \(n = 3\) variables:

\[
f(\mathbf{x}) \;=\; \exp\!\left(-\frac{1}{n}\sum_{i=1}^{n} x_i^2\right)
\;+\; \exp\!\left(-\frac{1}{n}\sum_{i=1}^{n} |x_i|\right).
\]

Evaluate \(f\) for the four candidates below to **3 decimal places**, then sort them into
**ascending** order of fitness.

\[
A = (0,0,0),\qquad B = (2,0,0),\qquad C = (1,1,0),\qquad D = (1,1,1).
\]

Use this table (no calculator needed):

| \(t\) | 0 | \(2/3\) | 1 | \(4/3\) |
|---|---:|---:|---:|---:|
| \(e^{-t}\) | 1.000000 | 0.513417 | 0.367879 | 0.263597 |

#### Answer — B3

| Cand. | \(\sum x_i^2\) | \(\tfrac13\sum x_i^2\) | \(\sum \lvert x_i\rvert\) | \(\tfrac13\sum \lvert x_i\rvert\) | \(f\) | 3 dp |
|---|---:|---:|---:|---:|---|---:|
| \(A=(0,0,0)\) | 0 | 0 | 0 | 0 | \(1.000000 + 1.000000\) | **2.000** |
| \(B=(2,0,0)\) | 4 | \(4/3\) | 2 | \(2/3\) | \(0.263597 + 0.513417\) | **0.777** |
| \(C=(1,1,0)\) | 2 | \(2/3\) | 2 | \(2/3\) | \(0.513417 + 0.513417\) | **1.027** |
| \(D=(1,1,1)\) | 3 | 1 | 3 | 1 | \(0.367879 + 0.367879\) | **0.736** |

Ascending order of fitness:

\[
\boxed{D\,(0.736) \;<\; B\,(0.777) \;<\; C\,(1.027) \;<\; A\,(2.000)}
\]

**Reading the result.** \(B\) and \(C\) have the *same* \(\sum|x_i| = 2\), so their second terms are
identical; they are separated purely by \(\sum x_i^2\) (4 vs 2). The squared term punishes putting
the whole budget into **one** large coordinate, so spreading it (\(C\)) beats concentrating it (\(B\)).
\(D\) is worst because it has the largest budget overall. This is exactly why Ackley-type functions
are used as EA benchmarks: the optimum is at the origin and the landscape penalises distance from it.

#### Marking — B3 (10)

| Checkpoint | Marks |
|---|---:|
| Both sums \(\sum x_i^2\) and \(\sum \lvert x_i \rvert\) computed correctly for all four | 3 |
| The \(1/n = 1/3\) factor applied **inside** the exponent | 2 |
| Four fitness values correct to 3 dp | 3 |
| Correct **ascending** ordering \(D < B < C < A\) | 2 |

**Common wrong paths and what they mean**
- **Dropping the \(1/n\)** → you get \(e^{-4}+e^{-2}\) etc. The *ordering is unchanged*, so you can
  still score the sort marks; the values are wrong. Always keep the normalisation — it is what makes
  Ackley comparable across dimensions.
- **Sorting descending** because "larger is better" feels like it should come first → read the
  instruction word. The recalled Feb-2026 paper asked for *ascending* precisely to catch this.
- **Confusing \(\sum x_i^2\) with \((\sum x_i)^2\)** → for \(C\) that gives 4 instead of 2 and
  wrongly ties \(B\) and \(C\).
- **Assuming \(B\) beats \(C\) because \(B\) has more zeros** → sparsity is not what this \(f\)
  rewards; magnitude is. Check by computing, not by intuition.

---

## Section C — Short answer (10 marks)

> The choice of representation in an evolutionary algorithm is not a free choice.
> Explain how the representation constrains which variation operators are available, and give
> **two** concrete examples in which a mismatched representation produces invalid or meaningless
> offspring. Suggest what the algorithm designer should do in each case.

### Model answer

**The core point.** A representation is a map between the *phenotype space* (candidate solutions to
the real problem) and the *genotype space* (the data structure the EA actually manipulates). Mutation
and recombination act on the **genotype**. They are therefore only legitimate if every string they can
produce still decodes to a meaningful phenotype. So the representation does not merely *store* a
solution — it determines which operators are even definable, and a well-chosen one makes the
operators cheap while a poor one forces expensive repair or rejection.

**Example 1 — permutation genome with one-point crossover.** For a TSP tour or an N-queens
configuration, the genotype is a permutation of \(1..L\); the constraint "every value appears exactly
once" is *global*, not per-gene. One-point crossover splices two prefixes and suffixes independently,
so the child typically repeats some cities and omits others: an invalid tour. Bit-flip-style mutation
has the same problem. *Remedy:* use operators that are closed on permutations — swap, insert,
scramble and inversion for mutation; order-1, PMX, cycle or edge recombination for crossover. These
are designed so the offspring is a permutation by construction, with no repair step.

**Example 2 — binary encoding of a real-valued variable.** Encoding \(x \in [a,b]\) as an \(L\)-bit
string and using bit-flip mutation makes the *size* of a phenotypic change depend on *which* bit
flips: flipping the least significant bit moves \(x\) by one resolution step, flipping the most
significant bit moves it half the range. Worse, adjacent real values can be far apart in Hamming
distance — the **Hamming cliff**, e.g. `0111` → `1000` requires four simultaneous flips to move one
step. The genotype neighbourhood therefore does not match the phenotype neighbourhood, and local
search in genotype space is not local in the problem. *Remedy:* use **Gray coding**, so that
consecutive integers differ in exactly one bit, or move to a **real-valued representation** with
Gaussian/uniform mutation and arithmetic or blend crossover, where "small change" means the same
thing in both spaces.

*(Either of these earns full credit; a tree/GP example also works: subtree crossover is used because
splicing arbitrary sub-lists of a flattened expression would produce syntactically illegal programs.
The **closure property** — every function must accept every value any other function or terminal can
return — is exactly the representation constraint that makes untyped GP operators safe.)*

**Closing principle.** The two properties to name are **locality** (a small genotype change should
produce a small phenotype change) and **closure/validity** (operators should not be able to leave the
feasible space). Choosing a representation means choosing a neighbourhood structure on the problem,
which is the same as choosing what "search locally" will mean — and by No Free Lunch, that choice,
not the algorithm's name, is where problem-specific knowledge enters.

### Marking — C (10)

| Checkpoint | Marks |
|---|---:|
| States that operators act on the genotype, so validity of offspring is a property of the representation | 2 |
| Example 1 correct and specific (names the operator, says *why* the offspring is invalid) | 2 |
| Example 2 correct and specific | 2 |
| A concrete remedy for each example (permutation-closed operators; Gray code / real encoding) | 2 |
| Names locality and/or closure as the general principle | 2 |

**Common wrong paths**
- Describing the five representations without ever explaining the *constraint* → this is a "why"
  question, not a "list" question. Marks come from the causal link.
- Saying "the representation must suit the problem" and stopping → true but content-free.
  Every mark here is earned by a specific mechanism.
- Confusing invalidity (permutation case: offspring is not a legal solution at all) with poor
  locality (binary case: offspring is legal but the search behaves badly). These are two
  *different* failures and naming both is what separates a strong answer.

---

## Answer sheet at a glance

```
A1 T   A2 F   A3 F   A4 T   A5 T   A6 T   A7 F   A8 F   A9 F   A10 T

B1a child1 = J B I D E F G H C A        B1a child2 = D F G J E B I H A C
B1b cycles = {1,3} {2,7,9,6} {4,10,8} {5}
B1b off1   = A G C D E B I H F J        B1b off2   = C B A J E F G D I H
B2  sum = 51666, denom = 4^8-1 = 65535, x = -5 + 516660/65535 ≈ 2.884
B3  A 2.000, B 0.777, C 1.027, D 0.736  →  ascending  D < B < C < A
C   genotype-level operators; permutation + 1-point => invalid tour;
    binary real encoding => Hamming cliff; remedies = permutation-closed
    operators / Gray code; principles = locality + closure
```

## Cross-references

- Order-1 fill convention and the four permutation crossovers: `notes/beginner-notes.tex` §7.6.
- Binary→real decoding and the \(2^L - 1\) denominator: `notes/beginner-notes.tex` §7.3.
- Arithmetic vs blend crossover and the hyper-box argument: `notes/beginner-notes.tex` §7.5.
- Tree node/edge counting and the closure property: `notes/beginner-notes.tex` §7.7.
- Format, scope and past-paper evidence: `quizzes/rednote-quiz1-intel.md`.
