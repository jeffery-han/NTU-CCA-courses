# EE-6204 Quiz 1 — evidence report

Built 2026-09-04 for `assessment/question-bank.json` (the second MCQ mock; the first is
`quizzes/quiz-1-mcq-practice.*`). This report separates **current official scope** from
**historical evidence**, and states what the mock does and does not claim.

## 1. Current official scope (authority: `official-scope`)

`quizzes/quiz-1-official-announcement.pdf` — Prof. Su Rong's NTULearn announcement, sent
2026-09-02 — is the single authority. It states:

- **When / where / how:** Fri 4 Sept 2026, 20:30–21:30, LT1, in person, MCQ, Respondus
  LockDown Browser, passcode released 20:29, one submission. 60 minutes given, roughly 30
  expected.
- **Equipment:** device + pen + ruler + draft paper; "no other equipment is needed" ⇒ **no
  calculator** ⇒ every number must be hand-computable.
- **Examinable topics, and only these three:**
  1. **graphical method**
  2. **simplex method**
  3. **sensitivity analysis for the simplex method**

Restated in-lecture in the Week 3 exercise class (`week-03-transcript`): *"in your quiz, I will
cover graphic method … simplex method … sensitivity analysis."* Same three.

**Explicitly out** (named as out by the lecturer, in the transcripts / STATUS): transportation,
the assignment / Hungarian method, all nonlinear programming, branch-and-bound (called
"the end of the LP", final-exam material), and the "dualise a 2-constraint LP to solve it
graphically" trick (a method aid the lecturer flagged, but **not** one of the three items).
Duality as a standalone topic is out; shadow prices / dual values **as read off the final
simplex tableau** are in, as part of "sensitivity analysis for the simplex method."

## 2. Historical evidence (authority: `historical-*`, `unofficial`)

**Small-sample warning:** there is **no exact-code EE-6204 Quiz 1 paper** in the local
materials, and **no official marking scheme** for any Quiz 1 question. All structural evidence
below is unofficial student recollection (小红书 + a WeChat group chat) plus the Week 3 worked
exercises. Fewer than three comparable papers exist — treat every "frequency" as a practice
priority, never as a prediction of marks or wording.

| Evidence | What it shows | Weight |
|---|---|---|
| `exercises-part1` (Week 3 worked class) | Graphical + simplex at quiz depth; a **degenerate optimal vertex** (all constraint lines concurrent) appears in Q1/Q2; minimum-ratio handling stressed | Style / difficulty anchor. Not a past paper. |
| 小红书 recollections (Feb 2026, Sep 2025 sittings) | Two eras: current run (Prof. Su Rong) = LP formulation + simplex on one LP; previous lecturer = transportation + constrained NLP. Current run "matrix transformed twice" (≈ 2 pivots) | Recurring structure: a **2-variable, 2-constraint, all-≤, maximisation LP solved in ~2 pivots** is the spine to drill. Unofficial. |
| WeChat `EE6204-26S1` group chat | Corroborates MCQ + LockDown + LT1 + the three-item scope; transportation "not tested" relayed from the lecturer | Confirms scope boundary. Unofficial paraphrase. |
| `week-02-transcript` | Lecturer perturbs a cost coefficient and an `A` entry, saying that is "how you operate … in a quiz or the final exam" | **Sensitivity is examinable**, not a guess. The perturbation style (change one number, keep the basis, read the new range) is the thing to practise. |

## 3. Coverage gaps in the existing practice material

`quizzes/quiz-1-mcq-practice.*` (18 items) already drills: corner enumeration, binding sets,
gradient direction, unbounded / multiple-optima recognition, standard form, entering / leaving /
ratio test, tableau reading, the optimality criterion, shadow prices off the z-row, RHS Δz, one
RHS range, complementary slackness, dual + strong-duality check.

Angles it does **not** cover, which this second mock adds for breadth:

- graphical **minimisation** with `≥` constraints;
- a **degenerate optimal vertex** from concurrent constraint lines (in the Week 3 exercises,
  absent from mock 1);
- a **redundant constraint** (present but never binding);
- **objective-coefficient range from the graph** (iso-profit slope between the two edge slopes)
  — and the check that it agrees with the tableau's `c1` range;
- identifying the **pivot element** (row ∧ column) rather than just the entering / leaving names;
- reading the **basic feasible solution from a mid-run tableau**;
- **unboundedness detected from a tableau** (entering column ≤ 0), not from a graph;
- **alternative optima detected from a final tableau** (zero reduced cost on a nonbasic variable);
- **shadow-price validity range** and the **extrapolation trap** (using a shadow price outside
  its RHS range);
- **pricing a new decision variable** (would a third product enter the basis?);
- **degeneracy ⇒ shadow prices / ranges need not be unique** (concept).

## 4. Evidence-weighted practice priorities (for this mock)

1. **Simplex mechanics on an all-≤ maximisation LP, ~2 pivots** — highest weight: it is the
   recurring current-run structure and the bulk of the marks in every recollection. → Part B
   (10 items), all on one spine LP.
2. **Sensitivity read from the final tableau** — lecturer-confirmed examinable; the perturbation
   style is specific and learnable. → Part C (8 items).
3. **Graphical method, including the special outcomes** (unbounded, alternative optima,
   degeneracy, redundancy, minimisation) — in scope, quick to test by MCQ, and the ruler
   requirement implies at least one to-scale graphical item. → Part A (9 items).

**Not a prediction.** This is a 27-item practice instrument. It does not claim any of these
questions, numbers, or the item count will match the real quiz. It claims only that a learner
who can do every item cold, in scope, is prepared for the three examinable topics.

## 5. What the mock deliberately excludes (to stay in scope)

Transportation, assignment, NLP, KKT, branch-and-bound, two-phase / Big-M artificial-variable
drills (kept to a single conceptual mention of what a `≥` row needs — no computation), the
dualise-to-graph trick, and any "write and solve the dual" item. Part C stays inside
"sensitivity analysis **for the simplex method**": everything is read from, or checked against,
the final tableau of the spine LP.
