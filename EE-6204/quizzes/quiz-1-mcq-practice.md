# EE6204 Quiz 1 — MCQ practice paper: key, reasons, and traps

**Companion to `quiz-1-mcq-practice.html`.** 18 single-answer items, 1 mark each, **total 18**.
Sit the HTML cold and timed (60 min, no calculator, ruler + paper) *before* reading this.

This paper is **unofficial**. It matches the official Quiz 1 shape — MCQ; scope = graphical
method + simplex method + sensitivity analysis for the simplex method; 60 min; no calculator
(`quiz-1-official-announcement.pdf`) — but every question and number here was written from
scratch. Q16 is flagged `unseen?`: RHS-range sensitivity is in scope and lecturer-flagged but
absent from circulating recollections, so treat it as a prediction of an unseen item type.

Grading: mark each item right/wrong (1/0). Then, for every miss, decide whether it was a
**slip** (misread the tableau, arithmetic) or an **inverted concept** (wrong rule) — only the
second kind needs a notes edit. An unanswered item is **blank, not wrong**; report it separately.

---

## LP A (Q1–Q4)

\[ \max\ z = 3x_1 + 2x_2 \quad\text{s.t.}\quad x_1 + x_2 \le 5,\quad x_1 + 3x_2 \le 9,\quad x_1 \le 4,\quad x_1,x_2 \ge 0. \]

Feasible-region corners and objective values (walk the boundary anticlockwise from the origin):

| vertex | from | \(z = 3x_1 + 2x_2\) |
|---|---|---:|
| \((0,0)\) | origin | 0 |
| \((4,0)\) | \(x_1 = 4\), \(x_2 = 0\) | 12 |
| \((4,1)\) | \(x_1 = 4 \cap x_1 + x_2 = 5\) | **14** |
| \((3,2)\) | \(x_1 + x_2 = 5 \cap x_1 + 3x_2 = 9\) | 13 |
| \((0,3)\) | \(x_1 + 3x_2 = 9\), \(x_1 = 0\) | 6 |

Optimum \((4,1)\), \(z = 14\). Binding there: \(x_1 \le 4\) and \(x_1 + x_2 \le 5\)
(check \(x_1 + 3x_2 = 4 + 3 = 7 < 9\), slack 2).

### Q1 — optimal \((x_1,x_2)\) → **(b) \((4,1)\)**
Reason: highest \(z\) over the five corners.
Traps: **(a) \((4,0)\)** stops at the first corner on the \(x_1\)-axis without sliding the value
line up; **(c) \((3,2)\)** is the next corner but \(z = 13 < 14\) — you slid one vertex too far;
**(d) \((0,3)\)** maximises \(x_2\), not \(z\).

### Q2 — max \(z\) → **(c) 14**
Trap: **(b) 13** = value at \((3,2)\); **(a) 12** = value at \((4,0)\). Both are "right method,
wrong vertex" — award 0 for MCQ but note it's a vertex-selection slip, not a concept error.

### Q3 — binding constraints at the optimum → **(b) \(x_1 \le 4\) and \(x_1 + x_2 \le 5\)**
Reason: substitute \((4,1)\). \(x_1 = 4\) (tight), \(x_1 + x_2 = 5\) (tight),
\(x_1 + 3x_2 = 7 < 9\) (slack).
Traps: **(a)** names the constraints binding at the *neighbouring* vertex \((3,2)\);
**(c) all three** is the degenerate case — not this LP; **(d)** forgets \(x_1 + x_2 = 5\) is also tight.

