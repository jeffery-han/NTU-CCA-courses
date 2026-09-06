# EE6221 Quiz 1 — past-paper intelligence

Compiled 2026-09-06 from a logged-in RedNote (小红书) search, one GitHub study note, and the
official NTULearn "Exercises for Kinematics (not for submission)" handout. Everything attributed to
students below is **unofficial recollection** — labelled as such wherever it is used.

## Bottom line

Quiz 1 has been, for several recent sittings, a **two-question, ~30-minute, closed-book, handwritten**
paper:

1. **D–H modelling.** Given a manipulator drawing: assign link frames (the "how to draw the x/y/z
   axes" procedure the instructor drilled repeatedly in lecture examples) and tabulate the four D–H
   parameters for every joint. One sitting had a 7-joint arm and students ran short on time — speed
   is the graded skill, not cleverness.
2. **Pick-and-place arm matrix.** Write the homogeneous transformation (arm matrix)
   $^{\text{base}}T_{\text{pick}}$ for a gripper picking a part from above. Lower difficulty; the
   instructor worked the method in class.

The format evidence is **converged** (four independent posters + one official handout point the same
way). Question wording and any recalled numbers are **approximate** and were re-derived from scratch
for the mock.

## The near-confirmation: the official practice handout

`resources/exercises-kinematics-not-for-submission.pdf` (NTULearn, "Exercises for Kinematics (not for
submission)") contains **exactly two problems**:

- **Problem 1** — planar 4-joint robot (joints 1–2 prismatic, 3–4 revolute with intersecting axes,
  200 mm tool): (a) D–H link-coordinate diagram + full parameter table, (b) direct kinematics
  $^{\text{wrist}}T_{\text{tool}}$ and $^{\text{base}}T_{\text{wrist}}$, (c) tool configuration vector
  + inverse kinematics, (d) tool configuration Jacobian.
- **Problem 2** — top view of a workstation with parts A $[6,12,2]^T$ and B $[10,5,1]^T$: (a) arm
  matrix $^{\text{base}}T_{\text{pick}}$ to pick A from above grasping the long sides, (b) arm matrix
  $^{\text{base}}T_{\text{place}}$ to stack A on B with centroids and major axes aligned.

RedNote poster **Kenta** states: *"quiz 前给出了两个练习题刚好对应这两个考点"* — the two practice
problems handed out before the quiz corresponded exactly to the two exam topics. Problem 1 → Quiz Q1,
Problem 2 → Quiz Q2. This upgrades the paper shape from student memory to an **official-current**
source. Parts (c)/(d) of Problem 1 (Jacobian; full IK) sit at or beyond the stated Quiz 1 boundary
and are treated as the "predicted extension", not the core paper.

The mock therefore uses a **different arm and different part coordinates** — reusing Problem 1's PPRR
arm or Problem 2's $[6,12,2]$/$[10,5,1]$ numbers would test recall of an answer the learner has
already seen (both are quoted verbatim in `output/self-studying/notes-bank.json`).

## Sources consulted

| # | Title / author | Platform | Date signal | Engagement | What it contains | Evidence class |
|---|---|---|---|---|---|---|
| 1 | *"EE6221 quiz1 总结"* — Kenta | RedNote | tagged 考试周; post id 68da1d38 (Sep 2024 era) | 22 likes, 2 comments | Q1 = D–H modelling (drilled x/y/z drawing), 4 params/joint, one 7-joint sitting, time-tight. Q2 = homogeneous translation matrix for a "pick" grasp, not hard. Two pre-quiz practice problems matched the two exam points. | Format: **high**. Question text: medium. |
| 2 | *"EE6221 Quiz1"* — 新叶猫 | RedNote | ongoing self-study log; id 69961ba1 | 57 likes | Image-based worked D–H solution with two posted **corrections**: (i) when joint Z-axes intersect ($a=0,d=0$) put the origins coincident and use Pythagorean (root) composition for the shortest distance between skew axes, with $x$ along that shortest-distance direction regardless of how "level" it looks; (ii) some $y$-axis arrows were drawn reversed. | Question text: medium. Answer key: **low** (student self-correction — re-derived below). |
| 3 | *"6221 Quiz1 真题回忆版"* — 新叶猫 | RedNote | id 699ef795 | 5 likes | "Recalled real questions" (image-only). Text note: mis-read "base frame" as "the base joint" rather than "the 0-0-0 origin" — a terminology trap worth flagging. | Question text: medium. |
| 4 | *"NTU EEE 选课第二学期"* — 彬仔睡不醒 | RedNote | S2 review, multi-course; id 6a1fcf3b | 16 likes | "EE6221: two quizzes + assignment; **first quiz mainly tests D–H coordinate frames and parameters**; second quiz is concept-based (10 True/False with justification + one short-answer)." Final exam structure Q1 D–H, Q2 robot control, Q3 mobile robot + IK, Q4 four-point method, Q5 Kalman filter. | Format: **high** (agrees with #1). |
| 5 | *"复习时长为一天，ee6221 基本上会写"* — 勇闯新加坡 | RedNote | id 681ad8df | 35 likes, 32 comments | "This year they added a lot of the **first instructor's kinematics-equations material, taught before Quiz 1**." Past papers are highly templated; ~75% fixed method. | Scope drift signal: pre-Quiz-1 content has been expanding. |
| 6 | *"EE6221 Quiz2 题型与考点"* — earthgull | RedNote | 24 秋 (Autumn 2024); id 6734935f | 68 likes, 14 comments | Quiz **2** structure only (TF + reasoning, multi-sensor, Lyapunov). Not Quiz 1 — recorded to keep the two quizzes from being confused. | Out of scope for Quiz 1. |
| 7 | `6221_review_before_quiz1.pdf` — KuRRe8/eeemsc-coursework | GitHub | authored 2024; OneNote export, author warns text unchecked | repo-level | Personal pre-Quiz-1 review note. Confirms the **Schilling** convention and notation used by the course: link transform $T^{k}_{k-1}=\text{Rot}(\theta_k,z)\,\text{Trans}(d_k,z)\,\text{Trans}(a_k,x)\,\text{Rot}(\alpha_k,x)$; tool orientation columns = normal/sliding/approach $=r_1/r_2/r_3$; tool configuration vector $w=[\,p\,;\ e^{q_n/\pi}r_3\,]$, $q_n=\pi\ln\lVert w_{4:6}\rVert$; inverse homogeneous transform $T^{-1}=\begin{bmatrix}R^{\mathsf T}&-R^{\mathsf T}p\\0&1\end{bmatrix}$. | Notation: **high** (matches `review-week-02-dh-algorithm-summary.pdf` and `notes/notes.tex`). |
| 8 | Course review posts (undertaker id 6a1e6c9c; Kongl id 6a224e95) | RedNote | S1 reviews | 67 / 186 likes | "Both instructors' quizzes are very stable in question type"; "quiz is pure routine". General corroboration only. | Format: low-specificity corroboration. |

Not used: commercial tutoring / answer-selling posts (述几留学生, 逃离李伟南, momo "收答案"), and any
post about a different course.

## Evidence classes applied

- **Format (drives the mock's structure) — HIGH.** 2 free-response questions; ~30 min; closed book;
  handwritten; Q1 = D–H frame assignment + parameter table for a multi-joint arm; Q2 = pick-from-above
  arm matrix. Sources 1, 4, 7 + the official handout agree.
- **Question text — MEDIUM.** Re-derived from in-scope topics; recalled wording treated as
  approximate; the mock deliberately changes the arm and the coordinates.
- **Answer keys — LOW / not adopted.** 新叶猫's self-corrections (source 2) are plausible textbook
  points but are re-derived against the instructor slides in `quiz-01-mock-01.md`, not copied.

## Scope boundary (unofficial — verify against the NTULearn notice)

From `STATUS.md`: Quiz 1 ≈ **23 Sep 2026**, ~30 min, rooms via NTULearn. Basis = class group chat
(~2026-09-02) + the instructor's Week 3 lecture remarks in a personal transcript ("first four weeks
only", explicitly excluding the following week). Mapped topics: frames/rotations, homogeneous
transforms + inversion, D–H direct kinematics + arm matrix + tool configuration vector, inverse
kinematics (atan2, elbow branches), cubic trajectory planning. **Out:** Jacobian / differential
motion / singularities, robot control, mobile robots, intelligent sensors.

Circulating Quiz 1 papers only ever show D–H + pick-and-place arm matrix. IK, the tool configuration
vector, and cubic trajectory planning are *in the stated scope* but *absent from recalled papers* —
so they are the likely "one unseen item". The mock puts them in a clearly labelled predicted
Section C.

## Still outstanding (needs the learner)

1. The **official NTULearn Quiz 1 announcement**: confirmed date, time, venue, duration, exact scope
   cutoff, permitted aids. Everything above about logistics is second-hand.
2. Whether the "first instructor's kinematics-equations" additions (source 5) are examinable in
   Quiz 1 this run.
3. Optional: RedNote comment threads on sources 1–3 (the `get_note_comments` call timed out; the
   caption evidence is already sufficient for format).
