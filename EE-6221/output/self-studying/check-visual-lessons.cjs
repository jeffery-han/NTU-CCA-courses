const assert=require('node:assert/strict'), fs=require('node:fs'), path=require('node:path');
const K=require('./self-study-assets/visual-lessons.js'), katex=require('./self-study-assets/katex/katex.min.js');
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-8,a+' != '+b);
K.forward(0,Math.PI/2).forEach((v,i)=>near(v,[1,1][i]));
assert.deepEqual(K.transform(2),[2,3]);
for(const [x,y] of [[1,1],[-1,1],[0,2],[.2,-.3],[1.9,0]]) {
 const r=K.inverse(x,y);assert.equal(r.kind,'reachable');
 r.branches.forEach(q=>K.forward(...q).forEach((v,i)=>near(v,[x,y][i])));
}
assert.equal(K.inverse(0,0).kind,'folded');assert.equal(K.inverse(2.1,0).kind,'unreachable');assert.equal(K.inverse(2,0).branches.length,1);
for(const T of [1,2,5]) {
 const a=K.cubic(0,T),b=K.cubic(T,T),m=K.cubic(T/2,T);
 near(a[0],0);near(b[0],1);near(a[1],0);near(b[1],0);near(m[0],.5);near(m[1],1.5/T);near(m[2],0);
}
const bank=JSON.parse(fs.readFileSync(path.join(__dirname,'notes-bank.json'),'utf8'));
let count=0;
for(const s of bank.sections) {
 assert.ok(s.visual_lesson_html.includes('data-correct="true"'));
 for(const text of [s.visual_lesson_html,s.content,...s.examples.map(x=>x.text),...s.exercises.map(x=>x.text)])
  for(const m of text.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$]*?)\$/g)) {
   const math=m[1]??m[2];
   assert.ok(!/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(math),'Control character in math');
   katex.renderToString(math,{throwOnError:true,displayMode:m[1]!==undefined});count++;
  }
}
const page=fs.readFileSync(path.join(__dirname,'beginner-notes.html'),'utf8'),ids=[...page.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(ids).size,ids.length,'Duplicate IDs');
for(const m of page.matchAll(/(?:href|src)="([^"]+)"/g)) {
 if(m[1].startsWith('#')) assert.ok(ids.includes(m[1].slice(1)));
 else if(!m[1].includes('://')) assert.ok(fs.existsSync(path.resolve(__dirname,m[1])),m[1]);
}
// Quiz 2 page: helpers, IDs, links (PDF #page anchors), and every pop-up slide image.
const Q2=require('./self-study-assets/quiz2-lessons.js');
assert.deepEqual(Q2.tof(340,0.01),{roundTrip:3.4,range:1.7});
assert.deepEqual(Q2.project(800,400,300,0.3,0.6,3).map(Math.round),[480,460]);
assert.deepEqual(Q2.project(800,400,300,0.6,1.2,6),Q2.project(800,400,300,0.3,0.6,3));
const r=Q2.fuse(20,4,26,2);near(r.x,24);near(r.P,4/3);near(r.K,2/3);
for(const [z1,s1,z2,s2] of [[0,1,10,1],[3,.5,9,10],[20,10,10,.5]]) {
 const q=Q2.fuse(z1,s1,z2,s2);near(q.w1+q.w2,1);assert.ok(q.P<Math.min(s1,s2));near(q.x,z1+q.K*(z2-z1));
}
const page2=fs.readFileSync(path.join(__dirname,'beginner-notes-quiz-2.html'),'utf8'),ids2=[...page2.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
assert.equal(new Set(ids2).size,ids2.length,'Duplicate IDs (quiz 2)');
for(const m of page2.matchAll(/(?:href|src)="([^"]+)"/g)) {
 if(m[1].startsWith('#')) assert.ok(ids2.includes(m[1].slice(1)),m[1]);
 else if(!m[1].includes('://')) assert.ok(fs.existsSync(path.resolve(__dirname,m[1].split('#')[0])),m[1]);
}
let pops=0;
for(const m of page2.matchAll(/data-pages="([^:]+):(\d+)-(\d+)"/g)) for(let p=+m[2];p<=+m[3];p++,pops++)
 assert.ok(fs.existsSync(path.join(__dirname,'quiz2-pages',m[1]+'-p'+String(p).padStart(3,'0')+'.jpg')),m[1]+' p'+p);
assert.ok(!/Lec [1-4] pp?\. \d/.test(page2.replace(/<a [^>]*data-pages[^>]*>[^<]*<\/a>/g,'').replace(/<[^>]+>/g,'')),'Unlinked slide citation');
// Every numeric check's data-answer must equal an independently recomputed value; no unlisted or missing ids.
const calc={
 'calc-k-gain':3/(3+1), 'calc-p-next':3*1/(3+1),
 'calc-three-x':(10/6+13/3+15/2)/(1/6+1/3+1/2), 'calc-three-p':1/(1/6+1/3+1/2),
 'calc-db':10*Math.log10(4/0.002), 'calc-precision':10/0.02, 'calc-accel-drift':0.5*0.02*10**2,
 'calc-echo':340*0.025/2, 'calc-laser-ps':2*0.015/3e8*1e12,
 'calc-bytes':100*100*3, 'calc-proj-u':600*(0.5/2.5)+320, 'calc-proj-v':500*(-0.2/2.5)+240,
 'calc-depth-size':800*1.8/120, 'calc-extrinsic-v':800*(0.2/(2+2))+300,
 'calc-homog-mx':0.4/(0.5*0.4+1),
 'calc-var-uniform':(0+4+16)/3-((0+2+4)/3)**2, 'calc-var-combo':0.5**2*4+(-2)**2*1, 'calc-avg-n':(1/4)**2*4*8,
 'calc-equal-w':0.25*4+0.25*2,
 'calc-batch-p':(()=>{const P=2,a=1,b=2,d=a*b+P*(a+b),K1=P*b/d,K2=P*a/d;return (1-K1-K2)**2*P+K1**2*a+K2**2*b;})(),
};
const found=[...page2.matchAll(/<fieldset class="check calc" id="([^"]+)" data-answer="([^"]+)"/g)];
assert.deepEqual(found.map(m=>m[1]).sort(),Object.keys(calc).sort(),'calc ids');
for(const m of found) assert.ok(Math.abs(+m[2]-calc[m[1]])<=1e-3*Math.max(1,Math.abs(calc[m[1]])),m[1]+': '+m[2]+' != '+calc[m[1]]);
const checks=(page.match(/class="check"/g)||[]).length+(page2.match(/class="check"/g)||[]).length;
console.log('PASS: numerical edge cases, '+checks+' checks over 2 pages, '+count+' KaTeX expressions, IDs, local links, '+pops+' pop-up slide images, '+found.length+' numeric answers.');
