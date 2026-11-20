"""Independent key checker for the EE6221 final-prep pages.

Recomputes every numeric key and asserts that the keys embedded in final-primer.html and
final-mock-a-guided.html (JSON in <script id="keys">) match.  Also asserts that every cited PDF and
every pop-up page image exists, and that progress keys are unique.
Run:  python3 final-check.py   (prints the keys; exits non-zero on any problem)
"""
import itertools, json, math, re, sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
r4 = lambda v: round(float(v), 4)


def dh(theta, d, a, alpha):
    ct, st, ca, sa = math.cos(theta), math.sin(theta), math.cos(alpha), math.sin(alpha)
    return [[ct, -ca * st, sa * st, a * ct], [st, ca * ct, -sa * ct, a * st], [0, sa, ca, d], [0, 0, 0, 1]]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def collinear(p, q, s):
    return (q[0] - p[0]) * (s[1] - p[1]) - (q[1] - p[1]) * (s[0] - p[0]) == 0


def good_groups(pts):
    return sum(1 for g in itertools.combinations(pts, 4)
               if not any(collinear(*t) for t in itertools.combinations(g, 3)))


def kalman_separate(p, sig2):
    S = sum(F(1) / s for s in sig2)
    L = [p / (s * (1 + p * S)) for s in sig2]
    pn = (1 - sum(L)) ** 2 * p + sum(l * l * s for l, s in zip(L, sig2))
    assert pn == 1 / (1 / p + S)
    return L, pn


def kalman_single(p, sig2):
    n = len(sig2); L = n * p / (n * n * p + sum(sig2))
    pn = (1 - n * L) ** 2 * p + L * L * sum(sig2)
    assert pn == 1 / (1 / p + F(n * n) / sum(sig2))
    return L, pn


# ---------------- primer ----------------
P = {}
P["c1"] = r4(5 * 2 ** 2 - 2 * math.cos(0))                          # beta of 3θθ'' + 5θ'^2 − 2cosθ at θ=0, θ'=2
wn = 0.5 * min(10, 18, 30); P["c2"] = r4(2 * 1.25 * wn); P["c2b"] = r4(wn ** 2)
P["c3"] = r4(F(3, 2 * 36))                                           # e_ss = d/(m kp)
P["c4"] = r4(F(1, 25) * (0 + 8 * (-1) + 16 * 1))                     # v = (1/ke)(f''d + kvf ef' + kpf ef)
P["c6"] = r4(1 * math.sqrt(32 / 30))                                 # ζ' = ζ √ρ
P["m1"] = r4(-0.25 * math.cos(math.pi))                              # −l cos β for β = π
P["m3"] = r4((0.4 - 0.2 * 1) / 0.05)                                 # φ' = (ẋ − l θ')/r
P["ik"] = r4(math.atan2(0.1, -0.1))
P["h1"] = good_groups([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])      # one collinear triple
P["k1"] = r4(kalman_separate(F(1), [F(1), F(4)])[1])

# ---------------- guided mock A ----------------
G = {}
# Q1: 23-24 S2 six-joint arm, D-H table from quiz-01-mock-05.md
TAB = [(None, 0.47, 0, math.pi / 2), (None, 0.16, 0.15, math.pi / 2), (None, 0, 0.18, 0),
       (None, 0, 0.17, -math.pi / 2), (None, 0.05, 0, math.pi / 2), (None, 0.20, 0, 0)]
G["q1_r1"] = [0.47, 0]; G["q1_r2"] = [0.16, 0.15]; G["q1_r34"] = [0.18, 0.17]; G["q1_r56"] = [0.05, 0.20]
q = [math.radians(v) for v in (90, -90, 90, 0, 90, 0)]
T = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
for qi, (_, d, a, al) in zip(q, TAB):
    T = mm(T, dh(qi, d, a, al))
