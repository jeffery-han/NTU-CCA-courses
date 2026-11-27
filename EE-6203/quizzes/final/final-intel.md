# EE6203 final exam — scope and format evidence

Compiled 2026-11-27 for a final the learner reports as **Tuesday 1 Dec 2026**.  The date, time, venue and aids are **not verified**: the local NTULearn library was last synced on 27 Oct and has no final-exam announcement, and no browser was connected for a fresh sync on 27 Nov.  Check the exam timetable / NTULearn before the paper.
No official EE6203 past paper is held locally (NTU Library papers are what EE-6221 used; see "Gap" below).

## Sources consulted

| Source | What it gives | Trust |
|---|---|---|
| `resources/transcripts-raw/week-01-transcript.txt` (Wen) | "For final exam, it will be 60 %.  We have four questions.  Each question will have 25 marks.  You can check past year papers … especially recent year papers."  "In our final exam, this [z-transform] table is given.  Unless required specifically, you can use this table."  "Some of the properties will be given in the final exam … we just give some necessary ones." | High (lecturer, machine transcript) |
| `resources/transcripts-raw/week-02-transcript.txt` (Wen) | "For the final exam, we have four [questions] … the exam paper lasts 3 hours.  Each question will have 25 marks." | High |
| `resources/transcripts-raw/week-05-transcript.txt` (Lee) | "The exam will constitute 60 %." | High |
| `resources/transcripts-raw/week-08-transcript.txt` (Lee) | Prediction-observer equation (15.1): "you do not [need to] remember … if I asked in the exam … this long equation will be provided." | High |
| `resources/transcripts-raw/week-09-transcript.txt` (Lee) | Infinite-time LQR: "this algebraic Riccati equation, and this K for the infinite time problem, will be given in the question if asked … the final time problem, the two design equations, K(k), S(k), will also be given.  So you don't need to remember these two equations."  Choose the root that makes S positive definite. | High |
| `quizzes/quiz-02/quiz-02-intel.md` (Lee, Week 7 make-up lecture) | For Quiz 2: "no formula sheet … only the transform table"; "you must remember … Ackermann formula … the controllability matrix".  Assume the same for the final. | High for Quiz 2; inference for the final |
| `quizzes/quiz-03/quiz-03-intel.md` (Wen, Week 12) | No w-plane Bode question (concept only); memorise the direct-design formula and its 4 conditions, pole-zero matching incl. (z+1) factors, the ZOH; not all z-transform properties are given; marginal stability is not stability. | High |
| `resources/public-archive-2026-08-24/topic-explainers/EE6203-热门考点分析.xlsx` | Topic-by-question map of 9 past finals, 15-S1 to 23-S1 (student-made) | Medium (topics); unofficial |
| `resources/public-archive-2026-08-24/past-exam-walkthroughs-2015-2023/` | Student solutions with the question restated; 23-S1 Q1–Q4 and 22-S1 Q1–Q5 read for shape | Medium for question shape; **answers not adopted** |
| Local NTULearn library (`ntulearn`, course_key 1) | 10 announcements, none about the final; last observed 27 Oct 2026 | Stale |

## Format

- **3 h, four questions, 25 marks each, 60 % of the course** (Wen Weeks 1–2; Lee Week 5).  Earlier sittings (2018–2022) had five questions; 23-S1 already had four.
- Aids: z-transform table supplied; some z-transform properties supplied; Lee's long formulas (observer equation 15.1, LQR design equations, the ARE) supplied *if asked*.  Calculator: assume allowed (Wen's quizzes allowed one); **not verified for the final**.
- Slots, from 23-S1 (four questions) and the lecturer split:

| Q | Lecturer | Typical content (23-S1 / 22-S1 recollections) |
|---|---|---|
| 1 | Wen Ch 1–3 | Is x(t) continuous-time; sample a piecewise x(t) and find X(z) from the definition; FVT; difference equation by z-transform (initial values from k < 0); sometimes pulse TF |
| 2 | Wen Ch 4–6 | Given G_ZAS(z), controller (P or PI): stability (poles or Jury), steady-state error; ripple-free / deadbeat design; sometimes pole-zero matching or bilinear + standard programming |
| 3 | Lee Lect 1–3 | Build a state model (from equations or a block diagram); continuous → discrete Φ, Θ; transfer function; recursion; controllability / observability determinant |
| 4 | Lee Lect 3–5 | Ackermann K; observer gain L_O (or reduced-order); infinite-time LQR (u*, convergence of x(k)); sometimes k_r for unit DC gain |

