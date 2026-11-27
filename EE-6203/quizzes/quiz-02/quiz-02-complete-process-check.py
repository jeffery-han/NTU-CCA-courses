"""Check every number in quiz-02-complete-process-explainer.html.

Run: python3 quiz-02-complete-process-check.py   (sympy; exits non-zero on any mismatch)
Plant: Test A Q2, A=[-1 0;1 -2], B=[1;0], C=[0 1], T=0.5, carried on to deadbeat K (LPH Lect 1-3).
"""
from sympy import Matrix, Rational, symbols, eye, exp, integrate, inverse_laplace_transform, Heaviside, simplify, factor, N

s, t, eta, z = symbols('s t eta z')
A, B, C, T = Matrix([[-1, 0], [1, -2]]), Matrix([1, 0]), Matrix([[0, 1]]), Rational(1, 2)


def near(a, b, tol=6e-4):
    assert abs(float(N(a)) - b) < tol, (N(a), b)


assert factor((C * (s * eye(2) - A).inv() * B)[0]) == 1 / ((s + 1) * (s + 2))
Pt = (s * eye(2) - A).inv().applyfunc(lambda e: inverse_laplace_transform(e, s, t).subs(Heaviside(t), 1))
assert simplify(Pt - Matrix([[exp(-t), 0], [exp(-t) - exp(-2 * t), exp(-2 * t)]])) == Matrix.zeros(2)
Ph = Pt.subs(t, T)
Th = Pt.applyfunc(lambda e: integrate(e.subs(t, eta), (eta, 0, T))) * B
assert simplify(Th[1] - (1 - exp(-T)) ** 2 / 2) == 0
for got, want in zip(list(Ph) + list(Th), [0.6065, 0, 0.2387, 0.3679, 0.3935, 0.0774]):
    near(got, want)

Wc = Matrix.hstack(Th, Ph * Th)
near(Wc.det(), 0.0297)
near(Matrix.vstack(C, C * Ph).det(), -0.2387)
near(Matrix.vstack(Matrix([[1, 0]]), Matrix([[1, 0]]) * Ph).det(), 0, 1e-12)

G = (C * (z * eye(2) - Ph).inv() * Th)[0]
near(G.subs(z, 1), 0.5, 1e-9)
near(-(Ph[1, 0] * Th[0] - Ph[0, 0] * Th[1]) / Th[1], -0.607, 1e-3)

last = Matrix([[0, 1]]) * Wc.inv()
near(last[0], -2.608, 2e-3); near(last[1], 13.258, 2e-3)
P2 = Ph ** 2
near(P2[1, 0], 0.2325)
K = last * P2
near(K[0], 2.1235); near(K[1], 1.7942)
M = (Ph - Th * K).applyfunc(simplify)
assert simplify(M.trace()) == 0 and simplify(M.det()) == 0
x0 = Matrix([1, 1]); x1 = M * x0
near((-K * x0)[0], -3.918, 1e-3); near(x1[0], -0.935, 1e-3); near(x1[1], 0.303, 1e-3)
near((-K * x1)[0], 1.441, 1e-3)
assert (M * x1).applyfunc(simplify) == Matrix([0, 0])
print('all checks passed')
