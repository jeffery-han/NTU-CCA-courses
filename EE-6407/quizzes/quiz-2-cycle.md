# EE6407 Quiz 2: train, test, retrain cycle (Mock C)

The interactive page is `quiz-2-cycle.html`, and every key on it is checked by `node quiz-2-cycle-check.mjs`.
This is **unofficial** practice material.

## Why this paper looks like this

The format and scope come from student recollections and classmates' messages, so treat them as unofficial and check them against the course email:

- The relayed scope is ML Lecture Notes 6–10, with deck 10 only up to k-means.
- Hierarchical clustering was reportedly said to be out of scope (unconfirmed).
- The paper is handwritten and takes 60 minutes.
- Every recalled past Quiz 2 had **two big calculation questions**, and a confusion matrix appeared in all of them.
- Other recalled items: Fisher's ratio with ranking, the peaking phenomenon as a short answer, and single-linkage hierarchical clustering (out of scope this term).
- The lecturer flagged k-means as very important in class.
- The Gini split is included only as a wildcard, because Week 11 named classification trees and the lecturer hinted at changing the format.

Conventions come from the course's worked examples:

- `7.2 Performance Evaluation Metrics.pdf`: the matrix has rows = predicted and columns = actual, laid out TP FP / FN TN.
- `9.3.1 Fisher's Ratio.pdf`: R = (m₁−m₂)²/(σ₁²+σ₂²), with the variance divided by N.
- `10.4.4 K-means-step.pdf`: assign, recompute the centroids, and repeat until nothing changes.

## Phase 1: Train (guided items, already keyed on the page)

| Module | Item | Key results |
|---|---|---|
| T1 | Shared past-paper matrix [[126, 11], [15, 100]] (rows = predicted) | N 252, Acc 0.8968, P 0.9197, R 0.8936, Spec 0.9009, F 0.9065 |
| T2 | Recalled 25-26 S1: 250+ / 150−, FN 10, FP 15 | TP 240, TN 135, P 0.9412, R 0.96, F 0.9505 |
| T3 | Worked example 9.3.1 | m₁ 1.05, m₂ 2.15, σ² 0.0125 each, R 48.4 |
| T4 | 1-D k-means on {1, 2, 4, 7, 8, 10}, starting from 1 and 4 | 1.5 / 7.25 → point 4 moves → 7/3 / 25/3, SSE 28/3 ≈ 9.3333 |
| T5 | Gini: 5+/3−, split into 4/0 and 1/3 | root 0.46875, right child 0.375, weighted 0.1875, gain 0.28125 |
| T6 | Peaking phenomenon | the five marking points below |

## Phase 2: Test (100 marks, 60 min)

### Q1: 160 positive, 240 negative, 25 missed, 30 falsely flagged (40)

| Part | Answer | Marks |
|---|---|---|
| (a) | Rows = predicted: [[TP 135, FP 30], [FN 25, TN 210]] | 8 |
| (b) | Acc 345/400 = 0.8625; error 0.1375; sensitivity = recall 135/160 = 0.8438; specificity 210/240 = 0.8750; precision 135/165 = 0.8182; F 270/325 = 0.8308 | 6 × 4 |
| (c) | Sensitivity and specificity are unchanged (each is a rate within one class) | 4 |
| (c) | FP 60, TN 420 → precision 135/195 = 0.6923, F 270/355 = 0.7606; accuracy 0.8672, error 0.1328 | 4 |

**Common wrong paths, and what each means:**
- Swapping FP and FN. You read the table with actual as the rows, which is an orientation error.
- Precision = 135/160. You used the recall denominator, so the two concepts are inverted.
- Averaging P and R arithmetically. You forgot that F is the harmonic mean.
- In (c), saying "every metric halves". You haven't seen that class-conditional rates don't depend on prevalence.

### Q2: 2-D k-means, k = 2, starting from c₁ = A(1,1) and c₂ = B(2,1) (40)

| Part | Answer | Marks |
|---|---|---|
| (a) | Squared distances to (A \| B): A 0\|1, B 1\|0, C 4\|5, D 25\|18, E 41\|32, F 25\|20, G 8\|5. Assign {A, C} \| {B, D, E, F, G} | 6 |
| (a) | c₁ = (1, 2), c₂ = (4, 3.6) | 8 |
| (b) | B moves to c₁ (d² = 2 vs 10.76); G stays (5 vs 1.36) | 6 |
| (b) | c₁ = (4/3, 5/3), c₂ = (4.5, 4.25) | 8 |
| (c) | Iteration 3: B 0.89 vs 16.81, G 4.56 vs 3.81, and nothing moves. Final clusters {A, B, C} and {D, E, F, G} | 6 |
| (d) | SSE = 10/3 + 31/4 = 133/12 ≈ 11.0833 | 6 |

**Common wrong paths, and what each means:**
- Stopping after iteration 1. You haven't learned the convergence condition.
- Keeping B in cluster 2. You didn't recompute the distances against the new centroids.
- Updating one centroid at a time inside the assignment pass. That is the online variant, not the batch algorithm the course uses.
- Giving SSE as a sum of unsquared distances.

### Q3: Fisher's ratio and peaking (20)

| Part | Answer | Marks |
|---|---|---|
| (a) | R: x₁ = 4, x₂ = 1, x₃ = 2, x₄ = 1.44 | 4 × 2 |
| (a) | Rank x₁ > x₃ > x₄ > x₂ | 4 |
| (b) | Five points: fixed N; error falls then rises as features are added; more parameters estimated from the same N (curse of dimensionality); the optimum dimensionality grows with N; therefore select features | 8 |

**Common wrong paths, and what each means:**
- Putting x₃ first. You left σ unsquared, which gives x₃ = 3 and x₁ = 2.857.
- Ranking by |m₁ − m₂| alone. You ignored the class spread.
- Calling peaking "overfitting from too many training epochs". You confused it with a different phenomenon; peaking is about the number of features relative to N.

## Phase 3: Retrain

Retrain unlocks once you submit the test:

- You tick only the rubric checkpoints you earned. Each topic with an unticked checkpoint becomes **open**.
- Open topics get random problems from `genCM` (with random table orientation), `genFR`, `genKM` (1-D, always needs at least one reassignment) and `genGini`.
- A topic closes after **two fully correct problems in a row**. The peaking topic closes when your rewritten paragraph covers all five points.
- **Export** produces a plain-text record of the session (train misses, self-mark, missed checkpoints, retrain status) to paste back for diagnosis and for the mistakes log.
