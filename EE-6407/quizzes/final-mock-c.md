# EE6407 final — Mock C: key and marking rubric

Unofficial practice paper (2026-11-19), step 5 of the final-prep protocol in `final-intel.md`: a cold re-test
weighted to the Mock B mistakes (`final-mistakes.md`). Sit it **after** `final-relearn.html`.
Paper: `final-mock-c.html` (answer-free). Checker: `final-mock-c-check.py`. **Total 100 marks** (4 × 25),
3 hours, closed book, calculator, handwritten.

Weighting: every Mock B loss returns on new numbers — PMX (Q1a), multinomial NB (Q2a), Gaussian NB (Q2b),
Gini formula (Q2c), soft-margin SVM with α = C (Q3a), Fisher criterion + distance (Q3b), Euclidean HAC (Q4a),
Davies–Bouldin (Q4b), Dunn (Q4c), Rand (Q4d). New: cycle crossover (Q1b) and the **Calinski–Harabasz index
(Q4e, the prediction item)** — in no 2024-26 paper; on the lecturer's revision list (revision deck p. 23).

Conventions as in `final-mock-b.md`, plus **CH = Σ nᵢ‖mᵢ − m‖² / Σ Cᵢ with Cᵢ = Σ‖x − mᵢ‖²**
(ml-slides-11 p. 14–15). The slide has **no** (N − K)/(K − 1) factor; the textbook form does. Use the slide.

Grading labels: **D** derivable, **C** convention-dependent.

---

## Q1 Genetic algorithms (25)

### (a) TSP with permutation coding (15)

Six cities, symmetric distances (row i, column j = distance between city i and j):

|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 0 | 4 | 7 | 6 | 9 | 5 |
| 2 | 4 | 0 | 3 | 8 | 6 | 7 |
| 3 | 7 | 3 | 0 | 5 | 4 | 8 |
| 4 | 6 | 8 | 5 | 0 | 3 | 6 |
| 5 | 9 | 6 | 4 | 3 | 0 | 5 |
| 6 | 5 | 7 | 8 | 6 | 5 | 0 |

A chromosome is the visiting order; the tour returns to the first city. Fitness f = 100/L.
P₁ = 1 3 5 2 6 4, P₂ = 2 4 1 6 3 5.

| Part | Key | Marks |
|---|---|---|
| (i) Tour lengths | L(P₁) = 7+4+6+7+6+6 = **36**; L(P₂) = 8+6+5+8+4+6 = **37** (the closing edge counts) | 4 D (2 each) |
| (ii) PMX child, segment = positions 3–5 from P₁ | **3 4 5 2 6 1** | 5 D |
| (iii) L and f | L(child) = 5+3+6+7+5+7 = **33**; f = 100/36 = **2.7778**, 100/37 = **2.7027**, 100/33 = **3.0303** | 3 D |
| (iv) Why a TSP operator must return a permutation; which mutation keeps the most adjacency | Every city once, else the tour skips or repeats a city (2). Inversion: reversing a segment changes only 2 edges (1); an adjacent swap (a length-2 inversion) is also accepted | 3 D |

PMX working: copy `_ _ 5 2 6 _`; P₂'s segment is 1 6 3; 6 already placed.
1 (pos 3): P₁ has 5 there → 5 is at pos 6 in P₂ → free → 1 to pos 6.
3 (pos 5): P₁ has 6 → 6 is at pos 4 in P₂ → occupied (2) → P₁ has 2 at pos 4 → 2 is at pos 1 in P₂ → free → 3 to pos 1.
Fill pos 2 from P₂: 4. Child = 3 4 5 2 6 1.

Wrong paths: filling P₂'s leftover values in order (order-1 crossover, gives 2 4 5 2 6 … with a
repeat, or 4 1 5 2 6 3) → mapping chain not applied; open tour (forgetting the last→first edge: 30 / 31 / 26);
f = L (would favour long tours).

### (b) Cycle crossover (10)

A = 1 2 3 4 5 6 7 8, B = 8 4 2 3 7 5 6 1.

| Part | Key | Marks |
|---|---|---|
| (i) Cycles (positions) | **{1, 8}, {2, 3, 4}, {5, 6, 7}** | 4 D |
| (ii) Child 1 (cycles alternately from A, B, A) | **1 4 2 3 5 6 7 8** | 3 D |
| (iii) Child 2 (B, A, B) | **8 2 3 4 7 5 6 1** | 2 D |
| (iv) What cycle crossover preserves | Every gene keeps a position it held in one parent; validity is automatic | 1 D |

