# EE6203 Quiz 3 — Mock A: questions, key and marking rubric

**Unofficial practice paper.** Built from C. Wen's Ch 4–6 notes and the topic pattern in `quiz-03-intel.md`. It is not a recalled paper. Conditions to practise under: 45 min, closed book, calculator, workings on paper. **Total 30 marks** (Q1 10 + Q2 10 + Q3 10). Every number is checked by `quiz-03-check.py`.

Sources: `resources/lecture-notes-weeks-01-04.pdf` (Ch 4, PDF pp. 164–166 Jury, 186–187 error constants); `resources/lecture-notes-chapters-05-06.pdf` (PDF pp. 7–8 bilinear, 14–15 pole-zero matching, 23 w-plane, 29 compensators, 49–56 direct design, 64–65 deadbeat, 73–82 ripple-free, 84 1-DOF, 89–93 pole placement, 104–110 direct/standard programming).

---

## Q1 (10 marks)

### (a) True or False? Give a one-line reason for each. (6 × 1 mark)

1. The transformation \(w=\frac{2}{T}\frac{z-1}{z+1}\) maps the inside of the unit circle in the z-plane onto the entire left half of the w-plane.
2. A phase-lag compensator is the right choice when the main goal is to widen the bandwidth and speed up the response.
3. For \(G_{ZAS}(z)=\dfrac{0.2\,z^{-3}(1+0.5z^{-1})}{(1-0.6z^{-1})(1-0.3z^{-1})}\), the deadbeat choice is \(G_{cl}(z)=z^{-3}\).
4. Standard programming of a controller with 3 poles and 2 zeros needs 5 delay elements.
5. In the 1-DOF loop, \(S(z)+T(z)=1\), so set-point tracking and disturbance rejection cannot be shaped independently.
6. In the pole-placement design with \(T_1=1\), feedback can move an unstable ("bad") zero of the plant to a better location.

### (b) Jury test (4 marks)

A unity-feedback loop with gain \(K\) and \(T=0.2\) s has closed-loop characteristic polynomial
\(P(z)=z^2-(1.6-0.4K)z+(0.6+0.2K)\).
(i) Find the range of \(K\) for stability. (ii) At the upper limit, where are the closed-loop poles, and at what frequency (rad/s) does the output oscillate?

### Key

(a)
1. **True.** \(|z|<1\) gives \(\operatorname{Re}w<0\) (p. 23).
2. **False.** Lead widens the bandwidth and speeds the response. Lag reduces the bandwidth and raises low-frequency gain, which improves steady-state accuracy (p. 29).
3. **True.** \(z^{-3}(1+0.5z^{-1})=\frac{z+0.5}{z^4}\) and the denominator is \(\frac{(z-0.6)(z-0.3)}{z^2}\), so \(G=\frac{0.2(z+0.5)}{z^2(z-0.6)(z-0.3)}\). Relative degree = 4 − 1 = 3. All poles and zeros are inside the unit circle, so \(m=3\) (pp. 64–65).
4. **False.** Standard programming needs \(n=3\) delays. Direct programming needs \(n+m=5\) (pp. 107, 110).
5. **True** (p. 84).
6. **False.** \(G_Y=\gamma z^{-k}B^b/\phi_{cl}\): bad zeros stay (p. 93).

(b) The Jury conditions for \(n=2\) are the first three (p. 166):
- \(|0.6+0.2K|<1\) gives \(-8<K<2\).
- \(P(1)=1-1.6+0.4K+0.6+0.2K=0.6K>0\) gives \(K>0\).
- \(P(-1)=1+1.6-0.4K+0.6+0.2K=3.2-0.2K>0\) (n even) gives \(K<16\).

So **\(0<K<2\)**. At \(K=2\): \(P=z^2-0.8z+1\), so the poles are \(z=0.4\pm j0.9165\) with \(|z|=1\) and \(\angle z=\pm\cos^{-1}0.4=\pm1.159\) rad. The output oscillates at \(\omega=\theta/T=1.159/0.2\approx\mathbf{5.80}\) rad/s.

### Rubric Q1 (10)
- (a) 1 mark per item. Award it only when both the T/F and the reason are right. A correct T/F with a wrong or missing reason gets ½.
- (b) 1: condition \(|a_2|<a_0\) applied correctly. 1: \(P(1)>0\) and \(P(-1)>0\) with the correct sign rule for n even. 1: intersection \(0<K<2\). 1: poles on the unit circle and \(\omega\approx5.8\) rad/s.

