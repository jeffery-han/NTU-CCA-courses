"""Key checker for final-mock-b (EE6407 final, Mock B).

Recomputes every numeric key from the question data and asserts that the JSON key block in
final-mock-b.md matches, and that final-mock-b.html contains no answer values.
Run:  python3 final-mock-b-check.py   (prints the keys; exits non-zero on any mismatch)
"""
import json, math, re, sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
r4 = lambda v: round(v, 4)
K = {}

# ---------- Q1(a) 8-queens, permutation coding, PMX ----------
def conflicts(q):
    return sum(1 for i, j in combinations(range(len(q)), 2) if abs(q[i] - q[j]) == j - i)

def pmx(p1, p2, a, b):  # 0-based inclusive segment, course convention (segment from p1)
    c = [None] * len(p1); c[a:b + 1] = p1[a:b + 1]
    for i in range(a, b + 1):
        v = p2[i]
        if v in c:
            continue
        j = i
        while True:
            j = p2.index(p1[j])
            if c[j] is None:
                c[j] = v; break
    return [p2[i] if x is None else x for i, x in enumerate(c)]

P1, P2 = [6, 2, 1, 3, 5, 8, 4, 7], [5, 1, 8, 2, 7, 6, 3, 4]
K["q1a_C_P1"] = conflicts(P1); K["q1a_f_P1"] = r4(1 - conflicts(P1) / 28)
K["q1a_C_P2"] = conflicts(P2); K["q1a_f_P2"] = r4(1 - conflicts(P2) / 28)
child = pmx(P1, P2, 2, 5); assert sorted(child) == list(range(1, 9))
K["q1a_child"] = "".join(map(str, child))
K["q1a_C_child"] = conflicts(child); K["q1a_f_child"] = r4(1 - conflicts(child) / 28)
K["q1a_space_perm"] = math.factorial(8); K["q1a_space_free"] = 8 ** 8

# ---------- Q1(b) minimisation -> roulette ----------
g = [4, 9, 1, 6, 10]
f = [1 / (1 + x) for x in g]; s = sum(f)
p = [x / s for x in f]
cum = [sum(p[:i + 1]) for i in range(5)]
for i in range(5):
    K[f"q1b_p{i+1}"] = r4(p[i])
K["q1b_expected3"] = r4(5 * p[2])
pick = lambda u: next(i + 1 for i, c in enumerate(cum) if u <= c)
K["q1b_picks"] = "".join(str(pick(u)) for u in (0.25, 0.80, 0.95))

# ---------- Q2(a) multinomial NB with Laplace ----------
spam = ["free win free", "win money", "free money now"]
ham = ["meeting now", "project meeting notes", "notes free", "project notes"]
vocab = sorted({w for d in spam + ham for w in d.split()}); d = len(vocab)
def cond(docs):
    words = " ".join(docs).split(); n = len(words)
    return {w: (words.count(w) + 1) / (n + d) for w in vocab}, n
cs, ns = cond(spam); ch, nh = cond(ham)
test = "free notes now free".split()
ps, ph = len(spam) / 7, len(ham) / 7
ss = ps * math.prod(cs[w] for w in test); sh = ph * math.prod(ch[w] for w in test)
K["q2a_d"] = d; K["q2a_nspam"] = ns; K["q2a_nham"] = nh
for w in ("free", "notes", "now"):
    K[f"q2a_{w}_S"] = r4(cs[w]); K[f"q2a_{w}_H"] = r4(ch[w])
K["q2a_scoreS_e4"] = r4(ss * 1e4); K["q2a_scoreH_e4"] = r4(sh * 1e4)
K["q2a_class"] = "ham" if sh > ss else "spam"
K["q2a_class_noprior"] = "ham" if sh / ph > ss / ps else "spam"

