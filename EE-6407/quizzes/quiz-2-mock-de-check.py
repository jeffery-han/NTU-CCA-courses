"""Independent check of every numeric key in quiz-2-mock-d/e (run: python3 quiz-2-mock-de-check.py)."""
from fractions import Fraction as F
def d2(p, c): return (p[0]-c[0])**2 + (p[1]-c[1])**2
def kmeans(P):
    c, lab, moves = [P[0], P[1]], None, []
    while True:
        nl = []
        for p in P:
            a, b = d2(p, c[0]), d2(p, c[1]); assert a != b, 'tie'
            nl.append(0 if a < b else 1)
        if nl == lab: break
        if lab: moves.append([i for i in range(len(P)) if nl[i] != lab[i]])
        lab = nl
        c = [tuple(F(sum(p[j] for p, l in zip(P, lab) if l == k), lab.count(k)) for j in (0, 1)) for k in (0, 1)]
    return lab, c, moves, sum(d2(p, c[l]) for p, l in zip(P, lab))
def metrics(TP, FN, FP, TN):
    N = TP+FN+FP+TN; P = F(TP, TP+FP); R = F(TP, TP+FN)
    return dict(acc=F(TP+TN, N), err=F(FP+FN, N), rec=R, spec=F(TN, TN+FP), prec=P, f=2*P*R/(P+R))
def fisher(rows): return [(F(a)-F(b))**2/(F(s)**2+F(t)**2) for a, b, s, t in rows]

# Mock D
m = metrics(80, 20, 20, 180); assert (m['acc'], m['err'], m['rec'], m['spec'], m['prec'], m['f']) == (F(13,15), F(2,15), F('0.8'), F('0.9'), F('0.8'), F('0.8'))
m = metrics(80, 20, 40, 360); assert (m['prec'], m['f'], m['acc'], m['err'], m['rec'], m['spec']) == (F(2,3), F(8,11), F(22,25), F(3,25), F('0.8'), F('0.9'))
lab, c, mv, sse = kmeans([(5,2),(5,5),(4,7),(3,7),(2,4),(2,3),(6,7)])
assert lab == [0,1,1,1,0,0,1] and c == [(3,3),(F(9,2),F(13,2))] and mv == [[4]] and sse == 16
assert fisher([('3','5','0.8','0.6'),('1','4','1.2','1.6'),('6','8','1','1'),('2','2.5','0.4','0.3')]) == [4, F(9,4), 2, 1]
# Mock E
m = metrics(40, 10, 30, 120); assert (m['acc'], m['err'], m['rec'], m['spec'], m['prec'], m['f']) == (F('0.8'), F('0.2'), F('0.8'), F('0.8'), F(4,7), F(2,3))
m = metrics(80, 20, 30, 120); assert (m['prec'], m['f'], m['acc'], m['err']) == (F(8,11), F(16,21), F('0.8'), F('0.2'))
lab, c, mv, sse = kmeans([(2,0),(5,7),(3,5),(1,6),(7,4),(0,0),(4,3)])
assert lab == [0,1,1,1,1,0,1] and c == [(1,0),(4,5)] and mv == [[6]] and sse == 32
assert fisher([('0','2','1','1'),('5','6','0.3','0.4'),('2','6','2.4','3.2'),('4','7','0.6','0.8')]) == [2, 4, 1, 9]
print('Mock D and Mock E keys: all checks pass')
