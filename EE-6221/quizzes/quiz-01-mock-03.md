# EE6221 Quiz 1 — Mock 3 answer key

**Sit `quiz-01-mock-03.html` before reading this file.** This is an unofficial practice paper, not a past quiz. Core: 20 marks; optional Section C: 5 marks. The suggested 30 minutes is a practice target, not a verified rule for the current quiz.

## Q1 — RRP arm (12)

One valid standard D–H assignment puts frame 0 at the base, frame 1 at the elbow, frame 2 at the rail, and frame 3 at the tool point. Every joint axis is vertical and upward. Choose $x_1$ from base to elbow, $x_2$ from elbow to rail, and $x_3\parallel x_2$; complete each right-handed frame with $y_k=z_k\times x_k$. The zero reference for $\theta_2$ makes link 2 collinear with link 1. Frame 1 is at height $h$; frame 2 stays at that height; frame 3 is $q_3$ higher.

| $k$ | $\theta_k$ | $d_k$ | $a_k$ | $\alpha_k$ | variable |
|---|---:|---:|---:|---:|---|
| 1 | $\theta_1$ | $h$ | $L_1$ | $0$ | $\theta_1$ |
| 2 | $\theta_2$ | $0$ | $L_2$ | $0$ | $\theta_2$ |
| 3 | $0$ | $q_3$ | $0$ | $0$ | $q_3$ |

The standard D–H formula gives, writing $c_i=\cos\theta_i$, $s_i=\sin\theta_i$,

$$
{}^0T_1=\begin{bmatrix}c_1&-s_1&0&L_1c_1\\s_1&c_1&0&L_1s_1\\0&0&1&h\\0&0&0&1\end{bmatrix},\quad
{}^1T_2=\begin{bmatrix}c_2&-s_2&0&L_2c_2\\s_2&c_2&0&L_2s_2\\0&0&1&0\\0&0&0&1\end{bmatrix},\quad
{}^2T_3=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&q_3\\0&0&0&1\end{bmatrix}.
$$

With $c_{12}=\cos(\theta_1+\theta_2)$ and $s_{12}=\sin(\theta_1+\theta_2)$,

$$
{}^0T_3=\begin{bmatrix}
c_{12}&-s_{12}&0&L_1c_1+L_2c_{12}\\
s_{12}&c_{12}&0&L_1s_1+L_2s_{12}\\
0&0&1&h+q_3\\0&0&0&1
\end{bmatrix}.
$$

At $(\theta_1,\theta_2,q_3)=(90^\circ,-90^\circ,2)$, the total horizontal angle is zero. Thus $R=I$, $p=(2,3,6)^T$. Physical checks: link 1 reaches 3 units along $+y_0$; link 2 reaches 2 units along $+x_0$; the carriage adds 2 units to height 4. All agree with $p$.

**Marking:** (a) 1 for three vertical joint axes, 1 for origins at elbow/rail/tool, 1 for consistent $x$ and right-handed $y$; (b) 1 each correct row; (c) 1 each link transform; (d) 1 product rotation, 1 product translation, 1 numeric result with physical check. Accept equivalent consistent frame signs and zero-angle references after checking the forward pose. Do not award full frame marks for placing frame 1 at the base or treating the fixed height as the variable $q_3$.

## Q2 — pick and place (8)

At pick, A's long faces run along $x_0$ and are separated along $y_0$. One valid choice is
$r_2=+y_0=(0,1,0)^T$, $r_3=-z_0=(0,0,-1)^T$, and
$r_1=r_2\times r_3=-x_0=(-1,0,0)^T$. Therefore

$$
{}^0T_{\rm pick}=\begin{bmatrix}
-1&0&0&4\\0&1&0&9\\0&0&-1&1\\0&0&0&1
\end{bmatrix}.
$$

B's top is $1.5+3/2=3$. A's centroid is another $2/2=1$ above that, so its destination is $(11,4,4)^T$. To align A's long axis with $y_0$, rotate the held part $90^\circ$ about $z_0$. One consistent choice is $r_2=+x_0$, $r_1=+y_0$, $r_3=-z_0$, giving

$$
{}^0T_{\rm place}=\begin{bmatrix}
0&1&0&11\\1&0&0&4\\0&0&-1&4\\0&0&0&1
\end{bmatrix}.
$$

For these choices, $R_{\rm place}R_{\rm pick}^T=R_z(-90^\circ)$. The object long axis $+x_0$ goes to $-y_0$, which is aligned with B's unoriented long axis. Both rotation matrices have orthonormal columns, $r_1\times r_2=r_3$, and determinant $+1$. The alternative $r_2=-y_0$ at pick or $r_2=-x_0$ at place is valid when the whole frame and object rotation remain consistent.

**Marking:** (a) 1 for perpendicular jaw direction with explanation, 1 for right-handed rotation, 1 for pick translation; (b) 1 for $z=4$, 1 for rotated place frame, 1 for $(11,4,4)^T$; (c) 1 for a right-handed check on both frames, 1 for a consistent quarter-turn. Do not infer the sliding direction from the length of the fingers: it is the open-close axis perpendicular to the contacted faces.

## Section C — optional prediction (5)

For any rigid transform, $T^{-1}=\begin{bmatrix}R^T&-R^Tp\\0&1\end{bmatrix}$. Using the pick choice above,

$$
({}^0T_{\rm pick})^{-1}=\begin{bmatrix}
-1&0&0&4\\0&1&0&-9\\0&0&-1&1\\0&0&0&1
\end{bmatrix}.
$$

At $q_n=0$, $e^{q_n/\pi}=1$, so $w=(4,9,1,0,0,-1)^T$. Mark (a) 1 for $R^T$, 1 for $-R^Tp$, 1 for the numeric inverse; (b) 1 for the position and 1 for the scaled approach vector. Recompute from the learner's own valid pick frame before marking.

## Provenance and verification

- `resources/exercises-kinematics-not-for-submission.pdf`, p. 2: two-part pick/place task shape; all geometry and numbers above are new.
- `resources/lecture-01-manipulator-kinematics.pdf`, pp. 57–58: normal/sliding/approach column convention; pp. 82–84: vertical-axis horizontal-jointed robot as a course example.
- `quizzes/quiz-01-intel.md`: unofficial prior-student format recollections, used only to choose a practice-paper shape.

The three D–H matrices were multiplied independently and the numeric pose, inverse, and both grasp frames were checked with matrix arithmetic. This key assumes the stated upward-positive prismatic rail; a reversed rail frame changes signs but is acceptable if used consistently.
