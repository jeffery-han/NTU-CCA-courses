"""Re-derives every key in final-mock-b.md and checks the paper page has no answers in it.
Run:  python3 final-mock-b-check.py
"""
import itertools, json, math, re
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
MD = (HERE / "final-mock-b.md").read_text()
PAGE = (HERE / "final-mock-b.html").read_text()
K = {}


def has(s):                                   # every key must be written in the .md
    assert s in MD, s


# ---------------- Q1: D-H, page frame R = right, U = up, O = out of page ----------------
R, U, O = (1, 0, 0), (0, 1, 0), (0, 0, 1)
neg = lambda a: tuple(-c for c in a)
cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
z = {0: U, 1: O, 2: O, 3: R, 4: U, 5: R, 6: R}
x = {0: R, 1: R, 2: R, 3: U, 4: O, 5: O, 6: O}


def twist(k):                                 # alpha_k: about x_k, z_{k-1} -> z_k
    if z[k - 1] == z[k]:
        return 0
    c = cross(z[k - 1], z[k])
    return 90 if c == x[k] else -90 if c == neg(x[k]) else None


def turn(k):                                  # theta_k at the drawn pose: about z_{k-1}, x_{k-1} -> x_k
    if x[k - 1] == x[k]:
        return 0
    if x[k - 1] == neg(x[k]):
        return 180
    c = cross(x[k - 1], x[k])
    return 90 if c == z[k - 1] else -90 if c == neg(z[k - 1]) else None


al = [twist(k) for k in range(1, 7)]
th = [turn(k) for k in range(1, 7)]
assert al == [90, 0, 90, 90, -90, 0], al
assert th == [0, 0, 90, 90, 0, 0], th
y = {k: cross(z[k], x[k]) for k in z}
assert y == {0: neg(O), 1: U, 2: U, 3: O, 4: R, 5: neg(U), 6: neg(U)}, y


def dh(t, d, a, alp):
    t, alp = math.radians(t), math.radians(alp)
    ct, st, ca, sa = math.cos(t), math.sin(t), math.cos(alp), math.sin(alp)
    return [[ct, -ca * st, sa * st, a * ct], [st, ca * ct, -sa * ct, a * st], [0, sa, ca, d], [0, 0, 0, 1]]


