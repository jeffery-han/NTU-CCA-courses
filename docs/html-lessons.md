# Interactive HTML study pages

Read this before building or editing any learner-facing HTML page (lesson, primer, mock).

## Learning-delivery formats

Where the two LaTeX notes exist, they and their compiled PDFs are the course's durable record.  Use the PDF of `beginner-notes.tex` for polished, printable teaching material and the PDF of `notes.tex` for compact review.

For a difficult first-learning topic, create a self-contained interactive HTML companion when progressive disclosure or interaction would materially improve understanding.  Design it around the learner's preference for construction over memorization: reveal derivations step by step, explain why each algebraic choice is made, connect prerequisites before use, include expandable definitions and pitfalls, and add small self-checks or interactive plots where useful.  End every named part or module with an exercise or explicit verification of the idea just taught, with immediate feedback before the learner continues.  Write the companion as authored teaching text — numbered parts, short paragraphs, inline worked examples — never as dumped notes-bank or slide-summary text, and keep process labels (`generated`, "sympy-checked") out of it.  Pitch exercises at the real assessment's difficulty (multi-step hand calculations, True/False with a reason, self-marked derivations), keep answers hidden until attempted, and verify every numeric key in a checker script.  Save answered checks in `localStorage` (stable keys, try/catch, a reset control) so a refresh does not erase progress.  The full checklist is the "Checklist" section below.  Keep the HTML course-specific, source-grounded, usable offline when practical, and supplementary to rather than a replacement for the canonical notes.  Make every source citation in the companion, including named references such as a lecture example or section number, open a pop-up showing the cited source pages as images, with a link to the original PDF at that page.  Record the companion and its source coverage in `STATUS.md`, and place it as "File conventions" below says.

Use an executable notebook such as `.ipynb` only when running code, changing parameters, or reproducing numerical results is itself part of learning the topic.  Prefer HTML for interactive explanation, PDF for durable reading and annotation, and notebooks for computation.  When a learner asks which single delivery format would teach a difficult topic best, default to self-contained HTML; when they ask for permanent or exam-review notes, default to the LaTeX-generated PDF.

## File conventions

- Safari on `file://` refuses to load anything through `../`.  So every folder that holds HTML keeps its own `vendor/` (MathJax) and its own page-image folder beside the pages, and every course has a root `index.html` launcher that links to all pages.  Add each new page to the launcher.
- The vendored MathJax bundle cannot autoload extensions: `\boldsymbol` stops all typesetting, so use `\mathbf`.
- Put new pages in `quizzes/`, so one `vendor/` and one image folder serve them.  Name the image folder `<assessment>-pages/` (e.g. `quiz-03-pages/`, `final-pages/`) and each image `<pdf-stem>-pNNN.jpg`.
- Each page with numeric keys has a checker script beside it (`<page>-check.py`) that recomputes every key.  Run it before handing off; `sh docs/run-checkers.sh EE-XXXX` runs every checker in a course.
- Record each new page as one line in the course `STATUS.md` "Study pages" section: path, what it is, its checker.

## Citations and page pop-ups

- Every source citation, and every named reference such as "Lecture Example 6.2" or "§7", is a link: `<a href="../resources/<file>.pdf#page=N" data-pages="<pdf-stem>:<first>-<last>">`.  `N` is the PDF page index, not the printed page number; check for an offset (EE-6204 `lecture-00`: printed p. 98 is PDF p. 103).
- Clicking the link opens one shared `<dialog>` that shows the cited pages as JPG images from the page-image folder beside the HTML file.  Reference implementations: `EE-6204/notes/quiz2-prep-learning.html` (PDF pages) and `EE-6203/notes/quiz2-prep-learning.html` (slides).
- Render pages with a Swift PDFKit script (this machine has no poppler or mutool).  Watch for `/Rotate` pages, and do not pipe the renderer into `head`.
- Confirm that every target PDF and every image exists (the checker script should assert it) and spot-check that each page shows the cited content.

## Layout

- Self-contained and offline, light and dark colour tokens, palette and structure taken from the course's existing pages.
- A page with more than a few sections gets a sticky contents sidebar, modelled on `EE-6203/notes/quiz2-prep-learning.html`: a 270px left column (`.app` grid `270px minmax(0,1fr)`; `position: sticky; height: 100vh; overflow-y: auto`) with the page title, one link per section built by script from the headings, a per-section `done/total` score that turns green when complete, and links to sibling pages.  Give the content column `min-width: 0`.  Under 860px the sidebar moves to the top as a two-column link grid.  Do not keep a second inline contents box.

