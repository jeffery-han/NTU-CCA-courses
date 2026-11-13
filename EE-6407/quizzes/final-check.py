"""Independent key checker for the EE6407 final-prep pages.

Recomputes every numeric key from the question data and asserts that the keys embedded in
final-primer.html and final-mock-a-guided.html (JSON in <script id="keys">) match.
Run:  python3 final-check.py   (prints the computed keys; exits non-zero on any mismatch)
"""
import json, math, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
r4 = lambda v: round(v, 4)
dist = lambda p, q: math.dist(p, q)


def decode(bits, lo, hi):
    return lo + (hi - lo) * int(bits, 2) / (2 ** len(bits) - 1)


def queens_conflicts(q):
    return sum(1 for i in range(len(q)) for j in range(i + 1, len(q)) if abs(q[i] - q[j]) == j - i)


def inv2(M):
    (a, b), (c, d) = M
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]], det


def mv(M, v):
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]


def scatter(X):
    m = [sum(c) / len(X) for c in zip(*X)]
    S = [[sum((x[i] - m[i]) * (x[j] - m[j]) for x in X) for j in range(2)] for i in range(2)]
    return m, S


# ---------------- primer ----------------
P = {}
P["g1"] = r4(decode("10110010", -5, 5))                               # 1.9804
P["g2"] = r4(0.25 * 0.2 + 0.75 * 0.6)                                # 0.5
c = queens_conflicts([1, 3, 2, 4]); assert c == 2
P["g3"] = r4(1 - c / (4 * 3 / 2))                                     # 0.6667
g1 = math.log(0.75) - 2.5 ** 2 / (2 * 4); g2 = math.log(0.25) - 1.5 ** 2 / (2 * 4)
P["m1"] = r4(g1 - g2)                                                 # class 1 margin
P["m2"] = r4((1 + 1) / (9 + 12))
Sinv, _ = inv2([[4, 1], [1, 2]]); w = mv(Sinv, [3, 1])
P["m3"] = r4(w[0])
w0 = -(w[0] * 5 + w[1] * 3) / 2; assert abs(w0 + 2) < 1e-9
P["m3b"] = r4(abs(w[0] * 2 + w[1] * 3 + w0) / math.hypot(*w))
P["m4"] = r4(2 / math.hypot(3, 4))                                    # 0.4
P["m5"] = r4(0.5 * (1 - 0.7 ** 2 - 0.3 ** 2))                         # 0.21 (slide: 1/2(1 - sum p^2))
P["m6"] = max(abs(a - b) for a in (1, 2) for b in (6, 9))             # complete link = 8
pts = [1, 2, 4, 7, 8]; cl = [p for p in pts if abs(p - 1) <= abs(p - 8)]
P["m7"] = r4(sum(cl) / len(cl))                                       # 2.3333
P["m8"] = r4(min(abs(a - b) for a in (0, 1) for b in (4, 6)) / max(1, 2))  # Dunn = 1.5
P["e1"] = r4((30 - 10) / (60 - 10))
pr, rc = 40 / 50, 40 / 60
P["e2"] = r4(2 * pr * rc / (pr + rc))
P["e3"] = r4(20 / (8 + 2))

# ---------------- guided mock A ----------------
G = {}
# Q1(a) binary decoding: f = x^2 + 2y^2 - 3x, x in [-4,4], y in [0,6], 8 bits each
xb, yb = "10110100", "01011010"
G["q1a_decx"] = int(xb, 2); G["q1a_decy"] = int(yb, 2)
x = decode(xb, -4, 4); y = decode(yb, 0, 6)
G["q1a_x"] = r4(x); G["q1a_y"] = r4(y)
G["q1a_f"] = r4(x * x + 2 * y * y - 3 * x)
G["q1a_res"] = r4(8 / 255)
G["q1a_bits"] = next(n for n in range(1, 40) if 8 / (2 ** n - 1) <= 0.001)
# Q1(b) portfolio crossover
P1 = [0.40, 0.10, 0.30, 0.20]; P2 = [0.10, 0.50, 0.20, 0.20]
mu = [0.08, 0.12, 0.10, 0.06]
Fit = lambda w: sum(m * v for m, v in zip(mu, w)) - 0.1 * sum(v * v for v in w)
c1 = [0.7 * a + 0.3 * b for a, b in zip(P1, P2)]
c2 = [0.3 * a + 0.7 * b for a, b in zip(P1, P2)]
assert abs(sum(c1) - 1) < 1e-12 and abs(sum(c2) - 1) < 1e-12
G["q1b_c1"] = [r4(v) for v in c1]; G["q1b_c2"] = [r4(v) for v in c2]
u = [0.1, 0.9, 0.5, 0.3]; al = 0.5
z = []
for a, b, ui in zip(P1, P2, u):
    lo, d = min(a, b), abs(a - b)
    z.append(lo - al * d + ui * (1 + 2 * al) * d)
