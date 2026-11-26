"""Independent key checker for final-relearn-q2-q5.html.

Recomputes every key (gains, force servo, wheel rows from hub-velocity projection, platform
speeds, IK with forward-kinematics substitution, homography rows and brute-force group counts,
Kalman gains by direct minimisation), then checks that the page keys match, that progress keys
are unique, that distractor feedback names wrong options, and that every cited page image exists.
Run:  python3 final-relearn-q2-q5-check.py
"""
import itertools, json, math, re
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = (HERE / "final-relearn-q2-q5.html").read_text()
r6 = lambda x: round(x, 6)
K = {}

# Part 1: Hz -> rad/s before halving; one-joint computed torque.
wn = 0.5 * (2 * math.pi * min(1.5, 4))
K["c_gain"] = [r6(wn), r6(wn ** 2), r6(2 * 1 * wn)]
v = 0.3 + 10 * -0.2 + 25 * 0.1
K["c_u"] = [r6(v), r6(4 * v + 2 * 0.5 + 39.2)]

# Part 2: force servo with 1/ke; steady state.
v3 = (0 + 10 * -2 + 25 * 4) / 50
K["h_u3"] = [r6(v3), r6(5 * v3 + 3 * 0.2 + 49 + 12)]
K["h_ss"] = r6(0.2 + 15 / 50)
K["h_tf"] = "false"

# Part 3: force-subspace disturbance; confirm by integrating the closed loop.
ke, m, kvf, kpf, d = 50, 5, 10, 25, 1.5
K["d_force"] = [r6(ke * d / m), r6(ke * d / (m * kpf)), r6(d / (m * kpf))]
q, dq, fd, dt = 0.2, 0.0, 15.0, 1e-4
for _ in range(int(10 / dt)):
    f = ke * (q - 0.2); ef = fd - f; def_ = -ke * dq
    vv = (kvf * def_ + kpf * ef) / ke
    u = m * vv + 3 * dq + 49 + f
    ddq = (u - 3 * dq - 49 - f - d) / m
    dq += ddq * dt; q += dq * dt
assert abs((fd - ke * (q - 0.2)) - K["d_force"][1]) < 1e-3

# Parts 4-5: wheel geometry, and rows from projecting the hub velocity (independent of the slide formula).
def geo(x, y, roll_dir=0.0):
    l = math.hypot(x, y); a = math.degrees(math.atan2(y, x)); b = (roll_dir + 90 - a + 180) % 360 - 180
    return l, a, b
def rows(x, y, ab):                       # coefficient of (xdot, ydot, thetadot) in v_hub . direction
    s = math.radians(ab)
    axle, roll = (math.cos(s), math.sin(s)), (math.sin(s), -math.cos(s))
    hub = lambda dirn: [dirn[0], dirn[1], -y * dirn[0] + x * dirn[1]]
    return [r6(c) + 0.0 for c in hub(roll) + hub(axle)]
l, a, b = geo(-0.3, 0.4)
K["w_geo"] = [r6(l), r6(a), r6(b)]
_, a2, b2 = geo(-0.3, -0.4)
K["w_geo2"] = [r6(a2), r6(b2)]
K["w_tf"] = "false"
K["w_rows"] = rows(-0.3, 0.4, a + b)
assert K["w_rows"] == [1, 0, -0.4, 0, 1, -0.3]
K["w_rowsC"] = rows(0.3, 0, 120)
# cross-check against the slide formula [sin(a+b), -cos(a+b), -l cos b], [cos(a+b), sin(a+b), l sin b]
B = math.radians(120)
assert K["w_rowsC"] == [r6(math.sin(B)), r6(-math.cos(B)), r6(-0.3 * math.cos(B)), r6(math.cos(B)), r6(math.sin(B)), r6(0.3 * math.sin(B))]

# Part 6: speeds.
xd, th = 0.5, 0.4
yd = 0.3 * th                                   # sliding of fixed wheels: yd + th * (-0.3) = 0
hubC = (xd, yd + 0.3 * th)
bC = math.atan2(hubC[0], -hubC[1])              # axle (cos b, sin b) perpendicular to hub velocity, b in (0, pi)
assert 0 < bC < math.pi and abs(hubC[0] * math.cos(bC) + hubC[1] * math.sin(bC)) < 1e-12
phiC = (hubC[0] * math.sin(bC) - hubC[1] * math.cos(bC)) / 0.04
assert abs(phiC - math.hypot(*hubC) / 0.04) < 1e-9
K["w_speed"] = [r6(yd), r6((xd - 0.4 * th) / 0.05), r6((xd + 0.4 * th) / 0.05), r6(bC), r6(phiC)]

