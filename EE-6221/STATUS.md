# EE-6221 status

Robotics and Intelligent Sensors.  Part 1: manipulator kinematics, robot control, mobile robots.  Part 2 (Prof. Hu Guoqiang, "HGQ"): sensors, vision, pose estimation, Kalman filter, vision-based control.  History and settled quiz details: `LOG.md`.  Paths are relative to `EE-6221/`.

## Now

- **Next assessment: final exam.**  Date, venue and format are **not recorded locally**; read NTULearn / the exam timetable first.  Quiz 1 (late Sep), Quiz 2 (4 Nov) and CA2 (due 7 Nov 2026) are over.
- Exam-scope facts on file (unofficial, from the Week 8 transcript, in `quizzes/quiz-02-intel.md`): for Part 2 the exam covers HGQ Lec 2–4.  `resources/part-2/part-2-summary.pdf` p. 1 lists per-lecture scope and depth.  Past finals put homography in Q4 and multi-sensor Kalman in Q5; mobile-robot wheel kinematics appeared as Q3 in 24-25 S1/S2 (peer tutor deck).
- Open loops:
  1. Robot control, mobile-robot kinematics and all of Part 2 are in no LaTeX note.  Part 2 Lec 1–4 exist only as HTML study pages; robot control, mobile robots and HGQ Lec 5–6 have no study page either.
  2. No Quiz 2 mistake record exists: `quizzes/quiz-02-mistakes.md` was planned and never created, and no Quiz 2 attempt is filed (the log only notes that Paper A "showed thin reasons").
  3. `resources/ee6221-tutor-exam-review-2026.pdf` pp. 27–58 (dynamics and control exam questions) are unused.
  4. No final-exam intel file yet (`quizzes/final-intel.md` does not exist).

## Notes

- `notes/beginner-notes.tex` (+ PDF) – teaching note, manipulator kinematics only (frames, rotations, homogeneous transforms, D-H, inverse kinematics, trajectory planning, Jacobians).
- `notes/notes.tex` (+ PDF) – review note, same scope.
- `notes/week-01-beginner-notes.tex` – old Week 1 supplement, kept, not maintained.
- `assignments/ca2-report/ca2-humanoid-robots-report.tex` (+ PDF) – CA2 report, complete.

## Sources

| Source (`resources/`) | Pages | Covered in | Qualifier |
|---|---|---|---|
| `lecture-01-manipulator-kinematics.pdf` | 1–156 | beginner §1–8; review note | Long manipulator derivations summarised. |
| `additional-materials/` (13 review and section PDFs) | all | partly, beginner §3–7 | Not cross-checked.  In that folder `example-3.1.pdf`, `week-05-velocity-kinematics.pdf` and `control-worked-example.pdf` are not covered. |
| `exercises-kinematics-not-for-submission.pdf`, `exercises-kinematics-solutions.pdf` | 1–2, 1–3 | Problem 1(c), 1(d) in both notes | Problem 1(a), (b) and Problem 2 not covered. |
| `lecture-02-robot-control.pdf` | 1–54 | not covered | |
| `lecture-03-mobile-robot-kinematics.pdf` | 1–40 | not covered | |
| `part-2/part-2-lecture-01…04-….pdf` (HGQ Lec 1–4) | 42, 51, 46, 45 pp. | HTML only: `output/self-studying/beginner-notes-quiz-2.html`, `quizzes/quiz-02-*.html` | No LaTeX.  Lec 2 pp. 38–51 and Lec 3 p. 18, pp. 33–36 are reference-only per the lecturer. |
| `part-2/part-2-lectures-05-06-vision-based-control-estimation.pdf` | 42 pp. | not covered | |
| `part-2/part-2-summary.pdf` | 88 pp. | not covered | HGQ's own summary; start here for exam scope. |
| `ee6221-tutor-exam-review-2026.pdf` | slides 1–59 | pp. 4–26 used in `quizzes/quiz-01-mock-05.html` | Exam-style questions, not authenticated papers.  Row-6 sign error corrected in the mock key. |
| `peer-tutor-deck-04-quiz2-mobile-kalman.pptx` | — | slides 2–10 in `quizzes/quiz-02-sprint.html` | Last year's Quiz 2 paper plus mobile-robot and Kalman exam questions. |
| `week-01…04-transcript.txt` (cleaned) | Weeks 1–4 | Weeks 1–2 in both notes; 3–4 not covered | |
| `transcripts-raw/week-01…10-transcript.txt` | Weeks 1–10 | Weeks 8–10 mined for Quiz 2 intel only | Week 11 onward not checked for upload since 27 Oct. |
| `course-syllabus.pdf`, `course-outline-part-01.pdf`, `cobot-programming-manual.pdf`, `important-notice-copyright.pdf` | all | course map only | Administrative. |
| `public-archive-2026-08-24/` | 19 files | 2015–18 and AY24-25 exam Q4/Q5 used in `quizzes/quiz-02-past-guided.html` | Unofficial solutions; two corrected in that page.  Rest unread. |

## Study pages

Open from `index.html`.  All are unofficial practice.

- Quiz 1 (kinematics): `quizzes/quiz-01-mock-01.html` … `-05.html` with keys in the matching `.md` (checker for 05: `quiz-01-mock-05-check.py`); `quiz-01-mock-02-q1-visual-answer.html` (interactive walkthrough); `quiz-01-stretch-01.html`; `quiz-01-tutor-kinematics-mock.html`.  Marked attempts: `quizzes/quiz-01-mock-0{1,2,5}-attempt-*-marked.md`, scans in `quizzes/attempts/`.
- Part 2 teaching: `output/self-studying/beginner-notes-quiz-2.html` (full lessons for Lec 1–4), `beginner-notes.html` (Quiz 1 topics), `review-page.html`.  Built from `output/self-studying/notes-bank.json` by `build-beginner.py`; validate with `node output/self-studying/check-visual-lessons.cjs`.  Never rebuild with `--mode both`.
- Quiz 2: `quizzes/quiz-02-primer.html`, `quiz-02-guided.html`, `quiz-02-past-guided.html` (real past exam questions), `quiz-02-mock-01.html` / `.md`, `quiz-02-kalman-sprint.html`, `quiz-02-sprint.html` (last year's paper + variants), `quiz-02-final-mocks.html` (Papers A, B), `quiz-02-mocks-cd.html` (Papers C, D).  Each has a checker `quizzes/<page>-check.py`.  Page images: `quizzes/quiz-02-primer-pages/`, `quiz-02-past-pages/`, `quiz-02-sprint-pages/`; KaTeX and figures in `quizzes/quiz-assets/`.
- Intel: `quizzes/quiz-01-intel.md`, `quiz-02-intel.md`.

## Unresolved

- Final-exam date, format and scope (see Now).
- Tutor deck pp. 4 and 11 both say "22-23 S2" but show different robots; the year of the p. 4 arm is unknown.
- Two illegible cells in the Mock 1 script (`quizzes/attempts/quiz-01-mock-01-2026-09-17.pdf`) were never confirmed by the learner.
