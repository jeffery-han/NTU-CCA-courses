"""Recompute every check key in final-primer.html and verify its citations.  Run: python3 final-check.py"""
from fractions import Fraction as F
from math import exp, sqrt, log
import json, os, re, cmath

here = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(here, 'final-primer.html'), encoding='utf-8').read()
KEYS = json.loads(re.search(r'<script type="application/json" id="keys">(.*?)</script>', html, re.S).group(1))

def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def inv2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return [[M[1][1] / d, -M[0][1] / d], [-M[1][0] / d, M[0][0] / d]]
def poly2(M, c1, c0): return [[(M2 := mm(M, M))[i][j] + c1 * M[i][j] + (c0 if i == j else 0) for j in range(2)] for i in range(2)]

got = {}
# Z1: FVT of 0.6 z^2 / ((z-1)(z-0.8)) -> 0.6/(1-0.8)
got['fvt'] = F(6, 10) / (1 - F(8, 10))
# Z2: y(k+2) - 0.5 y(k+1) = x(k), y(k)=0 for k<0
y = {-2: F(0), -1: F(0)}
for k in range(-2, 4): y[k + 2] = F(1, 2) * y[k + 1] + (1 if k >= 0 else 0)
got['de'] = y[3]
# Z3: G = 2/(s+2), T = ln 2: G_ZAS = (1 - e^{-2T})/(z - e^{-2T})
got['zas'] = 1 - exp(-2 * log(2))
# J1: CE z^2 + (0.2K - 1.4) z + (0.4 + 0.2K); scan K for stability
def stable(K):
    a1, a0 = 0.2 * K - 1.4, 0.4 + 0.2 * K; d = cmath.sqrt(a1 * a1 - 4 * a0)
    return max(abs((-a1 + d) / 2), abs((-a1 - d) / 2)) < 1 - 1e-9
ks = [k / 1000 for k in range(-2000, 6000) if stable(k / 1000)]
assert abs(min(ks) - 0.001) < 1e-9
got['jury'] = round(max(ks) + 0.001, 6)
got['ess'] = 1 / ((0.2 * 2 / 0.6) / 0.2)                  # Kv = (z-1)G/(Tz) at z = 1
# D1: ripple-free for G = 0.2(z+0.6)/((z-1)(z-0.3)): K = 1/1.6; U = Gcl R / G
got['rf'] = F(1) / F(16, 10)
got['rfu'] = got['rf'] / F(2, 10)                            # u(0) = K/0.2 (leading coefficient of U)
# simulate the loop to confirm u(0) and that u settles
yy, uu = [0.0] * 10, [0.0] * 10
# U(z) = Gcl R / G = 3.125 (z - 0.3)/z  ->  u = 3.125, -0.9375, 0, 0, ...; drive the plant with it
for k in range(10):
    uu[k] = {0: 3.125, 1: -0.9375}.get(k, 0.0)
    yy[k] = (yy[k-1] * 1.3 if k >= 1 else 0) - (0.3 * yy[k-2] if k >= 2 else 0) + (0.2 * uu[k-1] if k >= 1 else 0) + (0.12 * uu[k-2] if k >= 2 else 0)
assert abs(yy[1] - 0.625) < 1e-12 and all(abs(v - 1) < 1e-12 for v in yy[2:]), yy
# P1: D(s) = 2(s+1)/(s+4), T = 0.5, D(0) = 0.5
got['pz'] = 0.5 * (1 - exp(-2)) / (1 - exp(-0.5))
# S1: double integrator T = 0.5: Theta = [T^2/2, T]
T = F(1, 2)
A = [[F(1), T], [F(0), F(1)]]; B = [[T * T / 2], [T]]
got['th'] = B[0][0]
# S2: x(0)=0, u(0)=u(1)=1 -> x(2) = A B + B
x2 = [[mm(A, B)[i][0] + B[i][0]] for i in range(2)]
got['rec'] = x2[0][0]
# S3: deadbeat Ackermann K = [0 1] Wc^-1 A^2
Wc = [[B[0][0], mm(A, B)[0][0]], [B[1][0], mm(A, B)[1][0]]]
K = mm(mm([[0, 1]], inv2(Wc)), poly2(A, 0, 0))[0]
assert K == [1 / T ** 2, F(3, 2) / T]
got['k1'], got['k2'] = K
ABK = [[A[i][j] - B[i][0] * K[j] for j in range(2)] for i in range(2)]
assert mm(ABK, ABK) == [[0, 0], [0, 0]]
# O1: observer poles at 0.2, 0.2: alpha = z^2 - 0.4 z + 0.04
Cm = [[F(1), F(0)]]
Wo = [Cm[0], mm(Cm, A)[0]]
L = mm(poly2(A, F(-4, 10), F(4, 100)), mm(inv2(Wo), [[0], [1]]))
got['lo1'], got['lo2'] = L[0][0], L[1][0]
ALC = [[A[i][j] - L[i][0] * Cm[0][j] for j in range(2)] for i in range(2)]
assert (ALC[0][0] + ALC[1][1], ALC[0][0] * ALC[1][1] - ALC[0][1] * ALC[1][0]) == (F(4, 10), F(4, 100))
# Ex 4.3 statement on the card: deadbeat L = [2, 1/T], (A - LC)^2 = 0
L43 = mm(poly2(A, 0, 0), mm(inv2(Wo), [[0], [1]]))
assert L43 == [[2], [1 / T]]
# O2: reduced-order, Aaa = 1, Aab = T, Abb = 1, pole 0.4: z - 1 + T Lr = z - 0.4
got['lr'] = (1 - F(4, 10)) / T
assert (1 - F(5, 10)) / F(1, 10) == 5                         # Ex 4.4 on the card
# O3: k_r = 1 / [C (I - A + BK)^-1 B]
IAB = [[(1 if i == j else 0) - ABK[i][j] for j in range(2)] for i in range(2)]
got['kr'] = 1 / mm(Cm, mm(inv2(IAB), B))[0][0]
# L1: x(k+1) = 0.5x + u, Q = R = 2, S(2) = 0
a, b, Q, R = F(1, 2), F(1), F(2), F(2)
S = F(0)
for _ in range(2):
    Kk = b * S * a / (b * b * S + R); S = (a - b * Kk) ** 2 * S + R * Kk * Kk + Q
