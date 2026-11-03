"""Re-derives every number in quiz-02-guided.html and checks citation images. Run: python3 quiz-02-guided-check.py"""
from fractions import Fraction as F
from math import comb
import re, pathlib

here = pathlib.Path(__file__).parent
html = (here / "quiz-02-guided.html").read_text()

# A3 time of flight: 25 ms -> 8.5 m round trip, 4.25 m one way
assert F(340) * F(25, 1000) == F(85, 10) and F(340) * F(25, 1000) / 2 == F(425, 100)

# A5 pinhole: f*sigma = 200, (u0, v0) = (100, 100)
pix = lambda x, y, z: (200 * F(x, z) + 100, 200 * F(y, z) + 100)
assert pix(1, 2, 4) == (150, 200) and pix(1, 2, 8) == (125, 150) != (75, 100)

# A9 X in {-1,0,1}, Y = X^2: uncorrelated
X = [-1, 0, 1]
EX, EY, EXY = (sum(F(f(x), 3) for x in X) for f in (lambda x: x, lambda x: x * x, lambda x: x ** 3))
assert EXY - EX * EY == 0

# A10 trap: K = HAP/(H^2 P + R)
K = lambda A, H, P, R: F(H * A * P, H * H * P + R)
assert K(2, 1, 1, 1) == 1 and K(3, 1, 1, 1) == F(3, 2)

# B1(d) four-point groups from 12 points
assert comb(12, 4) == 495 == 11 * 5 * 9 and 12 * 11 * 10 * 9 == 11880

# B2(d) A = H = 1, Q = 0, x = 4, P = 6, R = 3, z = 10
k = K(1, 1, 6, 3)
assert k == F(2, 3) and 4 + k * (10 - 4) == 8
assert (1 - k) ** 2 * 6 + k ** 2 * 3 == 2 == (1 - k) * 6 == 1 / (F(1, 6) + F(1, 3))

# question ids unique (they key the saved ticks)
ids = re.findall(r'class="qn" data-id="([^"]+)"', html)
assert len(ids) == len(set(ids)) == 18, ids

# every cited slide image exists
stems = dict(re.findall(r'(L\d): "([^"]+)"', html))
for kk, lo, hi in re.findall(r'data-pages="(L\d):(\d+)-(\d+)"', html):
    for p in range(int(lo), int(hi) + 1):
        assert (here / "quiz-02-primer-pages" / f"{stems[kk]}-p{p:03d}.jpg").exists(), (kk, p)
print("all quiz-02-guided numbers and citations verified")
