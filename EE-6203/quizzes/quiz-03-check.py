"""Recompute every numeric key in quiz-03-mock-a.md and quiz-03-primer.html.

Run: python3 quiz-03-check.py   (needs sympy). Exits non-zero on any mismatch.
"""
import math
import sympy as sp

z, s, K = sp.symbols('z s K')


def close(a, b, tol=1e-3):
    a, b = float(a), float(b)
    assert abs(a - b) <= tol * max(1, abs(b)), (a, b)


def zoh_type1(a, gain, T):
    """G(s)=gain/(s(s+a)) with ZOH -> b1, b0, pole q (G = (b1 z + b0)/((z-1)(z-q)))."""
    q = math.exp(-a * T)
    b1 = gain * (a * T - 1 + q) / a**2
    b0 = gain * (1 - q - a * T * q) / a**2
    return b1, b0, q


# ---------------- Mock A ----------------
# Q1(b) Jury: P(z) = z^2 - (1.6 - 0.4K) z + (0.6 + 0.2K)
P = z**2 - (sp.Rational(8, 5) - sp.Rational(2, 5) * K) * z + (sp.Rational(3, 5) + sp.Rational(1, 5) * K)
c1 = sp.solve_univariate_inequality(sp.Abs(sp.Rational(3, 5) + K / 5) < 1, K, relational=False)
c2 = sp.solve_univariate_inequality(P.subs(z, 1) > 0, K, relational=False)
c3 = sp.solve_univariate_inequality(P.subs(z, -1) > 0, K, relational=False)
rng = c1.intersect(c2).intersect(c3)
assert rng == sp.Interval.open(0, 2), rng
assert sp.expand(P.subs(z, 1)) == sp.Rational(3, 5) * K
P2 = sp.expand(P.subs(K, 2))  # z^2 - 0.8 z + 1
roots = sp.Poly(P2, z).nroots()
assert all(abs(abs(complex(r)) - 1) < 1e-12 for r in roots)
theta = math.acos(0.4)
close(theta, 1.1593)
close(theta / 0.2, 5.796)

# Q2: C(s) = 5(s+2)/(s+10), T = 0.1
T = sp.Rational(1, 10)
Cs = 5 * (s + 2) / (s + 10)
Cz = sp.simplify(Cs.subs(s, 2 / T * (z - 1) / (z + 1)))
assert sp.simplify(Cz - (11 * z - 9) / (3 * z - 1)) == 0
assert Cz.subs(z, 1) == Cs.subs(s, 0) == 1
zero_pz, pole_pz = math.exp(-0.2), math.exp(-1.0)
alpha = (1 - pole_pz) / (1 - zero_pz)
close(zero_pz, 0.8187); close(pole_pz, 0.3679); close(alpha, 3.4868)
# high-frequency gains (z = -1) differ: bilinear 5 (= C(s->inf)), pole-zero matched alpha*(1+0.8187)/(1+0.3679)
close(((11 * -1 - 9) / (3 * -1 - 1)), 5.0)
close(alpha * (1 + zero_pz) / (1 + pole_pz), 4.636)
# standard programming: C = (11/3 - 3 z^-1)/(1 - (1/3) z^-1)
w = sp.symbols('w')  # w = z^-1
Cw = sp.simplify(Cz.subs(z, 1 / w))
assert sp.simplify(Cw - (sp.Rational(11, 3) - 3 * w) / (1 - w / 3)) == 0

