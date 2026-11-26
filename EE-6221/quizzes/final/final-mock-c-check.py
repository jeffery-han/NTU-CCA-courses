"""Checker for final-mock-c.html and its key final-mock-c.md.

Recomputes every number in the key: D-H forward kinematics of the model table (every frame axis
and the tip), simplified link matrices, computed-torque and hybrid values, the force-subspace
disturbance by ODE integration, wheel rows by hub-velocity projection, platform speeds, IK with
back-substitution, homography groups by brute force (with det M), and Kalman gains by exact
fractions.  Asserts each value appears in the key, and that the paper leaks none of them.
Run:  python3 final-mock-c-check.py
"""
import itertools, math, re
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = (HERE / "final-mock-c.html").read_text()
KEY = (HERE / "final-mock-c.md").read_text()
need = []                                   # strings that must appear in the key and not in the page
def f4(x): return f"{x:.4f}".replace("-", "−")

# ---------- Q1: model D-H table, world x right, y into page, z up ----------
def dh(t, d, a, al):
    t, al = math.radians(t), math.radians(al)
    ct, st, ca, sa = math.cos(t), math.sin(t), math.cos(al), math.sin(al)
    return [[ct, -ca * st, sa * st, a * ct], [st, ca * ct, -sa * ct, a * st], [0, sa, ca, d], [0, 0, 0, 1]]
mm = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
NAME = {(1, 0, 0): "→", (-1, 0, 0): "←", (0, 0, 1): "↑", (0, 0, -1): "↓", (0, 1, 0): "⊗", (0, -1, 0): "⊙"}
rows = [(0, 40, 0, 90), (90, 0, 30, 0), (0, 0, 0, 90), (0, 20, 0, -90), (-90, 0, 0, 90), (0, 12, 0, 0)]
expect = {0: ("→", "⊗", "↑"), 1: ("→", "↑", "⊙"), 2: ("↑", "←", "⊙"), 3: ("↑", "⊙", "→"),
          4: ("↑", "←", "⊙"), 5: ("→", "⊙", "↓"), 6: ("→", "⊙", "↓")}
M = [[float(i == j) for j in range(4)] for i in range(4)]
origins = {0: (0, 0)}
for k, r in enumerate(rows, 1):
    M = mm(M, dh(*r))
    ax = tuple(NAME[tuple(round(M[i][c]) for i in range(3))] for c in range(3))
    assert ax == expect[k], (k, ax)
    origins[k] = (round(M[0][3], 6), round(M[2][3], 6)); assert abs(M[1][3]) < 1e-9
assert origins == {0: (0, 0), 1: (0, 40), 2: (0, 70), 3: (0, 70), 4: (20, 70), 5: (20, 70), 6: (20, 58)}, origins
need += ["(20, 58)", "θ2 + 90°", "θ5 − 90°"]
# T12 with theta = q2 + 90: cos = -S2, sin = C2 (check numerically at q2 = 0.3)
q2 = 0.3; T = dh(math.degrees(q2) + 90, 0, 30, 0)
assert abs(T[0][0] + math.sin(q2)) < 1e-12 and abs(T[1][0] - math.cos(q2)) < 1e-12 and abs(T[0][3] + 30 * math.sin(q2)) < 1e-12
need += ["−30S_2", "30C_2"]

# ---------- Q2 ----------
wn = 0.5 * 2 * math.pi * min(4.5, 3, 7); kp = wn ** 2; kv = 2 * 1.2 * wn
kvf, kpf = 2 * wn, wn ** 2
q1, q2, dq1, dq2 = math.pi / 3, 0, 1, 0.5
v1 = 0 + kv * 0 + kp * 0.02
v2 = 0.4 + kv * -0.05 + kp * 0.01
u2 = (0.5 + 0.5 * math.cos(q2)) * v1 + 0.5 * v2 + 0.5 * math.sin(q2) * dq1 ** 2 + 4.9 * math.cos(q1 + q2)
need += [f4(wn), f4(kp), f4(kv), f4(kvf), f4(v1), f4(v2), f4(u2)]
ke, m3 = 60, 6
ef, def_ = 18 - 12, -ke * 0.1
v3 = (0 + kvf * def_ + kpf * ef) / ke
u3 = m3 * v3 + 3 * 0.1 + 58.8 + 12
q3ss = 0.15 + 18 / ke
assert abs(q3ss - 0.45) < 1e-12
need += [f4(v3), f4(u3), "0.45 m"]
rhs = ke * 3 / m3; ess = rhs / kpf
q, dq, dt = 0.15, 0.0, 1e-4
for _ in range(int(6 / dt)):
    f = ke * (q - 0.15); vv = (kvf * (-ke * dq) + kpf * (18 - f)) / ke
    ddq = (m3 * vv - 3) / m3                 # u3 cancels 3q'+58.8+f; the unknown d3 = 3 is left
    dq += ddq * dt; q += dq * dt
