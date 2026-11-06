"""Verify every numeric key in quiz-03-mock-c.html and quiz-03-mock-d.html.

Run: python3 quiz-03-mock-cd-check.py   (prints the keys; any mismatch raises AssertionError)
"""
import numpy as np
import sympy as sp

z, s = sp.symbols('z s')
close = lambda a, b, tol=5e-4: abs(float(a) - float(b)) <= tol * max(1, abs(float(b)))


def zoh(Gs, T):
    """G(z) = (1 - z^-1) Z{G(s)/s} by residues of G(s)/s * 1/(1 - e^{sT} z^-1)."""
    F = sp.apart(sp.together(Gs / s), s)
    out = 0
    for term in sp.Add.make_args(F):
        num, den = sp.fraction(sp.factor(term))
        p = sp.solve(den, s)[0]
        # simple and double poles only (enough here)
        mult = sp.roots(sp.Poly(den, s))[p]
        c = sp.limit(term * (s - p) ** mult, s, p)
        if mult == 1:
            out += c * z / (z - sp.exp(p * T))
        elif mult == 2 and p == 0:
            out += c * T * z / (z - 1) ** 2
        else:
            raise ValueError(term)
    return sp.simplify((z - 1) / z * out)


def stable_range(P, K, lo, hi, n=40001):
    Ks = np.linspace(lo, hi, n)
    ok = [max(abs(np.roots([float(c) for c in sp.Poly(P.subs(K, k), z).all_coeffs()]))) < 1 for k in Ks]
    idx = [i for i, v in enumerate(ok) if v]
    return Ks[idx[0]], Ks[idx[-1]]


K = sp.symbols('K')
keys = {}

# ---------------- Mock C ----------------
# C-Q1: K/(s(s+2)) with ZOH, T = 0.2
T = sp.Rational(1, 5)
G1 = sp.simplify(zoh(1 / (s * (s + 2)), T))
num, den = sp.fraction(sp.together(G1))
num = sp.Poly(sp.expand(num), z); den = sp.Poly(sp.expand(den), z)
lead = den.LC()
bn = [float(c / lead) for c in num.all_coeffs()]
an = [float(c / lead) for c in den.all_coeffs()]
print('C-Q1 G(z)/K numerator', bn, 'denominator', an)
keys['c-1a-b1'] = bn[0]  # 0.01758
keys['c-1a-b0'] = bn[1]  # 0.01539
assert close(an[1], -1.670320, 1e-4) and close(an[2], 0.670320, 1e-4)
P = sp.expand(sp.Poly(den, z).as_expr() + K * sp.Poly(num, z).as_expr())
lo, hi = stable_range(P, K, -5, 40)
Kmax = (1 - an[2]) / bn[1]  # binding condition |a2| < a0
print('C-Q1 stable K range by root scan', lo, hi, '| closed form 0 < K <', Kmax)
assert close(hi, Kmax, 1e-3) and abs(lo) < 2e-3
keys['c-1b-kmax'] = Kmax  # 21.46
Kv = float(sp.limit((z - 1) / z * G1 / T, z, 1))  # per unit K
print('C-Q1 Kv/K =', Kv)
assert close(Kv, 0.5, 1e-4)
keys['c-1c-kv'] = 4 * Kv          # K = 4 -> Kv = 2
keys['c-1c-ess'] = 1 / (4 * Kv)   # 0.5

# C-Q2: G(s) = (s+2)/((s+1)(s+4)), T = 0.2
T = sp.Rational(1, 5)
Gs = (s + 2) / ((s + 1) * (s + 4))
e = lambda x: sp.exp(-x * T)
alpha = sp.Rational(1, 2) * (1 - e(1)) * (1 - e(4)) / (1 - e(2))
print('C-Q2 PZM alpha (strictly proper, DC 0.5) =', float(alpha), ' zero', float(e(2)), 'poles', float(e(1)), float(e(4)))
keys['c-2a-alpha'] = float(alpha)
Gb = sp.factor(sp.simplify(Gs.subs(s, 2 / T * (z - 1) / (z + 1))))
print('C-Q2 bilinear', Gb)
nb, db = sp.fraction(sp.together(Gb))
db_ = sp.Poly(sp.expand(db), z); nb_ = sp.Poly(sp.expand(nb), z)
assert db_.all_coeffs() == [77, -96, 27] and nb_.all_coeffs() == [6, 2, -4], (db_.all_coeffs(), nb_.all_coeffs())
assert Gb.subs(z, 1) == sp.Rational(1, 2)
keys['c-2b-b0'] = 6 / 77      # 0.07792
keys['c-2b-a1'] = 96 / 77     # recursion coefficient +1.2468 on h(k-1)
keys['c-2b-a2'] = -27 / 77    # -0.35065 on h(k-2)

