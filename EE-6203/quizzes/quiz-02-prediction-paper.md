# EE6203 Quiz 2 prediction paper — key and marking rubric

> **UNOFFICIAL PREDICTION.** Constructed 2026-09-24; not an official paper, key or marking scheme.
> Exam page (answer-free): `quiz-02-prediction-paper.html`. Numerical check: `python3 quiz-02-prediction-check.py`.

## What is known and what is predicted

| Item | Status | Source |
|---|---|---|
| 5 Oct 2026 (Mon), 8:30–9:15 pm, 45 min, in person, 15 % | Official | `quiz-02-announcement-slide.jpg`; NTULearn announcement 28 Aug 2026 |
| Scope: LPH's first three lecture sessions (7 Sep, 14 Sep, 26 Sep make-up) | Official (LPH, Week 5 transcript) | "Today's lecture, next week lecture, and one more week … Lecture three" |
| Material expected in scope: `lph-lecture-01` to `lph-lecture-03` (Sections 1–13) | **Provisional** — confirm with the 26 Sep transcript | Session 2 (14 Sep) finished Lect 2 and began Lect 3 §9; session 3 may not reach §13, or may spill into Lect 4 §14 observers |
| Transform table supplied | Official (LPH, Week 5 transcript) | "the same table you will get for your quiz and the exam" → `../resources/lph-transform-table-ay2018-19-s1.pdf` |
| Format: one 25-mark structured question, 45 min | **Prediction** | An LPH exam question is 25 marks in a 3-hour, 4-question paper (= 45 min); 2018-19 Q3/Q4 shape (parts of 5–10 marks) |
| Closed book, calculator rules | Unknown ("more details later") | Paper avoids needing a calculator: \(T=\ln 2\) gives \(e^{-T}=\tfrac12\) |

**Sit it after the 26 Sep lecture.** Parts (a), (b) and the CCF step of (d) use only Weeks 5–6 material (Lect 1, Lect 2 §6–8). Part (c) (deadbeat, Lect 3 §12–13) and the observability half of (d) (Lect 3 §9–10) are taught on 26 Sep.

Collision check: none of the systems below appears in LPH Lect 1–3 examples (part (d) mirrors the *method* of Lect 3 Example 3.4, p. 6, but not its numbers: that example is \((z+0.2)/((z+0.8)(z+0.2))\)), the 2018-19 paper (A = diag(−10,−1); A = [[0,1],[1,0]]; deadbeat with \(e^{-T}\) entries) or the 2023 walkthroughs (A = diag(2,1); A = [[4,−1],[2,0]]; poles 0.9 ± j0.1).

---

## Question (25 marks)

**(a)** A continuous-time plant is
\(\dot{\mathbf x}(t)=\begin{bmatrix}-1&1\\0&-2\end{bmatrix}\mathbf x(t)+\begin{bmatrix}0\\1\end{bmatrix}u(t),\quad y(t)=\begin{bmatrix}1&0\end{bmatrix}\mathbf x(t)\).
It is driven through a ZOH and sampled with \(T=\ln 2\) s (so \(e^{-T}=\tfrac12,\ e^{-2T}=\tfrac14\)).
(i) Find \(\boldsymbol\Phi(T)\) and \(\boldsymbol\Theta(T)\) of the discretised model \(\mathbf x(k+1)=\boldsymbol\Phi(T)\mathbf x(k)+\boldsymbol\Theta(T)u(k)\). (ii) Where are the discrete-time poles? **(8 marks)**

**(b)** Find the pulse transfer function \(Y(z)/U(z)\) of the discretised model and confirm its poles agree with (a)(ii). **(5 marks)**

**(c)** (i) Show the discretised model is controllable. (ii) Design the deadbeat state-feedback gain \(\mathbf K\) (\(u(k)=-\mathbf K\mathbf x(k)\)) using Ackermann's formula. (iii) Verify the design from \(\mathbf x(0)=[1\ \ 0]^T\). **(6 marks)**

**(d)** \(G(z)=\dfrac{z-0.5}{z^2-0.1z-0.2}\). (i) Write its CCF by inspection. (ii) Test the controllability and observability of that realisation. (iii) Explain the result in terms of \(G(z)\). **(6 marks)**

---

## Key and rubric

### (a) — 8 marks · *Derivable*

\(s\mathbf I-\mathbf A=\begin{bmatrix}s+1&-1\\0&s+2\end{bmatrix}\Rightarrow[s\mathbf I-\mathbf A]^{-1}=\begin{bmatrix}\frac1{s+1}&\frac1{(s+1)(s+2)}\\0&\frac1{s+2}\end{bmatrix}\), and \(\frac1{(s+1)(s+2)}=\frac1{s+1}-\frac1{s+2}\).

\(\boldsymbol\Phi(t)=\begin{bmatrix}e^{-t}&e^{-t}-e^{-2t}\\0&e^{-2t}\end{bmatrix}\Rightarrow\boldsymbol\Phi(T)=\begin{bmatrix}\tfrac12&\tfrac14\\0&\tfrac14\end{bmatrix}\).

