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

---

# Addendum — WeChat class group intel (gathered 2026-09-02)

Source: the `EE6204-26S1` WeChat group chat (`59154079625@chatroom`, 984 messages,
window 2026-08-01 → 2026-09-02), exported locally with the `wechat-export` tool. This is
**current-cohort student discussion of the upcoming Quiz 1** for the run we are actually
sitting — more decisive than the 小红书 recollections above, but with the same trust rules:
it is students paraphrasing each other and two lecturer emails, not the emails themselves.

## Contamination warning — read first

This group's members also take **EE6407** and **EE6406**, and 6407 held its own quiz on the
night of **2026-09-01**. The chat interleaves both. Claims about *"昨晚的考试"* (last night's
exam), a **signature on submission**, rooms **LT19 / LT2A**, *"60 分钟没有电源"*, spaced
seating across several rooms, and a *"chessboard colouring"* question are **6407, not 6204**.
One member: *"一点进来以为这是 6407 的群."* Every item below is tagged with the course it
belongs to; anything unattributable is marked.

## The primary sources are two lecturer emails — nobody pasted them

Decisive facts (format, venue, passcode, LockDown requirement, timing) trace to **two emails
from Prof. Su Rong**, ~2026-08-29 and ~2026-09-02. **No student quoted either email
verbatim** in text — they paraphrase. The `wechat-export` tool is **text-only**: any
screenshot of an email or of the NTULearn announcement posted to the group is **not in this
export**, so the chat evidence is systematically incomplete on exactly the decisive artefact.
**Action: open those two emails and the NTULearn "Quiz 1" item directly.**

## Format — the current run has changed to MCQ (this contradicts the mock)

| Attribute | Current run (Su Rong, this cohort) — WeChat consensus | Trust |
|---|---|---|
| Question type | **Multiple choice.** 13 distinct members say MCQ / 选择题 / 单选; the ~08-29 email is cited as the source. Earlier the lecturer had said in class it would be *"either 2 long questions or 4 MCQ, decided by the Thursday before"* — the email resolved it to **MCQ**. | High |
| Single vs multi | Most read it as **single-answer** MCQ (*"MCQ 大多数情况都指单选"*, *"邮件里说了"*). A minority note "multiple-choice" only means several options, not necessarily one key. Not fully settled. | Medium |
| Long-answer / working | Consensus: **none** — pure MCQ. A few still hedge "单选 + 大题?". | Medium |
| Delivery | **On NTULearn, through Respondus LockDown Browser**, on your **own laptop/iPad**, **in person** in the lecture theatre. A **passcode is given on-site** at the start. | High |
| Venue | **LT1** (the normal lecture theatre — "他写教室了 … LT1"). Note LT1 ≠ LT1A; LT1 is on the level of the Li Wei Nan Library. | Medium-High |
| Attendance | Expected **in person**; likely a **paper sign-in**. Doing it from home is not sanctioned — LockDown Browser also does **webcam proctoring**. | Medium |
| Open/closed book | 小红书 said closed-book ("闭卷"). The WeChat group did **not** re-confirm this for the current run. Treat as **closed-book, unconfirmed**. | Low |
| Bring | Own device **+ charger** (few power outlets), **own scratch paper** ("草稿纸自备"). Pre-install LockDown Browser — see below. | Medium |