assert abs((18 - ke * (q - 0.15)) - ess) < 1e-3
assert rhs == 30
need += ["= 30", f4(ess)]

# ---------- Q3(a) ----------
def geo(x, y):
    l = math.hypot(x, y); a = math.degrees(math.atan2(y, x)); return l, a
def rowsv(x, y, ab):
    s = math.radians(ab); roll, axle = (math.sin(s), -math.cos(s)), (math.cos(s), math.sin(s))
    return [d[0] for d in (roll, axle)], [[d[0], d[1], -y * d[0] + x * d[1]] for d in (roll, axle)]
lA, aA = geo(-0.24, 0.07); bA = 90 - aA
lB, aB = geo(-0.24, -0.07); bB = (90 - aB + 180) % 360 - 180
lC, aC = geo(0.30, 0.10)
for x, y, a_, b_, l_ in ((-0.24, 0.07, aA, bA, lA), (-0.24, -0.07, aB, bB, lB)):
    _, (rr, sr) = rowsv(x, y, a_ + b_)
    B = math.radians(b_); slide = [-l_ * math.cos(B), l_ * math.sin(B)]
    assert abs(rr[2] - slide[0]) < 1e-12 and abs(sr[2] - slide[1]) < 1e-12
    assert [round(c, 9) for c in rr[:2]] == [1, 0] and [round(c, 9) for c in sr[:2]] == [0, 1]
need += ["0.25", f"{aA:.2f}°", f"−{abs(bA):.2f}°", f"−{abs(aB):.2f}°", f"−{abs(bB):.2f}°", f"{lC:.4f}", f"{aC:.2f}°"]
xd, th = 0.6, -0.5
yd = 0.24 * th                                     # sliding: yd + th * (-0.24) = 0
phA = (xd - th * 0.07) / 0.05; phB = (xd + th * 0.07) / 0.05
hub = (xd - th * 0.10, yd + th * 0.30)
rolldir = math.degrees(math.atan2(hub[1], hub[0]))  # rolling direction = alpha + beta - 90
bC = rolldir + 90 - aC
assert -90 < bC < 90
s = math.radians(aC + bC)
assert abs(hub[0] * math.cos(s) + hub[1] * math.sin(s)) < 1e-12            # sliding row satisfied
phC = (hub[0] * math.sin(s) - hub[1] * math.cos(s)) / 0.04
assert phC > 0 and abs(phC - math.hypot(*hub) / 0.04) < 1e-9
assert (round(yd, 12), round(phA, 12), round(phB, 12)) == (-0.12, 12.7, 11.3)
need += ["−0.12", "12.7", "11.3", f"{bC:.2f}°", f4(math.radians(bC)), f4(phC)]

# ---------- Q3(b) ----------
X, Y, Z, w6 = 0.3, 0.35, 0.18, -math.exp(0.75)
q4 = math.pi * math.log(-w6); q3 = 0.5 - Z
C2 = (X * X + Y * Y - 0.35 ** 2 - 0.25 ** 2) / (2 * 0.35 * 0.25)
sols = []
for sg in (1, -1):
    qq2 = sg * math.acos(C2); qq1 = math.atan2(Y, X) - math.atan2(0.25 * math.sin(qq2), 0.35 + 0.25 * math.cos(qq2))
    assert abs(0.35 * math.cos(qq1) + 0.25 * math.cos(qq1 + qq2) - X) < 1e-12 and abs(0.35 * math.sin(qq1) + 0.25 * math.sin(qq1 + qq2) - Y) < 1e-12
    sols.append((qq1, qq2))