## Topic frequency (spreadsheet, 9 papers 15-S1 … 23-S1; unofficial)

Highest-yield, in order: Ackermann **K** (7/7 papers with an LPH half mapped), **continuous → discrete Φ, Θ** (7/7), **FVT** (6), **ripple-free / deadbeat direct design** (5, every paper 19-S1 … 23-S1), **Jury** (5), **infinite-time LQR** (5), **controllability det W_C** (5), **pulse TF** (6), **observer gain L_O** (4), **observability det W_O** (4), difference equations (6).  Rare: finite-horizon LQR (2), k_r (2), reduced-order observer (1), similarity transform (2), programming (4 across direct/standard/series).  Never mapped: current observer, integral control, w-plane Bode (Wen: no Bode question).

## Conventions (checked against the slides)

- Wen: error **e = r − y**; K_v = lim_{z→1}(z − 1)G(z)/(Tz); stability is strict (|z| < 1), marginal is unstable.  Lecture notes pp. 164–191.
- Wen direct design: C = G_cl / [G(1 − G_cl)]; four conditions on G_cl; ripple-free keeps the plant zeros in G_cl.  Ch 5 pp. 49–82.
- Wen programming: standard needs n delays, direct needs n + m.  Ch 6 pp. 104–110.
- Lee: u = −Kx; **K = [0 … 0 1] W_C⁻¹ α_c(A)**; **L_O = α_O(A) W_O⁻¹ [0 … 0 1]ᵀ**; current observer **L_C = α_O(A) [CA; … ; CAⁿ]⁻¹ [0 … 1]ᵀ**; reduced-order error matrix A_bb − L_r A_ab.  Lect 3 p. 21, Lect 4 pp. 7, 14, 17.
- Lee integral control uses **e = y − r** (opposite sign to Wen): x_I(k+1) = x_I(k) + Cx(k) − r(k), u = −[K K_I][x; x_I] + K N_x r.  Lect 4 p. 30.
- Lee LQR cost carries a **½**: J = ½xᵀ(N)S x(N) + ½Σ(xᵀQx + uᵀRu).  A question written J = Σ(x² + u²) means **Q = R = 2** (Lect 5 Ex 5.2, p. 16).  Gains are unaffected; S and J* = ½x(0)ᵀS(0)x(0) are.
- Lee Riccati: K(k) = [BᵀS(k+1)B + R]⁻¹BᵀS(k+1)A, S(k) = (A − BK)ᵀS(k+1)(A − BK) + KᵀRK + Q; ARE for the infinite case; take the positive-definite root.  Lect 5 pp. 16–19.

## Conflicts and source errors

- **Error sign** differs between Wen (e = r − y) and Lee's integral control (e = y − r).  Use each lecturer's own sign in his question.
- **Lect 5 Ex 5.4, p. 26** prints x(2) = [0.2807 0]ᵀ; A − BK = [0 0.2087; 1 0] gives 0.2087, and the slide's own x(30) = 0.6206×10⁻¹⁰ = 0.2087¹⁵ (0.2807¹⁵ would be 5.3×10⁻⁹).  Slide typo; write 0.2087.

## Gap: official papers

No official EE6203 paper is local.  For EE-6221 the learner downloaded five papers from the NTU Library (Graduates folder) into `~/Downloads` on 20 Nov.  The same for EE6203 (2023-24 S1 onwards) would give the step-4 paper and confirm the four-question format.  Save as `tests/test-final-<year>-s<N>.pdf` (git-ignored; never commit).

## Protocol (shortened: 4 days)

| Step | Material | Status |
|---|---|---|
| 1 | `final-primer.html` (14 cards, 21 checks) | built 2026-11-27 |
| 2 | `final-mock-b.html` cold, 3 h, handwritten; key `final-mock-b.md` | built 2026-11-27 — **next** |
| 3 | Retrain every lost mark in `final-mistakes.md` | after grading |
| 4 | Most recent official paper, cold | needs the NTU Library download |

A guided Mock A was skipped for time; build one only if Mock B shows a whole slot cannot be attempted.
