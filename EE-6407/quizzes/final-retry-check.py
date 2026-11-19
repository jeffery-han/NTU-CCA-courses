"""Key checker for final-retry.html (EE6407 final, cold retries of the Mock B mistakes).

Recomputes every numeric key from the question data and asserts that the JSON in
<script id="keys"> of final-relearn.html matches; also checks that every data-k has a key,
that storage ids are unique, and that every cited page image exists.
Run:  python3 final-retry-check.py
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
s, f = svm([((3, 0), 1, .625), ((3, 2), 1, .625), ((1, 0), -1, .125), ((1, 2), -1, .125), ((2.5, 1), -1, 1.0), ((0, 4), -1, 0.0)], 1)
g, dd = f((2.4, 5))
K["r1_w"] = [s["w1"], s["w2"]]; K["r1_which"] = "1234"; K["r1_b"] = s["b"]; K["r1_mx"] = [s["margin"], s["xi"]]; K["r1_g"] = [r4(g), r4(dd)]
assert s["b_wrong"] == -2.3
m = mnb({"Sports": ["ball goal ball", "goal team"], "Politics": ["vote team", "vote law vote"]}, "ball vote team")
K["r2_counts"] = [m["d"], m["n_Sports"], m["n_Politics"]]
K["r2_sports"] = [m["p_ball_Sports"], m["p_vote_Sports"], m["p_team_Sports"]]
K["r2_politics"] = [m["p_ball_Politics"], m["p_vote_Politics"], m["p_team_Politics"]]
K["r2_scores"] = [r4(m["score_Sports"] * 1e3), r4(m["score_Politics"] * 1e3), m["class"]]
gn = gnb({1: (.5, (0, 2), (1, 1)), 2: (.5, (2, 1), (4, 1))}, (1, 2))
K["r3_lik"] = [gn["lik1"], gn["lik2"]]; K["r3_g"] = [gn["g1"], gn["g2"], gn["class"]]; K["r3_post"] = gn["post1"]
P = {"P": (0, 0), "Q": (1, 1), "R": (4, 0), "S": (4, 3)}
K["r4_matrix"] = [r4(math.dist(P[a], P[b])) for a, b in ["PQ", "PR", "PS", "QR", "QS", "RS"]]
K["r4_merges"] = [float(x.split("@")[1]) for x in single_link(P)]
ci = indices(P, ["P", "Q"], ["R", "S"], [["P"], ["Q", "R"], ["S"]])
K["r5_m"] = [float(v) for v in ci["m1"].split(",") + ci["m2"].split(",")]
K["r5_db"] = [ci["delta1"], ci["delta2"], ci["d12"], ci["DB"]]
gi = gini_split((6, 6), {"X": ((5, 3), (1, 3)), "Y": ((3, 0), (3, 6))})
K["r6"] = [gi["root"], gi["X_w"], gi["Y_w"], gi["best"]]
K["r7"] = pmx([3, 5, 1, 7, 2, 8, 6, 4], [8, 6, 2, 4, 3, 1, 7, 5], 2, 4)
K["r8"] = [ci["inter"], ci["diam"], ci["dunn"]]
K["r9"] = [ci["Ns"], ci["Nd"], ci["RI"]]
# keys must agree with final-mistakes.md
assert (K["r1_w"], K["r1_b"], K["r2_scores"][2], K["r3_post"], K["r4_merges"], K["r5_db"][3], K["r6"][3], K["r7"], K["r8"][2], K["r9"][2]) == \
    ([1, 0], -2, "Politics", 0.6938, [1.4142, 3.0, 3.1623], 0.6063, "Y", "86172345", 1.0541, 0.5), K

page = HERE / "final-retry.html"; html = page.read_text()
if "--write" in sys.argv:
    html = html.replace("__KEYS__", json.dumps(K)); page.write_text(html)
stored = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', html, re.S).group(1))
bad = [k for k in K if stored.get(k) != K[k]] + [k for k in stored if k not in K]
ks = re.findall(r'data-k="([^"]+)"', html); ids = re.findall(r'data-id="([^"]+)"', html)
assert set(ks) == set(K), set(ks) ^ set(K)
assert len(ks + ids) == len(set(ks + ids)), "duplicate storage ids"
for anchor in re.findall(r'href="final-relearn.html#(m\d)"', html):
    assert f'id="{anchor}"' in (HERE / "final-relearn.html").read_text(), anchor
for k, v in K.items(): print(f"{k:12s} {v}")
if bad: print("MISMATCH:", bad); sys.exit(1)
print(f"ok: {len(K)} keys match final-retry.html")
