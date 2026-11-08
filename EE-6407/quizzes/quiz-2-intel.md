# EE6407 Quiz 2 — scope and format evidence

Compiled 2026-11-08 from **local sources only**. No RedNote or other student-recollection search was
run for Quiz 2: the learner declined it in this session. Everything below is either a lecturer
statement in a transcript (high trust, modulo speech-recognition noise) or a pattern taken from
unofficial past-exam walkthroughs (pattern evidence only). Verify every logistic detail on NTULearn.

## Sources consulted

| Source | What it gives | Trust |
|---|---|---|
| `resources/transcripts-raw/week-05-transcript.txt`, `week-05-second-session-transcript.txt` | Assessment split. The ML part's continuous assessment is 30%: Quiz 2 10% and two assignments 10% each. Quiz on **Tuesday 10 November, the last week, 9:30–10:30 pm**. Venues LT19A and LT2A (allocation to be announced). The final exam has 4 questions: 1 GA, 3 ML. The lecturer warns that questions change every semester and that he sets more quiz questions because students reported finishing a one-hour quiz in 10 minutes. | High (lecturer statement) |
| `resources/transcripts-raw/week-11-transcript.txt` (closing minutes) | **Scope.** "The quiz include[s] the classification tree, the feature selection, and also the clustering", with feature selection and dimensionality reduction first in Week 12, then "at least half of the cluster part", and the quiz content "taught by next week". The quiz is 9:30–10:30, like Quiz 1. | High, but the ASR text is garbled; "classification three" is read here as *classification tree* |
| `resources/transcripts-raw/week-08*-transcript.txt` | No computer in the exam, so use the closed-form `w = S_W⁻¹(m₁ − m₂)` for LDA. Multiple discriminant analysis is "normally not" examined. | High |
| `resources/transcripts-raw/week-09*-transcript.txt` | "In the past years I often use this part in the exam": computing **b** from the support vectors with **α < C**, averaged. | High |
| `resources/transcripts-raw/week-10*-transcript.txt` | Tree impurity measures: entropy (log₂), Gini, misclassification. "Which impurity measure to use would be specified." | High |
| `resources/public-archive-2026-08-24/past-exam-walkthroughs-2020-2024/2[34]-S*-Q[234]*.pdf` | ML final-exam question types (2023–2024): data preparation (types, outliers, missing values, scaling); LDA two-class calculation; Gaussian and naive Bayes calculation; SVM w and b from α; LDA vs SVM comparison; accuracy, precision, recall and F; peaking phenomenon; filter feature selection; clustering-method choice; HAC single and complete linkage; k-means; DBSCAN; silhouette. | Pattern evidence; personal solutions that may contain errors |
| `resources/public-archive-2026-08-24/worked-slide-examples/2.ML/*.pdf` | Past-year slide examples (Fisher's ratio, mutual information, scatter separability, Minkowski distance, k-means and HAC steps, precision/recall). These fix the notation for the Week 12 topics. | Pattern evidence; older teaching run |

## What is known vs assumed

- **Known (lecturer):** date and time, the 10% weight, closed-book written format (same style as Quiz 1), and the ML-part scope including the classification tree, feature selection and early clustering.
- **Unknown:**
  - The question count and types. The mock assumes Quiz 1's shape: 10 T/F + calculations + a short answer.
  - Whether a calculator is allowed. Quiz 1 banned calculators. The ML lecturer only said "we cannot use a computer", so the mock uses hand-friendly numbers either way.
  - Exactly how much clustering is in scope. The mock uses the first half only: distances, k-means and HAC.
- **Missing locally:** this course's ML lecture slides, the **Week 12** recording or transcript, and any Quiz 2 past paper. NTULearn's local sync has 0 downloaded EE6407 files. Adding the Week 12 slides or transcript would settle the feature-selection and clustering scope.

## Open questions to check on NTULearn

1. The venue allocation for 10 Nov.
2. Calculator policy.
3. Whether Week 12 covered PCA or other dimensionality reduction beyond feature selection, and which clustering methods it reached.
