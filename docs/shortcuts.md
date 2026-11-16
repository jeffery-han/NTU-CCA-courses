# Project shortcuts: `/update` and `/synthesize`

These are project conventions, not built-in slash commands.

## `/update` course-note shortcut

Treat a message beginning with `/update` as a request to bring the active course's note up to date.

- Determine the target course from the current working directory, or from an explicitly supplied `EE-XXXX` code.  If neither is available, ask which course to update.
- Read the target course's `STATUS.md` first.  Inspect only the new resources, the stated uncovered ranges, and the source pages needed to answer the request; do not rescan material that the manifest marks as already covered unless verification is necessary.
- On every `/update`, inventory the target course after reading `STATUS.md`, then categorize misplaced or newly added files, improve unclear filenames when the correct identity is known, record every path change in `LOG.md`, and repair affected references before updating note content.  Apply this housekeeping step even when the request mentions only note content.
- Use any PDFs, slides, text, questions, or other context supplied with the message.  If the user supplies no new material, review the existing course sources and improve the two notes where useful.
- Update `notes/beginner-notes.tex`, `notes/notes.tex`, and `STATUS.md` with durable, source-grounded additions at their respective depths; do not merely summarize the chat response.  If a course has an established legacy location, preserve it until the file can be moved with all references updated in the same change.
- State the source files and page/slide range used when practical, compile if possible, and report the result concisely.

Examples:

```text
/update EE-6221: incorporate kinematics(3).pdf, slides 1–18
/update: add the explanation and worked example from my last question
```

## `/synthesize` learning-explanation shortcut

Treat a message beginning with `/synthesize` as a request to turn one learning problem and its follow-up discussion into a self-contained, logically ordered lesson.  The response is chat-only: leave course files unchanged, and use `/update` separately when the synthesis should become part of the permanent notes.

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
