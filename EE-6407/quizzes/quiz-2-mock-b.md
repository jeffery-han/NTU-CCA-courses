# EE6407 Quiz 2 — Mock Paper B (answer key + marking rubric)

**Unofficial practice paper**, written 2026-11-08 for the machine-learning part of EE6407. It is not a
real paper and the marking scheme below is not the lecturer's. Sit
[`quiz-2-mock-b.html`](quiz-2-mock-b.html) first; open this file only after submitting.

- **Order:** sit [`quiz-2-mock.html`](quiz-2-mock.html) first. Mock B is the follow-up paper for after its mistakes have been reviewed. It covers the same syllabus with different numbers, and adds traps the first paper lacks: a bounded SV inside the b average, a misclassification-impurity tie, linkage disagreement and the imbalanced-accuracy paradox.
- **Scope used:** the ML lectures, Weeks 5–12. The Week 11 lecture states that the quiz includes
  the classification tree, feature selection and the clustering taught by Week 12
  (`resources/transcripts-raw/week-11-transcript.txt`, end of lecture). See
  [`quiz-2-intel.md`](quiz-2-intel.md) for the evidence and its gaps.
- **Shape is a prediction.** No Quiz 2 past paper is available locally. The shape copies Quiz 1
  (10 True/False + calculations + short answer, one hour) and the calculation types that recur
  in the ML final-exam questions 2023–2024.
- **Every numeric answer is asserted in [`quiz-2-mock-b-check.py`](quiz-2-mock-b-check.py)**
  (`python3 EE-6407/quizzes/quiz-2-mock-b-check.py` → `all asserts passed`).
- **Total: 70 marks** — A 20, B1 10, B2 10, B3 10, B4 10, C 10.

---

## Section A — True / False (10 × 2 = 20)

One mark for the verdict, one for a correct reason when the learner gives one. With a verdict
only, award 2 for a right verdict. Confidence class in brackets.

| # | Statement (short) | Key | Reason | Class |
|---|---|---|---|---|
| 1 | °C temperature is ratio data, so 30 °C is twice as hot as 15 °C | **F** | °C is **interval** data: 0 °C is not "no temperature", so differences are meaningful but ratios are not (Week 6). | Derivable |
| 2 | Impute missing values of a **nominal** feature with the mean | **F** | A mean needs arithmetic on the values; nominal codes only say "different". Use the **mode** (Week 6; 23-S1 Q2 walkthrough). | Derivable |
| 3 | Gaussian naive Bayes ≡ replacing each class covariance by its diagonal | **T** | Independence within a class ⇒ zero off-diagonal covariances, so the joint Gaussian factorises into 1-D Gaussians (24-S1 Q2 walkthrough). | Derivable |
| 4 | Scaling LDA's `w` and `w0` by the same positive constant changes some predictions | **F** | `g(x) = wᵀx + w0` only matters through its sign; `k·g(x)` has the same sign for `k > 0`. | Derivable |
| 5 | Deleting an α = 0 training sample and retraining leaves the SVM boundary unchanged | **T** | `w = Σ αᵢ dᵢ xᵢ` and `b` use only support vectors (α > 0). The old solution still satisfies every constraint without that point, so it is still optimal. | Derivable |
| 6 | In soft-margin SVM, every SV with αᵢ = C lies exactly on the margin | **F** | αᵢ = C marks a **bounded** SV: inside the margin or misclassified (ξᵢ > 0). Points exactly on the margin have **0 < αᵢ < C**, and only those are used to compute `b` (Week 9). | Derivable |
| 7 | A 50/50 two-class node has entropy impurity = Gini impurity = 1 | **F** | Entropy = −2·0.5·log₂0.5 = **1**, but Gini = 1 − (0.25 + 0.25) = **0.5** (Week 10). | Derivable |
| 8 | In 10-fold CV each sample is tested exactly once and used for training nine times | **T** | The data are split into 10 disjoint folds. Each fold is the test set once, and in the other nine rounds it is part of the training set (Week 11). | Derivable |
| 9 | With N fixed, adding features can *increase* test error | **T** | This is the **peaking phenomenon**: performance first improves, then degrades past a critical number of features for a finite N (23-S2 Q3 walkthrough). | Convention-dependent (lecturer names it "peaking") |
| 10 | Euclidean k-means reaches the same clusters from any initial centroids | **F** | k-means only descends to a local optimum of the within-cluster sum of squares. The result depends on initialisation, which is why it is restarted several times. | Derivable |

