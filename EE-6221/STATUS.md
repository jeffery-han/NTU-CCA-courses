# EE-6221 note status

## Note files

- `quizzes/quiz-01-stretch-01.html` is an answer-free, offline seven-joint D–H stretch exercise adapted from the user-supplied tutor deck's slide 11. Its cropped source diagram is `quizzes/quiz-assets/ee6221-2022-2023-s2-q1-seven-joint-figure.png`. The deck labels the source as "22–23 S2 Q1" in a semester-exam review, so this is not presented as a past Quiz 1 paper or a format prediction.
- `quizzes/quiz-01-mock-04.html` is an answer-free final practice check with offline SVG top/side views: an articulated RRR D–H/translation problem and a pick/place grasp-axis problem. `quizzes/quiz-01-mock-04.md` is its separate verified key and rubric. The 18/20 threshold is a learner-facing study signal, not an official quiz rule. Topic sources: `resources/exercises-kinematics-not-for-submission.pdf` p. 2 and `resources/lecture-01-manipulator-kinematics.pdf` pp. 57–58, 61–70, 74–76; question shape remains based partly on the unofficial recollections in `quizzes/quiz-01-intel.md`.
- `quizzes/quiz-01-mock-03.html` is a new answer-free, offline Quiz 1 practice paper with two SVG diagrams: an RRP frame/D–H question and a pick/place question testing jaw closing direction. `quizzes/quiz-01-mock-03.md` is its separate answer key and marking guide. Its two-question shape uses the official practice exercise and unofficial prior-student recollections in `quizzes/quiz-01-intel.md`; it is not a past quiz. Optional Section C covers inverse transforms and the tool configuration vector. Sources: `resources/exercises-kinematics-not-for-submission.pdf` p. 2 and `resources/lecture-01-manipulator-kinematics.pdf` pp. 57–58, 82–84.
- `notes/beginner-notes.tex` - detailed, self-contained teaching note for the supplied manipulator-kinematics material; compiled PDF is stored beside it.
- `notes/notes.tex` - concise manipulator-kinematics review note; compiled PDF is stored beside it.
- `notes/week-01-beginner-notes.tex` - preserved Week 1-only teaching supplement; it is not the canonical full-scope beginner note.
- `quizzes/quiz-01-mock-01.html` + `quizzes/quiz-01-mock-01.md` - answer-free mock Quiz 1 (exam page) and its answer key / marking rubric / diagnosis guide. `quizzes/quiz-01-intel.md` records the past-paper intelligence it is built on (logged-in RedNote search + KuRRe8 GitHub study note + the official `exercises-kinematics-not-for-submission.pdf`). `quizzes/quiz-01-mock-02.html` + `quizzes/quiz-01-mock-02.md` are a second answer-free mock and its key/rubric/diagnosis file (same 25-mark shape: Q1 = 12, Q2 = 8, Section C = 5). Mock 2 rotates the architecture rather than drilling mock 1's errors: Q1 is an articulated **RRR** arm (twist at `alpha_1`, tool along `x_3`) instead of a cylindrical RPP; Q2's two parts have **perpendicular** long axes so the place pose needs a real 90-degree rotation about `z_0` rather than a copy of the pick orientation; Section C moves to **multi-branch IK** (genuine elbow-up/elbow-down from the shoulder+elbow 2R sub-chain) and **cubic trajectory interpolation**, the one in-scope topic mock 1 never tested. The tool-configuration vector is deliberately omitted (covered by mock 1). `quizzes/quiz-01-mock-02-q1-visual-answer.html` is an interactive walkthrough of mock 2's Q1 (answer-bearing; sit the paper first). Two linked SVG views - a top view for what `theta_1` does and a side view of the arm's own vertical plane for `theta_2`/`theta_3` - driven by angle sliders and four presets, with the D-H table, the three link transforms, the arm matrix, the orthonormality/determinant checks and the two IK branches all recomputed live from one 4x4 matrix product. Ends with a 15-assertion self-test panel that runs on load. Self-contained and offline (uses the in-directory `quiz-assets/`). `quizzes/attempts/quiz-01-mock-02-2026-09-18.pdf` is the sat script and `quizzes/quiz-01-mock-02-attempt-2026-09-18-marked.md` its marked record (12/20 core, 12/25 overall). All answers re-derived and numerically verified, including the closed-form arm matrix against the numeric product at 2000 random configurations and both IK branches forward-substituted to the target. `quizzes/attempts/quiz-01-mock-01-2026-09-17.pdf` is the learner's sat script (handwritten, scanned) and `quizzes/quiz-01-mock-01-attempt-2026-09-17-marked.md` is its marked record: 12/20 core, 15/25 overall, with a part-by-part breakdown and a slips-vs-inverted-concepts split. `quizzes/quiz-assets/` is a vendored copy of the KaTeX + `render-math.js` assets (kept in-directory so the page works from `file://` in Safari). Unofficial; mirrors the *format* of recalled real papers and re-derives every answer. Mock uses a cylindrical (RPP) arm and new part coordinates so it collides with neither `notes/` nor the `/self-study` bank.
- `output/self-studying/notes-bank.json` - `/self-study` bank scoped to Quiz 1 (6 sections: quiz logistics/scope, frames+rotations, homogeneous transforms, D-H direct kinematics, inverse kinematics, cubic trajectory planning). Built to `output/self-studying/beginner-notes.html` and `output/self-studying/review-page.html` (HTML mode; shares `output/self-studying/self-study-assets/`). Not a replacement for the canonical `.tex` notes; derived from `lecture-01-manipulator-kinematics.pdf`, `exercises-kinematics-not-for-submission.pdf`, `additional-materials/example-3.1.pdf`, and `notes/notes.tex`.

## Source coverage

