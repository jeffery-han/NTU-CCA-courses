"""Recompute every check key in final-primer.html and verify its citations.  Run: python3 final-check.py"""
from fractions import Fraction as F
from math import exp, sqrt, log, acos
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

# ---------- part exercises E1-E4: recompute every key number, check marks and that the page is answer-free ----------
md = open(os.path.join(here, 'final-primer-exercises.md'), encoding='utf-8').read()
def has(*vals):
    for v in vals: assert v.replace('-', '−') in md, v
def r4(x): return '%.4f' % x
# E1a: series vs closed form 0.25(z^3+z^2+z+1)/(z^3(z-1))
xs = [0, .25, .5, .75] + [1] * 400
for zz in (1.3, 2.0, -1.7):
    assert abs(sum(v * zz ** -k for k, v in enumerate(xs)) - 0.25 * (zz**3 + zz**2 + zz + 1) / (zz**3 * (zz - 1))) < 1e-9
# E1b: y1 final value, y3 closed form
y1 = [0.0]; y1 += [0.5 * sum(0.6 ** j for j in range(k)) for k in range(1, 200)]
assert abs(y1[-1] - 1.25) < 1e-9
y3 = [5 * 1.2 ** k - 5 for k in range(6)]; assert y3[0] == 0 and abs(y3[1] - 1) < 1e-12 and abs(y3[2] - 2.2) < 1e-12  # y(k+1) = 1.2y(k) + u
has('1.25', '5(1.2)ᵏ − 5')
# E1c: recursion vs closed form
y = {-2: 0.0, -1: 0.0}
for k in range(-2, 30): y[k + 2] = 0.7 * y[k + 1] - 0.1 * y[k] + 2 * (1 if k + 1 >= 0 else 0)
assert y[0] == 0 and y[1] == 2 and abs(y[2] - 3.4) < 1e-12
assert all(abs(y[k] - (5 - 20 / 3 * .5 ** k + 5 / 3 * .2 ** k)) < 1e-9 for k in range(30))
has('y(1) = 2**', '5 − (20/3)(0.5)ᵏ + (5/3)(0.2)ᵏ', '3.4')
# E1d: G_ZAS from step response of 1/((s+1)(s+2)) at T = ln 2: h(t) = 0.5 - e^-t + 0.5e^-2t
T = log(2); h = lambda t: 0.5 - exp(-t) + 0.5 * exp(-2 * t)
imp = []
for k in range(12):  # simulate 0.125(z+0.5)/((z-.5)(z-.25)): y(k) = .75y(k-1) - .125y(k-2) + .125u(k-1) + .0625u(k-2)
    u1 = 1 if k == 1 else 0; u2 = 1 if k == 2 else 0
    imp.append((0.75 * imp[k-1] if k >= 1 else 0) - (0.125 * imp[k-2] if k >= 2 else 0) + 0.125 * u1 + 0.0625 * u2)
assert all(abs(imp[k] - ((h(k * T) - h((k - 1) * T)) if k >= 1 else 0)) < 1e-12 for k in range(12))
a1, a0 = -0.75 + 2 * 0.125, 0.125 + 2 * 0.0625; assert (a1, a0) == (-0.5, 0.25)
p = complex(0.25, sqrt(0.25 - 0.0625)); assert abs(abs(p) - 0.5) < 1e-12
has('0.125(z + 0.5)/((z − 0.5)(z − 0.25))', '0.25(z + 0.5)/(z² − 0.5z + 0.25)', '0.25 ± j' + r4(p.imag))
# E2a
def st2(K):
    b1, b0 = 0.1 * K - 1.7, 0.7 + 0.08 * K; d = cmath.sqrt(b1 * b1 - 4 * b0)
    return max(abs((-b1 + d) / 2), abs((-b1 - d) / 2)) < 1 - 1e-9
ks = [k / 1000 for k in range(-3000, 10000) if st2(k / 1000)]
assert abs(min(ks) - 0.001) < 1e-9 and abs(max(ks) + 0.001 - 3.75) < 1e-9
w = acos(1.325 / 2) / 0.1; has('%.3f rad/s' % w)
Kv = 2 * 0.1 * 1.8 / (0.3 * 0.1); assert abs(Kv - 12) < 1e-9; has('1/12 = 0.0833')
# E2b: drive the plant with both control sequences
def plant(u, n=10):  # y(k) = 1.7y(k-1) - 0.7y(k-2) + 0.1u(k-1) + 0.08u(k-2)
    yv = []
    for k in range(n): yv.append((1.7 * yv[k-1] if k >= 1 else 0) - (0.7 * yv[k-2] if k >= 2 else 0) + (0.1 * u[k-1] if k >= 1 else 0) + (0.08 * u[k-2] if k >= 2 else 0))
    return yv
