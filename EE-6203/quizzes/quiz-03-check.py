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
print('all Quiz 3 keys verified')
