"""Independent check of every key in quiz-02-mock-tests.md (Tests A, B, C).

Run: python3 quiz-02-mock-tests-check.py   (sympy; exits non-zero on any mismatch)
Conventions follow LPH Lect 1-3: x(k+1)=Phi x+Theta u, u=-Kx, Ackermann K=[0 1]Wc^-1 alpha(Phi),
W_C=[Theta  Phi Theta], W_O=[C; C Phi].
"""
from sympy import (Matrix, Rational as R, symbols, exp, eye, zeros, simplify, integrate,
                   inverse_laplace_transform, Heaviside, factor, pi, sin, cos, N, expand, apart)

s, t, eta, z, T, beta = symbols('s t eta z T beta')
Z0, I2 = zeros(2), eye(2)


def near(a, b, tol=1e-4):
    return abs(complex(N(a)) - complex(N(b))) < tol


def phi_t(A):
    return (s * I2 - A).inv().applyfunc(
        lambda e: simplify(inverse_laplace_transform(e, s, t).subs(Heaviside(t), 1)))


def zoh(A, B, Tv):
    P = phi_t(A)
    Th = P.applyfunc(lambda e: integrate(e.subs(t, eta), (eta, 0, T))) * B
    return P, simplify(P.subs(t, Tv)), simplify(Th.subs(T, Tv))


def tf_s(A, B, C):
    return factor(simplify((C * (s * I2 - A).inv() * B)[0]))


def tf_z(P, Th, C):
    return simplify((C * (z * I2 - P).inv() * Th)[0])


def ackermann_deadbeat(P, Th):
    Wc = Th.row_join(P * Th)
    assert Wc.det() != 0
    return Matrix([[0, 1]]) * Wc.inv() * P ** 2


def step_route(Gs, a_list, Tv, zv):
    """(1 - z^-1) Z{G(s)/s} for G(s)/s with simple poles at 0 and -a: table z/(z-e^{-aT})."""
    pf = apart(Gs / s, s)
    total = 0
    for term in pf.as_ordered_terms():
        num, den = term.as_numer_denom()
        p = -[r for r in den.as_poly(s).all_roots()][0]   # den = c (s + a)
        c = num / den.as_poly(s).LC()
        total += c * zv / (zv - exp(-p * Tv))
    return (1 - 1 / zv) * total


C1 = Matrix([[1, 0]])

# ---------------- Test A ----------------
# Q1(i) series RLC, R=4, L=1, Cap=1/3, x1=vC, x2=i, y=vC
A_rlc, B_rlc = Matrix([[0, 3], [-1, -4]]), Matrix([0, 1])
# Q1(ii) block diagram: e=u-x1, x2 = 3/(s+4) e, x1 = (1/s) x2
A_bd, B_bd = Matrix([[0, 1], [-3, -4]]), Matrix([0, 3])
assert tf_s(A_rlc, B_rlc, C1) == tf_s(A_bd, B_bd, C1) == factor(3 / ((s + 1) * (s + 3)))
# Q2 two-lag cascade, ZOH T=0.5
A2, B2, C2 = Matrix([[-1, 0], [1, -2]]), Matrix([1, 0]), Matrix([[0, 1]])
Pt, P, Th = zoh(A2, B2, R(1, 2))
assert simplify(Pt - Matrix([[exp(-t), 0], [exp(-t) - exp(-2 * t), exp(-2 * t)]])) == Z0
assert near(P[0, 0], 0.60653) and near(P[1, 0], 0.23865) and near(P[1, 1], 0.36788)
assert near(Th[0], 0.39347) and near(Th[1], 0.07741)
Wc = Th.row_join(P * Th)
assert near((P * Th)[0], 0.23865) and near((P * Th)[1], 0.12238) and near(Wc.det(), 0.029683)
G = tf_z(P, Th, C2)
for zv in (2, -3, R(1, 3)):
    assert near(G.subs(z, zv), (0.077410 * zv + 0.046951) / ((zv - 0.60653) * (zv - 0.36788)))
    assert near(G.subs(z, zv), step_route(1 / ((s + 1) * (s + 2)), None, R(1, 2), zv))
assert near(G.subs(z, 1), R(1, 2))                 # ZOH keeps DC gain G(0)=1/2
# Q3 deadbeat
P3, Th3 = Matrix([[1, 1], [0, R(1, 2)]]), Matrix([R(1, 2), 1])
assert Th3.row_join(P3 * Th3) == Matrix([[R(1, 2), R(3, 2)], [1, R(1, 2)]])
assert Th3.row_join(P3 * Th3).inv() == Matrix([[R(-2, 5), R(6, 5)], [R(4, 5), R(-2, 5)]])
K3 = ackermann_deadbeat(P3, Th3)
assert K3 == Matrix([[R(4, 5), R(11, 10)]])
Acl = P3 - Th3 * K3
assert Acl == Matrix([[R(3, 5), R(9, 20)], [R(-4, 5), R(-3, 5)]]) and Acl ** 2 == Z0
x0 = Matrix([1, 1])
assert Acl * x0 == Matrix([R(21, 20), R(-7, 5)]) and Acl ** 2 * x0 == Matrix([0, 0])

