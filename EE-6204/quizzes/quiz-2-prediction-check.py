"""Independent derivation of every key in quiz-2-prediction.md.

Run:  python3 quiz-2-prediction-check.py
Exact arithmetic (Fraction) wherever the answer is rational; floats only for e^x.
Every printed value is what the learner should key in, already in the stated format.
"""
from fractions import Fraction as F
from math import exp, factorial


def r(x, dp):
    # Standard half-up rounding at the very end (never on intermediates).
    from decimal import Decimal, ROUND_HALF_UP
    return str(Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP))


def solve_pi(P):
    """Stationary vector of a 3x3 stochastic (DTMC) matrix, exact if entries are Fractions."""
    # pi (P - I) = 0 with sum = 1: replace last equation by normalisation, Gaussian elimination.
    n = len(P)
    A = [[P[j][i] - (1 if i == j else 0) for j in range(n)] for i in range(n)]
    A[-1] = [1] * n
    b = [0] * (n - 1) + [1]
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        p = next(k for k in range(c, n) if M[k][c] != 0)
        M[c], M[p] = M[p], M[c]
        M[c] = [v / M[c][c] for v in M[c]]
        for k in range(n):
            if k != c:
                M[k] = [a - M[k][c] * bc for a, bc in zip(M[k], M[c])]
    return [M[i][n] for i in range(n)]


key = {}

# ---------------- Q1  Poisson / exponential / geometric ----------------
lam = 3 + 2                      # superposition, calls per hour
m = lam * 0.5                    # 30 minutes
key['1a'] = r(exp(-m) * m**2 / 2, 4)
key['1b'] = str(F(3, 5))
key['1c'] = r(exp(-lam * F(15, 60)), 4)          # memoryless: only the 15 new minutes matter
key['1d'] = r(0.98**50, 4)                        # P(X>75 | X>25) = P(X>50) = (1-p)^50
key['1e'] = str(int(1 / F(2, 100)))               # E(X) = 1/p
key['1f'] = 'C'                                   # continuous observation, countable state
key['1g'] = 'C'                                   # P(T_i = n) = p_ii^(n-1) (1 - p_ii)

# ---------------- Q2  (s,S) inventory DTMC, weekly demand Poisson(0.5) ----------------
mu = 0.5
d0, d1 = exp(-mu), mu * exp(-mu)
d2p = 1 - d0 - d1
# state = stock at END of week; 0 is restocked to 2 before Monday, so rows 0 and 2 coincide
P = [[d2p, d1, d0],
     [1 - d0, d0, 0.0],
     [d2p, d1, d0]]
assert all(abs(sum(row) - 1) < 1e-12 for row in P)
key['2a'] = r(P[0][1], 4)
key['2b'] = r(P[1][0], 4)
key['2c'] = r(1 / (1 - P[1][1]), 4)               # mean sojourn = 1/(1-p11) weeks
P2 = [[sum(P[i][k] * P[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
key['2d'] = r(P2[2][0], 6)
pi = solve_pi(P)
assert abs(sum(pi) - 1) < 1e-12 and all(v >= 0 for v in pi)
key['2e'] = r(pi[0], 6)
key['2f'] = r(0 * pi[0] + 1 * pi[1] + 2 * pi[2], 4)

# ---------------- Q3  machine CTMC (fails in setup AND processing; discard after repair) ----------------
s, p, f, rr = F(6), F(3), F(1, 2), F(2)
Q = [[-(s + f), s, f],
     [p, -(p + f), f],
     [rr, F(0), -rr]]
assert all(sum(row) == 0 for row in Q)
# pi Q = 0 with sum 1  <=>  stationary vector of the uniformised chain I + Q/c
c = 10
Pu = [[(1 if i == j else 0) + Q[i][j] / c for j in range(3)] for i in range(3)]
piq = solve_pi(Pu)
assert sum(piq) == 1 and all(sum(piq[i] * Q[i][j] for i in range(3)) == 0 for j in range(3))
key['3a'] = r(Q[0][0], 1)
key['3b'] = r(60 / (p + f), 2)                    # minutes
key['3c'] = str(piq[0])
key['3d'] = r(p * piq[1], 6)                      # R = p * pi1 parts per hour
key['3e'] = str(piq[2])

# ---------------- Q4  queue design comparison, lambda = 9/h ----------------
lam = F(9)
# A: M/M/1, mu = 12/h
muA = F(12)
WA = 1 / (muA - lam)
key['4a'] = r(WA * 60, 2)
# B: M/M/2, mu = 6/h each
mB, muB = 2, F(6)
rho = lam / (mB * muB)
pi0 = 1 / ((mB * rho) ** mB / (factorial(mB) * (1 - rho)) + sum((mB * rho) ** k / factorial(k) for k in range(mB)))
QB = rho * (mB * rho) ** mB * pi0 / (factorial(mB) * (1 - rho) ** 2)
LB = QB + lam / muB
key['4b'] = str(pi0)
key['4c'] = r(LB, 4)
# C: M/M/1/3, mu = 12/h
N, rho = 3, lam / muA
piN = rho**N * (1 - rho) / (1 - rho ** (N + 1))
LC = rho * (1 - rho**N - N * rho**N * (1 - rho)) / ((1 - rho) * (1 - rho ** (N + 1)))
# cross-check L_C from the distribution itself
dist = [rho**k * (1 - rho) / (1 - rho ** (N + 1)) for k in range(N + 1)]
assert sum(dist) == 1 and sum(k * d for k, d in enumerate(dist)) == LC
key['4d'] = str(piN)
key['4e'] = r(LC, 6)
# D: M^b/M/1, batches of 3 at 3 batches/h, mu = 12/h
b, lb = 3, F(3)
rho = b * lb / muA
WD = (1 + b) / (2 * muA * (1 - rho))
assert WD == (rho * (1 + b) / (2 * (1 - rho))) / (lb * b)   # W = L/(lambda b)
key['4f'] = r(WD * 60, 2)
# A again: FIFO queueing-delay tail, P(d > t) = rho e^{-mu(1-rho)t} (lecture-02 p13-14; NOT on the appendix)
rhoA = lam / muA
key['4g'] = r(float(rhoA) * exp(-float(muA * (1 - rhoA)) * 10 / 60), 4)

if __name__ == '__main__':
    for k, v in key.items():
        print(f'{k}: {v}')
    # spot-checks of the hand derivation in quiz-2-prediction.md
    assert key['3c'] == '28/95' and key['3e'] == '1/5'
    assert key['4b'] == '1/7' and key['4d'] == '27/175' and key['4a'] == '20.00' and key['4f'] == '40.00'
    print('all checks passed')
