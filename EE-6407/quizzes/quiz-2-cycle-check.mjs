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
  const f = G.genFR(r), rows = [...f.prompt.matchAll(/<tr><th>Class \d<\/th>(.*?)<\/tr>/g)].map(x => [...x[1].matchAll(/<td>([\d.]+)<\/td>/g)].map(y => +y[1]));
  const fr = (mean(rows[0]) - mean(rows[1])) ** 2 / (pvar(rows[0]) + pvar(rows[1]));
  assert.ok(near(f.fields[4][1], fr, 1e-6) && Number.isFinite(fr) && fr > 0, 'genFR ' + s);
  const q = G.genKM(r), xs = q.prompt.match(/on <b>([\d, ]+)<\/b>/)[1].split(', ').map(Number), init = [...q.prompt.matchAll(/<b>(\d+)<\/b>/g)].map(x => +x[1]);
  const kk = G.kmeans1d(xs, init);
  assert.ok(kk.iters >= 3 && near(q.fields[0][1], Math.min(...kk.c)) && near(q.fields[2][1], kk.sse), 'genKM ' + s);
  const g = G.genGini(r), [p, n, a, b] = [...g.prompt.matchAll(/(\d+)/g)].map(x => +x[1]);
  const t = p + n, w = (a + b) / t * G.gini(a, b) + (t - a - b) / t * G.gini(p - a, n - b);
  assert.ok(near(g.fields[1][1], w) && g.fields[2][1] >= -1e-12, 'genGini ' + s);
}
console.log('quiz-2-cycle: all keys and 8000 generated problems verified');
