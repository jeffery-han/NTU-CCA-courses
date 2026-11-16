# EE-6203 status

Computer Control Systems.  Three teaching blocks: C. Wen Ch 1–4 (Weeks 1–4), Lee Peng Hin "LPH" Lect 1–5 (state space, optimal control), C. Wen Ch 5–6 (Weeks 10–12).  History and settled quiz details: `LOG.md`.  Paths are relative to `EE-6203/`.

## Now

- **Next assessment: final exam.**  Date, venue, format and scope are **not recorded locally**; read NTULearn / the exam timetable before any prep.  Quizzes 1–3 are over (Quiz 3 was 7 Nov 2026).
- Open loops:
  1. Quiz 3 mistakes are still open: retries R1–R6 and the Mock D items in `quizzes/quiz-03-mistakes.md`.  Ripple-free deadbeat was left blank in both Mock A and Mock D.
  2. No LaTeX note covers anything after Ch 4 (LPH Lect 1–5, Wen Ch 5–6).  Those topics exist only as HTML study pages.
  3. LPH Lect 4–5 (observers, integral control, LQR) have no study page and no note at all.
  4. No final-exam intel file yet (`quizzes/final-intel.md` does not exist).

## Notes

This course uses its own note filenames instead of `beginner-notes.tex` / `notes.tex`; keep them.

- `notes/quiz1-prep-learning.tex` (+ PDF, 30 pp.) – teaching note, Ch 1–4, with a Quiz 1 appendix.
- `notes/quiz1-prep-reviewing.tex` (+ PDF, 9 pp.) – review note, Ch 1–4.
- `notes/week-01-zero-background-notes.tex` – old Week 1 supplement, kept, not maintained.
- `notes/quiz1-prep-reviewing-pre-rename-2026-08-24.pdf` – superseded build, kept for traceability.

## Sources

| Source (`resources/`) | Pages | Covered in | Qualifier |
|---|---|---|---|
| `lecture-notes-weeks-01-04.pdf` (Wen Ch 1–4) | 1–225 | both `.tex` notes; `notes/quiz1-prep-learning.html` | Full at note depth.  pp. 196–225 are a recap.  Ch 4 = pp. 144–195. |
| `course-exercises.pdf`, `course-exercises-solutions.pdf` | 1–5, 1–26 | both `.tex` notes (representative methods) | Solutions are an unofficial compilation; re-derive before use. |
| `lph-lecture-01-…pdf`, `-02-…`, `-03-…` (§1–13) | 28, 20, 31 pp. | `notes/quiz2-prep-learning.html` only | No LaTeX.  Ex 1.3, 1.8, 2.8, 2.9, 3.6 summarised, not worked. |
| `lph-lecture-01-slide-40-theta-note.pdf`, `lph-matrix-basics-summary.pdf` | 1, 3 pp. | `notes/quiz2-prep-learning.html` Modules 3, 0 | |
| `lph-lecture-04-observers-integral-control.pdf` (§14–21) | 30 pp. | not covered | |
| `lph-lecture-05-optimal-control-lqr.pdf` (§22–23) | 26 pp. | not covered | |
| `lph-transform-table-ay2018-19-s1.pdf` | 2 pp. | not covered | The table issued in LPH's quiz and exam. |
| `lecture-notes-chapters-05-06.pdf` (Wen Ch 5–6) | 1–151 | `quizzes/quiz-03-primer.html` only | Primer depth.  Ex 5.5, Ex 5.13 and §6.6–6.7 summarised.  No LaTeX. |
| `week-01…07-transcript.txt` (cleaned) | Weeks 1–7 | Weeks 1–3 in the `.tex` notes; 4–7 mined for quiz rules only | Week 7 file is the 26 Sep make-up lecture. |
| `transcripts-raw/week-01…12-transcript.txt` | Weeks 1–12 | Weeks 8–12 raw only; 10–12 mined for Quiz 3 intel | Machine transcripts; do not adopt their wording. |
| `public-archive-2026-08-24/` | 163 files | four 2022–23 walkthroughs, one Ch 4 example, two explainers used as question-pattern evidence | Unofficial student material; index in its `README.md`.  Rest unread. |

## Study pages

Open from `index.html`.  All are unofficial practice.

- `notes/quiz1-prep-learning.html` – Ch 1–4 course, 6 modules, 48 checks, 2 mocks.
- `notes/quiz2-prep-learning.html` – LPH Lect 1–3 from zero, 12 modules, 71 checks; checker `notes/quiz2-prep-learning-check.py`; slide images `notes/quiz2-slides/`.
- `quizzes/quiz-01-evaluation-set.html` (+ `…-solutions.tex/.pdf`) – 44-item Ch 1–3 diagnostic.
- `quizzes/quiz-01-prediction-papers.html` – four Quiz 1 papers.
- `quizzes/quiz-02-prediction-paper.html` / `.md` – one 25-mark question; checker `quiz-02-prediction-check.py`.
- `quizzes/quiz-02-mock-tests.html` / `.md` – three 3-question papers; checker `quiz-02-mock-tests-check.py`.
- `quizzes/quiz-02-mock-test-a-solutions.html`, `quiz-02-mock-q1-rlc-explainer.html`, `quiz-02-transfer-function-explainer.html`, `quiz-02-complete-process-explainer.html` (checker `quiz-02-complete-process-check.py`) – worked walkthroughs for Test A.
- `quizzes/quiz-02-quick-reminder.html` – one-page Quiz 2 recall sheet.
- `quizzes/quiz-03-primer.html` – Ch 4–6 primer with beginner "Start here" blocks; checker `quiz-03-check.py`; page images `quizzes/quiz3-pages/`.
- `quizzes/quiz-03-mock-a.html` / `.md` (answer-free), `quiz-03-mock-b.html` / `.md` (step-by-step walkthrough) – checker `quiz-03-check.py`.
- `quizzes/quiz-03-mock-c.html`, `quiz-03-mock-d.html` – timed papers in the real Quiz 3 format (4 MCQ + 3 written); checker `quiz-03-mock-cd-check.py`.
- `quizzes/quiz-03-commute.html` – phone cram sheet ordered by marks lost.
- Intel and records: `quizzes/quiz-02-intel.md`, `quiz-03-intel.md`, `quiz-03-mistakes.md`, `attempts/`.

## Unresolved

- Final-exam date, format and scope (see Now).
- Whether the final follows the quiz pattern per block; no 2024–2026 exam paper is held locally (the archive stops at AY2018-19 solutions and 2015–2023 personal walkthroughs).
