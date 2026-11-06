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

Earlier context: the Week 11 recording (`resources/transcripts-raw/week-11-transcript.txt`, 26 Oct) says the quiz moved to Saturday because Monday of Week 13 is a public holiday, and that more details would come "next Monday". The Week 12 recording (2 Nov, `0_rqis9cve`) covered §5.6–5.7 (2-DOF pole placement, maglev-ball example) and all of Ch 6, then gave a review of Ch 1–6. Transcript downloaded 2026-11-06 to `resources/transcripts-raw/week-12-transcript.txt`; its quiz remarks are in the next section.

For comparison, Wen's Quiz 1 (31 Aug, Ch 1–3) was 30 min, one question in two parts, 25 marks (`quiz-01-*` files; results announcement 11 Sep).

## Week 12 lecture remarks (Wen, 2 Nov; `resources/transcripts-raw/week-12-transcript.txt`)

Official in the sense that Wen said them in class; the auto-transcript is noisy, so wording is paraphrased.

- **MCQs confirmed:** "for non-MCQ type questions, show the working … if it's MCQ, just give your choice". Logistics repeat the announcement (seated by 2:25 pm, attendance taken when you hand in).
- **w-plane Bode design (§5.3): no exam questions** on it, because drawing Bode plots is too time-consuming. You "should know how", so expect at most a concept MCQ. Of the compensators, only **phase lead** was covered; lag and lag-lead were not.
- **Direct design from G_cl (§5.4) is "a quite important approach".** Memorise C(z) = G_cl / [G(z)(1 − G_cl)] and the four necessary conditions: (i) realisable (relative degree of G_cl ≥ that of G); (ii) G_cl contains G's zeros outside the unit circle; (iii) G's unstable poles are zeros of 1 − G_cl; (iv) G_cl(1) = 1 for zero steady-state error. Finite settling and deadbeat (G_cl = z^-m) need a plant with no poles or zeros outside the unit circle. Ripple-free assumes a step input.
- **Memorise the pole-zero matching formula**, including the (z+1) factors for zeros at s = ∞ (n − m − 1 of them for a strictly proper result, n − m for a proper one) and the DC-gain match that fixes α.
- **Bilinear:** substitute s = (2/T)(z−1)/(z+1), simplify, then check the time response.
- **Ch 6:** direct and standard programming; coefficient-sensitivity result (clustered poles and zeros give large errors); series and parallel programming with 1st/2nd-order sections.
- **Ch 2–4 reminders:** the whole z-transform table is given, but you must remember its conditions (x(kT) = 0 for k < 0; some entries need k ≥ 1). **Not all z-transform properties are given.** Memorise the ZOH (1 − e^(−Ts))/s. Any inverse-z method is accepted unless the question names one. For difference equations, compute any initial values the question doesn't give; do not assume them. Stability means strictly inside the unit circle; marginal stability is not considered.

## Unofficial evidence

### Sources consulted

