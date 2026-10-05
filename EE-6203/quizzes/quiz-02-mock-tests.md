# EE6203 Quiz 2 — three mock tests: key and marking rubric

> **UNOFFICIAL.** Built 2026-10-05 from `quiz-02-intel.md`. Not an official paper, key or marking scheme.
> Exam page (answer-free): `quiz-02-mock-tests.html`. Every key below is asserted by `python3 quiz-02-mock-tests-check.py`.
> Open this file only after sitting a test.

## Provenance

| Test | Basis | Numbers | Status |
|---|---|---|---|
| **A** | AY24/25 S2 sitting (Passion阳, RedNote, Mar 2025): Q1 physical system + block diagram; Q2 discretise, controllability, TF "by formula"; Q3 deadbeat K + show deadbeat | New | Predicted |
| **B** | AY25/26 S1 sitting (yzmyyds GitHub recall, Sep 2025): ODE `5ÿ−2ẏ=2u`; β-system T=0.5 with X(z)/U(z); x(2) with inputs | **As recalled** | Reconstructed (wording approximate). Q3(ii)–(iii) deadbeat **added** because this year's scope reaches Ex 3.13 |
| **C** | AY25/26 S2 sitting (undertaker, RedNote, Mar 2026): block diagram; discretise + controllability **and** observability; fractional deadbeat K then x(3) | New | Predicted. Q2(iii) (sampling-period loss, Lect 3 §10.2 / Ex 3.6 method with ω=2) and Q3(iii) (zeros under feedback, §12) are predicted extensions |

Conditions (official, LPH 26 Sep, `resources/week-07-transcript.txt`): 45 min, no MCQ, closed book, no formula sheet, transform table supplied, own calculator. The mark split (Q1 8 / Q2 10 / Q3 7 = 25) is **estimated**; no recall gives it.

Collision check: Test A's systems were changed after a grep found the first draft repeated `notes/quiz2-prep-learning.html` (Module 3 servo at T=0.5 and the `[[0,1],[-2,-3]]` self-check). None of the systems below appears in the companion, `quiz-02-prediction-paper.*`, or the LPH Lect 1–3 worked examples checked by the companion. Test C Q2 reuses the **method** of Lect 3 Ex 3.6 (harmonic oscillator), not its numbers.

Conventions (LPH): \(\mathbf x(k+1)=\mathbf\Phi\mathbf x(k)+\mathbf\Theta u(k)\); \(\mathbf\Theta(T)=\int_0^T\mathbf\Phi(\eta)\,d\eta\,\mathbf B\); \(u=-\mathbf K\mathbf x\); \(\mathbf W_C=[\mathbf\Theta\ \ \mathbf\Phi\mathbf\Theta]\), \(\mathbf W_O=\begin{bmatrix}\mathbf C\\\mathbf C\mathbf\Phi\end{bmatrix}\); Ackermann \(\mathbf K=[0\ \ 1]\mathbf W_C^{-1}\alpha_C(\mathbf\Phi)\), deadbeat \(\alpha_C(z)=z^2\).

---

# Test A (predicted)

## A-Q1 — 8 marks · *Derivable*

**(i)** KVL: \(L\,\dot i+Ri+v_C=e\); capacitor: \(C\dot v_C=i\). With \(x_1=v_C,\ x_2=i\):
\(\dot x_1=\tfrac1C x_2=3x_2,\quad \dot x_2=-\tfrac1L x_1-\tfrac RL x_2+\tfrac1L e=-x_1-4x_2+e\).

\(\mathbf A=\begin{bmatrix}0&3\\-1&-4\end{bmatrix},\ \mathbf B=\begin{bmatrix}0\\1\end{bmatrix},\ \mathbf C=[1\ \ 0],\ D=0.\)

**(ii)** Block \(1/s\): \(\dot x_1=x_2\). Block \(3/(s+4)\) with input \(u-x_1\): \(\dot x_2=-4x_2+3(u-x_1)\).

