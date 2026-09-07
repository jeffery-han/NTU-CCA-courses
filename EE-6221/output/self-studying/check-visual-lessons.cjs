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
console.log('PASS: numerical edge cases, 6 checks, '+count+' KaTeX expressions, IDs and local links.');
