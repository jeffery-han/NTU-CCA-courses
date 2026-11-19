"""Key checker for final-relearn-c.html (EE6407 final, relearn page after Mock C).

Recomputes every numeric key from the question data and asserts that the JSON in
<script id="keys"> of final-relearn.html matches; also checks that every data-k has a key,
that storage ids are unique, and that every cited page image exists.
Run:  python3 final-relearn-c-check.py
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
import math
def L(D, t): return sum(D[t[i] - 1][t[(i + 1) % len(t)] - 1] for i in range(len(t)))
inv = lambda t: [t.index(i) + 1 for i in range(1, len(t) + 1)]
Y = [[0, 4, 6, 3, 7], [4, 0, 5, 8, 2], [6, 5, 0, 4, 9], [3, 8, 4, 0, 5], [7, 2, 9, 5, 0]]
assert (L(Y, [3, 1, 5, 2, 4]), L(Y, inv([3, 1, 5, 2, 4]))) == (27, 32)  # worked example and its trap
Z = [[0, 5, 3, 8, 4], [5, 0, 6, 2, 7], [3, 6, 0, 4, 9], [8, 2, 4, 0, 3], [4, 7, 9, 3, 0]]
a, b = L(Z, [4, 2, 5, 1, 3]), L(Z, [1, 2, 3, 4, 5])
K["tsp_L"] = [a, b]; K["tsp_f"] = [r4(100 / a), r4(100 / b), "A" if a < b else "B"]
w = indices({"A": (0, 0), "B": (4, 0), "C": (0, 2), "D": (8, 1), "E": (10, 1)}, ["A", "B", "C"], ["D", "E"], [["A", "B", "C"], ["D", "E"]])
assert (w["delta1"], w["DB"], w["CH"]) == (2.1082, 0.405, 4.6087)
P = {"P": (1, 1), "Q": (4, 1), "R": (1, 3), "S": (9, 2), "T": (11, 4), "U": (9, 4)}
o = indices(P, ["P", "Q", "R"], ["S", "T", "U"], [["P", "Q", "R"], ["S", "T", "U"]])
K["db_m"] = [float(v) for v in o["m1"].split(",") + o["m2"].split(",")]
K["db_delta"] = [o["delta1"], o["delta2"]]; K["db_val"] = [o["d12"], o["DB"]]
K["ch_g"] = [float(v) for v in o["gm"].split(",")]; K["ch_parts"] = [o["C1"], o["C2"], o["S1"], o["S2"]]; K["ch_val"] = o["CH"]
wv, b0 = (2, 1), -4; xi = []; loc = []
for x, d in [((1, 1.5), 1), ((1.5, 0.5), -1), ((2, 0), 1)]:
    g = wv[0] * x[0] + wv[1] * x[1] + b0; z = max(0, 1 - d * g); xi.append(r4(z))
    loc.append("outside" if z == 0 else "inside" if z < 1 else "boundary" if z == 1 else "wrong")
K["svm_xi"] = xi; K["svm_loc"] = loc
SW = [[10, 2], [2, 5]]; dm = (3, 1); det = SW[0][0] * SW[1][1] - SW[0][1] ** 2
wf = ((SW[1][1] * dm[0] - SW[0][1] * dm[1]) / det, (-SW[1][0] * dm[0] + SW[0][0] * dm[1]) / det)
K["fi_w"] = [r4(wf[0]), r4(wf[1])]
K["fi_bad"] = [r4(SW[0][0] * .3 + SW[0][1] * .087), r4(SW[1][0] * .3 + SW[1][1] * .087)]
m1, m2 = (4, 2), (1, 1); w0 = -(wf[0] * (m1[0] + m2[0]) + wf[1] * (m1[1] + m2[1])) / 2; nw = math.hypot(*wf)
gx = lambda x: wf[0] * x[0] + wf[1] * x[1] + w0
K["fi_conf"] = [r4(w0), r4(abs(gx(m1)) / nw), r4(abs(gx((2.8, 1.4))) / nw)]
C = [[0, 3, 8, 5, 6], [3, 0, 4, 7, 9], [8, 4, 0, 2, 6], [5, 7, 2, 0, 3], [6, 9, 6, 3, 0]]
l1, l2 = L(C, [2, 5, 1, 4, 3]), L(C, [1, 2, 3, 4, 5]); K["cold_tsp"] = [l1, l2, r4(100 / l1), r4(100 / l2)]
c = indices({"A": (1, 0), "B": (0, 3), "C": (2, 3), "D": (7, 2), "E": (9, 2), "F": (8, 5)}, ["A", "B", "C"], ["D", "E", "F"], [["A", "B", "C"], ["D", "E", "F"]])
K["cold_db"] = [c["delta1"], c["delta2"], c["d12"], c["DB"]]
K["cold_ch"] = [float(v) for v in c["gm"].split(",")] + [c["C1"], c["C2"], c["CH"]]
K["cold_svm"] = [r4(2 * 1.2 - 0.9 - 1), r4((2 * 1.2 - 0.9 - 1) / math.sqrt(5))]
f = fisher((5, 3), (1, 1), [[20, 4], [4, 12]], [[16, 2], [2, 20]], (3, 2.2)); K["cold_fi"] = [f["w1"], f["w2"]]
# retry keys must agree with final-mistakes.md
assert (K["cold_tsp"], K["cold_db"][3], K["cold_ch"][4], K["cold_fi"]) == ([26, 18, 3.8462, 5.5556], 0.4619, 4.6875, [0.1039, 0.043]), K

page = HERE / "final-relearn-c.html"; html = page.read_text()
if "--write" in sys.argv:
    html = html.replace("__KEYS__", json.dumps(K)); page.write_text(html)
stored = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', html, re.S).group(1))
bad = [k for k in K if stored.get(k) != K[k]] + [k for k in stored if k not in K]
ks = re.findall(r'data-k="([^"]+)"', html); ids = re.findall(r'data-id="([^"]+)"', html)
assert set(ks) == set(K), set(ks) ^ set(K)
assert len(ks + ids) == len(set(ks + ids)), "duplicate storage ids"
for stem, pages in re.findall(r'data-pages="([^:"]+):([0-9,]+)"', html):
    for p in pages.split(","):
        assert (HERE / "final-pages" / f"{stem}-p{int(p):03d}.jpg").exists(), (stem, p)
for k, v in K.items(): print(f"{k:10s} {v}")
if bad: print("MISMATCH:", bad); sys.exit(1)
print(f"ok: {len(K)} keys match final-relearn-c.html")
