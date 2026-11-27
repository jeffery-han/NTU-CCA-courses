# EE6203 Quiz 3 — Mock B: questions, key and marking rubric

**Unofficial practice paper, built to the recalled shape.** Three RedNote recollections of earlier sittings (Mar/Apr 2025, Apr 2026, fall 2024; see `quiz-03-intel.md`) agree on 3 calculation questions in 45 min:
- Q1: Jury K-range for a loop given as an open-loop G(z) with K.
- Q2: bilinear transform of a continuous G(s) (pole-zero matching in fall 2024).
- Q3: given G_ZAS(z) and G_cl = z⁻¹, decide whether the output can track the input, and if so design C(z) (ripple-free deadbeat in fall 2024).

All numbers here are new and checked by `quiz-03-check.py`. **Total 30 marks, 45 min**, closed book, calculator allowed. This year's scope adds Ch 6, so Q2(c) asks for an implementation.

Sources: `resources/lecture-notes-weeks-01-04.pdf` PDF pp. 164–166 (Jury rules), 174–175 (Ex 4.8, the K-range model for Q1) and 186–187 (error constants); `resources/lecture-notes-chapters-05-06.pdf` pp. 7–8, 14–17 (bilinear, pole-zero matching), 49–56 (direct design and its conditions), 64–65 (deadbeat), 104–107 (direct programming).

---

## Q1 (10 marks)
A unity-feedback digital loop (sampler, ZOH, plant) has open-loop pulse transfer function
\[G(z)=\frac{K(0.4261z+0.3608)}{(z-1)(z-0.6065)},\qquad T=1\ \text{s}.\]
(a) Find the closed-loop characteristic equation and the range of \(K\) for stability. (7)
(b) Find \(K_v\) as a function of \(K\), and the steady-state error to a unit ramp when \(K=0.5\). (3)

### Key
(a) \(1+G(z)=0\) gives \(P(z)=z^2+(0.4261K-1.6065)z+(0.6065+0.3608K)=0\). This is 2nd order, so only the first three conditions apply (p. 166):
- \(|0.6065+0.3608K|<1\) gives \(-4.452<K<1.0905\).
- \(P(1)=1-1.6065+0.6065+(0.4261+0.3608)K=0.7869K>0\) gives \(K>0\).
- \(P(-1)=1+1.6065+0.6065+(0.3608-0.4261)K=3.2131-0.0653K>0\) gives \(K<49.2\).

So **\(0<K<1.0905\)**. At \(K=1.0905\) the poles reach \(|z|=1\) as a complex pair.

(b) \(K_v=\lim_{z\to1}\frac{(1-z^{-1})G(z)}{T}=\frac{K(0.4261+0.3608)}{1\cdot(1-0.6065)}=\mathbf{2K}\). At \(K=0.5\): \(K_v=1\) and \(e_{ss}=1/K_v=\mathbf 1\).
(Cross-check: the plant behind this G(z) is \(K/(s(s+0.5))\), whose continuous \(K_v=K/0.5=2K\). Sampling with a ZOH does not change \(K_v\).)

### Rubric (10)
- (a) 2: CE correct (signs and the K terms). 1 each: the three conditions set up correctly. 2: intersection stated as \(0<K<1.09\).
- (b) 2: \(K_v=2K\), including the \(1/T\) and cancelling \((z-1)\). 1: \(e_{ss}=1\).

### Common wrong paths
- Writing the CE as \((z-1)(z-0.6065)+K\) and dropping the numerator polynomial.
- Using \(P(-1)<0\): that rule is for odd n only.
- Giving \(K<49.2\) as the answer: the binding condition here is \(|a_2|<a_0\).
- \(K_v\) without \(1/T\) happens to be harmless at T = 1, but state it.

---

## Q2 (10 marks)
A continuous system \(G(s)=\dfrac{4}{s^2+2s+4}\) is to be approximated digitally with \(T=0.5\) s.
(a) Find \(G(z)\) by the bilinear transformation. Check the DC gain and whether \(G(z)\) is stable. (4)
(b) Find the strictly proper pole-zero matched \(G(z)\), with the DC gain matched. (3)
(c) Write the difference equation that implements your answer to (a) by direct programming. How many delay elements does it use, and how many would standard programming use? (3)

### Key
(a) \(s=\frac{2}{T}\frac{z-1}{z+1}=4\frac{z-1}{z+1}\). Multiply numerator and denominator by \((z+1)^2\):
denominator \(16(z-1)^2+8(z-1)(z+1)+4(z+1)^2=28z^2-24z+12\); numerator \(4(z+1)^2\).
**\(G(z)=\dfrac{(z+1)^2}{7z^2-6z+3}\)**. DC: \(G(1)=4/4=1=G(0)\) ✓. The poles satisfy \(|z|^2=3/7\), so \(|z|=0.655<1\): stable.
(b) Poles \(s=-1\pm j\sqrt3\) (\(\zeta\omega_n=1\), \(\omega_d=\sqrt3\)). Mapped: \(z^2-2e^{-0.5}\cos(0.866)z+e^{-1}=z^2-0.7859z+0.3679\). There are 2 zeros at infinity, so the strictly proper form adds \(n-m-1=1\) zero at −1:
\(G(z)=\alpha\frac{z+1}{z^2-0.7859z+0.3679}\). From \(G(1)=1\): \(\alpha=\frac{1-0.7859+0.3679}{2}=\mathbf{0.2910}\).
(c) Divide by \(7z^2\): \(G=\frac{\frac17(1+2z^{-1}+z^{-2})}{1-\frac67z^{-1}+\frac37z^{-2}}\). Then
\(y(k)=\tfrac67y(k-1)-\tfrac37y(k-2)+\tfrac17\big[x(k)+2x(k-1)+x(k-2)\big]\).
Direct programming uses **\(n+m=4\)** delays; standard programming uses **\(n=2\)**.