# Q3: G(s) = 3/(s(s+3)), T = 0.2, ZOH
b1, b0, q = zoh_type1(3, 3, 0.2)
close(b1, 0.049604); close(b0, 0.040634); close(q, 0.548812)
zr = -b0 / b1
close(zr, -0.819166)
Kc = 1 / (1 - zr)
close(Kc, 0.549703)
Gz = b1 * (z - zr) / ((z - 1) * (z - q))
Gcl = Kc * (z - zr) / z**2
C = sp.simplify(Gcl / (Gz * (1 - Gcl)))
Cn, Cd = sp.fraction(sp.factor(sp.nsimplify(C, rational=False)))
# expected C(z) = (Kc/b1)(z - q)/(z + 0.450297)
Cexp = (Kc / b1) * (z - q) / (z + Kc * (-zr))
assert abs(complex(sp.N((C - Cexp).subs(z, 2.3)))) < 1e-9
close(Kc / b1, 11.0818); close(Kc * (-zr), 0.450297)
# sequences
x = sp.symbols('x')  # x = z^-1
R = 1 / (1 - x)
Yx = sp.series((Gcl * z / (z - 1)).subs(z, 1 / x), x, 0, 6).removeO()
Ux = sp.series((Gcl / Gz * z / (z - 1)).subs(z, 1 / x), x, 0, 6).removeO()
yk = [float(Yx.coeff(x, k)) for k in range(6)]
uk = [float(Ux.coeff(x, k)) for k in range(6)]
for got, exp in zip(yk, [0, 0.549703, 1, 1, 1, 1]):
    close(got, exp)
for got, exp in zip(uk, [11.0818, -6.0818, 0, 0, 0, 0]):
    assert abs(got - exp) < 1e-3, (uk)
# plain deadbeat comparison: C0 = (1/b1)(z-q)/(z - zr), u alternates with ratio zr
U0 = sp.series(((1 / z) / Gz * z / (z - 1)).subs(z, 1 / x), x, 0, 4).removeO()
u0 = [float(U0.coeff(x, k)) for k in range(4)]
close(u0[0], 20.160); close(u0[1], -27.578); close(u0[2] / u0[1], zr)
close(1 / b1, 20.160)

# ---------------- Mock B (recalled 3-question shape) ----------------
# Q1: G(z) = K(0.4261z + 0.3608)/((z-1)(z-0.6065)), from K/(s(s+0.5)), T = 1, ZOH
b1, b0, q = zoh_type1(0.5, 1, 1.0)
close(b1, 0.42612); close(b0, 0.36082); close(q, 0.60653)
PB = sp.expand((z - 1) * (z - q) + K * (b1 * z + b0))
close((1 - q) / b0, 1.0905)                         # |a2| < 1  -> K < 1.0905
close(sp.Poly(PB.subs(z, 1), K).all_coeffs()[0], 0.78694)  # P(1) = 0.7869K
close(sp.solve(PB.subs(z, -1), K)[0], 49.20)        # P(-1) > 0 -> K < 49.2
close((b1 + b0) / (1 - q), 2.0)                     # Kv = 2K
# Q2: G(s) = 4/(s^2+2s+4), T = 0.5
GB = sp.simplify((4 / (s**2 + 2 * s + 4)).subs(s, 4 * (z - 1) / (z + 1)))
assert sp.simplify(GB - (z + 1)**2 / (7 * z**2 - 6 * z + 3)) == 0
close(math.sqrt(3 / 7), 0.6547)
cB = 2 * math.exp(-0.5) * math.cos(math.sqrt(3) * 0.5); dB = math.exp(-1)
close(cB, 0.7859); close(dB, 0.3679); close((1 - cB + dB) / 2, 0.2910)
# Q3(a): G1 = 0.2(z+0.6)/((z-0.8)(z-0.4)), Gcl = z^-1
G1 = sp.Rational(1, 5) * (z + sp.Rational(3, 5)) / ((z - sp.Rational(4, 5)) * (z - sp.Rational(2, 5)))
C1 = sp.simplify((1 / z) / (G1 * (1 - 1 / z)))
assert sp.simplify(C1 - 5 * (z - sp.Rational(4, 5)) * (z - sp.Rational(2, 5)) / ((z - 1) * (z + sp.Rational(3, 5)))) == 0
# Q3(b): G2 = 0.1(z+1.5)/((z-1)(z-0.5)); z^-1 gives C pole at -1.5; fix Gcl = 0.4 z^-1 (1+1.5 z^-1)
G2 = sp.Rational(1, 10) * (z + sp.Rational(3, 2)) / ((z - 1) * (z - sp.Rational(1, 2)))
Cbad = sp.simplify((1 / z) / (G2 * (1 - 1 / z)))
assert sp.simplify(Cbad - 10 * (z - sp.Rational(1, 2)) / (z + sp.Rational(3, 2))) == 0
Gcl2 = sp.Rational(2, 5) * (z + sp.Rational(3, 2)) / z**2
C2 = sp.simplify(Gcl2 / (G2 * (1 - Gcl2)))
assert sp.simplify(C2 - 4 * (z - sp.Rational(1, 2)) / (z + sp.Rational(3, 5))) == 0
Y2 = sp.series((Gcl2 * z / (z - 1)).subs(z, 1 / x), x, 0, 5).removeO()
U2 = sp.series((Gcl2 / G2 * z / (z - 1)).subs(z, 1 / x), x, 0, 5).removeO()
assert [Y2.coeff(x, k) for k in range(4)] == [0, sp.Rational(2, 5), 1, 1]
assert [U2.coeff(x, k) for k in range(4)] == [4, -2, 0, 0]