# ---------- Q2(b) Gaussian naive Bayes ----------
x = (3, 4)
cls = {1: (0.6, (2, 5), (1, 4)), 2: (0.4, (4, 3), (2, 1))}
gs = {}
for k, (pr, mu, var) in cls.items():
    gs[k] = math.log(pr) - 0.5 * sum(math.log(v) for v in var) - 0.5 * sum((x[i] - mu[i]) ** 2 / var[i] for i in range(2))
    lik = math.prod(math.exp(-(x[i] - mu[i]) ** 2 / (2 * var[i])) / math.sqrt(2 * math.pi * var[i]) for i in range(2))
    K[f"q2b_lik{k}"] = r4(lik)
    K[f"q2b_g{k}"] = r4(gs[k])
K["q2b_class"] = 1 if gs[1] > gs[2] else 2
K["q2b_post1"] = r4(1 / (1 + math.exp(gs[2] - gs[1])))

# ---------- Q2(c) Gini root node, slide convention 1/2(1 - sum p^2) ----------
gini = lambda a, b: 0.5 * (1 - (a / (a + b)) ** 2 - (b / (a + b)) ** 2)
root = gini(10, 6); K["q2c_root"] = r4(root)
splits = {"A": ((7, 1), (3, 5)), "B": ((4, 0), (6, 6)), "C": ((8, 2), (2, 4))}
drops = {}
for nm, (l, rr) in splits.items():
    wtd = (sum(l) * gini(*l) + sum(rr) * gini(*rr)) / 16
    K[f"q2c_{nm}_weighted"] = r4(wtd); drops[nm] = root - wtd
    K[f"q2c_{nm}_drop"] = r4(root - wtd)
K["q2c_best"] = max(drops, key=drops.get)

# ---------- Q3(a) Fisher LDA ----------
m1, m2 = (6, 4), (2, 2)
S1, S2 = [[30, 10], [10, 20]], [[26, -2], [-2, 16]]
SW = [[S1[i][j] + S2[i][j] for j in range(2)] for i in range(2)]
det = SW[0][0] * SW[1][1] - SW[0][1] * SW[1][0]
inv = [[SW[1][1] / det, -SW[0][1] / det], [-SW[1][0] / det, SW[0][0] / det]]
dm = (m1[0] - m2[0], m1[1] - m2[1])
w = (inv[0][0] * dm[0] + inv[0][1] * dm[1], inv[1][0] * dm[0] + inv[1][1] * dm[1])
w0 = -(w[0] * (m1[0] + m2[0]) + w[1] * (m1[1] + m2[1])) / 2
K["q3a_det"] = det; K["q3a_w1"] = r4(w[0]); K["q3a_w2"] = r4(w[1]); K["q3a_w0"] = r4(w0)
xt = (3.5, 3)
gx = w[0] * xt[0] + w[1] * xt[1] + w0
K["q3a_g"] = r4(gx); K["q3a_class"] = 1 if gx > 0 else 2
K["q3a_dist"] = r4(abs(gx) / math.hypot(*w))
K["q3a_dist_m1"] = r4(abs(w[0] * m1[0] + w[1] * m1[1] + w0) / math.hypot(*w))

# ---------- Q3(b) soft-margin SVM, C = 1 ----------
Csv = 1
sv = [((2, 3), 1, 0.25), ((4, 1), 1, 0.5), ((1, 2), -1, 0.875), ((3, 0), -1, 0.875),
      ((2, 1.5), 1, 1.0), ((5, 4), 1, 0.0)]
assert abs(sum(a * dd for _, dd, a in sv)) < 1e-12
wv = tuple(sum(a * dd * xx[i] for xx, dd, a in sv) for i in range(2))
free = [(xx, dd) for xx, dd, a in sv if 0 < a < Csv]
bs = [dd - (wv[0] * xx[0] + wv[1] * xx[1]) for xx, dd in free]
b = sum(bs) / len(bs); assert max(bs) - min(bs) < 1e-12
allpos = [dd - (wv[0] * xx[0] + wv[1] * xx[1]) for xx, dd, a in sv if a > 0]
K["q3b_w1"] = r4(wv[0]); K["q3b_w2"] = r4(wv[1]); K["q3b_b"] = r4(b)
K["q3b_b_wrong_all"] = r4(sum(allpos) / len(allpos))
K["q3b_margin"] = r4(2 / math.hypot(*wv))
x5 = sv[4][0]; K["q3b_xi5"] = r4(1 - 1 * (wv[0] * x5[0] + wv[1] * x5[1] + b))
xq = (3.2, 1.2); gq = wv[0] * xq[0] + wv[1] * xq[1] + b
K["q3b_g"] = r4(gq); K["q3b_class"] = 1 if gq > 0 else -1; K["q3b_dist"] = r4(abs(gq) / math.hypot(*wv))

