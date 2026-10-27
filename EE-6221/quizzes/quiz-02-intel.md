# EE6221 Quiz #2 — intelligence and scope (compiled 2026-10-27)

## Official arrangement (NTULearn announcements 5 Oct and 26 Oct 2026, Prof. Hu Guoqiang)

- **Wed 4 Nov 2026, 8:00–9:00 pm, LT19A.** Lecture 6:30–7:30 pm (part of Lec 5); leave the LT 7:35–7:50 pm, re-enter 7:50–8:00 pm.
- **Topic: Weeks 8–11 = the four lectures** `resources/part-2/part-2-lecture-01…04`. "Short questions will be given to test how well students understand basic concepts covered in these four lectures."
- Paper and pen, **closed book, no calculator**, no phone/laptop/iPad. Photo ID; sit per the Quiz #1 arrangement. **15%**; absence without MC/LOA = zero.

## Lecturer statements (Week 8 recording, `resources/transcripts-raw/week-08-transcript.txt`, machine transcript)

- Quiz covers "the first four topics"; the **final exam** for Part 2 covers only Lec 2–4 (Lec 1 "not covered in the final exam"). So Lec 1 is quiz-only material — expect it on the quiz.
- Lec 1 is "concepts, no math"; Lec 2–4 add geometry/methods/math (also `part-2-summary.pdf` p. 1).
- **GPS:** "We include GPS in both internal and external state sensors." Resolves the Lec 1 p. 17 listing (GPS/INS/compass as proprioceptive). Do not answer "GPS is only exteroceptive".
- In-class discussion questions (Hu: "this is not a quiz", but Q5 is "a question to help you prepare for the quiz"): (1) can a robot act intelligently with only internal sensors? (2) why use multiple sensors? (3) which of camera / LiDAR / ultrasonic are active? (4) a sensor gives the same wrong reading every time — accurate or precise? (5) why does integrating IMU data forever drift? (6) ultrasonic TOF: 10 ms at 340 m/s → 3.4 m round trip → **1.7 m**. These define the expected *style*: concept + one-line reason, small hand calculations.

## Sources consulted

| # | Source | Date | What it contains | Evidence class |
|---|---|---|---|---|
| 1 | NTULearn announcements `_813452_1`, `_820265_1` | 5 & 26 Oct 2026 | Date/time/venue/scope/rules above | **Official** |
| 2 | Week 8 lecture recording (transcript) | Oct 2026 | Scope split quiz vs exam; GPS convention; six in-class questions | Lecturer statement (ASR text, wording approximate) |
| 3 | RedNote 彬仔睡不醒, id 6a1fcf3b (recorded in `quiz-01-intel.md` #4) | earlier run | "second quiz is concept-based (10 True/False with justification + one short-answer)" | Format: **medium** — single source, earlier year |
| 4 | RedNote earthgull "EE6221 Quiz2 题型与考点", id 6734935f (`quiz-01-intel.md` #6) | Autumn 2024 | TF + reasoning, multi-sensor, **Lyapunov** | Format: medium. Lyapunov = vision-based control (Lec 5–6) — **out of this year's scope** (scope drift: 2024 quiz evidently reached further) |
| 5 | `public-archive-2026-08-24/past-exam-2024-2025/test-final-2024-2025-semester-1.pdf` pp. 4–5 | AY24-25 S1 final | Q4 homography (12 coplanar points, G/H/J, count four-point groups); Q5 three-sensor Kalman gains + one-gain variant | Exam (not quiz) style — 20-mark derivations; signals which Lec 3–4 skills Hu examines |

RedNote re-check on 2026-10-27 failed: both the MCP and the browser session are **logged out** (login is the learner's action). Re-search "EE6221 quiz2" after logging in if more format evidence is wanted.

## Slide-convention traps (re-checked against the decks)

- Lec 1 p. 17 lists GPS, INS, compass as *proprioceptive*; textbooks say exteroceptive. Course answer: GPS is both (lecturer).
- Lec 1 p. 36 writes TOF as `d = c·t` with d the round-trip distance; p. 38 ultrasonic uses **`d = c·t/2`** (one-way). State which.
- Lec 1 p. 25: accuracy `= 1 − |m − v|/v`; precision `= range / standard deviation`.
- Lec 2 p. 30: `A = [fσx, −fσx tanα, u0; 0, fσy secα, v0; 0, 0, 1]`, `p = A m`, `m = [x/z, y/z, 1]ᵀ`.
- Lec 3 p. 13 says "no four 3D points coplanar" for the 8-point algorithm; p. 26 says "no more than 4 coplanar". Avoid answers that hinge on the exact count; the key fact is **not all coplanar** (p. 43).
- Lec 4 p. 42 writes `R = diag(σ1², σ2²)` for the *sequential* update, where the scalar update actually uses `R = σ2²` with `P0 = σ1²`. The result (12) is right; the R label is loose.

## Prediction (unofficial)

~10 True/False with one-line justification across Lec 1–4, plus one short-answer derivation. The most likely derivation is the **two-sensor Kalman fusion from first principles** — Lec 4 p. 42 literally sets "Q: Derive the above from first principles", and the 2024-25 exam Q5 is its three-sensor version. Second candidate: pinhole projection / normalised coordinates with integer intrinsics (no calculator). Lec 3 is likely tested conceptually (E vs H requirements, scale loss, number of solutions, positive-depth test) rather than by SVD arithmetic.

Mock built from this: `quiz-02-mock-01.html` (answer-free) + `quiz-02-mock-01.md` (key) + `quiz-02-mock-01-check.py`.