\(\mathbf A=\begin{bmatrix}0&1\\-3&-4\end{bmatrix},\ \mathbf B=\begin{bmatrix}0\\3\end{bmatrix},\ \mathbf C=[1\ \ 0].\)

**(iii)** Both: \(\det(s\mathbf I-\mathbf A)=s^2+4s+3\), \(\mathbf C\,\mathrm{adj}(s\mathbf I-\mathbf A)\,\mathbf B=3\), so
\(G(s)=\dfrac{3}{s^2+4s+3}=\dfrac{3}{(s+1)(s+3)}\) for both. Same transfer function, different states: \(x_1\) is the same, and \(x_2^{(ii)}=\dot x_1=3x_2^{(i)}\). So the models are related by the similarity transform \(\mathbf P=\mathrm{diag}(1,3)\). A state-space realisation is not unique (Lect 2 §5).

| Checkpoint | Marks |
|---|---:|
| (i) two physical laws written correctly | 1 |
| (i) A, B, C | 2 |
| (ii) each block's ODE from its input | 1 |
| (ii) A, B, C | 2 |
| (iii) both TFs = 3/((s+1)(s+3)) | 1 |
| (iii) comment: same TF, non-unique realisation / similarity | 1 |

Wrong paths: \(\dot x_1=i\) (forgot the \(1/C=3\) factor), so the (1,2) entry is 1; minus sign lost on the feedback (\(+3x_1\)); the gain 3 placed in \(\mathbf C\) instead of \(\mathbf B\) (the state at the block output absorbs the gain only if you label it that way, and the diagram fixes the labels).

## A-Q2 — 10 marks · *Derivable*

**(i)** \((s\mathbf I-\mathbf A)^{-1}=\begin{bmatrix}\frac1{s+1}&0\\\frac1{(s+1)(s+2)}&\frac1{s+2}\end{bmatrix}\), and \(\frac1{(s+1)(s+2)}=\frac1{s+1}-\frac1{s+2}\).

\(\mathbf\Phi(t)=\begin{bmatrix}e^{-t}&0\\e^{-t}-e^{-2t}&e^{-2t}\end{bmatrix}\Rightarrow\mathbf\Phi(0.5)=\begin{bmatrix}0.6065&0\\0.2387&0.3679\end{bmatrix}.\)

\(\mathbf B=[1\ 0]^T\) selects **column 1**:
\(\mathbf\Theta=\begin{bmatrix}1-e^{-T}\\(1-e^{-T})-\tfrac12(1-e^{-2T})\end{bmatrix}=\begin{bmatrix}0.3935\\0.0774\end{bmatrix}.\)

**(ii)** \(\mathbf\Phi\mathbf\Theta=[0.2387\ \ 0.1224]^T\); \(\mathbf W_C=\begin{bmatrix}0.3935&0.2387\\0.0774&0.1224\end{bmatrix}\), \(\det=0.0297\neq0\) → controllable.

**(iii)** Route 1 (formula): \((z\mathbf I-\mathbf\Phi)^{-1}=\frac{1}{(z-0.6065)(z-0.3679)}\begin{bmatrix}z-0.3679&0\\0.2387&z-0.6065\end{bmatrix}\). With \(\mathbf C=[0\ 1]\):
\(G(z)=\dfrac{0.2387(0.3935)+(z-0.6065)(0.0774)}{(z-0.6065)(z-0.3679)}=\dfrac{0.0774z+0.0470}{(z-0.6065)(z-0.3679)}\).
Poles \(0.6065=e^{-0.5},\ 0.3679=e^{-1}\) (the images \(e^{sT}\) of \(s=-1,-2\)). The zero is at \(-0.6065\).

Route 2 (table): \(G(s)=\frac1{(s+1)(s+2)}\), \(\frac{G(s)}{s}=\frac{1/2}{s}-\frac1{s+1}+\frac{1/2}{s+2}\), so
\(G(z)=(1-z^{-1})\left[\tfrac12\tfrac{z}{z-1}-\tfrac{z}{z-e^{-T}}+\tfrac12\tfrac{z}{z-e^{-2T}}\right]\), which equals Route 1 (asserted in the script). Check: \(G(1)=0.5=G(0)\), since a ZOH keeps the DC gain.

