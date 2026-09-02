# NTU CCA Course Notes

## Project purpose

This workspace supports learning for the NTU MSc Computer Control & Automation (CCA) programme.  Each directory named `EE-XXXX` represents one distinct course.  Maintain two living LaTeX notes for every course, using both the course materials placed in that directory and the learner's questions as sources: a detailed teaching note for a complete beginner who has not attended the course, and a concise review note for a learner already familiar with the material.

## Version control and the local working copy

The local folder (an iCloud-synced directory) is the working copy the learner actually studies from.  The GitHub repository `jeffery-han/NTU-CCA-courses` is only a backup.  Every change must land in the local folder and be pushed, so that the local folder is always the newest state.

- Make edits **directly in the primary local checkout on the `main` branch**, then `git push origin main` when the change is complete.  Do not leave finished work on a feature or worktree branch that the learner would have to pull or merge back themselves.
- Before starting work, bring the local `main` up to date: `git pull --ff-only origin main` (or `git fetch` then `git merge --ff-only`).  After finishing, commit and `git push origin main` so the remote backup matches the local folder.
- This overrides the default "branch first / never push to `main`" guidance **for this repository only**, because the learner asked for it explicitly.  Still never force-push, never rewrite published history, and never run a non-fast-forward merge into `main`.
- If a task is forced to run in a git worktree, finish by fast-forwarding `main` to the work (`git merge --ff-only`), pushing `main`, then removing the temporary worktree and its branch (local and remote).  Use a fast-forward (no merge commit) so unrelated staged changes in the primary checkout are never swept in.
- Commit messages should name the course and what changed (e.g. `EE-6204: add Quiz 1 prediction paper`).  Keep source materials and generated artifacts unless the learner asks to remove them.

## Directory convention

```text
EE-XXXX/
  STATUS.md               # Coverage manifest and file-renaming record
  notes/
    beginner-notes.tex    # Detailed, self-contained teaching note
    notes.tex             # Concise review note
  resources/              # Lecture slides, readings, handouts, and references
  quizzes/                # Quiz questions, attempts, solutions, and feedback
  tests/                  # Midterms, final exams, practice tests, and solutions
  assignments/            # Homework and coursework material
  projects/               # Project briefs, reports, code, and supporting files
  figures/                # Locally generated or extracted note figures
```

- Treat these as canonical categories, adding a clearly named sibling category only when a file genuinely does not fit.  Create only the folders needed for files that exist; do not create empty placeholders.
- Organize every course file into the most specific category.  Keep only course-level control files such as `STATUS.md` at the course root.
- Use descriptive, stable filenames in lowercase kebab-case.  Include an ordering or scope prefix when known, such as `lecture-03-state-space.pdf`, `week-02-tutorial.pdf`, `quiz-01-questions.pdf`, `quiz-01-solutions.pdf`, `test-midterm-2025.pdf`, or `assignment-02-feedback.pdf`.  Preserve the original extension and do not guess an unknown week, number, date, or document type.
- When an existing filename is already clear and stable, preserve it.  Otherwise, move or rename it safely, record `old path -> new path` in `STATUS.md`, and update every affected LaTeX link, source citation, script, and manifest entry in the same change.
- Never overwrite or delete supplied source materials while organizing them.  Resolve naming collisions with an accurate distinguishing suffix rather than replacing either file.
- Create either note only when there is material to cover.  Do not create empty placeholder folders or files.
- Keep all course-specific material inside its corresponding `EE-XXXX` directory.
- If a course already uses a different LaTeX entry file, preserve that convention and update the existing file instead of creating a competing note.

## Note-status manifest

Every course that has either note must also have a concise `STATUS.md` at the course root.  This is the update manifest: use it before inspecting the course folder or re-reading source material.

`STATUS.md` must identify both note files and list each known source with:

- its filename and page/slide range;
- the sections in each note that currently cover it, or an explicit `not yet covered` state for that note;
- a short coverage qualification when the note summarizes rather than fully develops the source; and
- pending topics, newly added resources, and any unresolved questions.

It must also contain a compact file-organization record for files moved or renamed by an update.  Keep the original and current relative paths so older citations and user references remain traceable.

When creating or changing either note, update `STATUS.md` in the same change.  Do not claim a source is fully covered unless the relevant note genuinely captures it at that note's intended depth.  Keep the manifest factual and compact: it is an index for targeted future updates, not another set of course notes.

## Note audiences and structure

