# EE6221 Quiz 1 — Final practice check: answer key

**Sit `quiz-01-mock-04.html` before reading this file.** This is an unofficial new practice paper, not a previous quiz. Core total: 20 marks. The 30-minute target and readiness threshold are study decisions, not NTU rules.

## Q1 — RRP arm (12)

Use the frame locations specified in the question, with every $z$ axis upward. Take $x_1$ along link 1, $x_2$ along link 2, and $x_3\parallel x_2$; set $y_k=z_k\times x_k$. One valid standard D–H table is:

| $k$ | $\theta_k$ | $d_k$ | $a_k$ | $\alpha_k$ | joint variable |
|---|---:|---:|---:|---:|---|
| 1 | $\theta_1$ | $h$ | $L_1$ | $0$ | $\theta_1$ |
| 2 | $\theta_2$ | $0$ | $L_2$ | $0$ | $\theta_2$ |
| 3 | $0$ | $q_3$ | $0$ | $0$ | $q_3$ |

With $c_i=\cos\theta_i$ and $s_i=\sin\theta_i$,

$$
{}^0T_1=\begin{bmatrix}c_1&-s_1&0&L_1c_1\\s_1&c_1&0&L_1s_1\\0&0&1&h\\0&0&0&1\end{bmatrix},\quad
{}^1T_2=\begin{bmatrix}c_2&-s_2&0&L_2c_2\\s_2&c_2&0&L_2s_2\\0&0&1&0\\0&0&0&1\end{bmatrix},\quad
{}^2T_3=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&q_3\\0&0&0&1\end{bmatrix}.
$$

Writing $c_{12}=\cos(\theta_1+\theta_2)$ and $s_{12}=\sin(\theta_1+\theta_2)$,

$$
{}^0T_3=\begin{bmatrix}
c_{12}&-s_{12}&0&L_1c_1+L_2c_{12}\\
s_{12}&c_{12}&0&L_1s_1+L_2s_{12}\\
0&0&1&h+q_3\\0&0&0&1
\end{bmatrix}.
$$

At $\theta_1=90^\circ$, $\theta_2=90^\circ$, $L_1=4$, $L_2=3$, $h=5$, $q_3=1$, the accumulated angle is $180^\circ$. Link 1 goes 4 along $+y_0$; link 2 goes 3 along $-x_0$. Therefore $p=(-3,4,6)^T$ and

$$
{}^0T_3=\begin{bmatrix}
-1&0&0&-3\\0&-1&0&4\\0&0&1&6\\0&0&0&1
\end{bmatrix}.
$$

**Marks:** (a) 1 for vertical axes, 1 for specified origins, 1 for consistent $x$ directions/right-handed frames; (b) 1 each row; (c) 1 each complete link matrix; (d) 1 symbolic rotation, 1 symbolic position, 1 correct numeric pose plus directional check. Accept an alternative consistent D–H frame assignment only after checking its physical tool pose. The critical check is that $a_k$ produces $(a_k\cos\theta_k,a_k\sin\theta_k,d_k)$ in the preceding frame, not $(a_k,0,d_k)$ unless $\theta_k=0$.

## Q2 — pick and place (8)

A's long side faces run along $y_0$ and are separated along $x_0$. One valid choice is $r_2=+x_0$, $r_3=-z_0$, and $r_1=r_2\times r_3=+y_0$. Thus

$$
{}^0T_{\rm pick}=\begin{bmatrix}
0&1&0&5\\1&0&0&11\\0&0&-1&1\\0&0&0&1
\end{bmatrix}.
$$

B's top height is $1.5+3/2=3$. A's centroid sits another $2/2=1$ above it, giving destination $(12,4,4)^T$. B's long axis runs along $x_0$, so rotate the held object one quarter-turn. Choose $r_2=+y_0$, $r_1=-x_0$, $r_3=-z_0$:

$$
{}^0T_{\rm place}=\begin{bmatrix}
-1&0&0&12\\0&1&0&4\\0&0&-1&4\\0&0&0&1
\end{bmatrix}.
$$

For these signs, $R_{\rm place}R_{\rm pick}^T=R_z(+90^\circ)$: A's $+y_0$ long axis becomes $-x_0$, aligned with B's long axis. Both $R$ blocks have orthonormal columns, $r_1\times r_2=r_3$, and determinant $+1$. Reversed but consistent jaw-axis signs are acceptable.

**Marks:** (a) 1 for the correct perpendicular jaw direction and sketch, 1 for the right-handed rotation, 1 for pick translation; (b) 1 for destination height 4, 1 for the changed orientation, 1 for complete place translation; (c) 1 for right-handed checks on both, 1 for a consistent $90^\circ$ turn.

## Readiness interpretation

The page's threshold is a practical stopping signal: at least 18/20 core, including at least 5/6 on Q1(c–d), a correct Q2 jaw direction, and a timed unassisted attempt. Meeting it supports stopping this D–H/pick-place drill; it does not verify every possible current Quiz 1 topic or official rule. The current NTULearn announcement controls those.

Topic basis: `resources/exercises-kinematics-not-for-submission.pdf` p. 2, `resources/lecture-01-manipulator-kinematics.pdf` pp. 57–58 and 82–84, and the labelled unofficial format summary in `quizzes/quiz-01-intel.md`. All geometry and numbers in this mock are new.
