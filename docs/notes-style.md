# Writing the LaTeX notes

Read this before creating or editing `notes/*.tex`.

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