# ---------------- Primer checks ----------------
# P1 Jury: z^2 + (K - 1.3) z + 0.4 -> -0.1 < K < 2.7
Pp = z**2 + (K - sp.Rational(13, 10)) * z + sp.Rational(2, 5)
assert sp.solve(Pp.subs(z, -1), K)[0] == sp.Rational(27, 10)
assert sp.solve(Pp.subs(z, 1), K)[0] == -sp.Rational(1, 10)
# P1 Kv: GH = 0.1(z+0.9)/((z-1)(z-0.6)), T = 0.1
Kv = sp.limit((1 - 1 / z) * sp.Rational(1, 10) * (z + sp.Rational(9, 10)) / ((z - 1) * (z - sp.Rational(3, 5))) / sp.Rational(1, 10), z, 1)
close(Kv, 4.75)
# P1 start-here: Ex 4.8 boundaries, Kv at K=1 and K=2 (T=1), simulated ramp error
P48 = z**2 + (sp.Float(0.3679) * K - sp.Float(1.3679)) * z + (sp.Float(0.3679) + sp.Float(0.2642) * K)
close(sp.expand(P48.subs(z, 1)).coeff(K), 0.6321); close(sp.expand(P48.subs(z, -1)).subs(K, 0), 2.7358)
close((1 - 0.3679) / 0.2642, 2.3925); close(2.7358 / 0.1037, 26.382)
rts = sp.Poly(P48.subs(K, 2.3925), z).nroots(); assert all(abs(abs(complex(r)) - 1) < 1e-4 for r in rts)
assert all(abs(complex(r)) > 1.07 for r in sp.Poly(P48.subs(K, 3), z).nroots())
for Kk, ess in ((1, 1.0), (2, 0.5)):
    Kv = sp.limit((1 - 1 / z) * Kk * (sp.Float(0.3679) * z + sp.Float(0.2642)) / ((z - sp.Float(0.3679)) * (z - 1)), z, 1)
    close(1 / Kv, ess)
    y = [0.0] * 400; r = list(range(400))
    for k in range(400):
        y[k] = (-(0.3679 * Kk - 1.3679) * (y[k-1] if k > 0 else 0) - (0.3679 + 0.2642 * Kk) * (y[k-2] if k > 1 else 0)
                + Kk * (0.3679 * (r[k-1] if k > 0 else 0) + 0.2642 * (r[k-2] if k > 1 else 0)))
    close(r[-1] - y[-1], ess)