### Common wrong paths
- Using \(P(-1)<0\): that rule is for odd \(n\) only. Here n = 2, so it would flip the bound.
- Stopping at \(K<16\): the binding condition is \(|a_2|<a_0\), not \(P(-1)\).
- Giving the oscillation frequency as \(\theta\) (rad/sample) without dividing by \(T\).
- Item 3: counting only the explicit \(z^{-3}\) and forgetting the denominator's \(z^{-2}\) normalisation (getting m = 4 or 5), or ignoring the numerator zero (getting m = 4).
- Item 4: quoting the direct-programming count.

---

## Q2 (10 marks)

An analog lead controller \(C(s)=\dfrac{5(s+2)}{s+10}\) is to run at \(T=0.1\) s.

(a) Find \(C(z)\) by the bilinear transformation \(s=\frac{2}{T}\frac{z-1}{z+1}\). Check its DC gain. (4)
(b) Find the pole-zero matched \(C(z)\) with the gain matched at DC. Compare its gain at \(z=-1\) with that of (a). (3)
(c) Write \(C(z)\) from (a) in the form (6.1) and give the standard-programming difference equations. How many delay elements are needed, and how many would direct programming need? (3)

### Key
(a) \(s=20\frac{z-1}{z+1}\), so
\(C(z)=5\,\frac{20(z-1)+2(z+1)}{20(z-1)+10(z+1)}=5\,\frac{22z-18}{30z-10}=\mathbf{\frac{11z-9}{3z-1}}=\frac{11}{3}\,\frac{z-0.8182}{z-0.3333}\).
DC check: \(C(1)=2/2=1=C(s)|_{s=0}=5\cdot2/10\). ✓

(b) There is one pole and one zero, so \(n-m=0\) and no zeros at −1 are added (p. 14). Zero \(e^{-2T}=e^{-0.2}=0.8187\); pole \(e^{-10T}=e^{-1}=0.3679\).
\(C(z)=\alpha\frac{z-0.8187}{z-0.3679}\). Setting \(C(1)=1\) gives \(\alpha=\frac{1-0.3679}{1-0.8187}=\mathbf{3.487}\).
Gain at \(z=-1\) (the folding frequency): bilinear gives \((-20)/(-4)=5\), which equals \(C(s\to\infty)=5\) exactly. Pole-zero matching gives \(3.487\cdot1.8187/1.3679\approx4.64\). The two mappings agree at DC and differ near \(\omega_s/2\).

(c) \(C(z)=\dfrac{\tfrac{11}{3}-3z^{-1}}{1-\tfrac13 z^{-1}}\), so \(b_0=11/3\), \(b_1=-3\), \(a_1=-1/3\).
Standard programming (6.5–6.6):
\(h(k)=e(k)+\tfrac13 h(k-1)\),
\(u(k)=\tfrac{11}{3}h(k)-3h(k-1)\).
This needs **1** delay element. Direct programming, \(u(k)=\tfrac13u(k-1)+\tfrac{11}{3}e(k)-3e(k-1)\), needs **2**.

### Rubric Q2 (10)
- (a) 1: substitution with \(2/T=20\). 2: correct simplification to \((11z-9)/(3z-1)\) or an equivalent. 1: DC check stated.
- (b) 1: mapped zero and pole \(e^{-0.2}\), \(e^{-1}\) with no extra \((z+1)\). 1: \(\alpha\) from DC matching. 1: the z = −1 comparison.
- (c) 1: (6.1) form with signs right. 1: both difference equations. 1: delay counts 1 vs 2.

### Common wrong paths
- Using \(T/2\) instead of \(2/T\), or \(s=\frac{2}{T}\frac{z+1}{z-1}\) (an inverted map): the DC check then fails, so always do it.
- Adding a \((z+1)\) factor in (b): that applies only when \(n>m\).
- Writing \(h(k)=e(k)-\tfrac13h(k-1)\): (6.6) is \(H=X-a_1z^{-1}H\) with \(a_1=-1/3\), so the sign flips to \(+\).
- Leaving \(C(z)\) in powers of \(z\) and reading the coefficients off as if it were (6.1).

---

## Q3 (10 marks)

A type-1 plant \(G(s)=\dfrac{3}{s(s+3)}\) is driven through a ZOH with \(T=0.2\) s.

(a) Show that \(G_{ZAS}(z)=\dfrac{0.04960(z+0.8192)}{(z-1)(z-0.5488)}\). State \(n\) and the relative degree. (3)
(b) Design a **ripple-free** deadbeat controller for a unit-step reference: choose \(G_{cl}(z)\) and find its gain. (3)
(c) Find \(C(z)\). (2)
(d) List \(u(k)\) and \(y(k)\) for \(k=0,1,2,3\). In one sentence, explain why the plain deadbeat choice \(G_{cl}=z^{-1}\) would ripple. (2)