# ---------------- Test B (reconstructed from the AY25/26 S1 recall) ----------------
# Q1 5y'' - 2y' = 2u
A1, B1 = Matrix([[0, 1], [0, R(2, 5)]]), Matrix([0, R(2, 5)])
assert tf_s(A1, B1, C1) == factor(2 / (s * (5 * s - 2)))
# Q2 A=[[1,beta],[0,2]], T=0.5
Pt, P, Th = zoh(Matrix([[1, beta], [0, 2]]), Matrix([0, 1]), R(1, 2))
assert simplify(Pt - Matrix([[exp(t), beta * (exp(2 * t) - exp(t))], [0, exp(2 * t)]])) == Z0
assert near(P[0, 0], 1.64872) and near(P[0, 1].subs(beta, 1), 1.06956) and near(P[1, 1], 2.71828)
assert near(Th[0].subs(beta, 1), 0.21042) and near(Th[1], 0.85914)
X = simplify((z * I2 - P).inv() * Th)
for zv in (3, -1):
    assert near(X[0].subs({z: zv, beta: 1}), (0.21042 * zv + 0.34692) / ((zv - 1.64872) * (zv - 2.71828)), 1e-3)
    assert near(X[1].subs(z, zv), 0.85914 / (zv - 2.71828))
dWc = simplify(Th.row_join(P * Th).det())
assert near(dWc.subs(beta, 1), -0.59612) and simplify(dWc.subs(beta, 0)) == 0
assert simplify(dWc / beta).free_symbols == set()     # det is (constant) * beta -> lost only at beta = 0
# Q3 x(k+1)=A x + B u
A3, B3 = Matrix([[1, R(1, 2)], [R(-1, 2), -1]]), Matrix([1, 1])
x1 = A3 * Matrix([2, 2]) + B3 * 1
x2 = A3 * x1 + B3 * (-1)
assert x1 == Matrix([4, -2]) and x2 == Matrix([2, -1])
assert expand(A3.charpoly(z).as_expr()) == z ** 2 - R(3, 4)
KB = ackermann_deadbeat(A3, B3)
assert B3.row_join(A3 * B3) == Matrix([[1, R(3, 2)], [1, R(-3, 2)]])
assert KB == Matrix([[R(1, 4), R(-1, 4)]]), KB
assert (A3 - B3 * KB) ** 2 == Z0

# ---------------- Test C ----------------
# Q1 block diagram: e=u-2y, x2 = 1/(s+1) e, x1 = y = 3/(s+2) x2
Ac1, Bc1 = Matrix([[-2, 3], [-2, -1]]), Matrix([0, 1])
assert tf_s(Ac1, Bc1, C1) == factor(3 / (s ** 2 + 3 * s + 8))
# Q2 oscillator omega=2
Pt, P, Th = zoh(Matrix([[0, 1], [-4, 0]]), Matrix([0, 1]), pi / 4)
assert simplify(Pt - Matrix([[cos(2 * t), sin(2 * t) / 2], [-2 * sin(2 * t), cos(2 * t)]])) == Z0
assert P == Matrix([[0, R(1, 2)], [-2, 0]]) and Th == Matrix([R(1, 4), R(1, 2)])
assert Th.row_join(P * Th) == Matrix([[R(1, 4), R(1, 4)], [R(1, 2), R(-1, 2)]])
assert Th.row_join(P * Th).det() == R(-1, 4) and C1.col_join(C1 * P).det() == R(1, 2)
PT = Pt.subs(t, T)
ThT = Pt.applyfunc(lambda e: integrate(e.subs(t, eta), (eta, 0, T))) * Matrix([0, 1])
assert simplify(ThT.row_join(PT * ThT).det() + sin(T) ** 3 * cos(T)) == 0
assert simplify(C1.col_join(C1 * PT).det() - sin(2 * T) / 2) == 0
# Q3 deadbeat + zero invariance
P3, Th3, C3 = Matrix([[R(1, 2), 0], [1, 1]]), Matrix([1, 1]), Matrix([[0, 1]])
KC = ackermann_deadbeat(P3, Th3)
assert Th3.row_join(P3 * Th3).inv() == Matrix([[R(4, 3), R(-1, 3)], [R(-2, 3), R(2, 3)]])
assert KC == Matrix([[R(5, 6), R(2, 3)]])
Acl = P3 - Th3 * KC
assert Acl == Matrix([[R(-1, 3), R(-2, 3)], [R(1, 6), R(1, 3)]]) and Acl ** 2 == Z0
x0 = Matrix([3, 0])
assert Acl * x0 == Matrix([-1, R(1, 2)]) and Acl ** 2 * x0 == Matrix([0, 0]) and Acl ** 3 * x0 == Matrix([0, 0])
Gol, Gcl = factor(tf_z(P3, Th3, C3)), factor(tf_z(Acl, Th3, C3))
assert simplify(Gol - (z + R(1, 2)) / ((z - R(1, 2)) * (z - 1))) == 0
assert simplify(Gcl - (z + R(1, 2)) / z ** 2) == 0, Gcl

print("all Quiz 2 mock-test keys verified (A, B, C)")