| Source | Pages/slides | `notes/beginner-notes.tex` coverage | `notes/notes.tex` coverage | Qualification |
|---|---:|---|---|---|
| `resources/course-outline-part-01.pdf` | p. 1 | Opening scope and course map | Course map and basic language | Supplied outline page covered for sequence and reference context. |
| `resources/lecture-01-manipulator-kinematics.pdf` | pp. 1-22 | Sections 1-2 | Course map and basic language | Robotics overview, architectures, DoF, workspace, and specifications covered; source examples remain selective. |
| same | pp. 23-52 | Sections 3-4 | Frames, rotations, and homogeneous transformations | Coordinate representations, rotations, composition order, and homogeneous transforms developed at beginner/review depth. |
| same | pp. 53-86 | Section 5 | Direct kinematics and D-H arm equation | D-H construction, arm-transform product, tool orientation vectors, and planar 2R example covered; long manipulator calculations are summarized. |
| same | pp. 87-117 | Section 6 | Inverse kinematics | Feasibility, multiplicity, analytic/numerical approaches, and quadrant handling covered; detailed source robot derivations remain selective. |
| same | pp. 118-132 | Section 7 | Trajectory planning | Pick/place framing, path-versus-trajectory distinction, and cubic interpolation covered. |
| same | pp. 133-156 | Section 8 | Differential motion, Jacobians, and singularities | Velocity mapping, pseudoinverse, rank loss, and singularity interpretation covered; implementation details remain selective. |
| `resources/week-01-transcript.txt` | Full transcript | Sections 1-4 | Sections 1-2 | Supports introductory teaching sequence; the handout controls notation and formal claims. |
| `resources/week-02-transcript.txt` | Full transcript | Section 5 | Direct kinematics and D-H arm equation | Supports D-H frame assignment, joint-variable identification, transform multiplication, and tool-axis interpretation; transcript errors are not adopted. |
| `resources/week-03-transcript.txt` | Full transcript | not yet covered | not yet covered | Week 3 lecture: forward-kinematics recap (two worked D-H examples, tool configuration vector) and start of inverse kinematics. Cleaned transcript; transcript errors are not adopted. |
| `resources/week-04-transcript.txt` | Full transcript | not yet covered | not yet covered | Week 4 lecture: analytic inverse kinematics (5-DoF and SCARA), work-cell/task planning with a camera, gravity part feeder, pick-and-place four-point plan, path-vs-trajectory, speed distribution function, cubic/quintic interpolation. Cleaned transcript; transcript errors are not adopted. Also states the unofficial Quiz 1 detail (23 Sep 2026, 7pm, 30 min, this LT, exam-style paper-and-pen, covers up to week 4). |
| `resources/public-archive-2026-08-24/lecture-slides/` | 9 PDFs; all pages | not yet covered | not yet covered | Public exact-code slides/reference files spanning kinematics, control, mobile robots, and intelligent sensors. |
| `resources/public-archive-2026-08-24/past-exam-solutions-2015-2018/` | 3 PDFs; all pages | not yet covered | not yet covered | Publicly posted solution compilations; not verified as official marking schemes. |
| `resources/public-archive-2026-08-24/past-exam-2024-2025/` | Paper and student solution; all pages | not yet covered | not yet covered | Exact-code recent paper plus an unofficial solution that explicitly omits Problem 3(a). |
| `resources/public-archive-2026-08-24/assignments-2020/` | 2 PDFs; all pages | not yet covered | not yet covered | Assignment brief and submitted student work; not a current assignment or official solution. |
| `resources/important-notice-copyright.pdf` | all pages | not yet covered | not yet covered | Administrative copyright notice; not teaching content. |
| `resources/course-syllabus.pdf` | all pages | Opening scope and course map (partial) | Course map and basic language (partial) | Official NTULearn "Course Information" syllabus; supersedes/duplicates some of `course-outline-part-01.pdf`, not yet cross-checked. |
| `resources/cobot-programming-manual.pdf` | all pages | not yet covered | not yet covered | "Manual for robot programming" (Introduction to Cobot) from the NTULearn Information folder; supports the optional cobot self-learn lab, not lecture content. |
| `resources/lecture-02-robot-control.pdf` | pp. 1-54 | not yet covered | not yet covered | Part 1 lecture 2, Robot Control: point-to-point vs path control, feedback block diagram, disturbance rejection, motion-control schemes. Added 2026-09-11; **out of Quiz 1 scope**. |
| `resources/lecture-03-mobile-robot-kinematics.pdf` | pp. 1-40 | not yet covered | not yet covered | Part 1 lecture 3, Mobile Robots: locomotion, wheel types, steered-wheel parameters, WMR kinematics. Added 2026-09-11; **out of Quiz 1 scope**. |
| `resources/additional-materials/week-05-velocity-kinematics.pdf` | pp. 1-3 | not yet covered | not yet covered | Week 5 annotated derivation: forward kinematic equations differentiated to velocity (opens the Jacobian thread). Added 2026-09-11. Pages are handwritten/annotated - native text extraction yields only fragments ("Forward kinematic equations", "=> velocity"); not OCR'd. **Out of Quiz 1 scope** and the evidence that the week-1-4 cutoff is a genuine topic boundary. |
| `resources/additional-materials/control-worked-example.pdf` | pp. 1-5 | not yet covered | not yet covered | Worked control example: error `e = xd - x`, characteristic equation, setting the `Kv`/`Kp` gains from a natural frequency. Added 2026-09-11; **out of Quiz 1 scope**. |
| `resources/exercises-kinematics-not-for-submission.pdf` | pp. 1-2 | PPRR Problem 1(c), both angle conventions; Problem 1(d), learner's convention | PPRR Problem 1(c), both angle conventions; Problem 1(d), learner's convention | Ungraded practice exercises. Problem 1(a), (b), and Problem 2 remain not yet covered by either note; the current additions develop the tool vector, IK, and tool-configuration Jacobian only. RedNote recollection (Kenta) links the two problem topics to Quiz 1; see `quizzes/quiz-01-intel.md`. |
| `resources/exercises-kinematics-solutions.pdf` | pp. 1-3 | Inverse kinematics: PPRR Problem 1(c), pp. 1-2 | Inverse kinematics: PPRR Problem 1(c), pp. 1-2 | Supplied worked solution, added 2026-09-23. The notes retain its downward-positive angle convention and also give the learner's upward-positive variant; its other calculations are not yet covered or independently adopted. D-H frame assignments need not be unique. |
| `resources/ee6221-tutor-exam-review-2026.pdf` | slides 1-59 | not yet covered | not yet covered | User-supplied tutor compilation. Slides 9, 11, 13-15 show past-semester-exam-style kinematics Q1 diagrams; slide 11's seven-joint figure is reused in `quizzes/quiz-01-stretch-01.html`. This deck is not an authenticated Quiz 1 paper. |
| `resources/additional-materials/review-week-01-rotations-translation.pdf` | all pages | Sections 3-4 (partial) | Frames, rotations, and homogeneous transformations (partial) | Instructor review slides for fundamental rotations/translation; not yet cross-checked against note content. |
| `resources/additional-materials/review-week-02-dh-algorithm-summary.pdf` | all pages | Section 5 (partial) | Direct kinematics and D-H arm equation (partial) | Instructor DH-algorithm summary slides; not yet cross-checked. |
| `resources/additional-materials/transformation-optional.pdf` | all pages | Sections 3-4 (partial) | Frames, rotations, and homogeneous transformations (partial) | Optional supplementary transformation-matrix slides. |
| `resources/additional-materials/review-week-03-tool-configuration-vector.pdf` | all pages | Section 5 (partial) | Direct kinematics and D-H arm equation (partial) | Instructor summary of the tool configuration vector. |
| `resources/additional-materials/example-3.1.pdf` | all pages | not yet covered | not yet covered | Worked Example 3.1 referenced by the Kinematics lecture. |
| `resources/additional-materials/review-week-04-inverse-kinematics-trajectory-planning.pdf` | all pages | Sections 6-7 (partial) | Inverse kinematics; Trajectory planning (partial) | Instructor review of IK and trajectory-planning concepts. |
| `resources/additional-materials/section-3.8-additional-slides.pdf` | all pages | Section 6 (partial) | Inverse kinematics (partial) | Additional slides for lecture section 3.8. |
| `resources/additional-materials/section-4.1-additional-slides.pdf` | all pages | Section 7 (partial) | Trajectory planning (partial) | Additional slides for lecture section 4.1. |
| `resources/additional-materials/section-4.2-pick-and-place.pdf` | all pages | Section 7 (partial) | Trajectory planning (partial) | Pick-and-place trajectory example detail. |
| `resources/additional-materials/section-4.3-illustration.pdf` | all pages | Section 7 (partial) | Trajectory planning (partial) | Illustration supporting lecture section 4.3. |
| `resources/additional-materials/section-4.4.1-cubic-polynomials.pdf` | all pages | Section 7 (partial) | Trajectory planning (partial) | Cubic-polynomial trajectory interpolation derivation. |

