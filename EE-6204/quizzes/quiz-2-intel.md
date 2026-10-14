# EE6204 Quiz 2 — intelligence file

Gathered 2026-10-14. Two layers: the **official** announcement (authoritative), then **unofficial /
historical** evidence used only to choose practice angles.

## ★ OFFICIAL (NTULearn announcements, read 2026-10-14)

Source: EE6204 NTULearn course announcements — "Quiz 2" (posted 2026-10-12 15:05) and
"*Important for Quiz*: Update the Respondus LockDown Browser" (2026-10-12 15:07), both by
Assoc Prof Patricia Wong; and "Welcome" (2026-08-03). Paraphrased.

| Item | Official statement |
|---|---|
| Topics | **Random Processes and Queuing Models** (Part 2, weeks 5–9) |
| Date / time | **Friday 23 October 2026, 6:30 pm – 7:20 pm (50 min)** |
| Venue | **LT1**, alternate seats per the seating plan, fill rows from the edge |
| Format | **Closed-book, computerized** quiz on NTULearn in **Respondus LockDown Browser** |
| Questions | **4 questions, do all** |
| Marking | **Only keyed-in answers are marked**; the system string-compares with the key. A different format is marked wrong. **No backend intervention.** |
| Answer format | Follow each question's instruction exactly — e.g. **number of decimal places (standard round-up/down)**, **fraction `a/b` in simplest form** |
| Working paper | Provided, **not marked**. Write name + matric no. on it and hand it in |
| Exam appendix | **Provided** (the Part 2 "Exam appendix" item = `resources/part-2/exam-appendix.pdf`). Do not write on it; return it |
| Calculator | **Bring your own** |
| Device | Own **notebook** with LockDown Browser — **not an iPad**. No power points: charge 100 %, disable sleep, update the OS first |
| LockDown Browser | **Update required** (CITS: mandatory for all users from 5 Oct 2026). Test with the NTULearn **"Mock quiz"** (Assignments, Quizzes folder; 20 min, proctored) |
| ID | Physical passport or a photocopy of it |
| Phone / watch | Airplane mode, in the bag. Phone use = potential cheating |
| Rules | Stay seated to the end; late-comer cut-off 10 min after start; everyone submits at the end |
| Absence | Soft-copy MC/LOA to the TA (cc Dr Patricia) by 23 Oct |
| Lecturer tip | Copy every keyed-in answer onto your working paper as a backup against a computer failure |
| Weighting ("Welcome") | **Quiz 1 16 %, Quiz 2 16 %, Assignment 8 %, Exam 60 %** |

### Consequences for preparation

- What is tested is the **number in the right format**. Keep full precision in the calculator and
  round once, at the end. Reduce fractions fully (`28/95`, not `56/190`).
- 4 questions / 50 min ≈ 12 min per question → each question is probably multi-part with
  several input boxes (inference, not stated).
- The appendix carries the queue formulas, so effort belongs in *modelling* (state space, TPM,
  generator, rate balance) and in calculation speed — not in memorising queue closed forms.

## Lecturer statements in the Week 4–8 transcripts (raw machine transcripts, read 2026-10-14)

Source: `resources/transcripts-raw/week-0{5,6,7,8}-transcript.txt` (Dr Patricia Wong; automatic transcription, wording approximate). Week 4 is Part 1 (Prof. Su Rong: NLP/KKT, plus "Newton method, we can ignore", final exam "very conceptual") — not Quiz 2.

