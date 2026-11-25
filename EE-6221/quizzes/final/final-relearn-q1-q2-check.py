"""Independent key checker for final-relearn-q1-q2.html.

Recomputes every key from geometry (D-H forward kinematics, cross products) and the
computed-torque formulas, asserts that the page's embedded keys match, that every distractor
feedback map is valid JSON naming a real wrong option, that progress keys are unique, and that
every cited PDF and pop-up image exists with no gap inside a cited range.
Run:  python3 final-relearn-q1-q2-check.py
"""
import json, math, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = (HERE / "final-relearn-q1-q2.html").read_text()

# World frame of the sketch: right = +x, up = +z, into page = +y (x0 right, z0 up).
V = {"right": (1, 0, 0), "left": (-1, 0, 0), "up": (0, 0, 1), "down": (0, 0, -1), "in": (0, 1, 0), "out": (0, -1, 0)}
NAME = {v: k for k, v in V.items()}
cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
neg = lambda a: tuple(-c for c in a)


def alpha(z_prev, x, z):                     # quarter-turn twist about x carrying z_prev onto z
    c = cross(z_prev, z)
    return 90 if c == x else -90 if c == neg(x) else (0 if z_prev == z else None)


def dh(t, d, a, al):
    t, al = math.radians(t), math.radians(al)
    ct, st, ca, sa = math.cos(t), math.sin(t), math.cos(al), math.sin(al)
    return [[ct, -ca * st, sa * st, a * ct], [st, ca * ct, -sa * ct, a * st], [0, sa, ca, d], [0, 0, 0, 1]]


