"""EE6407 Assignment 2: two-class Fisher linear discriminant, stdlib only.

Run from this directory:  python3 -I assignment-02-fisher-lda.py
Follows the Week 8 lecture convention (week-08-transcript.txt):
  S_i = sum (x - m_i)(x - m_i)^T (scatter, not divided by N_i),  S_W = S_1 + S_2,
  w = S_W^-1 (m_1 - m_2),  w0 = -w^T (m_1 + m_2) / 2,  g(x) = w^T x + w0 > 0 -> class 1.
Here class 1 = label +1 and class 2 = label -1 (the coding used in label_train.mat).
Prints the numbers and HTML fragments used in assignments-01-02-report.html and refreshes Figure 2 there.
"""
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # so `python3 -I` still finds the sibling reader
from mat_reader import read

X = read(HERE / 'assignment-02-data-train.mat')['data_train']
y = [int(r[0]) for r in read(HERE / 'assignment-02-label-train.mat')['label_train']]
T = read(HERE / 'assignment-02-data-test.mat')['data_test']
d = len(X[0])

dot = lambda a, b: sum(p * q for p, q in zip(a, b))


def mean(rows):
    return [sum(c) / len(rows) for c in zip(*rows)]


def scatter(rows, m):
    return [[sum((r[i] - m[i]) * (r[j] - m[j]) for r in rows) for j in range(d)] for i in range(d)]


def solve(A, b):
    """Gauss-Jordan with partial pivoting: returns x with A x = b."""
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * e for a, e in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


C1 = [x for x, t in zip(X, y) if t == 1]
C2 = [x for x, t in zip(X, y) if t == -1]
m1, m2 = mean(C1), mean(C2)
S1, S2 = scatter(C1, m1), scatter(C2, m2)
SW = [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(S1, S2)]
dm = [a - b for a, b in zip(m1, m2)]
w = solve(SW, dm)
mid = [(a + b) / 2 for a, b in zip(m1, m2)]
w0 = -dot(w, mid)
g = lambda x: dot(w, x) + w0
label = lambda x: 1 if g(x) > 0 else -1

train_pred = [label(x) for x in X]
acc = sum(p == t for p, t in zip(train_pred, y)) / len(y)
err1 = sum(1 for x in C1 if label(x) != 1)
err2 = sum(1 for x in C2 if label(x) != -1)
conf = {(t, p): sum(1 for x, t2 in zip(X, y) if t2 == t and label(x) == p) for t in (1, -1) for p in (1, -1)}
test = [(k + 1, x, g(x), label(x)) for k, x in enumerate(T)]
# Fisher criterion J(w) = (m1~ - m2~)^2 / (s1~^2 + s2~^2), projected means and scatters
J = lambda v: dot(v, dm) ** 2 / dot(v, [dot(r, v) for r in SW])
mt1, mt2 = dot(w, m1), dot(w, m2)                      # projected class means
s1 = sum((dot(w, x) - mt1) ** 2 for x in C1)           # projected within-class scatter
s2 = sum((dot(w, x) - mt2) ** 2 for x in C2)
sp = ((len(C1) - 1) * s1 / (len(C1) - 1) + (len(C2) - 1) * s2 / (len(C2) - 1)) / (len(X) - 2)  # pooled projected variance
nw = math.sqrt(dot(w, w))

# Three conventions for the bias, all with the same direction w
w0_cnt = -(len(C1) * mt1 + len(C2) * mt2) / len(X)                     # sample-size-weighted midpoint
w0_bayes = -(mt1 + mt2) / 2 + sp * math.log(len(C1) / len(C2)) / (mt1 - mt2)  # 1-D Gaussian Bayes threshold
thresh = {'midpoint of the two means': w0, 'sample-size-weighted mean': w0_cnt, 'Bayes-optimal (equal variance)': w0_bayes}
labels_under = {k: [1 if dot(w, x) + v > 0 else -1 for x in T] for k, v in thresh.items()}