| Checkpoint | Marks |
|---|---:|
| \((s\mathbf I-\mathbf A)^{-1}\) incl. partial fractions | 1 |
| \(\mathbf\Phi(t)\) and \(\mathbf\Phi(0.5)\) | 2 |
| \(\mathbf\Theta\) set up from column 1, integrated | 2 |
| \(\mathbf W_C\), det ≠ 0, conclusion | 2 |
| \(G(z)\) correct (either route) | 2 |
| Poles stated | 1 |

Wrong paths: integrating column 2 (that is \(\mathbf B=[0\ 1]^T\)); \(\mathbf\Theta\approx\mathbf BT\) (Euler, not ZOH); using \(\mathbf C=[1\ 0]\) by habit (this plant measures \(x_2\)); continuous poles \(-1,-2\) quoted as discrete poles; adjugate entries not swapped.

## A-Q3 — 7 marks · *Derivable* (K fractional, matching the 2026 S2 "fractional K" comment)

\(\mathbf\Phi\mathbf\Theta=[1.5\ \ 0.5]^T\), \(\mathbf W_C=\begin{bmatrix}\frac12&\frac32\\1&\frac12\end{bmatrix}\), \(\det=-\frac54\), \(\mathbf W_C^{-1}=\begin{bmatrix}-\frac25&\frac65\\\frac45&-\frac25\end{bmatrix}\).
\(\mathbf\Phi^2=\begin{bmatrix}1&\frac32\\0&\frac14\end{bmatrix}\). \(\mathbf K=[\tfrac45\ \ -\tfrac25]\,\mathbf\Phi^2=[\tfrac45\ \ \tfrac{11}{10}]\).

Alternative: match \(\det(z\mathbf I-\mathbf\Phi+\mathbf\Theta\mathbf K)=z^2\) coefficient by coefficient. It gives the same K.

**(ii)** \(\mathbf\Phi-\mathbf\Theta\mathbf K=\begin{bmatrix}\frac35&\frac{9}{20}\\-\frac45&-\frac35\end{bmatrix}\) (trace 0, det 0). \(\mathbf x(1)=[\tfrac{21}{20}\ \ -\tfrac75]^T\), \(\mathbf x(2)=\mathbf 0\). The state reaches zero in \(n=2\) steps and stays there.

| Checkpoint | Marks |
|---|---:|
| \(\mathbf W_C\), det ≠ 0 | 1 |
| \(\alpha_C(\mathbf\Phi)=\mathbf\Phi^2\) | 1 |
| \(\mathbf W_C^{-1}\) | 1 |
| \(\mathbf K=[4/5\ \ 11/10]\) | 2 |
| \(\mathbf x(1)\), \(\mathbf x(2)=0\) | 2 |

Wrong paths: first row of \(\mathbf W_C^{-1}\) instead of the last; closed loop written \(\mathbf\Phi+\mathbf\Theta\mathbf K\); expecting \(\mathbf x(1)=0\).

---

# Test B (reconstructed from the Sep 2025 recall)

## B-Q1 — 8 marks · *Derivable*

Normalise: \(\ddot y=0.4\dot y+0.4u\). \(\dot x_1=x_2,\ \dot x_2=0.4x_2+0.4u\):
\(\mathbf A=\begin{bmatrix}0&1\\0&0.4\end{bmatrix},\ \mathbf B=\begin{bmatrix}0\\0.4\end{bmatrix},\ y=[1\ \ 0]\mathbf x.\)
\(\dfrac{Y(s)}{U(s)}=\dfrac{2}{5s^2-2s}=\dfrac{0.4}{s(s-0.4)}\). It has a pole at the origin and an unstable pole at \(+0.4\).

| Checkpoint | Marks |
|---|---:|
| Divide by 5 (normalise) | 1 |
| \(\mathbf A\) (sign of 0.4 correct) | 2 |
| \(\mathbf B\), output equation | 2 |
| TF (Laplace of ODE or \(\mathbf C(s\mathbf I-\mathbf A)^{-1}\mathbf B\)) | 3 |

