# NTU CCA Course Notes

Study workspace for the NTU MSc Computer Control & Automation programme.  Each `EE-XXXX/` directory is one course.  The learner studies from this local, iCloud-synced folder; GitHub `jeffery-han/NTU-CCA-courses` is only a backup.

This file holds the rules that apply to every task.  Task-specific rules are in `docs/`; read the one the table names before starting that kind of work.

| Task | Read first |
|---|---|
| Anything in a course | that course's `STATUS.md` (current state; under 100 lines) |
| Write or edit `notes/*.tex` | `docs/notes-style.md` |
| Build or edit an HTML lesson, primer or mock | `docs/html-lessons.md` |
| A message starting `/update` or `/synthesize` | `docs/shortcuts.md` |
| Quiz or exam preparation: primer, mock, grading, mistake review | `docs/quiz-prep.md` (the `quiz-prep` skill points to the same file) |
| Before handing over any page that has an answer key | run `sh docs/run-checkers.sh EE-XXXX` |
| "When did X change?" / an old path | that course's `LOG.md` (history; search it, do not read it whole) |

Use one workflow for practice material: `docs/quiz-prep.md`.  The `course-assessment` skill (JSON question bank in `assessment/`) and the `self-study` skill (notes bank in `output/self-studying/`) are separate tools with their own folders; use them only when the learner names them, or to maintain pages they already built (`EE-6204/assessment/`, `EE-6221/output/self-studying/`).  For NTULearn use `ntulearn-browser` to sync and `ntulearn` to query what is already local; for RedNote use `rednote`.

## Course layout

```text
EE-XXXX/
  STATUS.md      # current state only; fixed template below
  LOG.md         # append-only history
  index.html     # launcher linking every HTML page (Safari needs it)
  resources/     # supplied material: slides, readings, transcripts-raw/, public archive
  notes/         # beginner-notes.tex, notes.tex and their PDFs
  quizzes/       # one folder per assessment: quiz-01/, quiz-02/, final/ (see docs/quiz-prep.md)
    final/       #   final-intel.md, pages, keys, checkers, final-pages/, quiz-assets/, attempts/
  tests/         # past exam papers (final papers are git-ignored: NTU-only)
  assignments/  projects/  figures/
```

- Put each file in the most specific folder.  Create a folder only when a file needs it.  Keep course material inside its own `EE-XXXX/`; do not touch another course unless asked.
- Name files in lowercase kebab-case with a zero-padded scope prefix: `lecture-03-state-space.pdf`, `quiz-02-mock-a.html`, `final-primer.html`, `week-07-transcript.txt`.  Do not guess an unknown number, date or type.  Existing files keep their names (EE-6204 and EE-6407 use `quiz-1-…`; continue each course's own pattern).
- Never overwrite or delete supplied source material or generated artifacts without being asked.  On a name collision add a distinguishing suffix.
- When a file moves or is renamed, record `old path -> new path` in `LOG.md` and fix every link, citation and script that used the old path, in the same change.
- Teaching material is in two forms.  HTML study pages are what the learner actually works from before each assessment.  The two LaTeX notes (`beginner-notes.tex` for a complete beginner, `notes.tex` for fast review) are the durable record; several topics do not have them yet, and `STATUS.md` says which.  Write or extend the LaTeX notes on `/update` or when asked; never claim LaTeX coverage that does not exist.

## STATUS.md and LOG.md

`STATUS.md` answers "what is true now and what is next".  Keep it under 100 lines, with exactly these sections:

1. **Now** – the next assessment (date, format, scope, with the source of each fact) and at most five open loops.
2. **Notes** – each note file and what it covers.
3. **Sources** – one row per source file or group: pages, where it is covered (or `not covered`), a short qualifier.
4. **Study pages** – one line per HTML page: path, purpose, checker script.
5. **Unresolved** – only questions still open.

Update `STATUS.md` in the same change as the work.  When an item is finished, settled or superseded, delete it from `STATUS.md` and add one dated line to `LOG.md`.  Verification details, scores, build notes and file moves go to `LOG.md`, never to `STATUS.md`.

## Git

- Work on `main` in the primary local checkout.  Before starting: `git pull --ff-only origin main`.  When the change is complete: commit and `git push origin main`.  The learner asked for this explicitly; it overrides "branch first / never push to main" for this repository only.
- Never force-push, rewrite published history, or make a non-fast-forward merge into `main`.
- If a task must run in a git worktree: finish by fast-forwarding `main` to the work (`git merge --ff-only`), push `main`, then remove the worktree and its branch, local and remote.  Do not leave finished work on a branch.
- Commit messages name the course and the change, e.g. `EE-6204: add Quiz 1 prediction paper`.

## Language

- Reply in English, including when the learner writes partly or wholly in Chinese.  Treat Chinese wording as a bridge to the technical idea: give the natural English term or question first, then answer in English.
- When the learner seems unsure how to say something in English, also teach the English: the vocabulary, a natural sentence pattern, and a brief usage distinction.  Example: for ``控制什么什么的是不是负反馈？'' first offer ``Is this control system using negative feedback?'' and clarify ``negative feedback'', ``closed-loop control'' and ``feedback controller''.
- Keep notes and study pages in English unless the learner asks for Chinese or bilingual text.  Short Chinese glosses are fine where they help vocabulary.

## Answering a learning question

1. Answer the question directly first.
2. Ground course-specific claims in the source: inspect the relevant pages before writing, and cite the file and page.  Mark anything that is your own explanation or example as such.
3. If the question is ambiguous or the source is missing, say so and ask for the page or context before making a source-specific claim.
4. Do not invent course policies, deadlines, weightings or official interpretations.  Mark unofficial information (student recollections, transcripts) as unofficial.