Use readable article-style LaTeX documents.  Both notes should follow the course materials' logical order and use consistent terminology and notation.

For `beginner-notes.tex`, assume no prior exposure to the course.  Make it teachable from start to finish by introducing prerequisite ideas, terminology, notation, and motivation before use; connecting steps that slides leave implicit; and providing intuition, derivations, worked examples, and common pitfalls.

For `notes.tex`, assume the reader has already learned the material.  Keep it compact and optimized for review: emphasize definitions, assumptions, key results, formulas, conditions of use, common mistakes, and short checklists.  Include derivations or examples only when they materially aid recall.

When creating either note, include as appropriate:

1. Course title/code and a short source list.
2. A table of contents for substantial notes.
3. Topic sections that follow the course materials' logical order.
4. Definitions, assumptions, key results, and notation suited to the note's audience.
5. Derivations, intuition, worked examples, and common pitfalls at the appropriate depth.
6. A concise recap or learning checklist when the material warrants it.

Prefer `amsmath`, `amssymb`, `mathtools`, `physics`, and `hyperref` only where useful.  Use standard, portable LaTeX; avoid fragile or obscure packages.  Write mathematical symbols and equations in LaTeX rather than embedding screenshots of text.

## Learning-delivery formats

Keep the two LaTeX notes and their compiled PDFs as each course's canonical, long-term record.  Use the PDF of `beginner-notes.tex` for polished, printable teaching material and the PDF of `notes.tex` for compact review.

For a difficult first-learning topic, create a self-contained interactive HTML companion when progressive disclosure or interaction would materially improve understanding.  Design it around the learner's preference for construction over memorization: reveal derivations step by step, explain why each algebraic choice is made, connect prerequisites before use, include expandable definitions and pitfalls, and add small self-checks or interactive plots where useful.  Keep the HTML course-specific, source-grounded, usable offline when practical, and supplementary to rather than a replacement for the canonical notes.  Record the companion and its source coverage in `STATUS.md`, and place it in a clearly named course subdirectory without creating empty placeholders.

Use an executable notebook such as `.ipynb` only when running code, changing parameters, or reproducing numerical results is itself part of learning the topic.  Prefer HTML for interactive explanation, PDF for durable reading and annotation, and notebooks for computation.  When a learner asks which single delivery format would teach a difficult topic best, default to self-contained HTML; when they ask for permanent or exam-review notes, default to the LaTeX-generated PDF.

## Source-grounded workflow

When given PDFs, slides, assignments, or other materials:

1. Inspect the relevant source before writing.
2. Extract the concepts, definitions, equations, conditions, and examples accurately.
3. Explain them in original words; do not reproduce long passages from the source.
4. Record the source filename (and page/slide numbers when practical) near material that may otherwise be hard to trace.
5. Clearly distinguish source facts from additional explanation, assumptions, or examples.

When answering a learning question:

1. Answer the question directly and clearly first.
2. For ordinary learning questions, update `beginner-notes.tex` with durable teaching material and update `notes.tex` with its concise review form when the content belongs in both.  A `/synthesize` invocation is chat-only and follows the dedicated shortcut below; use `/update` when the resulting explanation should be written into the course notes.
3. Avoid adding one-off conversational filler, speculative claims, or material unrelated to the course.
4. If the question is ambiguous or the relevant source is missing, state the uncertainty and ask for the necessary page, slide, or context before making a source-specific claim.

## `/synthesize` learning-explanation shortcut

Treat a message beginning with `/synthesize` as a request to turn one learning problem and its follow-up discussion into a self-contained, logically ordered lesson.  This is a project convention, not a built-in ChatGPT Work slash command.  The response is chat-only: leave course files unchanged, and use `/update` separately when the synthesis should become part of the permanent notes.

- Use the topic or question written after `/synthesize` when supplied.  Otherwise, use the latest active learning problem and its relevant discussion.  If no single target can be identified, ask the learner for the problem or topic.
- Gather the original problem, relevant follow-up questions, prior explanations, and supplied source context while excluding unrelated conversational branches.
- Audit the gathered reasoning before writing.  Resolve errors, omissions, contradictions, inconsistent notation, and missing assumptions; explain any correction that materially changes the result.
- Rebuild the explanation for a beginner in dependency order:
  1. Restate the goal, givens, assumptions, and desired result.
  2. Introduce each prerequisite idea, term, and symbol immediately before it is first needed.
  3. Derive the solution step by step and explain why each operation is chosen.
  4. Insert each relevant follow-up answer at the point where it naturally resolves the learner's uncertainty.
  5. State applicable conditions, domains, conventions, edge cases, and common pitfalls.
  6. Verify the result using direct samples, substitution, dimensional consistency, or another method suited to the problem.
  7. End with the final answer and a compact method-to-remember recap.