G["q1b_z"] = [r4(v) for v in z]; G["q1b_zsum"] = r4(sum(z))
assert all(v >= 0 for v in z)
zr = [v / sum(z) for v in z]
G["q1b_zr"] = [r4(v) for v in zr]
G["q1b_F_P1"] = r4(Fit(P1)); G["q1b_F_P2"] = r4(Fit(P2))
G["q1b_F_c1"] = r4(Fit(c1)); G["q1b_F_zr"] = r4(Fit(zr))
# Q2(a) Gaussian Bayes
m1, C1 = [0, 1], [[2, 0], [0, 1]]
m2, C2 = [2, 3], [[1, 0.5], [0.5, 2]]
xq = [1, 2]; pri = [600 / 1000, 400 / 1000]
out = []
for m, C, p in ((m1, C1, pri[0]), (m2, C2, pri[1])):
    Ci, det = inv2(C); dv = [xq[0] - m[0], xq[1] - m[1]]
    q = dv[0] * mv(Ci, dv)[0] + dv[1] * mv(Ci, dv)[1]
    out.append((q, det, math.log(p) - 0.5 * math.log(det) - 0.5 * q))
G["q2a_q1"], G["q2a_det1"], G["q2a_g1"] = r4(out[0][0]), r4(out[0][1]), r4(out[0][2])
G["q2a_q2"], G["q2a_det2"], G["q2a_g2"] = r4(out[1][0]), r4(out[1][1]), r4(out[1][2])
G["q2a_class"] = 1 if out[0][2] > out[1][2] else 2
# Q2(b) Bernoulli NB (Fever, Cough, Fatigue)
flu = ["YYY", "YYN", "YNY", "YYY", "NYY", "YNY"]
cold = ["NYN", "NYY", "YYN", "NNN"]
test = "NYY"
def nb(rows, prior):
    s = prior
    for k, v in enumerate(test):
        py = sum(r[k] == "Y" for r in rows) / len(rows)
        s *= py if v == "Y" else 1 - py
    return s
