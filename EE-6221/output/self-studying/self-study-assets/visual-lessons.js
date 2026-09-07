'use strict';
const Kinematics = {
  forward(a,b) { return [Math.cos(a)+Math.cos(a+b),Math.sin(a)+Math.sin(a+b)]; },
  inverse(x,y) {
    const r=Math.hypot(x,y);
    if(r>2+1e-10) return {kind:'unreachable',branches:[]};
    if(r<1e-10) return {kind:'folded',branches:[]};
    const b=Math.acos(Math.max(-1,Math.min(1,(r*r-2)/2)));
    return {kind:'reachable',branches:(b<1e-10?[0]:[b,-b]).map(q=>[Math.atan2(y,x)-Math.atan2(Math.sin(q),1+Math.cos(q)),q])};
  },
  cubic(t,T) { const u=t/T; return [3*u*u-2*u**3,6*u*(1-u)/T,(6-12*u)/T**2]; },
  transform(u) { return [2,1+u]; }
};
if(typeof module!=='undefined') module.exports=Kinematics;
if(typeof document!=='undefined') {
 const $=id=>document.getElementById(id), val=id=>Number($(id).value);
 const f=n=>(Math.abs(n)<.0005?0:n).toFixed(2), rad=d=>d*Math.PI/180, deg=r=>r*180/Math.PI;
 const blue='#226794',orange='#b55b20',green='#287052';
 function line(a,b,c,w=3,dash=false) {return '<line x1="'+a[0]+'" y1="'+a[1]+'" x2="'+b[0]+'" y2="'+b[1]+'" stroke="'+c+'" stroke-width="'+w+'" '+(dash?'stroke-dasharray="6 5"':'')+'/>';}
 function text(p,t,c='#233b48') {return '<text x="'+p[0]+'" y="'+p[1]+'" style="fill:'+c+'">'+t+'</text>';}
 function dot(p,c,r=5) {return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="'+r+'" fill="'+c+'"/>';}
 function arrow(a,b,c) {const t=Math.atan2(b[1]-a[1],b[0]-a[0]), end=o=>[b[0]-9*Math.cos(t+o),b[1]-9*Math.sin(t+o)];return line(a,b,c)+line(b,end(.45),c)+line(b,end(-.45),c);}
 const xy=(x,y)=>[260+55*x,165-55*y];
 function axes() {
  let s=line(xy(-3,0),xy(3,0),'#b4c6be',1)+line(xy(0,-2.5),xy(0,2.5),'#b4c6be',1);
  for(const n of [-2,-1,1,2]) s+=text([xy(n,0)[0]-5,185],n)+text([265,xy(0,n)[1]+5],n);
  return s+text([440,170],'x (m)')+text([270,22],'y (m)');
 }
 function rotation() {
  const a=rad(val('angle')),c=Math.cos(a),s=Math.sin(a),o=[260,165],v=(x,y)=>[260+95*x,165-95*y];
  $('rotation').innerHTML=arrow(o,v(1.4,0),blue)+arrow(o,v(0,1.35),blue)+text([405,185],'x_A',blue)+text([270,32],'y_A',blue)+arrow(o,v(c,s),orange)+arrow(o,v(-s,c),orange)+text([v(c,s)[0]+12,v(c,s)[1]+15],'x_B · P',orange)+text([v(-s,c)[0]+12,v(-s,c)[1]-10],'y_B',orange)+dot(v(c,s),green)+text([30,310],'P = 1 × x_B; z axes point out of the page');
  $('rotation-readout').textContent='θ = '+val('angle')+'°. Column 1 = ('+f(c)+', '+f(s)+', 0). Column 2 = ('+f(-s)+', '+f(c)+', 0). P in A = ('+f(c)+', '+f(s)+', 0).';
 }
 function transform() {
  const u=val('distance'),p=Kinematics.transform(u),pt=(x,y)=>[80+x*70,280-y*52];
  $('transform').innerHTML=arrow(pt(0,0),pt(4.8,0),'#b4c6be')+arrow(pt(0,0),pt(0,4.8),'#b4c6be')+arrow(pt(0,0),pt(2,1),blue)+arrow(pt(2,1),pt(...p),orange)+arrow(pt(2,1),pt(1,1),green)+dot(pt(...p),orange)+text([85,310],'A: (0,0)')+text([235,250],'B origin: (2,1)',blue)+text([pt(...p)[0]+12,pt(...p)[1]-10],'P: (2,'+f(p[1])+')',orange)+text([113,215],'y_B',green)+text([235,40],'x_B points upward',orange);
  $('transform-readout').textContent='Local ('+f(u)+', 0, 0) m → rotate to (0, '+f(u)+', 0) m → add (2,1,0) m → ('+f(p[0])+', '+f(p[1])+', 0) m.';
 }
 function links(a,b,c,dash=false) {const e=xy(Math.cos(a),Math.sin(a)),p=xy(...Kinematics.forward(a,b));return line(xy(0,0),e,c,5,dash)+line(e,p,c,5,dash)+dot(e,c)+dot(p,c);}
 function arm() {
  const a=rad(val('q1')),b=rad(val('q2')),p=Kinematics.forward(a,b),e=xy(Math.cos(a),Math.sin(a)),end=xy(...p);
  $('arm').innerHTML=axes()+line(xy(0,0),e,blue,7)+line(e,end,orange,7)+dot(xy(0,0),green,7)+dot(e,blue,7)+dot(end,orange,7)+text([25,290],'Blue: link 1 / x₁ · Orange: link 2 / x₂')+text([25,313],'Base → elbow → tool; z axes point out of page');
  $('arm-readout').textContent='Link directions: '+val('q1')+'° and '+(val('q1')+val('q2'))+'°. Tool = ('+p.map(f).join(', ')+') m. Tool orientation = '+(val('q1')+val('q2'))+'°.';
 }
 function inverse() {
  const x=val('target-x'),y=val('target-y'),r=Kinematics.inverse(x,y),p=xy(x,y);
  let s='<circle cx="260" cy="165" r="110" fill="#e9f3ed" stroke="#92bba4"/>'+axes();
  r.branches.forEach((q,i)=>s+=links(...q,i?orange:blue,i===1));
  $('ik').innerHTML=s+line([p[0]-7,p[1]-7],[p[0]+7,p[1]+7],'#902e46')+line([p[0]-7,p[1]+7],[p[0]+7,p[1]-7],'#902e46')+text([25,308],'Blue solid: branch 1 · orange dashed: branch 2');
  $('ik-readout').textContent=r.kind==='unreachable'?'Unreachable: target distance '+f(Math.hypot(x,y))+' m exceeds the 2 m reach.':r.kind==='folded'?'Target at origin: q₂ = ±180°. Any shoulder angle reaches it: infinitely many solutions.':r.branches.map((q,i)=>'Branch '+(i+1)+': q₁ = '+f(deg(q[0]))+'°, q₂ = '+f(deg(q[1]))+'°; forward check = ('+Kinematics.forward(...q).map(f).join(', ')+') m').join('. ')+(r.branches.length===1?'. Full extension: branches merge.':'. Position matches; orientation may differ.');
 }
 function trajectory() {
  const T=val('duration'),t=T*val('phase')/100,v=Kinematics.cubic(t,T);
  const specs=[['Position q (rad)',0,1.1,blue],['Velocity q̇ (rad/s)',0,1.6,orange],['Acceleration q̈ (rad/s²)',-6.5,6.5,green]];
  $('trajectory-plots').innerHTML=specs.map(([title,min,max,c],j)=>{
   const pt=(t,v)=>[65+t/T*400,160-(v-min)/(max-min)*120];
   let d='';for(let i=0;i<=100;i++){const p=pt(T*i/100,Kinematics.cubic(T*i/100,T)[j]);d+=(i?'L':'M')+p[0]+','+p[1]+' ';}
   return '<svg viewBox="0 0 520 210" role="img" aria-label="'+title+' over time">'+text([20,22],title)+line([65,40],[65,160],'#9eafa7',1)+line(pt(0,0),pt(T,0),'#9eafa7',1)+text([12,48],max)+text([12,160],min)+text([62,187],'0')+text([445,187],f(T))+text([210,202],'time (s)')+'<path d="'+d+'" fill="none" stroke="'+c+'" stroke-width="3"/>'+line([pt(t,0)[0],40],[pt(t,0)[0],160],'#6d7f78',1,true)+dot(pt(t,v[j]),c)+'</svg>';
  }).join('');
  $('trajectory-readout').textContent='At t = '+f(t)+' s: q = '+f(v[0])+' rad, q̇ = '+f(v[1])+' rad/s, q̈ = '+f(v[2])+' rad/s². Peak speed = '+f(1.5/T)+' rad/s. Endpoint accelerations = ±'+f(6/T**2)+' rad/s².';
 }
 for(const [ids,update] of [[['angle'],rotation],[['distance'],transform],[['q1','q2'],arm],[['target-x','target-y'],inverse],[['duration','phase'],trajectory]]) {
  const run=()=>{ids.forEach(id=>$(id+'-value').textContent=$(id).value);update();};
  ids.forEach(id=>$(id).addEventListener('input',run));run();
 }
 document.querySelectorAll('.check button').forEach(button=>button.addEventListener('click',()=>{
  const field=button.closest('fieldset'),correct=button.dataset.correct==='true';
  field.querySelectorAll('button').forEach(b=>{delete b.dataset.result;b.removeAttribute('aria-pressed');});
  button.dataset.result=correct?'correct':'wrong';button.setAttribute('aria-pressed','true');
  field.querySelector('.feedback').textContent=(correct?'Correct. ':'Not quite. ')+button.dataset.feedback;
 }));
}
