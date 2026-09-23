# EE6221 Quiz 1 — Final practice check: answer key

**Sit `quiz-01-mock-04.html` before reading this file.** This is an unofficial new practice paper, not a previous quiz. Core total: 20 marks. The 30-minute target and readiness threshold are study decisions, not NTU rules.

## Q1 — articulated RRR arm (12)

One valid standard D–H assignment puts frame 0 at the base with $z_0$ up, frame 1 at the shoulder with $z_1$ horizontal along $-y_0$ when $\theta_1=0$, frame 2 at the elbow with $z_2\parallel z_1$, and frame 3 at the tool point with $z_3\parallel z_2$. At the zero references, $x_1,x_2,x_3$ point outward along the arm; the $x_k$ directions rotate with their joints. Complete each right-handed frame with $y_k=z_k\times x_k$.

| $k$ | $\theta_k$ | $d_k$ | $a_k$ | $\alpha_k$ | variable |
|---|---:|---:|---:|---:|---|
| 1 | $\theta_1$ | $h$ | $0$ | $+90^\circ$ | $\theta_1$ |
| 2 | $\theta_2$ | $0$ | $L_2$ | $0$ | $\theta_2$ |
| 3 | $\theta_3$ | $0$ | $L_3$ | $0$ | $\theta_3$ |

The first twist changes the joint axis from vertical to horizontal; the shoulder and elbow axes are parallel, so later twists are zero. Writing $c_i=\cos\theta_i$ and $s_i=\sin\theta_i$,

$$
{}^0T_1=\begin{bmatrix}c_1&0&s_1&0\\s_1&0&-c_1&0\\0&1&0&h\\0&0&0&1\end{bmatrix},\quad
{}^1T_2=\begin{bmatrix}c_2&-s_2&0&L_2c_2\\s_2&c_2&0&L_2s_2\\0&0&1&0\\0&0&0&1\end{bmatrix},\quad
{}^2T_3=\begin{bmatrix}c_3&-s_3&0&L_3c_3\\s_3&c_3&0&L_3s_3\\0&0&1&0\\0&0&0&1\end{bmatrix}.
$$

Let $c_{23}=\cos(\theta_2+\theta_3)$, $s_{23}=\sin(\theta_2+\theta_3)$, and $r=L_2c_2+L_3c_{23}$. Then

$$
{}^0T_3=\begin{bmatrix}
c_1c_{23}&-c_1s_{23}&s_1&c_1r\\
s_1c_{23}&-s_1s_{23}&-c_1&s_1r\\
s_{23}&c_{23}&0&h+L_2s_2+L_3s_{23}\\
0&0&0&1
\end{bmatrix}.
$$

At $(\theta_1,\theta_2,\theta_3)=(0^\circ,90^\circ,-90^\circ)$, link 2 goes 4 upward from the shoulder and link 3 goes 3 along $+x_0$. Thus the tool point is $(3,0,3+4)=(3,0,7)$ and

$$
{}^0T_3=\begin{bmatrix}
1&0&0&3\\0&0&-1&0\\0&1&0&7\\0&0&0&1
\end{bmatrix}.
$$

**Marks:** (a) 1 for vertical waist/horizontal shoulder and elbow axes, 1 for base/shoulder/elbow/tool origins, 1 for consistent right-handed $x,y$ directions; (b) 1 for row 1 with $d_1=h$, $a_1=0$, and $\alpha_1=+90^\circ$, 1 each for rows 2 and 3; (c) 1 each complete link matrix; (d) 1 symbolic rotation, 1 symbolic position, 1 numeric result plus physical link-direction check. An alternative frame convention is acceptable if internally consistent and if it gives the same physical tool pose. A correct rotation with an unrotated link-length translation does not earn the symbolic-position mark.

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

Topic basis: `resources/exercises-kinematics-not-for-submission.pdf` p. 2, `resources/lecture-01-manipulator-kinematics.pdf` pp. 57–58, 61–70, and 74–76, and the labelled unofficial format summary in `quizzes/quiz-01-intel.md`. All geometry and numbers in this mock are new.