**Common wrong paths.**
- A1 "T": the learner treats any numeric scale as ratio. Ask what zero means.
- A5 "F": the learner thinks all training data shape the SVM. That is the LDA mindset: LDA uses every sample, SVM only the support vectors.
- A6 "T": the learner has the αᵢ = C and 0 < αᵢ < C roles swapped. This is the same gap B2 tests, so check both together.
- A7 "T": the learner remembers "maximum impurity = 1" for entropy and assumes Gini shares the scale.

---

## Section B1 — Fisher LDA, two classes (10)

Data: ω₁ = {(1,1), (2,3), (3,2)}, ω₂ = {(5,3), (6,5), (7,4)}. Test points (3.5, 5) and (4.5, 0).

| Step | Result | Marks |
|---|---|---|
| Means | m₁ = (2, 2), m₂ = (6, 4) | 1 |
| Class scatter matrices `Sᵢ = Σ (x − mᵢ)(x − mᵢ)ᵀ` | S₁ = S₂ = [[2, 1], [1, 2]] (deviations (−1,−1), (0,1), (1,0) in both classes) | 2 |
| Within-class scatter | S_W = S₁ + S₂ = [[4, 2], [2, 4]], det = 12 | 1 |
| Inverse | S_W⁻¹ = (1/12)·[[4, −2], [−2, 4]] | 1 |
| Direction | w = S_W⁻¹(m₁ − m₂) = (1/12)·[[4,−2],[−2,4]]·(−4, −2) = (1/12)(−12, 0) = **(−1, 0)** | 2 |
| Threshold | w₀ = −½ wᵀ(m₁ + m₂) = −½·(−1)·8 = **4** | 1 |
| Discriminant | g(x) = −x₁ + 4; classify ω₁ if g > 0, ω₂ if g < 0 | — |
| Test points | g(3.5, 5) = **+0.5 → ω₁**; g(4.5, 0) = **−0.5 → ω₂** | 1 |
| (c) Why x₂ is ignored | The means differ in x₂ (2 vs 4), but x₂ is correlated with x₁ inside each class. Once S_W⁻¹ removes that shared within-class spread, x₂ adds no separation beyond x₁, so its weight is 0. Using m₁ − m₂ alone would give (−4, −2) and wrongly weight x₂. | 1 |

**Common wrong paths.**
- Using *covariance* (÷N or ÷(N−1)) instead of *scatter* changes S_W by a positive factor. That rescales w but does **not** change any classification, so give full method marks if the learner was consistent. Note it, but deduct nothing.
- Computing w = S_W⁻¹(m₂ − m₁) flips the sign of g. That is fine *only if* the decision rule is flipped too. Deduct 1 if the rule was not flipped.
- Writing w₀ = +½ wᵀ(m₁ + m₂) gives the wrong side for both test points. That is a sign-convention gap, not a slip.
- Inverting a 2×2 matrix without swapping the diagonal and negating the off-diagonal entries is an arithmetic slip.

---

## Section B2 — soft-margin SVM: w and b from the α values (10)

C = 1.5. Training samples (x, d, α): (2,2,+1, 1.0), (3,1,+1, 0.75), (1,1,−1, 0.25), (2,1,−1, 1.5),
(4,4,+1, 0), (0,0,−1, 0).

