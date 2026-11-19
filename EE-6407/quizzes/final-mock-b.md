# EE6407 final — Mock B: key and marking rubric

Unofficial practice paper (2026-11-19), step 3 of the final-prep protocol in `final-intel.md`.
Paper: `final-mock-b.html` (answer-free). Checker: `final-mock-b-check.py` recomputes every number
below. **Total 100 marks** (4 × 25). 3 hours, closed book, calculator, handwritten.

Conventions (slides, confirmed again against the lecturer's revision deck
`resources/machine-learning/ml-revision-2026-s1.pdf`, posted after 2026-11-13):
Gini = ½(1 − Σp²) (revision p. 16; ml-slides-06 p. 14); w₀ = −wᵀ(m₁+m₂)/2 (revision p. 9);
soft-margin b averaged over 0 < α < C only (revision p. 14); Laplace (count+1)/(Σcount + d), d =
vocabulary of all training documents (ml-slides-03 p. 68); Davies–Bouldin δᵢ = RMS distance to the
centroid (ml-slides-11 p. 11–12); Dunn = min inter-cluster pair distance / max diameter (p. 8–9);
Rand index RI = (N_s + N_d)/C(N,2) (p. 17–18).

Grading labels: **D** derivable (mark firmly), **C** convention-dependent (course slide decides).

---

## Q1 Genetic algorithms (25)

### (a) 8-queens with permutation coding (15)

Gene i = row of the queen in column i. Fitness f(q) = 1 − C(q)/28, C = number of attacking
(diagonal) pairs. P₁ = 6 2 1 3 5 8 4 7, P₂ = 5 1 8 2 7 6 3 4.

| Part | Key | Marks |
|---|---|---|
| (i) Why permutation coding removes row and column conflicts; search-space size | One queen per column by position, one per row because each value appears once, so only diagonal attacks remain (2). 8! = 40 320 vs 8⁸ = 16 777 216 (1). | 3 D |
| (ii) C and f of P₁, P₂ | **C(P₁) = 4, f = 0.8571; C(P₂) = 5, f = 0.8214** | 4 D (1 per C with its pair list, 1 per f) |
| (iii) PMX child, segment = positions 3–6 from P₁ | **7 6 1 3 5 8 2 4** | 5 D |
| (iv) C and f of the child | **C = 1** (pair (1,2): rows 7, 6), **f = 0.9643** | 2 D |
| (v) Why the child is still a valid permutation, and one operator that would break it | PMX places each value once (repair by mapping). One-point crossover on two permutations can duplicate a value, i.e. two queens in one row | 1 D |

Attacking pairs (columns i < j with |qᵢ − qⱼ| = j − i):
- P₁ = 6 2 1 3 5 8 4 7: (1,4) rows 6,3; (2,3) rows 2,1; (2,5) rows 2,5; (4,8) rows 3,7 → C = 4.
- P₂ = 5 1 8 2 7 6 3 4: (1,4) rows 5,2; (5,6) rows 7,6; (5,8) rows 7,4; (6,8) rows 6,4; (7,8) rows 3,4 → C = 5.
- Child = 7 6 1 3 5 8 2 4: (1,2) rows 7,6 → C = 1. The child is better than both parents.

PMX working (course convention, `notes/beginner-notes.tex` §PMX):
1. Copy P₁ positions 3–6: `_ _ 1 3 5 8 _ _`.
2. P₂'s segment is 8 2 7 6. 8 is already placed. Unmatched: 2, 7, 6.
   - 2 (pos 4 in P₂): P₁ has 3 there; 3 is at pos 7 in P₂; pos 7 free → 2 goes to pos 7.
   - 7 (pos 5): P₁ has 5; 5 is at pos 1 in P₂; free → 7 goes to pos 1.
   - 6 (pos 6): P₁ has 8; 8 is at pos 3 in P₂ — occupied (by 1); P₁ has 1 at pos 3; 1 is at pos 2
     in P₂; free → 6 goes to pos 2. (chain of length 2)
3. Fill pos 8 from P₂: 4. Child = **7 6 1 3 5 8 2 4**; each of 1–8 once.

Common wrong paths: filling every free slot straight from P₂ (gives duplicates 2, 7, 6 vs lost 3,
5) → did not apply the mapping; stopping the 6-chain at the occupied pos 3 → chain not followed;
counting row/column conflicts as well → misunderstood what the coding guarantees; using f = 28 − C
when asked for [0, 1].

### (b) Minimisation and roulette selection (10)

Cost g = (4, 9, 1, 6, 10) for individuals 1–5; we minimise g. Fitness f = 1/(1+g).

