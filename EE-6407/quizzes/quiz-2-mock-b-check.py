"""Independent checker for every numeric key in EE-6407/quizzes/quiz-2-mock-b.md.
Run:  python3 quizzes/quiz-2-mock-b-check.py   (needs numpy). Silent asserts; prints the key."""
import itertools, math
import numpy as np

close = lambda a, b, t=1e-3: abs(a - b) < t

# ---------------- B1  Fisher LDA (two classes) ----------------
X1 = np.array([(1, 1), (2, 3), (3, 2)], float)
X2 = np.array([(5, 3), (6, 5), (7, 4)], float)
m1, m2 = X1.mean(0), X2.mean(0)
scatter = lambda X, m: sum(np.outer(x - m, x - m) for x in X)
S1, S2 = scatter(X1, m1), scatter(X2, m2)
Sw = S1 + S2
w = np.linalg.inv(Sw) @ (m1 - m2)
w0 = -0.5 * w @ (m1 + m2)
g = lambda x: w @ np.array(x, float) + w0
assert np.allclose(m1, (2, 2)) and np.allclose(m2, (6, 4))
assert np.allclose(S1, [[2, 1], [1, 2]]) and np.allclose(S2, [[2, 1], [1, 2]])
assert np.allclose(Sw, [[4, 2], [2, 4]]) and close(np.linalg.det(Sw), 12)
assert np.allclose(w, (-1, 0)) and close(w0, 4)
assert close(g((3.5, 5)), 0.5) and close(g((4.5, 0)), -0.5)
# naive "difference of means" direction would wrongly use x2:
assert not np.allclose((m1 - m2) / np.linalg.norm(m1 - m2), w / np.linalg.norm(w))
print("B1 m1", m1, "m2", m2, "Sw", Sw.tolist(), "w", w, "w0", w0,
      "g(3.5,5)", g((3.5, 5)), "g(4.5,0)", g((4.5, 0)))

# ---------------- B2  soft-margin SVM: w and b from alphas ----------------
C = 1.5
S = [((2, 2), +1, 1.0), ((3, 1), +1, 0.75), ((1, 1), -1, 0.25), ((2, 1), -1, 1.5),
     ((4, 4), +1, 0.0), ((0, 0), -1, 0.0)]
assert close(sum(a * d for _, d, a in S), 0)                     # sum alpha_i d_i = 0
wv = sum(a * d * np.array(x, float) for x, d, a in S)
assert np.allclose(wv, (1, 1))
margin = [(x, d) for x, d, a in S if 0 < a < C]
bs = [d - wv @ np.array(x, float) for x, d in margin]
b = float(np.mean(bs))
assert all(close(v, -3) for v in bs) and close(b, -3)
wrong_b = float(np.mean([d - wv @ np.array(x, float) for x, d, a in S if a > 0]))
assert close(wrong_b, -3.25)                                     # trap: including alpha=C point
f = lambda x: wv @ np.array(x, float) + b
# KKT: alpha=0 -> d f >= 1 ; 0<alpha<C -> d f = 1 ; alpha=C -> d f <= 1  => this IS the optimum
for x, d, a in S:
    yf = d * f(x)
    if a == 0: assert yf >= 1
    elif a < C: assert close(yf, 1)
    else: assert yf <= 1 + 1e-9
assert close(1 - (-1) * f((2, 1)), 1)                            # slack of the bounded SV = 1
assert close(f((3, 0.5)), 0.5) and close(f((1, 1.5)), -0.5)
print("B2 w", wv, "b", b, "(wrong avg incl. alpha=C:", wrong_b, ") f(3,0.5)", f((3, .5)), "f(1,1.5)", f((1, 1.5)))

# ---------------- B3  classification tree: impurity drop ----------------
H = lambda ps: -sum(p * math.log2(p) for p in ps if p > 0)
G = lambda ps: 1 - sum(p * p for p in ps)
M = lambda ps: 1 - max(ps)
def drop(fn, parent, kids):
    n = sum(parent)
    pr = lambda c: [k / sum(c) for k in c]
    return fn(pr(parent)) - sum(sum(c) / n * fn(pr(c)) for c in kids)