## Checklist

Each rule records a failure a learner reported on a shipped page.
## Teaching text, not a source dump

- Do not print `content`, `examples` or `exercises` verbatim into the lesson, even inside a collapsed block. Learners read it as unprocessed slide text. Author the lesson itself.
- Build each module from numbered parts in source order. Within a part, use short paragraphs: motivation, then definition, then intuition, then a worked example, then a pitfall. Introduce each symbol before its first use.
- Turn slide lists into explanation around one organising idea. For example, sort sensor families into "rate sensors integrate and drift" versus "absolute references correct them" instead of listing one slide per family.
- Collapse each slide conflict (wording that differs between pages, a label the lecturer overrode) into one short pitfall or exam-tip callout that states the answer to give. Do not narrate page-by-page.
- Keep process labels out of learner text: `generated`, `historical`, "agent-derived", "checked with sympy", "machine transcript". Keep provenance in the bank's `source_locator` and in the course manifest. Tell the learner only what affects trust, such as "supplementary example" or "the slide only poses this question".
- Put each worked example inline where it is needed, as its own visually distinct block.

## Depth follows the assessment scope

- Sort each part by what the assessment tests, not by how much the slides say. Teach at full depth, with every step and a real check: the lecturer's named key points, examinable derivations, and definitions that true/false items can test. Cut to a short gist and one concept check: background, hardware specifications, and slides the lecturer called "not tested".
- Mark every part with a visible depth badge (for example "Quiz focus" or "Idea only") and explain the badges once at the top.
- Do not drill arithmetic the assessment cannot ask for, such as log or picosecond calculations in a no-calculator quiz. Keep needed reference formulas in a collapsed "reference" block. Do not use folding to hide over-long text: if a part is background, rewrite it short.
- When a check is removed or replaced, give the new check a new legend. Saved progress is keyed by legend, so reusing one would mark the new check as already done.

## Exercises that teach

- End every named part with a check that gives immediate feedback. If the page claims this, count the parts to confirm it.
- Match the real assessment's format and difficulty. Read the quiz intel first. Prefer:
  - multi-step hand calculations with numbers that work without a calculator;
  - True/False items built on real misconceptions, whose feedback gives the one-line reason;
  - for each examinable derivation, "predict the next move" step reveals plus a self-marked derivation with a model answer.
- Avoid one-step recall such as "V(3X) = ?".
- Never print an answer directly after its question. Hide solutions behind a reveal shown after the attempt.
- Give every distractor feedback that names the specific misconception it represents.
- Numeric inputs must accept fractions such as `4/3`. Do not set `inputmode="decimal"`, because the iOS keyboard then has no `/` key.
- Compute every numeric answer independently in the page's checker script, so a wrong key fails the build. Recompute every new worked number exactly with fractions or sympy before publishing.

## Progress must survive a refresh

- Save each answered check in `localStorage` and restore it on load. Without this, a refresh wipes the learner's work.
- Key each check by a stable identity, such as section id plus legend, not by position. Assert in the checker that these keys are unique.
- Restore by replaying saved answers through the existing handlers, so feedback and tallies rebuild in one code path.
- Wrap every storage call in try/catch. The page must still work when storage is blocked.
- Provide a visible "Reset my answers" control.
- Test it in a real browser: answer, reload, confirm the state came back; reset, confirm it cleared.

## Rewrites keep coverage

- Before rewriting a lesson, record the set of cited source pages. Afterwards, list every page that lost its citation and either cite it again or confirm it holds no teachable content (references, history, title slides).

## Rendering traps

- KaTeX does not render inside attributes such as `data-feedback`. Use Unicode math there.
- If a build step splits HTML with a tag regex, keep raw `<` and `>` out of attribute values and math. Write `\lt`, `\gt` or entities instead.
- Show matrices as display math. Inline matrices break their lines badly.
- Before handing off, open the page and confirm three things: no KaTeX errors, no horizontal overflow at phone width, and every interactive check accepts its key and rejects a wrong value.