### Q4 — objective gradient → **(b) \((3,2)\)**
Reason: \(\nabla z = (\partial z/\partial x_1,\ \partial z/\partial x_2) = (3, 2)\); it points the
way \(z\) increases, perpendicular to the value lines \(3x_1 + 2x_2 = \text{const}\).
Traps: **(a) \((2,3)\)** swaps the components; **(c) \((-3,-2)\)** is the *decrease* direction
(that's for a min); **(d) \((5,9)\)** is a constraint coefficient vector, not the objective's.

---

### Q5 — classify \(\max\ x_1 + x_2\) s.t. \(x_1 - x_2 \le 2,\ -x_1 + x_2 \le 2,\ x_1,x_2 \ge 0\)
→ **(c) unbounded**
Reason: the two constraints only bound \(|x_1 - x_2| \le 2\); nothing caps \(x_1 + x_2\). Move
along the ray \(x_1 = x_2 = t\): both constraints give \(0 \le 2\), both variables stay \(\ge 0\),
and \(z = 2t \to \infty\).
Traps: **(a) infeasible** — the origin is feasible, so no; **(b) unique optimum** — there is no
finite optimum; **(d) infinitely many optima** confuses "unbounded feasible region" with
"unbounded objective" — a bounded objective on an unbounded region can still have one optimum, but
here the objective itself runs away.

### Q6 — optimal set of \(\max\ 2x_1 + 6x_2\) s.t. \(x_1 + 3x_2 \le 9,\ x_1 \le 6,\ x_1,x_2 \ge 0\)
→ **(c) every point on the segment joining \((0,3)\) and \((6,1)\)**
Reason: \(2x_1 + 6x_2 = 2(x_1 + 3x_2) \le 2(9) = 18\), attained for *every* point with
\(x_1 + 3x_2 = 9\). The objective line is parallel to that binding edge (multiple optima). The
edge runs from \((0,3)\) to where \(x_1 = 6\) hits it, i.e. \((6,1)\); both satisfy \(x_1 \le 6\).
Traps: **(a)/(b)** each pick one endpoint as if the optimum were unique; **(d) \((9,0)\)** is on
the line \(x_1 + 3x_2 = 9\) but violates \(x_1 \le 6\) — infeasible.

---

## LP B (Q7–Q13, and Part C)

\[ \max\ z = 4x_1 + 3x_2 \quad\text{s.t.}\quad 2x_1 + 3x_2 \le 12,\quad 2x_1 + x_2 \le 8,\quad x_1,x_2 \ge 0. \]

Standard form: \(2x_1 + 3x_2 + s_1 = 12\); \(2x_1 + x_2 + s_2 = 8\); objective row \(z - 4x_1 - 3x_2 = 0\).

**Tableau 0** (basis \(s_1, s_2\)):

| basis | \(z\) | \(x_1\) | \(x_2\) | \(s_1\) | \(s_2\) | RHS |
|---|--:|--:|--:|--:|--:|--:|
| \(z\)  | 1 | \(-4\) | \(-3\) | 0 | 0 | 0 |
| \(s_1\) | 0 | 2 | 3 | 1 | 0 | 12 |
| \(s_2\) | 0 | 2 | 1 | 0 | 1 | 8 |

**Pivot 1:** enter \(x_1\) (\(-4\), most negative). Ratios \(12/2 = 6\), \(8/2 = 4\) → \(s_2\) leaves.
Pivot on the \(2\) in the \(s_2\) row.

**Tableau 1** (basis \(s_1, x_1\)):

| basis | \(z\) | \(x_1\) | \(x_2\) | \(s_1\) | \(s_2\) | RHS |
|---|--:|--:|--:|--:|--:|--:|
| \(z\)  | 1 | 0 | \(-1\) | 0 | 2 | 16 |
| \(s_1\) | 0 | 0 | 2 | 1 | \(-1\) | 4 |
| \(x_1\) | 0 | 1 | \(0.5\) | 0 | \(0.5\) | 4 |

**Pivot 2:** enter \(x_2\) (\(-1\)). Ratios \(s_1\): \(4/2 = 2\); \(x_1\): \(4/0.5 = 8\) → \(s_1\) leaves.
Pivot on the \(2\) in the \(s_1\) row.

**Tableau 2** (basis \(x_2, x_1\)) — **optimal**, bottom row all \(\ge 0\):

| basis | \(z\) | \(x_1\) | \(x_2\) | \(s_1\) | \(s_2\) | RHS |
|---|--:|--:|--:|--:|--:|--:|
| \(z\)  | 1 | 0 | 0 | \(\tfrac12\) | \(\tfrac32\) | 18 |
| \(x_2\) | 0 | 0 | 1 | \(\tfrac12\) | \(-\tfrac12\) | 2 |
| \(x_1\) | 0 | 1 | 0 | \(-\tfrac14\) | \(\tfrac34\) | 3 |

Optimum \(x_1 = 3,\ x_2 = 2,\ z = 18\). Both constraints binding: \(2(3) + 3(2) = 12\),
\(2(3) + 2 = 8\), so \(s_1 = s_2 = 0\).

### Q7 — standard form of \(2x_1 + 3x_2 \le 12\) → **(b) \(2x_1 + 3x_2 + s_1 = 12,\ s_1 \ge 0\)**
Reason: a \(\le\) constraint takes a **slack** variable (unused resource, \(\ge 0\)).
Traps: **(a)** uses a *surplus* (\(-s_1\)) — that's for \(\ge\); **(c)** adds an artificial — only
needed when there is no obvious starting basic variable (equalities, \(\ge\) rows); **(d)** a free
slack breaks the "unused amount \(\ge 0\)" meaning. Concept error if chosen: slack vs surplus vs artificial.

### Q8 — first entering variable → **(a) \(x_1\)**
Reason: with the \(z - c^\mathsf{T}x = 0\) row, the most negative entry is \(-4\) under \(x_1\).
(Any negative may enter; \(-4\) is the standard pick and the one the tableaux here follow.)
Traps: **(b) \(x_2\)** enters *second*; **(c)/(d)** slacks never enter on the first pivot from an all-slack basis.

### Q9 — first leaving variable → **(b) \(s_2\) (ratio \(8/2 = 4\))**
Reason: minimum ratio over rows with a positive \(x_1\)-entry: \(12/2 = 6\) vs \(8/2 = 4\); the
smaller, 4, is the \(s_2\) row.
Traps: **(a) \(s_1\)** takes the *larger* ratio (would drive \(s_2\) negative); **(c)** \(x_1\) is
entering, not leaving; **(d)** both entries are positive, so it is not unbounded.

### Q10 — Tableau 1: next entering variable → **(b) \(x_2\)**
Reason: the \(z\)-row is \([\,0,\ -1,\ 0,\ 2\,]\); the only negative is \(-1\) under \(x_2\).
Traps: **(a) \(x_1\)** is already basic (\(z\)-row entry 0); **(c) \(s_1\)** has \(z\)-row entry 0;
**(d)** not optimal yet — a negative remains.

### Q11 — Tableau 1: second ratio test → **(a) compare \(4/2\) and \(4/0.5\); smaller is 2, so \(s_1\) leaves**
Reason: entering column \(x_2\) has positive entries \(2\) (\(s_1\) row) and \(0.5\) (\(x_1\) row);
ratios \(4/2 = 2\) and \(4/0.5 = 8\); the \(s_1\) row wins.
Traps: **(b)** right ratios, names the wrong leaving row; **(c)** false — the column *has*
positive entries; **(d)** both rows are eligible, not just \(x_1\).

### Q12 — Tableau 2: optimal solution → **(c) \(x_1 = 3,\ x_2 = 2,\ z = 18\)**
Reason: read the RHS against the basis — \(x_2 = 2\), \(x_1 = 3\), \(z = 18\); nonbasic \(s_1 = s_2 = 0\).
Traps: **(a)** is the solution *after pivot 1 only* (\(x_1 = 4\)); **(b)** swaps which variable is
where; **(d)** transposes \(x_1\) and \(x_2\) and mis-adds.

### Q13 — why Tableau 2 is optimal → **(a) every entry in the \(z\)-row is now \(\ge 0\)**
Reason: with the \(z - c^\mathsf{T}x = 0\) convention, no negative reduced cost means no variable
can improve \(z\) — the stopping rule.
Traps: **(b)/(c)/(d)** are all *true statements about this tableau* but none is the optimality
criterion. Choosing one is a concept gap: the test is the sign of the objective row, nothing else.

---

## Part C — sensitivity, from the final tableau of LP B

Final \(z\)-row: \(z = 18 - \tfrac12 s_1 - \tfrac32 s_2\).
Final \(x_2\)-row: \(x_2 + \tfrac12 s_1 - \tfrac12 s_2 = 2\).
Final \(x_1\)-row: \(x_1 - \tfrac14 s_1 + \tfrac34 s_2 = 3\).

### Q14 — shadow price of constraint 1 → **(b) \(\tfrac12\)**
Reason: the shadow price of constraint \(i\) is the final \(z\)-row coefficient under its slack
\(s_i\). Under \(s_1\): \(\tfrac12\).
Traps: **(c) \(\tfrac32\)** is constraint 2's shadow price (read the wrong column); **(a) 0** would
hold only if \(s_1\) were basic (non-binding); **(d) 2** is the \(s_2\)-coefficient from
*Tableau 1*, not the final one.

### Q15 — new \(z\) when \(b_2 : 8 \to 9\) → **(c) 19.5**
Reason: \(\Delta z = \Delta b_2 \times (\text{shadow price of constraint 2}) = 1 \times \tfrac32 = 1.5\),
so \(z = 18 + 1.5 = 19.5\).
Traps: **(a) 18** ignores the change; **(b) 18.5** uses constraint 1's price \(\tfrac12\);
**(d) 21** uses \(\tfrac32 \times 2\) or double-counts.

### Q16 `unseen?` — allowable range of \(b_1\) → **(a) \([8,\ 24]\)**
Reason: perturb \(b_1 \to 12 + \Delta\). New basic values = old + \(\Delta \times (s_1\text{ column})\):
\[ x_2 = 2 + \tfrac12\Delta \ge 0 \Rightarrow \Delta \ge -4, \qquad x_1 = 3 - \tfrac14\Delta \ge 0 \Rightarrow \Delta \le 12. \]
So \(\Delta \in [-4, 12]\) and \(b_1 \in [12 - 4,\ 12 + 12] = [8, 24]\).
Traps: **(b) \([0,12]\)** stops at \(\Delta \ge -12\) (uses the wrong row) and forgets the upper
limit; **(c) \([4,20]\)** uses \(\Delta = \pm 8\) (a sign/again wrong-row slip); **(d) \([11,13]\)**
is \(\pm 1\), treating the range as "one unit either way".
*If missed:* this is the notes-worthy gap — the RHS-ranging procedure \(B^{-1}(b + \Delta b) \ge 0\)
read straight off the final tableau's slack column.

### Q17 — shadow price when a slack is basic at 6 → **(c) 0**
Reason: complementary slackness — a constraint with positive slack is not binding, so relaxing it
buys nothing; its dual value is 0. (Equivalently: a basic variable has reduced cost 0, and the
shadow price *is* that slack's reduced cost.)
Traps: **(a) 6 / (b) \(\tfrac16\)** treat the slack's *value* as a price; **(d)** you don't need
the objective row — "slack basic and positive" already forces the price to 0.

### Q18 — optimal dual and dual objective → **(a) \(w = \left(\tfrac12, \tfrac32\right)\), dual objective 18**
Reason: the optimal dual variables are the shadow prices, \(w_1 = \tfrac12\), \(w_2 = \tfrac32\).
Dual objective \(= b_1 w_1 + b_2 w_2 = 12\cdot\tfrac12 + 8\cdot\tfrac32 = 6 + 12 = 18\), equal to
the primal optimum (strong duality) — a built-in check.
Traps: **(b)** swaps \(w_1, w_2\); **(c)** uses the objective coefficients as dual values;
**(d)** \(w = 0\) would need both primal constraints non-binding, but both are tight here.

---

## Marking summary

| Part | Items | Marks | Tests |
|---|---|--:|---|
| A — graphical method | Q1–Q6 | 6 | corner enumeration, binding set, gradient direction, unbounded / multiple-optima recognition |
| B — simplex method | Q7–Q13 | 7 | standard form, entering rule, minimum-ratio test, tableau reading, optimality criterion |
| C — sensitivity for simplex | Q14–Q18 | 5 | shadow prices off the \(z\)-row, RHS \(\Delta z\), RHS ranging, complementary slackness, dual solution + strong-duality check |
| **Total** | **18** | **18** | |

**Answer key (single line):**
`1b 2c 3b 4b 5c 6c 7b 8a 9b 10b 11a 12c 13a 14b 15c 16a 17c 18a`

**Confidence classes** (per the grading rules): every item here is *derivable* — the method is
unambiguous and the arithmetic checks. Q8 has a *convention* footnote (the "most negative"
entering rule is one choice; the lecturer's transcripts say any negative may enter, but the
worked tableaux and every course example use most-negative, so **(a)** is the intended answer and
choosing \(x_2\) first is still wrong here because the question fixes the rule).

## After grading — fold misses back in

- A concept miss on **Q7 / Q13 / Q14 / Q17** points at a rule that is already in
  `notes/beginner-notes.tex` (§4 standard form, §5 simplex stopping rule, §6 shadow prices /
  complementary slackness) — re-read that section, and if the note is thin, thicken it per the
  `/update` convention.
- A miss on **Q16** (RHS ranging) is the most likely real gap: `notes/beginner-notes.tex` §6
  states \(B^{-1}(b + \Delta b) \ge 0\) but has no worked range. Adding one (this LP B is a clean
  candidate) is a good `/update`.
- Slips on **Q1 / Q2 / Q12** (wrong vertex, misread RHS) are not notes gaps — they are "slow
  down and check" items for the real quiz.
