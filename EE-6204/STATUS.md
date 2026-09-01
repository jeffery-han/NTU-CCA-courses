# EE-6204 note status

## Note files

- `notes/beginner-notes.tex` - detailed, self-contained teaching note for the supplied LP/NLP material; compiled PDF is stored beside it.
- `notes/notes.tex` - concise LP/NLP review note; compiled PDF is stored beside it.
- `notes/week-01-beginner-notes.tex` - preserved Week 1-only teaching supplement; it is not the canonical full-scope beginner note.
- `notes/quiz1-prep-learning.html` - self-contained interactive Quiz 1 study companion (10 modules, 9 multiple-choice checks, a guided simplex pivot walker, a 14-cue recall trainer, a quiz-day plan). MathJax is vendored at `notes/vendor/mathjax/tex-mml-chtml.js` so it works offline; lab answers and recall progress persist per-browser in `localStorage` under `ee6204-quiz1-prep-learning-v1` (theme key `ee6204-theme`). Supplementary to the two LaTeX notes, which remain canonical. Covers the same LP/simplex/duality/sensitivity scope as `notes/beginner-notes.tex` §1-7 plus a collapsed legacy section pointing at transportation/NLP; the walker LP (`max 50x1+40x2` s.t. `x1+x2<=9`, `2x1+x2<=14`) and the graphical lab differ from both notes' worked examples and from the mock.

## Quiz 1 preparation (`quizzes/`)

- `quizzes/quiz-1-intel.md` - past-paper intelligence gathered 2026-09-02 from 小红书 (RedNote) and a web search. Records two eras: the **current run** (Prof. Su Rong, Feb 2026 sitting + this semester) = Week 4, ~16%, **30-min handwritten** quiz uploaded to NTULearn, Q1 LP formulation (~30%) + Q2 simplex (~70%) on one LP; and the **previous lecturer** (through Sep 2025) = Week 5, MCQ + fill-in-blank, Q1 balanced transportation (VAM), Q2 constrained NLP (Lagrange + Hessian). All unofficial; every recalled answer is re-derived, not adopted. No worked answer key for a Quiz 1 question was found in any post.
- `quizzes/quiz-1-prediction.md` - answer key + per-checkpoint marking rubric (Q1 = 5, Q2 = 11, core total 16) + "common wrong paths" for every part, built to the current-run shape. LP: `max 40x1+30x2` s.t. `x1+x2<=12`, `2x1+x2<=16` -> optimum `(4,8)`, `z=400`, 2 pivots; both the objective (`40,30`) and RHS (`12,16`) differ from `notes/beginner-notes.tex` §2.1's `30x+50y` / `16,11,15` example. Section S = predicted unseen **sensitivity/duality** item on the same LP (shadow prices `20,10`; `b1 in [8,16]`; `c1 in [30,60]`), lecturer-flagged in the Week 2 transcript. Section L = legacy transportation (supplies `20,30,25`, demands `15,20,20,20`, cost = 615, non-degenerate) + closed-box NLP (`V=32`, cube, bordered-Hessian check). Every number derived and checked here.
- `quizzes/quiz-1-prediction.html` - answer-free interactive rendering of the mock: 30-minute timer, "answered on paper" affordances, final-figure fields, `localStorage` autosave under `ee6204-quiz1-prediction-v1`, and a **Build answer sheet** export for pasting into Claude Code for grading. Reuses the vendored MathJax via `../notes/vendor/mathjax/tex-mml-chtml.js`. Contains no answers by design; the key sits in `quiz-1-prediction.md`.

## Source coverage