close(math.sqrt(0.3679 + 0.2642 * 2), 0.947)
# P1 start-here pole picture: 0.6+0.6j -> 45 deg -> 8 samples/turn, |p|=0.849
import cmath
close(360 / math.degrees(cmath.phase(0.6 + 0.6j)), 8); close(abs(0.6 + 0.6j), 0.849)
close(sum(0.5**k * 2.0**-k for k in range(200)), 2 / (2 - 0.5))   # Z{p^k} = z/(z-p) at z=2
# P2 bilinear 2/(s+2), T=0.5 -> (z+1)/(3z-1); pole-zero matched alpha = 1 - e^-1
Cb = sp.simplify((2 / (s + 2)).subs(s, 4 * (z - 1) / (z + 1)))
assert sp.simplify(Cb - (z + 1) / (3 * z - 1)) == 0
close(1 - math.exp(-1), 0.6321)
# P3 lead alpha for 30 deg
a30 = (1 - math.sin(math.radians(30))) / (1 + math.sin(math.radians(30)))
close(a30, 1 / 3); close(10 * math.log10(a30), -4.771)
# P4 relative degree of 0.05 z^-2 (1+0.7 z^-1)/((1-0.9z^-1)(1-0.5z^-1)) = 2
Gp = sp.simplify((sp.Rational(1, 20) * x**2 * (1 + sp.Rational(7, 10) * x) / ((1 - sp.Rational(9, 10) * x) * (1 - x / 2))).subs(x, 1 / z))
n_, d_ = sp.fraction(sp.factor(Gp))
assert sp.degree(d_, z) - sp.degree(n_, z) == 2
# P5 ripple-free K with plant zero at -0.6
close(1 / 1.6, 0.625)
# P6 gamma = phi(1)/Bb(1)
close((1 - 1.2 + 0.45) / (1 + 1.5), 0.1)
# P4 start-here: deadbeat for G = 0.5/(z-0.5) -> C = 2(z-0.5)/(z-1), Gcl = 1/z, step y = 0,1,1,...
G0 = sp.Rational(1, 2) / (z - sp.Rational(1, 2))
C0 = sp.simplify((1 / G0) * (1 / z) / (1 - 1 / z))
assert sp.simplify(C0 - 2 * (z - sp.Rational(1, 2)) / (z - 1)) == 0
assert sp.simplify(C0 * G0 / (1 + C0 * G0) - 1 / z) == 0
# P4 start-here check: relative degree of 0.2/(z^2-0.3z) = 2
n_, d_ = sp.fraction(sp.factor(sp.Rational(1, 5) / (z**2 - sp.Rational(3, 10) * z)))
assert sp.degree(d_, z) - sp.degree(n_, z) == 2
# P4 reldeg walkthrough: impulse of 0.05z^-2(1+0.7z^-1)/((1-0.9z^-1)(1-0.5z^-1)) -> 0, 0, 0.05
assert sp.expand((1 - sp.Rational(9, 10) * x) * (1 - x / 2)) == 1 - sp.Rational(7, 5) * x + sp.Rational(9, 20) * x**2
yk, u = [], [1, 0, 0, 0]
for k in range(4):
    g = lambda a, i: a[i] if i >= 0 else 0
    yk.append(1.4 * g(yk, k - 1) - 0.45 * g(yk, k - 2) + 0.05 * g(u, k - 2) + 0.035 * g(u, k - 3))
close(yk[0], 0); close(yk[1], 0); close(yk[2], 0.05)
# P4c: (0.2z^-2 + 0.1z^-4)/(1-0.5z^-1) -> relative degree 2
n_, d_ = sp.fraction(sp.factor(sp.simplify(((x**2 / 5 + x**4 / 10) / (1 - x / 2)).subs(x, 1 / z))))
assert sp.degree(d_, z) - sp.degree(n_, z) == 2
# P5 start-here: u sequences via U = Gcl R / G (x = z^-1)
def useq(Gcl, G, n=5):
    c = [float(v) for v in sp.Poly(sp.series(sp.simplify(Gcl / (1 - x) / G), x, 0, n).removeO(), x).all_coeffs()[::-1]]
    return c + [0.0] * (n - len(c))