tip = [r4(T[i][3]) for i in range(3)]
assert tip == [0.71, 0.0, 0.37], tip                                 # matches the mock-05 key
G["q1_tip"] = [tip[0], tip[2]]
# Q2(a): computed torque.  Dynamics:
#  (3+cos q2) q1'' + q2'' − 2 q1' q2' sin q2 + 15 cos q1 + d1 = u1
#  q1'' + q2'' + q1'^2 sin q2 + 5 cos(q1+q2) + d2 = u2
#  8 q3'' + 4 q3' + 78.4 + f = u3          resonances 12, 20, 30 rad/s
wn = 0.5 * min(12, 20, 30); G["q2a_wn"] = r4(wn)
G["q2a_k"] = [r4(2 * 1.2 * wn), r4(wn ** 2)]
G["q2a_b3"] = r4(4 * 0.5 + 78.4)
q1, q2, dq1, dq2 = 0, math.pi / 2, 1, 2
v1 = 0 + 14.4 * (-0.2) + 36 * 0.1; v2 = 0.5 + 14.4 * 0.1 + 36 * (-0.05)
G["q2a_v"] = [r4(v1), r4(v2)]
G["q2a_u1"] = r4((3 + math.cos(q2)) * v1 + 1 * v2 - 2 * dq1 * dq2 * math.sin(q2) + 15 * math.cos(q1))
# Q2(b): f = 30(q3 − 0.15); motion ζ = 1.05, force critically damped; constant d = (2, 1)
G["q2b_km"] = [r4(2 * 1.05 * wn), r4(wn ** 2)]
G["q2b_kf"] = [r4(2 * 1 * wn), r4(wn ** 2)]
v3 = F(1, 30) * (0 + 12 * F(-3, 10) + 36 * F(6, 10)); G["q2b_v3"] = r4(v3)
G["q2b_u3"] = r4(8 * v3 + 4 * 0 + F(784, 10) + 30 * (F(17, 100) - F(15, 100)))
Mb = [[3, 1], [1, 1]]; det = Mb[0][0] * Mb[1][1] - Mb[0][1] * Mb[1][0]
Minv_d = [F(Mb[1][1] * 2 - Mb[0][1] * 1, det), F(-Mb[1][0] * 2 + Mb[0][0] * 1, det)]
G["q2b_ess"] = [r4(x / 36) for x in Minv_d]
# Q2(c): true stiffness 32, controller uses 30
rho = F(32, 30); G["q2c_rho"] = r4(rho)
wn2 = math.sqrt(36 * rho); G["q2c_wn"] = r4(wn2); G["q2c_zeta"] = r4(12 * rho / (2 * wn2))
assert wn2 > 6                                                       # breaks ω_n ≤ 0.5·12
# Q3(a): fixed A at (0, 0.25), fixed B at (0, −0.25), r = 0.05; steered C at (0.4, 0), r = 0.04
xd, yd, th = 0.3, 0.0, 0.5
def j_row(al, be, l): return [math.sin(al + be), -math.cos(al + be), -l * math.cos(be)]
def c_row(al, be, l): return [math.cos(al + be), math.sin(al + be), l * math.sin(be)]
dot = lambda u, v: sum(a * b for a, b in zip(u, v))
xi = [xd, yd, th]
G["q3a_jB"] = [r4(v) + 0.0 for v in j_row(-math.pi / 2, math.pi, 0.25)]
G["q3a_phiA"] = r4(dot(j_row(math.pi / 2, 0, 0.25), xi) / 0.05)
G["q3a_phiB"] = r4(dot(j_row(-math.pi / 2, math.pi, 0.25), xi) / 0.05)
assert abs(dot(c_row(math.pi / 2, 0, 0.25), xi)) < 1e-12 and abs(dot(c_row(-math.pi / 2, math.pi, 0.25), xi)) < 1e-12
bC = math.atan2(-0.3, 0.2)                                           # 0.3 cos β + 0.2 sin β = 0
bC = bC + math.pi if bC < 0 else bC                                  # pick β in (0, π): forward spin
assert abs(dot(c_row(0, bC, 0.4), xi)) < 1e-12
G["q3a_betaC"] = r4(bC); G["q3a_phiC"] = r4(dot(j_row(0, bC, 0.4), xi) / 0.04)
vC = (xd - th * 0, yd + th * 0.4)                                    # rigid-body check: v = v_P + θ' × r
assert abs(math.hypot(*vC) - 0.04 * G["q3a_phiC"]) < 1e-3
# Q3(b): p = [C1(q2 + 0.2 C3), S1(q2 + 0.2 C3), 0.3 − 0.2 S3], target (0.3, 0.3, 0.2)
x, y, z = 0.3, 0.3, 0.2
a1 = math.atan2(y, x); a3 = math.asin((0.3 - z) / 0.2); a2 = math.hypot(x, y) - 0.2 * math.cos(a3)
G["q3b_q"] = [r4(a1), r4(a2), r4(a3)]
pp = lambda a, b, c: [math.cos(a) * (b + 0.2 * math.cos(c)), math.sin(a) * (b + 0.2 * math.cos(c)), 0.3 - 0.2 * math.sin(c)]
assert all(abs(u - v) < 1e-12 for u, v in zip(pp(a1, a2, a3), (x, y, z)))
G["q3b_dp3"] = [r4(-0.2 * math.cos(a1) * math.sin(a3)), r4(-0.2 * math.sin(a1) * math.sin(a3)), r4(-0.2 * math.cos(a3))]
# Q4: object-plane layout O1..O8
O = {1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (3, 0), 5: (0, 1), 6: (1, 1), 7: (2, 1), 8: (0, 2)}
lines = sorted(tuple(sorted(t)) for t in itertools.combinations(O, 3) if collinear(*(O[i] for i in t)))
assert lines == [(1, 2, 3), (1, 2, 4), (1, 3, 4), (1, 5, 8), (2, 3, 4), (3, 6, 8), (5, 6, 7)], lines
G["q4_G"] = good_groups([O[i] for i in range(1, 8)])                 # F_a sees O1..O7, F_b all
G["q4_H"] = good_groups([O[i] for i in range(4, 9)])                 # F_c sees O4..O8
G["q4_Kdirect"] = good_groups([O[i] for i in range(4, 8)])
G["q4_row"] = r4(-0.2 * 0.3)
# Q5: three sensors 2a², 3a², 6a²; a = 1, p_k = 1
L, pn = kalman_separate(F(1), [F(2), F(3), F(6)])
G["q5_L"] = [r4(v) for v in L]; G["q5_p"] = r4(pn)
Ls, ps = kalman_single(F(1), [F(2), F(3), F(6)])
G["q5_Ls"] = r4(Ls); G["q5_ps"] = r4(ps)
G["q5_info"] = [r4(sum(F(1) / s for s in (2, 3, 6))), r4(F(9, 11))]
# select / geometry keys
G["q2b_sub"] = "q3"                                                  # f depends on q3 only
G["q2c_ok"] = "no" if wn2 > 0.5 * 12 else "yes"
G["q3a_A"] = [r4(math.pi / 2), 0.0]; G["q3a_B"] = [r4(-math.pi / 2), r4(math.pi)]
assert dot(j_row(math.pi / 2, 0, 0.25), [1, 0, 0]) > 0 and dot(j_row(-math.pi / 2, math.pi, 0.25), [1, 0, 0]) > 0


