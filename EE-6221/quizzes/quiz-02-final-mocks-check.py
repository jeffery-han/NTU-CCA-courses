"""Check quiz-02-final-mocks.html: numeric keys, answer-key shape, and that every citation pop-up image exists."""
import re, pathlib
from fractions import Fraction as F
here = pathlib.Path(__file__).parent
html = (here / "quiz-02-final-mocks.html").read_text()
# B2: ultrasonic range d = c t / 2
assert F(340) * F(20, 1000) / 2 == F(17, 5)                     # 3.4 m, so "6.8 m" is False
assert re.search(r'data-id="b2" data-tf="F"', html)
# B6: V(X - 2Y) = V(X) + 4 V(Y) for uncorrelated X, Y; sample check with independent uniform signs
xs = [(x, y) for x in (-2, 2) for y in (-1, 1)]                 # V(X)=4, V(Y)=1, independent
E = lambda f: F(sum(f(x, y) for x, y in xs), len(xs))
V = lambda f: E(lambda x, y: f(x, y) ** 2) - E(f) ** 2
assert V(lambda x, y: x) == 4 and V(lambda x, y: y) == 1 and V(lambda x, y: x - 2 * y) == 8
assert re.search(r'data-id="b6" data-tf="T"', html)
# A5: zero-mean uncorrelated -> E[XY] = 0
assert E(lambda x, y: x * y) == 0
# B8: fusion z1=10 (var 1), z2=13 (var 2)
s1, s2, z1, z2 = F(1), F(2), F(10), F(13)
xh, P, w1 = (s2 * z1 + s1 * z2) / (s1 + s2), s1 * s2 / (s1 + s2), s2 / (s1 + s2)
assert (xh, P, w1) == (11, F(2, 3), F(2, 3)) and P < min(s1, s2)
K = s1 / (s1 + s2); assert z1 + K * (z2 - z1) == xh and (1 - K) * s1 == P   # sequential form agrees
truth = {"A": xh == 11, "B": P == F(2, 3), "C": P < min(s1, s2), "D": w1 == F(1, 3)}
assert 'data-mcq="' + "".join(k for k, v in truth.items() if v) + '"' in html
SRC = {"L1": "part-2-lecture-01-introduction-and-sensors", "L2": "part-2-lecture-02-vision-sensors-and-systems",
       "L3": "part-2-lecture-03-structure-and-pose-estimation", "L4": "part-2-lecture-04-kalman-filter-sensor-integration"}
for k, lo, hi in re.findall(r'data-pages="(\w+):(\d+)-(\d+)"', html):
    for n in range(int(lo), int(hi) + 1):
        f = here / "quiz-02-primer-pages" / f"{SRC[k]}-p{n:03d}.jpg"; assert f.exists(), f
for P_ in "ab":
    tf = re.findall(rf'data-id="{P_}\d" data-tf="([TF])"', html); mcq = re.findall(rf'data-id="{P_}\d" data-mcq', html)
    assert len(tf) == 7 and len(mcq) == 1, P_
    print(f"Paper {P_.upper()}: 7 T/F ({tf.count('T')} T / {tf.count('F')} F) + 1 MCQ")
assert html.count('class="ans" hidden') == 16
print("ok: keys verified, all pop-up images present, answers hidden until submit")