# Part 7: IK, checked by substituting back.
X, Y, Z, w6 = 0.5, 0.2, 0.25, -math.exp(0.5)
q4 = math.pi * math.log(abs(w6)); q3 = 0.6 - Z
C2 = (X * X + Y * Y - 0.4 ** 2 - 0.3 ** 2) / (2 * 0.4 * 0.3)
for s in (1, -1):
    q2 = s * math.acos(C2); q1 = math.atan2(Y, X) - math.atan2(0.3 * math.sin(q2), 0.4 + 0.3 * math.cos(q2))
    assert abs(0.4 * math.cos(q1) + 0.3 * math.cos(q1 + q2) - X) < 1e-12 and abs(0.4 * math.sin(q1) + 0.3 * math.sin(q1 + q2) - Y) < 1e-12
    if s == 1: K["ik"] = [r6(q4), r6(q3), r6(C2), r6(q2), r6(q1)]
h = 1e-6
K["ikV"] = [r6((-math.exp((math.pi / 2 + h) / math.pi) + math.exp((math.pi / 2 - h) / math.pi)) / (2 * h)), -1]

# Part 8: homography rows, verified against a real homography; brute-force group counts.
ax, ay, bx, by = 2, 1, 3, 4
K["hg_row"] = [-ax * bx, -ay * bx, -ax * by, -ay * by]
def collinear(p, q_, r):
    return (q_[0] - p[0]) * (r[1] - p[1]) - (q_[1] - p[1]) * (r[0] - p[0]) == 0
def count(P):
    return sum(1 for g in itertools.combinations(P, 4) if not any(collinear(*t) for t in itertools.combinations(g, 3)))
K["hg_count"] = [count([(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]), count([(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1)])]
G = [[F(1), F(2), F(3)], [F(-1), F(2), F(1)], [F(1, 5), F(1, 7), F(1)]]
for pa in [(2, 1), (0, 3), (-1, 4)]:
    m3 = [sum(G[i][0] * pa[0] + G[i][1] * pa[1] + G[i][2] for _ in [0]) for i in range(3)]
    pb = (m3[0] / m3[2], m3[1] / m3[2]); g = [G[0][0], G[0][1], G[0][2], G[1][0], G[1][1], G[1][2], G[2][0], G[2][1]]
    r1 = [pa[0], pa[1], 1, 0, 0, 0, -pa[0] * pb[0], -pa[1] * pb[0]]; r2 = [0, 0, 0, pa[0], pa[1], 1, -pa[0] * pb[1], -pa[1] * pb[1]]
    assert sum(x * y for x, y in zip(r1, g)) == pb[0] and sum(x * y for x, y in zip(r2, g)) == pb[1]
K["hg_chain"] = ["HG", "false"]

# Part 9: Kalman, by brute minimisation of p+ = (1 - sum L)^2 p + sum L^2 s^2.
s2, p = [2, 3, 6], 1
info = F(1, p) + sum(F(1, v) for v in s2); pp = 1 / info
L = [pp / v for v in s2]
grad = [-2 * (1 - sum(L)) * p + 2 * L[i] * s2[i] for i in range(3)]
assert all(gi == 0 for gi in grad)
K["k_sep"] = [float(pp)] + [r6(float(x)) for x in L]
n = 3; Ls = F(n * p, n * n * p + sum(s2)); ps = (1 - n * Ls) ** 2 * p + Ls ** 2 * sum(s2)
assert -2 * n * (1 - n * Ls) * p + 2 * Ls * sum(s2) == 0
K["k_shared"] = [float(Ls), float(ps)]

page_keys = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', PAGE, re.S).group(1))
bad = [k for k in set(K) | set(page_keys) if K.get(k) != page_keys.get(k)]
assert not bad, {k: (K.get(k), page_keys.get(k)) for k in bad}

ids = re.findall(r'data-(?:k|id)="([^"]+)"', PAGE)
assert len(ids) == len(set(ids)), "duplicate progress keys"
assert set(K) <= set(ids), set(K) - set(ids)
for step in re.findall(r'<div class="step[^"]*" data-k="([^"]+)">(.*?)</div>', PAGE, re.S):
    sid, html = step
    nin = len(re.findall(r"<input size", html)) + len(re.findall(r"<select", html))
    assert nin == (len(K[sid]) if isinstance(K[sid], list) else 1), (sid, nin)
    for i, (_, fb, opts) in enumerate(re.findall(r"<select( data-fb='([^']*)')?>(.*?)</select>", html, re.S)):
        if fb:
            ans = K[sid][i] if isinstance(K[sid], list) else K[sid]
            vals = re.findall(r'<option value="([^"]*)"', opts)
            for v in json.loads(fb): assert v in vals and v != ans, (sid, v)
# every Part ends with a check
parts = re.split(r'<h2 id="p\d+"', PAGE)[1:]
assert all('class="step' in s for s in parts[:-1]), "a Part has no check"
for href, pages in re.findall(r'href="([^"#]+)#page=\d+" data-pages="([^"]+)"', PAGE):
    assert (HERE / href).resolve().exists(), href
    stem, nums = pages.split(":"); nums = [int(x) for x in nums.split(",")]
    assert nums == list(range(nums[0], nums[-1] + 1)), pages
    for x in nums:
        assert (HERE / "final-pages" / f"{stem}-p{x:03d}.jpg").exists(), (stem, x)
print(json.dumps(K))
