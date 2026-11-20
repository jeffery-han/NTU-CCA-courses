# EE-6221 status

Robotics and Intelligent Sensors.  Part 1: manipulator kinematics, robot control, mobile robots.  Part 2 (Prof. Hu Guoqiang, "HGQ"): sensors, vision, pose estimation, Kalman filter, vision-based control.  History and settled quiz details: `LOG.md`.  Paths are relative to `EE-6221/`.

## Now

- **Next assessment: final exam.**  Date and venue **not verified** (no NTULearn announcement on 2026-11-20; check the exam timetable).  Format, from all five official past papers in `tests/` (git-ignored): 3 h, closed book, 5 compulsory questions × 20 marks, fixed slots Q1 D-H, Q2 robot control, Q3 mobile-platform constraints + arm IK, Q4 homography, Q5 multi-sensor Kalman.  Part 2 scope HGQ Lec 2–4 (Week 8 transcript).  Evidence and conventions: `quizzes/final/final-intel.md`.
- Prep protocol (8 steps, as EE-6407): steps 1–2 built (`final-primer.html`, `final-mock-a-guided.html`).  **Next: step 3, cold Mock B** (to build), then grading and `quizzes/final/final-mistakes.md`.  Official 2025-26 S1 and S2 are reserved for steps 7–8.
- Open loops:
  1. Robot control, mobile-robot kinematics and all of Part 2 are in no LaTeX note (HTML pages only; HGQ Lec 5–6 has none).
  2. No Quiz 2 mistake record exists (`quizzes/quiz-02/quiz-02-mistakes.md` was never created).
  3. `resources/ee6221-tutor-exam-review-2026.pdf` pp. 27–58 (dynamics and control exam questions) are unused; candidate material for Mock B / H.

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
| `lecture-02-robot-control.pdf` | 1–54 | pp. 8–13, 32–54 in `quizzes/final/final-primer.html` (C1–C6) | HTML only; dynamics derivation pp. 14–31 not covered. |
| `lecture-03-mobile-robot-kinematics.pdf` | 1–40 | pp. 21–39 in `quizzes/final/final-primer.html` (M1–M3) | HTML only; wheel types, Swedish wheel, pp. 1–20 not covered. |
| `additional-materials/review-week-06-control.pdf`, `robot-control-examples-additional-info.pdf`, `review-week-07-mobile-robot-kinematics.pdf` | 1, 3, 6 | `quizzes/final/final-primer.html` | Lecturer review sheets. |
| `exercises-robot-control-not-for-submission.pdf`, `exercises-robot-control-solutions.pdf` | 1, 5 | `quizzes/final/final-primer.html` C1–C2 | Handwritten solutions. |
| `../tests/test-final-2023-24-s2.pdf` … `-2025-26-s2.pdf` | 5 papers | topic map in `quizzes/final/final-intel.md` | Official, NTU-only, git-ignored.  2025-26 S1/S2 reserved for steps 7–8. |
| `part-2/part-2-lecture-01…04-….pdf` (HGQ Lec 1–4) | 42, 51, 46, 45 pp. | HTML only: `output/self-studying/beginner-notes-quiz-2.html`, `quizzes/quiz-02/quiz-02-*.html` | No LaTeX.  Lec 2 pp. 38–51 and Lec 3 p. 18, pp. 33–36 are reference-only per the lecturer. |
| `part-2/part-2-lectures-05-06-vision-based-control-estimation.pdf` | 42 pp. | not covered | |
| `part-2/part-2-summary.pdf` | 88 pp. | not covered | HGQ's own summary; start here for exam scope. |
| `ee6221-tutor-exam-review-2026.pdf` | slides 1–59 | pp. 4–26 used in `quizzes/quiz-01/quiz-01-mock-05.html` | Exam-style questions, not authenticated papers.  Row-6 sign error corrected in the mock key. |
| `peer-tutor-deck-04-quiz2-mobile-kalman.pptx` | — | slides 2–10 in `quizzes/quiz-02/quiz-02-sprint.html` | Last year's Quiz 2 paper plus mobile-robot and Kalman exam questions. |
| `week-01…04-transcript.txt` (cleaned) | Weeks 1–4 | Weeks 1–2 in both notes; 3–4 not covered | |
| `transcripts-raw/week-01…13-transcript.txt` | Weeks 1–13 | Weeks 8–10 mined for Quiz 2 intel; Weeks 5–7, 11–13 for final intel | All 13 gallery transcripts local (2026-11-20). |
| `course-syllabus.pdf`, `course-outline-part-01.pdf`, `cobot-programming-manual.pdf`, `important-notice-copyright.pdf` | all | course map only | Administrative. |
| `public-archive-2026-08-24/` | 19 files | 2015–18 and AY24-25 exam Q4/Q5 used in `quizzes/quiz-02/quiz-02-past-guided.html` | Unofficial solutions; two corrected in that page.  Rest unread. |

## Study pages

Open from `index.html`.  All are unofficial practice.  Each assessment has its own folder under `quizzes/` (`quiz-01/`, `quiz-02/`, `final/`) holding its pages, keys, checkers, intel, page images, its own `quiz-assets/` (KaTeX + figures) and `attempts/`; rule in `docs/quiz-prep.md` "Folder layout".

- Quiz 1 (`quizzes/quiz-01/`): `quiz-01-mock-01.html` … `-05.html` with keys in the matching `.md` (checker for 05: `quiz-01-mock-05-check.py`); `quiz-01-mock-02-q1-visual-answer.html` (interactive walkthrough); `quiz-01-stretch-01.html`; `quiz-01-tutor-kinematics-mock.html`; intel `quiz-01-intel.md`.  Marked attempts: `quiz-01-mock-0{1,2,5}-attempt-*-marked.md`, scans in `attempts/`.
- Part 2 teaching: `output/self-studying/beginner-notes-quiz-2.html` (full lessons for Lec 1–4), `beginner-notes.html` (Quiz 1 topics), `review-page.html`.  Built from `output/self-studying/notes-bank.json` by `build-beginner.py`; validate with `node output/self-studying/check-visual-lessons.cjs`.  Never rebuild with `--mode both`.
- Quiz 2 (`quizzes/quiz-02/`): `quiz-02-primer.html`, `quiz-02-guided.html`, `quiz-02-past-guided.html` (real past exam questions), `quiz-02-mock-01.html` / `.md`, `quiz-02-kalman-sprint.html`, `quiz-02-sprint.html` (last year's paper + variants), `quiz-02-final-mocks.html` (Papers A, B), `quiz-02-mocks-cd.html` (Papers C, D); intel `quiz-02-intel.md`.  Each has a checker `<page>-check.py`.  Page images: `quiz-02-primer-pages/`, `quiz-02-past-pages/`, `quiz-02-sprint-pages/`.
- Final (`quizzes/final/`): `final-primer.html` (step 1, one card per slot), `final-mock-a-guided.html` (step 2, full 5 × 20 paper in checked steps); intel `final-intel.md`.  Checker `final-check.py`; page images `final-pages/`.

## Unresolved

- Final-exam date, venue and calculator rule (see Now).
- Tutor deck pp. 4 and 11 both say "22-23 S2" but show different robots; the year of the p. 4 arm is unknown.
- Two illegible cells in the Mock 1 script (`quizzes/quiz-01/attempts/quiz-01-mock-01-2026-09-17.pdf`) were never confirmed by the learner.