| Part | Key | Marks |
|---|---|---|
| (i) Why raw g cannot be the roulette fitness | Roulette gives probability ∝ fitness, so larger g = more copies: it would favour the worst solutions; also needs f ≥ 0 (2) | 2 D |
| (ii) f and selection probabilities | f = 0.2, 0.1, 0.5, 0.1429, 0.0909; Σ = 1.0338; **p = 0.1935, 0.0967, 0.4837, 0.1382, 0.0879** | 4 D (2 f, 2 p) |
| (iii) Expected copies of individual 3 in a mating pool of 5 | **5 × 0.4837 = 2.4183** | 1 D |
| (iv) Spins u = 0.25, 0.80, 0.95 on the cumulative wheel (0.1935, 0.2902, 0.7739, 0.9121, 1) | **individuals 2, 4, 5** | 2 D |
| (v) The best individual was not picked in (iv): what does this show? | Selection is stochastic: it biases towards fit individuals but does not guarantee them; weak ones keep diversity (exploration). Elitism keeps the best if needed. | 1 D |

Common wrong paths: using f = −g (negative probabilities); normalising g instead of f (inverts
the preference); reading the wheel with u < cum instead of u ≤ cum (no change here).

---

## Q2 Bayes, naive Bayes, trees (25)

### (a) Multinomial naive Bayes with Laplace smoothing (10)

Spam: "free win free", "win money", "free money now". Ham: "meeting now", "project meeting
notes", "notes free", "project notes". Test: "free notes now free".

| Part | Key | Marks |
|---|---|---|
| Priors | P(S) = 3/7, P(H) = 4/7 | 1 D |
| Vocabulary and totals | d = 7 (free, win, money, now, meeting, project, notes); n_S = 8 words, n_H = 9 words | 1 C (d = whole training vocabulary) |
| Smoothed conditionals | P(free\|S) = 4/15 = **0.2667**, P(notes\|S) = 1/15 = **0.0667**, P(now\|S) = 2/15 = **0.1333**; P(free\|H) = 2/16 = **0.125**, P(notes\|H) = 4/16 = **0.25**, P(now\|H) = 2/16 = **0.125** | 4 D (½ each, rounded up) |
| Scores (free counted twice) | S: 3/7 · (4/15)² · (1/15) · (2/15) = **2.7090 × 10⁻⁴**; H: 4/7 · (2/16)² · (4/16) · (2/16) = **2.7902 × 10⁻⁴** | 3 D |
| Decision, and why Laplace | **Ham** (narrowly). Without smoothing P(notes\|S) = 0 would veto spam whatever the other words say | 1 D |

