# EE6407 Quiz 2 — Mock Paper (machine-learning part) — KEY + RUBRIC

> **Unofficial practice paper**, written 2026-11-08. Not a real paper and not an official marking scheme.
> Open this file only **after** submitting `quiz-2-mock.html`. Every number below is verified by
> `quiz-2-mock-check.py` (run `python3 quiz-2-mock-check.py`).

## What the paper is based on

| Evidence | Source | Trust |
|---|---|---|
| Quiz 2 = ML part, 10 %, Tue 10 Nov 2026, 9:30–10:30 pm, LT19A / LT2A (allocation "announced later") | `resources/transcripts-raw/week-05-transcript.txt`, `week-05-second-session-transcript.txt`, `week-11-transcript.txt` | Lecturer statement, but machine transcript — **verify on NTULearn** |
| Scope: everything taught up to the quiz — named: classification tree, feature selection, clustering | `week-11-transcript.txt` (end) | Noisy transcript wording |
| Lecturer wants "more questions" because students finished a 1-hour quiz in 10 min | `week-05-transcript.txt` | Lecturer statement |
| Exam-flagged calculations: Bernoulli NB ("you must know this"), 2-class Fisher `w = S_W⁻¹(m₁−m₂)`, `w₀` midpoint, SVM `b` from α and C ("often in the exam"), Gini threshold search | weeks 07–10 transcripts | Lecturer statement |
| Recurring final-exam ML question forms (Gaussian Bayes, FLD, SVM w/b, metrics, filter vs wrapper / SFS, HAC single/complete, DBSCAN) | `resources/public-archive-2026-08-24/past-exam-walkthroughs-2020-2024/*-Q2…Q4` | Student walkthroughs (pattern only) |

**Not known:** question count/types, calculator policy, open/closed book. RedNote needed a login and
gave nothing. The mock therefore uses hand-computable numbers (works with or without a calculator)
and is deliberately dense (80 marks / 60 min) because of the "more questions" remark.
Week 12–13 transcripts (feature selection, clustering) were not available locally; Section C and B6
follow the past-exam patterns for those topics.

Marks: A 10×2 = 20 · B1 10 · B2 10 · B3 10 · B4 8 · B5 6 · B6 8 · C 8 → **80**.

---

## Section A — True/False (2 each: 1 for T/F, 1 for a correct reason if asked in grading)

| # | Statement (short) | Key | Why |
|---|---|---|---|
| 1 | Mean imputation suits a nominal feature like "country" | **F** | Arithmetic is meaningless on nominal data; use the **mode** (ideally per class). |
| 2 | Min–max normalisation is sensitive to outliers | **T** | One extreme value sets max/min and squashes everything else into a tiny range. |
| 3 | Linear SVM: deleting training samples with αᵢ = 0 leaves w and b unchanged | **T** | `w = Σ αᵢdᵢxᵢ` and b come only from α > 0 (support vectors). |
| 4 | Naive Bayes assumes the features are conditionally independent given the class | **T** | That is the "naive" assumption: `p(x|ω) = Π p(xⱼ|ω)`. |
| 5 | Adding a variable to multiple linear regression never decreases training R² | **T** | OLS can always set the new coefficient to 0; RSS cannot rise. That is why adjusted R² exists. |
| 6 | Gini impurity of a node with class proportions (0.5, 0.5) equals 1 | **F** | `1 − (0.25+0.25) = 0.5`. (Entropy would be 1 bit — common mix-up.) |
| 7 | A wrapper method scores subsets by a separability measure (e.g. Fisher ratio) without training a classifier | **F** | That describes a **filter**. A wrapper puts the classifier in the loop (accuracy / error rate). |
| 8 | Single-linkage HAC uses the **maximum** pairwise distance between clusters | **F** | Single = **minimum**; complete = maximum. |
| 9 | DBSCAN needs the number of clusters k in advance | **F** | It needs `eps` and `MinPts`; k emerges. |
| 10 | Leave-one-out CV on N samples trains N models | **T** | Each sample is held out once. |

Balance: 5 T / 5 F.

---

## B1 — Bernoulli Naive Bayes (10)

Data (S = Student, H = HighIncome, W = Weekend):
Buy: YNY, YYY, NYY, YNN, YNY · No: NYN, NNN, YYN.

