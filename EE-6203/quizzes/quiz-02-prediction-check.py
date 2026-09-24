"""Independent numerical check of every key in quiz-02-prediction-paper.md.

Run: python3 quiz-02-prediction-check.py   (numpy only; exits non-zero on any mismatch)
Conventions follow LPH Lect 1-3: x(k+1)=Phi x+Theta u, u=-Kx, Ackermann K=[0..1]Wc^-1 alpha(A).
"""
import numpy as np

close = np.allclose

# (a) ZOH discretisation, T = ln 2
Ac = np.array([[-1.0, 1.0], [0.0, -2.0]])
Bc = np.array([[0.0], [1.0]])
C = np.array([[1.0, 0.0]])
T = np.log(2)


def expm(M, t):
    w, V = np.linalg.eig(M)          # Ac has distinct real eigenvalues
    return (V @ np.diag(np.exp(w * t)) @ np.linalg.inv(V)).real


Phi = expm(Ac, T)
n = 20000                             # Simpson's rule for Theta(T) = int_0^T Phi(eta) d eta B
eta = np.linspace(0, T, n + 1)
wts = np.ones(n + 1); wts[1:-1:2] = 4; wts[2:-1:2] = 2
Theta = sum(w * expm(Ac, e) @ Bc for w, e in zip(wts, eta)) * (T / n) / 3

assert close(Phi, [[1/2, 1/4], [0, 1/4]]), Phi
assert close(Theta, [[1/8], [3/8]]), Theta
assert close(sorted(np.linalg.eigvals(Phi)), [1/4, 1/2])

# (b) G(z) = C (zI - Phi)^-1 Theta  ==  (2z+1) / (16 (z-1/2)(z-1/4))
for z in (2.0, -3.0, 0.9 + 0.7j):
    lhs = (C @ np.linalg.inv(z * np.eye(2) - Phi) @ Theta)[0, 0]
    rhs = (2 * z + 1) / (16 * (z - 0.5) * (z - 0.25))
    assert close(lhs, rhs), (z, lhs, rhs)
assert close(3 / (16 * 0.5 * 0.75), (-C @ np.linalg.inv(Ac) @ Bc)[0, 0])   # ZOH keeps DC gain 1/2

# (c) controllability and deadbeat gain
Wc = np.hstack([Theta, Phi @ Theta])
assert close(Wc, [[1/8, 5/32], [3/8, 3/32]])
assert close(np.linalg.det(Wc), -3/64)
assert close(np.linalg.inv(Wc), [[-2, 10/3], [8, -8/3]])
K = np.array([[0.0, 1.0]]) @ np.linalg.inv(Wc) @ (Phi @ Phi)
assert close(K, [[2, 4/3]]), K
Acl = Phi - Theta @ K
assert close(Acl, [[1/4, 1/12], [-3/4, -1/4]])
assert close(Acl @ Acl, np.zeros((2, 2)))          # deadbeat: (Phi - Theta K)^2 = 0
x0 = np.array([[1.0], [0.0]])
x1 = Acl @ x0; x2 = Acl @ x1
assert close(x1, [[1/4], [-3/4]]) and close(x2, 0)

# (d) CCF by inspection of G(z) = (z - 0.5) / (z^2 - 0.3 z - 0.1)
assert close(np.polymul([1, -0.5], [1, 0.2]), [1, -0.3, -0.1])
Ad = np.array([[0.0, 1.0], [0.1, 0.3]])
Bd = np.array([[0.0], [1.0]])
Cd = np.array([[-0.5, 1.0]])
assert close(np.poly(Ad), [1, -0.3, -0.1])
Wo = np.vstack([Cd, Cd @ Ad])
assert close(Wo, [[-0.5, 1], [0.1, -0.2]])
assert np.linalg.matrix_rank(Wo) == 1                              # unobservable
assert np.linalg.matrix_rank(np.hstack([Bd, Ad @ Bd])) == 2        # controllable
for z in (2.0, -1.5):
    g = (Cd @ np.linalg.inv(z * np.eye(2) - Ad) @ Bd)[0, 0]
    assert close(g, 1 / (z + 0.2))                                 # cancelled to first order
# the unobservable mode is the cancelled pole z = 0.5: Wo v = 0 for its eigenvector
w, V = np.linalg.eig(Ad)
v = V[:, np.argmin(abs(w - 0.5))]
assert close(Wo @ v, 0)

print("all Quiz 2 prediction keys verified")