## Pending and unresolved

- Robot control, mobile-robot kinematics, and intelligent-sensor material remain pending in both notes. Course-specific public slides are now archived, but they have not yet been reviewed or synthesised.
- The public exams and assignment files are validated and indexed in the archive `README.md`; their calculations remain unchecked.
- No authenticated Quiz 1 paper was found. RedNote recollections (2024-25, `quizzes/quiz-01-intel.md`) suggest two free-response questions in ~30 min: D-H frame assignment/table and a pick-from-above arm matrix. The recalled seven-joint detail remains uncertain because the new tutor deck shows a seven-joint semester-exam Q1. The official practice handout supports topic selection but does not verify quiz format or wording.
- Quiz 1 mock built 2026-09-06 in `quizzes/`. **Sat, marked, and folded back on 2026-09-17** (loop stages 4-6 complete for mock 1). Still outstanding: the official NTULearn Quiz 1 notice (date/time/venue/duration/aids/exact cutoff); whether the "first instructor's kinematics-equations" additions are examinable this run; and two illegible cells in the script (the `z` entry of `0T_pick`, and a line read as `3 yeah.` where the Q2 orthonormality check belongs) that the learner should confirm.
- A line at the top of the sat script, numbered `1.`, states path-vs-trajectory correctly but matches no question on mock 1. Unresolved whether it was a pre-exam memory dump or an answer to something else; recorded, not graded.
- 2026-09-17 attempt to close the official-notice item **failed, and the item stays open**. The local `ntulearn` library holds EE6221 metadata only: 23 content nodes, but 0 materials discovered/downloaded/parsed, 0 announcements, 0 assessments, 0 indexed chunks (`library-status --course 3`, cache-only, last observed 2026-09-12T02:36Z, coverage PARTIAL). Every lexical search returns 0 hits - including `Jacobian`, which certainly appears in `lecture-01-manipulator-kinematics.pdf` - confirming the index is empty rather than the term absent. A fresh read was requested but could not run: no Chrome browser is connected to the `claude-in-chrome` extension (`list_connected_browsers` returned empty). **All Quiz 1 logistics therefore remain second-hand.** Re-run the `ntulearn-browser` sync for course_key 3 once Chrome is connected.
- Quiz 1 scope is UNOFFICIAL. Basis: class group-chat consensus (~2026-09-02) and the instructor's Week 3 lecture remarks (from a personal transcript) - quiz ~23 Sep 2026, ~30 min, rooms via NTULearn; "first four weeks only", explicitly excluding the following week's lecture. Mapped to: frames/rotations, homogeneous transforms, D-H direct kinematics + arm matrix + tool configuration vector, inverse kinematics, cubic trajectory planning. Jacobian / differential motion / singularities treated as out of scope. **Corroborated 2026-09-17:** the Week 5 material (`additional-materials/week-05-velocity-kinematics.pdf`) differentiates the forward kinematic equations to get velocity, i.e. week 5 opens the Jacobian/velocity thread, so "first four weeks" is a genuine topic boundary and not merely a slide count. The robot-control and mobile-robot decks added the same day are later units. Still unofficial - this is inference from material dates and content, not a lecturer statement about the quiz. Re-check against the official NTULearn notice when posted and update `output/self-studying/notes-bank.json` section order 10.
- Expand the detailed source robot examples only after choosing which manipulator convention/problem set the learner wants to practise.

