"""Check quiz-02-mocks-cd.html: numeric keys, answer-key shape, and that every citation pop-up image exists."""
import re, pathlib, math
from fractions import Fraction as F
here = pathlib.Path(__file__).parent
html = (here / "quiz-02-mocks-cd.html").read_text()
tf = lambda i: re.search(rf'data-id="{i}" data-tf="([TF])"', html).group(1)
assert 1 - F(abs(98 - 100), 100) == F(98, 100) and tf("c3") == "T"                 # accuracy
assert round(10 * math.log10(20 / 0.001)) == 43 and tf("d2") == "T"                # dynamic range
assert (500 * F(2, 10) + 320, 500 * F(-1, 10) + 240) == (420, 190) and tf("d4") == "T"  # p = A m
X = [1, 1, 1, 2, 2, 2, 2, 3]; EX = F(sum(X), 8); EX2 = F(sum(x * x for x in X), 8)
assert EX == F(7, 4) and EX2 - EX ** 2 == F(7, 16) and tf("d7") == "T"             # E, V of population
A = H = 1; P = 4; R = 4; Q = 0
K = F(A * H * P, H * H * P + R); Pn = A * A * P + Q - F((A * H * P) ** 2, H * H * P + R)
assert K == F(1, 2) and Pn == 2 and (1 - K * H) * P == Pn                         # B false (8)
assert 'data-mcq="ACD"' in html and 'data-mcq="ABD"' in html
SRC = {"L1": "part-2-lecture-01-introduction-and-sensors", "L2": "part-2-lecture-02-vision-sensors-and-systems",
       "L3": "part-2-lecture-03-structure-and-pose-estimation", "L4": "part-2-lecture-04-kalman-filter-sensor-integration"}
for k, lo, hi in re.findall(r'data-pages="(\w+):(\d+)-(\d+)"', html):
    for n in range(int(lo), int(hi) + 1):
        f = here / "quiz-02-primer-pages" / f"{SRC[k]}-p{n:03d}.jpg"; assert f.exists(), f
for p in "cd":
    v = re.findall(rf'data-id="{p}\d" data-tf="([TF])"', html)
    assert len(v) == 7 and len(re.findall(rf'data-id="{p}\d" data-mcq', html)) == 1
    print(f"Paper {p.upper()}: 7 T/F ({v.count('T')} T / {v.count('F')} F) + 1 MCQ")
assert html.count('class="ans" hidden') == 16 and html.count('class="must"') == 16
print("ok: keys verified, all pop-up images present, answers hidden until submit")
