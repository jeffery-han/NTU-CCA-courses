"""Recompute every numeric/choice answer in quiz2-prep-learning.html and check page structure.

Run: python3 quiz2-prep-learning-check.py   (needs numpy)
"""
import math
import re
from pathlib import Path

import numpy as np
from numpy.linalg import det, inv

M = np.array


def zoh(A, B, T, n=4000):
    """Phi(T)=expm(AT); Theta=int_0^T Phi dtau B via augmented-matrix exponential."""
    k = A.shape[0]
    aug = np.zeros((k + 1, k + 1))
    aug[:k, :k], aug[:k, k:] = A * T, B * T
    E = expm(aug)
    return E[:k, :k], E[:k, k:]


def expm(X, terms=60):
    out, term = np.eye(len(X)), np.eye(len(X))
    for i in range(1, terms):
        term = term @ X / i
        out = out + term
    return out


def ack(A, B, coeffs):
    """K = [0..1] Wc^-1 alpha(A); coeffs = alpha polynomial, highest power first."""
    n = A.shape[0]
    W = np.hstack([np.linalg.matrix_power(A, i) @ B for i in range(n)])
    aA = sum(c * np.linalg.matrix_power(A, n - i) for i, c in enumerate(coeffs))
    return (inv(W)[-1] @ aA).ravel()


def step(A, B, x, u):
    return A @ x + B.ravel() * u


exp = {}
# M0
exp['m0-1'] = det(M([[3, 1], [2, 4]]))
exp['m0-2'] = inv(M([[2, 1], [1, 1]]))[1, 1]
exp['m0-3'] = np.linalg.matrix_rank(M([[1, 2], [2, 4]]))
exp['m0-4'] = max(np.linalg.eigvals(M([[0, 1], [-6, -5]])).real)
# M1
exp['m1-1'], exp['m1-2'], exp['m1-3'] = -9 / 3, -12 / 3, 6 / 3
A1 = M([[0.5, 0], [1, -0.25]])  # discrete diagram
exp['m1-4'] = A1[1, 1]
exp['m1-5'] = -2 * 3
A, B, C = M([[0, 1], [-2, -3]]), M([[0], [2]]), M([[1, 0]])
exp['m1-6'] = (C @ inv(-A) @ B).item()
exp['m1-7'] = min(np.linalg.eigvals(A).real)
# block diagram worked example consistency: closed-loop char poly s^2+4s+6
assert np.allclose(np.poly(M([[0, 1], [-6, -4]])), [1, 4, 6])
# M2
exp['m2-1'] = math.exp(-1.5)
exp['m2-2'] = expm(M([[0, 1], [0, 0]]) * 2)[0, 1]
exp['m2-3'] = expm(M([[0, 1], [0, -2]]) * 1)[0, 1]
# M3
P, Th = zoh(M([[0, 1], [0, -1.0]]), M([[0], [1.0]]), 0.2)
exp['m3-1'], exp['m3-2'], exp['m3-3'], exp['m3-4'] = P[0, 1], P[1, 1], Th[0, 0], Th[1, 0]
P, Th = zoh(M([[0, 1], [0, 0.0]]), M([[0], [1.0]]), 0.5)
exp['m3-5'] = Th[0, 0]
# lecture servo T=0.1 and worked T=0.5 example
P, Th = zoh(M([[0, 1], [0, -1.0]]), M([[0], [1.0]]), 0.1)
assert np.allclose([P[0, 1], P[1, 1], Th[0, 0], Th[1, 0]], [0.0952, 0.905, 0.00484, 0.0952], atol=6e-4)
P5, Th5 = zoh(M([[0, 1], [0, -2.0]]), M([[0], [2.0]]), 0.5)
assert np.allclose([P5[0, 1], P5[1, 1], Th5[0, 0], Th5[1, 0]], [0.3161, 0.3679, 0.1839, 0.6321], atol=1e-4)
# M4
exp['m4-1'] = max(np.linalg.eigvals(M([[0.5, 1], [0, 0.2]])).real)
A4, B4, C4 = M([[0, 1], [-0.5, 1]]), M([[0], [1]]), M([[1, 0]])
exp['m4-2'] = abs(np.linalg.eigvals(A4)[0])
exp['m4-3'] = (C4 @ inv(np.eye(2) - A4) @ B4).item()
# zero of worked M3 system: C adj(zI-P) Th = 0
num = np.polyadd(np.polymul([Th5[0, 0]], [1, -P5[1, 1]]), [P5[0, 1] * Th5[1, 0]])
exp['m4-4'] = np.roots(num)[0]
exp['m4-5'] = -1
# M5
A, B = M([[0.5, 1], [0, -0.5]]), M([[1], [0]])
x1 = step(A, B, M([1.0, 2.0]), 1)
x2 = step(A, B, x1, 0)
exp['m5-1'], exp['m5-2'], exp['m5-3'] = x1[0], x2[0], x2[1]
xw = step(M([[0, 1], [-0.5, 1]]), M([[0], [1]]), step(M([[0, 1], [-0.5, 1]]), M([[0], [1]]), M([1.0, 0]), 2), -1)
assert np.allclose(xw, [1.5, 0.5])
# M6
exp['m6-1'], exp['m6-2'], exp['m6-3'], exp['m6-4'] = 0.12, -0.4, -1, 1.5
A, B = np.diag([0.2, 0.6]), M([[1], [1]])
a1 = -np.trace(A)
Wc = np.hstack([B, A @ B])
Pm = Wc @ M([[a1, 1], [1, 0]])
exp['m6-5'] = Pm[0, 0]
A, B = np.diag([0.5, 0.8]), M([[1], [1]])
Pm = np.hstack([B, A @ B]) @ M([[-1.3, 1], [1, 0]])
assert np.allclose(Pm, [[-0.8, 1], [-0.5, 1]]) and np.allclose(inv(Pm) @ A @ Pm, [[0, 1], [-0.4, 1.3]])
# M7
A, B = np.diag([0.5, 0.5]), M([[1], [2]])
exp['m7-1'] = np.linalg.matrix_rank(np.hstack([B, A @ B]))
A, B = M([[0, 1], [-0.5, 1]]), M([[0], [1]])
u = np.linalg.solve(np.hstack([A @ B, B]), [1, 0])  # [u0, u1]
exp['m7-2'], exp['m7-3'] = u
beta = 0.4
assert abs(det(np.hstack([M([[1], [1]]), M([[0.2, beta], [0, 0.6]]) @ M([[1], [1]])]))) < 1e-12
exp['m7-4'] = beta
# M8
Wo = np.vstack([M([[0, 1]]), M([[0, 1]]) @ M([[0.5, 1], [0, 0.25]])])
assert abs(det(Wo)) < 1e-12
A, B, C = M([[0, 1], [-0.5, 1]]), M([[1], [0]]), M([[1, 0]])
Wo = np.vstack([C, C @ A])
x0 = np.linalg.solve(Wo, [2, -1 - (C @ B).item() * 1])
exp['m8-2'] = x0[1]
exp['m8-3'] = math.pi / 2
# M9
k = ack(M([[0, 1], [-0.3, 1.2]]), M([[0], [1]]), [1, -0.9, 0.2])
exp['m9-1'], exp['m9-2'] = k
k = ack(M([[1, 1], [0, 1.0]]), M([[0.5], [1]]), [1, -1, 0.25])
exp['m9-3'], exp['m9-4'] = k
assert np.allclose(ack(M([[0, 1], [-0.5, 1.5]]), M([[0], [1]]), [1, -0.5, 0.06]), [-0.44, 1])
assert np.allclose(ack(M([[1, 0.5], [0, 1]]), M([[0.125], [0.5]]), [1, -1, 0.25]), [1, 1.75])
assert np.allclose(ack(M([[1, 0.0952], [0, 0.905]]), M([[0.00484], [0.0952]]), [1, -1.776, 0.819]), [4.52, 1.12], atol=0.01)
# M10
A, B = M([[1, 0.5], [0, 2.0]]), M([[1], [1.0]])
k = ack(A, B, [1, 0, 0])
exp['m10-1'], exp['m10-2'] = k
x0 = M([2.0, 0])
exp['m10-3'] = ((A - B @ k[None]) @ x0)[0]
exp['m10-4'] = -k @ x0
exp['m10-5'] = 3 * 0.2
exp['m10-6'] = -(1 / 0.5**2 + 3 / (2 * 0.5))
A, B = M([[1, 1], [0, 0.5]]), M([[0], [1.0]])
k = ack(A, B, [1, 0, 0])
Acl = A - B @ k[None]
assert np.allclose(k, [1, 1.5]) and np.allclose(Acl @ M([1, 1.0]), [2, -2]) and np.allclose(Acl @ Acl, 0)
for T in (2, 1, 0.5):  # Ex 3.12 table
    A, B = M([[1, T], [0, 1]]), M([[T * T / 2], [T]])
    k = ack(A, B, [1, 0, 0])
    assert np.allclose(k, [1 / T**2, 3 / (2 * T)])