def page_checks(f):
    bad = 0; txt = f.read_text()
    for href in re.findall(r'href="(\.\./resources/[^"#]+)', txt):
        if not (HERE / href).exists(): bad += 1; print("MISSING PDF", f.name, href)
    for spec in re.findall(r'data-pages="([^"]+)"', txt):
        stem, pages = spec.split(":")
        for p in pages.split(","):
            img = HERE / "final-pages" / f"{stem}-p{int(p):03d}.jpg"
            if not img.exists(): bad += 1; print("MISSING IMAGE", f.name, img.name)
    ids = re.findall(r'data-k="([^"]+)"', txt) + re.findall(r'data-id="([^"]+)"', txt)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: bad += 1; print("DUPLICATE progress keys", f.name, dup)
    return bad


if __name__ == "__main__":
    print(json.dumps({"primer": P, "guided": G}))
    bad = 0
    for fname, ref in (("final-primer.html", P), ("final-mock-a-guided.html", G)):
        f = HERE / fname
        if not f.exists():
            print("skip (missing):", fname); continue
        emb = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', f.read_text(), re.S).group(1))
        for k, v in ref.items():
            if json.dumps(emb.get(k)) != json.dumps(v):
                bad += 1; print("MISMATCH", fname, k, emb.get(k), "!=", v)
        extra = set(emb) - set(ref)
        if extra: bad += 1; print("UNVERIFIED keys in", fname, extra)
        bad += page_checks(f)
    print("OK" if not bad else f"{bad} problem(s)"); sys.exit(1 if bad else 0)
