# EE6203 Quiz 2 (LPH part) — intelligence

Compiled 2026-09-24. Everything from students or archives is **unofficial**; official items cite the lecturer.

## Sources consulted

| Source | Author / origin | Date | What it contains |
|---|---|---|---|
| `quiz-02-announcement-slide.jpg` | LPH lecture slide (photo) | 2026 S1 | Quiz date, time, weight, scope wording, in-person |
| NTULearn announcement "State-Space and Optimal Control - from 7 Sept 2026" | Dr Lee Peng Hin | 28 Aug 2026 | Takes over from 7 Sep; notes in "Lee PH" folder; quiz 5 Oct, 15 % |
| NTULearn announcements on the 21 Sep reschedule | Dr Lee Peng Hin | 20–21 Sep 2026 | 21 Sep cancelled; make-up Sat 26 Sep, 9:30–12:30, LT28, recorded |
| `resources/week-05-transcript.txt` | LPH Lecture 1 recording | 7 Sep 2026 | 5 lectures × 3 h; quiz covers "Today's lecture, next week lecture, and one more week … Lecture three"; quiz sits in the Lecture 4 slot after recess; same transform table as quiz and exam |
| `resources/week-06-transcript.txt` | LPH Lecture 2 recording | 14 Sep 2026 | Finished Lect 2 (controllability) and began Lect 3 §9 (observability) |
| `resources/public-archive-2026-08-24/past-exam-solutions-2014-2019/EE6203 2018-2019.pdf` pp. 11–13 | Public NTU-CCA repo (scanned exam paper + student solutions) | Nov/Dec 2018 | LPH questions: Q3(a) ZOH discretisation + discrete poles (10), Q3(b) choose C for observability (5), Q3(c) LQR (5), Q4(a) deadbeat state feedback (7), Q4(b)–(c) observers (7, 6) |
| `.../past-exam-walkthroughs-2015-2023/22-S1-Q3`, `23-S1-Q3`, `23-S1-Q4` | freshman2233 personal solutions | 2022–23 | State-space model / \(C(zI-A)^{-1}B+D\); Ackermann pole placement |
| RedNote search "EE6203 quiz2" | — | 2026-09-24 | **Not searched**: the RedNote page load timed out (30 s). Retry once logged in if recollections from earlier runs are wanted |

## Classified claims

| Class | Claim | Trust | Use |
|---|---|---|---|
| Format | 45 min, 15 %, in person, 5 Oct 8:30–9:15 pm | **Official** | Timer and weighting |
| Format | Scope = LPH's first three lecture sessions | **Official** | Lect 1–3 material |
| Format | Transform table issued (`lph-transform-table-ay2018-19-s1.pdf`) | **Official** (spoken) | Supplied with the paper |
| Format | Question count/type, closed book, calculator | **Unknown** — "more details later" | Predicted: one 25-mark structured question (= one LPH exam question's size and time) |
| Question text | ZOH discretisation, discrete poles, observability via choice of C, deadbeat design, Ackermann | Medium (recurring exam topics, not quiz recollections) | Topic weighting of the prediction paper |
| Answer keys | Student walkthrough answers | **Low** | Not used; every key re-derived and checked by `quiz-02-prediction-check.py` |

## Scope boundary (provisional)

Lect 1 §1–4, Lect 2 §5–8, Lect 3 §9–13 are expected. Session 3 (26 Sep) decides whether §11–13 (state feedback, Ackermann, deadbeat) are reached and whether Lect 4 §14 (observers) starts. **Re-check against the 26 Sep transcript.** Past-exam observer and LQR parts (Lect 4–5) are outside Quiz 2 unless that transcript says otherwise.

Schedule facts above come from NTULearn and the lecturer; verify any change there, not from student posts.