\(\boldsymbol\Theta(T)=\int_0^T\boldsymbol\Phi(\eta)\,d\eta\,\mathbf B=\begin{bmatrix}\int_0^T(e^{-\eta}-e^{-2\eta})d\eta\\\int_0^Te^{-2\eta}d\eta\end{bmatrix}=\begin{bmatrix}(1-e^{-T})-\tfrac12(1-e^{-2T})\\\tfrac12(1-e^{-2T})\end{bmatrix}=\begin{bmatrix}\tfrac18\\\tfrac38\end{bmatrix}\).

Poles: eigenvalues of the triangular \(\boldsymbol\Phi(T)\) → \(z=\tfrac12,\ \tfrac14\) (\(=e^{-T},e^{-2T}\), i.e. \(z=e^{sT}\) of \(s=-1,-2\)).

| Checkpoint | Marks |
|---|---:|
| \([s\mathbf I-\mathbf A]^{-1}\) correct (incl. partial fractions of the off-diagonal term) | 2 |
| \(\boldsymbol\Phi(t)\) by inverse Laplace, then \(\boldsymbol\Phi(T)\) numerically | 2 |
| \(\boldsymbol\Theta(T)\) set up as \(\int_0^T\boldsymbol\Phi(\eta)d\eta\,\mathbf B\) (only 2nd column of \(\boldsymbol\Phi\) needed) | 1 |
| \(\boldsymbol\Theta(T)=[1/8\ \ 3/8]^T\) | 2 |
| Poles \(1/2,\ 1/4\) with a reason (eigenvalues / \(e^{sT}\)) | 1 |

Common wrong paths: using \(\mathbf A\mathbf B T\) or \(\mathbf B T\) for \(\boldsymbol\Theta\) (Euler approximation, not ZOH-exact); integrating the first column of \(\boldsymbol\Phi\) (multiplying by \(\mathbf B\) selects column 2); writing \(\boldsymbol\Phi(T)=e^{\mathbf A}T\) or exponentiating entry-wise (\(e^{1}\) in the (1,2) slot) — the matrix exponential is not element-wise; sign slip giving \(\boldsymbol\Theta_1=\tfrac78\) (added instead of subtracted the \(e^{-2\eta}\) integral: \(\tfrac12+\tfrac38\)); poles quoted as \(-1,-2\) (continuous poles, not discrete).

### (b) — 5 marks · *Derivable*

\(z\mathbf I-\boldsymbol\Phi=\begin{bmatrix}z-\frac12&-\frac14\\0&z-\frac14\end{bmatrix},\ [z\mathbf I-\boldsymbol\Phi]^{-1}=\dfrac1{(z-\frac12)(z-\frac14)}\begin{bmatrix}z-\frac14&\frac14\\0&z-\frac12\end{bmatrix}\).

\(\dfrac{Y(z)}{U(z)}=\mathbf C[z\mathbf I-\boldsymbol\Phi]^{-1}\boldsymbol\Theta=\dfrac{\frac18(z-\frac14)+\frac14\cdot\frac38}{(z-\frac12)(z-\frac14)}=\dfrac{\frac z8+\frac1{16}}{(z-\frac12)(z-\frac14)}=\dfrac{2z+1}{16(z-\frac12)(z-\frac14)}=\dfrac{2z+1}{16z^2-12z+2}\).

Poles \(\tfrac12,\tfrac14\) = eigenvalues of \(\boldsymbol\Phi\) (no cancellation; zero at \(-\tfrac12\)). Sanity check: DC gain \(G(1)=\frac{3}{16\cdot\frac12\cdot\frac34}=\frac12\) equals the continuous DC gain \(-\mathbf C\mathbf A^{-1}\mathbf B=\frac12\) (ZOH preserves DC gain).

| Checkpoint | Marks |
|---|---:|
| Formula \(\mathbf C[z\mathbf I-\boldsymbol\Phi]^{-1}\boldsymbol\Theta\) (+\(D=0\)) stated | 1 |
| Correct \([z\mathbf I-\boldsymbol\Phi]^{-1}\) (adjugate / determinant) | 2 |
| Simplified \(G(z)\) | 1 |
| Pole agreement stated | 1 |

Common wrong paths: using \(\mathbf A\) (continuous) instead of \(\boldsymbol\Phi(T)\); adjugate without transposing/swapping (off-diagonal left in place with wrong sign); multiplying \(\boldsymbol\Theta\mathbf C\) in the wrong order.

### (c) — 6 marks · *Derivable* (Lect 3 §12–13; taught 26 Sep)

\(\boldsymbol\Phi\boldsymbol\Theta=[\tfrac5{32}\ \ \tfrac3{32}]^T\), \(\mathbf W_C=[\boldsymbol\Theta\ \ \boldsymbol\Phi\boldsymbol\Theta]=\begin{bmatrix}\frac18&\frac5{32}\\\frac38&\frac3{32}\end{bmatrix}\), \(|\mathbf W_C|=\frac3{256}-\frac{15}{256}=-\frac3{64}\neq0\) → controllable.

