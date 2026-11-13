# EE6407 final exam — scope and format evidence

Compiled 2026-11-13. The primary evidence is the **official past papers** from the NTU Library
repository (Graduates folder, last three academic years). They are stored locally in `tests/` and
**git-ignored**: they are NTU-only, copyright-marked, and this backup repo is public. This file
summarises topics only. Lecturer statements come from transcripts. Student material is unofficial.
**This sitting's date, time and venue are NOT verified.** EE6407 is not on the NTU undergraduate
exam timetable (23 Nov – 3 Dec 2026). Check the postgraduate timetable or StudentLink.

## Sources consulted

| Source | What it gives | Trust |
|---|---|---|
| `tests/test-final-2024-25-s1.pdf`, `-2024-25-s2.pdf`, `-2025-26-s1.pdf`, `-2025-26-s2.pdf` (NTU Library, EE6407) | Four complete official papers | **Official** |
| `tests/test-final-2023-24-s1-ee6227.pdf`, `-2023-24-s2-ee6227.pdf` (NTU Library, old code EE6227) | Two older official papers. Not re-read page by page; topics match the docx summary below. | Official |
| `resources/transcripts-raw/week-05-transcript.txt` | Lecturer: 4 questions, 1 GA + 3 ML; questions change every semester | High |
| `resources/transcripts-raw/week-13-transcript.txt` (+ second session), end section | The lecturer's ML revision list and exam remarks (see "Scope") | High |
| `resources/transcripts-raw/week-12-transcript.txt` | k-means: in a past exam most students could not run it by hand on given centres | High |
| `resources/machine-learning/ml-slides-01…11-*.pdf` | Formula conventions (Gini = ½(1 − Σp²), ml-slides-06 p. 14) | Official |
| `resources/public-archive-2026-08-24/exam-summary/6407考试原题.docx`, `past-exam-walkthroughs-2020-2024/` | Student summaries and personal solutions | Unofficial; keys not trusted |
| 小红书 | Skipped by the learner on 2026-11-13. The official papers replace it. | — |

## Format (official, constant over all four EE6407 papers)

- **3 hours, closed book, 4 questions, answer all, 25 marks each.** Questions are split into parts of 5–18 marks.
- **Q1 = GA (25 marks), Q2–Q4 = ML.** Each GA question has two independent parts: one calculation and one shorter argument.
- Calculator: not stated on the papers. The answers need one, and one was allowed for Quiz 2.
- Large numbers are given (e.g. scatter matrices ~100), so expect 4-significant-figure hand arithmetic.

## Topic map (official papers)

| Sitting | Q1 GA | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| 24-25 S1 | 12-bit binary decoding of (x, y, z) on [−10, 10]³, binary-resolution limitation (15); real-coded fitness = estimation error from sensor points (10) | Gaussian **Bayes** rule from m, C with unequal priors 500/300 (12); **naive Bayes** on the same data (13) | **Fisher LDA** design + classify (12); separable **SVM** w, w₀ from 4 SVs and α + classify (13) | **HAC** single (9) and complete (7) linkage + dendrograms; **silhouette** (9) |
| 24-25 S2 | n-queens diagonal-conflict equation C(Q), value for an 8-queen string, fitness in [0, 1] (10); real-coded **flexible-α arithmetic crossover**, F before/after, for/against (15) | Soft-margin **SVM primal** explained (10); w, b from 6 SVs with **C = 1** (15) | **Bernoulli NB** (binary table) (10); **Fisher LDA** (10); classify + **distance to boundary** + confidence (5) | Describe **k-means** (5); choosing k (5); irregular shapes? (5); single-linkage **HAC** from a distance matrix (10) |
| 25-26 S1 | Portfolio weights Σw = 1: **whole arithmetic** and **quasi-blend** crossover with given rᵢ, validity repair (18); **black-box problem classification** — elevator control (7) | **LDA as an optimisation problem** + rationale (12); design (8); classify + confidence (5) | **Bernoulli NB** (categorical binary) (9); **multinomial NB** on word sequences (9); **Gini root-node** choice from 3 binary features (7) | Four clustering families + applications (8); **centroid-linkage** HAC, 3-D samples, dendrogram (10); **Dunn index** (7) |
| 25-26 S2 | Two-knight tour, permutation coding of 64 squares: fitness function and fitness of a given string (18); stagnation, **exploration vs exploitation** (7) | **LDA** design (12 incl. "when does LDA perform best"); classify + distance + confidence (6); LDA when **d is large relative to N** + remedy (7) | Soft-margin SVM: role of ξ and C (7); w, w₀ from 8 SVs with **C = 3** (12); classify + distance + confidence (6) | Single-linkage **HAC** (3-D) (8); **k-means 2 iterations** from given centres (12); choosing K (5) |

