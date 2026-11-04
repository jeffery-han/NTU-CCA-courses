# EE6203 Quiz 3: intel and scope

Compiled 2026-11-04. Official facts and unofficial evidence are kept apart. Nothing below the "Unofficial" heading is an official statement.

## Official (NTULearn announcement "Quiz 3", posted 30 Oct 2026, 10:09 AM, C. Wen; read 2026-11-04)

| Item | Announcement text (condensed) |
|---|---|
| Date / time | Sat 7 Nov 2026, 2:30–3:15 pm; be seated by 2:25 pm (starts and ends on time) |
| Venue | LT 2A; grouping and seating as Quiz 1 (`quizzes/quiz-01-03-grouping.pdf`, `quiz-01-03-seating-arrangement.pdf`), with an empty seat on each side |
| Duration | 45 min |
| Format | Closed book. "For non-MCQ type questions, all workings must be clearly shown on the question paper provided." This wording suggests the paper may also contain MCQs, but the announcement does not say so. |
| Scope | All topics in Wen's lectures in Weeks 4, 10, 11 and 12, i.e. Chapters 4, 5 and 6 of his notes (`resources/lecture-notes-weeks-01-04.pdf` pp. 144–195 for Ch 4; `resources/lecture-notes-chapters-05-06.pdf` pp. 1–126 for Ch 5–6) |
| Aids | Own calculator; "the necessary Transform pairs will be provided"; no phone, no unauthorised material |
| Weight | 15 % |
| Absence | Zero without a valid reason (MC); email Wen by 5 pm, 8 Nov 2026 |

Earlier context: the Week 11 recording (`resources/transcripts-raw/week-11-transcript.txt`, 26 Oct) says the quiz moved to Saturday because Monday of Week 13 is a public holiday, and that more details would come "next Monday". The Week 12 recording (2 Nov) has an attached transcript `82539 - 0_rqis9cve - PID 117.txt` (86.77 KB), seen on its Attachments tab on 2026-11-04 but **not yet downloaded**. Its opening slide shows §5.6 Two Degrees of Freedom, so Week 12 covered §5.6 onward plus Ch 6.

For comparison, Wen's Quiz 1 (31 Aug, Ch 1–3) was 30 min, one question in two parts, 25 marks (`quiz-01-*` files; results announcement 11 Sep).

## Unofficial evidence

### Sources consulted

| Source | Author / date | What it contains | Used for |
|---|---|---|---|
| RedNote search "EE6203 quiz3" | — | Not run: the RedNote MCP session was logged out (2026-11-04) | — |
| `resources/public-archive-2026-08-24/topic-explainers/EE6203-热门考点分析.xlsx` | freshman2233 (GitHub), covers 15-S1 to 23-S1 finals | Topic-by-question map of past **final exams** (not quizzes) | Topic weighting below |
| `resources/public-archive-2026-08-24/assignments-2021-2022/assignment-2/Assignment2.pdf` | Wen, AY21-22 (assignments replaced quizzes that year) | One question, 4 × 25 marks: closed-loop pulse TF with gain K, Jury range of K, w-plane Bode at K = 1, K for PM = 50° and the resulting GM | Question shape for Ch 4–5 |
| Past-exam solution PDFs 2014–2019 | NTU-CCA repo | Scanned, no text layer; not read this session | — |

### Topic frequency in past finals for the Ch 4–6 part (spreadsheet; question numbers as listed)

| Topic | Past-final hits | Note |
|---|---|---|
| Ripple-free / deadbeat design (§5.4.2–5.4.3) | Q2, Q5, Q5 (+ proof that C(z) needs an integrator), Q5 (deadbeat and ripple) | The most frequent Ch 5 item |
| Jury / pole stability (§4.3) | Q2, Q2, Q5, Q1 | Often a gain range |
| s → z mapping: bilinear; pole-zero matching of a 2nd-order controller (§5.2.2) | Q5, Q5 | |
| Direct / standard programming (§6.3–6.4); series programming (§6.7.1) | Q5, Q5, Q2 | Usually a "realise this controller" part |
| Steady-state error (§4.4.2) | Q2 | |
| w-plane frequency design (§5.3) | none in the map; it is the whole of the AY21-22 Assignment 2 | |
| 2-DOF / pole placement (§5.5–5.7) | none in the map | Newer material, so a likely candidate for an unseen item (prediction) |

These are final-exam patterns, so they show what Wen tends to set from this material, not the Quiz 3 paper itself. No recalled Quiz 3 question text or answer key was found, so nothing here needs correcting.

## How the mock uses this

`quiz-03-mock-a.*` gives 30 marks in 45 min: Q1 is short items (True/False with a reason, standing in for possible MCQs) plus a Jury gain range; Q2 maps an analog lead controller by bilinear and pole-zero matching and then realises it by standard programming; Q3 is a ripple-free deadbeat design for a type-1 plant. All numbers are new and checked by `quiz-03-check.py`.

## Open items

- Download the Week 12 transcript (needs the learner's OK) and look for any "quiz" remarks.
- Log RedNote back in (`rednote-mcp init`) and search for "EE6203 quiz 3" / "EE6203 Wen quiz" recollections.