Wrong paths: \(-0.4\) in \(\mathbf A\) (the ODE has \(-2\dot y\) on the left, so it moves across as \(+0.4\)); \(\mathbf B=[0\ 2]^T\) (not normalised).

## B-Q2 — 10 marks · *Derivable*

**(i)** \((s\mathbf I-\mathbf A)^{-1}=\begin{bmatrix}\frac1{s-1}&\frac{\beta}{(s-1)(s-2)}\\0&\frac1{s-2}\end{bmatrix}\), \(\frac{\beta}{(s-1)(s-2)}=\beta\left(\frac1{s-2}-\frac1{s-1}\right)\).
\(\mathbf\Phi(t)=\begin{bmatrix}e^t&\beta(e^{2t}-e^t)\\0&e^{2t}\end{bmatrix}\Rightarrow\mathbf\Phi(0.5)=\begin{bmatrix}1.6487&1.0696\beta\\0&2.7183\end{bmatrix}.\)
Column 2: \(\mathbf\Theta=\begin{bmatrix}\beta\left[\tfrac12(e^{2T}-1)-(e^{T}-1)\right]\\\tfrac12(e^{2T}-1)\end{bmatrix}=\begin{bmatrix}0.2104\beta\\0.8591\end{bmatrix}.\)

**(ii)** \(\mathbf X(z)/U(z)=(z\mathbf I-\mathbf\Phi)^{-1}\mathbf\Theta\). This is the state vector, not \(Y\):
\[\frac{\mathbf X(z)}{U(z)}=\begin{bmatrix}\dfrac{\beta(0.2104z+0.3469)}{(z-1.6487)(z-2.7183)}\\[2mm]\dfrac{0.8591}{z-2.7183}\end{bmatrix}.\]
(Numerator of row 1: \((z-2.7183)(0.2104\beta)+1.0696\beta(0.8591)\).)

**(iii)** \(\mathbf\Phi\mathbf\Theta=[1.2658\beta\ \ 2.3354]^T\); \(\det\mathbf W_C=0.2104\beta(2.3354)-0.8591(1.2658\beta)=-0.596\beta\).
Exactly, \(\det\mathbf W_C=-\beta\cdot\tfrac12(e^{2T}-1)(e^{2T}-e^{T})(e^{T}-1)\). Controllable **iff \(\beta\neq0\)**. At \(\beta=0\), \(x_1\) is decoupled from \(u\), so the mode \(z=e^{0.5}\) can't be reached. You can see it in (ii): \(X_1/U\equiv0\).

| Checkpoint | Marks |
|---|---:|
| \(\mathbf\Phi(t)\) incl. the β partial fraction | 2 |
| \(\mathbf\Phi(0.5)\) numerically | 1 |
| \(\mathbf\Theta\) | 2 |
| \((z\mathbf I-\mathbf\Phi)^{-1}\) and both rows of X/U | 3 |
| \(\det\mathbf W_C\propto\beta\) → lost only at β = 0, with reason | 2 |

Wrong paths: answering with \(Y(z)/U(z)\) only (the recall asks for \(\mathbf X\)); concluding "never controllable" or "always controllable" without isolating β; numeric slip \(e^{0.5}\approx1.6487\), \(e\approx2.7183\).

## B-Q3 — 7 marks · *Derivable*

**(i)** \(\mathbf x(1)=\mathbf A\mathbf x(0)+\mathbf Bu(0)=[3\ \ -3]^T+[1\ \ 1]^T=[4\ \ -2]^T\);
\(\mathbf x(2)=\mathbf A\mathbf x(1)+\mathbf Bu(1)=[3\ \ 0]^T-[1\ \ 1]^T=[2\ \ -1]^T\).