Deadbeat: \(\alpha_C(z)=z^2\Rightarrow\alpha_C(\boldsymbol\Phi)=\boldsymbol\Phi^2=\begin{bmatrix}\frac14&\frac3{16}\\0&\frac1{16}\end{bmatrix}\); \(\mathbf W_C^{-1}=\begin{bmatrix}-2&\frac{10}3\\8&-\frac83\end{bmatrix}\).

\(\mathbf K=[0\ \ 1]\mathbf W_C^{-1}\boldsymbol\Phi^2=[8\ \ -\tfrac83]\boldsymbol\Phi^2=[2\ \ \tfrac43]\).

Verify: \(\boldsymbol\Phi-\boldsymbol\Theta\mathbf K=\begin{bmatrix}\frac14&\frac1{12}\\-\frac34&-\frac14\end{bmatrix}\) (trace 0, det 0 ⇒ char. poly \(z^2\)); \(\mathbf x(1)=[\frac14\ \ -\frac34]^T,\ \mathbf x(2)=\mathbf 0\) — state reaches zero in \(n=2\) steps.

| Checkpoint | Marks |
|---|---:|
| \(\mathbf W_C\) formed and \(\lvert\mathbf W_C\rvert\neq0\) | 1 |
| \(\alpha_C(\boldsymbol\Phi)=\boldsymbol\Phi^2\) (deadbeat ⇒ all poles at 0) | 1 |
| \(\mathbf W_C^{-1}\) correct | 1 |
| \(\mathbf K=[2\ \ 4/3]\) | 2 |
| Verification (\(\mathbf x(2)=0\), or char. poly \(=z^2\)) | 1 |

Common wrong paths: \(\mathbf W_C=[\boldsymbol\Theta\ \ \boldsymbol\Phi^T\boldsymbol\Theta]\) or rows instead of columns; picking the *first* row of \(\mathbf W_C^{-1}\) (\([1\ 0]\) instead of \([0\ 1]\)); using \(\mathbf A+\mathbf B\mathbf K\) (the slides use \(u=-\mathbf K\mathbf x\), so the closed loop is \(\boldsymbol\Phi-\boldsymbol\Theta\mathbf K\)); expecting \(\mathbf x(1)=0\) — deadbeat needs up to \(n\) steps, not one.

### (d) — 6 marks · *Derivable*; part (iii) wording *convention-dependent*

(i) \(a_1=-0.1,\ a_0=-0.2,\ b_1=1,\ b_0=-0.5\) (LPH §6.3 layout):
\(\mathbf A_C=\begin{bmatrix}0&1\\0.2&0.1\end{bmatrix},\ \mathbf B_C=\begin{bmatrix}0\\1\end{bmatrix},\ \mathbf C_C=[-0.5\ \ 1],\ d_C=0\).

(ii) \(\mathbf W_C=[\mathbf B_C\ \ \mathbf A_C\mathbf B_C]=\begin{bmatrix}0&1\\1&0.1\end{bmatrix}\), \(|\mathbf W_C|=-1\neq0\) → controllable (always, for a CCF).
\(\mathbf C_C\mathbf A_C=[0.2\ \ -0.4]\), \(\mathbf W_O=\begin{bmatrix}-0.5&1\\0.2&-0.4\end{bmatrix}\), \(|\mathbf W_O|=0.2-0.2=0\) → **not observable**.

(iii) \(z^2-0.1z-0.2=(z-0.5)(z+0.4)\): the zero at 0.5 cancels the pole at 0.5, so \(G(z)=\frac1{z+0.4}\) is really first order. A 2-state realisation of it must lose controllability or observability (Lect 3 §10.1); the CCF keeps controllability, so the mode \(z=0.5\) is unobservable. (An OCF of the same \(G\) would be observable but uncontrollable.)

| Checkpoint | Marks |
|---|---:|
| CCF with coefficients in LPH's layout (bottom row \(-a_0,-a_1\); \(\mathbf C_C=[b_0\ b_1]\)) | 2 |
| Controllable (with \(\mathbf W_C\)) | 1 |
| \(\mathbf W_O\) and \(\lvert\mathbf W_O\rvert=0\) ⇒ unobservable | 2 |
| Pole–zero cancellation at 0.5 identified as the cause | 1 |

Common wrong paths: bottom row \([-0.2\ \ -0.1]\) or \([0.1\ \ 0.2]\) (sign/order of \(a_i\) flipped); \(\mathbf C_C=[1\ \ -0.5]\) (\(b\) order reversed); concluding "minimal/ both properties hold" after checking only controllability; cancelling first and writing a 1-state CCF — correct TF, but it answers a different question and loses (ii)/(iii).

---

## Total: 8 + 5 + 6 + 6 = **25 marks**

## Predicted novel item (label: prediction)

In-scope topics absent from circulating papers and most likely for an "unseen" part: **loss of controllability/observability due to sampling** (Lect 3 §10.2 — e.g. an undamped oscillator sampled at \(\omega T=\pi\)), and **similarity transformation to CCF with \(\mathbf P=\mathbf W_C\tilde{\mathbf W}_C^{-1}\)** (Lect 2 §6.1). Both are worth one practice pass before 5 Oct.