ud = [10.0] + [-15 * (-0.8) ** (k - 1) for k in range(1, 10)]
assert [round(v, 6) for v in ud[:4]] == [10, -15, 12, -9.6] and all(abs(v - 1) < 1e-9 for v in plant(ud)[1:])
Kr = 1 / 1.8; ur = [Kr / 0.1, -0.7 * Kr / 0.1] + [0.0] * 8
yr = plant(ur); assert abs(yr[1] - Kr) < 1e-12 and all(abs(v - 1) < 1e-12 for v in yr[2:])
has(r4(Kr), '5.556(z − 0.7)/(z + 0.4444)', '5.556, −3.889, 0, 0')
# E2c: Tustin of (s+2)/(s+10), T = 0.1
c = 2 / 0.1
nz, nc, dz, dc = c + 2, -c + 2, c + 10, -c + 10
assert (nz, nc, dz, dc) == (22, -18, 30, -10)
has(r4(nz / dz), r4(-nc / nz), r4(-dc / dz), '0.6 m(k − 1)'); assert abs(nz / dz * (-nc / nz) - 0.6) < 1e-12
assert abs((nz + nc) / (dz + dc) - 0.2) < 1e-12
# E3
T = 0.2; e2 = exp(-2 * T)
Phi = [[1, (1 - e2) / 2], [0, e2]]; Th = [[T / 2 - (1 - e2) / 4], [(1 - e2) / 2]]
for t in (0.1, 0.2, 0.37):  # e^{At} by series
    M = [[1, 0], [0, 1]]; S_ = [[1.0, 0.0], [0.0, 1.0]]; At = [[0, t], [0, -2 * t]]
    for n in range(1, 40): M = [[v / n for v in row] for row in mm(M, At)]; S_ = [[S_[i][j] + M[i][j] for j in range(2)] for i in range(2)]
    assert abs(S_[0][1] - (1 - exp(-2 * t)) / 2) < 1e-12 and abs(S_[1][1] - exp(-2 * t)) < 1e-12
th1 = sum(((1 - exp(-2 * (i + .5) * T / 2000)) / 2) * T / 2000 for i in range(2000)); assert abs(th1 - Th[0][0]) < 1e-8
has('%.4f' % Phi[0][1], '%.4f' % e2, '%.5f' % Th[0][0])
n0 = Th[0][0]; n1 = Phi[0][1] * Th[1][0] - Th[0][0] * Phi[1][1]
has('%.5f' % n0 + 'z + ' + '%.5f' % n1, '(z + ' + r4(n1 / n0) + ')')
assert abs((n0 + n1) / (1 - e2) / T - 0.5) < 1e-12
PT = mm(Phi, Th); dWc = Th[0][0] * PT[1][0] - PT[0][0] * Th[1][0]
has('%.5f' % PT[0][0], '%.4f' % PT[1][0], '%.6f' % dWc, r4(0.1 / Phi[0][1]))
# E4
A = [[1, 0.4], [0, 0.6]]; B = [[0.2], [1]]; Cm = [[1, 0]]
AB = mm(A, B); Wc = [[B[0][0], AB[0][0]], [B[1][0], AB[1][0]]]
K4 = mm(mm([[0, 1]], inv2(Wc)), poly2(A, -0.8, 0.25))[0]
ABK = [[A[i][j] - B[i][0] * K4[j] for j in range(2)] for i in range(2)]
assert abs(ABK[0][0] + ABK[1][1] - 0.8) < 1e-12 and abs(ABK[0][0] * ABK[1][1] - ABK[0][1] * ABK[1][0] - 0.25) < 1e-12
has(r4(K4[0]) + ' ' + r4(K4[1]), r4(ABK[0][1]), r4(ABK[1][1]))
Wo = [Cm[0], mm(Cm, A)[0]]; L4 = mm(poly2(A, 0, 0), mm(inv2(Wo), [[0], [1]]))
ALC = [[A[i][j] - L4[i][0] * Cm[0][j] for j in range(2)] for i in range(2)]
assert all(abs(v) < 1e-12 for row in mm(ALC, ALC) for v in row)
has('[%.1f; %.1f]' % (L4[0][0], L4[1][0]))
Lr = (0.6 - 0.2) / 0.4; assert abs(Lr - 1) < 1e-12 and abs((1 - Lr * 0.2) - 0.8) < 1e-12
IAB = [[(1 if i == j else 0) - ABK[i][j] for j in range(2)] for i in range(2)]
kr4 = 1 / mm(Cm, mm(inv2(IAB), B))[0][0]; has('**k_r = ' + r4(kr4))
Sx = 0.0
for _ in range(500): Kq = 1.5 * Sx / (Sx + 2); Sx = (1.5 - Kq) ** 2 * Sx + 2 * Kq * Kq + 2
assert abs(Sx * Sx - 4.5 * Sx - 4) < 1e-9
has(r4(Sx), r4(Kq), r4(1.5 - Kq), r4((1.5 - Kq) ** 2), r4(Sx / 2))
# page: four exercises, marks attribute sums to 25 and matches each part's heading, no key numbers leaked
exs = re.findall(r'<div class="card exercise" data-ex="(E\d)" data-marks="([^"]+)">(.*?)\n</div>\n', html, re.S)
assert [e[0] for e in exs] == ['E1', 'E2', 'E3', 'E4'], [e[0] for e in exs]
for ex, marks, body in exs:
    pm = dict(m.split(':') for m in marks.split(','))
    assert sum(map(int, pm.values())) == 25, ex
    heads = dict(re.findall(r'<div data-part="(\w)"><h4>\(\1\) (\d+) marks</h4>', body))
    assert heads == pm, (ex, heads, pm)
    for part, n in pm.items():  # sub-part marks add up where they are given
        sub = re.search(r'<div data-part="%s">(.*?)</div>' % part, body, re.S).group(1)
        bs = [int(b) for b in re.findall(r'<b>\((\d+)\)</b>', sub)]
        assert not bs or sum(bs) == int(n), (ex, part, bs, n)
    assert '## ' + ex + ' ' in md
ex_html = ''.join(e[2] for e in exs)
for leak in ('3.75', '0.5556', '5.556', '0.1648', '0.9375', '0.6125', '1.0868', '5.2604', '0.4132', '0.7333', '8.466', '0.6066', '1.25'):
    assert leak not in ex_html, 'answer leaked into the page: ' + leak
print('final-primer keys and citations OK (%d checks keyed, %d citations); part exercises E1-E4 keys OK' % (len(KEYS), len(cites)))