def fk(rows):
    M = [[float(i == j) for j in range(4)] for i in range(4)]
    for r in rows:
        T = dh(*r); M = [[sum(M[i][k] * T[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    return M


K = {}
K["r_theta"] = "false"                        # θ of a revolute joint is the variable (Lec 1 p. 56)
# Figure 1 dimensions -> cells: verified below by FK reproducing the figure's tip.
K["r_dim1"] = ["d1", "d2", "a2", "a3"]
K["r_dim2"] = ["a4", "d5", "d6"]
cells = dict(zip(K["r_dim1"] + K["r_dim2"], [.47, .16, .15, .18, .17, .05, .20]))
c = lambda n: cells.get(n, 0)
z = {0: V["up"], 1: V["right"], 2: V["in"], 3: V["in"], 4: V["up"], 5: V["right"], 6: V["right"]}
x = {1: V["in"], 2: V["down"], 3: V["right"], 4: V["right"], 5: V["out"], 6: V["out"]}
al = [alpha(z[k - 1], x[k], z[k]) for k in range(1, 7)]
assert al == [90, -90, 0, 90, -90, 0], al
pose = [90, -90, -90, 0, -90, 0]                # the learner's sketched (stretched) pose
rows = [(pose[k], c(f"d{k+1}"), c(f"a{k+1}"), al[k]) for k in range(6)]
M = fk(rows); tip = [round(M[i][3], 6) for i in range(3)]
assert tip == [0.71, 0, 0.37], tip
for k in range(1, 7):                          # every frame's x and z axes match the drawing
    Mk = fk(rows[:k])
    assert tuple(round(Mk[i][0]) for i in range(3)) == x[k] and tuple(round(Mk[i][2]) for i in range(3)) == z[k], k
K["r_alpha"] = [al[3], al[4]]
K["r_alpha_tf"] = "false"
K["r_y"] = [NAME[cross(z[0], V["right"])], NAME[cross(z[1], x[1])], NAME[cross(z[5], x[5])]]
# Retry variant: gripper axis 0.05 below, tool 0.25.
rv = list(rows); rv[4] = (pose[4], -0.05, 0, al[4]); rv[5] = (pose[5], 0.25, 0, al[5])
M = fk(rv); tipv = [round(M[i][3], 6) for i in range(3)]
assert tipv[1] == 0
K["r_retry"] = [0.17, -0.05, 0.25]
K["r_retry_al"] = [al[3], al[4]]
K["r_retry_tip"] = [tipv[0], tipv[2]]
assert K["r_retry_tip"] == [0.76, 0.27]
K["b_class"] = ["alpha", "beta", "beta", "beta", "none", "beta"]
K["b_beta3"] = round(4 * 0.5 + 78.4 + 1.2, 4)
K["b_ess"] = round(6 / (4 * 25), 4)
K["b_known"] = "true"
K["b_kp"] = round(10 / (2 * 0.02), 4)
# Worked example: integrate m(e'' + kv e' + kp e) = d and confirm e_ss = d/(m kp) = 0.05.
m_, kv_, kp_, d_, e_, de_, dt_ = 2, 20, 100, 10, 0.0, 0.0, 1e-4
for _ in range(int(3 / dt_)):
    de_ += (d_ / m_ - kv_ * de_ - kp_ * e_) * dt_; e_ += de_ * dt_
assert abs(e_ - d_ / (m_ * kp_)) < 1e-4 and d_ / (m_ * kp_) == 0.05, e_

# Part 6: official 2024-25 S2 Q1 (wall arm, cm).  Tutor-verified table (quiz-01-mock-05.md Q3).
W = [("t1", 25, 0, 90), ("t2", 11, 0, -90), (-90, "d3", 0, -90), ("t4", 0, 15, -90), ("t5", 4, 0, 90), ("t6", 20, 0, 0)]
K["w_z0"] = "right"; K["w_var"] = "d3"; K["w_theta3"] = "false"
lengths = {25: None, 11: None, 15: None, 4: None, 20: None}
for k, (_, d, a, _) in enumerate(W, 1):
    if isinstance(d, (int, float)) and d: lengths[d] = f"d{k}"
    if a: lengths[a] = f"a{k}"
assert None not in lengths.values(), lengths          # every printed length lands in exactly one cell
K["w_dims"] = [lengths[n] for n in (25, 11, 15, 4, 20)]
K["w_alpha"] = [abs(r[3]) for r in W]
# Straightened pose with d3 = 20: search revolute angles in 90° steps for tip (0, -15, 80) cm
# (z0 out of the wall, y0 down): 25+20+15+20 out, 11+4 up.
import itertools
hit = None
for t1, t2, t4, t5, t6 in itertools.product((0, 90, 180, -90), repeat=5):
    th = {"t1": t1, "t2": t2, "t4": t4, "t5": t5, "t6": t6}
    rows = [(th.get(t, t), 20 if d == "d3" else d, a, al) for t, d, a, al in W]
    M = fk(rows)
    if [round(M[i][3], 6) for i in range(3)] == [0, -15, 80]:
        hit = (t1, t2, t4, t5, t6); break
assert hit, "wall-arm table does not reach (0, -15, 80)"
K["w_tip"] = [80, 15]

# Part 8: official 2024-25 S1 Q2 (3-DOF hybrid position/force control with disturbances).
# Plant: (5 q2^2 + 1) q1'' + ... + d1 = u1;  5 q2'' + ... + d2 = u2;  3 q3'' + 2 q3' + 29.4 + d3 + f = u3
# f = 22(q3 - 0.2), resonances 5, 10, 15 rad/s; motion zeta = 1.05, force zeta = 1.
K["c_sub"] = ["q3", "yes", "no"]
w_res_min = min(5, 10, 15)
wn = 0.5 * w_res_min
K["c_wn"] = wn
zeta_m, zeta_f = 1.05, 1.0
kvm, kpm = round(2 * zeta_m * wn, 6), round(wn ** 2, 6)
kvf, kpf = round(2 * zeta_f * wn, 6), round(wn ** 2, 6)
K["c_gains"] = [kvm, kpm, kvf, kpf]
m3, ke = 3, 22
K["c_v3_coeff"] = round(m3 / ke, 6)
# Spot-check u3 at q3 = 0.25, dq3 = 0.5, ddf_d = 0, ef = 1.6, def = 0.2.
q3_s, dq3_s, ef_s, def_s = 0.25, 0.5, 1.6, 0.2
f_s = round(ke * (q3_s - 0.2), 6)
v3_s = (0 + kvf * def_s + kpf * ef_s) / ke
beta3_s = 2 * dq3_s + 29.4 + f_s
u3_s = round(m3 * v3_s + beta3_s, 6)
K["c_u3"] = [f_s, u3_s]
# Part (b) error-equation RHS at q2 = 1, d1 = 6, d2 = 5, d3 = 3.
q2_e, d1_e, d2_e, d3_e = 1, 6, 5, 3
K["c_dist_rhs"] = [round(d1_e / (5 * q2_e ** 2 + 1), 6), round(d2_e / 5, 6), round(ke * d3_e / m3, 6)]
# Numerically integrate joint 3 plant 3 q3'' + 2 q3' + 29.4 + d3 + f = u3 with constant fd = 10, d3 = 3
# and confirm steady-state force error ef_ss = (22 * d3) / (3 * kpf).
q3_, dq3_, fd_, dt_ = 0.2, 0.0, 10.0, 1e-4
for _ in range(int(12 / dt_)):
    f_ = ke * (q3_ - 0.2)
    df_ = ke * dq3_
    ef_ = fd_ - f_
    def_ = -df_
    v3_ = (kvf * def_ + kpf * ef_) / ke
    u3_ = m3 * v3_ + 2 * dq3_ + 29.4 + f_
    ddq3_ = (u3_ - 2 * dq3_ - 29.4 - d3_e - f_) / m3
    dq3_ += ddq3_ * dt_
    q3_ += dq3_ * dt_
ef_ss_num = fd_ - ke * (q3_ - 0.2)
ef_ss_ana = (ke * d3_e) / (m3 * kpf)
assert abs(ef_ss_num - ef_ss_ana) < 1e-3, (ef_ss_num, ef_ss_ana)

page_keys = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', PAGE, re.S).group(1))
bad = [k for k in set(K) | set(page_keys) if K.get(k) != page_keys.get(k)]
assert not bad, {k: (K.get(k), page_keys.get(k)) for k in bad}

ids = re.findall(r'data-(?:k|id)="([^"]+)"', PAGE)
assert len(ids) == len(set(ids)), "duplicate progress keys"
assert set(K) <= set(ids), set(K) - set(ids)

# Distractor feedback: valid JSON, keys are real options that are wrong answers.
for step in re.findall(r'<div class="step[^"]*" data-k="([^"]+)">(.*?)</div>\s*(?=<div class="step|<!--|<h2|<div class="pit|$)', PAGE, re.S):
    sid, html = step
    sels = re.findall(r"<select( data-fb='([^']*)')?>(.*?)</select>", html, re.S)
    for i, (_, fb, opts) in enumerate(sels):
        if not fb:
            continue
        m = json.loads(fb)
        values = re.findall(r'<option value="([^"]*)"', opts)
        ans = K[sid][i] if isinstance(K[sid], list) else K[sid]
        for v in m:
            assert v in values and v != ans, (sid, v)
        assert "<" not in fb and ">" not in fb, sid

# Citations: PDFs exist; images exist; no gap inside a range.
for href, pages in re.findall(r'href="([^"#]+)#page=\d+" data-pages="([^"]+)"', PAGE):
    assert (HERE / href).resolve().exists(), href
    stem, nums = pages.split(":"); nums = [int(n) for n in nums.split(",")]
    assert nums == list(range(nums[0], nums[-1] + 1)), pages
    for n in nums:
        assert (HERE / "final-pages" / f"{stem}-p{n:03d}.jpg").exists(), (stem, n)
for src in re.findall(r'<img src="([^"]+)"', PAGE):
    # ntu-only/ holds crops of official papers; it is git-ignored, so a fresh clone lacks it.
    if src.startswith("ntu-only/") and not (HERE / "ntu-only").exists():
        continue
    assert (HERE / src).exists(), src

print(json.dumps(K))