**(a)** Priors `P(Buy)=5/8`, `P(No)=3/8`. Conditionals:
Buy: P(S=Y)=4/5, P(H=Y)=2/5, P(W=Y)=4/5 · No: P(S=Y)=1/3, P(H=Y)=2/3, P(W=Y)=0/3.

x = (S=Y, H=N, W=N):
- Buy: `5/8 · 4/5 · 3/5 · 1/5 = 3/50 = 0.0600`
- No:  `3/8 · 1/3 · 1/3 · 3/3 = 1/24 ≈ 0.0417`
- → **Buy**, posterior `0.06 / 0.10167 ≈ 0.590`.

**(b)** x = (S=N, H=Y, W=Y): Buy `5/8·1/5·2/5·4/5 = 1/25 = 0.04`; No `3/8·2/3·2/3·0 = 0`.
→ Buy with posterior 1. **Problem: zero-frequency** — one unseen feature value (W=Y never seen with
No) vetoes the whole class regardless of the other evidence.

**(c)** Laplace, `P = (count+1)/(N_class+2)`:
- Buy: `5/8 · 2/7 · 3/7 · 5/7 = 75/1372 ≈ 0.0547`
- No:  `3/8 · 3/5 · 3/5 · 1/5 = 27/1000 = 0.0270`
- → still **Buy**, posterior ≈ 0.669 (no longer a certain 1).

Rubric: priors 1 · six conditionals 2 · (a) products 2 + decision/posterior 1 · (b) identify zero-frequency 2 · (c) smoothed products + decision 2.
**Wrong paths:** forgetting the prior (decides on likelihood only) → wrong if priors matter; using P(W=Y) instead of P(W=N)=1−P(W=Y) for a "N" feature; Laplace with +1/+1 denominator (should be +2 for a binary feature, as stated).

---

## B2 — Fisher LDA (10)

Class 1: (1,2),(2,4),(3,3) · Class 2: (5,1),(6,3),(7,2).

1. `m₁ = (2,3)`, `m₂ = (6,2)`.
2. Deviations are (−1,−1),(0,1),(1,0) in **both** classes → `S₁ = S₂ = [[2,1],[1,2]]`, `S_W = [[4,2],[2,4]]`.
3. `det = 12`, `S_W⁻¹ = (1/12)[[4,−2],[−2,4]]`.
4. `w = S_W⁻¹(m₁−m₂) = (1/12)[[4,−2],[−2,4]](−4,1)ᵀ = (1/12)(−18,12) = (−1.5, 1)`.
5. `w₀ = −½wᵀ(m₁+m₂) = −½(−1.5·8 + 1·5) = 3.5`.
6. `g(x) = −1.5x₁ + x₂ + 3.5`; decide class 1 if g > 0. Check: g(m₁) = +3.5, g(m₂) = −3.5. ✔
7. x = (4,3): g = 0.5 → **class 1**; distance to boundary `0.5/‖w‖ = 0.5/√3.25 ≈ 0.277`.
   x = (4.5,2): g = −1.25 → **class 2**.

Rubric: means 1 · S₁,S₂ 2 · S_W & inverse 2 · w 2 · w₀ 1 · two classifications 1 · distance 1.
**Wrong paths:** `m₂−m₁` order → w flipped (−w); with the midpoint w₀ the rule "g>0 → class 1" then labels everything backwards — check the sign on m₁ (lecturer stressed this). Covariance (÷N or ÷(N−1)) instead of scatter: w is only scaled, decisions unchanged — accept. Forgetting the ½ in w₀.

---

## B3 — Soft-margin SVM, recover w and b (10)

C = 0.25; SVs: (3,3) d=+1 α=0.1875 · (4,2) d=+1 α=0.125 · (1,1) d=−1 α=0.0625 · (2,1) d=−1 α=0.25.

1. Check `Σαᵢdᵢ = 0.1875+0.125−0.0625−0.25 = 0` ✔.
2. `w = Σαᵢdᵢxᵢ = (0.5625+0.5−0.0625−0.5, 0.5625+0.25−0.0625−0.25) = (0.5, 0.5)`.
3. Margin SVs are those with **0 < α < C**: (3,3),(4,2),(1,1). (2,1) has α = C → bounded, inside the margin → **excluded**.
4. `b = dᵢ − wᵀxᵢ`: −2, −2, −2 → **b = −2**.
5. `f(5,0) = 2.5 − 2 = 0.5 > 0` → **+1**.
6. Margin width `2/‖w‖ = 2/0.7071 ≈ 2.828`.
7. Slack of (2,1): `ξ = 1 − d·f(x) = 1 − (−1)(−0.5) = 0.5`.