## File-organization record

- 2026-09-23: user-supplied WeChat temporary file `6221 tutor(1).pdf -> resources/ee6221-tutor-exam-review-2026.pdf` (copied, not moved; original preserved). Its slide-11 diagram was cropped into `quizzes/quiz-assets/ee6221-2022-2023-s2-q1-seven-joint-figure.png` for the practice page.
- 2026-09-23: `resources/EE6221_Assignment_solution.pdf -> resources/exercises-kinematics-solutions.pdf` (descriptive name for the supplied three-page exercise solution; content preserved).
- 2026-09-18 attempt filing: `~/Downloads/Scanned Document 6.pdf -> quizzes/attempts/quiz-01-mock-02-2026-09-18.pdf` (copied, not moved; the original is left in Downloads for the learner to delete). New sibling file `quizzes/quiz-01-mock-02-attempt-2026-09-18-marked.md`.
- 2026-09-17 attempt filing: new `quizzes/attempts/` directory (canonical home for sat scripts). `~/Downloads/Scanned Document 5.pdf -> quizzes/attempts/quiz-01-mock-01-2026-09-17.pdf` (copied, not moved - the original is left in Downloads for the learner to delete). New sibling file `quizzes/quiz-01-mock-01-attempt-2026-09-17-marked.md`.

- 2026-09-17 housekeeping (quiz-prep stage-2 pass): filed the four resources added 2026-09-11 and one stray course-root artifact. `resources/Robot control(1).pdf -> resources/lecture-02-robot-control.pdf`; `resources/Mobile Robot Kinematics(1).pdf -> resources/lecture-03-mobile-robot-kinematics.pdf`; `resources/Week 5 Kinamatics.pdf -> resources/additional-materials/week-05-velocity-kinematics.pdf` (identified by content: forward kinematic equations differentiated to velocity; the source spelling "Kinamatics" was a typo); `resources/control example.pdf -> resources/additional-materials/control-worked-example.pdf` (identified by content: error/characteristic-equation/gain-setting slides). `notes.pdf -> notes/notes.pdf` - the compiled review note was sitting at the course root while `STATUS.md` claimed it was beside its `.tex`; the course root now holds only `STATUS.md`. No file was overwritten or deleted, and no reference needed repair: a repo-wide grep for all five old names found zero citations in any `.md`, `.tex`, `.json`, or `.html`.

- 2026-09-04 transcript clean-up: both raw Gemini transcripts were archived and replaced by a filler-cleaned version at the same canonical path (existing citations still resolve). `resources/week-01-transcript.txt -> resources/transcripts-raw/week-01-transcript.txt`; `resources/week-02-transcript.txt -> resources/transcripts-raw/week-02-transcript.txt`. The `resources/transcripts-raw/` directory is new (holds the verbatim originals). New `resources/week-0N-transcript.txt` files are the cleaned text: double-spacing collapsed, filler / false starts / immediate repetitions removed, recurring ASR garble for standard terms fixed (e.g. "revue joint" -> "revolute joint", "cartan" -> "Cartesian", "DH digram" -> "DH diagram"). Word retention 94-95% vs raw; no summarization. No note content changed.
- 2026-09-06 transcript clean-up (week 3-4): same procedure as the 2026-09-04 pass. Raw Gemini transcripts for weeks 3 and 4 were added, archived verbatim, and replaced by a filler-cleaned version at the same canonical path. `resources/week-03-transcript.txt -> resources/transcripts-raw/week-03-transcript.txt`; `resources/week-04-transcript.txt -> resources/transcripts-raw/week-04-transcript.txt` (verbatim originals: 18621 / 18103 words). New `resources/week-0{3,4}-transcript.txt` are the cleaned text: double-spacing collapsed, filler / false starts / immediate repetitions removed, one-blank-line paragraphing, recurring ASR garble for standard terms fixed (e.g. "two frame" -> "tool frame", "row angle" -> "roll angle", "fiscal" -> "physical", "whiz/wrist" fixed, "revue/revenue joint" -> "revolute joint", "any/en factor" -> "end effector", "peak/praise point" -> "pick/place point"). Spans that would need reconstructing the claim were left verbatim rather than guessed. Staff name in the week-4 quiz remark anonymized to "the Part 2 lecturer" (matching the week-1 treatment). Word retention 92-94% vs raw; no summarization. No note content changed.
- `Outline for Part I.pdf -> resources/course-outline-part-01.pdf`
- `kinematics(3).pdf -> resources/lecture-01-manipulator-kinematics.pdf`
- `6221-week1.txt -> resources/week-01-transcript.txt`
- `6221-week2.txt -> resources/week-02-transcript.txt`
- `notes.tex -> notes/notes.tex`; `notes.pdf -> notes/notes.pdf`
- `week1-beginner-notes.tex -> notes/week-01-beginner-notes.tex`; `week1-beginner-notes.pdf -> notes/week-01-beginner-notes.pdf`
- 2026-08-24: added `resources/public-archive-2026-08-24/` with 16 valid PDFs, source metadata, and a provenance README. Generic robotics resources, unrelated codes, and commercial solution sites were excluded.
- 2026-09-05 NTULearn sync: downloaded and organized all remaining EE6221 NTULearn content-page resources not previously captured. New top-level files: `Important Notice on Copyright -> resources/important-notice-copyright.pdf`; `Course Information (EE6221_syllabus.pdf) -> resources/course-syllabus.pdf`; `Manual for robot programming (Introduction to Cobot_01July_v2.pdf) -> resources/cobot-programming-manual.pdf`; `Exercises for Kinematics (not for submission) (Assignment for Kinematis.pdf) -> resources/exercises-kinematics-not-for-submission.pdf`. New `resources/additional-materials/` directory holds the "Additional materials" folder's 11 items: `Review for Week 1.pdf -> review-week-01-rotations-translation.pdf`; `Summary of DH_1.pdf -> review-week-02-dh-algorithm-summary.pdf`; `Trenaformation mtrix.pdf -> transformation-optional.pdf`; `Summary of Tool Configuration Vector.pdf -> review-week-03-tool-configuration-vector.pdf`; `example3.1.pdf -> example-3.1.pdf`; `Summary.pdf -> review-week-04-inverse-kinematics-trajectory-planning.pdf` (identified by content: IK/trajectory-planning review slide); `Section 3.8.pdf -> section-3.8-additional-slides.pdf`; `Section 4.1.pdf -> section-4.1-additional-slides.pdf`; `pick and place.pdf -> section-4.2-pick-and-place.pdf`; `Section 4.3.pdf -> section-4.3-illustration.pdf`; `interpolation.pdf -> section-4.4.1-cubic-polynomials.pdf` (identified by content: cubic-polynomial trajectory derivation). "Optional Cobot Self-learn Session" was left undownloaded — it is an announcement/sign-up text item, not a file resource. `Course Outline for Part I` and `Kinematics` were already organized (unchanged). All new PDFs are unreviewed by the notes; see the source-coverage table above.

