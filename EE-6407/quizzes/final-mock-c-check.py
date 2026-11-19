"""Key checker for final-mock-c (EE6407 final, Mock C, weighted to the Mock B mistakes).

Recomputes every numeric key from the question data, asserts that the JSON key block in final-mock-c.md
matches, and that final-mock-c.html carries no answers.
Run:  python3 final-mock-c-check.py
"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
import math
from itertools import combinations
r4 = lambda v: round(v, 4)

def svm(sv, C):
    assert abs(sum(a * d for _, d, a in sv)) < 1e-12
    w = tuple(sum(a * d * x[i] for x, d, a in sv) for i in range(2))
    gx = lambda x: w[0] * x[0] + w[1] * x[1]
    free = [d - gx(x) for x, d, a in sv if 0 < a < C]
    assert max(free) - min(free) < 1e-12
    b = sum(free) / len(free)
    allp = [d - gx(x) for x, d, a in sv if a > 0]
    bnd = [(x, d) for x, d, a in sv if a == C][0]
    return dict(w1=r4(w[0]), w2=r4(w[1]), b=r4(b), b_wrong=r4(sum(allp) / len(allp)),
                margin=r4(2 / math.hypot(*w)), xi=r4(1 - bnd[1] * (gx(bnd[0]) + b)),
                nfree=len(free)), (lambda x: (gx(x) + b, abs(gx(x) + b) / math.hypot(*w)))

def mnb(classes, test):
    vocab = sorted({t for docs in classes.values() for d in docs for t in d.split()})
    d = len(vocab); N = sum(len(v) for v in classes.values()); out = {"d": d}; sc = {}
    for c, docs in classes.items():
        ws = " ".join(docs).split(); n = len(ws); out[f"n_{c}"] = n
        p = {t: (ws.count(t) + 1) / (n + d) for t in vocab}
        for t in sorted(set(test.split())): out[f"p_{t}_{c}"] = r4(p[t])
        sc[c] = len(docs) / N * math.prod(p[t] for t in test.split())
        out[f"score_{c}"] = sc[c]
    out["class"] = max(sc, key=sc.get)
    return out

def gnb(cls, x):
    out = {}; g = {}
    for k, (pr, mu, var) in cls.items():
        out[f"lik{k}"] = r4(math.prod(math.exp(-(x[i] - mu[i]) ** 2 / (2 * var[i])) / math.sqrt(2 * math.pi * var[i]) for i in range(2)))
        g[k] = math.log(pr) - .5 * sum(math.log(v) for v in var) - .5 * sum((x[i] - mu[i]) ** 2 / var[i] for i in range(2))
        out[f"g{k}"] = r4(g[k])
    out["class"] = max(g, key=g.get); out["post1"] = r4(1 / (1 + math.exp(g[2] - g[1])))
    return out

def gini(a, b): return .5 * (1 - (a / (a + b)) ** 2 - (b / (a + b)) ** 2)
def gini_split(node, splits):
    n = sum(node); root = gini(*node); out = {"root": r4(root)}; drops = {}
    for nm, (l, rr) in splits.items():
        wt = (sum(l) * gini(*l) + sum(rr) * gini(*rr)) / n
        out[f"{nm}_w"] = r4(wt); out[f"{nm}_drop"] = r4(root - wt); drops[nm] = root - wt
    out["best"] = max(drops, key=drops.get); return out

def single_link(P):
    dist = lambda a, c: math.dist(P[a], P[c])
    ds = [r4(dist(a, c)) for a, c in combinations(P, 2)]; assert len(set(ds)) == len(ds), "tie"
    cl = [frozenset(k) for k in P]; merges = []
    while len(cl) > 1:
        (i, j), h = min((((i, j), min(dist(a, c) for a in cl[i] for c in cl[j])) for i, j in combinations(range(len(cl)), 2)), key=lambda t: t[1])
        merges.append("".join(sorted(cl[i] | cl[j])) + "@" + str(r4(h)))
        n = cl[i] | cl[j]; cl = [c for k, c in enumerate(cl) if k not in (i, j)] + [n]
    return merges

def indices(P, c1, c2, other):
    cen = lambda c: tuple(sum(P[k][i] for k in c) / len(c) for i in range(2))
    dl = lambda c: math.sqrt(sum(math.dist(P[k], cen(c)) ** 2 for k in c) / len(c))
    m1, m2 = cen(c1), cen(c2); d12 = math.dist(m1, m2)
    o = {"m1": f"{r4(m1[0])},{r4(m1[1])}", "m2": f"{r4(m2[0])},{r4(m2[1])}", "delta1": r4(dl(c1)), "delta2": r4(dl(c2)),
         "d12": r4(d12), "DB": r4((dl(c1) + dl(c2)) / d12)}
    inter = min(math.dist(P[a], P[b]) for a in c1 for b in c2)
    diam = max(math.dist(P[a], P[b]) for c in (c1, c2) for a, b in combinations(c, 2))
    o.update(inter=r4(inter), diam=r4(diam), dunn=r4(inter / diam))
    l1 = {k: (0 if k in c1 else 1) for k in P}; l2 = {k: i for i, c in enumerate(other) for k in c}
    pairs = list(combinations(P, 2))
    Ns = sum(1 for a, b in pairs if l1[a] == l1[b] and l2[a] == l2[b]); Nd = sum(1 for a, b in pairs if l1[a] != l1[b] and l2[a] != l2[b])
    o.update(Ns=Ns, Nd=Nd, RI=r4((Ns + Nd) / len(pairs)))
    gm = tuple(sum(P[k][i] for k in P) / len(P) for i in range(2))
    Cs = [sum(math.dist(P[k], cen(c)) ** 2 for k in c) for c in (c1, c2)]
    Ss = [math.dist(cen(c), gm) ** 2 for c in (c1, c2)]
    o.update(gm=f"{r4(gm[0])},{r4(gm[1])}", C1=r4(Cs[0]), C2=r4(Cs[1]), S1=r4(Ss[0]), S2=r4(Ss[1]),
             CH=r4((len(c1) * Ss[0] + len(c2) * Ss[1]) / sum(Cs)))
    return o

def pmx(p1, p2, a, b):
    c = [None] * len(p1); c[a:b + 1] = p1[a:b + 1]
    for i in range(a, b + 1):
        v = p2[i]
        if v in c: continue
        j = i
        while True:
            j = p2.index(p1[j])
            if c[j] is None: c[j] = v; break
    c = [p2[i] if x is None else x for i, x in enumerate(c)]; assert sorted(c) == sorted(p1); return "".join(map(str, c))

def fisher(m1, m2, S1, S2, x):
    SW = [[S1[i][j] + S2[i][j] for j in range(2)] for i in range(2)]
    det = SW[0][0] * SW[1][1] - SW[0][1] * SW[1][0]
    inv = [[SW[1][1] / det, -SW[0][1] / det], [-SW[1][0] / det, SW[0][0] / det]]
    dm = (m1[0] - m2[0], m1[1] - m2[1])
    w = (inv[0][0] * dm[0] + inv[0][1] * dm[1], inv[1][0] * dm[0] + inv[1][1] * dm[1])
    w0 = -(w[0] * (m1[0] + m2[0]) + w[1] * (m1[1] + m2[1])) / 2
    g = lambda p: w[0] * p[0] + w[1] * p[1] + w0
    return dict(SW=SW, det=det, w1=r4(w[0]), w2=r4(w[1]), w0=r4(w0), g=r4(g(x)), cls=1 if g(x) > 0 else 2,
                dist=r4(abs(g(x)) / math.hypot(*w)), dist_m1=r4(abs(g(m1)) / math.hypot(*w)))

def flat(prefix, d): return {f"{prefix}_{k}": v for k, v in d.items()}

K = {}
# ---- Q1(a) TSP, PMX ----
D = [[0, 4, 7, 6, 9, 5], [4, 0, 3, 8, 6, 7], [7, 3, 0, 5, 4, 8], [6, 8, 5, 0, 3, 6], [9, 6, 4, 3, 0, 5], [5, 7, 8, 6, 5, 0]]
assert all(D[i][j] == D[j][i] for i in range(6) for j in range(6))
L = lambda t: sum(D[t[i] - 1][t[(i + 1) % 6] - 1] for i in range(6))
P1, P2 = [1, 3, 5, 2, 6, 4], [2, 4, 1, 6, 3, 5]
child = pmx(P1, P2, 2, 4); cl = [int(c) for c in child]
K.update(q1a_L1=L(P1), q1a_L2=L(P2), q1a_child=child, q1a_Lc=L(cl),
         q1a_f1=r4(100 / L(P1)), q1a_f2=r4(100 / L(P2)), q1a_fc=r4(100 / L(cl)))
# ---- Q1(b) cycle crossover ----
A, B = [1, 2, 3, 4, 5, 6, 7, 8], [8, 4, 2, 3, 7, 5, 6, 1]
seen, cyc = set(), []
for s0 in range(8):
    if s0 in seen: continue
    c, i = [], s0
    while i not in seen: seen.add(i); c.append(i); i = A.index(B[i])
    cyc.append(c)
K["q1b_cycles"] = "|".join("".join(str(i + 1) for i in sorted(c)) for c in cyc)
ch1, ch2 = [None] * 8, [None] * 8
for k, c in enumerate(cyc):
    for i in c:
        ch1[i] = (A if k % 2 == 0 else B)[i]; ch2[i] = (B if k % 2 == 0 else A)[i]
assert sorted(ch1) == A and sorted(ch2) == A
K["q1b_child1"] = "".join(map(str, ch1)); K["q1b_child2"] = "".join(map(str, ch2))
# ---- Q2 ----
K.update(flat("q2a", mnb({"Urgent": ["server down now", "fix server now"], "Normal": ["lunch plan", "plan meeting now", "meeting notes"]}, "server meeting now now")))
K["q2a_score_Urgent"] = r4(K["q2a_score_Urgent"] * 1e4); K["q2a_score_Normal"] = r4(K["q2a_score_Normal"] * 1e4)
K.update(flat("q2b", gnb({1: (.3, (4, 5), (1, 4)), 2: (.7, (2, 1), (2, 1))}, (3, 3))))
K.update(flat("q2c", gini_split((8, 12), {"F1": ((6, 2), (2, 10)), "F2": ((8, 6), (0, 6)), "F3": ((5, 5), (3, 7))})))
# ---- Q3 ----
s, f = svm([((1, 0), 1, 1 / 8), ((2, 2), 1, 11 / 8), ((0, 0), -1, 13 / 8), ((1, 2), -1, 15 / 8), ((0.5, 0), 1, 2.0), ((3, 1), 1, 0.0)], 2)
K.update(flat("q3a", s)); g, dd = f((1.2, 0.9)); K["q3a_g"] = r4(g); K["q3a_dist"] = r4(dd)
fi = fisher((5, 3), (1, 1), [[20, 4], [4, 12]], [[16, 2], [2, 20]], (3, 2.2)); fi.pop("SW")
K.update(flat("q3b", fi))
# ---- Q4 ----
P = {"A": (2, 0), "B": (3, 5), "C": (3, 0), "D": (10, 10), "E": (14, 4)}
for n, m in enumerate(single_link(P), 1): K[f"q4a_merge{n}"] = m
K.update(flat("q4", indices(P, ["A", "B", "C"], ["D", "E"], [["A"], ["B", "C"], ["D", "E"]])))

for k, v in K.items(): print(f"{k:22s} {v}")
md = (HERE / "final-mock-c.md").read_text()
blk = re.search(r"```json keys\n(.*?)\n```", md, re.S); assert blk, "no ```json keys block"
stored = json.loads(blk.group(1))
bad = [k for k in K if stored.get(k) != K[k]] + [k for k in stored if k not in K]
html = (HERE / "final-mock-c.html").read_text()
assert "json keys" not in html and "Model answer" not in html, "answers leaked into the paper"
if bad: print("MISMATCH:", bad); sys.exit(1)
print(f"ok: {len(K)} keys match final-mock-c.md")