got['lq1'] = Kk
# Ex 5.2 on the card: A = 2, B = 1, Q = R = 2, S(3) = 0 -> K(1) = 1, S(1) = 6, K(0) = 1.5, S(0) = 8
S, seq = F(0), []
for _ in range(3):
    Kk = F(2) * S / (S + 2); S = (2 - Kk) ** 2 * S + 2 * Kk * Kk + 2; seq.append((Kk, S))
assert seq == [(0, 2), (1, 6), (F(3, 2), 8)]
# L2: x(k+1) = 2x + u, Q = R = 2, infinite horizon: S^2 - 8S - 4 = 0
S = 0.0
for _ in range(300):
    Kk = 2 * S / (S + 2); S = (2 - Kk) ** 2 * S + 2 * Kk * Kk + 2
assert abs(S - (4 + 2 * sqrt(5))) < 1e-9
got['lq2'], got['lq2s'] = Kk, S
# Ex 5.4 typo note: 0.2087^15 ~ 0.62e-10
assert abs(0.2087 ** 15 - 0.6206e-10) / 0.6206e-10 < 0.02 and abs(0.2807 ** 15 - 0.6206e-10) / 0.6206e-10 > 50

assert set(got) == set(KEYS), set(got) ^ set(KEYS)
for k, v in got.items():
    assert abs(float(v) - KEYS[k]) <= max(0.0015, abs(KEYS[k]) * 0.002) / 2, (k, float(v), KEYS[k])

# every numeric input maps to a key, every select card has data-sel
cards = re.findall(r'<div class="card" data-k="([^"]+)"([^>]*)>(.*?)\n</div>', html, re.S)
assert len(cards) == 14, len(cards)
for k, attrs, body in cards:
    assert k in KEYS
    if 'data-num="2"' in body: assert 'data-k2=' in attrs and re.search(r'data-k2="([^"]+)"', attrs).group(1) in KEYS
    if '<select>' in body:
        sel = re.search(r'data-sel="([^"]+)"', attrs).group(1)
        assert '<option>' + sel + '</option>' in body, (k, sel)
    assert '<div class="chk">' in body, k                     # every card ends with a check
# citations: target PDF exists, page images exist for the whole range
res = os.path.normpath(os.path.join(here, '..', '..', 'resources'))
cites = re.findall(r'href="\.\./\.\./resources/([^"#]+)#page=(\d+)" data-pages="([^:]+):(\d+)(?:-(\d+))?"', html)
assert len(cites) >= 20, len(cites)
for pdf, first, stem, a, b in cites:
    assert os.path.exists(os.path.join(res, pdf)), pdf
    assert pdf == stem + '.pdf' and first == a, (pdf, first, stem, a)
    for p in range(int(a), int(b or a) + 1):
        assert os.path.exists(os.path.join(here, 'final-pages', '%s-p%03d.jpg' % (stem, p))), (stem, p)
for rel in re.findall(r'href="(\.\./[^"#]+)"', html):
    assert os.path.exists(os.path.normpath(os.path.join(here, rel))), rel
print('final-primer keys and citations OK (%d checks keyed, %d citations)' % (len(KEYS), len(cites)))