# C-Q3: G = 0.5(z+0.4)/((z-1.5)(z-0.2)), Gcl = a0 z^-1 + a1 z^-2
a0, a1 = sp.symbols('a0 a1')
Gp = sp.Rational(1, 2) * (z + sp.Rational(2, 5)) / ((z - sp.Rational(3, 2)) * (z - sp.Rational(1, 5)))
Gcl = a0 / z + a1 / z ** 2
sol = sp.solve([Gcl.subs(z, 1) - 1, (1 - Gcl).subs(z, sp.Rational(3, 2))], [a0, a1])
print('C-Q3 a0, a1 =', sol)
assert sol == {a0: sp.Rational(5, 2), a1: sp.Rational(-3, 2)}
Gcl = Gcl.subs(sol)
C = sp.factor(sp.simplify(Gcl / (Gp * (1 - Gcl))))
print('C-Q3 C(z) =', C)
assert sp.simplify(C - 5 * (z - sp.Rational(3, 5)) * (z - sp.Rational(1, 5)) / ((z + sp.Rational(2, 5)) * (z - 1))) == 0
Y = sp.series((Gcl * z / (z - 1)).subs(z, 1 / sp.Symbol('w')), sp.Symbol('w'), 0, 5).removeO()
y = [Y.coeff(sp.Symbol('w'), k) for k in range(4)]
print('C-Q3 y(0..3) =', y)
assert y == [0, sp.Rational(5, 2), 1, 1]
U = sp.series((Gcl / Gp * z / (z - 1)).subs(z, 1 / sp.Symbol('w')), sp.Symbol('w'), 0, 6).removeO()
u = [U.coeff(sp.Symbol('w'), k) for k in range(5)]
print('C-Q3 u(0..4) =', u)
keys['c-3b-a0'] = 2.5
keys['c-3b-a1'] = -1.5
keys['c-3c-y1'] = 2.5
keys['c-3c-y2'] = 1.0
# closed-loop poles of the realised loop must be inside (the C pole at 1 is the integrator, cancelled by no one)
CLchar = sp.Poly(sp.expand(sp.fraction(sp.together(1 + C * Gp))[0]), z)
print('C-Q3 1+CG numerator roots', [complex(r) for r in sp.Poly(CLchar).nroots()])

# ---------------- Mock D ----------------
# D-A1: Kp
Gd = sp.Rational(1, 2) * (z + sp.Rational(1, 2)) / ((z - sp.Rational(1, 2)) * (z - sp.Rational(1, 5)))
Kp = Gd.subs(z, 1)
print('D-A1 Kp', Kp, 'ess', 1 / (1 + Kp), ' CL poles', sp.Poly(sp.expand((z - 0.5) * (z - 0.2) + 0.5 * (z + 0.5)), z).nroots())
assert Kp == sp.Rational(15, 8) and close(1 / (1 + Kp), 0.347826)

# D-Q1: P = z^3 - 1.5 z^2 + 0.5 z + K
P = z ** 3 - sp.Rational(3, 2) * z ** 2 + sp.Rational(1, 2) * z + K
lo, hi = stable_range(P, K, -2, 4)
Kb = (-1.5 + np.sqrt(1.5 ** 2 + 2)) / 2
print('D-Q1 root-scan range', lo, hi, '| b-row closed form', Kb)
assert abs(lo) < 2e-3 and close(hi, Kb, 1e-3)
keys['d-1a-kmax'] = Kb  # 0.2808
T = sp.Rational(1, 10)
Kv = sp.limit((z - 1) / z * sp.Rational(1, 5) / (z * (z - 1) * (z - sp.Rational(1, 2))) / T, z, 1)
print('D-Q1 Kv at K=0.2, T=0.1 =', Kv)
assert Kv == 4
keys['d-1b-kv'] = 4
keys['d-1b-ess'] = 0.25