# leave-one-out: refit direction AND bias without each sample
def split_fit(rows, labs):
    a = [x for x, t in zip(rows, labs) if t == 1]
    b = [x for x, t in zip(rows, labs) if t == -1]
    ma, mb = mean(a), mean(b)
    sw = [[u + v for u, v in zip(r1, r2)] for r1, r2 in zip(scatter(a, ma), scatter(b, mb))]
    wv = solve(sw, [u - v for u, v in zip(ma, mb)])
    return wv, -dot(wv, [(u + v) / 2 for u, v in zip(ma, mb)])

loo = []
for i in range(len(X)):
    wv, b = split_fit(X[:i] + X[i + 1:], y[:i] + y[i + 1:])
    loo.append((y[i], 1 if dot(wv, X[i]) + b > 0 else -1))
conf_loo = {(t, p): sum(1 for tt, pp in loo if tt == t and pp == p) for t in (1, -1) for p in (1, -1)}
loo_acc = sum(1 for t, p in loo if t == p) / len(loo)


# self-checks: w really solves S_W w = m1 - m2; the midpoint lies on the boundary; w maximises J
assert len(X) == len(y) == 577 and len(T) == 23 and (len(C1), len(C2)) == (301, 276)
assert all(isinstance(v, float) and math.isfinite(v) for r in X + T for v in r)  # no missing values
assert max(abs(dot(r, w) - b) for r, b in zip(SW, dm)) < 1e-9
assert abs(g(mid)) < 1e-12 and g(m1) > 0 > g(m2)
# self-check: reported counts, alternative thresholds, and LOO figure
assert (conf[(1, 1)], conf[(1, -1)], conf[(-1, 1)], conf[(-1, -1)]) == (288, 13, 26, 250)
assert abs(acc - 538 / 577) < 1e-12 and abs(loo_acc - 537 / 577) < 1e-12
assert len({tuple(v) for v in labels_under.values()}) == 1          # every bias convention agrees on the test set
assert min(abs(t[2]) for t in test) > max(abs(v - w0) for v in thresh.values())

for i in range(d):  # any small perturbation of w lowers the Fisher ratio
    for s in (1e-3, -1e-3):
        v = w[:]; v[i] += s * math.sqrt(dot(w, w))
        assert J(v) < J(w)