Cycle 1: pos 1 holds 1 in A; B has 8 there; 8 is at pos 8 in A; B has 1 there → back to the start.

---

## Q2 Naive Bayes and trees (25)

### (a) Multinomial NB with Laplace smoothing (9)

Urgent: "server down now", "fix server now". Normal: "lunch plan", "plan meeting now", "meeting notes".
Test: "server meeting now now".

| Part | Key | Marks |
|---|---|---|
| Priors, d, totals | 2/5, 3/5; d = **8**; n_U = **6**, n_N = **7** | 2 C (d) |
| Conditionals | U: server 3/14 = **0.2143**, meeting 1/14 = **0.0714**, now 3/14 = **0.2143**; N: server 1/15 = **0.0667**, meeting 3/15 = **0.2**, now 2/15 = **0.1333** | 3 D |
| Scores (now counted twice) | U: 0.4 · 0.2143 · 0.0714 · 0.2143² = **2.8113 × 10⁻⁴**; N: 0.6 · 0.0667 · 0.2 · 0.1333² = **1.4222 × 10⁻⁴** | 3 D |
| Decision | **Urgent** | 1 D |

### (b) Gaussian naive Bayes (9)

P(ω₁) = 0.3, μ₁ = (4, 5), σ₁² = (1, 4); P(ω₂) = 0.7, μ₂ = (2, 1), σ₂² = (2, 1). x = (3, 3).

| Part | Key | Marks |
|---|---|---|
| Likelihoods | p(x\|ω₁) = **0.0293**, p(x\|ω₂) = **0.0119** | 3 D |
| g₁, g₂, decision | **−2.8971**, **−2.9532** → **ω₁** (likelihood beats the 0.7 prior) | 3 D |
| Posterior P(ω₁\|x) | **0.5140** → low confidence | 3 D |

Wrong path: using σ in place of σ² (for ω₁ feature 2, σ = 2 but σ² = 4); deciding on the prior alone.

### (c) Gini (7)

20 samples (8 +, 12 −). F1: (6, 2) | (2, 10); F2: (8, 6) | (0, 6); F3: (5, 5) | (3, 7).

Root **0.24**; weighted F1 **0.1583**, F2 **0.1714**, F3 **0.2300**; drops **0.0817**, **0.0686**, **0.0100** → **F1**.
Marks: root 1 (C), weighted 3, drops 2, choice 1. Wrong path: ½Σp² (purity) or unweighted children.

---

## Q3 SVM and Fisher LDA (25)

### (a) Soft-margin SVM, C = 2 (13)

| i | xᵢ | dᵢ | αᵢ |
|---|---|---|---|
| 1 | (1, 0) | +1 | 0.125 |
| 2 | (2, 2) | +1 | 1.375 |
| 3 | (0, 0) | −1 | 1.625 |
| 4 | (1, 2) | −1 | 1.875 |
| 5 | (0.5, 0) | +1 | 2 |
| 6 | (3, 1) | +1 | 0 |

| Part | Key | Marks |
|---|---|---|
| Σαᵢdᵢ = 0 | 0.125 + 1.375 + 2 − 1.625 − 1.875 = 0 | 1 D |
| w | **(2, −1)** | 3 D |
| Samples for b | 1–4 (0 < α < C); not 5 (α = C) or 6 (α = 0) | 2 C |
| b | each gives −1 → **b = −1** (wrongly using point 5 too: −0.8) | 2 D |
| Margin | 2/√5 = **0.8944** | 1 D |
| ξ₅ | 1 − 1·(1 − 0 − 1) = **1** → x₅ lies on the boundary | 2 D |
| Classify (1.2, 0.9) | g = 2.4 − 0.9 − 1 = **0.5** → **+1**; distance 0.5/√5 = **0.2236** < half-margin 0.4472 → inside the margin, low confidence | 2 D |

### (b) Fisher LDA (12)

m₁ = (5, 3), m₂ = (1, 1), S₁ = [[20, 4], [4, 12]], S₂ = [[16, 2], [2, 20]]. x = (3, 2.2).

| Part | Key | Marks |
|---|---|---|
| Criterion | J(w) = wᵀS_Bw / wᵀS_Ww; S_B = (m₁−m₂)(m₁−m₂)ᵀ; S_W = S₁ + S₂; large projected mean gap, small projected spread | 3 D |
| S_W, w | [[36, 6], [6, 32]], det **1116**; w = (1/1116)(32·4 − 6·2, −6·4 + 36·2) = (116, 48)/1116 = **(0.1039, 0.0430)** | 4 D |
| w₀ | −w·(3, 2) = **−0.3978** | 2 C |
| Classify | g = 0.3118 + 0.0946 − 0.3978 = **0.0086 > 0 → ω₁** | 1 D |
| Distance, confidence | **0.0765**; m₁ is **2.2304** away → x is almost on the boundary: very low confidence | 2 D |

