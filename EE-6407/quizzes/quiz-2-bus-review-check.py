"""Checks quiz-2-bus-review.html: every key names a real option, ids are unique, numeric keys recompute."""
import re, sys, pathlib
html = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "quiz-2-bus-review.html").read_text()
blocks = re.findall(r'<div class="q" data-id="(\w+)" data-answer="(\w)">(.*?)<p class="why"', html, re.S)
ids = [b[0] for b in blocks]
assert len(ids) == len(set(ids)) == html.count('class="q"'), "duplicate or unparsed question"
keyed = {}
for qid, ans, body in blocks:
    opts = dict(re.findall(r'data-opt="(\w)">(.*?)</button>', body))
    assert ans in opts, f"{qid}: key {ans} not an option"
    keyed[qid] = opts[ans]
num = lambda q: float(re.search(r'-?[\d.]+', keyed[q]).group())
assert num("m2") == 8 / (8 + 2)                          # precision
assert num("m8") == 50                                    # LOOCV
assert num("t1") == 1 - (0.5**2 + 0.5**2)                 # Gini 50/50
assert abs(num("t2") - (0.8 * 0.5 + 0.2 * 0)) < 1e-12     # weighted Gini
assert abs(num("t3") - (0.48 - 0.30)) < 1e-12             # impurity drop
assert num("f1") == 3**2 / (1**2 + 2**2)                  # Fisher with squared sigma
assert num("f6") == 4                                     # SFS first step
assert keyed["c2"] == "(2, 2)" and (0+2+4)/3 == 2 == (0+4+2)/3
assert num("c3") == (3-1)**2 + (1-1)**2
assert num("c6") == min(abs(a-b) for a in (1,2) for b in (6,9))
assert abs(num("c9") - (6-2)/max(2,6)) < 0.005
assert num("c10") == abs(4-1) + abs(6-2)
assert num("e2") == 2 / (3**2 + 4**2) ** 0.5
assert "x₂, x₄" in keyed["f2"]                            # top-2 of {0.8,2.5,0.1,1.6}
print(f"ok: {len(ids)} questions")
