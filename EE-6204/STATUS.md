# EE-6204 note status

## Note files

- `notes/beginner-notes.tex` - detailed, self-contained teaching note for the supplied LP/NLP material; compiled PDF is stored beside it.
- `notes/notes.tex` - concise LP/NLP review note; compiled PDF is stored beside it.
- `notes/week-01-beginner-notes.tex` - preserved Week 1-only teaching supplement; it is not the canonical full-scope beginner note.

## Source coverage

| Source | Pages/slides | `notes/beginner-notes.tex` coverage | `notes/notes.tex` coverage | Qualification |
|---|---:|---|---|---|
| `resources/lecture-01-04-linear-and-nonlinear-programming.pdf` | PDF pp. 1-90 | Sections 1-7 | Sections 1-4 | LP modelling, geometry, standard form, simplex, duality, sensitivity, transportation, and assignment are developed at beginner/review depth; source tableaux are selectively summarized. |
| same | PDF pp. 91-141 | Sections 8-9 | Sections 5-6 | Scalar/multivariable optimisation, Newton methods, equality constraints, and KKT conditions are covered; source calculations are represented by original explanations rather than copied. |
| same | PDF p. 142 | none needed | none needed | Blank terminal slide. |
| `resources/introduction-to-linear-programming.pdf` | PDF pp. 1-43 | Sections 1-4 | Sections 1-2 | Optimisation vocabulary, formulation, LP geometry, special outcomes, and standard-form preparation are covered; source code snippets and bibliography are not reproduced. |
| same | PDF p. 44 | none needed | none needed | Blank terminal slide. |
| `resources/week-01-transcript.txt` | Full transcript | Sections 1-4 | Sections 1-2 | Supports the beginner teaching order and modelling emphasis; PDFs control formal notation and claims. |
| `resources/week-02-transcript.txt` | Full transcript | Section 5 | Section 2.3 | Supports the simplex construction, pivot interpretation, and ratio-test emphasis; automatic transcript errors are not adopted as terminology. |
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

## File-organization record

- `EE6204 LP NLP(1).pdf -> resources/lecture-01-04-linear-and-nonlinear-programming.pdf`
- `Introduction to Linear Programming.pdf -> resources/introduction-to-linear-programming.pdf`
- `week1-transcript.txt -> resources/week-01-transcript.txt`
- `week2-trans.txt -> resources/week-02-transcript.txt`
- `notes.tex -> notes/notes.tex`; `notes.pdf -> notes/notes.pdf`
- `week1-beginner-notes.tex -> notes/week-01-beginner-notes.tex`; `week1-beginner-notes.pdf -> notes/week-01-beginner-notes.pdf`
- 2026-08-24: added `resources/public-archive-2026-08-24/` with 106 valid PDFs, one valid XLSX workbook, source metadata, and a provenance README. Commercial textbook scans and unrelated material were excluded.

## Update record

- 2026-08-24: brought the course into the updated canonical layout, repaired note citations, preserved the Week 1-only supplement under an honest scoped filename, and created the canonical full LP/NLP beginner note. The archive remains explicitly separate from reviewed note coverage.
- 2026-08-24: compiled all three note outputs twice (`notes/beginner-notes.pdf`: 5 pages; `notes/notes.pdf`: 8 pages; `notes/week-01-beginner-notes.pdf`: 3 pages). Rendered and visually checked every page; no clipping, overlap, broken equations, or unreadable text was found.