| Source | Pages/slides | `notes/beginner-notes.tex` coverage | `notes/notes.tex` coverage | Qualification |
|---|---:|---|---|---|
| `resources/lecture-01-04-linear-and-nonlinear-programming.pdf` | PDF pp. 1-90 | Sections 1-7 | Sections 1-4 | LP modelling, geometry, standard form, simplex, duality, sensitivity, transportation, and assignment are developed at beginner/review depth; source tableaux are selectively summarized. |
| same | PDF pp. 91-141 | Sections 8-9 | Sections 5-6 | Scalar/multivariable optimisation, Newton methods, equality constraints, and KKT conditions are covered; source calculations are represented by original explanations rather than copied. |
| same | PDF p. 142 | none needed | none needed | Blank terminal slide. |
| `resources/introduction-to-linear-programming.pdf` | PDF pp. 1-43 | Sections 1-4 | Sections 1-2 | Optimisation vocabulary, formulation, LP geometry, special outcomes, and standard-form preparation are covered; source code snippets and bibliography are not reproduced. |
| same | PDF p. 44 | none needed | none needed | Blank terminal slide. |
| `resources/week-01-transcript.txt` | Full transcript | Sections 1-4 | Sections 1-2 | Supports the beginner teaching order and modelling emphasis; PDFs control formal notation and claims. |
| `resources/week-02-transcript.txt` | Full transcript | Section 5 | Section 2.3 | Supports the simplex construction, pivot interpretation, and ratio-test emphasis; automatic transcript errors are not adopted as terminology. Also the source for the Quiz 1 format and the `z - cᵀx = 0` convention used in `notes/quiz1-prep-learning.html` and `quizzes/quiz-1-prediction.*`, and for the "sensitivity technique is quiz-relevant" signpost. |
| `resources/week-01-transcript.txt` + `resources/week-02-transcript.txt` | quiz-logistics passages | Quiz 1 companion + mock header | (unofficial) | Prof. Su Rong states: quiz at the end of the Week 4 lecture; ~30 min; problem posted as a PDF on NTULearn; answers handwritten, photographed, uploaded (10-15 min extra); bring own laptop/iPad. Phrased "most likely" / "details will come later" - flagged for NTULearn verification. |
| 小红书 (xiaohongshu) `EE6204` / `6204 quiz1` search | 6 relevant notes, logged-in session, 2026-09-02 | `quizzes/quiz-1-intel.md` | (unofficial) | Student recollections of the Feb 2026 and Sep 2025 sittings and the two-era format split. Not official papers or marking schemes; recalled answers are re-derived. |
| `resources/public-archive-2026-08-24/past-exam-solutions-2012-2019/` | 6 PDFs; all pages | not yet covered | not yet covered | Publicly posted solution compilations; provenance does not establish official marking-scheme status. |
| `resources/public-archive-2026-08-24/past-exam-walkthroughs-2015-2023/` | 29 PDFs; all pages | not yet covered | not yet covered | Personal question-level walkthroughs. Re-derive calculations before synthesis. |
| `resources/public-archive-2026-08-24/worked-slide-examples/` | 59 PDFs; all pages | not yet covered | not yet covered | LP/NLP, stochastic-process/queueing, and decision-analysis worked examples from a public student repository. |
| `resources/public-archive-2026-08-24/topic-explainers/` | 11 PDFs and workbook Sheet1-Sheet3 | not yet covered | not yet covered | Supplementary explainers and frequency analysis; not evidence of current assessment scope. |
| `resources/public-archive-2026-08-24/course-outline/ee6204-obtl-abridged.pdf` | All pages | not yet covered | not yet covered | Public abridged outcome/course-outline file; verify current official policy separately. |

## Pending and unresolved