Common wrong paths: using each word once (Bernoulli thinking) → free must appear squared;
dropping priors → spam wins (the trap); d = 4 or 5 (only the test words, or only one class's words);
denominators = number of documents instead of number of words.

### (b) Gaussian naive Bayes (8)

P(ω₁) = 0.6, μ₁ = (2, 5), σ₁² = (1, 4); P(ω₂) = 0.4, μ₂ = (4, 3), σ₂² = (2, 1). x = (3, 4).

| Part | Key | Marks |
|---|---|---|
| Class-conditional likelihoods p(x\|ωⱼ) = Π N(xᵢ; μ, σ²) | p(x\|ω₁) = **0.0426**, p(x\|ω₂) = **0.0532** | 3 D |
| Discriminants gⱼ = ln P(ωⱼ) − ½Σ ln σ² − ½Σ (xᵢ−μᵢ)²/σᵢ² (2π dropped) | g₁ = **−1.8290**, g₂ = **−2.0129** | 2 D |
| Decision | **ω₁** (the prior overturns the likelihood) | 1 D |
| Posterior P(ω₁\|x) | 0.6·0.0426 / (0.6·0.0426 + 0.4·0.0532) = **0.5458** | 2 D |

Common wrong paths: σ instead of σ² in the exponent (σ₁ for feature 2 is 2, not 4); deciding on
likelihood alone (gives ω₂); forgetting the ½ ln σ² term when comparing logs.

### (c) Root-node choice by Gini (7)

16 samples, 10 (+) and 6 (−). A: A=1 → 7+, 1−; A=0 → 3+, 5−. B: B=1 → 4+, 0−; B=0 → 6+, 6−.
C: C=1 → 8+, 2−; C=0 → 2+, 4−. Use Gini = ½(1 − Σp²).

| Part | Key | Marks |
|---|---|---|
| Root impurity | **0.2344** | 1 C |
| Weighted child impurity | A **0.1719**, B **0.1875**, C **0.1833** | 3 D |
| Impurity drops | A **0.0625**, B **0.0469**, C **0.0510** | 2 D |
| Choice | **A** — not B, although B has a pure branch: its pure branch holds only 4 of 16 samples and leaves 12 at maximum impurity | 1 D |

Common wrong paths: 1 − Σp² (doubles every number; the choice is unchanged but the values lose the
convention mark); unweighted average of the two children (gives B: (0 + 0.25)/2 = 0.125 smallest);
choosing the split with a pure child.

---

## Q3 Fisher LDA and SVM (25)

### (a) Fisher LDA (14)

m₁ = (6, 4), m₂ = (2, 2), S₁ = [[30, 10], [10, 20]], S₂ = [[26, −2], [−2, 16]]. Test x = (3.5, 3).

| Part | Key | Marks |
|---|---|---|
| (i) Fisher criterion and S_B | J(w) = wᵀS_Bw / wᵀS_Ww, S_B = (m₁−m₂)(m₁−m₂)ᵀ; maximise between-class separation of the projected means relative to within-class scatter | 3 D |
| (ii) S_W | [[56, 8], [8, 36]], det = **1952** | 1 D |
| (iii) w = S_W⁻¹(m₁ − m₂) | S_W⁻¹ = (1/1952)[[36, −8], [−8, 56]]; w = (128, 80)/1952 = **(0.0656, 0.0410)** | 4 D |
| (iv) w₀ | −wᵀ(m₁+m₂)/2 = −w·(4, 3) = **−0.3852** | 2 C |
| (v) Classify x | g(x) = 0.2295 + 0.1230 − 0.3852 = **−0.0328 < 0 → ω₂** | 2 D |
| (vi) Distance to the boundary and confidence | \|g\|/‖w‖ = 0.0328/0.0773 = **0.4240**; low confidence: m₁ itself is 2.226 from the boundary, so x is very close to it | 2 D |

Common wrong paths: w = S_W⁻¹(m₂ − m₁) (sign flip → class flips unless w₀ flips too); S_W =
(S₁+S₂)/2 (scales w, keeps the class; lose the S_W mark only); forgetting ‖w‖ in the distance;
rounding w to 2 dp early (g becomes −0.03 or 0, the decision can be lost).

### (b) Soft-margin SVM, C = 1 (11)

| i | xᵢ | dᵢ | αᵢ |
|---|---|---|---|
| 1 | (2, 3) | +1 | 0.25 |
| 2 | (4, 1) | +1 | 0.5 |
| 3 | (1, 2) | −1 | 0.875 |
| 4 | (3, 0) | −1 | 0.875 |
| 5 | (2, 1.5) | +1 | 1 |
| 6 | (5, 4) | +1 | 0 |

| Part | Key | Marks |
|---|---|---|
| (i) Check Σαᵢdᵢ = 0 | 0.25 + 0.5 + 1 − 0.875 − 0.875 = 0 | 1 D |
| (ii) w = Σαᵢdᵢxᵢ | (4.5, 2.75) − (3.5, 1.75) = **(1, 1)** | 3 D |
| (iii) Which points give b, and why | Only 0 < α < C: points 1–4. Point 5 has α = C (inside the margin, ξ > 0, so dᵢ(wᵀxᵢ + b) = 1 does not hold); point 6 has α = 0 (not a support vector) | 2 C (ml-slides-05 p. 40; revision p. 14) |
| (iv) b | each of points 1–4 gives dᵢ − wᵀxᵢ = −4; **b = −4** (wrong path: including point 5 gives −3.7) | 2 D |
| (v) Margin width and ξ₅ | 2/‖w‖ = **1.4142**; ξ₅ = 1 − d₅(wᵀx₅ + b) = 1 − (−0.5) = **1.5** → x₅ is misclassified | 1 D |
| (vi) Classify (3.2, 1.2), distance, confidence | g = 0.4 → **class +1**; distance 0.4/√2 = **0.2828** < half-margin 0.7071 → inside the margin, low confidence | 2 D |

---

## Q4 Clustering (25)

Points A(0, 0), B(1, 2), C(4, 0), D(8, 7), E(9, 4), F(12, 8), Euclidean distance.

### (a) Single-linkage HAC (10)

Distance matrix (exact): AB 2.2361, AC 4, AD 10.6301, AE 9.8489, AF 14.4222, BC 3.6056,
BD 8.6023, BE 8.2462, BF 12.5300, CD 8.0623, CE 6.4031, CF 11.3137, DE 3.1623, DF 4.1231, EF 5.

| Merge | Clusters | Height |
|---|---|---|
| 1 | {A, B} | **2.2361** |
| 2 | {D, E} | **3.1623** |
| 3 | {A, B, C} (via BC) | **3.6056** |
| 4 | {D, E, F} (via DF) | **4.1231** |
| 5 | all (via CE) | **6.4031** |

Marks: distance matrix 3, each merge with its updated matrix 1 × 5, dendrogram with heights to
scale 1, two-cluster cut {A, B, C} | {D, E, F} 1. Wrong path: complete-linkage update (max) gives the same merge order but heights 4, 5 and 14.4222
for merges 3–5; give no height marks for those.

### (b) Davies–Bouldin index of the 2-cluster cut (7)

| Part | Key | Marks |
|---|---|---|
| Centroids | m₁ = (1.6667, 0.6667), m₂ = (9.6667, 6.3333) | 2 D |
| δ (RMS distance to centroid) | δ₁ = √(34/9) = **1.9437**, δ₂ = **2.4037** | 2 C |
| d(1, 2) | **9.8036** | 1 D |
| DB = (δ₁ + δ₂)/d(1, 2) (K = 2, so S₁ = S₂ = S₁₂) | **0.4434**; small → compact, well separated | 2 D |

Wrong path: mean (not RMS) distance to the centroid; the course slide uses the RMS form.

### (c) Dunn index (4)

Min inter-cluster pair distance = CE = **6.4031**; max diameter = EF = **5** (cluster 1 diameter is
AC = 4). Dunn = **1.2806** (> 1 → clusters further apart than they are wide). Marks 2 + 1 + 1.

### (d) Rand index — *prediction item* (4)

Not in any 2024-26 official paper. Predicted because the lecturer's revision deck lists it (p. 23)
and ml-slides-11 p. 17–18 gives the formula. Compare the single-link cut {A,B,C}|{D,E,F} with
a second method's result {A,B}|{C,D,E}|{F}.

N_s (same cluster in both) = 2 (AB, DE); N_d (different in both) = 7 (AD, AE, AF, BD, BE, BF, CF);
C(6, 2) = 15. **RI = 9/15 = 0.6**. Marks: N_s 1, N_d 2, RI 1.

Wrong path: counting pairs that agree in one method only; using C(6,2) = 30.

---

## Machine-checked keys

```json keys
{
 "q1a_C_P1": 4, "q1a_f_P1": 0.8571, "q1a_C_P2": 5, "q1a_f_P2": 0.8214,
 "q1a_child": "76135824", "q1a_C_child": 1, "q1a_f_child": 0.9643,
 "q1a_space_perm": 40320, "q1a_space_free": 16777216,
 "q1b_p1": 0.1935, "q1b_p2": 0.0967, "q1b_p3": 0.4837, "q1b_p4": 0.1382, "q1b_p5": 0.0879,
 "q1b_expected3": 2.4183, "q1b_picks": "245",
 "q2a_d": 7, "q2a_nspam": 8, "q2a_nham": 9,
 "q2a_free_S": 0.2667, "q2a_free_H": 0.125, "q2a_notes_S": 0.0667, "q2a_notes_H": 0.25,
 "q2a_now_S": 0.1333, "q2a_now_H": 0.125,
 "q2a_scoreS_e4": 2.709, "q2a_scoreH_e4": 2.7902, "q2a_class": "ham", "q2a_class_noprior": "spam",
 "q2b_lik1": 0.0426, "q2b_g1": -1.829, "q2b_lik2": 0.0532, "q2b_g2": -2.0129,
 "q2b_class": 1, "q2b_post1": 0.5458,
 "q2c_root": 0.2344, "q2c_A_weighted": 0.1719, "q2c_A_drop": 0.0625,
 "q2c_B_weighted": 0.1875, "q2c_B_drop": 0.0469, "q2c_C_weighted": 0.1833, "q2c_C_drop": 0.051,
 "q2c_best": "A",
 "q3a_det": 1952, "q3a_w1": 0.0656, "q3a_w2": 0.041, "q3a_w0": -0.3852,
 "q3a_g": -0.0328, "q3a_class": 2, "q3a_dist": 0.424, "q3a_dist_m1": 2.226,
 "q3b_w1": 1.0, "q3b_w2": 1.0, "q3b_b": -4.0, "q3b_b_wrong_all": -3.7, "q3b_margin": 1.4142,
 "q3b_xi5": 1.5, "q3b_g": 0.4, "q3b_class": 1, "q3b_dist": 0.2828,
 "q4a_merge1": "AB@2.2361", "q4a_merge2": "DE@3.1623", "q4a_merge3": "ABC@3.6056",
 "q4a_merge4": "DEF@4.1231", "q4a_merge5": "ABCDEF@6.4031", "q4a_cut2": "ABC|DEF",
 "q4b_m1": "1.6667,0.6667", "q4b_m2": "9.6667,6.3333", "q4b_delta1": 1.9437, "q4b_delta2": 2.4037,
 "q4b_d12": 9.8036, "q4b_DB": 0.4434,
 "q4c_inter": 6.4031, "q4c_diam": 5.0, "q4c_dunn": 1.2806,
 "q4d_Ns": 2, "q4d_Nd": 7, "q4d_RI": 0.6
}
```