Wrong path: rounding w to 2 dp gives g ≈ 0 or negative.

---

## Q4 Clustering (25)

A(2, 0), B(3, 5), C(3, 0), D(10, 10), E(14, 4); Euclidean distance.

| Part | Key | Marks |
|---|---|---|
| (a) Single-link HAC | AC **1**; {A,C}+B via BC **5**; DE **7.2111**; all via BD **8.6023**; cut at 2: {A,B,C} \| {D,E} | 8 D (matrix 2, merges 4, dendrogram 1, cut 1) |
| (b) Davies–Bouldin | m₁ = (2.6667, 1.6667), m₂ = (12, 7); δ₁ = **2.4037**, δ₂ = **3.6056**; d = **10.7497**; DB = **0.5590** | 6 C |
| (c) Dunn | min inter = BD **8.6023**; max diameter = DE **7.2111**; Dunn = **1.1929** | 4 D |
| (d) Rand vs {A} \| {B, C} \| {D, E} | N_s = **2** (BC, DE); N_d = **6**; RI = 8/10 = **0.8** | 3 D |
| (e) Calinski–Harabasz (prediction) | m = (6.4, 3.8); C₁ = **17.3333**, C₂ = **26**; S₁ = ‖m₁ − m‖² = **18.4889**, S₂ = **41.6**; CH = (3·18.4889 + 2·41.6)/(17.3333 + 26) = 138.6667/43.3333 = **3.2** | 4 C |

---

## Machine-checked keys

```json keys
{
 "q1a_L1": 36, "q1a_L2": 37, "q1a_child": "345261", "q1a_Lc": 33,
 "q1a_f1": 2.7778, "q1a_f2": 2.7027, "q1a_fc": 3.0303,
 "q1b_cycles": "18|234|567", "q1b_child1": "14235678", "q1b_child2": "82347561",
 "q2a_d": 8, "q2a_n_Urgent": 6, "q2a_p_meeting_Urgent": 0.0714, "q2a_p_now_Urgent": 0.2143,
 "q2a_p_server_Urgent": 0.2143, "q2a_score_Urgent": 2.8113, "q2a_n_Normal": 7,
 "q2a_p_meeting_Normal": 0.2, "q2a_p_now_Normal": 0.1333, "q2a_p_server_Normal": 0.0667,
 "q2a_score_Normal": 1.4222, "q2a_class": "Urgent",
 "q2b_lik1": 0.0293, "q2b_g1": -2.8971, "q2b_lik2": 0.0119, "q2b_g2": -2.9532, "q2b_class": 1, "q2b_post1": 0.514,
 "q2c_root": 0.24, "q2c_F1_w": 0.1583, "q2c_F1_drop": 0.0817, "q2c_F2_w": 0.1714, "q2c_F2_drop": 0.0686,
 "q2c_F3_w": 0.23, "q2c_F3_drop": 0.01, "q2c_best": "F1",
 "q3a_w1": 2.0, "q3a_w2": -1.0, "q3a_b": -1.0, "q3a_b_wrong": -0.8, "q3a_margin": 0.8944, "q3a_xi": 1.0,
 "q3a_nfree": 4, "q3a_g": 0.5, "q3a_dist": 0.2236,
 "q3b_det": 1116, "q3b_w1": 0.1039, "q3b_w2": 0.043, "q3b_w0": -0.3978, "q3b_g": 0.0086, "q3b_cls": 1,
 "q3b_dist": 0.0765, "q3b_dist_m1": 2.2304,
 "q4a_merge1": "AC@1.0", "q4a_merge2": "ABC@5.0", "q4a_merge3": "DE@7.2111", "q4a_merge4": "ABCDE@8.6023",
 "q4_m1": "2.6667,1.6667", "q4_m2": "12.0,7.0", "q4_delta1": 2.4037, "q4_delta2": 3.6056, "q4_d12": 10.7497,
 "q4_DB": 0.559, "q4_inter": 8.6023, "q4_diam": 7.2111, "q4_dunn": 1.1929, "q4_Ns": 2, "q4_Nd": 6, "q4_RI": 0.8,
 "q4_gm": "6.4,3.8", "q4_C1": 17.3333, "q4_C2": 26.0, "q4_S1": 18.4889, "q4_S2": 41.6, "q4_CH": 3.2
}
```
