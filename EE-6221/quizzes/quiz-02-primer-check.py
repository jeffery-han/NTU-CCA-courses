"""Re-derives every numeric key in quiz-02-primer.html. Run: python3 quiz-02-primer-check.py"""
from fractions import Fraction as F
import re, pathlib

# worked examples
assert F(340) * F(40, 1000) / 2 == F(68, 10)                      # TOF 40 ms -> 6.8 m
assert 1 - F(2, 50) == F(96, 100)                                  # accuracy 0.96
assert (400 * F(3, 10) / 3 + 300, 400 * F(6, 10) / 3 + 200) == (340, 280)
assert 4 * 1 + 9 * 2 == 22                                         # V(2X-3Y)
assert (4 * 20 + 2 * 26) / F(6) == 22 and 1 / (F(1, 2) + F(1, 4)) == F(4, 3)

# check keys, recomputed
keys = {
    "c1b": [F(340) * F(12, 1000) / 2],
    "c2a": [400 * F(-4, 10) / 2 + 300, 400 * F(2, 10) / 2 + 200],
    "c5a": [1 * 3 + (-2) ** 2 * 1],
    "c6a": [(1 * 8 + 3 * 12) / F(4), 1 / (F(1, 3) + 1)],
}
html = pathlib.Path(__file__).with_name("quiz-02-primer.html").read_text()
for cid, want in keys.items():
    got = re.search(rf'data-id="{cid}"[^>]*data-ans="([^"]+)"', html).group(1).split(",")
    assert [F(g) for g in got] == want, (cid, got, want)

# every cited slide image exists
stems = dict(re.findall(r'(L\d): "([^"]+)"', html))
for k, lo, hi in re.findall(r'data-pages="(L\d):(\d+)-(\d+)"', html):
    for p in range(int(lo), int(hi) + 1):
        assert pathlib.Path(__file__).with_name("quiz-02-primer-pages").joinpath(f"{stems[k]}-p{p:03d}.jpg").exists(), (k, p)
print("all quiz-02-primer keys verified")