| Part | Key | Marks |
|---|---|---|
| (a) Check Σαᵢdᵢ = 0 | 1 + 0.75 − 0.25 − 1.5 = 0 ✓ | 1 |
| (b) w = Σ αᵢ dᵢ xᵢ | (2,2) + 0.75(3,1) − 0.25(1,1) − 1.5(2,1) = (2 + 2.25 − 0.25 − 3, 2 + 0.75 − 0.25 − 1.5) = **(1, 1)** | 3 |
| (c) Classify the SVs | **Margin SVs** (0 < α < C): (2,2), (3,1), (1,1). **Bounded SV** (α = C): (2,1). **Not SVs**: (4,4), (0,0) | 2 |
| (d) b from margin SVs only, `b = dₛ − wᵀxₛ`, averaged | (2,2): 1 − 4 = −3; (3,1): 1 − 4 = −3; (1,1): −1 − 2 = −3 ⇒ **b = −3** | 2 |
| (e) Classify test points with f(x) = wᵀx + b | f(3, 0.5) = **+0.5 → +1**; f(1, 1.5) = **−0.5 → −1** | 1 |
| (f) Position of (2,1) | f(2,1) = 0, so it lies **on the decision boundary**, inside the margin, with slack ξ = 1 − d·f = **1** | 1 |

**Common wrong paths.**
- **Including the bounded SV in the b average** gives (−3 −3 −3 −4)/4 = **−3.25**. This is the main concept being tested: a bounded SV does not satisfy dₛ(wᵀxₛ + b) = 1, so it cannot pin b. Award 0/2 for (d), and record it as a concept gap.
- Leaving out dᵢ in w = Σ αᵢ dᵢ xᵢ gives (5.5, 4.5). That is a concept gap: the labels set the direction.
- Treating α = 0 points as support vectors.

---

## Section B3 — classification tree: choosing the root split (10)

Root: 16 samples, 8 ω₁ / 8 ω₂. Split A → left (6 ω₁, 2 ω₂), right (2 ω₁, 6 ω₂). Split B → left (4, 0), right
(4, 8). Given log₂3 ≈ 1.585.

The impurity drop is Δi = i(N) − P_L·i(N_L) − P_R·i(N_R).

| Measure | i(root) | Split A | Split B | Winner | Marks |
|---|---|---|---|---|---|
| Entropy | 1 | children H(¼,¾) = 2 − ¾·log₂3 = 0.8113 each → Δ = **0.1887** | left 0, right H(⅓,⅔) = log₂3 − ⅔ = 0.9183, weighted ¾·0.9183 = 0.6887 → Δ = **0.3113** | **B** | 4 |
| Gini | 0.5 | children 1 − (9/16 + 1/16) = 0.375 → Δ = **0.125** | right 1 − (1/9 + 4/9) = 4/9; ¾·4/9 = 1/3 → Δ = **1/6 ≈ 0.1667** | **B** | 3 |
| Misclassification | 0.5 | children 0.25 → Δ = **0.25** | right 1/3; ¾·1/3 = 0.25 → Δ = **0.25** | **tie** | 2 |
| (d) Comment | Misclassification impurity cannot tell the splits apart, even though B produces a **pure** left node. Entropy and Gini are strictly concave, so they reward purer children. This is why entropy is the usual choice. | | | | 1 |

**Common wrong paths.**
- Forgetting the child weights P_L, P_R (averaging the child impurities 50/50) gives B: 1 − (0 + 0.9183)/2 = 0.541. The winner comes out the same by luck, but award 0 for method.
- Reading "Gini = 1 − Σp" or squaring the wrong thing.
- Natural logs instead of base 2 for entropy. The ranking is unchanged but the values are wrong; deduct 1.

---

## Section B4 — feature ranking and hierarchical clustering (10)

### (a) Fisher's ratio (4)

FR = (m₁ − m₂)² / (σ₁² + σ₂²), with σ² dividing by N (the archive convention, worked example 9.3.1).