| Week | What she said / did | Use |
|---|---|---|
| 5 | Announced Quiz 2: Friday, 6:30 pm, NTULearn, **"will cover the first five weeks… of my class… random processes and queuing theory"**. Taught probability preliminaries selectively (sets, conditional probability, independence, random variables, expectation; **jumped p78 → p98 to the Poisson distribution, "used in our topic later on"**), then lecture-01 to p17 (geometric, exponential, memoryless, process classification with the stock-price examples, Poisson process). | Scope = Part 2 weeks 5–9; Poisson r.v. examinable |
| 6 | Followed `random-process-additional-notes-p1-19.pdf` (her summary); DTMC: Markov property, TPM rows sum to 1, n-step, state probabilities, Eg 6.1 cases, introduced steady state. | — |
| 7 | DTMC steady state finished; CTMC: homogeneity, exponential sojourn, generator, Kolmogorov; **"rate balance — don't remember the formula… outflow from state j = inflow into state j"**; Eg 9.1 resume and discard policies, solving `πQ = 0` set as practice. Stopped at p67. | Rate balance from the diagram is the expected method |
| 8 | Birth–death; queues: notation, Little, M/M/1 — **"no need to memorize, it's in the exam appendix… we will have it in exam and also in quiz"**; **"what we need to know is… recognize that it is an M/M/1… ρ ≥ 1 → unstable"**; derived the **M/M/1 waiting-time distributions** `F_d`, `F_w` (not on the appendix). Re-announced: quiz 23 Oct, "about 45 or 50 minutes", LT, update LockDown Browser. | Appendix confirmed for the quiz; waiting-time cdfs are a gap the appendix does not fill |
| 9 | **Not yet held (expected ~16 Oct):** "next week we'll do this queuing model, and then we'll do some questions" — M/M/1/N, M/M/m, Mᵇ/M/1 still to be taught. | **Re-sync the Week 9 transcript before the quiz**; any worked "questions" are the best style evidence available |

## What the exam appendix gives (and what it does not)

`resources/part-2/exam-appendix.pdf`, 2 pages, image-only. **Given:** for **M/M/1**, **M/M/1/N**,
**M/M/m** and **Mᵇ/M/1** — ρ, π₀, πₖ, L, Q, W, D. **Not given (must know):** geometric /
exponential / Poisson pmfs, cdfs and means; the memoryless property; superposition /
decomposition; DTMC TPM rules, `P(n) = Pⁿ`, `π(n) = π(0)Pⁿ`, `Y = YP`, mean sojourn
`1/(1−pᵢᵢ)`; CTMC generator rules (rows sum to 0), sojourn `EXP(−qᵢᵢ)`, `πQ = 0`, rate balance;
birth–death product formula; Little's law `L = λW`, `Q = λD`; utilisation `U = 1 − π₀`;
production rate `(1 − π₀)µ` or `pπ₁`.

Note the appendix's M/M/1/N `W` and `D` equal `L/λ` and `Q/λ` with the **nominal** λ (as in
lecture Eg 4.1: `W = 1.566/8`), not the effective (accepted) rate. Follow the appendix if a
question asks for W of an M/M/1/N queue; mention the effective-rate version only if asked.

---

# Unofficial / historical background (method practice only)

## RedNote recollections (gathered 2026-10-14 in a parallel logged-in Safari session)
Updated 2026-10-14. Read in logged-in Safari on Xiaohongshu/RedNote, searching `EE6204 Quiz2`, `EE6204 quiz 2`, and `6204 quiz2`. These searches returned the same core reports; this is a targeted search, not an exhaustive archive.

**Status: unofficial.** Student recollections and an explicitly GPT-generated reconstruction are preparation evidence, not an official paper, marking scheme, or confirmation of this semester's scope. (When this section was written in a parallel session the official announcement had not yet been read; the ★ OFFICIAL section above now supersedes any logistics below.)

## Sources and deduplication