**LockDown Browser (Respondus).** Follow-up email ~2026-09-02 makes it **mandatory**.
- Download **before** the quiz via NTU's institution-specific URL; sign in with your **NTU
  email + password**. One link seen posted: `download.respondus.com/lockdown/download.php?id=946716216`
  (unverified that this is NTU's official link — prefer the URL in the email).
- **macOS:** works, reported laggy. **iPad:** works — the app is region-locked, not in the
  CN App Store, switch App Store region to find it. **Android: not supported.**
- Test-launch it once before Friday.

### Implication for the next 48h (not new intel — a consequence)

The existing `quiz-1-prediction.md` / `.html` is built as **handwritten free-response, 16
marks, multi-pivot simplex by hand, answer-on-paper**. The current-run evidence says **MCQ,
closed-book, likely no calculator, in person**. **The mock's shape no longer matches the
current run.** Still useful for *method* revision, but under MCQ the likely items are:
reading a given tableau (identify entering/leaving variable and why; ratio test), reading
**shadow prices / reduced costs off a final row**, recognising **unbounded / infeasible /
degenerate / multiple-optima** tableaux, standard-form conversion, graphical-method corner
identification, and sign-convention questions (`z − cᵀx = 0`, optimality when bottom row ≥ 0)
— *recognition* of a correct derivation, not long hand-computation.

## Scope boundary — well-corroborated by this group (lead with this)

From the Week-3/4 review lecture (卓轩: *"he spent nearly 2 hours reviewing the three topics
below"*) and the ~08-29 email:

| | Topic | Evidence |
|---|---|---|
| **IN** | Graphical method | 卓轩, ZX, AUDREY independently |
| **IN** | Simplex method | same; plus 小红书 |
| **IN** | Sensitivity analysis | 卓轩, AUDREY, ZX independently — **named as examinable** |
| in-scope by implication only | Duality | *"对偶讲完了"* (covered) but **no student names it as examinable**; do not promote it just because it sits next to sensitivity |
| **OUT** | Transportation problem (运输问题, deck 3, "special LP") | 卓轩 relays a direct lecturer statement: *"这个他说不考"* |
| **OUT** | Assignment problem (指派问题) | not mentioned as examinable; grouped with transportation |
| **OUT** | Nonlinear programming (deck 4) | not yet taught at quiz time; *"we haven't even learned that"* |
| **OUT** | The Week 4 lecture's own content | Black, 多瑜小师: *"不考"* |
| **Cutoff** | *"只考到 lecture 2 结束"* | 多瑜小师, confirmed by 欣尘宇宙 — consistent with all of the above |

**This upgrades Section S of the mock.** The prediction file labelled a
**sensitivity/duality** item as a *predicted unseen* extension. The class now reports
sensitivity analysis as **explicitly examinable** — the prediction was right; treat Section S
as **corroborated core**, not a guess.

## Weighting — three conflicting numbers, unresolved

| Figure | Source |
|---|---|
| **Quiz 1 = 20%**, Quiz 2 = 20%, final = 60% | Black, 2026-08-11 (most-repeated in the group) |
| Two quizzes = **32% total**, plus an **8% assignment** nobody has seen | Dérive, 2026-09-01 |
| ≈**16%** | Feb-2026 小红书 recollection (in the main file above) |

Do not adopt one. **Check the course outline / NTULearn grade breakdown.**

## Disputed / unattributable — do not rely on

- **Calculator.** 杰尼 (2026-08-28): *"要"* (bring one). Grylls (2026-09-02, same message
  says *"还是单选题"* → likely 6204): *"quiz 没让带计算器."* **Genuinely disputed.** Plan for
  **no calculator** (safer for a closed-book MCQ) but bring a basic one in case.
- **Duration.** 矢向 (2026-09-02): *"60 分钟没有电源"* — course **ambiguous** (could be the
  6407 exam), though 矢向 asks a 6204 scope question minutes later. The `week-02-transcript.txt`
  has Prof. Su Rong saying **"30-minute quiz"** — a direct lecturer statement, higher trust.
  **Conflict unresolved; the 30-min figure is not overturned by this chat.**
- **Lockdown / seating / sign-in specifics** cited from *"last night"* are **6407**.

## Logistics to verify (updated) — from the emails, not this file

1. **Read the two Prof. Su Rong emails** (~08-29 and ~09-02) and the NTULearn "Quiz 1" item —
   they are the primary source for everything above.
2. Exact **date / time / room** and whether it is in the Week 4 lecture slot.
3. **LockDown Browser** — correct NTU download URL; install and test-launch before the quiz.
4. **Passcode** mechanism — on-site only?
5. **Calculator** allowed? **Closed-book** confirmed for the current run?
6. **Weighting** — resolve the 16 / 20 / 32+8 conflict against the official breakdown.
7. Whether **single-answer** or **multi-answer** MCQ.

---

# Addendum — Week 3 exercise-class transcript (primary, in-lecture; added 2026-09-03)

Source: `resources/week-03-transcript.txt` — the full Week 3 lecture, which was an **exercise
class** run by Prof. Su Rong. Its handwritten worked solutions are
`resources/EE6204_Exercises-part1.pdf` (5 problems). Unlike the 小红书 and WeChat material
above, this is the **lecturer speaking in class**, not a student paraphrase — highest trust for
scope, with the usual caveat that it is an auto-generated transcript (garbles like "77x2" for
7x₂, "bronch in the bound" for branch and bound).

## Scope — stated directly by the lecturer, and it matches the cohort intel

> "in your quiz, I will cover graphic method. I will cover the simplex method, and I will cover
> the sensitivity analysis. ... If it's a written one, maybe up to two questions."

- **IN: graphical method, simplex method, sensitivity analysis.** Same three topics the WeChat
  group reported. Section S of the mock stays **corroborated core**, not a prediction.
- **OUT: assignment / Hungarian method — from BOTH Quiz 1 and the final exam.** Direct quote:
  *"it will not be tested in the quiz, and it will also not be tested in the final exam. For the
  Hungarian algorithm."* This is stronger than the earlier "grouped with transportation, not
  mentioned" — it is an explicit double exclusion.
- **OUT: transportation, NLP, Week-4 content** — unchanged.

## MCQ finding is NOT reopened by this transcript

The Week 3 lecturer is still **undecided**: *"I'm actually thinking whether I should use the so
called MCQ ... easy for me to mark."* Elsewhere he had framed it as *"either 2 long questions or
4 MCQ."* The WeChat intel says the **~2026-08-29 email resolved it to MCQ**. The Week 3 lecture
is at or before that email, so this transcript is a **pre-decision snapshot** — it is
consistent with "not yet decided", not evidence against MCQ. Do not treat it as reviving the
conflict.

## Duration conflict — now resolved to 30 minutes

Second in-lecture statement: *"I only give you 30 minutes, so it cannot be too complex."* With
the Week 2 *"30-minute quiz"* statement, that is **two independent lecturer statements** for 30
min versus one course-ambiguous WeChat *"60 分钟"* (probably the EE6407 exam). Treat **30 min**
as settled.

## Two techniques the lecturer flagged as possible quiz items

1. **Dualise to reduce the variable count for a graphical solution.** *"If I strongly request
   you to use a graphic way to solve this problem [and it] is more than two variables ... use
   the duality theory to transform this into the dual problem, [which] will have a fewer number
   of variables."* The dual has one variable per primal constraint, so a `>2`-variable /
   2-constraint LP dualises to something graphable. He may also **pose** a problem in dual/matrix
   form (`z = bᵀw`). Now in `beginner-notes.tex` §6 and `notes.tex` §3.1.
2. **Solve an integer LP graphically** (lattice + value line): *"find all the integer solutions
   ... you are still sliding down this guy until you touch the first integer value ... whenever
   you enumerate, I will give you zero marks because you have no idea [of the method]."* Now in
   `beginner-notes.tex` §7.1 and `notes.tex` §4.3. **Branch and bound** he mentions only in
   passing (*"the more commonly used method to solve integer programming ... the end of the
   LP"*) — it is **not** in the lecture deck; treat it as **final-exam** material (still added
   to the notes, labelled as such).

## Marking expectations (source-grounded pitfall)

The lecturer **counts your constraint lines** and wants to see the value line with its gradient
arrow and the first/last-contact vertex marked explicitly: *"I'm going to count how many lines
you have ... I want to see the gradient direction ... this is the value line, and then this
point, the first touched."* A correct final answer with no drawn construction loses marks;
enumeration instead of method scores zero.

## `EE6204_Exercises-part1.pdf` — the 5 worked problems (all re-derived here)

| # | Type | Problem | Answer (this file's derivation) |
|---|---|---|---|
| Q1 | Graphical | `max 5x₁+7x₂` s.t. `4x₁+5x₂≤20, 2x₁+6x₂≤24, 6x₁+4x₂≤16` | `(0,4)`, `f=28`. **Degenerate** — all three constraint lines pass through `(0,4)`. |
| Q2 | Simplex | same LP | `(0,4)`, `z=28`; optimal tableau is degenerate (`S₂=S₃=0`); ratio test is a **three-way tie** `20/5=24/6=16/4=4`. |
| Q3 | Branch & bound | `max 7x₁+5x₂` s.t. `4x₁+6x₂≤18, 2x₁+6x₂≤9, 6x₁+3x₂≤27`, integer | LP relaxation `(4.5,0)`, `z=31.5`; integer optimum **`(4,0)`, `z=28`**. `x₁≥5` infeasible; `x₁≤4` → `(4,1/6)`; then `x₂≤0` → `(4,0)`, `x₂≥1` → `(1.5,1)` `z=15.5` pruned. *(Source tree stops at an unlabelled node; completed here.)* |
| Q4 | Graphical | `max 200x+550y` s.t. `100x+250y≤5000, x+y≤50` | `(0,20)`, `z=11000`. *(Solution blank in source — derived here.)* |
| Q5 | Simplex | same as Q4 | `(0,20)`, `z=11000`. *(Blank in source.)* |

**Source erratum (Q1):** the gradient is annotated `∇f = [7; 5]`; for `f = 5x₁+7x₂` it is
`[5; 7]`. Does not change the optimum. Do not attribute the handwriting.

## Effect on the mock — deferred, but noted

The mock (`quiz-1-prediction.*`) is still handwritten free-response and still not rebuilt. If it
is reshaped for MCQ, **Q1/Q2 above is the best source-grounded item now available**: a tableau
with a three-way ratio-test tie and a degenerate optimal basis (`S₂=S₃=0`) — "identify the
entering/leaving variable and say why the BFS is degenerate". Add one graphical
integer-lattice recognition item too.
