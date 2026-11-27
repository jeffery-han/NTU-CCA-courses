"""Independent key checker for final-relearn-2025-26-s1.html.

Recomputes every numeric key from first principles (exact fractions where possible,
brute-force group counting for homography), asserts the page's embedded keys match,
that progress keys are unique, distractor maps name real wrong options, and that every
cited PDF and pop-up page image exists with no gap inside a range.
Run:  python3 final-relearn-2025-26-s1-check.py
"""
import json, math, re
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = (HERE / "final-relearn-2025-26-s1.html").read_text()
r6 = lambda x: round(float(x), 6)
K = {}

# ---------- Part 1: multi-sensor Kalman (information form) ----------
def kalman(p, variances):
    """Minimise p' = c^2 p + sum L_i^2 s_i over L by brute algebra: L_i s_i = c p."""
    S = sum(F(1) / s for s in variances)
    c = 1 / (1 + p * S)
    L = [c * p / s for s in variances]
    pn = (1 - sum(L)) ** 2 * p + sum(l * l * s for l, s in zip(L, variances))
    assert pn == c * p and 1 / pn == 1 / p + S
    # first-order conditions hold
    for l, s in zip(L, variances):
        assert -2 * (1 - sum(L)) * p + 2 * l * s == 0
    return S, L, pn

K["k5_err"] = ["a", "plus"]
S, L, pn = kalman(F(1), [F(2), F(3), F(6)])
K["k5_fresh"] = [r6(S)] + [r6(x) for x in L] + [r6(pn)]
_, La, pa = kalman(F(1), [F(1), F(2)])            # exam (a), a = 1, p_k = 1
K["k5_exam_a"] = [r6(La[0]), r6(La[1]), r6(pa)]
assert La == [F(2, 5), F(1, 5)]
Sb, Lb, pb = kalman(F(1), [F(3), F(4), F(5)])     # exam (b)
K["k5_exam_b"] = [r6(x) for x in Lb] + [r6(pb)]
assert Sb == F(47, 60) and Lb == [F(20, 107), F(15, 107), F(12, 107)]
assert F(3, 2) > F(47, 60)
K["k5_c"] = "g1"

# ---------- Part 2: homography rows and group counts ----------
def rows(p, q):
    px, py = p; qx, qy = q
    return [[px, py, 1, 0, 0, 0, -px * qx, -py * qx], [0, 0, 0, px, py, 1, -px * qy, -py * qy]]

R = rows((2, 1), (3, -1))
# verify against a random homography: rows @ g == q
import random
random.seed(1)
G = [[random.uniform(-1, 1) for _ in range(3)] for _ in range(3)]; G[2][2] = 1.0
p = (0.3, -0.7); h = [sum(G[i][j] * v for j, v in enumerate((*p, 1))) for i in range(3)]
q = (h[0] / h[2], h[1] / h[2]); g = [G[0][0], G[0][1], G[0][2], G[1][0], G[1][1], G[1][2], G[2][0], G[2][1]]
for row, rhs in zip(rows(p, q), q):
    assert abs(sum(a * b for a, b in zip(row, g)) - rhs) < 1e-12
K["k4_rows"] = [R[0][6], R[0][7], R[1][6], R[1][7]]

def groups(line_sizes):
    pts = [(li, k) for li, n in enumerate(line_sizes) for k in range(n)]
    return sum(1 for c in combinations(pts, 4)
               if max(sum(1 for (li, _) in c if li == L_) for L_ in range(len(line_sizes))) <= 2)

K["k4_exam"] = [groups([3, 4]), groups([4, 2])]
assert K["k4_exam"] == [18, 6]
assert math.comb(7, 4) - 4 * (7 - 3) + 1 == 20 and math.comb(6, 4) - 4 * (6 - 3) + 1 == 4  # learner's formula
K["k4_fresh"] = [groups([3, 3, 2]), groups([4, 4])]
assert K["k4_fresh"] == [60, 36]
K["k4_valid"] = "no_fp"
K["k4_mn"] = "false"

# ---------- Part 3: wheel rows ----------
x, y = 0.10, -0.24
l = math.hypot(x, y); a = math.degrees(math.atan2(y, x)); b = 90 - a
assert abs(-l * math.cos(math.radians(b)) - (-y)) < 1e-12 and abs(l * math.sin(math.radians(b)) - x) < 1e-12
K["k3_fresh"] = [r6(l), r6(a), r6(b), r6(-y), r6(x)]
for (wx, wy), (roll, slide) in {(-0.10, 0.25): (-0.25, -0.10), (-0.10, -0.25): (0.25, -0.10)}.items():
    bb = math.radians(90 - math.degrees(math.atan2(wy, wx)))
    L_ = math.hypot(wx, wy)
    assert abs(-L_ * math.cos(bb) - roll) < 1e-12 and abs(L_ * math.sin(bb) - slide) < 1e-12