### Frequency (4 official EE6407 papers)

| Item | Count | Notes |
|---|---|---|
| Fisher LDA design (w = S_W⁻¹(m₁ − m₂), w₀ from midpoint) | **4/4** | S_W = S₁ + S₂ (scatter matrices given) |
| Distance to boundary \|g(x)\|/‖w‖ + confidence | **3/4** | LDA ×3, SVM ×1 |
| SVM w and b from support vectors | **3/4** | Soft margin twice: b only from 0 < α < C (α = C excluded) |
| Naive Bayes (Gaussian / Bernoulli / multinomial) | **3/4** | Bernoulli twice, multinomial once, Gaussian once |
| HAC + dendrogram | **4/4** | Single ×3, complete ×1, centroid ×1 |
| k-means: describe / run / choose K | 3/4 | Hand iteration once (25-26 S2) |
| Cluster evaluation index (silhouette, Dunn) | 2/4 | |
| Gini root-node selection | 1/4 | ½(1 − Σp²) |
| Gaussian Bayes rule with priors | 1/4 | |
| GA: crossover arithmetic on real vectors | 2/4 | Flexible-α, whole arithmetic, quasi-blend |
| GA: permutation coding + fitness (n-queens, knight tour) | 2/4 | |
| GA: binary decoding | 1/4 | |
| GA: concept (exploration/exploitation, black-box classification) | 2/4 | |
| Regression, metrics / CV, feature selection, data preparation, bagging | **0/4** | Present in older EE6227 papers (21-24). The lecturer's Week 13 list keeps them in scope, so a short part is possible. |

## Scope (lecturer's Week 13 revision list, ML part)

1. Data preparation: data types, missing values, outliers, standardisation vs min-max normalisation.
2. Bayes decision rule (Gaussian); naive Bayes: Gaussian, multinomial, Bernoulli (count tables).
3. Fisher LDA: `w = S_W⁻¹(m₁ − m₂)`; `w₀ = −wᵀ(m₁+m₂)/2`. No computer, so compute directly; SVD is not used.
4. Linear SVM: `w = Σ αᵢ dᵢ xᵢ`; b from support vectors, averaged. Soft margin: use only `0 < αᵢ < C` for b; "if you use all the support vectors you get wrong results".
5. Trees: entropy and **Gini ½(1 − Σp²)**. "You will be instructed" which measure to use. Bagging / random forest.
6. Regression: OLS, ridge (L2), lasso (L1, variable selection).
7. Evaluation procedures (holdout … LOO) and metrics (precision/recall/F, when to emphasise which).
8. Curse of dimensionality; feature selection vs extraction; SFS/SBS.
9. Clustering: k-means (run by hand), HAC with **dendrogram heights proportional to merge distance** and the distance matrix shown at each step, DBSCAN, GMM/EM; silhouette, Dunn, Davies–Bouldin.

GA scope: the whole GA part (Weeks 1–4). The official Q1s use binary decoding, real-coded
crossovers (whole arithmetic, flexible-α, blend), permutation coding with problem-specific fitness,
and the problem classification and exploration/exploitation concepts.

## Open questions

1. This sitting's exam date, time and venue; calculator policy.
2. Whether a part on regression, metrics or feature selection returns (absent in 2024-26, but in the lecturer's list).
