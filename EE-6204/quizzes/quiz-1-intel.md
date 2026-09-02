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
| Question type | **Multiple choice.** 13 distinct members say MCQ / 选择题 / 单选; the ~08-29 email is cited as the source. **Now independently confirmed by the Week 3 lecture transcript** (`resources/week-03-transcript.txt`, see the second addendum below): the lecturer said the quiz would be *either* "two written questions" *or* "MCQ" and that he would decide by "next Thursday" — the ~08-29 email resolved it to **MCQ**. | High |
| Single vs multi | Most read it as **single-answer** MCQ (*"MCQ 大多数情况都指单选"*, *"邮件里说了"*). A minority note "multiple-choice" only means several options, not necessarily one key. Not fully settled. | Medium |
| Long-answer / working | Consensus: **none** — pure MCQ. A few still hedge "单选 + 大题?". Chat also paraphrases the in-class framing as *"要么两道大题 要么四道选择"* — the alternative was **~4 MCQ**, not a long paper, so expect a **short** MCQ set. | Medium |
| Delivery | **On NTULearn, through Respondus LockDown Browser**, on your **own laptop/iPad**, **in person** in the lecture theatre. A **passcode is given on-site** at the start. | High |
| Venue | **LT1** = **Lecture Theatre 1, Nanyang Executive Centre** (building **"Von Lee Yong Miang"**), **2nd floor, above McDonald's**, same level as **Lee Wee Nam Library**. Heavily corroborated across 2026-08-11→08-22. **Not** LT1A (ground floor, opposite McDonald's) and **not** LKC-LT (Lee Kong Chian Lecture Theatre, by Canteen B) — both were named as wrong guesses in the chat. | High |
| Attendance | **In person**, lecture first then quiz at the end of the session (先上课再考试 — many confirmations; one *"先考试再上课"* dissent overruled). Likely a **paper sign-in**. Doing it from home is not sanctioned — LockDown Browser also does **webcam proctoring**. | Medium-High |
| Open/closed book | **Closed-book, no formula sheet.** 杰尼 (2026-08-26): *"是闭卷"* — a 6204-specific student report, but on a **last-semester (pre-format-change)** basis. Reinforced by the lecturer in the Week 3 transcript: *"we will not give you the table. You have to memorize. It's not going to be in the … appendix"* (re the simplex tableau / sensitivity formulas). Still worth a glance at the email for the MCQ run. | Medium |
| Bring | Own device **+ charger** (few power outlets — seats with sockets are on the edges and fill up fast), **own scratch paper** ("草稿纸自备"). Pre-install LockDown Browser — see below. | Medium |

