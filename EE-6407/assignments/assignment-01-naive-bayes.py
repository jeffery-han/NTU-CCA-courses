"""EE6407 Assignment 1: data checks + Gaussian Naive Bayes, stdlib only.

Run from this directory:  python3 -I assignment-01-naive-bayes.py
Prints the numbers and HTML table fragments used in assignment-01-report-draft.html.
"""
import math, statistics as st, sys
from decimal import Decimal as D
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # so `python3 -I` still finds the sibling reader
from xlsx_reader import read
CLASSES = (1, 2, 3)
FEATS = 'ABCD'


def load(name, labelled):
    rows = []
    for n, r in read(HERE / name):
        x = [r.get(c) for c in FEATS]
        rows.append((n, x, int(r['E'])) if labelled else (n, x))
    return rows


def tukey(values, k):
    """Exact-decimal Tukey fences (avoids 0.3 + 3*0.1 != 0.6 float edge)."""
    q1, _, q3 = st.quantiles([D(str(v)) for v in values], n=4, method='inclusive')
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def flag(rows, k):
    out = []
    for c in CLASSES:
        cls = [(n, x) for n, x, y in rows if y == c]
        for j, f in enumerate(FEATS):
            lo, hi = tukey([x[j] for _, x in cls], k)
            med = st.median(x[j] for _, x in cls)
            out += [(n, f, c, x[j], float(lo), float(hi), med)
                    for n, x in cls if not lo <= D(str(x[j])) <= hi]
    return sorted(out)


def fit(rows):
    model = {}
    for c in CLASSES:
        X = [x for _, x, y in rows if y == c]
        mu = [st.mean(r[j] for r in X) for j in range(4)]
        var = [st.variance(r[j] for r in X) for j in range(4)]  # unbiased, N-1
        model[c] = (len(X), len(rows), mu, var)
    return model


def g(model, c, x):
    """g_c(x) = ln P(w_c) - sum_j [ 1/2 ln(2 pi var_cj) + (x_j - mu_cj)^2 / (2 var_cj) ]"""
    nc, n, mu, var = model[c]
    return math.log(nc / n) - sum(0.5 * math.log(2 * math.pi * var[j]) + (x[j] - mu[j]) ** 2 / (2 * var[j])
                                  for j in range(4))


def predict(model, x):
    return max(CLASSES, key=lambda c: g(model, c, x))


train, test = load('assignment-01-training-data.xlsx', True), load('assignment-01-test-data.xlsx', False)
missing = [(n, FEATS[j]) for n, x, _ in train for j, v in enumerate(x) if not isinstance(v, float)]
complete = [r for r in train if all(isinstance(v, float) for v in r[1])]
far = flag(complete, 3)        # removed
mild = [f for f in flag(complete, D('1.5')) if f[0] not in {r[0] for r in far}]  # kept
clean = [r for r in complete if r[0] not in {f[0] for f in far}]
model = fit(clean)
preds = [(n, x, predict(model, x), {c: g(model, c, x) for c in CLASSES}) for n, x in test]
acc = sum(predict(model, x) == y for _, x, y in clean) / len(clean)

# self-check: the documented rule gives exactly these rows, and N vs N-1 variance agree
assert missing == [(39, 'A'), (61, 'A'), (83, 'D')]
assert [f[0] for f in far] == [91, 96, 117] and len(clean) == 114
mle = {c: (nc, n, mu, [v * (nc - 1) / nc for v in var]) for c, (nc, n, mu, var) in model.items()}
assert [predict(mle, x) for _, x in test] == [p for _, _, p, _ in preds]

if __name__ == '__main__':
    f2 = lambda v: f'{v:.2f}'
    print('missing', missing, '\nfar-out', far, '\nmild kept', mild)
    print('class sizes', {c: model[c][0] for c in CLASSES}, 'resub acc', round(acc, 4))
    print('\n<!-- outliers -->')
    for n, f, c, v, lo, hi, med in far:
        print(f'<tr><td>{n}</td><td>{f}</td><td>{c}</td><td>{v}</td><td>{med}</td><td>[{f2(lo)}, {f2(hi)}]</td></tr>')
    print('\n<!-- mild -->')
    print(', '.join(f'row {n} ({f}={v}, class {c})' for n, f, c, v, *_ in mild))
    print('\n<!-- params -->')
    for c in CLASSES:
        nc, n, mu, var = model[c]
        cells = ''.join(f'<td>{m:.4f}</td><td>{v:.4f}</td>' for m, v in zip(mu, var))
        print(f'<tr><th>{c}</th><td>{nc}/{n} = {nc/n:.4f}</td>{cells}</tr>')
    print('\n<!-- predictions -->')
    for n, x, p, gs in preds:
        print(f'<tr><td>{n}</td>' + ''.join(f'<td>{v}</td>' for v in x)
              + ''.join(f'<td>{gs[c]:.2f}</td>' for c in CLASSES) + f'<td><b>{p}</b></td></tr>')
    print('\n<!-- worked test 11 -->')
    x = test[10][1]
    for c in CLASSES:
        nc, n, mu, var = model[c]
        terms = [0.5 * math.log(2 * math.pi * var[j]) + (x[j] - mu[j]) ** 2 / (2 * var[j]) for j in range(4)]
        print(c, f'lnP={math.log(nc/n):.4f}', 'terms', [round(t, 4) for t in terms], f'g={g(model, c, x):.4f}')