root = (8, 8)
splitA = [(6, 2), (2, 6)]
splitB = [(4, 0), (4, 8)]
res = {(nm, s): drop(fn, root, kids) for nm, fn in (("entropy", H), ("gini", G), ("miscl", M))
       for s, kids in (("A", splitA), ("B", splitB))}
assert close(res["entropy", "A"], 0.1887) and close(res["entropy", "B"], 0.3113)
assert close(res["gini", "A"], 0.125) and close(res["gini", "B"], 1 / 6)
assert close(res["miscl", "A"], 0.25) and close(res["miscl", "B"], 0.25)   # tie
assert close(H([1/3, 2/3]), 0.9183) and close(H([.25, .75]), 0.8113)
# hand formulas with log2(3) = 1.585 given in the paper
L3 = 1.585
assert close(L3 - 2/3, 0.9183, 2e-3) and close(2 - 0.75 * L3, 0.8113, 2e-3)
print("B3", {k: round(v, 4) for k, v in res.items()})

# ---------------- B4(a)  Fisher's ratio ----------------
def FR(a, b):
    a, b = np.array(a, float), np.array(b, float)
    return (a.mean() - b.mean()) ** 2 / (a.var() + b.var())   # np.var divides by N (archive convention)
fr1 = FR([1, 2, 3], [4, 5, 6]); fr2 = FR([0, 4, 8], [6, 10, 14])
assert close(fr1, 6.75) and close(fr2, 1.6875) and fr1 > fr2
print("B4a FR(f1)", fr1, "FR(f2)", fr2)

# ---------------- B4(b)  HAC, Manhattan distance ----------------
P = {"A": (0, 0), "B": (0, 1), "C": (0, 3), "D": (3, 0), "E": (6, 1)}
man = lambda p, q: abs(p[0] - q[0]) + abs(p[1] - q[1])
def hac(link):
    cl = [(k,) for k in P]; steps = []
    while len(cl) > 1:
        cand = sorted(((min if link == "single" else max)(man(P[a], P[b]) for a in ci for b in cj), i, j)
                      for (i, ci), (j, cj) in itertools.combinations(enumerate(cl), 2))
        assert len(cand) == 1 or cand[0][0] < cand[1][0], ("tie", link, cand[:3], cl)
        d, i, j = cand[0]
        steps.append(("".join(cl[i]), "".join(cl[j]), d))
        cl = [c for k, c in enumerate(cl) if k not in (i, j)] + [tuple(sorted(cl[i] + cl[j]))]
    return steps
single, complete = hac("single"), hac("complete")
norm = lambda st: [({x, y}, d) for x, y, d in st]
assert norm(single) == norm([("A", "B", 1), ("AB", "C", 2), ("ABC", "D", 3), ("ABCD", "E", 4)])
assert norm(complete) == norm([("A", "B", 1), ("AB", "C", 3), ("D", "E", 4), ("ABC", "DE", 8)])
print("B4b single", single); print("B4b complete", complete)
print("B4b Manhattan matrix:")
for p in P: print("  ", p, [man(P[p], P[q]) for q in P])

# ---------------- C  imbalanced evaluation ----------------
def metrics(TP, FN, FP, TN):
    acc = (TP + TN) / (TP + FN + FP + TN)
    pre = TP / (TP + FP) if TP + FP else float("nan")
    rec = TP / (TP + FN)
    f1 = 2 * pre * rec / (pre + rec) if TP else 0.0
    return acc, pre, rec, f1
A_ = metrics(0, 50, 0, 950)
B_ = metrics(40, 10, 60, 890)
assert close(A_[0], 0.95) and A_[2] == 0 and A_[3] == 0 and math.isnan(A_[1])
assert close(B_[0], 0.93) and close(B_[1], 0.4) and close(B_[2], 0.8) and close(B_[3], 8 / 15)
print("C  classifier A acc/pre/rec/F1", A_); print("C  classifier B acc/pre/rec/F1", B_)
print("all asserts passed")
