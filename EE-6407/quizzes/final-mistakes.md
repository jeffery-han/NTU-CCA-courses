# EE6407 final — mistakes log

Step 4 of the final-prep protocol (`final-intel.md`). One row per lost mark group, largest loss first. An item
closes only when its retry on fresh numbers is right. Retry keys were recomputed in Python on 2026-11-19.

## Mock B (sat 2026-11-19, scan `attempts/final-mock-b-2026-11-19.pdf`) — 40 / 100

Q1 19.5/25 · Q2 4/25 · Q3 10/25 · Q4 6.5/25. Blanks marked "forgot" (out of knowledge, not time): Q2(b), Q3(b),
Q4(b) after the centroids, Q4(c), Q4(d). Q2(a) stopped after the priors.

| # | Item (lost) | What was written | Why it is wrong | Rule | Retry | Status |
|---|---|---|---|---|---|---|
| 1 | Q3(b) soft-margin SVM (11) | "totally forgot" | Blank: whole procedure missing | w = Σ αᵢdᵢxᵢ over α > 0; b = average of dᵢ − wᵀxᵢ over **0 < α < C only**; margin 2/‖w‖; ξᵢ = 1 − dᵢ(wᵀxᵢ + b) | SVs (3,0)+ .625, (3,2)+ .625, (1,0)− .125, (1,2)− .125, (2.5,1)− 1, (0,4)− 0; C = 1; classify (2.4, 5). Key: w = (1, 0), b = −2 (−2.3 if (2.5,1) is used), margin 2, ξ = 1.5, g = 0.4 → +1, distance 0.4 | open |
| 2 | Q2(a) multinomial NB (8) | Tally table, d = 7, priors right; then crossed-out "P(s\|free) = 4/11" and stopped | Started computing a posterior P(class\|word) instead of the class-conditional P(word\|class); never reached the smoothed counts | P(w\|c) = (count of w in class c + 1)/(total words in c + d); score = P(c) × Π over **every token** (repeats multiply) | Sports: "ball goal ball", "goal team"; Politics: "vote team", "vote law vote"; test "ball vote team". Key: d = 5, n = 5 each; ball .3/.1, vote .1/.4, team .2/.2; scores .003 vs .004 → Politics | open |
| 3 | Q2(b) Gaussian NB (8) | p(x\|ω₁) = 1/((2π)^{2/2}·C⁻¹)·exp((x−m)ᵀC(x−m)) with "?" | Inverse and determinant swapped, ½ and minus sign missing; and naive Bayes needs no matrix at all: it is a product of 1-D Gaussians | Naive: p(x\|ω) = Π 1/√(2πσᵢ²)·exp(−(xᵢ−μᵢ)²/(2σᵢ²)); log form gⱼ = ln P − ½Σ ln σᵢ² − ½Σ (xᵢ−μᵢ)²/σᵢ² | P = .5/.5; ω₁ μ (0,2) σ² (1,1); ω₂ μ (2,1) σ² (4,1); x = (1,2). Key: lik .0965/.0426; g −1.1931/−2.0113 → ω₁; posterior .6938 | open |
| 4 | Q4(a) HAC distances (5.5) | Squared distances (5, 13, 113…) but AC = 4 (unsquared) → first merge {A,C} at 4 | "Euclidean distance" means √(Σ diff²). Squaring keeps single-link order but every height is wrong, and mixing one unsquared entry changed the first merge | Take the square root before filling the matrix; dendrogram heights are the real distances | P(0,0) Q(1,1) R(4,0) S(4,3): matrix and single-link merges. Key: PQ 1.4142, RS 3, then {PQ}{RS} at QR 3.1623 | open |
| 5 | Q4(b) Davies–Bouldin (5) | centroids right; δ = Σ d(cᵢ, s); "forgot DB" | δ is the RMS distance, not a sum; S₁₂ and DB not known | δᵢ = √((1/nᵢ)Σ‖x − mᵢ‖²); S_ij = (δᵢ + δⱼ)/d(mᵢ, mⱼ); DB = mean over i of max_j S_ij (K = 2: DB = S₁₂) | Same 4 points, clusters {P,Q}, {R,S}. Key: m (0.5,0.5), (4,1.5); δ .7071, 1.5; d 3.6401; DB .6063 | open |
| 6 | Q2(c) Gini formula (5) | G = ½[(1−p₊)² + (1−p₋)²] → root 0.2656 | That is ½Σp² (purity), not impurity. The sample weighting (4/16, 12/16) was **right**; A was chosen correctly by consistent reasoning | Gini = ½(1 − Σ pⱼ²): pure node 0, 50/50 node 0.25 | 12 samples 6/6. X: (5,3) \| (1,3); Y: (3,0) \| (3,6). Key: root .25; X .2188 (drop .0312); Y .1667 (drop .0833) → Y | open |
| 7 | Q1(a)(iii) PMX (4) | child 2 7 1 3 5 8 6 4: filled P₂'s values in order, skipping used ones | That is order-1 crossover, not PMX. PMX keeps P₂'s *positions* via the mapping chain | For each unmatched value v in P₂'s segment: look at P₁ at v's position → find that value in P₂ → place v there if free, else repeat | P₁ 3 5 1 7 2 8 6 4, P₂ 8 6 2 4 3 1 7 5, segment 3–5. Key: 8 6 1 7 2 3 4 5 | open |
| 8 | Q4(c) Dunn (4) | "forgot" | — | Dunn = (min distance between points in different clusters)/(max diameter = largest within-cluster pair distance) | Same 4 points. Key: QR 3.1623 / RS 3 = 1.0541 | open |
| 9 | Q4(d) Rand index (4) | "forgot" | — | RI = (N_s + N_d)/C(N,2): pairs together in both + pairs apart in both | {P,Q}{R,S} vs {P}{Q,R}{S}. Key: N_s 0, N_d 3 (PR, PS, QS), RI = 3/6 = 0.5 | open |
| 10 | Q3(a)(i) Fisher criterion (3) | not attempted | — | J(w) = wᵀS_Bw / wᵀS_Ww, S_B = (m₁−m₂)(m₁−m₂)ᵀ, S_W = S₁ + S₂, Sᵢ = Σ(x−mᵢ)(x−mᵢ)ᵀ: far-apart projected means, tight projected classes | Write it from memory, then say why maximising it gives w ∝ S_W⁻¹(m₁−m₂) | open |
| 11 | Q1(b)(ii) probabilities p₄, p₅ (1) | 0.148, 0.094 (sum 1.016) | Division slip | Probabilities must sum to 1: check before moving on | — (slip; no retry) | closed |
| 12 | Q3(a)(vi) distance (1) | −0.423 "< 1, not very confident" | Distance is \|g\|/‖w‖ (positive); "< 1" is no yardstick | Compare with the means' distance (m₁ is 2.226 away) | — (fold into item 10 retry) | open |