### Rubric (10)
- (a) 1: substitution with \(2/T=4\). 2: correct \(G(z)\). 1: DC check and stability by \(|z|=\sqrt{3/7}\).
- (b) 1: mapped pole polynomial. 1: one \((z+1)\) factor. 1: \(\alpha\).
- (c) 2: difference equation with correct signs and the \(1/7\) normalisation. 1: delay counts.

### Common wrong paths
- Not clearing \((z+1)^2\) consistently: the numerator must become \(4(z+1)^2\), not 4.
- In (b), adding two \((z+1)\) factors (that is the proper version), or none.
- In (c), keeping \(-6/7\) as written. (6.2) uses \(-a_1\), and here \(a_1=-6/7\), so the term is \(+\frac67y(k-1)\).

---

## Q3 (10 marks)
Unity feedback with a digital controller \(C(z)\) in front of \(G_{ZAS}(z)\). The desired closed loop is \(G_{cl}(z)=z^{-1}\).
(a) \(G_{ZAS}(z)=\dfrac{0.2(z+0.6)}{(z-0.8)(z-0.4)}\). Can \(G_{cl}=z^{-1}\) be used, and will the output track a step? If so, find \(C(z)\). (5)
(b) Repeat for \(G_{ZAS}(z)=\dfrac{0.1(z+1.5)}{(z-1)(z-0.5)}\). If \(z^{-1}\) is unacceptable, explain why, choose a valid \(G_{cl}\), and find \(C(z)\) and the output \(y(k)\), \(k=0..3\). (5)

### Key
(a) Check the four conditions (p. 56):
1. The relative degree of \(G_{ZAS}\) is 2 − 1 = 1, and \(z^{-1}\) has relative degree 1 ✓ (causal).
2. The only zero is −0.6, inside the circle ✓.
3. The poles 0.8 and 0.4 are stable ✓.
4. \(G_{cl}(1)=1\) ✓, so the step error is zero.

So **yes**. \(C=\frac{1}{G_{ZAS}}\frac{z^{-1}}{1-z^{-1}}=\frac{(z-0.8)(z-0.4)}{0.2(z+0.6)}\cdot\frac{1}{z-1}=\mathbf{\frac{5(z-0.8)(z-0.4)}{(z-1)(z+0.6)}}\). The type-0 plant needs the controller integrator at z = 1. (Remark: C cancels the plant zero at −0.6, so expect some intersample ripple. That is the ripple-free topic.)

(b) The zero at −1.5 lies **outside** the unit circle. With \(G_{cl}=z^{-1}\), \(C=\frac{10(z-0.5)}{z+1.5}\) has an unstable pole at −1.5, cancelling the plant zero. \(u(k)\) then grows without bound: the loop is input-output stable but not asymptotically stable (condition (ii), p. 52).
The fix keeps the bad zero in \(G_{cl}\): **\(G_{cl}=Kz^{-1}(1+1.5z^{-1})\)**, with \(G_{cl}(1)=2.5K=1\), so **K = 0.4**. Causality: relative degree 1 ✓. Condition (iii): the pole at z = 1 is marginal and is contained in \(1-G_{cl}\) because \(G_{cl}(1)=1\).
\(1-G_{cl}=\frac{z^2-0.4z-0.6}{z^2}=\frac{(z-1)(z+0.6)}{z^2}\), so
\(C=\frac{G_{cl}}{G_{ZAS}(1-G_{cl})}=\mathbf{\frac{4(z-0.5)}{z+0.6}}\).
\(Y=G_{cl}R\): **y = 0, 0.4, 1, 1**. (Also \(u = 4, -2, 0, 0\), as expected for a type-1 plant.) The price is one extra sample of settling.

### Rubric (10)
- (a) 2: all four conditions checked and named. 1: "yes, tracks". 2: \(C(z)\) correct.
- (b) 2: identifies the zero outside the circle and the unstable C(z). 1: \(G_{cl}\) with the bad zero and \(K=0.4\). 1: \(C(z)\). 1: \(y(k)\).

### Common wrong paths
- Answering "yes" in (b) because \(G_{cl}(1)=1\). Steady-state tracking is not enough when an unstable zero is cancelled.
- Putting \(K\) so that \(K\cdot1.5=1\): it is \(G_{cl}(1)=K(1+1.5)\).
- Treating the plant pole at z = 1 as forcing extra work: \(1-G_{cl}\) automatically has the factor \(z-1\) once \(G_{cl}(1)=1\).
