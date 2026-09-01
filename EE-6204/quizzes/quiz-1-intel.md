# EE6204 Quiz 1 — past-paper intelligence

Gathered 2026-09-02 by searching 小红书 (RedNote) for `EE6204`, `6204 quiz1`, and
`EE6204 quiz1回顾` in a logged-in session (`type=51` notes search), plus a general web
search and the local `resources/public-archive-2026-08-24/`.

**Everything in this file is unofficial student recollection.** It is not an official paper
and not a marking scheme. Treat every recalled question and every "answer" as a study
hypothesis to re-derive, not as ground truth. **Verify all quiz logistics (date, time,
venue, weighting, open/closed book) on NTULearn.**

---

## Sources consulted

| Note title | Author | Posted | Likes | What it contains |
|---|---|---|---:|---|
| `以后选6204的同学有福了` (cover text: `我爱死Prof. Su Rong了 / 新老师开盲盒成功`) | 小心地滑 | 2026-02-06 (edited) | 25 | **Most decisive.** One post. Reconstruction of the **Feb 2026 sitting** — the first quiz set by the new Part-1 lecturer. Gives explicit weighting and topic split (see below). Comments confirm the answer format is **handwritten on paper**. |
| `EE6204quiz1` | aun | 2025-09-13 | 16 | The **AY25-26 S1 (Sep 2025) sitting**, set by the *previous* lecturer. Format, timing, and a description of both questions. Comments add detail (VAM, "container with a lid"). |
| `EE6204 quiz 01` | earthgull | 2025-02-20 | 18 | The **AY24-25 S2 (Feb 2025) sitting**, previous lecturer. Caption: two big questions — transportation, and NLP with mixed constraint types + positive-definiteness check. *(Its images are graphical-LP case diagrams watermarked 知乎 @王源 — third-party study material, not that quiz's questions.)* |
| `NTU EEE 6407＆6204 quiz1回顾` | 今天可以去哪玩 | 2025-09-19 | 38 | Format recap for the Sep 2025 sitting: Week 5, fill-in-blank + MCQ, ~10 sub-items, Q1 balanced transportation, Q2 NLP with Lagrange + Hessian. |
| `🇸🇬NTU EE6204 Quiz以及GPT答案` | 梵高先生不姓梵 | 2026-07-09 | 51 | **Quiz 2 content, not Quiz 1** — DTMC/CTMC Markov chains and queueing. Listed here only so it is not mistaken for Quiz 1 material. |
| Web search (`NTU EE6204 quiz`) | — | 2026-09 | — | Course-review sites: "two open-book quizzes, not particularly difficult." Consistent with an own-device online sitting; nothing question-specific. |

**Lecturer identification.** The current Part-1 lecturer is **Prof. Su Rong**. This comes from
the cover-image text of the 小心地滑 post above (*"I love Prof. Su Rong! New teacher, opened the
blind box successfully"*) together with `resources/week-01-transcript.txt`, where the lecturer
introduces himself (*"my name is So"*). Neither alone is proof; the pairing is.

---

## The scope boundary (Stage 2)

**Confirmed for the current run (Prof. Su Rong, this semester), from `resources/week-01-transcript.txt`
and `resources/week-02-transcript.txt`:**

- The quiz is **at the end of the Week 4 lecture**, in the last hour ("30-minute quiz, very simple
  one"). It moved to Week 4 with the new lecturer; it used to be Week 5.
- **Delivery:** the problem is posted as a **PDF on NTULearn**; the portal opens ~5 minutes before
  and closes 30 minutes later. You **handwrite your solution, photograph it, and upload it** to
  NTULearn (a further 10–15 minutes allowed for upload). Bring your own laptop or iPad; only
  network access is needed. *(This is a lecturer statement in a lecture transcript, phrased as
  "most likely" and "details will come later" — still flag it for NTULearn confirmation.)*
- **Examinable topics** are Prof. Su Rong's Part 1: **LP modelling / formulation, the graphical
  method, standard form, and the simplex method**, with only "a little bit" of nonlinear
  programming "mentioned in the fourth lecture."
- Week 2 additionally developed **duality** (heavily — the transcript mentions the dual dozens of
  times) and **sensitivity analysis**. In the Week 2 sensitivity worked example the lecturer says
  explicitly: *"everybody knows actually in a quiz or in the final exam, how do you operate"* while
  perturbing a cost coefficient (`c₁ → c₁ + θ`) and an `A`-matrix entry. **Sensitivity technique is
  flagged by this lecturer as quiz-relevant.**
- Weeks 3–4 transcripts are **not available locally**. Transportation/assignment depth for the
  current run is therefore unconfirmed; the Week 2 transcript contains **no** "transportation"
  mentions and only three "assignment" mentions as of that point in the course.

---

## Evidence classified

### Format — HIGH trust where the two most recent sources agree

| Attribute | Current run (Su Rong, Feb 2026 + this semester) | Previous lecturer (through Sep 2025) |
|---|---|---|
| Week | **4** | 5 |
| Duration | **30 min** written + 10–15 min upload | ~1 hour |
| Weighting | **≈16%** ("16分就一题" — the whole paper is ~16 marks on essentially one topic) | not stated |
| Answer mode | **Handwritten on paper, photographed, uploaded to NTULearn** (comment: "纸上手写") | MCQ + fill-in-the-blank, done in the browser |
| Questions | **2**: Q1 = LP formulation (≈30% of marks), Q2 = simplex method (≈70%) | **2** big questions, ~10 sub-items total |
| Q1 topic | Translate a word problem into an objective function + constraints | Balanced **transportation** problem (VAM initial solution, then optimality) |
| Q2 topic | Solve an LP by the **simplex method**; "matrix transformed twice" (≈2 pivots); can be checked with the graphical method | **Constrained NLP** with inequality constraints — Lagrange/KKT solution + Hessian positive-definiteness check |
| Difficulty | "very simple, relax"; "we're both happy"; felt like undergraduate optimization theory | "teacher is gentle"; Q1 easy if you know VAM |

**Read of the two eras.** Prof. Su Rong took over Part 1 and rebuilt the quiz around **LP
formulation + simplex only**, dropping the transportation and NLP questions that the previous
lecturer used. One RedNote commenter who sat Feb 2026: *"last year we were tested on nonlinear"* —
reply: *"we haven't even learned that yet."* The current run is taught by the same Prof. Su Rong,
so the **Feb 2026 shape is the best predictor**.

### Recalled question text — MEDIUM trust (re-derive; wording is approximate)

- **Current-run Q1 (LP formulation).** "Convert the problem statement into an objective function
  and constraints" — a standard product-mix / resource-allocation word problem. No numbers recalled.
- **Current-run Q2 (simplex).** Solve the LP from Q1 (or a given LP) by the simplex method; about
  two pivot iterations; "you can verify the answer with the graphical method." Prof. Su Rong's
  convention (from `week-02-transcript.txt`): write the objective row as `z − cᵀx = 0` (negative
  objective coefficients in the bottom row); **stop when every bottom-row entry is ≥ 0**; a
  maximization with all `≤` constraints needs **slack variables only** — no surplus, no artificial,
  no Big-M. He also says *"the most negative one is not really critical"* — any negative bottom-row
  entry may enter; only the minimum-ratio test is forced (it keeps the RHS column ≥ 0).
- **Previous-run Q1 (transportation).** Balanced transportation table; check/enforce balance
  (add a dummy row/column if `Σsupply ≠ Σdemand`); build an initial BFS with **Vogel's
  Approximation Method**; test optimality with `uᵢ + vⱼ = cᵢⱼ` potentials and `cᵢⱼ − uᵢ − vⱼ`
  reduced costs; if not optimal, one stepping-stone/MODI loop.
- **Previous-run Q2 (constrained NLP).** Minimize the material used to build a **container that
  holds a fixed volume** (a box or cylinder). One RedNote poster lost time by assuming an
  open-top container when the problem specified a **closed** one — read whether a lid is included.
  Method: Lagrangian with the volume equality constraint, solve the stationarity system, then a
  second-order (bordered-Hessian or Hessian definiteness) check to confirm a minimum. "Mixed
  constraint types" and "inequality constraints" were mentioned — i.e. a KKT treatment.

### Answer keys — LOW trust — NONE are reproduced here

No RedNote post gave a worked numeric answer for a Quiz 1 question. The one post with a full
answer key (`NTU EE6204 Quiz以及GPT答案`) is **Quiz 2** (Markov chains) and its answers are
GPT-generated by the poster's own admission. Every answer in `quiz-1-prediction.md` was derived
here from scratch and validity-checked.

---

## What this produces (Stage 3)

`quiz-1-prediction.md` / `.html` — a mock built to the **current-run (Su Rong) shape**:

- **Q1 formulation + Q2 simplex on one LP**, 16 marks, 30-minute timer, "answer on paper" mode —
  mirrors Feb 2026 exactly.
- **Predicted unseen item:** a **sensitivity / duality** extension on the *same* LP (shadow prices
  read off the final tableau, one-more-unit interpretation, RHS ranging via `B⁻¹(b + Δb) ≥ 0`,
  cost-coefficient ranging with `θ`). This is the in-scope topic the lecturer flagged as
  quiz-relevant but that is absent from the circulating recollection — labelled as a prediction.
- **Legacy block:** transportation (VAM + one MODI step) and a constrained-NLP box problem,
  labelled "previous lecturer's format through Sep 2025 — retained in case the coordinator
  reverts." Lower probability for the current run.

## Logistics to verify on NTULearn (do not take from this file)

- Exact date, time, and whether it is in the Week 4 lecture slot.
- Weighting (RedNote says ≈16%; the course historically has two quizzes).
- Whether it is genuinely open-book / own-notes (own-device suggests yes, but unconfirmed).
- Whether a calculator or formula sheet is allowed.