### Key
(a) \(G_{ZAS}=(1-z^{-1})\mathcal Z\{3/(s^2(s+3))\}\). Partial fractions: \(\frac{3}{s^2(s+3)}=\frac1{s^2}-\frac{1/3}{s}+\frac{1/3}{s+3}\).
\(\mathcal Z\): \(\frac{Tz}{(z-1)^2}-\frac13\frac{z}{z-1}+\frac13\frac{z}{z-e^{-0.6}}\). Multiplying by \((z-1)/z\) and combining gives
numerator \(\frac{1}{3}[(aT-1+e^{-aT})z+(1-e^{-aT}-aTe^{-aT})]\) with \(aT=0.6\), \(e^{-0.6}=0.5488\):
\(\frac13[0.1488z+0.1219]=0.04960z+0.04063=0.04960(z+0.8192)\).
So \(G_{ZAS}=\frac{0.04960(z+0.8192)}{(z-1)(z-0.5488)}\), with \(n=2\) and relative degree 1. In \(z^{-1}\) form: \(\frac{0.04960z^{-1}(1+0.8192z^{-1})}{(1-z^{-1})(1-0.5488z^{-1})}\).

(b) From (5.13), \(U(z)=G_{cl}\frac{R}{G_{ZAS}}=G_{cl}\,\frac{(1-0.5488z^{-1})}{0.04960\,z^{-1}(1+0.8192z^{-1})}\). The \((1-z^{-1})\) from \(R\) cancels the plant integrator. For \(U(z)\) to be a finite polynomial (and \(u(k)=0\) for \(k\ge n=2\), since the plant is type 1), \(G_{cl}\) must contain the delay \(z^{-1}\) and the zero factor \((1+0.8192z^{-1})\):
\(G_{cl}=K z^{-1}(1+0.8192z^{-1})\). Setting \(G_{cl}(1)=1\) gives \(K=1/1.8192=\mathbf{0.5497}\).

(c) \(1-G_{cl}=\frac{z^2-0.5497z-0.4503}{z^2}=\frac{(z-1)(z+0.4503)}{z^2}\). Then
\(C=\frac{G_{cl}}{G_{ZAS}(1-G_{cl})}=\mathbf{11.08\,\frac{z-0.5488}{z+0.4503}}\) (gain \(K/0.04960\)). Equivalently \(\frac{11.08(1-0.5488z^{-1})}{1+0.4503z^{-1}}\).

(d) \(U(z)=\frac{K}{0.0496}(1-0.5488z^{-1})=11.08-6.08z^{-1}\), so **u = 11.08, −6.08, 0, 0**.
\(Y=G_{cl}R\): **y = 0, 0.5497, 1, 1**. Check: \(y(1)=K\), and \(y(k)=1\) from \(k=2\) on.
Plain deadbeat \(G_{cl}=z^{-1}\) gives \(C=\frac{1}{0.0496}\frac{z-0.5488}{z+0.8192}\). This cancels the plant zero at −0.819, which is close to −1, so \(u(k)\) alternates in sign, decaying only by a factor of 0.819 per step (20.2, −27.6, 22.6, …). The output therefore oscillates between samples.

### Rubric Q3 (10)
- (a) 1: partial fractions. 1: z-transforms with \(e^{-0.6}\). 1: final form, plus \(n=2\) and relative degree 1.
- (b) 1: uses (5.13) and the type-1 argument for \(u(k)=0\), \(k\ge2\). 1: \(G_{cl}\) contains \(z^{-1}\) and the plant zero. 1: \(K=0.5497\).
- (c) 1: factor \(1-G_{cl}\). 1: \(C(z)\) with the pole at −0.4503 and gain 11.08.
- (d) 1: both sequences. 1: ripple explanation naming the cancelled zero near −1.

### Common wrong paths
- Using \(\mathcal Z\{G(s)\}\) instead of \((1-z^{-1})\mathcal Z\{G(s)/s\}\) (omitting the ZOH).
- Ripple-free \(G_{cl}\) without the plant zero factor: you are back to the plain deadbeat design and get ripple.
- Making \(u(k)\) a non-zero constant: that is the type-0 case (Ex 5.12, which needs an integrator in \(C\)). For a type-1 plant, \(u\to0\).
- \(K=1/0.8192\): \(G_{cl}(1)=K(1+0.8192)\), not \(K\cdot0.8192\).
- Arithmetic check: \(C\) should have no factor \((z-1)\) here, because the plant already supplies the integrator.