# ---------- Q4 clustering ----------
P = {"A": (0, 0), "B": (1, 2), "C": (4, 0), "D": (8, 7), "E": (9, 4), "F": (12, 8)}
dist = lambda a, c: math.dist(P[a], P[c])
pair_d = [r4(dist(a, c)) for a, c in combinations(P, 2)]
assert len(set(pair_d)) == len(pair_d), "tie in distance matrix"
clusters = [frozenset(k) for k in P]; merges = []
while len(clusters) > 1:
    (i, j), h = min((((i, j), min(dist(a, c) for a in clusters[i] for c in clusters[j]))
                     for i, j in combinations(range(len(clusters)), 2)), key=lambda t: t[1])
    new = clusters[i] | clusters[j]
    merges.append(("".join(sorted(clusters[i] | clusters[j])), r4(h)))
    clusters = [c for k, c in enumerate(clusters) if k not in (i, j)] + [new]
for n, (members, h) in enumerate(merges, 1):
    K[f"q4a_merge{n}"] = f"{members}@{h}"
c1, c2 = ["A", "B", "C"], ["D", "E", "F"]
K["q4a_cut2"] = "ABC|DEF"

def centroid(cl):
    return tuple(sum(P[k][i] for k in cl) / len(cl) for i in range(2))
def delta(cl):
    m = centroid(cl); return math.sqrt(sum(math.dist(P[k], m) ** 2 for k in cl) / len(cl))
mA, mB = centroid(c1), centroid(c2)
K["q4b_m1"] = f"{r4(mA[0])},{r4(mA[1])}"; K["q4b_m2"] = f"{r4(mB[0])},{r4(mB[1])}"
K["q4b_delta1"] = r4(delta(c1)); K["q4b_delta2"] = r4(delta(c2))
K["q4b_d12"] = r4(math.dist(mA, mB))
K["q4b_DB"] = r4((delta(c1) + delta(c2)) / math.dist(mA, mB))

inter = min(dist(a, c) for a in c1 for c in c2)
diam = max(max(dist(a, c) for a, c in combinations(cl, 2)) for cl in (c1, c2))
K["q4c_inter"] = r4(inter); K["q4c_diam"] = r4(diam); K["q4c_dunn"] = r4(inter / diam)

lab1 = {k: (0 if k in c1 else 1) for k in P}
lab2 = {"A": 0, "B": 0, "C": 1, "D": 1, "E": 1, "F": 2}
Ns = sum(1 for a, c in combinations(P, 2) if lab1[a] == lab1[c] and lab2[a] == lab2[c])
Nd = sum(1 for a, c in combinations(P, 2) if lab1[a] != lab1[c] and lab2[a] != lab2[c])
K["q4d_Ns"] = Ns; K["q4d_Nd"] = Nd; K["q4d_RI"] = r4((Ns + Nd) / 15)

# ---------- compare with the key file ----------
for k, v in K.items():
    print(f"{k:20s} {v}")
md = (HERE / "final-mock-b.md").read_text()
block = re.search(r"```json keys\n(.*?)\n```", md, re.S)
assert block, "no ```json keys block in final-mock-b.md"
stored = json.loads(block.group(1))
bad = [k for k in K if stored.get(k) != K[k]] + [k for k in stored if k not in K]
html = (HERE / "final-mock-b.html").read_text()
assert "json keys" not in html and "Model answer" not in html, "answers leaked into the paper"
for img in ("ml-revision-2026-s1-p014.jpg", "ml-revision-2026-s1-p016.jpg", "ml-slides-11-clustering-evaluation-p017.jpg"):
    assert (HERE / "final-pages" / img).exists(), img
if bad:
    print("MISMATCH:", bad); sys.exit(1)
print(f"ok: {len(K)} keys match final-mock-b.md")
