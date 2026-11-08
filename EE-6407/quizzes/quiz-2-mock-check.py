"""Verify every numeric key in quiz-2-mock.md. Run: python3 quiz-2-mock-check.py"""
from fractions import Fraction as F
import math

close = lambda a, b, t=5e-4: abs(a - b) < t

# B1 Bernoulli Naive Bayes. rows: (Student, HighIncome, Weekend, class)
rows = [("Y","N","Y","Buy"),("Y","Y","Y","Buy"),("N","Y","Y","Buy"),("Y","N","N","Buy"),("Y","N","Y","Buy"),
        ("N","Y","N","No"),("N","N","N","No"),("Y","Y","N","No")]
def nb(x, lap=False):
    out = {}
    for c in ("Buy", "No"):
        R = [r for r in rows if r[3] == c]
        s = F(len(R), len(rows))
        for j, v in enumerate(x):
            k = sum(r[j] == v for r in R)
            s *= F(k + 1, len(R) + 2) if lap else F(k, len(R))
        out[c] = s
    return out
a = nb(("Y","N","N")); assert a == {"Buy": F(3,50), "No": F(1,24)}
assert close(float(a["Buy"]/(a["Buy"]+a["No"])), 0.590)
b = nb(("N","Y","Y")); assert b["Buy"] == F(1,25) and b["No"] == 0
c = nb(("N","Y","Y"), lap=True); assert c["Buy"] == F(75,1372) and c["No"] == F(27,1000)
assert close(float(c["Buy"]), 0.05466) and close(float(c["Buy"]/(c["Buy"]+c["No"])), 0.6694)

# B2 Fisher LDA
C1 = [(1,2),(2,4),(3,3)]; C2 = [(5,1),(6,3),(7,2)]
mean = lambda P: tuple(F(sum(p[i] for p in P), len(P)) for i in (0,1))
m1, m2 = mean(C1), mean(C2); assert m1 == (2,3) and m2 == (6,2)
def S(P, m):
    s = [[F(0)]*2 for _ in range(2)]
    for p in P:
        d = (p[0]-m[0], p[1]-m[1])
        for i in (0,1):
            for j in (0,1): s[i][j] += d[i]*d[j]
    return s
S1, S2 = S(C1, m1), S(C2, m2); assert S1 == [[2,1],[1,2]] == S2
Sw = [[S1[i][j]+S2[i][j] for j in (0,1)] for i in (0,1)]
det = Sw[0][0]*Sw[1][1]-Sw[0][1]*Sw[1][0]; assert det == 12
inv = [[Sw[1][1]/det, -Sw[0][1]/det], [-Sw[1][0]/det, Sw[0][0]/det]]
dm = (m1[0]-m2[0], m1[1]-m2[1])
w = tuple(inv[i][0]*dm[0]+inv[i][1]*dm[1] for i in (0,1)); assert w == (F(-3,2), 1)
w0 = -(w[0]*(m1[0]+m2[0]) + w[1]*(m1[1]+m2[1]))/2; assert w0 == F(7,2)
g = lambda x: w[0]*x[0] + w[1]*x[1] + w0
assert g(m1) == F(7,2) and g(m2) == F(-7,2) and g((4,3)) == F(1,2) and g((F(9,2),2)) == F(-5,4)
assert close(float(g((4,3)))/math.hypot(*map(float, w)), 0.2774)
for p in C1: assert g(p) > 0
for p in C2: assert g(p) < 0