# M11 drill
exp['d1-1'] = -2 / 4
exp['d1-2'] = 8 / 4
g, T = 2.0, math.log(2)
P, Th = zoh(M([[-1, g], [0, -2]]), M([[0], [1.0]]), T)
exp['d2-1'], exp['d2-2'] = P[0, 1], Th[0, 0]
exp['d2-3'] = det(np.hstack([Th, P @ Th]))
num = np.polyadd(np.polymul([Th[0, 0]], [1, -P[1, 1]]), [P[0, 1] * Th[1, 0]])
exp['d2-4'] = np.roots(num)[0]
k = ack(P, Th, [1, 0, 0])
exp['d3-1'], exp['d3-2'] = k
x0 = M([1.0, 1.0])
exp['d3-3'] = -k @ x0
x1 = (P - Th @ k[None]) @ x0
exp['d3-4'], exp['d3-5'] = x1
assert np.allclose((P - Th @ k[None]) @ x1, 0)

# ---- compare against the page ----
html = Path(__file__).with_name('quiz2-prep-learning.html').read_text()
page = dict(re.findall(r'data-id="([\w-]+)" data-answer="([^"]+)"', html))
choices = re.findall(r'data-id="([\w-]+)" data-choice="(\d+)"', html)
assert set(page) == set(exp), (set(page) ^ set(exp))
bad = [(i, float(v), exp[i]) for i, v in page.items() if abs(float(v) - exp[i]) > max(0.002 * abs(exp[i]), 1e-5)]
assert not bad, bad
for i, c in choices:  # each choice index must point at an existing option
    block = html.split(f'data-id="{i}"')[1].split('</ol>')[0]
    assert int(c) < block.count('<li>'), i
sections = re.split(r'<section class="module', html)[1:]
assert len(sections) == 12 and all('class="q"' in s for s in sections), 'every module needs exercises'
print(f'OK: {len(page)} numeric + {len(choices)} choice answers verified across {len(sections)} modules')
