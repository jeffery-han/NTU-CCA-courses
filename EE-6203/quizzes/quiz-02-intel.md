# EE6203 Quiz 2 (LPH part) — intelligence

Compiled 2026-09-24; past-sitting recollections added the same day. Everything from students or archives is **unofficial**; official items cite the lecturer.

## Sources consulted

| Source | Author / origin | Date | Engagement | What it contains |
|---|---|---|---|---|
| `quiz-02-announcement-slide.jpg` | LPH lecture slide (photo) | 2026 S1 | — | Quiz date, time, weight, scope wording, in-person |
| NTULearn announcement "State-Space and Optimal Control - from 7 Sept 2026" | Dr Lee Peng Hin | 28 Aug 2026 | — | Takes over from 7 Sep; notes in "Lee PH" folder; quiz 5 Oct, 15 % |
| NTULearn announcements on the 21 Sep reschedule | Dr Lee Peng Hin | 20–21 Sep 2026 | — | 21 Sep cancelled; make-up Sat 26 Sep, 9:30–12:30, LT28, recorded |
| `resources/week-05-transcript.txt` | LPH Lecture 1 recording | 7 Sep 2026 | — | 5 lectures × 3 h; quiz covers "Today's lecture, next week lecture, and one more week … Lecture three"; quiz sits in the Lecture 4 slot after recess; same transform table as quiz and exam |
| `resources/week-06-transcript.txt` | LPH Lecture 2 recording | 14 Sep 2026 | — | Finished Lect 2 (controllability) and began Lect 3 §9 (observability) |
| RedNote "NTU EE6203 quiz2" ([note](https://www.xiaohongshu.com/explore/69aed1c2000000001b01cc45)) | undertaker | 2026-03-09 (AY25/26 S2 sitting) | 3 likes, 5 saves, 3 comments | **Scope "LPH-Lecture1～3", 45 min, 3 questions**; question outline (below). Comment thread: two sitters both got a **fractional K** in Q3 and neither was sure |
| RedNote "🇸🇬NTU EE6203 quiz2小记" ([note](https://www.xiaohongshu.com/explore/67d9a63c000000001b038dd1)) | Passion阳 | 2025-03-19 (AY24/25 S2 sitting) | 78 likes, 113 saves, 14 comments | 3 questions with sub-parts (below); images are the poster's LPH slide screenshots per sub-part, **not** the quiz paper. Comments: "考得差不多" (that's about what was tested), "和上学期的差不多" (similar to last semester's), author confirms Master's course |
| GitHub `yzmyyds/NTU_EE6203` → `Quizs(Recall_Version)/Quiz2_Recall.md` (+ `.pdf`) | yzmyyds | committed 2025-09-22 (AY25/26 S1 sitting) | — | 3 questions with actual recalled matrices (below); same LPH `Lect 1–5.pdf` in the repo |
| `resources/public-archive-2026-08-24/past-exam-solutions-2014-2019/EE6203 2018-2019.pdf` pp. 11–13 | Public NTU-CCA repo (scanned exam paper + student solutions) | Nov/Dec 2018 | — | LPH **exam** questions: Q3(a) ZOH discretisation + discrete poles (10), Q3(b) choose C for observability (5), Q3(c) LQR (5), Q4(a) deadbeat state feedback (7), Q4(b)–(c) observers (7, 6) |
| `.../past-exam-walkthroughs-2015-2023/22-S1-Q3`, `23-S1-Q3`, `23-S1-Q4` | freshman2233 personal solutions | 2022–23 | — | State-space model / \(C(zI-A)^{-1}B+D\); Ackermann pole placement |
| Web search (3 queries: "EE6203 quiz 2 state space Lee Peng Hin NTU", "\"EE6203\" quiz recall", "NTU EE6203 小红书 quiz2 回忆") | — | 2026-09-24 | — | Nothing new: only the known GitHub repos, Course Hero/Scribd course files |
| GitHub `naminibaga/solved-ee6203-assignment-{1,2}` | — | 2023 | — | README only (paid-solution listing); nothing usable |

## Past Quiz 2 sittings (unofficial recollections)

| | 2025 S2 (Passion阳, Mar 2025) | 2025 S1 (yzmyyds, Sep 2025) | 2026 S2 (undertaker, Mar 2026) |
|---|---|---|---|
| **Q1 — modelling** | (i) state-space model from a physical system (poster attaches the Lect 1 servomotor slide); (ii) state-space model from a block diagram | (i) state equations from \(5\ddot y-2\dot y=2u\), \(y=x_1,\ x_2=\dot x_1\); (ii) \(Y(s)/U(s)\) | 2nd-order state-space model of the whole system from a **block diagram** |
| **Q2 — ZOH discretisation** | (i) continuous system + sampler \(T\) → discrete state-space; (ii) controllability; (iii) discrete TF "by formula" | \(\dot{\mathbf x}=\begin{bmatrix}1&\beta\\0&2\end{bmatrix}\mathbf x+\begin{bmatrix}0\\1\end{bmatrix}u,\ y=[1\ 0]\mathbf x\), \(T=0.5\): (i) discretise; (ii) \(\mathbf X(z)/U(z)\) in terms of \(\beta\); (iii) controllability as \(\beta\) varies | 2nd-order continuous system: (i) discretise with given \(T\); (ii) **controllability and observability** of the result |
| **Q3 — discrete response / design** | (i) **deadbeat** state-feedback gain \(\mathbf K\); (ii) show the response is deadbeat | State-transition: \(\mathbf A=\begin{bmatrix}1&0.5\\-0.5&-1\end{bmatrix},\ \mathbf B=[1\ 1]^T,\ \mathbf x(0)=[2\ 2]^T,\ u(0)=1,\ u(1)=-1\) → \(\mathbf x(2)\) (recall writes \(\dot X\) but the question is discrete) | 2nd-order discrete system: (i) **deadbeat** \(\mathbf K\) (fractional); (ii) with that \(\mathbf K\) and given \(\mathbf x(0)\), find \(\mathbf x(3)\) |

## Classified claims

| Class | Claim | Trust | Use |
|---|---|---|---|
| Format | 45 min, 15 %, in person, 5 Oct 8:30–9:15 pm | **Official** | Timer and weighting |
| Format | Scope = LPH's first three lecture sessions (Lect 1–3) | **Official** (LPH, Week 5) + matches "LPH-Lecture1～3" in the 2026 S2 recollection | Lect 1–3 material |
| Format | Transform table issued (`lph-transform-table-ay2018-19-s1.pdf`) | **Official** (spoken) | Supplied with the paper |
| Format | **3 questions, each 2nd-order, multi-part** | **High** — 3 independent sittings agree; "similar to last semester" comment | Drive the paper's shape |
| Format | Q1 modelling → Q2 ZOH discretisation + structural property → Q3 discrete response/design | **High** — same order in all 3 | Question order |
| Format | Closed book, calculator, marks per question | **Unknown** — no recollection states them; LPH "more details later" | Keep numbers hand-tractable |
| Question text | Q1: block diagram (2/3) or physical system/ODE (2/3) to state space; TF sometimes asked | Medium | Practise both routes |
| Question text | Q2: controllability every time (3/3); observability (1/3); discrete TF (2/3); a symbolic parameter (\(\beta\)) once | Medium | Expect a rank test, possibly parametric |
| Question text | Q3: deadbeat \(\mathbf K\) (2/3) then a response check (\(\mathbf x(n)=0\), or \(\mathbf x(3)\)); pure state transition \(\mathbf x(2)\) once (1/3, the S1 sitting where the quiz came earlier) | Medium | Deadbeat + iterate \(\mathbf x(k+1)=(\mathbf A-\mathbf B\mathbf K)\mathbf x(k)\) |
| Answer keys | "K came out as fractions" (2026 S2 comment) | **Low** — two unsure sitters | Not adopted; fractions are plausible for a deadbeat gain but prove nothing |
| Answer keys | Student walkthrough answers | **Low** | Not used; every key re-derived and checked by `quiz-02-prediction-check.py` |

## Conflicts and uncertainty

- **Q3 content differs between sittings.** Both S2 sittings asked deadbeat design; the S1 2025 sitting asked a plain state-transition \(\mathbf x(2)\) instead. A likely (unverified) reason is timing: the S1 2025 recall was committed on 22 Sep 2025, so that quiz may have come before deadbeat was taught. This year the quiz follows three sessions, so the S2 pattern (deadbeat) is the better guide **if** the 26 Sep session reaches Lect 3 §13. Prepare both: deadbeat \(\mathbf K\) *and* iterating the state equation with inputs.
- **Q1 source varies** (physical system / ODE / block diagram). Practise all three.
- **The 2025 S2 poster's images are slide screenshots**, confirmed by the poster's own framing (page references p1–p9 per sub-part); do not treat them as quiz figures.
- The 2025 S1 recall writes \(\dot X\) for Q3 although it asks for \(\mathbf x(2)\) of a "discrete" model; read it as \(\mathbf x(k+1)=\mathbf A\mathbf x(k)+\mathbf B u(k)\).

## Implication for `quiz-02-prediction-paper`

The current prediction paper (one 25-mark question, parts a–d) predates this evidence. It covers Q2 and Q3 topics (ZOH discretisation, TF, controllability, deadbeat, observability) but **lacks a Q1 modelling question (block diagram / physical system / ODE → state space)** and does not follow the 3-question layout. Rebuild or add a second paper in the 3-question shape.

## Scope boundary (provisional)

Lect 1 §1–4, Lect 2 §5–8, Lect 3 §9–13 are expected (now corroborated by the 2026 S2 "LPH-Lecture1～3"). Session 3 (26 Sep) decides whether §11–13 (state feedback, Ackermann, deadbeat) are reached and whether Lect 4 §14 (observers) starts. **Re-check against the 26 Sep transcript.** Past-exam observer and LQR parts (Lect 4–5) are outside Quiz 2 unless that transcript says otherwise.

Schedule facts come from NTULearn and the lecturer; verify any change there, not from student posts.
