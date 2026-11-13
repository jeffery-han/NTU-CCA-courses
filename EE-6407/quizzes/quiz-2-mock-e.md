# EE6407 Quiz 2 Mock E (key and rubric)

Interactive page: `quiz-2-mock-e.html`. Numbers checked by `python3 quiz-2-mock-de-check.py`.
Unofficial practice material: the format copies Mock C (`quiz-2-cycle.md`), but the numbers are chosen so they work out by hand.

## Q1: confusion matrix (40)

| Marks | Checkpoint |
|---|---|
| 8 | The matrix in rows = predicted, columns = actual: TP = 40, FP = 30 (top row); FN = 10, TN = 120 (bottom row). |
| 4 | Accuracy = (40+120)/200 = 0.8000. |
| 4 | Error rate = (30+10)/200 = 0.2000, i.e. 1 − accuracy. |
| 4 | Sensitivity = recall = 40/50 = 0.8000. |
| 4 | Specificity = 120/150 = 0.8000. |
| 4 | Precision = 40/(40+30) = 4/7 = 0.5714. |
| 4 | F-score = 2PR/(P+R) = 2TP/(2TP+FP+FN) = 80/120 = 0.6667. (The arithmetic mean 0.6857 is wrong: F is the harmonic mean.) |
| 4 | (c) Sensitivity and specificity are unchanged, because each is a rate within one actual class (column). The reason must be stated. |
| 4 | (c) With TP = 80 and FN = 20: precision rises to 80/110 = 0.7273 and F to 160/210 = 0.7619, because more positives means more TPs against the same FPs. Accuracy stays 200/250 = 0.8000 (error 0.2000) only because sensitivity = specificity: accuracy is their prevalence-weighted average. |

## Q2: 2-D k-means (40)

| Marks | Checkpoint |
|---|---|
| 6 | Iteration 1 assignment (squared distances to A(2,0) | B(5,7)): A 0|58 → c₁; B 58|0 → c₂; C 26|8, D 37|17, E 41|13 → c₂; F 4|74, G 13|17 → c₁. Clusters {A, F, G} | {B, C, D, E}. |
| 8 | Iteration 1 centroids: c₁ = mean{A, F, G} = (6/3, 3/3) = (2, 1); c₂ = mean{B, C, D, E} = (16/4, 22/4) = (4, 5.5). |
| 6 | Iteration 2: G moves to c₂ (d² = 8 vs 6.25). The others don't change (e.g. A 1 vs 34.25, F 5 vs 46.25). |
| 8 | Iteration 2 centroids: c₁ = mean{A, F} = (1, 0); c₂ = mean{B, C, D, E, G} = (20/5, 25/5) = (4, 5). |
| 6 | Iteration 3: no point changes cluster (e.g. G 18 vs 4 → c₂; A 1 vs 29 → c₁; F 1 vs 41 → c₁), so the algorithm stops. Final clusters {A, F} and {B, C, D, E, G}. |
| 6 | SSE = (1 + 1) + (5 + 1 + 10 + 10 + 4) = 2 + 30 = 32. |

## Q3: Fisher ratio + peaking (20)

| Marks | Checkpoint |
|---|---|
| 8 | Fisher ratios, with σ squared: x₁ = 4/(1+1) = 2; x₂ = 1/(0.09+0.16) = 4; x₃ = 16/(5.76+10.24) = 1; x₄ = 9/(0.36+0.64) = 9 (2 marks each). |
| 4 | Ranking x₄ > x₂ > x₁ > x₃. (If σ is left unsquared you get x₄ > x₃ > x₁ > x₂, a sign of the variance trap; ranking by the mean gap alone puts x₃ first.) |
| 8 | Peaking: a fixed N; error falls and then rises as features are added; more parameters estimated from the same N (curse of dimensionality); the optimum dimensionality grows with N; therefore select features. Roughly 2 marks per point, 8 maximum. |