assert abs(q3 - 0.32) < 1e-12 and abs(C2 - 0.11 / 0.7) < 1e-12
need += [f4(q4), "0.32 m", "11/70", f4(sols[0][1]), f4(sols[0][0]), f4(sols[1][0])]

# ---------- Q4 ----------
P = {1: (0, 0), 2: (4, 0), 3: (4, 2), 4: (0, 2), 5: (2, 1), 6: (2, 0), 7: (2, 2)}
col = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0
def groups(S): return [g for g in itertools.combinations(sorted(S), 4) if not any(col(*[P[i] for i in t]) for t in itertools.combinations(g, 3))]
def det(A):
    A = [row[:] for row in A]; n = len(A); dv = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return 0
        if p != c: A[c], A[p] = A[p], A[c]; dv = -dv
        dv *= A[c][c]
        for r in range(c + 1, n):
            fct = A[r][c] / A[c][c]; A[r] = [x - fct * y for x, y in zip(A[r], A[c])]
    return dv
Gt = [[Fr(6, 5), Fr(1, 10), Fr(1, 2)], [Fr(-1, 5), Fr(1), Fr(1, 3)], [Fr(1, 20), Fr(1, 30), Fr(1)]]
def Mrows(ids):
    R = []
    for i in ids:
        ax, ay = map(Fr, P[i]); w = [Gt[r][0] * ax + Gt[r][1] * ay + Gt[r][2] for r in range(3)]; bx, by = w[0] / w[2], w[1] / w[2]
        R += [[ax, ay, 1, 0, 0, 0, -ax * bx, -ay * bx], [0, 0, 0, ax, ay, 1, -ax * by, -ay * by]]
    return R
Fa, Fb, Fc = {1, 2, 4, 6, 7}, set(P), {3, 4, 5, 6, 7}
gG, gH = groups(Fa & Fb), groups(Fb & Fc)
assert gG == [(1, 2, 4, 7), (1, 4, 6, 7), (2, 4, 6, 7)] and gH == [(3, 4, 5, 6)]
for g in itertools.combinations(sorted(Fa & Fb), 4):
    assert (det(Mrows(g)) != 0) == (g in gG), g
assert len(Fa & Fc) == 3
assert groups((Fb - {6}) & Fc) == []                     # twist: H cannot be found
need += ["{O1, O2, O4, O7}", "{O1, O4, O6, O7}", "{O2, O4, O6, O7}", "{O3, O4, O5, O6}"]
ax, ay, bx, by = 1.5, 2.2, 2.1, 1.8
need += [f"{-ax * bx:.2f}".replace("-", "−"), f"{-ay * bx:.2f}".replace("-", "−"), f"{-ax * by:.2f}".replace("-", "−"), f"{-ay * by:.2f}".replace("-", "−")]

# ---------- Q5 (units of a^2) ----------
s2 = {1: Fr(3), 2: Fr(6), 3: Fr(1)}; p = Fr(2)
pp = 1 / (1 / p + sum(1 / v for v in s2.values()))
L = {i: pp / v for i, v in s2.items()}
assert all(-2 * (1 - sum(L.values())) * p + 2 * L[i] * s2[i] == 0 for i in L)
assert (pp, L[1], L[2], L[3]) == (Fr(1, 2), Fr(1, 6), Fr(1, 12), Fr(1, 2))
infoA, infoB = 1 / s2[3], 1 / s2[1] + 1 / s2[2]
assert infoA == 1 and infoB == Fr(1, 2)
n, S = 3, sum(s2.values()); Ls = n * p / (n * n * p + S); ps = (1 - n * Ls) ** 2 * p + Ls ** 2 * S
assert -2 * n * (1 - n * Ls) * p + 2 * Ls * S == 0 and 1 / ps == 1 / p + Fr(n * n) / S
pA = 1 / (1 / p + infoA)
assert (Ls, ps, pA) == (Fr(3, 14), Fr(5, 7), Fr(2, 3)) and ps > pA
need += ["1/6", "1/12", "3/14", "5/7", "2/3"]

missing = [s for s in need if s not in KEY]
assert not missing, missing
leaks = [s for s in need if len(s) > 4 and s in PAGE]
assert not leaks, leaks
assert len(re.findall(r'data-item="', PAGE)) == 13 and len(set(re.findall(r'data-item="([^"]+)"', PAGE))) == 13
print("ok", len(need), "values")
