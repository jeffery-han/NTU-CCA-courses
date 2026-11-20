"""Re-derives every numeric/symbolic key in quiz-02-mock-01.md. Run: python3 quiz-02-mock-01-check.py"""
from fractions import Fraction as F
import sympy as sp

# A2: ultrasonic, round-trip TOF 30 ms, c = 340 m/s -> d = c t / 2 (Lec 1 p38)
assert F(340) * F(30, 1000) / 2 == F(51, 10)

# A4: pinhole, f*sx = f*sy = 500, alpha = 0, (u0, v0) = (320, 240) (Lec 2 p30)
A = sp.Matrix([[500, 0, 320], [0, 500, 240], [0, 0, 1]])
mbar = sp.Matrix([sp.Rational(2, 10), sp.Rational(-1, 10), 2])
m = mbar / mbar[2]
assert list(A * m) == [370, 215, 1]
# A5 / depth ambiguity: A^{-1} p returns normalised m, not mbar; scaling mbar leaves p unchanged
assert A.inv() * (A * m) == m and (A * ((3 * mbar) / (3 * mbar)[2])) == A * m

# A7: any E = [x]x R has singular values (s, s, 0) (Lec 3 p17)
def skew(v):
    return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
th = sp.pi / 3
R = sp.Matrix([[sp.cos(th), 0, sp.sin(th)], [0, 1, 0], [-sp.sin(th), 0, sp.cos(th)]])
E = skew([1, 2, 2]) * R
ev = (E.T * E).eigenvals()  # squared singular values -> multiplicity
assert {sp.nsimplify(k): v for k, v in ev.items()} == {0: 1, 9: 2}, ev

# A9: V(X - Y) = V(X) + V(Y) for uncorrelated X, Y (Lec 4 p15 with Y -> -Y)
vx, vy = sp.symbols("vx vy", positive=True)
assert sp.simplify(vx + (-1) ** 2 * vy - (vx + vy)) == 0

# A10: scalar gain K = A H P / (H^2 P + R) -> 0 as R -> oo (Lec 4 p31)
P, Rn = sp.symbols("P R", positive=True)
assert sp.limit(1 * 1 * P / (P + Rn), Rn, sp.oo) == 0

# B(a)-(b): batch two-sensor fusion, minimise P+ = (1-K1-K2)^2 P + K1^2 s1 + K2^2 s2 (Lec 4 p36-40)
K1, K2, s1, s2 = sp.symbols("K1 K2 s1 s2", positive=True)
Pn = (1 - K1 - K2) ** 2 * P + K1 ** 2 * s1 + K2 ** 2 * s2
sol = sp.solve([sp.diff(Pn, K1), sp.diff(Pn, K2)], [K1, K2], dict=True)[0]
den = s1 * s2 + P * (s1 + s2)
assert sp.simplify(sol[K1] - P * s2 / den) == 0 and sp.simplify(sol[K2] - P * s1 / den) == 0
Pmin = sp.simplify(Pn.subs(sol))
assert sp.simplify(Pmin - P * s1 * s2 / den) == 0
# no prior information (P -> oo): weights tend to s2/(s1+s2), s1/(s1+s2); variance to s1 s2/(s1+s2)
assert sp.limit(sol[K1], P, sp.oo) == s2 / (s1 + s2) and sp.limit(Pmin, P, sp.oo) == s1 * s2 / (s1 + s2)

# B(c): sequential, x0 = z1 = 10, P0 = s1 = 1, then z2 = 15 with s2 = 4 (Lec 4 p41-42)
s1v, s2v, z1, z2 = F(1), F(4), F(10), F(15)
K = s1v / (s1v + s2v)
xhat = z1 + K * (z2 - z1)
Pf = (1 - K) * s1v
assert K == F(1, 5) and xhat == 11 and Pf == F(4, 5)
assert xhat == s2v / (s1v + s2v) * z1 + s1v / (s1v + s2v) * z2  # weighted-average form (12)
assert Pf < s1v and Pf < s2v
# B(d): a third sensor with variance 4 fused after -> P = 1/(1/1 + 1/4 + 1/4) = 2/3
assert 1 / (1 / s1v + 1 / s2v + 1 / s2v) == F(2, 3)

print("all quiz-02-mock-01 keys verified")