**(ii)** *(added)* \(\mathbf W_C=[\mathbf B\ \ \mathbf A\mathbf B]=\begin{bmatrix}1&\frac32\\1&-\frac32\end{bmatrix}\), \(\det=-3\), \(\mathbf W_C^{-1}=\begin{bmatrix}\frac12&\frac12\\\frac13&-\frac13\end{bmatrix}\).
\(\mathbf A^2=\tfrac34\mathbf I\) (Cayley–Hamilton: the characteristic polynomial is \(z^2-\tfrac34\)). \(\mathbf K=[\tfrac13\ \ -\tfrac13]\cdot\tfrac34\mathbf I=[\tfrac14\ \ -\tfrac14]\).

**(iii)** \(\mathbf A-\mathbf B\mathbf K=\begin{bmatrix}\frac34&\frac34\\-\frac34&-\frac34\end{bmatrix}\): trace 0, det 0, so the characteristic polynomial is \(z^2\).

| Checkpoint | Marks |
|---|---:|
| \(\mathbf x(1)\) | 1 |
| \(\mathbf x(2)\) with \(u(1)=-1\) | 2 |
| \(\mathbf W_C^{-1}\), \(\mathbf A^2\) | 1 |
| \(\mathbf K=[1/4\ \ -1/4]\) | 2 |
| Char. poly \(z^2\) shown | 1 |

Wrong paths: using \(u(0)\) again at step 2; computing \(\mathbf x(2)=\mathbf A^2\mathbf x(0)\) and forgetting the input terms \(\mathbf A\mathbf Bu(0)+\mathbf Bu(1)\).

---

# Test C (predicted)

## C-Q1 — 8 marks · *Derivable*

\(x_2\) is the output of \(\frac1{s+1}\), whose input is \(u-2y=u-2x_1\): \(\dot x_2=-x_2-2x_1+u\).
\(x_1\) is the output of \(\frac3{s+2}\), whose input is \(x_2\): \(\dot x_1=-2x_1+3x_2\).
\(\mathbf A=\begin{bmatrix}-2&3\\-2&-1\end{bmatrix},\ \mathbf B=\begin{bmatrix}0\\1\end{bmatrix},\ \mathbf C=[1\ \ 0].\)
\(\det(s\mathbf I-\mathbf A)=(s+2)(s+1)+6=s^2+3s+8\), \(\mathbf C\,\mathrm{adj}\,\mathbf B=3\), so \(\dfrac{Y}{U}=\dfrac{3}{s^2+3s+8}\).
Check by block algebra: \(\frac{F}{1+2F}\) with \(F=\frac{3}{(s+1)(s+2)}\).

| Checkpoint | Marks |
|---|---:|
| Each block → first-order ODE (\(\dot x=-ax+k\cdot\)input) | 2 |
| Junction signal \(u-2x_1\) with the gain 2 | 1 |
| A, B, C | 3 |
| TF | 2 |

Wrong paths: feedback gain dropped (−1 instead of −2 in \(a_{21}\)); the 3 put in \(\mathbf C\); signs flipped in the summing junction.

## C-Q2 — 10 marks · *Derivable*; (iii) *predicted*

**(i)** \(\det(s\mathbf I-\mathbf A)=s^2+4\), so \(\mathbf\Phi(t)=\begin{bmatrix}\cos2t&\frac12\sin2t\\-2\sin2t&\cos2t\end{bmatrix}\) (table: \(\frac{\omega}{s^2+\omega^2},\frac{s}{s^2+\omega^2}\)).
At \(T=\pi/4\): \(\mathbf\Phi=\begin{bmatrix}0&\frac12\\-2&0\end{bmatrix}\), \(\mathbf\Theta=\begin{bmatrix}\frac14(1-\cos2T)\\\frac12\sin2T\end{bmatrix}=\begin{bmatrix}\frac14\\\frac12\end{bmatrix}\).

**(ii)** \(\mathbf W_C=\begin{bmatrix}\frac14&\frac14\\\frac12&-\frac12\end{bmatrix}\), \(\det=-\tfrac14\neq0\) → controllable. \(\mathbf W_O=\begin{bmatrix}1&0\\0&\frac12\end{bmatrix}\), \(\det=\tfrac12\neq0\) → observable.