def figure_projection():
    """Inline SVG: histograms of g(x) for each training class, test samples as ticks below, boundary g = 0."""
    W, H, L, R, Tp, B = 640, 300, 46, 16, 14, 64
    K = 1e3  # plot g in units of 10^-3
    gs1, gs2 = [K * g(x) for x in C1], [K * g(x) for x in C2]
    lo = 5 * math.floor(min(gs1 + gs2) / 5)
    hi = 5 * math.ceil(max(gs1 + gs2) / 5)
    bw = 1.0
    nb = int(round((hi - lo) / bw))
    hist = lambda vs: [sum(1 for v in vs if lo + k * bw <= v < lo + (k + 1) * bw) for k in range(nb)]
    h1, h2 = hist(gs1), hist(gs2)
    ymax = max(h1 + h2)
    ytop = 5 * math.ceil(ymax / 5)
    sx = lambda v: L + (v - lo) / (hi - lo) * (W - L - R)
    base = H - B
    sy = lambda c: base - c / ytop * (base - Tp)
    col = {1: '#2a78d6', -1: '#eb6834'}
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="fig2cap" font-family="system-ui, sans-serif" font-size="11">',
         f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>']
    for c in range(0, ytop + 1, 5 if ytop <= 40 else 10):
        o.append(f'<line x1="{L}" y1="{sy(c):.1f}" x2="{W-R}" y2="{sy(c):.1f}" stroke="#e6e5e1"/>')
        o.append(f'<text x="{L-6}" y="{sy(c)+4:.1f}" text-anchor="end" fill="#52514e">{c}</text>')
    for v in range(lo, hi + 1, 5):
        lbl = str(v).replace('-', '−')  # proper minus sign, not a hyphen
        o.append(f'<text x="{sx(v):.1f}" y="{base+16}" text-anchor="middle" fill="#52514e">{lbl}</text>')
    for hs, c, pat in ((h2, -1, ''), (h1, 1, '')):
        for k, n in enumerate(hs):
            if n:
                x0 = sx(lo + k * bw)
                o.append(f'<rect x="{x0+0.5:.1f}" y="{sy(n):.1f}" width="{sx(lo+bw)-sx(lo)-1:.1f}" height="{base-sy(n):.1f}" '
                         f'fill="{col[c]}" fill-opacity="0.45" stroke="{col[c]}" stroke-width="1"/>')
    # fitted 1-D Gaussians of the projected values, drawn on the histogram scale (counts per bin)
    for cls, sc, c in ((C1, s1, 1), (C2, s2, -1)):
        m_, sd_ = (mt1, math.sqrt(s1 / (len(C1) - 1))) if c == 1 else (mt2, math.sqrt(s2 / (len(C2) - 1)))
        pts = []
        for k in range(181):
            v = lo + (hi - lo) * k / 180
            dens = math.exp(-((v - K * m_) ** 2) / (2 * (K * sd_) ** 2)) / (K * sd_ * math.sqrt(2 * math.pi))
            pts.append(f'{sx(v):.1f},{sy(len(cls) * bw * dens):.1f}')
        o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col[c]}" stroke-width="1.6"/>')

    o.append(f'<line x1="{L}" y1="{base}" x2="{W-R}" y2="{base}" stroke="#52514e"/>')
    o.append(f'<line x1="{sx(0):.1f}" y1="{Tp}" x2="{sx(0):.1f}" y2="{base+30}" stroke="#0b0b0b" stroke-width="1.5" stroke-dasharray="5 4"/>')
    o.append(f'<text x="{sx(0)+5:.1f}" y="{Tp+10}" fill="#0b0b0b">g(x) = 0</text>')
    for m_, c, tag in ((mt1, 1, 'm̃₁'), (mt2, -1, 'm̃₂')):
        xm = sx(K * m_)
        o.append(f'<line x1="{xm:.1f}" y1="{Tp+18}" x2="{xm:.1f}" y2="{base}" stroke="{col[c]}" '
                 f'stroke-width="1.2" stroke-dasharray="2 3"/>')
        o.append(f'<text x="{xm + (5 if c == 1 else -5):.1f}" y="{Tp+30}" '
                 f'text-anchor="{"start" if c == 1 else "end"}" fill="{col[c]}">{tag} = {K*m_:+.2f}</text>')
    for n, x, gv, p in test:  # test samples as ticks in a strip under the axis
        o.append(f'<g><line x1="{sx(K*gv):.1f}" y1="{base+22}" x2="{sx(K*gv):.1f}" y2="{base+36}" stroke="{col[p]}" stroke-width="2"/>'
                 f'<title>Test {n}: g = {K*gv:.3f}×10⁻³, predicted {p:+d}</title></g>')
    o.append(f'<text x="{L}" y="{base+48}" fill="#52514e">test samples (tick colour = predicted class)</text>')
    o.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-4}" text-anchor="middle" fill="#0b0b0b">g(x) = (wᵀx + w₀) × 10³</text>')
    o.append(f'<text transform="translate(12,{(Tp+base)/2:.0f}) rotate(-90)" text-anchor="middle" fill="#0b0b0b">Training samples</text>')
    lx, ly = W - R - 150, Tp + 8
    o.append(f'<rect x="{lx-8}" y="{ly-6}" width="150" height="44" fill="#fcfcfb" stroke="#e6e5e1"/>')
    for i, (c, txt) in enumerate(((1, 'Class 1 (label +1)'), (-1, 'Class 2 (label −1)'))):
        o.append(f'<rect x="{lx}" y="{ly+i*18}" width="12" height="10" fill="{col[c]}" fill-opacity="0.45" stroke="{col[c]}"/>')
        o.append(f'<text x="{lx+18}" y="{ly+i*18+9}" fill="#0b0b0b">{txt}</text>')
    o.append('</svg>')
    return '\n'.join(o)


def write_figure(html_path):
    s = html_path.read_text(encoding='utf-8')
    a, b = '<!-- FIG2 START -->', '<!-- FIG2 END -->'
    i, j = s.index(a) + len(a), s.index(b)
    html_path.write_text(s[:i] + '\n' + figure_projection() + '\n' + s[j:], encoding='utf-8')