| Feature | ω₁ | ω₂ | means | σ₁², σ₂² | FR |
|---|---|---|---|---|---|
| f₁ | 1, 2, 3 | 4, 5, 6 | 2, 5 | 2/3, 2/3 | 9 / (4/3) = **6.75** |
| f₂ | 0, 4, 8 | 6, 10, 14 | 4, 10 | 32/3, 32/3 | 36 / (64/3) = **1.6875** |

Rank: **f₁ > f₂**. f₂ has the larger mean gap, but its classes are far more spread out, so they
overlap more. (Dividing by N−1 gives 4.5 and 1.125: the same ranking, so award full marks.)

### (b) HAC, Manhattan distance (6)

Points A(0,0), B(0,1), C(0,3), D(3,0), E(6,1). Distance matrix (2 marks):

```
     A  B  C  D  E
A    0  1  3  3  7
B    1  0  2  4  6
C    3  2  0  6  8
D    3  4  6  0  4
E    7  6  8  4  0
```

| Linkage | Merge sequence (height) | 2-cluster cut | Marks |
|---|---|---|---|
| Single (min) | AB (1) → ABC (2) → ABCD (3) → ABCDE (4) | **{A,B,C,D}, {E}** | 2 |
| Complete (max) | AB (1) → ABC (3) → DE (4) → ABCDE (8) | **{A,B,C}, {D,E}** | 2 |

Single linkage *chains*: D joins via its nearest neighbour A (distance 3) even though D is 6 from C.
Complete linkage judges a cluster by its farthest pair, so it keeps compact groups.

**Common wrong paths.**
- Euclidean instead of Manhattan: the question names the metric. Every height changes, so deduct the distance-matrix marks and re-mark the merges against the learner's own matrix.
- Complete linkage implemented as "distance between the two newest members".
- Using single-linkage heights in a complete-linkage dendrogram.

---

## Section C — evaluation on imbalanced data (10)

1000 test samples, 50 positive. Classifier A predicts everything negative. Classifier B: TP 40, FN 10,
FP 60, TN 890.

| Item | A | B | Marks |
|---|---|---|---|
| Accuracy | 950/1000 = **95%** | 930/1000 = **93%** | 2 |
| Precision TP/(TP+FP) | **undefined** (0/0, no positive predictions) | 40/100 = **0.40** | 2 |
| Recall TP/(TP+FN) | 0/50 = **0** | 40/50 = **0.80** | 2 |
| F1 = 2PR/(P+R) | **0** | 2·0.4·0.8/1.2 = **0.533** | 1 |
| Argument | Accuracy rewards A for copying the majority class. With 95% negatives, "always negative" already scores 95%. B finds 80% of the positives, so it is the useful classifier, and only precision, recall and F1 show this. | | 2 |
| Procedure | Use **stratified** k-fold cross-validation, so every fold keeps the 5% positive rate and a fold never ends up with no positives. Accept "repeat hold-out several times and report mean ± std" for 0.5. | | 1 |

**Common wrong paths.**
- Precision = TP/(TP+FN). That is recall; check whether the two were swapped consistently.
- Calling A's precision "0" rather than undefined. Accept it with a note; the point is that it is not a number you can rank on.
- Choosing A because 95% > 93%.

---

## Predicted unseen item (not in this paper)

From the ML final-exam questions 2023–2024 and the archive's worked examples (labelled prediction,
not evidence):
- **Gaussian / naive Bayes discriminant with numbers** (23-S1 Q3b, 24-S1 Q2). The likeliest heavy calculation; it was left out here only to keep one hour realistic.
- **Mutual information from a joint table** (worked example 9.3.2), as the feature-selection alternative to Fisher's ratio.
- **k-means: one assignment-and-update iteration** (the Week 12 first-half clustering material).
- **Data-preparation short answer**: data types, outliers via the 1.5·IQR rule, imputation, min-max vs z-score (23-S1 Q2).