- Random processes, Markov chains, queueing models, and decision analysis remain pending in both canonical notes. The public archive contains worked examples, but no current official slide deck for these parts is locally available.
- The public archive is validated and indexed in its `README.md`, but its student solutions remain unsynthesised.
- No exact-code public quiz file or 2024-2026 EE-6204 paper was found in the 2026-08-24 search. Do not relabel examinations, assignments, or examples as quizzes.
- Assessment-format comments in public student repositories are historical and unofficial; verify current arrangements in NTULearn.
- **Quiz 1 scope boundary (from Weeks 1-2 transcripts only):** Prof. Su Rong's Part 1 = LP formulation, graphical method, standard form, simplex; duality and sensitivity developed heavily in Week 2 and flagged as quiz-relevant; only "a little bit" of NLP "in the fourth lecture". Weeks 3-4 transcripts are **not available locally**, so transportation/assignment depth and the exact NLP cut-off for the current run are unconfirmed. The Feb 2026 recollection is "LP + simplex only, very simple, 16 marks". Verify against NTULearn / the Week 4 lecture.
- **Quiz 1 logistics are unofficial student recollection** (Week 4, ~16%, 30-min handwritten upload). Confirm date, time, weighting, and whether notes/calculator are allowed on NTULearn before relying on them.
- `notes/beginner-notes.tex` line ~152 has `,quad g_j(x)\geq0` where `,\quad` is intended - a literal "quad" will render in the KKT primal-feasibility line. Not touched by this update (no `.tex` recompile was in scope); fix on the next `/update` that compiles the notes.

## File-organization record

- `EE6204 LP NLP(1).pdf -> resources/lecture-01-04-linear-and-nonlinear-programming.pdf`
- `Introduction to Linear Programming.pdf -> resources/introduction-to-linear-programming.pdf`
- `week1-transcript.txt -> resources/week-01-transcript.txt`
- `week2-trans.txt -> resources/week-02-transcript.txt`
- `notes.tex -> notes/notes.tex`; `notes.pdf -> notes/notes.pdf`
- `week1-beginner-notes.tex -> notes/week-01-beginner-notes.tex`; `week1-beginner-notes.pdf -> notes/week-01-beginner-notes.pdf`
- 2026-08-24: added `resources/public-archive-2026-08-24/` with 106 valid PDFs, one valid XLSX workbook, source metadata, and a provenance README. Commercial textbook scans and unrelated material were excluded.
- 2026-09-02: created the `quizzes/` directory (first use for EE-6204) with `quiz-1-intel.md`, `quiz-1-prediction.md`, and `quiz-1-prediction.html`. Added `notes/quiz1-prep-learning.html` and vendored `notes/vendor/mathjax/tex-mml-chtml.js` (1.17 MB, copied from `EE-6203/notes/vendor/mathjax/` - not duplicated per-file). No existing file was moved, renamed, or deleted; no `.tex` or PDF changed. The two HTML pages link relatively to each other, to `notes/beginner-notes.pdf` / `notes/notes.pdf`, and to `quizzes/quiz-1-intel.md` / `quiz-1-prediction.md`; all targets confirmed present. 小红书 material was gathered in a logged-in Chrome session (screenshots read, not saved); the user performed the login.

## Update record

- 2026-08-24: brought the course into the updated canonical layout, repaired note citations, preserved the Week 1-only supplement under an honest scoped filename, and created the canonical full LP/NLP beginner note. The archive remains explicitly separate from reviewed note coverage.
- 2026-08-24: compiled all three note outputs twice (`notes/beginner-notes.pdf`: 5 pages; `notes/notes.pdf`: 8 pages; `notes/week-01-beginner-notes.pdf`: 3 pages). Rendered and visually checked every page; no clipping, overlap, broken equations, or unreadable text was found.
- 2026-09-02 Quiz 1 preparation: gathered unofficial 小红书 past-paper intel (`quizzes/quiz-1-intel.md`), built the source-grounded answer-free mock (`quizzes/quiz-1-prediction.html` + `.md` with rubric), and the from-scratch interactive study companion (`notes/quiz1-prep-learning.html`). Both pages verified in Chrome over a local HTTP server: MathJax typesets from the vendored copy (no offline banner), the pivot walker advances through all three tableaux with correct arithmetic and rejects wrong entering/leaving choices with the ratio-test reason, `localStorage` persists across reload, the mock's Build-answer-sheet export produces a self-contained block, and the console is clean. Every LP, tableau, dual, and sensitivity range in the mock and companion was derived and cross-checked here. No `.tex` or PDF was changed; the KKT `,quad` typo above is recorded for the next compile.