**LockDown Browser (Respondus).** Follow-up email ~2026-09-02 makes it **mandatory**.
- Download **before** the quiz via NTU's institution-specific URL; sign in with your **NTU
  email + password**. One link seen posted: `download.respondus.com/lockdown/download.php?id=946716216`
  (unverified that this is NTU's official link — prefer the URL in the email).
- **macOS:** works, reported laggy. **iPad:** works — the app is region-locked, not in the
  CN App Store, switch App Store region to find it. **Android: not supported.**
- Test-launch it once before Friday.

### Implication for the next 48h (not new intel — a consequence)

The existing `quiz-1-prediction.md` / `.html` is built as **handwritten free-response, 16
marks, multi-pivot simplex by hand, answer-on-paper**. The current-run evidence — now **two
independent confirmations**, the ~08-29 email (via chat) *and* the Week 3 lecture transcript —
says **MCQ, closed-book, ~30 min, in person**. **The mock's shape no longer matches the
current run.** Still useful for *method* revision, but under MCQ the likely items are:

- reading a given tableau — identify the **entering / leaving variable** and *why* (most-negative
  row-0 entry; min-ratio test), spot **degeneracy** (a tie in the ratio test);
- reading **shadow prices / reduced costs off the final row**, and the **RHS / cost ranges** over
  which the current basis stays optimal (sensitivity — the lecturer worked this at length);
- recognising **unbounded / infeasible (empty region) / degenerate / multiple-optima** tableaux;
- **standard-form conversion** (slack variables only for all-≤ max; `z − cᵀx = 0` row; optimal
  when the bottom row ≥ 0);
- **graphical method**: identify the correct constraint-line / gradient / iso-value-line setup and
  the optimal **corner**; and two lecturer-flagged twists —
  (a) a primal with **>2 variables** that must be **dualised to 2** to be graphable
  (*"the question asks you to use a graphic way … just find a way to transform the problem"*), and
  (b) an **integer** optimum (*"the number of products … has to be integer"*) = the last lattice
  point the objective line meets inside the feasible region.

*Recognition* of a correct derivation, not long hand-computation. See the second addendum for the
lecturer's own words on each of these.

## Scope boundary — well-corroborated by this group (lead with this)

From the Week-3/4 review lecture (卓轩: *"he spent nearly 2 hours reviewing the three topics
below"*) and the ~08-29 email:

| | Topic | Evidence |
|---|---|---|
| **IN** | Graphical method | 卓轩, ZX, AUDREY independently |
| **IN** | Simplex method | same; plus 小红书 |
| **IN** | Sensitivity analysis | 卓轩, AUDREY, ZX independently — **named as examinable**; lecturer worked b-ranging and c-ranging at length in Week 3 |
| **IN** (as an instrument inside the graphical item) | Duality | **Upgraded.** Not just "covered" — the Week 3 transcript has the lecturer saying he *may* pose a graphical question whose primal has too many variables to graph, so you **dualise to two variables and solve the dual graphically** (*"I may use the duality things to write … then you can use a graphic way to solve it"*). Know weak/strong duality and complementary slackness well enough to convert and to read one problem's solution off the other. |
| **OUT** | Transportation problem (运输问题, deck 3, "special LP") | 卓轩 relays a direct lecturer statement: *"这个他说不考"*. Week 3 transcript covers it only as an in-class exercise. |
| **OUT** | Assignment problem / Hungarian algorithm (指派问题) | **Now a direct lecturer statement** (Week 3 transcript): *"it will not be tested in the quiz, and it will also not be tested in the final exam … only for fun."* |
| **OUT** | Nonlinear programming (deck 4) | Week 3 transcript: *"non-linear programming will be tested in the **final exam**"* — i.e. **not the quiz**. Week 4 teaches golden-section/Fibonacci search + a KKT intro, *then* the quiz; that Week 4 content is not on Quiz 1. |
| **OUT** | The Week 4 lecture's own content | Black, 多瑜小师, Ella: *"不考"* / Week 3 transcript ("… then we start to do the quiz") |
| **Cutoff** | *"只考到 lecture 2 结束"* | 多瑜小师, confirmed by 欣尘宇宙 — consistent with all of the above |

**This upgrades Section S of the mock.** The prediction file labelled a
**sensitivity/duality** item as a *predicted unseen* extension. The class now reports
sensitivity analysis as **explicitly examinable** — the prediction was right; treat Section S
as **corroborated core**, not a guess.

## Weighting — likely 20%, still verify

| Figure | Source |
|---|---|
| **Quiz 1 = 20%**, Quiz 2 = 20%, final = 60% | 6204-specific support: 南笺 and an unnamed member, **2026-09-01** (*"区区百分之二十"* / *"好像说20"*). *(An identical "期末60 / quiz1 20 / quiz2 20" line from Black on 08-11 is **not** evidence — it is in a 6488 double-slit-interference thread; Black self-corrects later, "我以为488". Do not cite it.)* |
| Two quizzes = **32% total**, plus an **8% assignment** nobody has seen | Dérive, 2026-09-01 — in a **6204/6407-mixed** thread, so the course is unclear. The Week 3 transcript has the lecturer say the extra exercises are *"optional … it's not assignment"* (×2), which suggests **6204 has no assignment component** — so this figure is likely not 6204's. |
| ≈**16%** | Feb-2026 小红书 recollection (in the main file above) |

Do not adopt one. **Check the course outline / NTULearn grade breakdown.** Best current guess:
**20%**, no assignment.

## Resolved by the Week 3 transcript

- **Duration = ~30 minutes.** Now a **direct lecturer statement in three separate lectures**
  (weeks 1, 2 and 3 — Week 3: *"I only give you 30 minutes, so it cannot be too complex"*). The
  chat's *"60 分钟没有电源"* (矢向, 2026-09-02) is **6407** — its quiz ran 60 min, 21:30–22:30, on
  the night of 09-01. **No longer an open conflict.** (The MCQ run's length is not separately
  stated; assume ~30 min.)
- **Date / sequence.** The Week 3 lecture was **Fri 2026-08-28** ("see you next week"; "half an
  hour [on the] social algorithm and one half an hour on the KKT … then we start to do the quiz").
  So **Quiz 1 is at the end of the Week 4 session — Friday 2026-09-04** — lecture (~1.5 h) first,
  then the quiz. Still worth a NTULearn check for the exact clock time and room.

## Disputed / unattributable — do not rely on

- **Calculator.** 杰尼 (2026-08-28, *before* the MCQ email): *"要"* (bring one). Grylls
  (2026-09-02, MCQ context): *"quiz 没让带计算器."* The Week 3 transcript does not mention a
  calculator. **Still disputed** — plan for **no calculator** (an MCQ that "cannot be too complex"
  should not need one) but bring a basic one in case.
- **Lockdown / seating / sign-in specifics** cited from *"last night"* are **6407**.

## Logistics to verify (updated) — from the emails, not this file

1. **Read the two Prof. Su Rong emails** (~08-29 and ~09-02) and the NTULearn "Quiz 1" item —
   they are the primary source for format, venue, passcode and timing.
2. Exact **clock time and room** for the Friday 2026-09-04 session (the date itself is settled).
3. **LockDown Browser** — correct NTU download URL; install and test-launch before Friday.
4. **Passcode** mechanism — on-site only?
5. **Calculator** allowed?
6. **Weighting** — confirm 20% (and that there is no assignment) against the official breakdown.
7. Whether **single-answer** or **multi-answer** MCQ.

---

# Second addendum — Week 3 review-lecture transcript (gathered 2026-09-02)

Source: `resources/week-03-transcript.txt` — an auto-transcription of the **Week 3 lecture,
Friday 2026-08-28** (the ~2-hour review session the chat's 卓轩 was describing on 08-28). This
is **Prof. Su Rong speaking directly**, so where it and the student paraphrase disagree, this
wins. The transcription is rough in places (`scientific analysis` = *sensitivity analysis*,
`nada / nina / num media` = *nonlinear*, `synplex` = *simplex*, `S matrix` and `y vector` are
real terms he uses); quotes below are lightly de-garbled and marked with `≈`.

This transcript was added to `resources/` after the WeChat addendum was written and had **not**
been cross-referenced. It confirms several things the addendum only had second-hand and adds
items the chat never mentioned.

## Format — in the lecturer's own words

> ≈ "It's the option there: either you use a pen to write and take a photo upload, or I will
> directly give you MCQ. If MCQ, you complete online — you still need paper, but you don't take
> a photo and upload any more. I will let you know **by next Thursday**."

That is the source of the chat's *"两道大题 or 四道选择, told by Thursday"* paraphrase. The
~08-29 email then resolved it to **MCQ**. So the current run is MCQ with **two independent
confirmations** (this transcript + the email via chat), not chat-only.

## Topic coverage — breadth depends on the format (and the format is MCQ)

> ≈ "In your quiz I will cover graphic method, simplex method, and sensitivity analysis.
> If it's a **written** one — maybe up to **two** questions [no time for three]. But if **MCQ**,
> I probably will cover **all** [three] topics."

Read this as **breadth, not extra scope**: under MCQ, expect **at least one item on each of
graphical method, simplex, and sensitivity analysis**. Under the (rejected) written option you
would have seen only two of the three. Either way the topic list is the same three.

He also warns the items are not purely mechanical: ≈ "more challenging … some **tricks** will
be in. But as long as you fully understand every example in your slides and watch today's
recording, it should be okay." → **work the worked slide examples** in
`resources/public-archive-2026-08-24/worked-slide-examples/Part 1 …`.

## Duration and materials

- ≈ "I only give you **30 minutes**, so it cannot be too complex." (Third lecture in a row he
  says 30 min. The chat's "60 min" is 6407.)
- ≈ "In the exam we will **not give you the table**. You have to **memorize**. It's not going to
  be in the … **appendix**." → the simplex tableau construction and the sensitivity-analysis
  relations are **not** provided. `resources/public-archive-2026-08-24/topic-explainers/EE6204_appendix.pdf`
  will not contain them. Closed-book.

## Graphical method — what he actually drilled

1. **Rubric for a drawn answer** (still useful for "which of these setups is correct" MCQs):
   ≈ "I want to see all the boundary lines — I will count how many constraints you have and how
   many lines you have — the **gradient direction**, the **value [iso-objective] line**, and the
   **first point the value line touches that is still inside the feasible region**." Then state
   `x*` and `Z*`.
2. **Dualise-to-graph trick (new — not in the chat).** ≈ "In a quiz I may not write it in this
   [primal] manner — I may use the **duality** things to write, so you can have more variables.
   If you use duality, transform into another form, then you can use a **graphic** way to solve
   it… The question asks you to use a graphic way, so it **must** be doable that way — just find
   a way to transform the problem." → a graphical item may hand you a primal with **3+
   variables**; its **dual has 2**, so dualise, solve the 2-variable dual graphically, and
   recover the primal answer via **complementary slackness**. **This is why duality is
   examinable.**
3. **Integer optimum (new).** ≈ "If I ask you to find **all the integer solutions** — slide the
   value line down until it touches the **first integer point** still inside the region." ≈ "I
   may ask you to find the **number of products** to produce — that has to be an integer." → be
   ready to give the last **lattice point** the objective line meets in the feasible region, not
   just the LP optimum.

## Simplex — the MCQ-shaped skills

- **Read the basis off a tableau:** a column that is all zeros except a single `1` is a pivot
  column; its variable is **basic** and takes the value in that row's RHS. ≈ "If you can see the
  basic variable straight from the matrix, I'm fine — you don't have to write the list."
- **Entering variable:** ≈ "by convention the **most negative** row-0 entry; but if someone
  picks a **less** negative one I can't call it wrong." Any negative row-0 entry may enter.
- **Leaving variable:** **minimum ratio test** (RHS ÷ positive entry in the pivot column) — it
  keeps the RHS column ≥ 0. ≈ A **tie** in the ratio test (his example: all ratios = 4) ⇒
  **degeneracy** — pick either.
- **Alternative optima:** at optimality a **zero row-0 entry for a non-basic variable** ⇒ another
  optimal vertex one pivot away.
- **Infeasible:** ≈ "the feasible region is empty ⇒ no solution."
- Consistent with the main file: all-≤ maximisation needs **slack variables only** — no surplus,
  no artificial, no Big-M. (He drops a dual example precisely because it would drag in artificial
  variables and the two-phase / Big-M machinery.)

## Sensitivity analysis — exactly the operations he worked (so the mock's Section S is right)

From the **final** tableau he identifies the **S matrix** (the block under the slack columns =
`B⁻¹`) and the **y vector** (row-0 slack entries = **shadow prices**). Then:

- **RHS ranging.** Perturb one `bᵢ → bᵢ + δ`. Find the δ range for which the last column,
  `S·(b + Δb)`, stays **≥ 0** — then the current basis is still optimal and `x*` shifts
  predictably; outside it you must pivot once more.
- **Cost ranging.** Perturb `c` (his example perturbs **both** coefficients: `5 + δ`, `7 + δ`).
  Find the δ range keeping **row 0 ≥ 0**; his worked answer is `δ ≤ 21`.
- **Past the range.** At `δ = 22` the tableau is no longer optimal — do **one more** elementary
  row operation. Sometimes ("good luck") the basis and optimal value are unchanged; sometimes a
  variable must leave the basis.
- His verdict: ≈ "sensitivity analysis is very powerful but quite **tedious** — a lot of
  analysis." Good MCQ territory: give a final tableau, ask for a shadow price, a reduced cost,
  or the width of a range.

## Not on the quiz — direct lecturer statements

- **Assignment problem / Hungarian algorithm:** ≈ "it will **not** be tested in the quiz, and it
  will **also not** be tested in the **final** exam … only for fun."
- **Transportation:** covered as an in-class exercise only; the chat's 卓轩 relays ≈ "这个他说不考".
- **Nonlinear programming:** ≈ "will be tested in the **final exam**" — not the quiz. Week 4
  teaches golden-section / Fibonacci search and a KKT introduction, ≈ "then we start to do the
  quiz"; that Week 4 material is **not** on Quiz 1. (For the final: ≈ "I don't need you to solve
  the KKT, but at least know how to use it — some qualitative questions may be asked.")

## Bearing on the weighting question

≈ "I will try to give more exercise, but it's just **optional** — **it's not an assignment**"
(said twice). Suggests **6204 has no assignment component**, so the chat's "8% assignment" is
probably another course. Best guess for the breakdown: **Quiz 1 20% + Quiz 2 20% + final 60%**,
no assignment — still confirm on NTULearn.

## Not folded into the notes

The Week 3 sensitivity worked example (S-matrix / y-vector identification, b- and c-ranging,
the one-more-pivot case) is teaching material that belongs in `notes/beginner-notes.tex` §6 and
`notes/notes.tex` §2.3. It was **not** added in this pass (intel-only, matching the prior
WeChat pass). Fold it in on the next `/update` that recompiles the notes.
