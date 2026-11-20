"""Check quiz-02-sprint.html: numeric keys and that every citation pop-up image exists."""
import re, pathlib
from fractions import Fraction as F
here = pathlib.Path(__file__).parent
html = (here / "quiz-02-sprint.html").read_text()
# D2: optimal fusion of variances 2 and 6
p = 1 / (F(1, 2) + F(1, 6)); assert p == F(3, 2) and 'data-num="1.5"' in html
L = (F(2) / (2 + 6)); assert (1 - L) ** 2 * 2 + L ** 2 * 6 == p          # gain form agrees
# variance identity sample check: X, Y uncorrelated discrete
xs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]                                # uniform, independent signs
E = lambda f: F(sum(f(x, y) for x, y in xs), len(xs))
assert E(lambda x, y: (x + y) ** 2) - E(lambda x, y: x + y) ** 2 == 2
SRC = {"L1": "part-2-lecture-01-introduction-and-sensors", "L2": "part-2-lecture-02-vision-sensors-and-systems",
       "L3": "part-2-lecture-03-structure-and-pose-estimation", "L4": "part-2-lecture-04-kalman-filter-sensor-integration"}
for k, lo, hi in re.findall(r'data-pages="(\w+):(\d+)-(\d+)"', html):
    for n in range(int(lo), int(hi) + 1):
        f = here / "quiz-02-primer-pages" / f"{SRC[k]}-p{n:03d}.jpg"; assert f.exists(), f
for imgs in re.findall(r'data-img="([\d,]*)"', html):
    for n in filter(None, imgs.split(",")):
        assert (here / "quiz-02-sprint-pages" / f"tutor4-image{n}.png").exists(), n
tf = re.findall(r'data-tf="([TF])"', html)
print(f"ok: {len(tf)} T/F items ({tf.count('T')} T / {tf.count('F')} F), all pop-up images present")
