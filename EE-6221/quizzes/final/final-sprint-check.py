"""Independent key checker for final-sprint.html.

Recomputes every numeric and symbolic key, verifies distractor feedback maps,
unique progress keys, no inputmode="decimal", and contiguous citation images.
Run:  python3 final-sprint-check.py
"""
import itertools, json, math, re
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = (HERE / "final-sprint.html").read_text()

K = {}

# Part 1: D-H offset matrices
# T3_2: theta = q3 - 90 => C = +S3, S = -C3; alpha = +90 => S_al = 1, C_al = 0
K["dh_shift"] = ["S3", "-C3", "-C3", "-S3"]
# T2_1: theta = q2 + 90 => C = -S2, S = +C2; a2 = 25, alpha = 0
K["dh_plus90"] = ["-S2", "C2", "-25S2", "25C2"]

# Part 2: Hz resonances, beta, alpha^-1 d
wmin = 2 * math.pi * min(2.5, 5, 8)
wn = 0.5 * wmin
kp = wn ** 2
kv = 2 * 1.2 * wn
K["q2_hz"] = [round(wmin, 6), round(wn, 6), round(kp, 6), round(kv, 6)]
K["q2_beta_tf"] = "false"
# alpha_m = [[3, 1], [1, 1]], det = 2, alpha_m^-1 = 0.5 * [[1, -1], [-1, 3]], d = [6, 2]
det = 3 * 1 - 1 * 1
rhs1 = (1 * 6 - 1 * 2) / det
rhs2 = (-1 * 6 + 3 * 2) / det
e1ss = rhs1 / 16
K["q2_alpha_inv"] = [round(rhs1, 6), round(rhs2, 6), round(e1ss, 6)]

# Part 3: Wheel geometry & IK
xA, yA = -0.12, 0.16
lA = math.hypot(xA, yA)
ca, sa = xA / lA, yA / lA
K["q3_wheel_geo"] = [round(lA, 6), round(ca, 6), round(sa, 6), round(-yA, 6), round(xA, 6)]

x, y, z = 0.7, 0.9, 1.0
X, Y, Z = x - 0.1, y - 0.1, z
q1 = math.atan2(Y, X)
q2 = math.atan2(math.hypot(X, Y), Z)
q3 = math.sqrt(X ** 2 + Y ** 2 + Z ** 2) - 0.2
assert abs((q3 + 0.2) * math.cos(q1) * math.sin(q2) + 0.1 - x) < 1e-12
assert abs((q3 + 0.2) * math.sin(q1) * math.sin(q2) + 0.1 - y) < 1e-12
assert abs((q3 + 0.2) * math.cos(q2) - z) < 1e-12
K["q3_ik_quick"] = [round(q1, 6), round(q2, 6), round(q3, 6)]

# Part 4: Homography line-split counts & rows
# L1: 1..4, L2: 5..7, L3: 8..9
P = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (2, 0), 9: (2, 1)}
col = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0
cnt = lambda S: sum(1 for g in itertools.combinations(sorted(S), 4)
                    if not any(col(P[t[0]], P[t[1]], P[t[2]]) for t in itertools.combinations(g, 3)))
assert cnt({1, 2, 3, 4, 5, 6, 7}) == 18
assert cnt({5, 6, 7, 8, 9}) == 3
assert cnt({5, 6, 7}) == 0
K["q4_counts"] = [18, 3, "no", "yes"]
K["q4_rows"] = [-2 * 4, -3 * 4, -2 * 5, -3 * 5]

# Part 5: Kalman
K["q5_tf"] = "false"
info1 = Fr(1, 2) + Fr(1, 6)
inv_pk1 = Fr(1, 3) + info1
pk1 = 1 / inv_pk1
L1, L2 = pk1 / 2, pk1 / 6
K["q5_calc"] = [round(float(info1), 6), round(float(inv_pk1), 6), round(float(pk1), 6),
                round(float(L1), 6), round(float(L2), 6)]
info2 = Fr(1, 4) * 3
assert info2 > info1
K["q5_compare"] = "g2"

# Verify embedded keys match recomputed keys
page_keys = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', PAGE, re.S).group(1))
bad = [k for k in set(K) | set(page_keys) if K.get(k) != page_keys.get(k)]
assert not bad, {k: (K.get(k), page_keys.get(k)) for k in bad}

# Verify unique progress keys and no inputmode="decimal"
ids = re.findall(r'data-(?:k|id)="([^"]+)"', PAGE)
assert len(ids) == len(set(ids)), "duplicate progress keys"
assert set(K) <= set(ids), set(K) - set(ids)
assert 'inputmode="decimal"' not in PAGE, "do not set inputmode=decimal"

# Verify distractor feedback maps
for step in re.findall(r'<div class="step[^"]*" data-k="([^"]+)">(.*?)</div>\s*(?=<div class="step|<!--|<h2|</main)', PAGE, re.S):
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

# Verify citations: PDFs exist, images exist, contiguous ranges
for href, pages in re.findall(r'href="([^"#]+)#page=\d+" data-pages="([^"]+)"', PAGE):
    assert (HERE / href).resolve().exists(), href
    stem, nums = pages.split(":")
    nums = [int(n) for n in nums.split(",")]
    assert nums == list(range(nums[0], nums[-1] + 1)), pages
    for n in nums:
        assert (HERE / "final-pages" / f"{stem}-p{n:03d}.jpg").exists(), (stem, n)

print(json.dumps(K))