if __name__ == '__main__':
    f = lambda v: f'{1e3 * v:.4f}'  # vectors printed in units of 10^-3 where noted
    vec = lambda v: '(' + ', '.join(f(t) for t in v) + ')'
    print('N1, N2 =', len(C1), len(C2), ' resub', 538, '/', 577, round(acc, 4), ' LOO', round(loo_acc, 4),
          ' errors', err1, err2, ' J(w)', round(J(w), 6))
    print('projected means x1e3', round(1e3 * mt1, 4), round(1e3 * mt2, 4),
          ' sds x1e3', round(1e3 * math.sqrt(s1 / (len(C1) - 1)), 4), round(1e3 * math.sqrt(s2 / (len(C2) - 1)), 4),
          ' |w|', round(nw, 8))
    print('test distance to boundary', round(min(abs(t[2]) for t in test) / nw, 4),
          round(max(abs(t[2]) for t in test) / nw, 4))
    v4 = lambda v: '(' + ', '.join(f'{t:.4f}' for t in v) + ')'
    print('m1 =', v4(m1)); print('m2 =', v4(m2)); print('m1-m2 =', v4(dm))
    print('w  = 1e-3 *', vec(w)); print('w0 = 1e-3 *', f(w0))
    print('w*575 =', vec([575 * t for t in w]), ' w0*575 =', f(575 * w0))
    print('w/|w| =', '(%.4f, %.4f, %.4f, %.4f, %.4f)' % tuple(t / nw for t in w), ' w0/|w| =', round(w0 / nw, 4))
    print('\n<!-- SW -->')
    for r in SW:
        print(('<tr>' + ''.join(f'<td>{v:.2f}</td>' for v in r) + '</tr>').replace('-', '−'))
    print('\n<!-- confusion -->')
    for t in (1, -1):
        print(f'<tr><th>{t:+d}</th>' + ''.join(f'<td>{conf[(t, p)]}</td>' for p in (1, -1)) + '</tr>')
    print('\n<!-- loo -->')
    for t in (1, -1):
        print(f'<tr><th>{t:+d}</th>' + ''.join(f'<td>{conf_loo[(t, p)]}</td>' for p in (1, -1)) + '</tr>')
    print(f'<!-- loo acc --> {sum(1 for t, p in loo if t == p)}/{len(loo)} = {loo_acc:.4f}')
    print('\n<!-- thresholds -->')
    for k, v in thresh.items():
        same = 'yes' if labels_under[k] == labels_under['midpoint of the two means'] else 'NO'
        print((f'<tr><td>{k}</td><td>{1e3 * v:.4f}</td><td>{same}</td></tr>').replace('-', '−'))
    print(1e3 * thresh['Bayes-optimal (equal variance)'] - 1e3 * w0)
    print('\n<!-- scalings -->')
    print(('<tr><td>S<sub>W</sub> (scatter, as computed)</td><td>' + vec(w) + '</td><td>' + f(w0) + '</td><td>10<sup>−3</sup></td></tr>').replace('-', '−'))
    print(('<tr><td>Σ<sub>W</sub> = S<sub>W</sub>/575 (pooled covariance)</td><td>' + vec([575 * t for t in w]) + '</td><td>' + f(575 * w0) + '</td><td>—</td></tr>').replace('-', '−'))
    print(('<tr><td>unit vector</td><td>' + '(%.4f, %.4f, %.4f, %.4f, %.4f)' % tuple(t / nw for t in w) + '</td><td>' + f'{w0 / nw:.4f}' + '</td><td>—</td></tr>').replace('-', '−'))
    print('\n<!-- test -->')
    for n, x, gv, p in test:
        print((f'<tr><td>{n}</td>' + ''.join(f'<td>{v:.3f}</td>' for v in x) + f'<td>{1e3 * gv:.3f}</td><td><b>{p:+d}</b></td></tr>').replace('-', '−'))
    print('\nlabels:', ' '.join(f'{p:+d}' for *_, p in test))
    print('closest:', sorted(test, key=lambda t: abs(t[2]))[:3])
    if (HERE / 'assignments-01-02-report.html').read_text(encoding='utf-8').count('<!-- FIG2 START -->'):
        write_figure(HERE / 'assignments-01-02-report.html')