- 2026-09-06 Quiz 1 mock: new `quizzes/` directory (canonical home for quiz practice, per `CLAUDE.md`). Added `quiz-01-intel.md`, `quiz-01-mock-01.html`, `quiz-01-mock-01.md`, and `quiz-assets/` (vendored copy of `output/self-studying/self-study-assets/` — KaTeX + `render-math.js`, duplicated in-directory so the page loads from `file://` in Safari without `..` subresource paths). No source material moved or renamed. The separate research handover at `~/Projects/output/quiz-test-prep/` now points here as the canonical location.

## Update record

- 2026-09-23: Added an answer-free seven-joint D–H stretch page from the tutor deck's semester-exam-style Q1, with a readable cropped diagram. Audited `quizzes/quiz-01-intel.md` so the deck is not mistaken for Quiz 1 evidence; exact quiz format remains unverified. The canonical notes were not changed, so no LaTeX compilation was needed.
- 2026-09-23: Revised `quizzes/quiz-01-mock-04.html` and its key after checking Mock 3 overlap against the saved Quiz 1 intel. Q1 now uses an articulated RRR arm with a nonzero D–H twist, giving a genuine architecture change while still checking rotated link translations. No source files moved or renamed; canonical notes already cover the underlying rules.
- 2026-09-23: Added `quizzes/quiz-01-mock-03.html` and a separate answer key after the learner's grasp-axis question. New RRP geometry and reversed pick/place long-axis orientation avoid reusing Mock 1 or 2 answers. No source files were moved or renamed; canonical notes already explain that sliding is perpendicular to grasped long faces.
- 2026-09-23: Derived the $6\times4$ tool-configuration Jacobian for PPRR Problem 1(d) using the learner's upward-positive frame and explicit joint order in both notes. No files were organized or renamed. Both PDFs compiled with XeLaTeX and the revised pages were visually checked.
- 2026-09-23: Expanded both notes' IK-method explanation with a planar 2R example: square-and-add elimination, elbow branches, why direct tangent division loses quadrant information, and forward substitution. No files were organized or renamed. Both PDFs compiled with XeLaTeX and the revised pages were visually checked.
- 2026-09-23: Clarified in both PPRR inverse-kinematics notes that the tool vector has six coordinate entries but only four joint variables, and that planar motion forces entries 2 and 5 to zero for reachable targets. No files were organized or renamed. Both PDFs compiled with XeLaTeX and the revised pages were visually checked.
- 2026-09-23: Checked the learner's PPRR D--H assignment ($\alpha_2=\alpha_3=+\pi/2$), corrected its third-row rotation, and added the upward-positive tool vector and inverse kinematics to both notes. The learner's photos remain conversation sources, not repository files; no course files were organized or renamed. Both PDFs compiled with XeLaTeX; the revised pages were visually checked.
- 2026-09-23: Added a worked derivation of the PPRR tool-configuration vector and inverse kinematics from exercise Problem 1(c) to both canonical notes, using the supplied solution's sign convention. The beginner note explains the wrist-to-tip offset, scaled approach vector, quadrant-aware angle recovery, feasibility, and substitution check; the review note retains the equations and conditions. Both PDFs compiled with XeLaTeX and the added pages were visually checked. Other exercise parts remain pending.
- 2026-09-18 Q1 visual walkthrough: added `quizzes/quiz-01-mock-02-q1-visual-answer.html`, an interactive answer for
mock 2 Question 1, built on the insight that the arm never needs a 3D drawing - `theta_1` only chooses which vertical
plane the arm occupies, and `theta_2`/`theta_3` act as a planar 2R arm inside it, so a top view plus a side view of
that plane carry every answer in parts (a)-(d). Also demonstrates Section C1: the "exam values" and "same tool tip,
elbow up" presets are the two IK branches and visibly land on the same point.
  Verification: the math was checked in node before the page was written, the page's own 15 assertions were then run
  headlessly against a stub DOM (all pass - stated answers, origin landmarks, `R^T R = I` and `det R = +1` over 400
  random configurations, closed form vs. matrix product, `theta_1` cannot change height, IK round trip both branches,
  unreachable target rejected), the inline script was syntax-checked, and the generated SVG was validated as
  well-formed XML and swept for NaN. Structural checks: all asset refs local and resolving, no remote requests, every
  `getElementById` target present, every CSS variable declared, all five self-check questions resolvable with feedback.
  Three real defects were found and fixed during QA: (i) `drawIK()` was defined but never called, so the Section 5 IK
  table would have rendered empty; (ii) a CSS `fill` on `.lbls` overrode the per-frame `fill` presentation attribute,
  so the frame colours were being ignored - moved into `style=`; (iii) the side view clipped badly, because folding the
  arm back takes the radial coordinate to -6 while the grid only spanned `r` in [-2,8] - rescaled to cover the full
  reach envelope and re-checked over the entire slider range.
  **Correction prompted by the learner:** the page had labelled the arm matrix's third column "the approach axis
  `r_3`". That is wrong for a D-H link frame. Row 3 has `alpha_3 = 0`, so `z_3` is parallel to the elbow axis and
  square to the arm's plane; the reach direction is `x_3`, which is exactly why the tool length belongs in the `a`
  column. The normal/sliding/approach naming describes a *tool* frame, reached by appending a further fixed rotation
  that gets no D-H row. The page now highlights column 1 as `x_3` and carries a dedicated explanation, and the
  distinction was folded into `notes/beginner-notes.tex` sec. 5 ("Every D-H z is a joint axis - the reach direction is
  x") and as a caveat opening `notes/notes.tex`'s "Tool orientation vectors", whose previous wording invited exactly
  this reading. Both notes recompiled (7 pages each).
  **Second correction, same thread.** The first fix overstated the rule as "every D-H z is a joint axis". The learner
  pushed back - there is no joint at frame 3 - and was right. The precise rule is `z_{k-1}` is the axis of joint `k`,
  so an n-joint arm's joints are described by `z_0 ... z_{n-1}` and **`z_n` is not a joint axis**: nothing downstream
  constrains it, which is exactly why `alpha_n` and `d_n` are a free choice. `alpha_3 = 0` (giving `z_3 || z_2`) is a
  convention picked because it keeps the table simplest, not a physical fact; `alpha_3 = +-90` is equally correct with a
  matching arm matrix. Added the accompanying reason a gripper frame must be an appended fixed rotation rather than a
  D-H row: `Rot(x, alpha_n)` holds `x_n` fixed and only spins `y_n, z_n` about it, so `alpha_n` can never point `z_n`
  along `x_n` however it is chosen. Corrected in all three places (the walkthrough's part-(a) bullet, its part-(d)
  detail box and its figure caption; `notes/beginner-notes.tex` sec. 5, now split into "Which z axes are joint axes -
  and why the last one is not" plus a separate approach-vector pitfall; and `notes/notes.tex`'s "Tool orientation
  vectors" caveat). Re-audited: `grep` confirms no blanket "every z is a joint axis" claim survives in any note or
  quiz file. Both notes recompiled again (7 pages each); the walkthrough's 15 assertions still pass.

- 2026-09-18 Quiz 1 mock 2 stages 4-6 (sat, marked, folded back). Score 12/20 core, 12/25 overall; breakdown in
`quizzes/quiz-01-mock-02-attempt-2026-09-18-marked.md`. Core matched mock 1's 12/20 but the composition shifted:
**the mock 1 fold-back worked** - the D-H table went 1/3 -> 3/3 (three joints, three rows, twist correctly in row 1,
tool folded into `a_3 + L_t` rather than given a joint row, no table/transform sign contradiction) and the frame
diagram 3/4 -> 4/4. Two new items were folded into both notes:
  1. **Where each frame's origin lands.** `d_k` steps the origin along `z_{k-1}`, then `a_k` steps it along `x_k`, so
     `a_k != 0` displaces the origin by the link length - which is why `a_k` *is* the link length when `x_k` runs along
     the link. For the articulated RRR arm: frame 1 = shoulder, frame 2 = elbow, frame 3 = wrist. Paired with the
     pitfall that **`a_k = 0` does not mean two frames coincide** - it means the origin stays on the `z_{k-1}` axis
     because the joint axes intersect. Added to `notes/beginner-notes.tex` sec. 5 ("Where each frame's origin actually
     lands" + a Common pitfall) and `notes/notes.tex` ("Where the origins land").
  2. **The pick and the place are two different orientations.** `r_2` depends on the part's orientation *at that pose*:
     its current orientation at the pick, its *target* orientation at the place. Long axes differing by 90 degrees give
     `R_place = Rz(+-90) R_pick`. Critically, `R^T R = I` and `det R = +1` **cannot** catch a correct matrix attached to
     the wrong pose, so the recommended habit is to write the long-axis direction for each pose down before writing
     either matrix. Added to `notes/beginner-notes.tex` sec. 7 and `notes/notes.tex`'s grasp-pose recipe, which also
     gained "three terms, computed from the given dimensions, never carried over from a similar problem".
  The place-height slip (stopped at the supporting surface, dropping the moving part's half-height) was **not** treated
  as a new gap - the three-term formula was already in both notes from the mock 1 fold-back and the same checkpoint was
  passed on mock 1, so it is execution, not understanding.
  **Correction to the mock:** `quizzes/quiz-01-mock-02.md` Q1(a) had described frame 2's origin as the shoulder and
  claimed frames 1 and 2 coincide when `a_1 = 0`. Both were wrong - frame 2 is at the elbow. Found because the sat
  script drew it correctly and disagreed with the key; verified numerically (`o_1 = (0,0,4)`, `o_2 = (0,2.598,5.5)`,
  `|o_1 - o_2| = a_2 = 3`). The key and its checkpoint 4 are corrected and carry a dated correction notice; marks and
  the arm matrix are unaffected, since the closed form was verified from the link-matrix product and never depended on
  that prose. This is the origin of note item 1 above.
  **Confirmed pacing problem (twice now, not a one-off):** mock 1 ended with Q1(d) blank; mock 2 ended with Q1(c),
  Q1(d) and all of Section C blank - 10 of the 13 marks lost were *blank, not wrong*. The script shows three separate
  drawings of the link-coordinate diagram, two struck through. Recorded as exam technique in the marked file (draw the
  frames once; write the three link matrices straight off a correct table, since that is the cheapest mark on the
  paper; budget roughly Q1 18 min / Q2 12 min), deliberately **not** written into the `.tex` notes, which are subject
  notes rather than exam technique.
  Compilation: both notes rebuilt with `xelatex` (`notes.pdf` 7 pages, `beginner-notes.pdf` 6 -> 7 pages) and the
  changed pages visually inspected.
- 2026-09-18 Quiz 1 mock 2 (quiz-prep stage 3, second pass). Built `quizzes/quiz-01-mock-02.html` (answer-free;
30-minute timer over Q1+Q2 with Section C untimed, localStorage under its own key `ee6221-quiz1-mock2` so mock 1's
saved state is untouched, per-question "answered on paper" toggles, plain-text export, two new inline SVG figures,
light/dark tokens, offline via the existing in-directory `quiz-assets/`) and `quizzes/quiz-01-mock-02.md` (key,
per-checkpoint rubric totalling 25, and a "common wrong paths" table per question). Coverage was chosen for breadth,
not remediation - the learner explicitly asked that mock 2 not be built solely around the mock 1 performance - and the
`quiz-01-mock-02.md` header documents the Mock 1 -> Mock 2 rotation choice by choice. Collision-checked against
`notes/*.tex`, `quizzes/quiz-01-mock-01.*` and `output/self-studying/notes-bank.json`: the articulated RRR arm appears
in the notes only as a taxonomy label (never a worked D-H example) and none of mock 2's numbers occur anywhere.
Validation: all answers re-derived from scratch and checked numerically (`Q1` closed form vs. the numeric product of
the three link matrices at 2000 random configurations; both `C1` IK branches forward-substituted to the target exactly;
`C2` cubic checked at `t = 0, T/2, T` for value and velocity); page structurally validated (balanced containers, every
`data-q` referenced by the exporter present in the DOM, every `getElementById` target present, all four asset
references local and resolving, 70 balanced math spans, no remote requests). One real defect was found and fixed
during figure QA: part E's rectangle had been placed *at* its centroid rather than centred on it, clipping below the
viewBox; both figures now stay inside their viewBoxes and the px<->cm mapping reproduces the stated centroids and side
lengths exactly. A deliberate trap is documented for the grader: mock 2's correct `0T_pick` rotation block is
numerically identical to the answer the learner got *wrong* on mock 1, because part E's long axis is along `y_0`
instead of `x_0` - `quiz-01-mock-02.md` carries an explicit grader's note not to mark it wrong for consistency, nor to
credit it without the reasoning. Neither note `.tex` was changed; no source file moved or renamed. Stages 4-6 for
mock 2 pending the learner. Clarified the same day, before the paper was sat, after the learner asked whether the "wrist" label implied a fourth joint: the figure label now reads "wrist point (no joint)", the caption says all three joints are shown, and a note in the question body states that the tool is rigid and that tool orientation is therefore not independently controllable on a 3-DOF arm (which is why Section C asks for position-only IK). Wording only - no question, answer, or mark allocation changed.

- 2026-09-17 quiz-prep stages 4-6 (mock 1 sat, marked, folded back). Score 12/20 core, 15/25 overall; full breakdown in
`quizzes/quiz-01-mock-01-attempt-2026-09-17-marked.md`. Four errors were judged conceptual rather than execution slips
and were written into both notes at their respective depths:
  1. **A D-H table has one row per joint; a rigid tool is not a joint.** The script gave `L_t` a joint row, which
     displaced the revolute `theta_1` and silently cost the chain a degree of freedom. Added to
     `notes/beginner-notes.tex` sec. 5 as "One row per joint --- and a rigid tool is not a joint" plus a
     "thirty-second pre-flight check" (star the joint variables, count them against the figure), and to
     `notes/notes.tex` sec. "Standard Denavit--Hartenberg parameters" as a compact "Table invariants" list. The
     existing text said only "Only one of theta_k and d_k is a joint variable", which did not rule out a tool row.
  2. **Grasp direction.** `r_2` (sliding) is perpendicular to the faces being grasped, so grasping the long sides
     closes the jaws along the *short* axis. Neither note covered how to build a grasp pose; added as a four-step
     recipe (approach, sliding, normal by cross product, translation incl. the stacking half-heights) in
     `beginner-notes.tex` sec. 7 and as a compact "Grasp-pose recipe" in `notes.tex` sec. "Trajectory planning".
  3. **Tool-configuration vector exponent.** `q_n` is the tool *roll* angle, the rotation about the approach vector
     (`resources/lecture-01-manipulator-kinematics.pdf`, pp. 92-93), not the base joint angle; an arm with no roll DOF
     has `q_n = 0` and `||w_{4:6}|| = 1`. The beginner note had no tool-configuration-vector section at all - one was
     added with the derivation and the pitfall; `notes.tex` gained the decode identity and the explicit warning.
  4. **An IK answer is unfinished without feasibility and a branch count.** Added `d_3 >= 0`, column stroke, and the
     rule that elbow-up/elbow-down pairs come from a 2R sub-chain (so a cylindrical arm's solution is unique) to both
     notes.
  The mock itself needed no correction: every item the script lost marks on was correctly specified, and Section C was
  marked against the learner's own `alpha_2 = +pi/2` frame choice, which `quiz-01-mock-01.md` already permits as
  equally correct. The `q_n` wording in the marked file was corrected mid-review after checking the lecture source -
  "last joint's variable" and "tool roll angle" are the same thing for a standard wrist but not for this arm, and the
  lecture defines the latter.
  Compilation: both notes rebuilt with `xelatex` (`notes.pdf` 6 -> 7 pages, `beginner-notes.pdf` 5 -> 6 pages) and the
  changed pages visually inspected. This required replacing `\usepackage{xurl}` with `url` +
  `\g@addto@macro\UrlBreaks\UrlOrds` in `notes/notes.tex` and `notes/beginner-notes.tex`: `xurl.sty` is absent from
  this machine's TinyTeX, a **pre-existing** blocker unrelated to this change that had left both notes uncompilable.
  Long `\source{}` paths still break across lines correctly. `notes/week-01-beginner-notes.tex` still uses `xurl` and
  remains uncompilable here; left alone as out of scope.

- 2026-09-17 quiz-prep loop (stages 1-3 re-check; stage 4 handed to the learner): re-read the manifest, filed five files (see the file-organization record), and re-checked the Quiz 1 scope boundary against the four resources that landed after the 2026-09-05 sync. Week 5 opens velocity/Jacobian, which corroborates the week-1-4 cutoff and leaves `quizzes/quiz-01-mock-01.{html,md}` correctly scoped - no mock content changed. The official NTULearn notice could not be retrieved (empty local index; no connected Chrome) and stays listed under Pending. Neither note `.tex` was edited, so no recompile was needed; stage 6 will follow the graded attempt.

- 2026-09-07 beginner HTML improvement: rebuilt output/self-studying/beginner-notes.html as six progressive modules with topic navigation, rotating-frame and translated-point diagrams, a shared 1 m + 1 m planar arm, both position-only IK branches and workspace limits, and position/velocity/acceleration plots with duration/progress controls. Added numerical examples, expandable derivations and reference practice, a pick-from-above matrix, tool-configuration-vector explanation, and immediate feedback at the end of every module. notes-bank.json stores the added visual_lesson_html alongside existing content/examples/exercises; rebuild with python3 output/self-studying/build-beginner.py. Uses existing offline KaTeX plus self-study-assets/visual-lessons.css and visual-lessons.js; no new runtime dependency. Rechecked selected handout pages in pp.25–70, 97–98, 130–132; supplementary planar geometry and numeric examples are labelled. Qualified unverified quiz predictions, same-origin rotation use, common-factor IK branches, and frame-choice equivalence. Canonical LaTeX/PDFs and the existing review page were not rebuilt. No source files moved or renamed.
- Validation for the 2026-09-07 HTML update: node output/self-studying/check-visual-lessons.cjs passes forward/inverse numerical substitution, unreachable/folded/full-extension edge cases, cubic endpoint and midpoint checks, all 440 math expressions through KaTeX, unique IDs, and local links. Safari file:// checks confirmed diagrams, slider updates, expandable matrix derivations, wrong/correct answer feedback, and trajectory duration updates; representative diagrams, equations, and graphs visually inspected. Dedicated phone-device and print QA not performed.


- 2026-09-06 Quiz 1 mock (quiz-prep loop stages 1-3): compiled past-paper intelligence from a logged-in RedNote search (8 sources, format evidence converged: 2 free-response questions, ~30 min, D-H modelling + pick-and-place arm matrix), the KuRRe8 GitHub pre-quiz note (confirms Schilling notation), and the official `exercises-kinematics-not-for-submission.pdf` (its two problems match the two recalled quiz topics). Built an answer-free exam page (`quiz-01-mock-01.html`: 30-min timer, localStorage autosave, per-question "answered on paper" toggles, plain-text export, inline SVG figures) and its key/rubric/diagnosis file (`quiz-01-mock-01.md`, 25 marks: Q1 cylindrical RPP arm D-H = 12, Q2 pick/place arm matrix = 8, Section C predicted IK + tool config vector = 5). All answers re-derived from scratch and numerically self-checked; arm and coordinates chosen to collide with neither `notes/` nor the `/self-study` bank. Scope/date remain UNOFFICIAL (see Pending). Stages 4-6 (sit cold, grade, fold into notes) pending the learner.
- 2026-09-06 `/self-study` Quiz 1: created `output/self-studying/` with `notes-bank.json` (6 sections), `config.json` (html), and built `beginner-notes.html` + `review-page.html` + `self-study-assets/`. Schema validation passed; both HTML pages rendered and visually checked in a browser (KaTeX math, matrices, provenance labels all correct; no LaTeX leakage). Scope established from an unofficial group-chat + lecture-remark basis (see Pending and unresolved). No `.tex` note or resource file was changed. `output/` is a new top-level directory for generated study material.
- 2026-08-24: brought the course into the updated canonical layout, repaired note citations, preserved the Week 1-only supplement under an honest scoped filename, and created the canonical full manipulator-kinematics beginner note. Archived later-course material remains explicitly separate from reviewed note coverage.
- 2026-08-24: compiled all three note outputs twice (`notes/beginner-notes.pdf`: 5 pages; `notes/notes.pdf`: 6 pages; `notes/week-01-beginner-notes.pdf`: 3 pages). Rendered and visually checked every page; no clipping, overlap, broken equations, or unreadable text was found.
