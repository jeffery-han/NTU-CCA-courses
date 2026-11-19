# EE-6407 status

Genetic Algorithms and Machine Learning.  Part 1: evolutionary computing (GA).  Part 2 from Week 5: machine learning (Assoc Prof Mao Kezhi).  History and settled quiz details: `LOG.md`.  Paths are relative to `EE-6407/`.

## Now

- **Next assessment: final exam.**  Format is official from the four past papers: 3 h, 4 × 25 marks, Q1 GA, Q2–Q4 ML.  **Date, time and venue are not verified** (EE6407 is not on the undergraduate timetable; `quizzes/final-intel.md` gives the 23 Nov – 3 Dec 2026 exam window).  Check the postgraduate timetable or StudentLink.
- **Final-prep protocol is running**: 8 steps in `quizzes/final-intel.md` (primer → guided mock A → Mock B → retrain → Mock C → hard mock H → official 2025-26 S1 → official 2025-26 S2; the 2024-25 papers are spare).  Steps 1–2 done (learner finished Mock A on 2026-11-19).  Step 3 (Mock B) is graded.  Step 4 (relearn + retries) done; **Step 5 Mock C graded 82/100 (Mock B was 40). Next: the open items in `quizzes/final-mistakes.md` (TSP decoding, Calinski–Harabasz, Davies–Bouldin δ, SVM reasons, Fisher check), then Step 6 hard mock H (to build).**
- Open loops:
  1. The ML half of the course is in no LaTeX note; both notes are Quiz-1-only.
  2. Gini convention: the slides use ½(1 − Σp²) (`ml-slides-06` p. 14) and the final pages follow them; the older `quizzes/quiz-2-primer.html` uses 1 − Σp² and was left unchanged.
  3. Quiz 2 weak spots still untested in the final mocks (`quizzes/quiz-2-retrain-handoff.md`): confusion-matrix metrics under class-count change, 2-D k-means with SSE, Fisher-ratio ranking.  Sample-weighted Gini was done right in Mock B.
  4. The two 2023-24 EE6227 papers have not been re-read page by page.

## Notes

- `notes/beginner-notes.tex` (+ PDF, 30 pp.) – teaching note, GA Weeks 1–3: problem classes, complexity, EA loop, 8-queens, simple GA, no free lunch, five representations and their operators.
- `notes/notes.tex` (+ PDF, 15 pp.) – review note, same scope.
- `assignments/report-tex/assignments-01-02-report.tex` – submitted Assignments 1–2 report (Naïve Bayes, Fisher LDA); numbers come from `assignments/assignment-01-naive-bayes.py` and `assignments/assignment-02-fisher-lda.py`.

## Sources

| Source (`resources/`) | Pages | Covered in | Qualifier |
|---|---|---|---|
| `lecture-01-evolutionary-computing-part-1.pdf` | 1–36 | both notes | Full.  Slide-65 hand-simulation table not transcribed. |
| `lecture-01-evolutionary-computing-part-2.pdf` (representations deck) | all | both notes, written from the Week 3 transcript | No cross-check of the notes against this deck is recorded (it was thought missing until 2026-11-13).  Slide 60 onward (fitness scaling, selection schemes, population management) was outside Quiz 1 and is not in the notes. |
| `n-queens-evolution-search-paper.pdf` | 2–6 | both notes | Core method only. |
| `machine-learning/ml-slides-01…11-….pdf` (+ SVM KKT supplement, Python handout) | all | `quizzes/final-primer.html`, `final-mock-a-guided.html`, `final-mock-b`, `final-relearn`, `final-mock-c` only | No LaTeX.  Synced 2026-11-13. |
| `machine-learning/ml-revision-2026-s1.pdf` (lecturer's ML revision deck) | 1–23 | topic list in `quizzes/final-intel.md`; conventions used by `final-mock-b` | Outline plus key formulas only.  Synced 2026-11-19. |
| `week-01…04-transcript.txt` (cleaned) | Weeks 1–4 | both notes | Week 4 states the Quiz 1 scope boundary. |
| `transcripts-raw/week-01…13-transcript.txt` and `…-second-session-…` (Weeks 4–13) | Weeks 1–13 | Weeks 5–13 mined for Quiz 2 and final intel only | Each lecture is given twice; use the second session only to fill gaps.  Week 13 ends with the ML revision list. |
| `../tests/test-final-2024-25-s{1,2}.pdf`, `../tests/test-final-2025-26-s{1,2}.pdf` | all | topic map in `quizzes/final-intel.md` | **Official, git-ignored (NTU-only); never commit.**  2025-26 papers are reserved for steps 7–8: do not use their questions earlier. |
| `../tests/test-final-2023-24-s{1,2}-ee6227.pdf` | all | topic map only | Official, old course code, git-ignored. |
| `public-archive-2026-08-24/` | 124 files | four walkthroughs, the EE6227 quiz pp. 1–2 and one workbook used as question-pattern evidence | Unofficial; keys not trusted.  Rest unread. |

## Study pages

Open from `index.html`.  All are unofficial practice.

- Final: `quizzes/final-primer.html` (16 topic cards, 18 checks), `quizzes/final-mock-a-guided.html` (full 4 × 25 paper as 56 steps); checker `quizzes/final-check.py`; `quizzes/final-mock-b.html` (Step 3, cold answer-free 4 × 25 paper, 3 h countdown, export) with key/rubric `final-mock-b.md` and checker `final-mock-b-check.py`; `quizzes/final-relearn.html` (Step 4, six from-zero modules on the Mock B gaps, 23 checked steps; checker `final-relearn-check.py`); `quizzes/final-retry.html` (Step 4, cold retries of the open mistakes, 20 checked steps + 2 written; checker `final-retry-check.py`); `quizzes/final-mock-c.html` (Step 5, cold answer-free re-test, export) with key/rubric `final-mock-c.md` and checker `final-mock-c-check.py`; page images `quizzes/final-pages/`.
- Quiz 2 (ML): `quizzes/quiz-2-primer.html`; `quiz-2-mock.html` / `.md` (checker `quiz-2-mock-check.py`); `quiz-2-mock-b.html` / `.md` (`quiz-2-mock-b-check.py`); `quiz-2-cycle.html` / `.md` = Mock C with train / test / retrain drills (`quiz-2-cycle-check.mjs`); `quiz-2-mock-d.html`, `quiz-2-mock-e.html` (`quiz-2-mock-de-check.py`); `quiz-2-bus-review.html` (phone review, `quiz-2-bus-review-check.py`).
- Quiz 1 (GA): `notes/quiz1-prep-learning.html` (8 modules, 9 labs); `quizzes/quiz-1-prediction.html` / `.md` (Mock A); `quizzes/quiz-1-mock-b.html` / `.md` (answer-free).
- Intel and records: `quizzes/final-mistakes.md` (final retrain log), `quizzes/attempts/final-mock-b-2026-11-19.pdf` (Mock B script), `quizzes/final-intel.md`, `quiz-2-intel.md`, `rednote-quiz1-intel.md`, `quiz-2-retrain-handoff.md` (learner's Quiz 2 evidence as of 2026-11-10).

## Unresolved

- Final-exam date, time and venue (see Now).
- Three copies of the assignment report PDF exist (`assignments/EE6407 Assignments 1 and 2.pdf` is a pre-fix browser print; `assignments/report-tex/EE6407-Assignment1&2-HanChang.pdf` is untracked; the tracked `report-tex/assignments-01-02-report.pdf` is deleted in the working copy).  The learner should say which one was submitted.