Rubric: Σαd check 1 · w 3 · identify margin SVs 2 · b 2 · classification 1 · width or ξ 1.
**Wrong paths:** averaging b over **all four** SVs gives −2.125 (concept error: bounded SVs violate `d·f = 1`); using `b = wᵀx − d` (sign); margin `1/‖w‖` (half-width).

---

## B4 — Decision tree, Gini (8)

x: 22 25 28 31 35 40 44 50 55 60 · y: N N Y N Y Y Y Y N Y. Root 6Y/4N → **Gini 0.48**.

| threshold | left | right | weighted Gini |
|---|---|---|---|
| 26.5 | NN → 0 | 6Y2N → 0.375 | **0.300** |
| 33 | 1Y3N → 0.375 | 5Y1N → 0.278 | 0.317 |
| 52.5 | 5Y3N → 0.469 | 1Y1N → 0.5 | 0.475 |
| Smoker (given) | 4Y1N → 0.32 | 2Y3N → 0.48 | 0.400 |

→ Split on **x < 26.5**; impurity drop `0.48 − 0.30 = 0.18`.
Rubric: root 1 · each of 3 thresholds 1.5 (4.5) · smoker 1 · choice + drop 1.5.
**Wrong paths:** unweighted average of child Ginis; using thresholds at data values instead of midpoints; Gini with `1 − Σp` (no square).

---

## B5 — Metrics (6)

TP 40, FN 10, FP 8, TN 142 (N = 200).
Accuracy 0.910 · Precision 40/48 = 0.833 · Recall/sensitivity 0.800 · Specificity 142/150 = 0.947 · F1 = 0.816 · FPR 0.053.
(b) Always-negative classifier: accuracy 150/200 = **0.75** but recall 0 → accuracy hides minority-class failure under imbalance; report precision/recall/F1.
Rubric: 6 metrics × 0.5 = 3 · (b) number 1 + reason 2.
**Wrong paths:** precision ↔ recall swapped; F1 as arithmetic mean (0.817 — close, but say harmonic).

---

## B6 — Clustering (8)

Points A=1, B=2, C=4.5, D=8, E=9.5.

(a) Single linkage: AB@1 → DE@1.5 → {ABC}@2.5 → all @3.5.
(b) Complete linkage: AB@1 → DE@1.5 → {ABC}@3.5 → all @8.5. Same 2-cluster cut {A,B,C} | {D,E}; the heights differ.
(c) k-means, k=2, init centroids 1 and 9.5: assign {A,B,C} | {D,E} → centroids **2.5, 8.75**; reassign: C is 2 from 2.5 vs 4.25 from 8.75 → no change → converged.
Rubric: (a) 3 · (b) 3 · (c) 2.
**Wrong paths:** mixing up single/complete; in (b) taking C–{DE} = 3.5 (that is the min, not the max = 5).

---

## Section C — Feature selection (8)

(a) Fisher ratio `(m₁−m₂)²/(σ₁²+σ₂²)` (σ² ÷ N, as in the worked example):
f1: means 2, 5; variances 2/3, 2/3 → **6.75**. f2: means 4, 5; variances 8/3, 8/3 → **0.1875**. Select **f1**. (3)

(b) Sequential forward selection with a filter criterion (5):
start empty → for each unused feature, evaluate criterion (e.g. Mahalanobis / scatter separability `tr(S_W⁻¹S_B)` or Fisher ratio) of current set ∪ {f} → add the best → repeat until k features or criterion stops improving. Cost: O(d·k) evaluations vs 2^d exhaustive; weakness: cannot remove a feature once added (nesting), may miss pairs that are only good together. Filter vs wrapper: filter = fast, classifier-independent; wrapper = classifier in the loop, better fit, costly, overfit risk.
Rubric: procedure 2 · criterion named 1 · stopping rule 1 · one limitation or filter/wrapper contrast 1.

---

## Predicted "unseen" items (not in the paper — drill these too)

Prediction only: box-plot fences `Q1 − 1.5·IQR`, `Q3 + 1.5·IQR` and whisker = nearest data value inside; z-score vs min–max; Gaussian (multivariate normal) discriminant with given means/covariances; ridge `θ = (XᵀX+λI)⁻¹Xᵀy`; R² and adjusted R²; entropy / information gain instead of Gini; DBSCAN core/border/noise labelling.
