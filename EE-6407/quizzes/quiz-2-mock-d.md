# EE6407 Quiz 2 Mock D (key and rubric)

Interactive page: `quiz-2-mock-d.html`. Numbers checked by `python3 quiz-2-mock-de-check.py`.
Unofficial practice material: the format copies Mock C (`quiz-2-cycle.md`), but the numbers are chosen so they work out by hand.

## Q1: confusion matrix (40)

| Marks | Checkpoint |
|---|---|
| 8 | The matrix in rows = predicted, columns = actual: TP = 80, FP = 20 (top row); FN = 20, TN = 180 (bottom row). |
| 4 | Accuracy = (80+180)/300 = 13/15 = 0.8667. |
| 4 | Error rate = (20+20)/300 = 2/15 = 0.1333, i.e. 1 − accuracy. |
| 4 | Sensitivity = recall = 80/100 = 0.8000. |
| 4 | Specificity = 180/200 = 0.9000. |
| 4 | Precision = 80/(80+20) = 0.8000. (It equals recall here only because FP = FN; the denominators are still different counts.) |
| 4 | F-score = 2PR/(P+R) = 2TP/(2TP+FP+FN) = 160/200 = 0.8000. |
| 4 | (c) Sensitivity and specificity are unchanged, because each is a rate within one actual class (column). The reason must be stated. |
| 4 | (c) With FP = 40 and TN = 360: precision falls to 80/120 = 0.6667 and F to 160/220 = 0.7273, because precision's denominator includes the FPs. Accuracy rises to 440/500 = 0.8800 and error falls to 0.1200, because the larger negative class has the higher rate (specificity 0.9 > recall 0.8). |

## Q2: 2-D k-means (40)

| Marks | Checkpoint |
|---|---|
| 6 | Iteration 1 assignment (squared distances to A(5,2) | B(5,5)): A 0|9 → c₁; B 9|0 → c₂; C 26|5, D 29|8, E 13|10, G 26|5 → c₂; F 10|13 → c₁. Clusters {A, F} | {B, C, D, E, G}. |
| 8 | Iteration 1 centroids: c₁ = mean{A, F} = (3.5, 2.5); c₂ = mean{B, C, D, E, G} = (20/5, 30/5) = (4, 6). |
| 6 | Iteration 2: E moves to c₁ (d² = 4.5 vs 8). The others don't change (e.g. F 2.5 vs 13, B 8.5 vs 2). |
| 8 | Iteration 2 centroids: c₁ = mean{A, E, F} = (9/3, 9/3) = (3, 3); c₂ = mean{B, C, D, G} = (18/4, 26/4) = (4.5, 6.5). |
| 6 | Iteration 3: no point changes cluster (e.g. E 2 vs 12.5 → c₁; B 8 vs 2.5 → c₂; A 5 vs 20.5 → c₁), so the algorithm stops. Final clusters {A, E, F} and {B, C, D, G}. |
| 6 | SSE = (5 + 2 + 1) + (2.5 + 0.5 + 2.5 + 2.5) = 8 + 8 = 16. |

## Q3: Fisher ratio + peaking (20)

| Marks | Checkpoint |
|---|---|
| 8 | Fisher ratios, with σ squared: x₁ = 4/(0.64+0.36) = 4; x₂ = 9/(1.44+2.56) = 2.25; x₃ = 4/2 = 2; x₄ = 0.25/(0.16+0.09) = 1 (2 marks each). |
| 4 | Ranking x₁ > x₂ > x₃ > x₄. (If σ is left unsquared you get x₂ first, a sign of the variance trap; ranking by the mean gap alone also puts x₂ first.) |
| 8 | Peaking: a fixed N; error falls and then rises as features are added; more parameters estimated from the same N (curse of dimensionality); the optimum dimensionality grows with N; therefore select features. Roughly 2 marks per point, 8 maximum. |