K["k3_exam"] = [-0.25, -0.1, 0.25, -0.1]
assert math.cos(math.atan2(0.25, -0.10)) < 0
K["k3_cos"] = "neg"

# ---------- Part 4: arm IK ----------
def ik(x, y, z):
    X, Y = x - 0.05, y - 0.05
    rho = math.hypot(X, Y)
    q3 = math.hypot(rho, z) - 0.3
    q2 = math.atan2(rho, z); q1 = math.atan2(Y, X)
    # forward check
    fk = ((q3 + .3) * math.cos(q1) * math.sin(q2) + .05, (q3 + .3) * math.sin(q1) * math.sin(q2) + .05, (q3 + .3) * math.cos(q2))
    assert all(abs(u - v) < 1e-12 for u, v in zip(fk, (x, y, z)))
    return [r6(math.degrees(q1)), r6(math.degrees(q2)), r6(q3)]

K["k3b_exam"] = ik(0.35, 0.45, 0.50)
K["k3b_fresh"] = ik(-0.19, 0.37, -0.30)
assert abs(K["k3b_fresh"][2] - 0.2) < 1e-9
K["k3b_tf"] = "false"

# ---------- Part 5: hybrid control, coupled alpha ----------
def coupled(A, d, kp):
    (a11, a12), (a21, a22) = A
    det = F(a11 * a22 - a12 * a21)
    inv = [[a22 / det, -a12 / det], [-a21 / det, a11 / det]]
    rhs = [inv[0][0] * d[0] + inv[0][1] * d[1], inv[1][0] * d[0] + inv[1][1] * d[1]]
    return rhs, [r / kp for r in rhs]

rhs, ess = coupled([[2, 1], [1, 1]], [3, 1], 16)
K["k2_inv"] = [r6(rhs[0]), r6(rhs[1]), r6(ess[0]), r6(ess[1])]
assert rhs == [2, -1]
rhs, ess = coupled([[3, 1], [1, 1]], [4, 1], 16)
K["k2_fresh"] = [r6(rhs[0]), r6(rhs[1]), r6(ess[0])]
assert rhs == [F(3, 2), F(-1, 2)]
K["k2_beta"] = ["minus", "rhs"]
# gains from the paper
wn = 0.5 * min(8, 16, 24)
assert (wn, wn ** 2, 2 * 1.25 * wn, 2 * 1.05 * wn, 2 * 1 * wn) == (4, 16, 10, 8.4, 8)

# ---------- page consistency ----------
page_keys = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', PAGE, re.S).group(1))
bad = [k for k in set(K) | set(page_keys) if K.get(k) != page_keys.get(k)]
assert not bad, {k: (K.get(k), page_keys.get(k)) for k in bad}

ids = re.findall(r'data-(?:k|id)="([^"]+)"', PAGE)
assert len(ids) == len(set(ids)), "duplicate progress keys"
assert set(K) <= set(ids), set(K) - set(ids)
assert 'inputmode="decimal"' not in PAGE

for sid, html in re.findall(r'<div class="step[^"]*" data-k="([^"]+)">(.*?)</div>\s*(?=<div class="step|<!--|<h2|<div class="rule|</main)', PAGE, re.S):
    sels = re.findall(r"<select( data-fb='([^']*)')?>(.*?)</select>", html, re.S)
    for i, (_, fb, opts) in enumerate(sels):
        values = re.findall(r'<option value="([^"]*)"', opts)
        ans = K[sid][i] if isinstance(K[sid], list) else K[sid]
        assert ans in values, (sid, ans)
        if fb:
            m = json.loads(fb)
            for v in m:
                assert v in values and v != ans, (sid, v)
            assert "<" not in fb and ">" not in fb, sid

cites = re.findall(r'href="([^"#]+)#page=(\d+)" data-pages="([^"]+)"', PAGE)
assert cites
for href, first, pages in cites:
    assert (HERE / href).resolve().exists(), href
    stem, nums = pages.split(":")
    nums = [int(n) for n in nums.split(",")]
    assert nums[0] == int(first) and nums == list(range(nums[0], nums[-1] + 1)), pages
    for n in nums:
        assert (HERE / "final-pages" / f"{stem}-p{n:03d}.jpg").exists(), (stem, n)

print(json.dumps(K))