# D-Q2: D(s) = 4(s+2)/(s+8), T = 0.1
T = sp.Rational(1, 10)
Ds = 4 * (s + 2) / (s + 8)
Db = sp.factor(sp.simplify(Ds.subs(s, 2 / T * (z - 1) / (z + 1))))
print('D-Q2 bilinear', Db)
assert sp.simplify(Db - (22 * z - 18) / (7 * z - 3)) == 0
keys['d-2a-gain'] = 22 / 7       # 3.1429
keys['d-2a-zero'] = 18 / 22      # 0.8182
keys['d-2a-pole'] = 3 / 7        # 0.4286
alpha = (1 - sp.exp(-sp.Rational(8, 10))) / (1 - sp.exp(-sp.Rational(2, 10)))
print('D-Q2 PZM alpha', float(alpha))
keys['d-2b-alpha'] = float(alpha)   # 3.0372
# direct programming, unit-step error
u = []; e = [1, 1, 1]
for k in range(3):
    uk = sp.Rational(3, 7) * (u[k - 1] if k else 0) + sp.Rational(22, 7) * e[k] - sp.Rational(18, 7) * (e[k - 1] if k else 0)
    u.append(uk)
print('D-Q2 u(0..2) for unit-step e', u, [float(x) for x in u])
assert u[0] == sp.Rational(22, 7) and u[1] == sp.Rational(94, 49)
keys['d-2c-u0'] = 22 / 7
keys['d-2c-u1'] = 94 / 49

# D-Q3: G = 0.25(z+0.8)/((z-1)(z-0.5))
Gp = sp.Rational(1, 4) * (z + sp.Rational(4, 5)) / ((z - 1) * (z - sp.Rational(1, 2)))
w = sp.Symbol('w')
seq = lambda F, n: [sp.series(F.subs(z, 1 / w), w, 0, n + 1).removeO().coeff(w, k) for k in range(n)]
Gcl = 1 / z
C = sp.factor(sp.simplify(Gcl / (Gp * (1 - Gcl))))
print('D-Q3a C(z) =', C)
assert sp.simplify(C - 4 * (z - sp.Rational(1, 2)) / (z + sp.Rational(4, 5))) == 0
u = seq(Gcl / Gp * z / (z - 1), 5)
print('D-Q3b u(0..4) =', u, [float(x) for x in u])
assert [float(x) for x in u[:4]] == [4.0, -5.2, 4.16, -3.328]
keys['d-3b-u1'] = -5.2
keys['d-3b-u2'] = 4.16
Kc = sp.Rational(1, 1) / sp.Rational(9, 5)
Gcl = Kc / z * (1 + sp.Rational(4, 5) / z)
C = sp.factor(sp.simplify(Gcl / (Gp * (1 - Gcl))))
print('D-Q3c K =', Kc, float(Kc), ' C(z) =', C)
assert sp.simplify(C - sp.Rational(20, 9) * (z - sp.Rational(1, 2)) / (z + sp.Rational(4, 9))) == 0
y = seq(Gcl * z / (z - 1), 4); u = seq(Gcl / Gp * z / (z - 1), 5)
print('D-Q3c y(0..3) =', y, ' u(0..4) =', u)
assert y == [0, sp.Rational(5, 9), 1, 1] and u == [sp.Rational(20, 9), sp.Rational(-10, 9), 0, 0, 0]
keys['d-3c-K'] = float(Kc)        # 0.5556
keys['d-3c-y1'] = 5 / 9
keys['d-3c-u0'] = 20 / 9          # 2.2222

print('\nAll keys verified:')
for k, v in keys.items():
    print(f'  {k:12s} {v:.6g}')

# Every data-ans in the two pages must match a verified key (within the page tolerance).
import re, pathlib
here = pathlib.Path(__file__).parent
for page in ['quiz-03-mock-c.html', 'quiz-03-mock-d.html']:
    p = here / page
    if not p.exists():
        continue
    html = p.read_text(encoding='utf-8')
    found = re.findall(r'data-id="([^"]+)"[^>]*data-ans="([^"]+)"', html)
    for qid, ans in found:
        assert qid in keys, f'{page}: {qid} has no verified key'
        a = eval(ans.replace('/', '/'))  # fractions like 2/21
        assert close(a, keys[qid], 2e-3), f'{page}: {qid} page {a} vs key {keys[qid]}'
    print(f'{page}: {len(found)} numeric boxes match the verified keys')