sf, sc = nb(flu, 6 / 10), nb(cold, 4 / 10)
G["q2b_flu"], G["q2b_cold"] = r4(sf), r4(sc)
G["q2b_class"] = "Cold" if sc > sf else "Flu"
G["q2b_post"] = r4(max(sf, sc) / (sf + sc))
# Q3(a) Fisher LDA from raw samples
X1 = [(1, 2), (2, 4), (3, 3)]; X2 = [(4, 0), (6, 1), (5, 2)]
M1, S1 = scatter(X1); M2, S2 = scatter(X2)
SW = [[S1[i][j] + S2[i][j] for j in range(2)] for i in range(2)]
G["q3a_m1"], G["q3a_m2"] = [r4(v) for v in M1], [r4(v) for v in M2]
G["q3a_S1"], G["q3a_SW"] = [[r4(v) for v in row] for row in S1], [[r4(v) for v in row] for row in SW]
SWi, det = inv2(SW); G["q3a_det"] = r4(det)
wl = mv(SWi, [M1[0] - M2[0], M1[1] - M2[1]])
w0l = -(wl[0] * (M1[0] + M2[0]) + wl[1] * (M1[1] + M2[1])) / 2
G["q3a_w"] = [r4(v) for v in wl]; G["q3a_w0"] = r4(w0l)
assert wl[0] * M1[0] + wl[1] * M1[1] + w0l > 0          # g(m1) > 0 -> class 1 side
gx = wl[0] * 3 + wl[1] * 2 + w0l
G["q3a_g"] = r4(gx); G["q3a_dist"] = r4(abs(gx) / math.hypot(*wl))
# Q3(b) soft-margin SVM, C = 1; bound SV (2,1.5) has alpha = C
C = 1.0
SV = [((3, 1), +1, 0.25), ((1, 1), -1, 0.75), ((2, 0), -1, 0.5), ((2, 1.5), +1, 1.0)]
assert abs(sum(a * d for _, d, a in SV)) < 1e-12
ws = [sum(a * d * x[k] for x, d, a in SV) for k in range(2)]
G["q3b_w"] = [r4(v) for v in ws]
bs = [d - (ws[0] * x[0] + ws[1] * x[1]) for x, d, a in SV if 0 < a < C]
assert max(bs) - min(bs) < 1e-12                          # KKT-consistent: all free SVs agree
G["q3b_b"] = r4(sum(bs) / len(bs))
ball = [d - (ws[0] * x[0] + ws[1] * x[1]) for x, d, a in SV]
G["q3b_b_wrong"] = r4(sum(ball) / len(ball))
xi = 1 - (+1) * (ws[0] * 2 + ws[1] * 1.5 + G["q3b_b"])
G["q3b_xi"] = r4(xi)
G["q3b_margin"] = r4(2 / math.hypot(*ws))
gt = ws[0] * 2.5 + ws[1] * 2 + G["q3b_b"]
G["q3b_g"] = r4(gt); G["q3b_dist"] = r4(abs(gt) / math.hypot(*ws))
# Q4(a) complete-linkage HAC on a distance matrix
names = "ABCDE"
D = [[0, 2, 6, 10, 9], [2, 0, 5, 9, 8], [6, 5, 0, 4, 5], [10, 9, 4, 0, 3], [9, 8, 5, 3, 0]]
def hac(link):
    cls = [[i] for i in range(5)]; hs = []
    while len(cls) > 1:
        best = None
        for i in range(len(cls)):
            for j in range(i + 1, len(cls)):
                d = link(D[a][b] for a in cls[i] for b in cls[j])
                if best is None or d < best[0]: best = (d, i, j)
        d, i, j = best; hs.append(("".join(names[k] for k in sorted(cls[i] + cls[j])), d))
        cls = [c for k, c in enumerate(cls) if k not in (i, j)] + [cls[i] + cls[j]]
    return hs
G["q4a_complete"] = hac(max); G["q4a_single"] = hac(min)
# Q4(b) k-means, 2 iterations
pts = [(1, 1), (2, 1), (1, 3), (5, 4), (6, 5), (4, 6)]
cs = [(1, 1), (2, 1)]; hist = []
for _ in range(2):
    lab = [min(range(2), key=lambda k: dist(p, cs[k])) for p in pts]
    cs = [tuple(sum(p[t] for p, l in zip(pts, lab) if l == k) / lab.count(k) for t in range(2)) for k in range(2)]
    hist.append(("".join(str(l + 1) for l in lab), [[r4(v) for v in c] for c in cs]))
G["q4b_iter"] = hist
lab = [min(range(2), key=lambda k: dist(p, cs[k])) for p in pts]
G["q4b_converged"] = "".join(str(l + 1) for l in lab) == hist[-1][0]
G["q4b_sse"] = r4(sum(dist(p, cs[l]) ** 2 for p, l in zip(pts, lab)))
# Q4(c) silhouette of (2,1), slide convention: a = mean intra, b = MIN distance to other-cluster samples
own = [p for p, l in zip(pts, lab) if l == lab[1] and p != (2, 1)]
oth = [p for p, l in zip(pts, lab) if l != lab[1]]
a = sum(dist((2, 1), p) for p in own) / len(own); b = min(dist((2, 1), p) for p in oth)
G["q4c_a"], G["q4c_b"], G["q4c_s"] = r4(a), r4(b), r4((b - a) / max(a, b))

if __name__ == "__main__":
    print(json.dumps({"primer": P, "guided": G}, indent=1))
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
    print("OK" if not bad else f"{bad} problem(s)"); sys.exit(1 if bad else 0)
