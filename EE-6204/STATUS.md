# EE-6204 status

Systems Analysis.  Part 1: LP / NLP (Prof. Su Rong).  Part 2: random processes, Markov chains, queueing.  Part 3: decision analysis (AHP).  History and settled quiz details: `LOG.md`.  Paths are relative to `EE-6204/`.

## Now

- **Next assessment: final exam, 60 %** (official Welcome announcement: Quiz 1 16 %, Quiz 2 16 %, Assignment 8 %, Exam 60 %).  Date, venue and format are **not recorded locally**; read NTULearn / the exam timetable first.  Quizzes 1 and 2 are over (Quiz 2 was 23 Oct 2026).
- Lecturer remarks already on file that bound the final: the Hungarian / assignment method is tested in neither Quiz 1 nor the final; branch and bound is "final-exam material" (Week 3 transcript, unofficial wording).
- Open loops:
  1. Part 2 is not in either LaTeX note; it exists only in `notes/quiz2-prep-learning.html`.
  2. Quiz 2 mock result (9/25: DTMC inventory, CTMC and all queue items weak) was drilled in `quizzes/quiz-2-followup.html` but never folded into the notes.
  3. Part 3 (decision analysis): only the AHP assignment paper is local; no lecture slides, no note, no study page.
  4. Week 4 (NLP / KKT) and Weeks 9–10 transcripts are unmined.
  5. No final-exam intel file yet (`quizzes/final-intel.md` does not exist).

## Notes

- `notes/beginner-notes.tex` (+ PDF, 13 pp.) – teaching note, Part 1 only: LP modelling, graphical method, simplex, duality, sensitivity, integer LP, transportation / assignment, NLP, KKT.
- `notes/notes.tex` (+ PDF, 14 pp.) – review note, same scope.
- `notes/week-01-beginner-notes.tex` – old Week 1 supplement, kept, not maintained.
- `slides/sensitivity-analysis-simplex-method-v2.pptx` – nine-slide sensitivity teaching deck.

## Sources

| Source (`resources/`) | Pages | Covered in | Qualifier |
|---|---|---|---|
| `lecture-01-04-linear-and-nonlinear-programming.pdf` | 1–141 | beginner §1–9; review §1–6 | Tableaux summarised selectively. |
| `introduction-to-linear-programming.pdf` | 1–43 | beginner §1–4; review §1–2 | |
| `EE6204_Exercises-part1.pdf` (keep this filename: it is an iCloud sync target) | 5 pp. | both notes, Appendix A; `notes/exercises-part1-mock.html` | Q3 tree and Q4–Q5 solutions are completed in the notes, blank in the source. |
| `week-01…03-transcript.txt` (cleaned) | Weeks 1–3 | both notes | Week 3 = exercise class. |
| `transcripts-raw/week-01…10-transcript.txt` | Weeks 1–10 | Weeks 5–8 mined for Quiz 2 intel only | Week 4 = NLP/KKT, 9–10 unmined.  Machine transcripts. |
| `part-2/lecture-00-probability-preliminaries.pdf` | 115 pp. | `notes/quiz2-prep-learning.html` (pp. 98–110 only) | No LaTeX. |
| `part-2/lecture-01-random-processes.pdf` | 72 pp. | `notes/quiz2-prep-learning.html` Modules 1–7 | Quiz depth; image-only pages not transcribed.  No LaTeX. |
| `part-2/lecture-02-queuing-models.pdf` | 33 pp. | `notes/quiz2-prep-learning.html` Module 8 | pp. 29–31 (generating functions) not reproduced.  No LaTeX. |
| `part-2/exam-appendix.pdf` | 2 pp. | summarised in `quizzes/quiz-2-intel.md` | Formula sheet given in Quiz 2: M/M/1, M/M/1/N, M/M/m, Mᵇ/M/1. |
| `part-2/two-questions-random-process-queue.pdf`, `part-2/exercises-solution.pdf` | 7, 1 pp. | worked in `notes/quiz2-prep-learning.html` | Lecturer's sample questions. |
| `part-2/main-points-lecture-{1,2,3}.pdf`, `part-2/queue-summary.pdf`, handwritten and additional notes in `part-2/` | — | consistent with the HTML page | `part-2/dtmc-ctmc-notation-comparison.pdf` (18 pp.) not read in detail. |
| `../assignments/decision-analysis-ahp-assignment.pdf` | 1–8 | not covered | Question paper only, no key. |
| `public-archive-2026-08-24/` | about 110 files | not covered | Unofficial student material; index in its `README.md`. |

## Study pages

Open from `index.html`.  All are unofficial practice.

- `notes/quiz1-prep-learning.html` – LP / simplex / sensitivity course, 10 modules, pivot walker.
- `notes/exercises-part1-mock.html` – the five Week 3 exercise problems as a marked mock.
- `notes/quiz2-prep-learning.html` – Part 2 course, 10 modules, 47 checks, steady-state solver, queue calculator; page images `notes/quiz2-pages/`.
- `quizzes/quiz-1-mcq-practice.html` / `.md` – 18-item MCQ mock in the official Quiz 1 format.
- `quizzes/quiz-1-prediction.html` / `.md` – free-response method drill (not the real format).
- `assessment/quiz.html` – second 27-item MCQ mock built with the `course-assessment` skill; its bank, key and weakness log are beside it.  Frozen; do not add new work here.
- `quizzes/quiz-2-prediction.html` / `.md` – 25-box mock in the official Quiz 2 format; checker `quiz-2-prediction-check.py`.
- `quizzes/quiz-2-followup.html` – 20-box drill on the mock's misses.
- `quizzes/quiz-2-flashcards.html` – 41 cards; not checked page by page against the PDFs.
- Intel: `quizzes/quiz-1-intel.md`, `quiz-2-intel.md`, `quiz-1-official-announcement.pdf`.

## Unresolved

- Final-exam date, format and scope (see Now).
- Four pages carry uncommitted local edits from 2026-10-15 that swap `../resources/`, `../notes/`, `../quizzes/` links for `resources-link/`, `notes-link/`, `quizzes-link/`, folders that do not exist, so those links are broken in the working copy: `notes/exercises-part1-mock.html`, `notes/quiz1-prep-learning.html`, `quizzes/quiz-1-mcq-practice.html`, `quizzes/quiz-1-prediction.html`.  The committed versions are correct.  Waiting for the learner to say revert (`git restore <file>`) or keep.
- `notes/quiz2-prep-learning.html`: one long inline formula overflows at phone width.