**(iii)** In general, with \(c=\cos2T,\ s=\sin2T\): \(\det\mathbf W_C=-\tfrac14 s(1-c)=-\sin^3T\cos T\) and \(\det\mathbf W_O=\tfrac12\sin2T\).
Both vanish exactly when \(\sin 2T=0\), i.e. **\(T=k\pi/2,\ k=1,2,\dots\)**, or \(\omega T=k\pi\) with \(\omega=2\). At those periods the samples land at the same phase of the oscillation, so the sampled model can't see or steer it. This is the Lect 3 §10.2 / Ex 3.6 result. The continuous plant is controllable and observable, so sampling is the only way to lose these properties.

| Checkpoint | Marks |
|---|---:|
| \(\mathbf\Phi(t)\) via table | 2 |
| \(\mathbf\Phi(\pi/4)\), \(\mathbf\Theta\) | 2 |
| \(\mathbf W_C\) test | 1.5 |
| \(\mathbf W_O\) test | 1.5 |
| (iii) det as a function of T, \(T=k\pi/2\) | 3 |

Wrong paths: \(\mathbf\Phi(t)=\begin{bmatrix}\cos2t&\sin2t\\-\sin2t&\cos2t\end{bmatrix}\) (dropped the \(\omega\) scalings \(1/2\) and \(2\)); radians vs degrees on the calculator; answering \(T=k\pi\) (that is \(\omega T=2k\pi\), half the true set).

## C-Q3 — 7 marks · *Derivable*; (iii) *predicted*

**(i)** \(\mathbf\Phi\mathbf\Theta=[\tfrac12\ \ 2]^T\), \(\mathbf W_C=\begin{bmatrix}1&\frac12\\1&2\end{bmatrix}\), \(\det=\tfrac32\), \(\mathbf W_C^{-1}=\begin{bmatrix}\frac43&-\frac13\\-\frac23&\frac23\end{bmatrix}\).
\(\mathbf\Phi^2=\begin{bmatrix}\frac14&0\\\frac32&1\end{bmatrix}\), so \(\mathbf K=[-\tfrac23\ \ \tfrac23]\mathbf\Phi^2=[\tfrac56\ \ \tfrac23]\).

**(ii)** \(\mathbf\Phi-\mathbf\Theta\mathbf K=\begin{bmatrix}-\frac13&-\frac23\\\frac16&\frac13\end{bmatrix}\). \(\mathbf x(1)=[-1\ \ \tfrac12]^T\), \(\mathbf x(2)=\mathbf 0\), so **\(\mathbf x(3)=\mathbf 0\)**. A deadbeat second-order system is at rest after 2 steps, so you don't need to iterate a third time. Showing \(\mathbf x(2)=0\) is the proof.

**(iii)** Open loop: \(\dfrac{Y}{U}=\dfrac{z+\frac12}{(z-\frac12)(z-1)}\). Closed loop: \(\dfrac{Y}{V}=\mathbf C(z\mathbf I-\mathbf\Phi+\mathbf\Theta\mathbf K)^{-1}\mathbf\Theta=\dfrac{z+\frac12}{z^2}\).
The poles move to 0 and the **zero stays at \(-\tfrac12\)**: state feedback moves poles, not zeros (Lect 3 §12).

| Checkpoint | Marks |
|---|---:|
| \(\mathbf W_C^{-1}\), \(\mathbf\Phi^2\) | 1 |
| \(\mathbf K=[5/6\ \ 2/3]\) | 2 |
| \(\mathbf x(1)\), \(\mathbf x(2)=0\Rightarrow\mathbf x(3)=0\) | 2 |
| Both TFs, zero unchanged | 2 |

Wrong paths: iterating with the open-loop \(\mathbf\Phi\) instead of \(\mathbf\Phi-\mathbf\Theta\mathbf K\); thinking feedback cancels or moves the zero.

---

## Totals

Each test: Q1 8 + Q2 10 + Q3 7 = **25 marks** (split estimated).