| ID | Source | Date visible | Evidence inspected / value |
|---|---|---|---|
| S1 | [EE6204 quiz2 — aun](https://www.rednote.com/discovery/item/68fb6d0b0000000004010ac6) | 2025-10-24 | Entire caption and its one comment. Detailed four-page recollection; strongest question-topic evidence found. |
| S2 | [EE6204quiz2 — momo](https://www.rednote.com/discovery/item/68fb3fd300000000050107b6) | 2025-10-24 | Caption and two comments. Difficulty/formula-recall reaction only; no questions or exam rules. One commenter is S1's author, so this is not independent topic corroboration. |
| S3 | [🇸🇬NTU EE6204 Quiz以及GPT答案 — 梵高先生不姓梵](https://www.rednote.com/discovery/item/695a36fe000000002202dc8b) | “Edited at Jul 9”; search displays 07-09, no year | Caption and all nine images. Poster describes an approximately 95% similar reconstruction and explicitly says questions/solutions come from GPT. The claimed similarity is unverified; original sitting date unknown. |

S3 was already identified as Quiz 2 material in [quiz-1-intel.md](quiz-1-intel.md), “Sources consulted” and “Answer keys.” This file expands that existing lead once; it is not counted as a newly discovered or independent past paper. The earlier log dates it 2026-07-09; the live UI only showed the month/day edit label, which cannot date the exam. English and Chinese image sections are duplicate presentations of the same reconstruction, with different numbering: **17 versus 27 is not evidence of two papers or an actual exam question count.**

## What the October 2025 recollection reports

S1 describes four pages:

1. **Concepts:** distributions of DTMC and CTMC sojourn times; two scenarios classifying time and state space separately as discrete or continuous.
2. **DTMC:** construct the transition probability matrix (TPM) and calculate stationary probabilities from a supplied transition diagram.
3. **Queues:** calculate and compare M/M/1 and M/M/2 performance quantities. The author says the task resembles queueing slide Example 5.1 with numerical inputs. This example reference has not been matched to our local slides.
4. **CTMC:** construct the transition rate matrix and calculate stationary probabilities from a supplied transition diagram.

The author's comment advises bringing a calculator. **Historical student advice only; permission for the upcoming quiz is unknown.** The author found it manageable, while S2 found the formulas/questions difficult. Neither opinion establishes objective difficulty.

## Additional question patterns visible in the reconstruction

S3 images 1–4 give an English reconstruction; images 4–9 repeat/expand it in Chinese. Besides S1's topic clusters, they include DTMC mean sojourn times, identifying the state with greatest stationary probability, hourly queueing cost, and choosing a queueing design separately by total time, queue-only time, and cost. These extra subtopics are supported by **the reconstruction only**.

The displayed question styles mix selecting options and entering matrices/numerical values, including simplest fractions and six-decimal probabilities. This describes S3's study artifact, not a verified historical or current exam interface. The images inspected are formatted reconstructions/solutions; no authenticated original quiz paper was established.

## Independently checked examples from S3

The following arithmetic was re-derived and checked with exact rational calculations, including stationarity, row sums, normalization, and queueing identities. This verifies the displayed examples mathematically under the assumptions below; it does not authenticate their origin.

### DTMC — images 1 and 5

For states ordered 0, 1, 2 and rows representing the starting state:

```text
P = [0    1    0  ]
    [0.3  0    0.7]
    [0.5  0.4  0.1]

y = (31/111, 45/111, 35/111)
  ≈ (0.279279, 0.405405, 0.315315)
```

Every row of P sums to 1, yP = y, and the entries of y sum to 1. State 1 has the largest stationary fraction of time. This finite chain is irreducible and aperiodic (state 2 has a self-loop), so the stationary vector is also the limiting distribution.

For a sojourn counted as the number of time steps up to the first departure, including the departure step, the means are `1/(1-p_ii)`: **1, 1, 10/9 steps**. This uses the geometric distribution on 1, 2, …; counting only self-loops gives a different mean. An absorbing state would not have a finite departure time.

### CTMC — images 2, 8 and 9

```text
G = [-4   4   0]
    [ 2  -5   3]
    [ 0   1  -1]

pi = (1/9, 2/9, 2/3)
```

G is the generator (called Q in the post); rows sum to 0 and pi G = 0. Off-diagonal entries are rates, not probabilities. Holding times are exponential with exit rate `-g_ii` for these nonabsorbing states. Keep generator Q distinct from the queue-length Q below.

### Queue comparison — images 3, 7 and 8

Assume a stable, infinite-capacity queue with Poisson arrivals, independent exponential service times, and identical servers within each system. Arrival rate is 2 parts/hour in both systems. M/M/1 service rate is 6 parts/hour; M/M/2 service rate is **3 parts/hour per server**.

The post's notation is `L` = mean number in system, `Q` = mean number waiting, `W` = mean total time in system, `D` = mean queue-only delay. Many textbooks instead use Lq and Wq for Q and D.

| Model | L | Q | W (hours) | D (hours) |
|---|---:|---:|---:|---:|
| M/M/1 | 1/2 | 1/6 | 1/4 | 1/12 |
| M/M/2 | 3/4 | 1/12 | 3/8 | 1/24 |

Checks: `L = lambda W`, `Q = lambda D`, and `W = D + 1/mu` using the per-server mu. M/M/1 has shorter total time; M/M/2 has shorter queue-only delay. Equal aggregate capacity does not make the two systems equivalent: service itself takes longer at each slower server.

The displayed inventory rates are $5 and $4 per part per hour; maintenance is $200 and $150 per 100 hours, respectively. Under the post's interpretation—inventory cost applies to L and maintenance is the **whole system's** cost—both cost $4.50/hour. If maintenance is per machine or inventory applies only to waiting parts, re-read the problem and recalculate; those interpretations were not authenticated against an original paper.

## Preparation priorities and traps

Use this as a provisional practice list, then check it against the current lecturer's slides and announcement:

- Classify the time index and state space independently; continuous time does not imply continuous state.
- Distinguish geometric DTMC holding times from exponential CTMC holding times and from Poisson event counts.
- Read directed diagrams into P or a generator, check their row sums, then solve stationary balance with normalization.
- Practise M/M/1 and M/M/2 with units, per-server service rates, stability, and both Little's-law identities.
- Compare models by the quantity actually requested; optionally drill cost and mean sojourn questions from S3.

**Classification caveat (S3 image 2/6):** hourly supermarket customer counts use discrete time and discrete state. A thermometer displaying one decimal place has discrete *reported readings*, while underlying physical temperature is ordinarily modeled continuously. Continuous observation over an interval versus sampling times also matters. S3's temperature answer assumes the reported reading is the process state and observation is continuous; do not memorize the option without defining X(t).

## Reconciliation with the official announcement and local slides (2026-10-14)

- **Resolved by the official announcement:** date/time/venue, 50 min, **4 questions**, closed book, **calculator allowed** (so S1's "bring a calculator" advice holds this year), appendix provided, LockDown Browser, 16 % weighting. Answers are typed in a stated number of decimal places or as simplest fractions; S3 shows six-decimal probabilities; that format is unverified for the real paper, so follow each box's instruction (the mock uses 6 d.p. in four boxes to practise it).
- **S1's "Example 5.1" is matched:** `resources/part-2/lecture-02-queuing-models.pdf` p26–27, *Eg 5.1* — two separate M/M/1 queues (λ/2, µ each) vs one M/M/1 with 2µ vs one M/M/2 (µ each); result W(single 2µ) < W(M/M/2) < W(separate). Taught in `notes/quiz2-prep-learning.html` module 8.
- **S1's four-page shape (concepts → DTMC → queues → CTMC) matches the official 4-question count.** The mock's Q1 therefore includes process-classification and sojourn-distribution items; still a prediction.

## Archive and lecturer-sheet evidence


**Nothing below is official.** It is used only to choose practice angles. No answer key from
any of these sources is adopted; every mock answer is derived independently in
`quizzes/quiz-2-prediction-check.py`.

## Sources consulted

| Source | Author / origin | Date | What it contains | Used for |
|---|---|---|---|---|
| `resources/part-2/two-questions-random-process-queue.pdf` | Dr Patricia Wong (NTULearn, "Additional notes in lecture") | 2026 | Two lecturer-set questions: (1) (s,S) PC-inventory DTMC with Poisson(1) weekly demand → state space, TPM, steady state; (2) two M/M/1 queues vs one M/M/2 → L, idle proportion, comparison | **Highest-value style evidence** — the lecturer's own question shape |
| `resources/part-2/exercises-solution.pdf` | Lecturer | 2026 | Answers to Problems 6.2, 6.3, 9.4 | Confirms DTMC n-step, DTMC steady state, CTMC rate-balance are drilled |
| `resources/public-archive-2026-08-24/topic-explainers/EE6204-热门考点分析.xlsx` | freshman2233 (public GitHub) | ≤2024 | Topic × year table for **final exams** 2015–2023 | Topic frequency (below) |
| `…/past-exam-walkthroughs-2015-2023/2{1,2,3}-S1-Q{3,4}*.pdf` | same | 2021–2023 | Handwritten student walkthroughs of final-exam Q3 / Q4 | Question style (inventory DTMC with Poisson usage `e^{-0.1}`; machine CTMC with production rate; queue design with monthly profit / break-even) |
| RedNote S1–S3 | see "RedNote recollections" above | 2025-10-24 / 07-09 | Read in a parallel logged-in Safari session 2026-10-14 | Question-shape evidence (S1); reconstruction-only extras (S3) |
| `EE6204-26S1` WeChat group | — | — | **Not re-exported** — the `wechat-export` venv is gone; reinstalling + key extraction needs the learner | Pending |
| Web search `EE6204 Systems Analysis NTU quiz 2 Markov chain queue` | — | 2026-10-14 | Nothing course-specific | — |

## Final-exam topic frequency (same lecturer, 2015–2023; **final exam, not quiz**)

From the workbook (7 papers). These are **exam** questions; do not relabel them as quiz questions.

| Topic | Papers | Typical asks |
|---|---:|---|
| DTMC: state space + TPM | 7/7 | define `Xₙ`, list S, write every `pᵢⱼ` (often Poisson demand / usage) |
| DTMC: steady state | 6/7 | solve `Y = YP`, Σ = 1; comment on the result |
| DTMC: mean sojourn time | 4/7 | `E(Tᵢ) = 1/(1−pᵢᵢ)` + comment |
| DTMC: n-step / state probs | 2/7 | "probability after 4 weeks / 3 months" |
| CTMC: transition diagram + steady state | 5/7 | machine with setup / processing / failure / repair; rate balance |
| CTMC: production rate R | 3/7 | `R = p·π₁`, compare two designs |
| Queues: M/M/1, M/M/1/N, M/M/m, Mᵇ/M/1 | 4/7 | L, W, Q, D, π₀, "proportion of time idle", compare / recommend |
| Poisson process probability | 1/7 | probability of k arrivals in an interval |

**Reading for Quiz 2 (inference):** the 4 quiz questions plausibly map to (1) random-variable /
Poisson basics, (2) a DTMC (likely inventory with Poisson demand), (3) a CTMC machine model,
(4) a queue computation/comparison using the appendix. This is a prediction, not a fact.

## Conflicts and uncertainty

- **Weighting:** earlier WeChat chatter (see `quiz-1-intel.md`) said Quiz 2 = 20 %; the official
  Welcome post says **16 %**. Official wins.
- **Calculator:** Quiz 1 was no-calculator; **Quiz 2 explicitly allows one**. Do not carry the
  Quiz 1 habit of avoiding `e^{-x}`.
- **Question count per part / decimal places:** not stated beyond "follow the instructions".

## Open items

0. **Week 9 lecture transcript** (≈16 Oct): re-sync from NTULearn Media Gallery and mine it — it should finish the queue models and work "some questions".
1. RedNote: done (S1–S3 above). A search for Feb-2026-sitting posts could still add evidence.
2. WeChat: run `~/Projects/wechat-export/setup.sh` then export `EE6204-26S1` for 2026-09-02 → today
   if current-cohort chatter about Quiz 2 is wanted.
