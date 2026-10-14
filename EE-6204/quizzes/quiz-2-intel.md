# EE6204 Quiz 2 — historical preparation context

Updated 2026-10-14. Read in logged-in Safari on Xiaohongshu/RedNote, searching `EE6204 Quiz2`, `EE6204 quiz 2`, and `6204 quiz2`. These searches returned the same core reports; this is a targeted search, not an exhaustive archive.

**Status: unofficial.** Student recollections and an explicitly GPT-generated reconstruction are preparation evidence, not an official paper, marking scheme, or confirmation of this semester's scope. No current Quiz 2 announcement was inspected. Do not inherit Quiz 1's lecturer, calculator rule, duration, weighting, or LockDown arrangements.

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

## Still unknown / next source checks

- Current official scope, quiz date, duration, weighting, question count, format, open/closed-book status, calculator policy, allowed appendix, and software requirements.
- Whether S3 reconstructs the October 2025 sitting: its topic overlap is consistent, but no explicit sitting date establishes this. Do not treat overlap as two independent verified papers.
- Match S1's Example 5.1 and these topic patterns to the newly present `../resources/part-2/` materials before building a mock or updating canonical teaching notes. Those materials were inventoried, not read for this search.

No source file was moved or renamed. This is an intelligence-only update; canonical LaTeX notes and PDFs were not changed.
