# EE6407 final exam — scope and format evidence

Compiled 2026-11-13 after a fresh NTULearn sync (course `_2706625_1`: content, announcements and Media
Gallery). Lecturer statements in transcripts are high trust, allowing for speech-recognition noise.
Student material is **unofficial**: use it for patterns only, and re-derive every answer.
**The exam date, time and venue are NOT verified.** EE6407 is not on the NTU undergraduate exam
timetable (that timetable runs 23 Nov – 3 Dec 2026). Check the postgraduate timetable or StudentLink.

## Sources consulted

| Source | What it gives | Trust |
|---|---|---|
| `resources/transcripts-raw/week-05-transcript.txt` (+ second session) | The final has **4 questions: 1 GA + 3 ML**. Questions change every semester. | High (lecturer) |
| `resources/transcripts-raw/week-13-transcript.txt`, end section ("brief review what we have studied in the machine learning part") | The lecturer's own **ML revision list** (see "Scope" below). Exam-specific remarks: no computer in the exam, so compute LDA `w` directly rather than by SVD; for soft-margin SVM, `b` comes only from support vectors with `0 < α < C`; using all support vectors gives "wrong results"; you should be able to use **either** impurity measure. | High |
| `resources/transcripts-raw/week-13-second-session-transcript.txt` | The same review, plus: "if we have such a question … you will be instructed" which impurity measure to use. Draw dendrogram heights proportional to the merge distance, and give the similarity matrix at every step. | High |
| `resources/transcripts-raw/week-12-transcript.txt` | k-means: in a past exam most students could describe the algorithm but could not **run it** on given initial centroids and samples. | High |
| `resources/machine-learning/ml-slides-01…11-*.pdf` (NTULearn "Machine Learning Lecture Note-1…10", downloaded 2026-11-13) | The full ML deck set. These are the controlling source for formula conventions. | Official |
| `resources/public-archive-2026-08-24/exam-summary/6407考试原题.docx` | Chinese recollection of 21-22 S2, 22-23 S2, 23-24 S1, 23-24 S2 finals (under the older code EE6227) | Unofficial; question text approximate |
| `resources/public-archive-2026-08-24/past-exam-walkthroughs-2020-2024/*.pdf` (25 files) | Personal solutions per question, 20-S2 to 24-S1 | Unofficial; keys may be wrong |
| 小红书 (RedNote) | **Not searched yet**: the MCP login failed on 2026-11-11 | — |

## Format (pattern from past papers)

Every sitting from 21-22 S2 to 24-25 S1 has 4 questions. Older papers (≤ 22-23 S2) put 2 questions
on GA; from 23-24 S1 on, GA has 1 (Q1), matching the lecturer's "1 GA + 3 ML" statement. The 20-S2
paper (PSO, CNN) belongs to an older syllabus and is ignored. Duration and marks per question are
not confirmed locally.

| Sitting | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| 21-22 S2 | GA scenario (helmet; real vs binary coding) | GA: NP/TSP, distance matrix, cycle crossover | Bayes rule from μ, Σ; Fisher LDA; evaluation procedures and metrics | filter vs wrapper diagram; 3 clustering families; DBSCAN steps |
| 22-23 S2 | GA scenario (heartbeats; fitness normalisation) | GA: arithmetic recombination, 18-bit encoding | feature-selection method; Fisher LDA; k-fold CV | HAC + dendrogram; choose and describe a clustering method |
| 23-24 S1 | GA: 12-city TSP, new recombination operator | **data preparation** (types, outliers, missing values, scaling) | LDA classify; naive Bayes classify | choose a clustering algorithm for figures ×2; 5 clustering evaluation metrics |
| 23-24 S2 | GA: PID real/binary coding; voucher genotype and fitness | **SVM** primal; w, b from α; LDA vs SVM | confusion-matrix metrics; peaking phenomenon; 3 feature-subset methods | 4 clustering methods and their applications; HAC + dendrogram |
| 24-25 S1 | GA: 12-bit encoding of x, y, z | Bayes (Gaussian) + naive Bayes | Fisher LDA + SVM | HAC single then complete linkage + dendrogram; silhouette |

Pattern: the **ML calculation core** is fixed. LDA appears in 5/5 sittings and Bayes/NB in 3/5.
SVM w,b appears twice, HAC + dendrogram 3 times, and confusion-matrix metrics once in the final plus
in every Quiz 2. Descriptive parts recur: clustering families and scenarios, DBSCAN steps, feature
selection (filter/wrapper, SFS/SBS), peaking, data preparation and evaluation procedures. The
summary's author calls the ML questions highly standard ("背多分", memorise-for-marks) and the GA
question the hardest on the paper.

## Scope (lecturer's Week 13 revision list, ML part)

1. Data preparation: data types (nominal/ordinal, quantitative), missing values, outliers, standardisation `(x−μ)/σ` vs min-max normalisation to [0, 1].
2. Bayes decision rule with Gaussian class-conditional densities; naive Bayes in three forms (Gaussian, multinomial, Bernoulli with count tables).
3. Fisher LDA: `w = S_W⁻¹(m₁ − m₂)`; `w₀` from the midpoint `(m₁+m₂)/2` lying on the boundary.
4. Linear SVM: separable primal/dual; `w = Σ αᵢ yᵢ xᵢ`; `b` from support vectors (averaged); soft margin with slack and C: `b` uses only `0 < αᵢ < C`.
5. Classification trees: entropy and **Gini = ½(1 − Σp²)** (ML-Slides6 p. 14, worked 0.09 on p. 15); choosing the split feature and threshold; bagging / random forest.
6. Regression: OLS, ridge (L2), lasso (L1, which also selects variables).
7. Evaluation: holdout, repeated holdout, k-fold, repeated k-fold, leave-one-out; accuracy, sensitivity, specificity, precision, recall, F-score, and when to prefer recall vs precision.
8. Curse of dimensionality (distance concentration, sparsity); feature selection vs extraction; individual vs subset evaluation; SFS / SBS.
9. Clustering: k-means (run it by hand), agglomerative HAC + dendrogram, DBSCAN, Gaussian mixture / EM; evaluation by silhouette, Dunn and Davies–Bouldin (ML-Slides11).

GA scope for the 1 GA question: the Weeks 1–4 material already covered in `notes/` (see STATUS.md).
The final may go beyond the Quiz 1 boundary (slide 60 onward: fitness scaling, selection schemes,
population management). **Unconfirmed — check.**

## Open questions

1. Exam date, time, venue, duration, calculator policy (calculator was allowed in Quiz 2).
2. Whether GA material after the Quiz 1 boundary is examinable.
3. RedNote recollections of the 24-25 S2 / 25-26 S1 finals (not yet searched).
