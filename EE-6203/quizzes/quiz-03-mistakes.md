# EE6203 Quiz 3 — mistakes log (unofficial practice)

One entry per lost mark, most marks first. An entry closes only when its retry is right.
Key and rubric: `quiz-03-mock-a.md`. Retry numbers were checked with Python on 2026-11-07.

## Mock A, first sit (export 2026-11-06; typed finals only, no working on paper, timer not started)

Score **10.5 / 30** (Q1 4.5, Q2 5.5, Q3 0.5). 8 of the 19.5 lost marks were **blank** (Q3 b–d 7, Q1b(ii) 1).
The other 11.5 were wrong answers, missing reasons, or missing steps.

| # | Item | Written | What went wrong | Class | Rule | Retry |
|---|---|---|---|---|---|---|
| 1 | Q3(b–d) ripple-free deadbeat, 7 marks | blank | Did not attempt | blank (time or knowledge, not yet known) | Ripple-free: `G_cl = K z^-1 (1 + b z^-1)` keeps the plant zero, and `K = 1/G_cl-part(1)` | R6 open |
| 2 | Q3(a) ZOH discretisation, 3 marks | "order 1, R=1" | n = 2 (two poles: 1 and 0.5488). No derivation shown | concept: order = number of poles of G_ZAS | `G_ZAS = (1 - z^-1) Z{G(s)/s}`; order = denominator degree | R6 open |
| 3 | Q1(a) reasons, 2 marks | none | A T/F answer without a reason earns ½ | exam technique | Always write one line of reason | — |
| 4 | Q2(b) pole-zero matching, 2.5 marks | `1 - e^-1/(z - e^-1)` | Dropped the mapped zero `e^-sT` (s = −2) and the DC gain α. Looks like the ZOH formula, not P-Z matching | concept: mixed-up method | Map every pole and zero with `z = e^{sT}`, then choose α so that `C(1) = C(s=0)` | R4 open |
| 5 | Q2(c), 2 marks | form right; "2 delay" | No difference equations. Standard programming needs n = 1 delay; 2 is the direct-programming count | concept: standard vs direct | Standard: n delays. Direct: n + m | R5 open |
| 6 | Q1b, 1.5 marks | `[0,2]` | Closed interval: at K = 0 (pole at z = 1) and at K = 2 (\|z\| = 1) the loop is only marginally stable. Part (ii) blank | concept: strict inequalities | Jury gives strict `<`, so write `0 < K < 2` | R3 open |
| 7 | Q1(a)3, 1 mark | False (key: True) | Relative degree of the whole G is 3 once both z^-3 and the denominator are converted to powers of z | concept | m = relative degree after writing G in powers of z | R1 open |
| 8 | Q1(a)4, 1 mark | True (key: False) | Gave the direct-programming count (5); standard needs 3 | concept (same as #5) | Standard = n delays | R2 open |
