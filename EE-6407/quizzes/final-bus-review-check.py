"""Checks final-bus-review.html: every key names a real option, ids are unique, numeric keys recompute."""
import re, sys, math, pathlib
html = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).with_name("final-bus-review.html")).read_text()
blocks = re.findall(r'<div class="q" data-id="(\w+)" data-answer="(\w)">(.*?)<p class="why"', html, re.S)
ids = [b[0] for b in blocks]
assert len(ids) == len(set(ids)) == html.count('class="q"'), "duplicate or unparsed question"
keyed = {}
for qid, ans, body in blocks:
    opts = dict(re.findall(r'data-opt="(\w)">(.*?)</button>', body))
    assert ans in opts, f"{qid}: key {ans} not an option"
    assert len(set(opts.values())) == len(opts), f"{qid}: duplicate option text"
    keyed[qid] = opts[ans]
num = lambda q: float(re.search(r'-?[\d.]+', keyed[q].replace("−", "-")).group())
close = lambda q, v: abs(num(q) - v) < 5e-4 * max(1, abs(v))
def pmx(p1, p2, a, b):
    c = [None] * len(p1); c[a:b + 1] = p1[a:b + 1]
    for i in range(a, b + 1):
        v = p2[i]
        if v in c: continue
        j = i
        while a <= j <= b: j = p2.index(p1[j])
        c[j] = v
    return [p2[i] if x is None else x for i, x in enumerate(c)]
assert close("g1", 0 + 14 * int("101", 2) / (2**3 - 1))
assert close("g2", 5 / (2 + 3 + 5))
assert keyed["g3"] == "d(2,1) + d(1,4) + d(4,3) + d(3,2)"
assert close("g4", 0.25 * 4 + 0.75 * 8)
assert keyed["g5"] == " ".join(map(str, pmx([1, 2, 3, 4, 5], [3, 5, 1, 2, 4], 1, 2)))
assert close("b1", (2 + 1) / (6 + 4))
assert close("b3", -(2**2) / (2 * 4))
assert close("b4", 1 / (1 + math.exp(-math.log(3))))
assert close("t1", 0.5 * (1 - (3/4)**2 - (1/4)**2))
assert close("t2", 0.4 * 0 + 0.6 * 0.25)
assert close("s2", 2 / math.hypot(3, 4))
g = 1 * 2.5 + 0 * 7 - 2; assert close("s3", max(0, 1 - (-1) * g))
assert close("s5", 0.5 + 0.5 - 0.2)
assert keyed["f1"] == "(2, 1)" and (4 / 2, 4 / 4) == (2, 1)
assert close("f2", -(2 * (3 + 1) + 1 * (1 + 1)) / 2)
assert (2 * 1 + 1 * 1, 1 * 1 + 2 * 1) == (3, 3) and keyed["f3"] == "Yes"
c1 = [0, 2, 10, 12]; a1 = [x for x in c1 if abs(x - 0) <= abs(x - 2)]; a2 = [x for x in c1 if x not in a1]
assert keyed["k1"] == f"{sum(a1)/len(a1):g} and {sum(a2)/len(a2):g}"
assert close("k2", max(abs(a - b) for a in (1, 2) for b in (6, 9)))
assert keyed["k3"] == "False" and math.hypot(3, 4) == 5
assert close("i1", math.sqrt((1 + 1 + 4) / 3))
assert close("i2", 6 / 3)
assert close("i3", 6 / math.comb(5, 2))
assert close("i4", (2 * 4 + 2 * 4) / 8)
assert close("i6", (6 - 2) / max(2, 6))
assert close("w2", 6 / (6 + 2))
assert close("w3", (7 - 2) / (12 - 2))
assert close("w4", (13 - 10) / 2)
assert close("w5", 20)
print(f"ok: {len(ids)} questions")
