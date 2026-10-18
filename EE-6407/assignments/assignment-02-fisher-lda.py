"""EE6407 Assignment 2: two-class Fisher linear discriminant, stdlib only.

Run from this directory:  python3 -I assignment-02-fisher-lda.py
Follows the Week 8 lecture convention (week-08-transcript.txt):
  S_i = sum (x - m_i)(x - m_i)^T (scatter, not divided by N_i),  S_W = S_1 + S_2,
  w = S_W^-1 (m_1 - m_2),  w0 = -w^T (m_1 + m_2) / 2,  g(x) = w^T x + w0 > 0 -> class 1.
Here class 1 = label +1 and class 2 = label -1 (the coding used in label_train.mat).
Prints the numbers and HTML fragments used in assignment-01-report-draft.html and refreshes Figure 2 there.
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
test = [(k + 1, x, g(x), label(x)) for k, x in enumerate(T)]
# Fisher criterion J(w) = (m1~ - m2~)^2 / (s1~^2 + s2~^2), projected means and scatters
J = lambda v: dot(v, dm) ** 2 / dot(v, [dot(r, v) for r in SW])

# self-checks: w really solves S_W w = m1 - m2; the midpoint lies on the boundary; w maximises J
assert len(X) == len(y) == 577 and len(T) == 23 and (len(C1), len(C2)) == (301, 276)
assert all(isinstance(v, float) and math.isfinite(v) for r in X + T for v in r)  # no missing values
assert max(abs(dot(r, w) - b) for r, b in zip(SW, dm)) < 1e-9
assert abs(g(mid)) < 1e-12 and g(m1) > 0 > g(m2)
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
        o.append(f'<text x="{sx(v):.1f}" y="{base+16}" text-anchor="middle" fill="#52514e">{v}</text>')
    for hs, c, pat in ((h2, -1, ''), (h1, 1, '')):
        for k, n in enumerate(hs):
            if n:
                x0 = sx(lo + k * bw)
                o.append(f'<rect x="{x0+0.5:.1f}" y="{sy(n):.1f}" width="{sx(lo+bw)-sx(lo)-1:.1f}" height="{base-sy(n):.1f}" '
                         f'fill="{col[c]}" fill-opacity="0.45" stroke="{col[c]}" stroke-width="1"/>')
    o.append(f'<line x1="{L}" y1="{base}" x2="{W-R}" y2="{base}" stroke="#52514e"/>')
    o.append(f'<line x1="{sx(0):.1f}" y1="{Tp}" x2="{sx(0):.1f}" y2="{base+30}" stroke="#0b0b0b" stroke-width="1.5" stroke-dasharray="5 4"/>')
    o.append(f'<text x="{sx(0)+5:.1f}" y="{Tp+10}" fill="#0b0b0b">g(x) = 0</text>')
    for n, x, gv, p in test:  # test samples as ticks in a strip under the axis
        o.append(f'<g><line x1="{sx(K*gv):.1f}" y1="{base+22}" x2="{sx(K*gv):.1f}" y2="{base+36}" stroke="{col[p]}" stroke-width="2"/>'
                 f'<title>Test {n}: g = {K*gv:.3f}×10⁻³, predicted {p:+d}</title></g>')
    o.append(f'<text x="{L}" y="{base+48}" fill="#52514e">test samples (tick colour = predicted class)</text>')
    o.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-4}" text-anchor="middle" fill="#0b0b0b">g(x) = wᵀx + w₀  (×10⁻³)</text>')
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
    print('N1, N2 =', len(C1), len(C2), ' train acc', round(acc, 4), ' errors', err1, err2, ' J(w)', round(J(w), 4))
    v4 = lambda v: '(' + ', '.join(f'{t:.4f}' for t in v) + ')'
    print('m1 =', v4(m1)); print('m2 =', v4(m2)); print('m1-m2 =', v4(dm))
    print('w  = 1e-3 *', vec(w)); print('w0 = 1e-3 *', f(w0)); print('|w| =', math.sqrt(dot(w, w)))
    print('\n<!-- SW -->')
    for r in SW:
        print('<tr>' + ''.join(f'<td>{v:.2f}</td>' for v in r) + '</tr>')
    print('\n<!-- test -->')
    for n, x, gv, p in test:
        print(f'<tr><td>{n}</td>' + ''.join(f'<td>{v:.3f}</td>' for v in x) + f'<td>{1e3 * gv:.3f}</td><td><b>{p:+d}</b></td></tr>')
    print('\nlabels:', ' '.join(f'{p:+d}' for *_, p in test))
    print('closest:', sorted(test, key=lambda t: abs(t[2]))[:3])
    if (HERE / 'assignment-01-report-draft.html').read_text(encoding='utf-8').count('<!-- FIG2 START -->'):
        write_figure(HERE / 'assignment-01-report-draft.html')