| Source | Author / date | What it contains | Used for |
|---|---|---|---|
| RedNote "🇸🇬NTU EE6203 quiz3小记" ([link](https://www.xiaohongshu.com/explore/67fe7f12000000001c010d02)) | Passion阳, ~Apr 2025 (25S2), 155 likes, 11 comments | 3 questions: (1) Jury K-range; (2) bilinear transform of a continuous G(s) to G(z); (3) given G_ZAS(z), decide whether the output tracks the input with G_cl = z⁻¹, and if so design C(z). Its 4 images are lecture slides the questions resembled: Ex 4.8 (Jury, open-loop G(z) with K), §5.2.2 bilinear, §5.4 direct design (5.11). | Mock B shape |
| RedNote "NTU EE6203 quiz3" ([link](https://www.xiaohongshu.com/explore/69dceefb000000002102fa63)) | undertaker, Apr 2026 (26S2) | Scope "WCY Lecture 4–5", 45 min, 3 questions, the same three as above: block diagram + open-loop TF with K → Jury; G(s) + T → bilinear; block diagram + G_ZAS + desired G_cl → can it track, and if so C(z) | Mock B shape |
| RedNote "EE6203 Quiz 3题型与考点" ([link](https://www.xiaohongshu.com/explore/67335068000000003c01ed23)) | earthgull, fall 2024 (24S1), 31 likes | 3 calculation questions: Jury criterion, pole-zero matching, ripple-free deadbeat | Mock A Q2(b)/Q3; Mock B Q2(b) |
| RedNote "EE6203 Quiz1 26S1" ([link](https://www.xiaohongshu.com/explore/6a959b24000000002601739f)) | Allegra, 31 Aug 2026 | Wen's Quiz 1 **this semester**: one 12-mark calculation + four MCQs (3, 3, 3, 4), total 25 | Evidence that Wen now uses MCQs, so Quiz 3 may too |
| RedNote comment threads | — | `get_note_comments` timed out on 2026-11-04; not read | — |
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

These are final-exam patterns, so they show what Wen tends to set from this material, not the Quiz 3 paper itself. ### Quiz 3 format from recollections (medium trust: three independent posters agree)

- **Format (high agreement):** 3 calculation questions, 45 min. Every recalled sitting had a Jury K-range question and a z-domain direct-design question. The middle question was the bilinear transform twice and pole-zero matching once.
- **Question text:** only paraphrased; no numbers were recalled and no answer keys were posted, so there is nothing to correct.
- **This year differs:** the scope now includes **Ch 6** (implementation), and Wen's 26S1 Quiz 1 mixed MCQs with calculation. Expect the same three calculation types plus possibly short MCQs on Ch 5–6 concepts (lead/lag, 1-DOF/2-DOF, pole placement, programming forms). That last part is a prediction.

### WeChat class group (`EE6203-26S1`, 930 messages, 24 Aug – 6 Nov 2026; exported locally 2026-11-06)

Classmates' messages, paraphrased with no names. The export is kept outside this repo. Nothing here contradicts the official facts above.

- **Quiz 3 logistics:** classmates agree on Sat 7 Nov, 2:30 pm, and the Quiz 1 seating PDF ("Seating Arrangement for Quiz 1 and Quiz 3", the same file as `quiz-01-03-seating-arrangement.pdf`).
- **Same recollections as ours:** on 5 Nov the Passion阳 RedNote post was shared as "what Quiz 3 will test". On 6 Nov a classmate posted a topic list merged from "three seniors' posts" (an image the export cannot decrypt). It is very likely the three RedNote posts in the table above. Classmates add that the 24/25 and 26S2 sittings had the same shape. No new recollection or question numbers appeared.
- **The recall pattern repeated in Quiz 2 (LPH, 5 Oct):** right after that quiz, one classmate said anyone who prepared the recalled paper "got full marks … full copy paste of recall". Others gave K = 4.5 and 0.5 for the last part. This is one person's claim and it concerns a different lecturer, but it supports drilling the recalled Quiz 3 shape (Mock B) as the main rehearsal.
- **Quiz 1 as sat (31 Aug, Wen):** one calculation question plus four MCQs (one student counted three). A shared answer string was "CBCB". This confirms the RedNote Quiz 1 post, so Wen setting MCQs on Quiz 3 is plausible.
- **Jury table notation:** one classmate could not find where b, c, q are defined. Another pointed to Ch 4 slides 21–22, roughly PDF pp. 164–165 of `resources/lecture-notes-weeks-01-04.pdf` (Table 4-1, general form of the Jury table). You build the table yourself; it is not given.
- **Tables handout:** a student-made `Tables_讲义全部表格汇总.pdf` (12 pp.) collects the numbered tables from Wen's Weeks 1–4 notes (z-transform Table 2-1, properties 2-2, Table 2-3, 3-1, Jury 4-1 to 4-3, system types 4-4, static error constants 4-5). A classmate said in August that this is what Wen hands out. Wen's Week 12 remark (transform table given, **not** all properties) outranks that claim, so assume the Jury and error-constant tables are **not** provided.
- **Attendance:** after Quiz 1, one student who had sat it was shown as absent and had to email the lecturer. A classmate said this happened the previous semester too. Hand the paper in personally and make sure your attendance is recorded.

## How the mocks use this

- **Mock B** (`quiz-03-mock-b.*`) copies the recalled 3-question shape: Q1 Jury from an open-loop G(z) with K, plus K_v; Q2 bilinear, then pole-zero matching, then direct programming; Q3 "can G_cl = z⁻¹ be used?" for one plant where it can and one where an outside-circle zero forbids it.
- **Mock A**: `quiz-03-mock-a.*` gives 30 marks in 45 min: Q1 is short items (True/False with a reason, standing in for possible MCQs) plus a Jury gain range; Q2 maps an analog lead controller by bilinear and pole-zero matching and then realises it by standard programming; Q3 is a ripple-free deadbeat design for a type-1 plant. All numbers are new and checked by `quiz-03-check.py`.
- **Mocks C and D** (`quiz-03-mock-c.html`, `quiz-03-mock-d.html`, added 7 Nov at the learner's request for "the real quiz, no T/F"): full timed papers in the confirmed format. Section A has 4 single-answer MCQs (3 marks each). Section B has the 3 recalled calculation questions: Jury K-range, s→z mapping plus Ch 6 programming, and direct design. Total 40 marks in 45 min (the mark split is a guess). C: 2nd-order Jury from ZOH + K/(s(s+2)); matched + bilinear + standard programming; unstable plant pole, so G_cl = a0 z⁻¹ + a1 z⁻². D: 3rd-order Jury where the b-row binds; lead controller bilinear/matched + direct programming; z⁻¹ design with ripple, then ripple-free. Keys checked by `quiz-03-mock-cd-check.py`.

## Open items

- RedNote comment threads (11 + 16 comments on the two main posts) not yet read; the tool timed out.
