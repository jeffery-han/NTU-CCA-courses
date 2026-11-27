"""Recompute every key in final-mock-b.md (EE6203 final Mock B).  Run: python3 final-mock-b-check.py"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose
import cmath, os, re

def close(a, b, tol=5e-4): return abs(a - b) <= tol * max(1, abs(b))
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def inv2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return [[M[1][1] / d, -M[0][1] / d], [-M[1][0] / d, M[0][0] / d]]
def charpoly2(M): return (-(M[0][0] + M[1][1]), M[0][0] * M[1][1] - M[0][1] * M[1][0])  # z^2 + c1 z + c0

# ---------------- Q1 ----------------
# (a) x(t)=2 on [0,1), e^{-(t-1)} for t>=1, T=0.5.  X(z) = 2 + 2 z^-1 + z^-1/(z - e^-0.5)
T = 0.5
xs = [2 if k * T < 1 else exp(-(k * T - 1)) for k in range(60)]
z0 = 1.7
series = sum(x * z0 ** -k for k, x in enumerate(xs))
closed = 2 + 2 / z0 + 1 / (z0 * (z0 - exp(-0.5)))
assert close(series, closed, 1e-9), (series, closed)
assert close(exp(-0.5), 0.60653)
# (b) FVT: Y1 = 0.6 z^2 / ((z-1)(z-0.4)) -> 0.6*1/(1-0.4) = 1 ; Y2 = z/((z-1)(z+1)) -> FVT not applicable
y1 = [0.0] * 200  # inverse by recursion: (z^2 - 1.4 z + 0.4) Y = 0.6 z^2  -> y(k) = 1.4 y(k-1) - 0.4 y(k-2) + 0.6 delta(k)
for k in range(200):
    y1[k] = 1.4 * (y1[k-1] if k >= 1 else 0) - 0.4 * (y1[k-2] if k >= 2 else 0) + (0.6 if k == 0 else 0)
assert close(y1[-1], 1.0, 1e-9)
y2 = [0.0] * 50   # (z^2 - 1) Y = z -> y(k) = y(k-2) + delta(k-1): 0,1,0,1,... no limit
for k in range(50):
    y2[k] = (y2[k-2] if k >= 2 else 0) + (1 if k == 1 else 0)
assert y2[-1] != y2[-2]
# (c) y(k+2) - 0.9 y(k+1) + 0.2 y(k) = x(k), x = unit step for k>=0, y(k)=0 for k<0
y = {-2: 0, -1: 0}
for k in range(-2, 60):
    y[k + 2] = F(9, 10) * y[k + 1] + (-F(1, 5) * y[k]) + (1 if k >= 0 else 0)
assert y[0] == 0 and y[1] == 0 and y[2] == 1 and y[3] == F(19, 10)
c1, c2, c3 = F(10, 3), F(-20), F(50, 3)   # y(k) = 10/3 - 20 (0.5)^k + 50/3 (0.4)^k
for k in range(12):
    assert c1 + c2 * F(1, 2) ** k + c3 * F(2, 5) ** k == y[k], k
# (d) G(s) = 1/(s(s+1)), ZOH, T = ln 2: G_ZAS = (b1 z + b0)/((z-1)(z-0.5))
Tq = log(2); b1 = Tq - 1 + exp(-Tq); b0 = 1 - exp(-Tq) - Tq * exp(-Tq)
assert close(b1, 0.19315) and close(b0, 0.15343)
# check by simulating the continuous plant under a unit ZOH step: y(kT) = kT - 1 + e^{-kT}
ystep = lambda t: t - 1 + exp(-t)
g = [0, b1]                                  # step response of G_ZAS via recursion on (z-1)(z-0.5) = z^2 - 1.5 z + 0.5
ys = [0.0, 0.0]; us = [1.0] * 40
for k in range(2, 30):
    ys.append(1.5 * ys[k-1] - 0.5 * ys[k-2] + b1 * us[k-1] + b0 * us[k-2])
ys[1] = b1  # k=1: y(1) = b1 u(0)
ys2 = [0.0, b1]
for k in range(2, 30):
    ys2.append(1.5 * ys2[k-1] - 0.5 * ys2[k-2] + b1 * 1 + b0 * 1)
for k in range(30):
    assert close(ys2[k], ystep(k * Tq), 1e-9), (k, ys2[k], ystep(k * Tq))

# ---------------- Q2 ----------------
# G_ZAS = 0.4(z+0.5)/((z-1)(z-0.6)), T = 0.1, C(z) = K
def poles_cl(K):
    a1, a0 = 0.4 * K - 1.6, 0.6 + 0.2 * K
    d = cmath.sqrt(a1 * a1 - 4 * a0)
    return [(-a1 + d) / 2, (-a1 - d) / 2]
stable = [K / 1000 for K in range(-3000, 20000) if max(abs(p) for p in poles_cl(K / 1000)) < 1]
assert close(min(stable), 0.001) and close(max(stable), 1.999), (min(stable), max(stable))
Kv = lambda K: 0.4 * K * 1.5 / (0.4 * 0.1)      # lim (z-1)/(Tz) G
assert close(Kv(1), 15) and close(1 / Kv(1), 1 / 15)
# (b)(i) minimal-prototype deadbeat Gcl = z^-1 -> C = (z-0.6)/(0.4(z+0.5)); U(z) = (z-0.6)/(0.4(z+0.5)) * ... ripples
# simulate loop: plant difference eq y(k) = 1.6y(k-1) - 0.6y(k-2) + 0.4u(k-1) + 0.2u(k-2)
def sim(ctrl_num, ctrl_den, n=12):
    # controller u(k) = (sum num_i e(k-i) - sum_{i>=1} den_i u(k-i)) / den_0 ; num/den in powers of z^-1
    y = [0.0] * n; u = [0.0] * n; e = [0.0] * n
    for k in range(n):
        y[k] = (1.6 * y[k-1] if k >= 1 else 0) - (0.6 * y[k-2] if k >= 2 else 0) + (0.4 * u[k-1] if k >= 1 else 0) + (0.2 * u[k-2] if k >= 2 else 0)
        e[k] = 1 - y[k]
        u[k] = (sum(ctrl_num[i] * e[k-i] for i in range(len(ctrl_num)) if k - i >= 0) - sum(ctrl_den[i] * u[k-i] for i in range(1, len(ctrl_den)) if k - i >= 0)) / ctrl_den[0]
    return y, u
y, u = sim([1 / 0.4, -0.6 / 0.4], [1, 0.5])          # C = (1 - 0.6 z^-1) / (0.4 (1 + 0.5 z^-1))
assert all(close(v, 1, 1e-9) for v in y[1:]), y
assert close(u[0], 2.5) and all(close(u[k], -2.75 * (-0.5) ** (k - 1), 1e-9) for k in range(1, 12))  # U = 2.5(z-0.6)/(z+0.5): alternates, decays, never exactly settles
# (b)(ii) ripple-free: Gcl = (2/3)(z+0.5)/z^2, C = (5/3)(z-0.6)/(z+1/3)
y, u = sim([5 / 3, -1.0], [1, 1 / 3])
assert close(y[1], 2 / 3, 1e-9) and all(close(v, 1, 1e-9) for v in y[2:]), y
assert close(u[0], 5 / 3) and close(u[1], -1) and all(close(v, 0, 1e-9) for v in u[2:]), u
# (c) pole-zero matching of D(s) = 5(s+1)/(s+5), T = 0.2
zq, pq = exp(-0.2), exp(-1.0)
alpha = 1 * (1 - pq) / (1 - zq)       # D(0) = 1
assert close(zq, 0.81873) and close(pq, 0.36788) and close(alpha, 3.4871)
# standard programming: m(k) = e(k) + p m(k-1); u(k) = alpha (m(k) - zq m(k-1)); one delay

# ---------------- Q3 ----------------
# y'' + 4y' + 3y = u: x1 = y, x2 = y', A = [[0,1],[-3,-4]], B = [0,1], C = [1,0], T = ln 2
Phi = [[F(11, 16), F(3, 16)], [F(-9, 16), F(-1, 16)]]
Theta = [[F(5, 48)], [F(3, 16)]]
# e^{At} = [[1.5e^-t - 0.5e^-3t, 0.5e^-t - 0.5e^-3t], [-1.5e^-t + 1.5e^-3t, -0.5e^-t + 1.5e^-3t]] at e^-T = 1/2
h = F(1, 2)
assert Phi == [[F(3, 2) * h - h ** 3 / 2, h / 2 - h ** 3 / 2], [-F(3, 2) * h + F(3, 2) * h ** 3, -h / 2 + F(3, 2) * h ** 3]]
# Theta = int_0^T [0.5e^-s - 0.5e^-3s ; -0.5e^-s + 1.5e^-3s] ds
assert Theta == [[(1 - h) / 2 - (1 - h ** 3) / 6], [-(1 - h) / 2 + (1 - h ** 3) / 2]]
# numeric check by series expansion of e^{AT}
A = [[0.0, 1.0], [-3.0, -4.0]]
def expm(M, t, terms=40):
    R = [[1.0, 0.0], [0.0, 1.0]]; P = [[1.0, 0.0], [0.0, 1.0]]
    for n in range(1, terms):
        P = [[sum(P[i][k] * M[k][j] for k in range(2)) * t / n for j in range(2)] for i in range(2)]
        R = [[R[i][j] + P[i][j] for j in range(2)] for i in range(2)]
    return R
E = expm(A, log(2))
assert all(close(E[i][j], float(Phi[i][j]), 1e-9) for i in range(2) for j in range(2))
# Theta = int_0^T e^{A s} ds B  (trapezoid on fine grid)
N = 4000; th = [0.0, 0.0]
for i in range(N + 1):
    s = log(2) * i / N; w = 0.5 if i in (0, N) else 1.0; Es = expm(A, s, 25)
    th[0] += w * Es[0][1] * log(2) / N; th[1] += w * Es[1][1] * log(2) / N
assert close(th[0], 5 / 48, 1e-6) and close(th[1], 3 / 16, 1e-6), th
# (b) G(z) = C (zI-Phi)^-1 Theta = (5/48)(z + 0.4) / ((z-0.5)(z-0.125))
for zz in (F(2), F(3, 2), F(-3)):
    M = [[zz - Phi[0][0], -Phi[0][1]], [-Phi[1][0], zz - Phi[1][1]]]
    Gz = mm([[1, 0]], mm(inv2(M), Theta))[0][0]
    assert Gz == F(5, 48) * (zz + F(2, 5)) / ((zz - F(1, 2)) * (zz - F(1, 8)))
# DC-gain cross-check: G(1) must equal the continuous DC gain 1/3
assert F(5, 48) * F(7, 5) / (F(1, 2) * F(7, 8)) == F(1, 3)
# (c) W_C, W_O
PT = mm(Phi, Theta)
assert PT == [[F(41, 384)], [F(-9, 128)]]
detWc = Theta[0][0] * PT[1][0] - PT[0][0] * Theta[1][0]
assert detWc == F(-7, 256)
CPhi = mm([[1, 0]], Phi)[0]
assert CPhi == [F(11, 16), F(3, 16)] and 1 * CPhi[1] - 0 * CPhi[0] == F(3, 16)
# (d) drive x(0) = [1,0] to x(2) = 0
P2 = mm(Phi, Phi)
assert P2 == [[F(47, 128), F(15, 128)], [F(-45, 128), F(-13, 128)]]
rhs = [-P2[0][0], -P2[1][0]]
M = [[PT[0][0], Theta[0][0]], [PT[1][0], Theta[1][0]]]
u0, u1 = [sum(inv2(M)[i][j] * rhs[j] for j in range(2)) for i in range(2)]
assert (u0, u1) == (F(-27, 7), F(3, 7))
x = [[F(1)], [F(0)]]
for uk in (u0, u1):
    x = [[mm(Phi, x)[i][0] + Theta[i][0] * uk] for i in range(2)]
assert x == [[0], [0]]

# ---------------- Q4 ----------------
A = [[F(1), F(1)], [F(0), F(1, 2)]]; B = [[F(0)], [F(1)]]; C = [[F(1), F(0)]]
A2 = mm(A, A)
assert A2 == [[1, F(3, 2)], [0, F(1, 4)]]
# (a) Ackermann K for alpha_c = z^2 - z + 0.34
ac = [[A2[i][j] - A[i][j] + (F(34, 100) if i == j else 0) for j in range(2)] for i in range(2)]
Wc = [[B[0][0], mm(A, B)[0][0]], [B[1][0], mm(A, B)[1][0]]]
K = mm(mm([[0, 1]], inv2(Wc)), ac)[0]
assert K == [F(34, 100), F(1, 2)]
ABK = [[A[i][j] - B[i][0] * K[j] for j in range(2)] for i in range(2)]
assert charpoly2(ABK) == (-1, F(34, 100))
# (b)(i) prediction observer, deadbeat (alpha_o = z^2)
Wo = [C[0], mm(C, A)[0]]
LO = mm(A2, mm(inv2(Wo), [[0], [1]]))
assert LO == [[F(3, 2)], [F(1, 4)]]
ALC = [[A[i][j] - LO[i][0] * C[0][j] for j in range(2)] for i in range(2)]
assert charpoly2(ALC) == (0, 0)
assert mm(ALC, ALC) == [[0, 0], [0, 0]]       # e(2) = 0 for any e(0)
# (b)(ii) current observer, deadbeat: L_C = alpha(A) [CA; CA^2]^-1 [0;1]
CA, CA2 = mm(C, A)[0], mm(C, A2)[0]
LC = mm(A2, mm(inv2([CA, CA2]), [[0], [1]]))
assert LC == [[1], [F(1, 2)]]
LCCA = [[LC[i][0] * CA[j] for j in range(2)] for i in range(2)]
Ecur = [[A[i][j] - LCCA[i][j] for j in range(2)] for i in range(2)]
assert charpoly2(Ecur) == (0, 0)
# (c) separation and k_r
I_ABK = [[(1 if i == j else 0) - ABK[i][j] for j in range(2)] for i in range(2)]
dc = mm(C, mm(inv2(I_ABK), B))[0][0]
assert dc == 1 / F(34, 100) and 1 / dc == F(34, 100)
# (d) LQR: x(k+1) = x + 2u, J = sum(x^2 + u^2)  ->  Q = R = 2 (J = 1/2 sum(Q x^2 + R u^2))
a, b, Q, R = F(1), F(2), F(2), F(2)
def step(S):
    Kk = b * S * a / (b * b * S + R)
    return Kk, (a - b * Kk) ** 2 * S + Kk * Kk * R + Q
K1, S1 = step(F(0))
K0, S0 = step(S1)
assert (K1, S1, K0, S0) == (0, 2, F(2, 5), F(12, 5))
x0 = 2
assert F(1, 2) * S0 * x0 ** 2 == F(24, 5)
# brute force over u0 for N = 2 horizon: J = x0^2 + u0^2 + (x0 + 2u0)^2
best = min(((x0 ** 2 + u ** 2 + (x0 + 2 * u) ** 2), u) for u in [i / 1000 for i in range(-3000, 3000)])
assert close(best[0], 4.8, 1e-6) and close(best[1], -0.8, 1e-6)
S = 0.0
for _ in range(200):
    Kk = 2 * S / (4 * S + 2); S = (1 - 2 * Kk) ** 2 * S + 2 * Kk * Kk + 2
assert close(S, 1 + sqrt(2), 1e-12) and close(Kk, sqrt(2) - 1, 1e-12)
assert close(1 - 2 * Kk, 3 - 2 * sqrt(2), 1e-12)
assert close(0.5 * S * 4, 2 + 2 * sqrt(2), 1e-12)
assert close(-Kk * 2, -0.82843) and close(2 * (1 - 2 * Kk), 0.34315)

# ---------------- page integrity ----------------
here = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(here, 'final-mock-b.html'), encoding='utf-8').read()
items = re.findall(r'data-item="([^"]+)"', html)
assert len(items) == len(set(items)), items
marks = sum(int(m) for m in re.findall(r'<h3>\([a-z]+\)[^<]*<span class="marks">(\d+)</span>', html))
assert marks == 100, marks
md = open(os.path.join(here, 'final-mock-b.md'), encoding='utf-8').read()
assert 'Total: 100' in md
print('final-mock-b keys OK')
