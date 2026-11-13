// Verifies quiz-2-cycle.html: Train step keys, Test rubric numbers, and the Retrain generators.
// Run: node quiz-2-cycle-check.mjs   (from this folder)
import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';

const html = readFileSync(new URL('./quiz-2-cycle.html', import.meta.url), 'utf8');
const gen = html.slice(html.indexOf('// GEN-START'), html.indexOf('// GEN-END'));
const trainSrc = html.slice(html.indexOf('const TRAIN = ['), html.indexOf('const PEAK_POINTS'));
const G = new Function(gen + '\nconst cite=()=>"";\n' + trainSrc + '\nreturn {close,parseNum,mkRng,genCM,genFR,genKM,genGini,kmeans1d,gini,TRAIN};')();
const near = (a, b, t = 1e-9) => Math.abs(a - b) <= t;
const has = s => assert.ok(html.includes(s), 'missing in page: ' + s);

// ---- input parsing
assert.ok(G.close('89.36', 126 / 141) && G.close('0.8936', 126 / 141) && G.close('7/3', 7 / 3) && !G.close('0.88', 126 / 141));

// ---- Train keys, recomputed independently
const k = Object.fromEntries(G.TRAIN.map(m => [m.id, m.steps.map(s => s[1])]));
const cm = (TP, FP, FN, TN) => { const P = TP / (TP + FP), R = TP / (TP + FN); return { acc: (TP + TN) / (TP + FP + FN + TN), P, R, spec: TN / (TN + FP), F: 2 * P * R / (P + R) }; };
let m = cm(126, 11, 15, 100);
[126, 11, 15, 252, m.acc, m.P, m.R, m.spec, m.F].forEach((v, i) => assert.ok(near(k.t1[i], v), 't1 step ' + (i + 1)));
m = cm(240, 15, 10, 135);
[10, 240, 135, m.P, m.R, m.F].forEach((v, i) => assert.ok(near(k.t2[i], v), 't2 step ' + (i + 1)));
const mean = a => a.reduce((s, x) => s + x, 0) / a.length, pvar = a => mean(a.map(x => (x - mean(a)) ** 2));
const c1 = [1.2, 1, 0.9, 1.1], c2 = [2.2, 2.3, 2.1, 2];
[mean(c1), mean(c2), pvar(c1), pvar(c2), (mean(c1) - mean(c2)) ** 2 / (pvar(c1) + pvar(c2))].forEach((v, i) => assert.ok(near(k.t3[i], v, 1e-9), 't3 step ' + (i + 1)));
const km = G.kmeans1d([1, 2, 4, 7, 8, 10], [1, 4]);
assert.equal(km.iters, 3);
assert.ok(near(k.t4[0], 1.5) && near(k.t4[1], 7.25) && k.t4[2] === 1 && near(k.t4[3], km.c[0]) && near(k.t4[4], km.c[1]) && near(k.t4[5], km.sse));
[G.gini(5, 3), G.gini(1, 3), 0.5 * G.gini(1, 3), G.gini(5, 3) - 0.5 * G.gini(1, 3)].forEach((v, i) => assert.ok(near(k.t5[i], v), 't5 step ' + (i + 1)));

// ---- Test Q1
m = cm(135, 30, 25, 210);
assert.ok(near(m.acc, 0.8625) && near(m.R, 0.84375) && near(m.spec, 0.875));
has('0.8625'); has('0.1375'); has('0.8438'); has('0.8750'); has('0.8182'); has('0.8308');
const m2 = cm(135, 60, 25, 420);
assert.ok(near(m2.R, m.R) && near(m2.spec, m.spec));
has(m2.P.toFixed(4)); has(m2.F.toFixed(4)); has((555 / 640).toFixed(4)); has((85 / 640).toFixed(4));

