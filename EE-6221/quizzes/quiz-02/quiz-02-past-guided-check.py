"""Re-derives every key in quiz-02-past-guided.html and checks citation images. Run: python3 quiz-02-past-guided-check.py"""
from fractions import Fraction as F
from itertools import combinations
import re, pathlib
import sympy as sp

here = pathlib.Path(__file__).parent
html = (here / "quiz-02-past-guided.html").read_text()
num = dict(re.findall(r'data-id="(\w+)" data-num="([^"]+)"', html))

# A6 TOF 10 ms at 340 m/s; A11 32x32 8-bit image
assert F(340) * F(1, 100) / 2 == F(17, 10) and num["pa6"] == "1.7"
assert (2 ** 8, 32 * 32) == (256, 1024) and num["pa11"] == "256,1024"

def good_groups(points, lines):
    """4-point groups with no three points on one of the given lines."""
    return [g for g in combinations(points, 4) if not any(len(set(g) & L) >= 3 for L in lines)]

# B1 2016-17: triangle O1-O4-O6, side points O2, O3, O5
lines = [{1, 2, 4}, {1, 3, 6}, {4, 5, 6}]
g = good_groups(range(1, 7), lines)
assert len(g) == 6 and (2, 3, 5, 6) in g and (1, 2, 3, 4) not in g and num["pb1c"] == "6"
assert sorted(g) == [(1, 2, 3, 5), (1, 2, 5, 6), (1, 3, 4, 5), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 5, 6)]
assert len({1, 2, 3, 5} & {2, 3, 4, 5}) == 3  # B1(b): only 3 common points

# B3 AY24-25: 3 columns x 4 rows; H uses points common to Fq and Fd = O5..O12
grid = [set(range(1, 5)), set(range(5, 9)), set(range(9, 13))] + [{r, r + 4, r + 8} for r in range(1, 5)]
assert len(grid) == 7
assert len(good_groups(range(5, 13), grid)) == 36 != 68 and num["pb3b"] == "36"
assert (1, 2, 5, 6) in good_groups(range(1, 9), grid)          # B3(a) choice valid
assert not good_groups(range(5, 9), grid)                     # B3(c): O5..O8 collinear

# Kalman: generic optimum of p' = (1 - sum c_i L_i)^2 p + sum L_i^2 s_i (+ q)
p, a, s, s1, s2, c1, c2, M, N = sp.symbols("p a sigma sigma1 sigma2 c1 c2 M N", positive=True)
def optimum(cs, vs, q=0):
    Ls = sp.symbols(f"L1:{len(cs) + 1}")
    P = (1 - sum(c * L for c, L in zip(cs, Ls))) ** 2 * p + sum(L ** 2 * v for L, v in zip(Ls, vs)) + q
    sol = sp.solve([sp.diff(P, L) for L in Ls], Ls, dict=True)[0]
    return [sp.simplify(sol[L]) for L in Ls], sp.simplify(P.subs(sol))

# C1 2016-17: one gain, variances s^2, s^2, 4s^2
P1 = (1 - 3 * M) ** 2 * p + 6 * s ** 2 * M ** 2
Mopt = sp.solve(sp.diff(P1, M), M)[0]
assert sp.simplify(Mopt - p / (3 * p + 2 * s ** 2)) == 0
assert sp.simplify(P1.subs(M, Mopt) - 2 * s ** 2 * p / (3 * p + 2 * s ** 2)) == 0
pk = lambda k: F(2, 2 + 3 * k)          # p_{k+1}/sigma^2 from p_1 = sigma^2
x = F(1)
for k in range(1, 8):
    x = 2 * x / (3 * x + 2); assert x == pk(k)
assert pk(6) == F(1, 10) and pk(7) < F(1, 10) and num["pc1b"] == "7"

# C2 AY24-25: three gains and one gain, variances a^2, 4a^2, 9a^2
Ls, P = optimum([1, 1, 1], [a ** 2, 4 * a ** 2, 9 * a ** 2])
D = 36 * a ** 2 + 49 * p
assert [sp.simplify(L - e) for L, e in zip(Ls, [36 * p / D, 9 * p / D, 4 * p / D])] == [0, 0, 0]
assert sp.simplify(P - 36 * a ** 2 * p / D) == 0
P1 = (1 - 3 * M) ** 2 * p + 14 * a ** 2 * M ** 2
Mopt = sp.solve(sp.diff(P1, M), M)[0]
assert sp.simplify(Mopt - 3 * p / (9 * p + 14 * a ** 2)) == 0
assert sp.simplify(P1.subs(M, Mopt) - 14 * a ** 2 * p / (9 * p + 14 * a ** 2)) == 0
assert F(9, 14) < 1 < F(49, 36)

# C3 2015-16: gains c1, c2
Ls, P = optimum([c1, c2], [s1 ** 2, s2 ** 2])
S = c1 ** 2 / s1 ** 2 + c2 ** 2 / s2 ** 2
assert sp.simplify(P - p / (1 + p * S)) == 0
assert sp.simplify(Ls[0] - c1 * p / (s1 ** 2 * (1 + p * S))) == 0
assert sp.simplify(P.subs({c1: s1, c2: s2}) - p / (1 + 2 * p)) == 0

# C4 2017-18: N equal sensors plus process noise (check N = 2, 3, 4)
sw = sp.Symbol("sigma_w", positive=True)
for n in (2, 3, 4):
    Ls, P = optimum([1] * n, [s ** 2] * n, sw ** 2)
    assert all(sp.simplify(L - p / (s ** 2 + n * p)) == 0 for L in Ls)
    assert sp.simplify(P - (s ** 2 * p / (s ** 2 + n * p) + sw ** 2)) == 0

# ids unique (they key the saved state); every numeric item checked above
ids = re.findall(r'class="qn" data-id="([^"]+)"', html)
assert len(ids) == len(set(ids)) == 31, len(ids)
assert set(num) == {"pa6", "pa11", "pb1c", "pb3b", "pc1b"}

# every cited page image exists
imgs = {"L1": "quiz-02-primer-pages/part-2-lecture-01-introduction-and-sensors",
        "L2": "quiz-02-primer-pages/part-2-lecture-02-vision-sensors-and-systems",
        "L3": "quiz-02-primer-pages/part-2-lecture-03-structure-and-pose-estimation",
        "L4": "quiz-02-primer-pages/part-2-lecture-04-kalman-filter-sensor-integration",
        "E1516": "quiz-02-past-pages/exam-2015-2016", "E1617": "quiz-02-past-pages/exam-2016-2017",
        "E1718": "quiz-02-past-pages/exam-2017-2018", "E2425": "quiz-02-past-pages/exam-2024-2025-s1"}
cites = re.findall(r'data-pages="(\w+):(\d+)-(\d+)"', html)
for k, lo, hi in cites:
    for n in range(int(lo), int(hi) + 1):
        assert (here / f"{imgs[k]}-p{n:03d}.jpg").exists(), (k, n)
for f in re.findall(r'src="(quiz-assets/[^"]+)"', html):
    assert (here / f).exists(), f
print(f"all quiz-02-past-guided keys verified ({len(ids)} items, {len(cites)} citations)")