F = sp.Float
G8 = F(1.8604e-4) * (1 + F(0.9293) * x) * x / ((1 - F(0.8187) * x) * (1 - F(0.9802) * x))
u8 = useq(x, G8); close(u8[0], 5375.2); close(u8[1], -9289.4); close(u8[2], 8651.9)
G10 = F(0.0048374) * (1 + F(0.9672) * x) * x / ((1 - x) * (1 - F(0.9048) * x))
K10 = 1 / F(1.9672); close(K10, 0.5083)
u10 = useq(K10 * x * (1 + F(0.9672) * x), G10); close(u10[0], 105.08); close(u10[1], -95.08); close(u10[2], 0)
G12 = F(0.0035501) * (1 + F(0.6945) * x) * x / ((1 - F(0.9048) * x) * (1 - F(0.3679) * x))
K12 = 1 / F(1.6945); close(K12, 0.5901)
u12 = useq(K12 * x * (1 + F(0.6945) * x), G12); close(u12[0], 166.23); close(u12[1], -45.33); close(u12[2], 10.0); close(u12[4], 10.0)
Gc = sp.Rational(1, 10) * x * (1 + x / 2) / ((1 - x) * (1 - sp.Rational(3, 5) * x))
uc = useq(sp.Rational(2, 3) * x * (1 + x / 2), Gc); close(uc[0], 20 / 3); close(uc[1], -4); close(uc[2], 0)
# P6 start-here: pole placement, G = z^-1 (1+2x)/((1-x/2)(1-2x)), Ag=1-x/2, Ab=1-2x, Bb=1+2x
def pp(phi):
    r1, s0 = sp.symbols('r1 s0')
    sol = sp.solve(sp.Poly(sp.expand((1 - 2 * x) * (1 + r1 * x) + x * (1 + 2 * x) * s0 - phi), x).all_coeffs(), [r1, s0])
    return sol[r1], sol[s0], phi.subs(x, 1) / 3
r1_, s0_, g_ = pp(1 - x + sp.Rational(6, 25) * x**2); close(r1_, 0.44); close(s0_, 0.56); close(g_, 0.08)
A_, B_, Rc_, Sc_ = (1 - x / 2) * (1 - 2 * x), 1 + 2 * x, 1 + r1_ * x, (1 - x / 2) * s0_
assert sp.expand(Rc_ * A_ + x * B_ * Sc_ - (1 - x / 2) * (1 - x + sp.Rational(6, 25) * x**2)) == 0
GY_ = g_ * x * B_ / (1 - x + sp.Rational(6, 25) * x**2); close(GY_.subs(x, 1), 1)
ys = [float(c) for c in sp.Poly(sp.series(GY_ / (1 - x), x, 0, 4).removeO(), x).all_coeffs()[::-1]]
close(ys[1], 0.08); close(ys[2], 0.32); close(ys[3], 0.5408)
close(sp.limit(g_ * (1 - x / 2) / Rc_ - Sc_ / Rc_ * GY_, x, 1), -1 / 6)
r1_, s0_, g_ = pp((1 - x / 2)**2); close(s0_, 0.5625); close(r1_, 0.4375); close(g_, 1 / 12)
print('all Quiz 3 keys verified')

# ---------------- Mock B step-by-step page checks ----------------
close((1 - 0.5) / b0, 1.386)                                  # b-1a-upper: pole moved to 0.5
close(1 / (2 * 0.25), 2)                                      # b-1b-ess
assert sp.simplify((3 / (s + 3)).subs(s, 4 * (z - 1) / (z + 1)) - 3 * (z + 1) / (7 * z - 1)) == 0  # b-2a-bil -> 1/7
close(1 - math.exp(-2), 0.8647)                               # b-2b-alpha
Cd = sp.simplify(((2 - sp.Rational(6, 5) * x) / (1 - x / 2)).subs(x, 1 / z))
assert sp.Poly(sp.fraction(sp.factor(Cd))[1], z).all_coeffs()[-1] / sp.Poly(sp.fraction(sp.factor(Cd))[1], z).all_coeffs()[0] == -sp.Rational(1, 2)  # b-2c-coef: -a1 = 0.5
assert sp.simplify(((sp.Rational(1, 7) * (1 + 2 * x + x**2)) / (1 - sp.Rational(6, 7) * x + sp.Rational(3, 7) * x**2)).subs(x, 1)) == 1  # 2c DC check
n_, d_ = sp.fraction(sp.factor(sp.Rational(3, 10) / (z * (z - sp.Rational(1, 2)))))
assert sp.degree(d_, z) - sp.degree(n_, z) == 2               # b-3a-reldeg
assert sp.Rational(1, 3) * (1 + 2) == 1                       # b-3b-K
assert sp.factor(1 - Gcl2) == sp.factor((z - 1) * (z + sp.Rational(3, 5)) / z**2)
close(math.sqrt(0.6065 + 0.3608 * 0.5), 0.887)                # 1a sanity sample K=0.5
assert (0.4261 * 0.5 - 1.6065)**2 - 4 * (0.6065 + 0.3608 * 0.5) < 0
print('Mock B step page keys verified')