// ---- Test Q2: 2-D k-means
const P = { A: [1, 1], B: [2, 1], C: [1, 3], D: [5, 4], E: [6, 5], F: [4, 5], G: [3, 3] };
const d2 = (p, c) => (p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2;
let cs = [P.A, P.B], hist = [];
for (let it = 0; it < 10; it++) {
  const asg = Object.fromEntries(Object.entries(P).map(([n, p]) => { const a = d2(p, cs[0]), b = d2(p, cs[1]); assert.notEqual(a, b, 'tie at ' + n); return [n, a < b ? 0 : 1]; }));
  hist.push(asg);
  cs = [0, 1].map(j => { const g = Object.keys(P).filter(n => asg[n] === j); return [mean(g.map(n => P[n][0])), mean(g.map(n => P[n][1]))]; });
  if (it && JSON.stringify(hist[it]) === JSON.stringify(hist[it - 1])) break;
}
assert.equal(hist.length, 3, 'converges on 3rd pass');
assert.deepEqual(Object.keys(P).filter(n => hist[0][n] === 0), ['A', 'C']);
assert.deepEqual(Object.keys(P).filter(n => hist[1][n] === 0), ['A', 'B', 'C']);
assert.ok(near(cs[0][0], 4 / 3) && near(cs[0][1], 5 / 3) && near(cs[1][0], 4.5) && near(cs[1][1], 4.25));
const sse = Object.keys(P).reduce((s, n) => s + d2(P[n], cs[hist[2][n]]), 0);
assert.ok(near(sse, 133 / 12)); has('11.0833');
assert.ok(near(d2(P.B, cs[0]), 8 / 9) && near(d2(P.B, cs[1]), 16.8125) && near(d2(P.G, cs[0]), 41 / 9) && near(d2(P.G, cs[1]), 3.8125));

// ---- Pre-retrain review: independently verify worked SSE terms and unequal child weights.
['A', 'B', 'C'].forEach((name, i) => assert.ok(near(d2(P[name], cs[0]), [5 / 9, 8 / 9, 17 / 9][i]), 'review SSE ' + name));
['D', 'E', 'F', 'G'].forEach((name, i) => assert.ok(near(d2(P[name], cs[1]), [.3125, 2.8125, .8125, 3.8125][i]), 'review SSE ' + name));
const reviewRoot = G.gini(6, 4), reviewRight = G.gini(2, 4), reviewWeighted = 4 / 10 * G.gini(4, 0) + 6 / 10 * reviewRight;
assert.ok(near(reviewRoot, .48) && near(reviewRight, 4 / 9) && near(reviewWeighted, 4 / 15));
assert.ok(near(reviewRoot - reviewWeighted, 16 / 75));
has('4/15 ≈ 0.2667'); has('16/75 ≈ 0.2133');

// ---- Test Q3: Fisher ratios and the unsquared-sigma trap
const feats = { x1: [4, 6, .6, .8], x2: [2, 2.5, .3, .4], x3: [10, 13, 1.5, 1.5], x4: [7, 7.6, .3, .4] };
const R = Object.fromEntries(Object.entries(feats).map(([f, [a, b, s1, s2]]) => [f, (a - b) ** 2 / (s1 ** 2 + s2 ** 2)]));
assert.ok(near(R.x1, 4) && near(R.x2, 1) && near(R.x3, 2) && near(R.x4, 1.44));
assert.deepEqual(Object.keys(R).sort((a, b) => R[b] - R[a]), ['x1', 'x3', 'x4', 'x2']);
const Rw = Object.fromEntries(Object.entries(feats).map(([f, [a, b, s1, s2]]) => [f, (a - b) ** 2 / (s1 + s2)]));
assert.equal(Object.keys(Rw).sort((a, b) => Rw[b] - Rw[a])[0], 'x3', 'trap should put x3 first');

// ---- Rubric totals 100
const rub = html.slice(html.indexOf('const RUBRIC = ['), html.indexOf('const TOPICS'));
const marks = [...rub.matchAll(/\['q\d', '\w+', (\d+),/g)].map(x => +x[1]);
assert.equal(marks.reduce((s, x) => s + x, 0), 100);

// ---- Generators: 2000 draws each, answers re-derived from the prompt numbers
for (let s = 1; s <= 2000; s++) {
  const r = G.mkRng(s);
  const c = G.genCM(r), nums = [...c.prompt.matchAll(/<td>(\d+)<\/td>/g)].map(x => +x[1]);
  const rowsPred = c.prompt.includes('rows are the predicted');
  const [TP, FP, FN, TN] = rowsPred ? nums : [nums[0], nums[2], nums[1], nums[3]];
  const e = cm(TP, FP, FN, TN);
  [e.acc, e.R, e.spec, e.P, e.F].forEach((v, i) => assert.ok(near(c.fields[i][1], v), 'genCM ' + s));
  const factorCM = cm(TP, 2 * FP, FN, 2 * TN);
  [TP + FN, TP + FP, e.R, e.spec, factorCM.P, factorCM.F, factorCM.acc, 1 - factorCM.acc, 1]
    .forEach((v, i) => assert.ok(near(c.fields[i + 5][1], v), 'class-count change ' + s));
  // Swapping precision and recall must fail at least one field whenever FP != FN.
  if (FP !== FN) assert.ok(!G.close(String(e.P), e.R) || !G.close(String(e.R), e.P), 'metric swap ' + s);
  const f = G.genFR(r);
  const rows = [...f.prompt.matchAll(/<tr><th>x(\d)<\/th>(.*?)<\/tr>/g)].map(x => ({
    id: +x[1], values: [...x[2].matchAll(/<td>([\d.]+)<\/td>/g)].map(y => +y[1])
  }));
  const ratios = rows.map(({id, values: [a, b, s1, s2]}) => ({id, R: (a - b) ** 2 / (s1 ** 2 + s2 ** 2)}));
  ratios.forEach((v, i) => assert.ok(near(rows[i].values[4], v.R, .000051), 'supplied Fisher value ' + s));
  assert.equal(f.fields[0][2][f.fields[0][1] - 1], 'σ₁² + σ₂²');
  ratios.sort((a, b) => b.R - a.R).forEach((v, i) => assert.equal(f.fields[i + 1][1], v.id, 'ranking ' + s));
  const q = G.genKM(r);
  const points = [...q.prompt.matchAll(/<tr><th>([A-G])<\/th><td>(\d+)<\/td><td>(\d+)<\/td><\/tr>/g)]
    .map(x => [+x[2], +x[3]]);
  assert.equal(points.length, 7);
  let centers = [points[0], points[1]], last = null, passes = [], centerHistory = [];
  for (let it = 0; it < 10; it++) {
    const assignments = points.map(p => {
      const a = d2(p, centers[0]), b = d2(p, centers[1]);
      assert.notEqual(a, b, 'no tie ' + s);
      return a < b ? 0 : 1;
    });
    passes.push(assignments);
    centers = [0, 1].map(j => [0, 1].map(dim => mean(points.filter((_, i) => assignments[i] === j).map(p => p[dim]))));
    centerHistory.push(centers);
    if (last && assignments.every((v, i) => v === last[i])) break;
    last = assignments;
  }
  assert.equal(passes.length, 3, '2-D convergence ' + s);
  assert.deepEqual(passes[0], [0, 1, 0, 1, 1, 1, 1]);
  assert.deepEqual(passes[1], [0, 0, 0, 1, 1, 1, 1]);
  const first = centerHistory[0];
  const clusterSSE = [0, 1].map(j => points.reduce((sum, p, i) => sum + (passes[2][i] === j ? d2(p, centers[j]) : 0), 0));
  const display = v => String(Math.round(v * 10000) / 10000);
  const suppliedDistances = [...q.prompt.matchAll(/squared distances <b>([\d.]+) to c₁<\/b> and <b>([\d.]+) to c₂<\/b>/g)].map(x => [+x[1], +x[2]]);
  assert.equal(suppliedDistances.length, 2);
  [points[1], points[6]].forEach((point, i) => {
    const cc = i === 0 ? first : centers;
    suppliedDistances[i].forEach((v, j) => assert.ok(near(v, d2(point, cc[j]), .000051), 'supplied distance ' + s));
  });
  const suppliedSSE = q.prompt.match(/Cluster SSEs are already calculated: <b>([\d.]+)<\/b> and <b>([\d.]+)<\/b>; total <b>([\d.]+)<\/b>/);
  [...clusterSSE, clusterSSE[0] + clusterSSE[1]].forEach((v, i) => assert.ok(near(+suppliedSSE[i + 1], v, .000051), 'supplied SSE ' + s));
  const selected = field => field[2][field[1] - 1];
  assert.equal(q.fields[0][1], passes[1][1] + 1);
  assert.equal(selected(q.fields[1]), 'Means of the new members: (' + centers[0].map(display).join(', ') + ') and (' + centers[1].map(display).join(', ') + ')');
  assert.equal(q.fields[2][1], passes[2][6] + 1);
  assert.equal(selected(q.fields[3]), 'Yes: a full assignment pass changes no memberships');
  assert.equal(selected(q.fields[4]), 'Sum of squared distances to each point’s final assigned centroid');
  const g = G.genGini(r), [p, n, a, b] = [...g.prompt.matchAll(/(\d+)/g)].map(x => +x[1]);
  const t = p + n, left = a + b, right = t - left;
  const w = left / t * G.gini(a, b) + right / t * G.gini(p - a, n - b);
  assert.notEqual(left, right, 'weighting distractors must be different ' + s);
  assert.equal(selected(g.fields[0]), '(' + left + '/' + t + ') GL + (' + right + '/' + t + ') GR');
  assert.equal(selected(g.fields[1]), 'Root Gini − weighted child Gini');
  assert.equal(g.fields[2][1], left > right ? 1 : 2);
  assert.ok(g.prompt.includes('root Gini = ' + display(G.gini(p, n))) && g.prompt.includes('left Gini GL = ' + display(G.gini(a, b))) && g.prompt.includes('right Gini GR = ' + display(G.gini(p - a, n - b))));
  assert.ok(g.key.includes('weighted Gini is ' + display(w)) && g.key.includes('Gini = ' + display(G.gini(p, n) - w)));
  for (const problem of [f, q, g]) {
    for (const field of problem.fields) {
      assert.equal(new Set(field[2]).size, field[2].length, 'distinct dropdown choices ' + s);
      assert.ok(Number.isInteger(field[1]) && field[1] >= 1 && field[1] <= field[2].length);
      assert.ok(G.close(String(field[1]), field[1]) && !G.close('', field[1]));
      for (let wrong = 1; wrong <= field[2].length; wrong++) if (wrong !== field[1]) assert.ok(!G.close(String(wrong), field[1]));
    }
  }
}
// Targeted queue keeps past Train/Test storage and makes peaking optional.
has("const KEY = 'ee6407-quiz2-cycle-v1'");
const topicSrc = html.slice(html.indexOf('const TOPICS = {'), html.indexOf('function renderRubric()'));
const stateSrc = html.slice(html.indexOf('function openTopics()'), html.indexOf('/* ---------------- RETRAIN: generators'));
const mockState = { re: {}, rubric: {} };
const queue = new Function('S', 'RUBRIC', 'genCM', 'genKM', 'genFR', 'genGini', topicSrc + stateSrc + ';return {topicState};')
  (mockState, [], G.genCM, G.genKM, G.genFR, G.genGini);
for (const name of ['cm', 'km', 'fr', 'gini']) assert.equal(queue.topicState(name), 'open');
assert.equal(queue.topicState('peak'), 'opt');
mockState.re.cm = {closed: true};
assert.equal(queue.topicState('cm'), 'closed');
// Dropdowns use the existing saved-value and numeric-checking path.
const drawSrc = html.slice(html.indexOf('function drawProblem(k)'), html.indexOf("document.addEventListener('click', e => {\n  const g ="));
const problem = G.genKM(G.mkRng(42)), box = {};
const draw = new Function('live', '$', 'typeset', 'f4', drawSrc + ';return drawProblem;')
  ({km: problem}, () => box, () => {}, v => String(v));
draw('km');
assert.equal((box.innerHTML.match(/<select /g) || []).length, problem.fields.length);
assert.ok(!box.innerHTML.includes(' selected'));
problem.vals = problem.fields.map(f => String(f[1])); problem.res = problem.fields.map(() => true); problem.done = true;
draw('km');
assert.equal((box.innerHTML.match(/ selected/g) || []).length, problem.fields.length);
problem.res[0] = false;
draw('km');
assert.ok(box.innerHTML.includes('→ Cluster 1'), 'feedback names the option rather than a numeric code');
console.log('quiz-2-cycle: reviews, dropdown rendering, targeted queue and 8000 generated problems verified');