def fk(rows):
    M = [[float(i == j) for j in range(4)] for i in range(4)]
    out = []
    for r in rows:
        T = dh(*r)
        M = [[sum(M[i][k] * T[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
        out.append(M)
    return out


D4 = 20                                        # figure is drawn with d4 = 20 cm
d = [30, 0, 0, D4, 5, 12]
a = [0, 25, 0, 0, 0, 0]
rows = [(th[k], d[k], a[k], al[k]) for k in range(6)]
# frame-0 vector (x0 = R, y0 = into page, z0 = U) -> page coordinates
page = lambda v: tuple(round(v[0] * x[0][i] + v[1] * y[0][i] + v[2] * z[0][i], 6) for i in range(3))
origins = {1: (0, 30, 0), 2: (25, 30, 0), 3: (25, 30, 0), 4: (45, 30, 0), 5: (45, 35, 0), 6: (57, 35, 0)}
for k, M in enumerate(fk(rows), 1):
    assert page([M[i][3] for i in range(3)]) == tuple(float(c) for c in origins[k]), k
    assert page([M[i][0] for i in range(3)]) == x[k] and page([M[i][2] for i in range(3)]) == z[k], k
K["q1_tip_cm"] = [57, 35]
has("(57, 35)")
# every printed length lands in exactly one cell
cells = {30: "d1", 25: "a2", 5: "d5", 12: "d6"}
assert [c for c in ("d1", "a2", "d5", "d6")] == [cells[n] for n in (30, 25, 5, 12)]
for row in ["| 1 | \\(\\theta_1\\) | 30 | 0 | \\(+90^\\circ\\) |",
            "| 2 | \\(\\theta_2\\) | 0 | 25 | 0 |",
            "| 3 | \\(\\theta_3+90^\\circ\\) | 0 | 0 | \\(+90^\\circ\\) |",
            "| 4 | \\(90^\\circ\\) (fixed) | \\(d_4\\) | 0 | \\(+90^\\circ\\) |",
            "| 5 | \\(\\theta_5\\) | 5 | 0 | \\(-90^\\circ\\) |",
            "| 6 | \\(\\theta_6\\) | 12 | 0 | 0 |"]:
    has(row)
# T23 with theta = theta3 + 90 deg, alpha = +90 deg
t3 = sp.symbols("theta3")
ct, st = sp.cos(t3 + sp.pi / 2), sp.sin(t3 + sp.pi / 2)
T23 = sp.Matrix([[ct, 0, st, 0], [st, 0, -ct, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
assert sp.simplify(T23 - sp.Matrix([[-sp.sin(t3), 0, sp.cos(t3), 0], [sp.cos(t3), 0, sp.sin(t3), 0], [0, 1, 0, 0], [0, 0, 0, 1]])) == sp.zeros(4)
has("-S_3&0&C_3&0\\\\C_3&0&S_3&0\\\\0&1&0&0")
has("C_2&-S_2&0&25C_2\\\\S_2&C_2&0&25S_2")
has("C_1&0&S_1&0\\\\S_1&0&-C_1&0\\\\0&1&0&30")

# ---------------- Q2: robot control ----------------
wres = 2 * math.pi * 2                          # lowest resonance 2 Hz
wn = 0.5 * wres
kv, kp = 2 * 1.1 * wn, wn ** 2
kvf, kpf = 2 * 1.0 * wn, wn ** 2
K["q2_wn"], K["q2_kv"], K["q2_kp"] = round(wn, 4), round(kv, 4), round(kp, 4)
K["q2_kvf"], K["q2_kpf"] = round(kvf, 4), round(kpf, 4)
assert (K["q2_wn"], K["q2_kv"], K["q2_kp"], K["q2_kvf"]) == (6.2832, 13.823, 39.4784, 12.5664)
for s in ("6.2832", "13.823", "39.478", "12.566"):
    has(s)
q2, dq1, dq2 = math.pi / 3, 1.0, -1.0
v1 = 0 + kv * (-0.1) + kp * 0.05
v2 = 0.2 + kv * 0.05 + kp * (-0.02)
u1 = (5 + 2 * math.cos(q2)) * v1 + (1 + math.cos(q2)) * v2 - math.sin(q2) * (2 * dq1 * dq2 + dq2 ** 2) + 3 * dq1
K["q2_v1"], K["q2_v2"], K["q2_u1"] = round(v1, 4), round(v2, 4), round(u1, 3)
assert (K["q2_v1"], K["q2_v2"], K["q2_u1"]) == (0.5916, 0.1016, 7.568), (v1, v2, u1)
for s in ("0.5916", "0.1016", "7.568"):
    has(s)
# mass matrix is positive definite for every q2: det = 4 - cos^2 q2 > 0
c = sp.symbols("c")
assert sp.expand((5 + 2 * c) * 1 - (1 + c) ** 2) == 4 - c ** 2
# (b) steady state q3 for fd = 10 N, ke = 40, xe = 0.3
K["q2_q3ss"] = 0.3 + 10 / 40
assert K["q2_q3ss"] == 0.55
has("0.55")
# (c) d3 = 2 N inside the force subspace: f'' = ke (v3 - d3/m3) -> rhs = ke d3 / m3
m3, ke, d3 = 4, 40, 2
rhs = ke * d3 / m3
K["q2_rhs"], K["q2_efss"] = rhs, round(rhs / kpf, 4)
assert rhs == 20 and K["q2_efss"] == 0.5066
has("0.5066")
# confirm by integrating q3 dynamics with the force servo
q3, dq3, dt, fd = 0.3, 0.0, 1e-4, 10.0
for _ in range(int(6 / dt)):
    f = ke * (q3 - 0.3)
    ef, def_ = fd - f, -ke * dq3
    v3 = (kvf * def_ + kpf * ef) / ke
    u3 = m3 * v3 + 2 * dq3 + 39.2 + f
    ddq3 = (u3 - 2 * dq3 - 39.2 - f - d3) / m3
    dq3 += ddq3 * dt; q3 += dq3 * dt
assert abs((fd - ke * (q3 - 0.3)) - rhs / kpf) < 1e-3

# ---------------- Q3(a): wheels ----------------
def wheel(px, py, alpha_plus_beta):
    al_ = math.atan2(py, px); l = math.hypot(px, py); be = alpha_plus_beta - al_
    roll = [math.sin(al_ + be), -math.cos(al_ + be), -l * math.cos(be)]
    slide = [math.cos(al_ + be), math.sin(al_ + be), l * math.sin(be)]
    return al_, be, l, [round(v, 6) for v in roll], [round(v, 6) for v in slide]


A = wheel(-0.2, 0.15, math.pi / 2)
B = wheel(-0.2, -0.15, math.pi / 2)
assert A[3] == [1, 0, -0.15] and A[4] == [0, 1, -0.2], A
assert B[3] == [1, 0, 0.15] and B[4] == [0, 1, -0.2], B
K["q3_alphaA_deg"], K["q3_betaA_deg"] = round(math.degrees(A[0]), 2), round(math.degrees(A[1]), 2)
K["q3_l"] = round(A[2], 6)
assert (K["q3_alphaA_deg"], K["q3_betaA_deg"], K["q3_l"]) == (143.13, -53.13, 0.25)
has("143.13"); has("−53.13°")
# physical check: wheel-point velocity = (xdot - thdot*py, ydot + thdot*px)
for (px, py), w in (((-0.2, 0.15), A), ((-0.2, -0.15), B)):
    xd, yd, t = 0.37, -0.11, 0.9
    vx, vy = xd - t * py, yd + t * px
    assert abs(w[3][0] * xd + w[3][1] * yd + w[3][2] * t - vx) < 1e-9
    assert abs(w[4][0] * xd + w[4][1] * yd + w[4][2] * t - vy) < 1e-9
xd, td = 0.4, 0.5
yd = 0.2 * td                                    # rear sliding rows force ydot = 0.2 thdot
K["q3_ydot"] = yd
pA, pB = (xd - 0.15 * td) / 0.05, (xd + 0.15 * td) / 0.05
K["q3_phiA"], K["q3_phiB"] = round(pA, 4), round(pB, 4)
assert (K["q3_ydot"], K["q3_phiA"], K["q3_phiB"]) == (0.1, 6.5, 9.5)
be = math.pi - math.atan(1.6)                    # 0.4 cos b + (0.1 + 0.3*0.5) sin b = 0
assert abs(0.4 * math.cos(be) + 0.25 * math.sin(be)) < 1e-12
pC = (0.4 * math.sin(be) - 0.1 * math.cos(be) - 0.3 * math.cos(be) * td) / 0.04
K["q3_betaC"], K["q3_phiC"] = round(be, 4), round(pC, 3)
assert (K["q3_betaC"], K["q3_phiC"]) == (2.1294, 11.792), (be, pC)
assert abs(pC * 0.04 - math.hypot(0.4, 0.1 + 0.3 * td)) < 1e-12   # wheel speed = point speed
for s in ("0.1", "6.5", "9.5", "2.1294", "11.792"):
    has(s)

# ---------------- Q3(b): SCARA-type arm ----------------
q1s, q2s, q3s, q4s = sp.symbols("q1 q2 q3 q4")
p = sp.Matrix([0.3 * sp.cos(q1s) + 0.2 * sp.cos(q1s + q2s), 0.3 * sp.sin(q1s) + 0.2 * sp.sin(q1s + q2s), 0.45 - q3s])
w = sp.Matrix([*p, 0, 0, -sp.exp(q4s / sp.pi)])
V = w.jacobian([q1s, q2s, q3s, q4s])
assert V[:, 2] == sp.Matrix([0, 0, -1, 0, 0, 0])
assert sp.simplify(V[5, 3] + sp.exp(q4s / sp.pi) / sp.pi) == 0
tx, ty, tz = 0.1, 0.4, 0.2
q4v = math.pi * 0.25
q3v = 0.45 - tz
c2 = (tx ** 2 + ty ** 2 - 0.09 - 0.04) / (2 * 0.3 * 0.2)
assert abs(c2 - 1 / 3) < 1e-12
sols = []
for sgn in (1, -1):
    q2v = sgn * math.acos(c2)
    q1v = math.atan2(ty, tx) - math.atan2(0.2 * math.sin(q2v), 0.3 + 0.2 * math.cos(q2v))
    pv = [float(e) for e in p.subs({q1s: q1v, q2s: q2v, q3s: q3v})]
    assert max(abs(pv[0] - tx), abs(pv[1] - ty), abs(pv[2] - tz)) < 1e-12
    sols.append((round(q1v, 4), round(q2v, 4)))
K["q3_q3"], K["q3_q4"], K["q3_sols"] = q3v, round(q4v, 4), sols
assert sols == [(0.8508, 1.231), (1.8008, -1.231)], sols
for s in ("0.25", "0.7854", "0.8508", "1.2310", "1.8008"):
    has(s)

# ---------------- Q4: homography groups ----------------
P = {1: (0, 0), 2: (3, 0), 3: (6, 0), 4: (3, 3), 5: (0, 6), 6: (0, 3), 7: (2, 2)}
col = lambda i, j, k: (P[j][0] - P[i][0]) * (P[k][1] - P[i][1]) - (P[j][1] - P[i][1]) * (P[k][0] - P[i][0]) == 0
triples = [t for t in itertools.combinations(P, 3) if col(*t)]
assert triples == [(1, 2, 3), (1, 4, 7), (1, 5, 6), (2, 5, 7), (3, 4, 5), (3, 6, 7)], triples
valid = lambda S: [g for g in itertools.combinations(sorted(S), 4) if not any(col(*t) for t in itertools.combinations(g, 3))]
Fa, Fb, Fc, Fc2 = {1, 2, 3, 6, 7}, set(P), {3, 4, 5, 6, 7}, {3, 4, 5, 7}
K["q4_all"] = len(valid(P))
K["q4_G"], K["q4_H"], K["q4_K_direct"] = valid(Fa & Fb), valid(Fb & Fc), valid(Fa & Fc)
K["q4_H_alt"] = valid(Fb & Fc2)
assert K["q4_all"] == 11 and K["q4_G"] == [(1, 2, 6, 7)] and K["q4_H"] == [(4, 5, 6, 7)]
assert K["q4_K_direct"] == [] and len(Fa & Fc) == 3 and K["q4_H_alt"] == [] and len(Fa & Fc2) == 2
has("\\{O_1,O_2,O_6,O_7\\}"); has("\\{O_4,O_5,O_6,O_7\\}")
# the 8x8 system for the chosen G group is non-singular for a generic projective image
Hs = sp.Matrix([[1.1, 0.2, 0.3], [-0.1, 0.9, 0.4], [0.05, 0.02, 1]])
Mrows = []
for i in (1, 2, 6, 7):
    ax, ay = P[i]; b = Hs * sp.Matrix([ax, ay, 1]); bx, by = b[0] / b[2], b[1] / b[2]
    Mrows += [[ax, ay, 1, 0, 0, 0, -ax * bx, -ay * bx], [0, 0, 0, ax, ay, 1, -ax * by, -ay * by]]
assert abs(sp.Matrix(Mrows).det()) > 1e-9
# a group with three collinear points makes it singular
Mrows = []
for i in (1, 2, 3, 6):
    ax, ay = P[i]; b = Hs * sp.Matrix([ax, ay, 1]); bx, by = b[0] / b[2], b[1] / b[2]
    Mrows += [[ax, ay, 1, 0, 0, 0, -ax * bx, -ay * bx], [0, 0, 0, ax, ay, 1, -ax * by, -ay * by]]
assert abs(sp.Matrix(Mrows).det()) < 1e-9

# ---------------- Q5: grouped sensors (variances in units of a^2) ----------------
var = [F(1), F(2), F(4), F(4)]
pk = sp.symbols("p", positive=True)
Ls = sp.symbols("L1:5")
pn = (1 - sum(Ls)) ** 2 * pk + sum(L ** 2 * s for L, s in zip(Ls, var))
sol = sp.solve([sp.diff(pn, L) for L in Ls], Ls, dict=True)[0]
S = sum(1 / s for s in var)
assert S == 2
for L, s in zip(Ls, var):
    assert sp.simplify(sol[L] - pk / (s * (1 + pk * S))) == 0
assert sp.simplify(1 / pn.subs(sol) - (1 / pk + S)) == 0
gains = [sol[L].subs(pk, 1) for L in Ls]
K["q5_gains_at_p1"] = [str(g) for g in gains]
assert gains == [F(1, 3), F(1, 6), F(1, 12), F(1, 12)]
assert pn.subs(sol).subs(pk, 1) == F(1, 3)
has("1/3"); has("1/6"); has("1/12")
# (b) S1 alone vs S2-S4 with separate gains: information 1 vs 1/2 + 1/4 + 1/4 = 1 -> equal
infoA, infoB = 1 / var[0], sum(1 / s for s in var[1:])
assert infoA == infoB == 1
# (c) S2-S4 with one shared gain: p+ = (1-3L)^2 p + L^2 * sum(var)
L = sp.symbols("L")
pn1 = (1 - 3 * L) ** 2 * pk + L ** 2 * sum(var[1:])
Lopt = sp.solve(sp.diff(pn1, L), L)[0]
assert sp.simplify(Lopt - 3 * pk / (9 * pk + 10)) == 0
assert sp.simplify(1 / pn1.subs(L, Lopt) - (1 / pk + sp.Rational(9, 10))) == 0
assert sp.Rational(9, 10) < infoA
K["q5_shared_info"] = "9/10"
assert pn1.subs(L, Lopt).subs(pk, 1) == F(10, 19)
assert 1 / (1 + infoA) == F(1, 2)
assert Lopt.subs(pk, 1) == F(3, 19)
has("9/10"); has("10/19"); has("3/19")

# ---------------- the paper page carries no answers ----------------
for leak in ("143.13", "6.2832", "0.5066", "0.8508", "10/19", "O_1,O_2,O_6,O_7", "57, 35"):
    assert leak not in PAGE, leak
items = re.findall(r'data-item="([^"]+)"', PAGE)
assert len(items) == len(set(items)) == 13, items
for img in re.findall(r'<img src="([^"]+)"', PAGE):
    assert (HERE / img).exists(), img
print(json.dumps(K))