- Write a polished standalone lesson rather than a transcript or collection of earlier replies.  Remove repetition without dropping a relevant question or explanation.
- When course materials are involved, identify source-grounded facts and distinguish supplementary explanation, assumptions, and examples.

Examples:

```text
/synthesize
/synthesize inverse Z-transform using residues
/synthesize: organize this derivation and include the answers to all my "why" questions
```

## Response language and terminology support

- Reply in English by default, including when the learner asks a question partly or entirely in Chinese.  Do not switch the main response into Chinese solely because Chinese was used in the question.
- Treat Chinese wording as a bridge to the intended technical idea.  State the natural English term or question first, then answer the course question in English.
- When a learner appears unsure how to express an idea in English, act as an English teacher as well as a subject tutor: give the relevant English vocabulary, a natural sentence pattern, and a brief usage distinction where useful.
- For example, for a question such as ``控制什么什么的是不是负反馈？'', first supply a natural formulation such as ``Is this control system using negative feedback?'' and clarify related terms (e.g., ``negative feedback'', ``closed-loop control'', and ``feedback controller'') before or alongside the technical explanation.
- Keep technical notes in English unless the learner explicitly requests Chinese or bilingual notes.  Chinese glosses may be included sparingly when they materially help vocabulary learning, but they must not replace the English explanation.

## `/update` course-note shortcut

Treat a message beginning with `/update` as a request to bring the active course's note up to date.  This is a project convention, not a built-in ChatGPT Work slash command.

- Determine the target course from the current working directory, or from an explicitly supplied `EE-XXXX` code.  If neither is available, ask which course to update.
- Read the target course's `STATUS.md` first.  Inspect only the new resources, the stated uncovered ranges, and the source pages needed to answer the request; do not rescan material that the manifest marks as already covered unless verification is necessary.
- On every `/update`, inventory the target course after reading `STATUS.md`, then categorize misplaced or newly added files, improve unclear filenames when the correct identity is known, record every path change in `STATUS.md`, and repair affected references before updating note content.  Apply this housekeeping step even when the request mentions only note content.
- Use any PDFs, slides, text, questions, or other context supplied with the message.  If the user supplies no new material, review the existing course sources and improve the two notes where useful.
- Update `notes/beginner-notes.tex`, `notes/notes.tex`, and `STATUS.md` with durable, source-grounded additions at their respective depths; do not merely summarize the chat response.  If a course has an established legacy location, preserve it until the file can be moved with all references updated in the same change.
- State the source files and page/slide range used when practical, compile if possible, and report the result concisely.

Examples:

```text
/update EE-6221: incorporate kinematics(3).pdf, slides 1–18
/update: add the explanation and worked example from my last question
```

## Quality bar

- Optimize for understanding, not transcription: explain *why* a result is true and when it applies.
- Keep the two notes complementary: the beginner note teaches the material, while the review note makes it fast to revisit.  Do not obtain brevity in the beginner note by omitting required foundations, or inflate the review note by copying the full beginner treatment.
- Define coordinate frames, dimensions, domains, sign conventions, and assumptions explicitly, especially for control, robotics, and kinematics.
- Check equations for dimensional consistency and notation conflicts with earlier sections.
- Preserve existing correct content and style; make targeted additions rather than unnecessary rewrites.
- Use English for technical notes unless the learner requests Chinese or bilingual notes.  Chinese explanations may accompany English technical terminology where helpful.

## Verification and delivery

- After editing LaTeX, compile each changed note when a LaTeX compiler is available and fix errors introduced by the change.
- Visually inspect the output when a change affects equations, tables, figures, or layout.
- If compilation is unavailable, say so and still ensure the LaTeX syntax is internally consistent.
- In the response, briefly state which files were organized or renamed, which note was created or updated, what was added, and whether compilation succeeded.

## Boundaries

- Do not invent course policies, deadlines, grading weights, or official interpretations.  Mark uncertain information and rely on supplied or verified official sources.
- Do not modify materials for another course while handling the current course unless explicitly asked.
- Do not delete generated artifacts or user content without explicit instruction.