# B3 soft-margin SVM: alphas given, C = 0.25
Cc = F(1,4)
sv = [((3,3),1,F(3,16)), ((4,2),1,F(1,8)), ((1,1),-1,F(1,16)), ((2,1),-1,F(1,4))]
assert sum(a*d for _,d,a in sv) == 0
w = tuple(sum(a*d*x[i] for x,d,a in sv) for i in (0,1)); assert w == (F(1,2), F(1,2))
margin = [(x,d) for x,d,a in sv if 0 < a < Cc]; assert len(margin) == 3
bs = [d - (w[0]*x[0]+w[1]*x[1]) for x,d in margin]; assert bs == [-2,-2,-2]
b = sum(bs)/len(bs)
wrong_b = sum(d-(w[0]*x[0]+w[1]*x[1]) for x,d,_ in sv)/4; assert wrong_b == F(-17,8)
f = lambda x: w[0]*x[0]+w[1]*x[1]+b
assert f((5,0)) == F(1,2)
assert 1 - (-1)*f((2,1)) == F(1,2)           # slack of the bounded SV
assert close(2/math.hypot(0.5,0.5), 2.8284)

# B4 Gini
xs = [22,25,28,31,35,40,44,50,55,60]; ys = list("NNYNYYYYNY")
gini = lambda L: 1 - sum((L.count(k)/len(L))**2 for k in set(L)) if L else 0
assert close(gini(ys), 0.48)
def split(t):
    L = [y for x,y in zip(xs,ys) if x < t]; R = [y for x,y in zip(xs,ys) if x >= t]
    return len(L)/10*gini(L) + len(R)/10*gini(R)
assert close(split(26.5), 0.300) and close(split(33), 0.3167) and close(split(52.5), 0.475)
smoker = 0.5*(1-(0.8**2+0.2**2)) + 0.5*(1-(0.4**2+0.6**2)); assert close(smoker, 0.400)
assert close(0.48 - split(26.5), 0.18)

# B5 confusion matrix
TP, FN, FP, TN = 40, 10, 8, 142
P, R = TP/(TP+FP), TP/(TP+FN)
assert close((TP+TN)/200, 0.91) and close(P, 0.8333) and R == 0.8
assert close(TN/(TN+FP), 0.9467) and close(2*P*R/(P+R), 0.8163) and close(FP/(FP+TN), 0.0533)
assert close((FP+TN)/200, 0.75)

# B6 HAC on 1-D points + k-means
pts = {"A":1, "B":2, "C":4.5, "D":8, "E":9.5}
def hac(link):
    cl = [frozenset(k) for k in pts]; seq = []
    while len(cl) > 1:
        best = min(((link(abs(pts[i]-pts[j]) for i in p for j in q), p, q)
                    for a, p in enumerate(cl) for q in cl[a+1:]), key=lambda t: t[0])
        d, p, q = best; cl = [c for c in cl if c not in (p, q)] + [p | q]
        seq.append(("".join(sorted(p | q)), d))
    return seq
assert hac(min) == [("AB",1), ("DE",1.5), ("ABC",2.5), ("ABCDE",3.5)]
assert hac(max) == [("AB",1), ("DE",1.5), ("ABC",3.5), ("ABCDE",8.5)]
c1, c2 = 1, 9.5
for _ in range(3):
    g1 = [v for v in pts.values() if abs(v-c1) <= abs(v-c2)]; g2 = [v for v in pts.values() if v not in g1]
    c1, c2 = sum(g1)/len(g1), sum(g2)/len(g2)
assert (c1, c2) == (2.5, 8.75)

# C Fisher ratio, population variance (divide by N) as in the worked example
def fr(a, b):
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    va = sum((v-ma)**2 for v in a)/len(a); vb = sum((v-mb)**2 for v in b)/len(b)
    return (ma-mb)**2/(va+vb)
assert close(fr([1,2,3],[4,5,6]), 6.75) and close(fr([2,6,4],[3,7,5]), 0.1875)

print("all quiz-2 mock keys verified")

# primer quick checks
assert 30 + 1.5*10 == 45
assert max(0.5*0.2*0.5, 0.5*0.4*0.1) == 0.05
assert (4/4) == 1                                  # w = diag(1/2,1/4)(2,4) = (1,1)
assert round(2/math.sqrt(5), 3) == 0.894
assert close(1-0.49-0.09, 0.42) and 30/40 == 0.75 and 1-20/100 == 0.8
assert 9/(1+2) == 3 and min(abs(a-b) for a in (1,2) for b in (6,9)) == 4
print("primer checks verified")
