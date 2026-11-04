"""Check quiz-02-kalman-sprint.html: numeric keys against the slide formulas, and that every pop-up image exists."""
import re, pathlib
from fractions import Fraction as F
here = pathlib.Path(__file__).parent
html = (here / "quiz-02-kalman-sprint.html").read_text().split("<main>")[1].split("</main>")[0]
def kf(P, R, A=1, H=1, Q=0):  # Lec 4 pp. 29, 31
    P, R = F(P), F(R); K = A * H * P / (H * H * P + R)
    return K, A * A * P + Q - (A * H * P) ** 2 / (H * H * P + R)
num = dict(re.findall(r'data-id="(\w+)" data-num="([^"]+)"', html))
fr = lambda v: F(v)
assert fr(num["k3a"]) == kf(6, 3)[0]
assert [fr(v) for v in num["k4a"].split(",")] == list(kf(4, 4))
assert fr(num["k4b"]) == kf(6, 3)[1] == 1 / (F(1, 6) + F(1, 3))
s1, s2, z1, z2 = F(1), F(2), F(10), F(13)
xh = (s2 * z1 + s1 * z2) / (s1 + s2); K, P = kf(s1, s2)
assert z1 + K * (z2 - z1) == xh and [fr(v) for v in num["k5a"].split(",")] == [xh, P]
for P_, R_ in [(4, 4), (6, 3), (1, 2), (5, 7)]:                     # identities taught in Part 4
    K, Pn = kf(P_, R_); assert Pn == (1 - K) * P_ == 1 / (F(1, P_) + F(1, R_)) and Pn < min(P_, R_)
for k, lo, hi in re.findall(r'data-pages="(\w+):(\d+)-(\d+)"', html):
    assert k == "L4"
    for n in range(int(lo), int(hi) + 1):
        f = here / "quiz-02-primer-pages" / f"part-2-lecture-04-kalman-filter-sensor-integration-p{n:03d}.jpg"; assert f.exists(), f
tf = re.findall(r'data-tf="([TF])"', html)
print(f"ok: {len(num)} numeric checks, {len(tf)} T/F ({tf.count('T')} T / {tf.count('F')} F), all pop-up images present")
