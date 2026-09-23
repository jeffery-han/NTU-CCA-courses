"""Numerical check of the quiz-01-mock-05 answer key (run: python3 quiz-01-mock-05-check.py).

For each D-H table: search joint angles in multiples of pi/2 for a pose where every z_{k-1}
lies along joint k's physical axis and the tool tip equals the figure's dimension sums.
A table that passes describes the drawn robot; a wrong alpha, d or a makes the search fail.
"""
import itertools
import numpy as np

pi = np.pi


def dh(theta, d, a, alpha):
    ct, st, ca, sa = np.cos(theta), np.sin(theta), np.cos(alpha), np.sin(alpha)
    return np.array([[ct, -ca * st, sa * st, a * ct],
                     [st, ca * ct, -sa * ct, a * st],
                     [0, sa, ca, d],
                     [0, 0, 0, 1.0]])


def frames(rows):
    T, out = np.eye(4), [np.eye(4)]
    for r in rows:
        T = T @ dh(*r)
        out.append(T)
    return out


X, Y, Z = np.eye(3)


def find_pose(table, axes, tip, offsets=None):
    """table rows: (theta, d, a, alpha) with theta=None for a revolute variable."""
    free = [i for i, r in enumerate(table) if r[0] is None]
    offsets = offsets or {}
    for combo in itertools.product([0, pi / 2, pi, -pi / 2], repeat=len(free)):
        rows = [list(r) for r in table]
        for i, q in zip(free, combo):
            rows[i][0] = q + offsets.get(i, 0.0)
        F = frames(rows)
        ok_axes = all(abs(abs(F[k][:3, 2] @ ax) - 1) < 1e-9 for k, ax in enumerate(axes))
        if ok_axes and np.allclose(F[-1][:3, 3], tip, atol=1e-9):
            return [round(np.degrees(r[0]), 2) for r in rows]
    raise AssertionError("no pose matches the figure")


# Q1  23-24 S2 Q1 (tutor p.9-10): tip at (0.16+0.18+0.17+0.20, 0, 0.47-0.15+0.05)
A = [(None, 0.47, 0, pi / 2), (None, 0.16, 0.15, pi / 2), (None, 0, 0.18, 0),
     (None, 0, 0.17, -pi / 2), (None, 0.05, 0, pi / 2), (None, 0.20, 0, 0)]
print("Q1 pose (deg):", find_pose(A, [Z, X, Y, Y, Z, X], [0.71, 0, 0.37]))

# Q2  22-23 S2 Q1 seven-joint (tutor p.11-12), d5 = 0.30: tip (0.22+0.20+0.30+0.12, 0, 0.65-0.15+0.05)
B = [(None, 0.65, 0.22, -pi / 2), (None, 0, 0, -pi / 2), (None, 0.20, 0.15, pi / 2),
     (None, 0, 0, -pi / 2), (pi / 2, 0.30, 0, pi / 2), (None, -0.05, 0, -pi / 2), (None, 0.12, 0, 0)]
print("Q2 pose (deg):", find_pose(B, [Z, Y, X, Y, X, Z, X], [0.84, 0, 0.55]))

# Q3  24-25 S2 Q1 wall-mounted, cm (tutor p.13-16); base: z0 out of wall, y0 down. d3 = 20
C = [(None, 25, 0, pi / 2), (None, 11, 0, -pi / 2), (-pi / 2, 20, 0, -pi / 2),
     (None, 0, 15, -pi / 2), (None, 4, 0, pi / 2), (None, 20, 0, 0)]
print("Q3 pose (deg):", find_pose(C, [Z, Y, Z, X, Y, Z], [0, -15, 80]))
T23 = dh(-pi / 2, 7.0, 0, -pi / 2)  # tutor's third link matrix with d3 = 7
assert np.allclose(T23, [[0, 0, 1, 0], [-1, 0, 0, 0], [0, -1, 0, 7], [0, 0, 0, 1]])

# Q4  tutor p.4 six-joint, q1 prismatic = 0.80; no tutor solution. q4 and q5 axes are parallel
# and offset 0.18 across, 0.10 down, so a4 = sqrt(0.18^2 + 0.10^2) with a -29.05 deg angle offset.
a4, phi = np.hypot(0.18, 0.10), np.arctan2(0.10, 0.18)
D = [(0, 0.80, 0.15, pi), (None, 0.20, 0, pi / 2), (None, 0, 0.19, 0),
     (None, 0, a4, 0), (None, 0, 0, pi / 2), (None, 0.25, 0, 0)]
print("Q4 pose (deg):", find_pose(D, [Z, Z, Y, Y, Y, X], [0.77, 0, 0.50], offsets={3: phi, 4: -phi}),
      f"a4 = {a4:.4f} m")

# Q5  4-variable mobile-platform IK (tutor p.17-24)
def w(q):
    q1, q2, q3, q4 = q
    S1, C1, S3, C3, e = np.sin(q1), np.cos(q1), np.sin(q3), np.cos(q3), np.exp(q4 / pi)
    return np.array([S1 * q2 + .25 * S1 * C3, C1 * q2 + .25 * C1 * C3, -.25 * S3 + .25,
                     -e * S1 * C3, e * C1 * C3, -e * S3])


def J(q):
    q1, q2, q3, q4 = q
    S1, C1, S3, C3, e = np.sin(q1), np.cos(q1), np.sin(q3), np.cos(q3), np.exp(q4 / pi)
    return np.array([[C1 * q2 + .25 * C1 * C3, S1, -.25 * S1 * S3, 0],
                     [-S1 * q2 - .25 * S1 * C3, C1, -.25 * C1 * S3, 0],
                     [0, 0, -.25 * C3, 0],
                     [-e * C1 * C3, 0, e * S1 * S3, -e * S1 * C3 / pi],
                     [-e * S1 * C3, 0, -e * C1 * S3, e * C1 * C3 / pi],
                     [0, 0, -e * C3, -e * S3 / pi]])


q = np.array([0.3, 0.1, 0.7, 0.4])
num = np.column_stack([(w(q + h) - w(q - h)) / 2e-6 for h in np.eye(4) * 1e-6])
assert np.allclose(J(q), num, atol=1e-6)
for sol in ([pi / 4, np.sqrt(2) / 5, pi / 2, 0], [-3 * pi / 4, -np.sqrt(2) / 5, pi / 2, 0]):
    assert np.allclose(w(sol)[:3], [0.2, 0.2, 0]) and np.allclose(w(sol)[3:], [0, 0, -1])
print("Q5 Jacobian, both IK branches and approach vector (0,0,-1): ok")

# Q6  22-23 S2 Q3(b) spherical RRP IK
x, y, z = 0.15, 0.25, 0.025
q1, q2, q3 = np.arctan2(y, x), np.arctan2(np.hypot(x, y), z), np.linalg.norm([x, y, z]) - 0.1
for a, b in ((q1, q2), (q1 + pi, -q2)):
    assert np.allclose([np.cos(a) * np.sin(b), np.sin(a) * np.sin(b), np.cos(b)] * np.array(q3 + 0.1), [x, y, z])
print(f"Q6 q1 = {np.degrees(q1):.2f} deg, q2 = {np.degrees(q2):.2f} deg, q3 = {q3:.4f}")
