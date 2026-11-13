# EE6407 Quiz 2 retrain handoff

Updated: 10 November 2026, Asia/Singapore.

## Goal and current state

Personalise the Retrain section of `quiz-2-cycle.html` around the learner’s Mock C attempt. Changes are applied to the original local Courses checkout on `main`. They are not committed or pushed because this session cannot write to `.git`.

The learner clarified that omitted arithmetic reflected time pressure and reluctance to type calculator results, not necessarily a lack of understanding. Prioritise conceptual decisions and explanations. Do not restore mandatory calculator-heavy drills without being asked.

## Learning evidence

- Initial exported self-mark was 0/100 because rubric boxes were unticked. The chat estimated approximately 63/100 with partial credit; this is not an official grade or a calibrated diagnostic score. The estimate counted the F-score formula as correct at the learner’s request.
- Initially, precision and recall were swapped; sensitivity was forgotten, specificity omitted, and the effect of doubling actual negatives was uncertain.
- A subsequent screenshot correctly demonstrated recall/sensitivity, specificity, precision, their denominators, and the effect of doubling actual negatives. All 14 entries were independently checked against the page’s tolerance. Some decimals were truncated rather than rounded. This supports improvement on that example, not universal mastery.
- Screenshot counts: TP=133, FP=13, FN=19, TN=150. Actual positives=152; predicted positives=146. After doubling actual negatives, FP=26 and TN=300. Recall remains 0.875; specificity remains approximately 0.9202. Correct four-decimal rounding: original precision 0.9110, original F 0.8926, new precision 0.8365, new F 0.8553, new accuracy 0.9059, new error 0.0941.
- k-means: correct first centroids, B’s movement and final clusters in the initial attempt; SSE method understood. Numerical final centroids and SSE were not supplied, so their omission does not establish a conceptual gap. The written comparison repeated the same centroid on both sides; reinforce comparison against both centroids. C’s initial squared distance was written as 3 instead of 4.
- Fisher: all four ratio expressions were correct; explicit feature ordering was missing. Do not diagnose a variance-concept failure from this attempt.
- Peaking: the explanation was assessed as full credit in chat. Optional polish is unreliable parameter estimates from fixed N and the conclusion to select features.
- Weighted Gini was revealed in Train after a wrong try. Retain sample-weighting practice. No subsequent learner attempt on the new k-means/Fisher/Gini drills has been observed.

## Implemented changes

| File | Current role |
| --- | --- |
| `quiz-2-cycle.html` | Personalised feedback, session instructions, closable topic reviews, worked examples and targeted practice. |
| `quiz-2-cycle-check.mjs` | Independent checks of original keys, review examples, supplied calculations, dropdown answer keys and rendering. |
| `../STATUS.md` | Dated record of the personalised retrain, reviews and concept-focused revision. |

Current practice:

- Metrics retains numerical entry; the learner’s screenshot demonstrated the repaired distinctions. Further practice is optional from a tutoring perspective, although the existing two-correct streak still controls the page’s closed status.
- k-means supplies distances, candidate centroids and SSE values. Dropdowns test membership, updating both centroids, convergence and the SSE definition.
- Fisher supplies calculated ratios. Dropdowns test the variance denominator and rank all four features.
- Gini supplies counts and impurities. Dropdowns test sample-weighted expressions, gain direction and which child receives more weight. Child sizes are unequal so a plain average is not accidentally valid.
- Peaking stays optional, with a self-assessed rewrite and the existing T6 checklist.
- Concept-choice positions are shuffled; answers are checked using the existing numeric-value path. Wrong selections reveal the correct option text. Explanations are provided after checking; the learner’s spoken/written reasons are not automatically graded.
- Two fully correct fresh problems close a numeric/dropdown topic. A wrong or blank answer resets its streak. Reviews and worked examples are visible before practice; fresh-problem keys remain hidden until checked.

## Progress and limits

- Existing localStorage key is unchanged: `ee6407-quiz2-cycle-v1`. Train/Test data and the self-mark rubric were preserved; no score or completion boxes were automatically filled.
- Saved topic tries, streaks and closed status remain in localStorage. Active generated problems live in the in-memory `live` object and do not survive refresh. Dropdown restoration was tested during re-rendering, not across browser reloads.
- Concept drills demonstrate method selection, not calculator speed or a full unaided written solution.
- Original Train/Test content, LaTeX notes and supplied source materials were not edited.

## Verification and blockers

Latest verification passed:

```sh
node EE-6407/quizzes/quiz-2-cycle-check.mjs
git diff --check
```

The checker verifies 2,000 problems per generator (8,000 total), including independent 2-D k-means iteration, supplied Fisher ratios, Gini arithmetic, correct/incorrect/blank choices, unique options, targeted queue behaviour and dropdown re-rendering/feedback. Inline scripts also passed syntax checks.

Actual browser rendering and reload persistence remain unverified: Chrome headless failed earlier, and Computer Use reported that the browser access host was unavailable. Do not describe this as a completed browser test.

`git pull --ff-only origin main` failed on `.git/FETCH_HEAD`; staging failed on `.git/index.lock`, both with “Operation not permitted”. Courses files are writable, but `.git` remains explicitly read-only. Do not bypass this restriction or claim the backup is synced.

## Next steps

1. Have the learner refresh the original HTML, continue with the concept drills, and assess their explanations before assigning more arithmetic.
2. When browser access works, check review folding, dropdown feedback, narrow-screen layout and saved topic status across reloads without resetting the learner’s real progress.
3. When normal Git write access is available, inspect status and the current diff, sync `main` safely, then commit and push only this task’s four files: the HTML, checker, course STATUS and this handoff. Follow the root `AGENTS.md`; do not force-push or sweep in unrelated changes. The checkout has numerous unrelated modified/untracked files.

Earlier prepared copies and a patch remain in `/Users/jefferyhan/Documents/Codex/2026-11-10/dear-all-this-assignment-contains-questions/`. They predate the reviews and concept-focused revision. The current Courses files are authoritative; do not reinstall those stale copies.
