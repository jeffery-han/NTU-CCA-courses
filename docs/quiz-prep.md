# Quiz and exam preparation loop

Read this before building a primer or mock, grading an attempt, or planning revision for a quiz or final.  Page-building rules (layout, citations, checks, Safari) are in `docs/html-lessons.md`; this file is the process.

The learning happens when the learner sits a paper cold, finds out exactly why each lost mark was lost, and retries a fresh variant.  Everything before that is setup.  Keep priming to about a fifth of the learner's time.  If you are writing a long explainer before the learner has attempted a question, stop and build the mock.

## Start here: find the current step

1. Read the course `STATUS.md`.  "Now" names the next assessment and the current step of this loop.
2. Read `quizzes/<assessment>/<assessment>-intel.md` and `quizzes/<assessment>/<assessment>-mistakes.md` if they exist.
3. Resume at the first step below that is not done.  Do not rebuild a file that exists; `STATUS.md` "Study pages" lists them.
4. When a step finishes, update "Now" in `STATUS.md` with the next step, in the same change.

`<assessment>` is `quiz-01`, `quiz-02`, … or `final` (follow the course's existing pattern, e.g. `quiz-2` in EE-6204 and EE-6407).

## Folder layout: one folder per assessment

Every prep file for an assessment lives in its own folder, `quizzes/<assessment>/`, named exactly like the file prefix: `quizzes/quiz-01/`, `quizzes/quiz-02/`, `quizzes/final/` (or `quizzes/quiz-1/` where the course uses `quiz-1-…`).  Nothing for a specific assessment sits loose in `quizzes/`.

```text
quizzes/
  quiz-01/
    quiz-01-intel.md  quiz-01-mistakes.md
    quiz-01-primer.html  quiz-01-mock-a.html  quiz-01-mock-a.md  quiz-01-mock-a-check.py
    quiz-01-pages/      # rendered source pages for citation pop-ups
    quiz-assets/        # this folder's own KaTeX/MathJax copy and figures (Safari: no ../)
    attempts/           # the learner's scanned scripts for this assessment
  quiz-02/  …
  final/    …
```

- Create the folder when the first file for that assessment is made.  Each folder is self-contained for Safari: its own maths bundle, page images and figures; copy a shared figure rather than linking across folders.
- Links inside a page: siblings in the same folder by bare name; the course's source PDFs as `../../resources/<file>.pdf#page=N`; a page in another assessment's folder as `../<other>/<page>.html`, with a note that Safari users open it from the course `index.html`.
- **Migrating a course still laid out flat**: the first time a course's `quizzes/` is touched under this rule, move every `<assessment>-*` file (and its `-pages/` folder, figures and attempts) into its folder; give each folder its own asset copy; rewrite `../resources/` to `../../resources/`, cross-assessment links, export/key paths (`quizzes/<assessment>/…`) and any links from `index.html`, `output/` or notes; record the mapping in `LOG.md`; run `sh docs/run-checkers.sh EE-XXXX` and open a page in a browser.  Do it in a change of its own, and not while another job has uncommitted edits in that course's `quizzes/`.  EE-6221 is the reference layout (migrated 2026-11-21).

## Step 1 – Sync NTULearn (every session, before anything else)

A mock built on stale sources teaches wrong formulas and misses topics.

- Run the `ntulearn-browser` sync for the course: slides, Media Gallery transcripts, announcements, assessment pages.  File new items by the layout in `AGENTS.md`; add them to `STATUS.md` "Sources".
- List every lecture week and slide deck up to the assessment and mark each **local** or **missing**.  Tell the learner what is missing before continuing.  If the browser is unavailable, say so and ask for the files.
- Never report a transcript as "not posted" without a screenshot of its Attachments tab.
- Read the official announcement for date, venue, duration, format, aids and scope.  Put those facts, with their source, in `STATUS.md` "Now".

## Step 2 – Gather evidence into `quizzes/<assessment>/<assessment>-intel.md`

Check sources in this order:

1. **Official past papers** (NTU Library exam papers, for finals).  Save as `tests/test-final-<year>-s<N>.pdf`.  They are git-ignored; never commit them.  Reserve the two most recent papers for the last two steps of a final protocol and do not reuse their numbers in mocks.
2. **Lecturer statements**: the announcement, and scope or "this will be tested" remarks in the transcripts (cite week and file).
3. **Peer material**: tutor decks, the class group chat export, the local `resources/public-archive-*/`.
4. **RedNote** recollections (the `rednote` skill).

Start the file with a sources-consulted table.  Classify every claim:

| Evidence | Trust | Use |
|---|---|---|
| Format: counts, types, duration, aids, scope boundary | High when official or when several independent people agree | Sets the mock's structure |
| Question text | Medium | Re-derive; wording is approximate |
| Student answer keys | Low | Never adopt; re-derive every answer |

Also record in the intel file:

- **The scope boundary**, with the exact source (announcement line, slide number, lecturer remark).  Re-check it when a new source arrives.
- **A convention list**: every formula whose form differs between textbooks, checked against the **slides** with page numbers (e.g. EE-6407 Gini is `½(1 − Σp²)`, not `1 − Σp²`).  Every page built later uses these conventions.
- **Conflicts**, shown as both readings, not smoothed into one.

Everything from student recollection is unofficial: label it so in every file it reaches.  Never state a date, time or venue from student posts.

## Step 3 – Light primer

`quizzes/<assessment>/<assessment>-primer.html`: per in-scope topic, the idea in two or three sentences, the formulas, one worked example, one or two checks with immediate feedback.  No long derivations.  Link to an existing study page instead of rewriting it.  Skip topics the learner already passes.

If the learner then asks for more explanation of one part, rebuild that part from zero as a collapsible "Start here" block: picture first, a symbol table, each formula derived, the reason behind each condition, one verified example, one self-check.

## Step 4 – Guided mock (optional; use when the learner cannot yet attempt the paper)

`quizzes/<assessment>/<assessment>-mock-a-guided.html`: a full paper in the real format, broken into checked steps.  The learner answers each step first; the hint and worked line open only after an attempt.

## Step 5 – Cold mock

Two files, kept separate on purpose:

- `quizzes/<assessment>/<assessment>-mock-<x>.html` – the paper, with **no answers** in it.  Real section counts, question types, marks and time limit; a timer; autosave; an "answered on paper" toggle for written questions; an export button that produces one plain-text block (paper name, key-file path, marks, elapsed time, each answer, `<blank>` markers) readable in a fresh conversation.
- `quizzes/<assessment>/<assessment>-mock-<x>.md` – questions, full key, a per-checkpoint marking rubric with a stated total, and "common wrong paths and what each implies" for every question.
- `quizzes/<assessment>/<assessment>-mock-<x>-check.py` – recomputes every key.  Run `docs/run-checkers.sh EE-XXXX` before handing the paper over.

Rules for the paper:

- Mirror the real format.  Do not replace free response with multiple choice because it is easier to mark.
- Honour the real aids.  No calculator means numbers that work by hand, or a supplied table.
- Use new numbers and a different angle from every existing page.  Search the notes and existing mocks for your worked values before writing.
- Follow the convention list from the intel file and the conventions in the notes.
- Pitch difficulty at or slightly above the real paper.  This semester's quizzes ran harder than the recollections predicted.
- Include one unseen item from an in-scope topic that circulating papers omit, labelled as a prediction in the `.md`.

The learner sits it closed book and timed, handwritten when the real paper is handwritten.  Handwritten scripts go to `quizzes/<assessment>/attempts/<paper>-<date>.pdf` (or `.jpg`).

## Step 6 – Grade

Mark against the rubric part by part and state the total.

- Give method marks where the approach was right; say which checkpoint earned them.
- A blank is **blank, not wrong**.  Report blanks separately: out of time, or out of knowledge?
- Separate arithmetic slips from concept errors.
- State how sure each mark is: *derivable* (method is unambiguous: mark firmly), *convention-dependent* (depends on the lecturer's wording: say what the course material supports), or *disputed* (sources conflict: show both and say which is safer to write).
- Where the learner was wrong, show the correct derivation, not only the answer.
- Save the grading as `quizzes/<assessment>/<paper>-attempt-<date>-marked.md`, one per paper sitting, extended as later questions are graded: a marks table by rubric item, a transcription of what was written (tables, matrices, key numbers), the verdict and correct value for each lost mark, and mistakes-log numbers.  Later sessions read this file instead of re-reading the scan; grading boxes in HTML pages may repeat it for the learner.

## Step 7 – Retrain on every mistake (most of the time goes here)

For each wrong or blank item, largest mark loss first:

1. **Diagnose**: quote what was written, name the step that went wrong, and say whether it was a slip, a concept gap or a misread question.
2. **Teach only that gap**, from zero if needed.
3. **One rule to remember**, in one line.
4. **Retry** on a fresh variant.  The item stays open until the retry is right.

Log each item in `quizzes/<assessment>/<assessment>-mistakes.md`: question, what was written, why wrong, rule, retry result (open / closed).  Then run the next cold mock weighted toward the open items, and repeat steps 5–7.

## Step 8 – Fold back into the notes

For each mistake that showed a real gap (not a slip): add the explanation to the course's teaching note and its short form to the review note (`docs/notes-style.md`; `STATUS.md` "Notes" names the files), recompile, and correct any mock wording the grading showed to be wrong, saying so openly.  If the course has no LaTeX note for that topic yet, add the explanation to the relevant study page as a "Start here" block and leave the gap listed in `STATUS.md`.

## Final-exam protocol

Use this sequence for a final; write the chosen steps as a table in `quizzes/final/final-intel.md` and track the current step in `STATUS.md` "Now".

| Step | Material | Mode |
|---|---|---|
| 1 | `final-primer.html` | Light primer, one card per examined topic |
| 2 | `final-mock-a-guided.html` | Full paper as checked steps |
| 3 | Mock B | Cold, full length, handwritten; graded |
| 4 | Retrain | Every lost mark, logged in `final-mistakes.md` |
| 5 | Mock C | Cold, new numbers, weighted to the open mistakes |
| 6 | Hard mock H | Cold, wider topic range and harder traps than past papers |
| 7 | Second most recent official paper | Cold, exam conditions; graded and retrained |
| 8 | Most recent official paper | Dress rehearsal, then a re-test built from the mistakes log |

Shorten it when time is short: keep steps 1, 3, 4 and 7.  Start by carrying forward the open items from the course's quiz mistake logs; they are the best predictor of marks lost in the final.

## Always

- Re-derive every answer independently and sanity-check it (a permutation operator returns a permutation; a decoded value lies inside its interval).
- Never invent policies, weightings, dates or official interpretations.
- Keep the course's material inside its own `EE-XXXX/` folder.
