"""EE6407 Assignment 1: data checks + Gaussian Naive Bayes, stdlib only.

Run from this directory:  python3 -I assignment-01-naive-bayes.py
Prints the numbers and HTML table fragments used in assignments-01-02-report.html.
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


def posteriors(model, x):
    """Class posteriors by log-sum-exp on g_i(x) (numerically safe)."""
    gs = {c: g(model, c, x) for c in CLASSES}
    top = max(gs.values())
    e = {c: math.exp(v - top) for c, v in gs.items()}
    z = sum(e.values())
    return {c: e[c] / z for c in CLASSES}


def corr(rows, j, k):
    a, b = [x[j] for _, x, _ in rows], [x[k] for _, x, _ in rows]
    ma, mb = st.mean(a), st.mean(b)
    return (sum((u - ma) * (v - mb) for u, v in zip(a, b))
            / math.sqrt(sum((u - ma) ** 2 for u in a) * sum((v - mb) ** 2 for v in b)))



train, test = load('assignment-01-training-data.xlsx', True), load('assignment-01-test-data.xlsx', False)
missing = [(n, FEATS[j]) for n, x, _ in train for j, v in enumerate(x) if not isinstance(v, float)]
complete = [r for r in train if all(isinstance(v, float) for v in r[1])]
far = flag(complete, 3)        # removed
mild = [f for f in flag(complete, D('1.5')) if f[0] not in {r[0] for r in far}]  # kept
clean = [r for r in complete if r[0] not in {f[0] for f in far}]
model = fit(clean)
preds = [(n, x, predict(model, x), {c: g(model, c, x) for c in CLASSES}) for n, x in test]
acc = sum(predict(model, x) == y for _, x, y in clean) / len(clean)

# resubstitution confusion matrix, and the samples it gets wrong
conf = {(t, p): 0 for t in CLASSES for p in CLASSES}
for _, x, y in clean:
    conf[(y, predict(model, x))] += 1
wrong = [(n, y, predict(model, x)) for n, x, y in clean if predict(model, x) != y]

# leave-one-out: refit without each sample. The cleaning decisions (which rows to drop) are
# fixed first, so this measures the classifier, not the outlier rule.
loo = [(y, predict(fit(clean[:i] + clean[i + 1:]), x)) for i, (_, x, y) in enumerate(clean)]
conf_loo = {(t, p): sum(1 for tt, ppp in loo if tt == t and ppp == p) for t in CLASSES for p in CLASSES}
loo_acc = sum(1 for t, p in loo if t == p) / len(loo)

# margin to the runner-up class and posterior of the winner, per test sample
margin = {n: sorted(v.values())[-1] - sorted(v.values())[-2] for n, _, _, v in preds}
post = {n: posteriors(model, x) for n, x, _, _ in preds}
closest = sorted(margin, key=lambda k: margin[k])[:4]

# naive Bayes assumes independence: how wrong is that for the strongest feature pair?
r_ac = corr(clean, 0, 2)
r_ac_cls = {c: corr([(n, x, y) for n, x, y in clean if y == c], 0, 2) for c in CLASSES}

# self-check: the documented rule gives exactly these rows, and N vs N-1 variance agree
assert missing == [(39, 'A'), (61, 'A'), (83, 'D')]
assert [f[0] for f in far] == [91, 96, 117] and len(clean) == 114
mle = {c: (nc, n, mu, [v * (nc - 1) / nc for v in var]) for c, (nc, n, mu, var) in model.items()}
assert [predict(mle, x) for _, x in test] == [p for _, _, p, _ in preds]
# self-check: reported counts, ties, and the identity between full and reduced discriminants
assert sum(conf.values()) == 114 and len(wrong) == 5 and wrong == [(12, 2, 3), (23, 2, 3), (56, 3, 2), (85, 2, 3), (89, 3, 2)]
assert abs(acc - 109 / 114) < 1e-12 and abs(loo_acc - 108 / 114) < 1e-12
assert closest == [17, 23, 30, 11]
assert all(abs(sum(post[n].values()) - 1) < 1e-12 for n in post)
assert not any(abs(gs[a] - gs[b]) < 1e-9 for _, _, _, gs in preds for a in CLASSES for b in CLASSES if a < b)



def figure_c_vs_d():
    """Inline SVG: feature C vs D, train (filled) / test (hollow, predicted class), mu +/- 2 sigma ellipses."""
    W, H, L, R, T, B = 640, 400, 52, 16, 14, 44
    x0, x1, y0, y1 = 0, 7.5, 0, 2.8
    sx = lambda v: L + (v - x0) / (x1 - x0) * (W - L - R)
    sy = lambda v: H - B - (v - y0) / (y1 - y0) * (H - T - B)
    col = {1: '#2a78d6', 2: '#eb6834', 3: '#1baf7a'}  # categorical slots 1-3, fixed order

    def mark(c, x, y, fill, r=4.5):
        px, py = sx(x), sy(y)
        if c == 1:
            return f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{fill}" stroke="{col[c]}" stroke-width="1.6"/>'
        if c == 2:
            s = r * 0.9
            return f'<rect x="{px-s:.1f}" y="{py-s:.1f}" width="{2*s:.1f}" height="{2*s:.1f}" fill="{fill}" stroke="{col[c]}" stroke-width="1.6"/>'
        s = r * 1.15
        return f'<path d="M{px:.1f},{py-s:.1f} L{px+s:.1f},{py+s*0.8:.1f} L{px-s:.1f},{py+s*0.8:.1f} Z" fill="{fill}" stroke="{col[c]}" stroke-width="1.6"/>'

    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig1cap" font-family="system-ui, sans-serif" font-size="11">',
         f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>']
    for v in range(0, 8):  # grid + x ticks
        o.append(f'<line x1="{sx(v):.1f}" y1="{T}" x2="{sx(v):.1f}" y2="{H-B}" stroke="#e6e5e1" stroke-width="1"/>')
        o.append(f'<text x="{sx(v):.1f}" y="{H-B+16}" text-anchor="middle" fill="#52514e">{v}</text>')
    for v in (0, 0.5, 1, 1.5, 2, 2.5):
        o.append(f'<line x1="{L}" y1="{sy(v):.1f}" x2="{W-R}" y2="{sy(v):.1f}" stroke="#e6e5e1" stroke-width="1"/>')
        o.append(f'<text x="{L-8}" y="{sy(v)+4:.1f}" text-anchor="end" fill="#52514e">{v:g}</text>')
    o.append(f'<line x1="{L}" y1="{H-B}" x2="{W-R}" y2="{H-B}" stroke="#52514e"/>')
    o.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-8}" text-anchor="middle" fill="#0b0b0b">Feature C</text>')
    o.append(f'<text transform="translate(14,{(T+H-B)/2:.0f}) rotate(-90)" text-anchor="middle" fill="#0b0b0b">Feature D</text>')
    for c in CLASSES:  # axis-aligned ellipses = what naive Bayes assumes (diagonal covariance)
        _, _, mu, var = model[c]
        rx = 2 * math.sqrt(var[2]) / (x1 - x0) * (W - L - R)
        ry = 2 * math.sqrt(var[3]) / (y1 - y0) * (H - T - B)
        o.append(f'<ellipse cx="{sx(mu[2]):.1f}" cy="{sy(mu[3]):.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" '
                 f'stroke="{col[c]}" stroke-width="1.5" stroke-dasharray="5 4" opacity="0.9"/>')
    for c in CLASSES:  # class centroids (mu_C, mu_D)
        _, _, mu, _ = model[c]
        cx, cy = sx(mu[2]), sy(mu[3])
        o.append(f'<g><path d="M{cx-5:.1f},{cy:.1f} h10 M{cx:.1f},{cy-5:.1f} v10" stroke="{col[c]}" '
                 f'stroke-width="1.8"/><title>Class {c} centroid: C={mu[2]:.2f}, D={mu[3]:.2f}</title></g>')

    for n, x, y in clean:
        o.append(f'<g>{mark(y, x[2], x[3], col[y])}<title>Train row {n}: C={x[2]}, D={x[3]}, class {y}</title></g>')
    for n, x, p, _ in preds:
        o.append(f'<g>{mark(p, x[2], x[3], "#ffffff", 5.5)}<title>Test {n}: C={x[2]}, D={x[3]}, predicted class {p}</title></g>')
    for n in (11, 17, 23):  # labelled: the worked example plus the two closest decisions
        x = test[n - 1][1]
        dx, dy = {11: (12, 4), 17: (8, -8), 23: (-30, 16)}[n]  # offsets keep the three labels apart
        o.append(f'<text x="{sx(x[2])+dx:.1f}" y="{sy(x[3])+dy:.1f}" fill="#0b0b0b" font-weight="600" font-size="10" stroke="#fcfcfb" stroke-width="3" paint-order="stroke">test {n}</text>')
    # outliers outside the plotted range: arrows at the edge
    tr = {n: x for n, x, _ in train}
    yr, xr = tr[91][3], tr[117][2]
    o.append(f'<text x="{W-R-4}" y="{sy(yr)-8:.1f}" text-anchor="end" fill="#0b0b0b">row 91 removed: C = 16.0 →</text>')
    o.append(f'<text x="{sx(xr)+6:.1f}" y="{T+12}" fill="#0b0b0b">↑ row 117 removed: D = 5.3</text>')
    # legend (empty upper-left region)
    lx, ly = L + 14, T + 14
    o.append(f'<rect x="{lx-8}" y="{ly-10}" width="230" height="132" fill="#fcfcfb" stroke="#e6e5e1"/>')
    for i, c in enumerate(CLASSES):
        yy = ly + 6 + i * 18
        o.append(mark(c, (lx + 6 - L) / (W - L - R) * (x1 - x0) + x0, y0 + (H - B - yy) / (H - T - B) * (y1 - y0), col[c]))
        o.append(f'<text x="{lx+18}" y="{yy+4}" fill="#0b0b0b">Class {c}</text>')
    o.append(f'<text x="{lx}" y="{ly+68}" fill="#52514e">filled = training, hollow = test</text>')
    o.append(f'<text x="{lx}" y="{ly+84}" fill="#52514e">(test drawn in predicted class)</text>')
    o.append(f'<text x="{lx}" y="{ly+100}" fill="#52514e">dashed ellipse = 2σ density contour</text>')
    o.append(f'<text x="{lx}" y="{ly+116}" fill="#52514e">✛ = class centroid (μ<tspan font-size="9">C</tspan>, μ<tspan font-size="9">D</tspan>)</text>')
    o.append('</svg>')
    return '\n'.join(o)


def write_figure(html_path):
    s = html_path.read_text(encoding='utf-8')
    a, b = '<!-- FIG1 START -->', '<!-- FIG1 END -->'
    i, j = s.index(a) + len(a), s.index(b)
    html_path.write_text(s[:i] + '\n' + figure_c_vs_d() + '\n' + s[j:], encoding='utf-8')

CONST = 2 * math.log(2 * math.pi)  # d/2 * ln(2*pi) for d = 4: the constant dropped in the reduced form


if __name__ == '__main__':
    write_figure(HERE / 'assignments-01-02-report.html')  # keeps Figure 1 in sync with the data
    f2 = lambda v: f'{v:.2f}'
    tv = {n: (x, y) for n, x, y in train}
    print('missing', missing, '\nfar-out', far, '\nmild kept', mild)
    print('class sizes', {c: model[c][0] for c in CLASSES},
          'resub', sum(conf.values()) - len(wrong), '/', sum(conf.values()), round(acc, 4),
          'loo', round(loo_acc, 4), 'dropped constant', round(CONST, 4))
    print('\n<!-- outliers -->')
    for n, f, c, v, lo, hi, med in far:
        j = FEATS.index(f)
        cls = [x[j] for _, x, y in clean if y == c]
        mu, sd = st.mean(cls), st.stdev(cls)
        vec = ', '.join(f'{t:g}' for t in tv[n][0])
        print(f'<tr><td>{n}</td><td>({vec})</td><td>{c}</td><td>{f} = {v:g}</td>'
              f'<td>{mu:.3f} ({sd:.3f})</td><td>{(v - mu) / sd:.1f}</td><td>[{f2(lo)}, {f2(hi)}]</td></tr>')
    print('\n<!-- mild -->')
    print(', '.join(f'row {n} ({f} = {v:g}, class {c}, z = {(v - st.mean([x[FEATS.index(f)] for _, x, y in clean if y == c])) / st.stdev([x[FEATS.index(f)] for _, x, y in clean if y == c]):.2f})'
                    for n, f, c, v, *_ in mild))
    print('\n<!-- params -->')
    for c in CLASSES:
        nc, n, mu, var = model[c]
        cells = ''.join(f'<td>{m:.4f}</td><td>{v:.4f}</td>' for m, v in zip(mu, var))
        print(f'<tr><th>{c}</th><td>{nc}/{n} = {nc/n:.4f}</td>{cells}</tr>')
    print('\n<!-- confusion -->')
    for t in CLASSES:
        print(f'<tr><th>{t}</th>' + ''.join(f'<td>{conf[(t, p)]}</td>' for p in CLASSES)
              + f'<td>{sum(conf[(t, p)] for p in CLASSES)}</td></tr>')
    print('<tr><th>all</th>' + ''.join(f'<td>{sum(conf[(t, p)] for t in CLASSES)}</td>' for p in CLASSES)
          + f'<td>{sum(conf.values())}</td></tr>')
    print('\n<!-- loo -->')
    for t in CLASSES:
        print(f'<tr><th>{t}</th>' + ''.join(f'<td>{conf_loo[(t, p)]}</td>' for p in CLASSES) + '</tr>')
    print(f'accuracy {sum(1 for t, p in loo if t == p)}/{len(loo)} = {loo_acc:.4f}')
    print('\n<!-- predictions -->')
    for n, x, p, gs in preds:
        print((f'<tr><td>{n}</td>' + ''.join(f'<td>{v}</td>' for v in x)
               + ''.join(f'<td>{gs[c]:.2f}</td>' for c in CLASSES) + f'<td><b>{p}</b></td>'
               + f'<td>{100 * post[n][p]:.1f}</td><td>{margin[n]:.2f}</td></tr>').replace('-', '−'))
    print('\n<!-- margins -->')
    for n in sorted(margin, key=lambda k: margin[k])[:6]:
        print(f'  test {n}: predicted {next(p for nn, _, p, _ in preds if nn == n)}, margin {margin[n]:.3f}, P = {100 * post[n][next(p for nn, _, p, _ in preds if nn == n)]:.1f}%')
    print('\n<!-- correlation A,C -->', f'pooled {r_ac:.3f}', {c: round(r_ac_cls[c], 3) for c in CLASSES})
    print('\n<!-- solution summary -->')
    for c in CLASSES:
        print(f'  class {c}:', ', '.join(str(n) for n, _, p, _ in preds if p == c))
    print('\n<!-- worked test 11 -->')
    x = test[10][1]
    for c in CLASSES:
        nc, n, mu, var = model[c]
        terms = [0.5 * math.log(2 * math.pi * var[j]) + (x[j] - mu[j]) ** 2 / (2 * var[j]) for j in range(4)]
        print(c, f'lnP={math.log(nc/n):.4f}', 'terms', [round(t, 4) for t in terms],
              f'g={g(model, c, x):.4f}', f'g_tilde={g(model, c, x) + CONST:.4f}',
              f'P={100 * post[11][c]:.2f}%')
    print('sum of terms class 3 =', round(sum(0.5 * math.log(2 * math.pi * model[3][3][j])
                                              + (x[j] - model[3][2][j]) ** 2 / (2 * model[3][3][j]) for j in range(4)), 4))

