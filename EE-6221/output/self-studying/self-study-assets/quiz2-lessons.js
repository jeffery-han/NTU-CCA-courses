'use strict';
const Q2 = {
  tof(c,t) { return {roundTrip:c*t, range:c*t/2}; },
  project(f,u0,v0,x,y,z) { return [f*x/z+u0, f*y/z+v0]; },
  fuse(z1,s1,z2,s2) {
    const w1=s2/(s1+s2), K=s1/(s1+s2);
    return {w1, w2:1-w1, K, x:w1*z1+(1-w1)*z2, P:s1*s2/(s1+s2)};
  }
};
if(typeof module!=='undefined') module.exports=Q2;
if(typeof document!=='undefined') {
 const $=id=>document.getElementById(id), val=id=>Number($(id).value), f=(n,d=2)=>(Math.abs(n)<5e-4?0:n).toFixed(d);
 const blue='#226794',orange='#b55b20',green='#287052',grey='#9eafa7';
 const line=(a,b,c,w=2,dash)=>'<line x1="'+a[0]+'" y1="'+a[1]+'" x2="'+b[0]+'" y2="'+b[1]+'" stroke="'+c+'" stroke-width="'+w+'"'+(dash?' stroke-dasharray="6 5"':'')+'/>';
 const text=(p,t,c='#233b48')=>'<text x="'+p[0]+'" y="'+p[1]+'" style="fill:'+c+'">'+t+'</text>';
 const dot=(p,c,r=5)=>'<circle cx="'+p[0]+'" cy="'+p[1]+'" r="'+r+'" fill="'+c+'"/>';
 function tof() {
  const sound=$('tof-medium').value==='340', t=val('tof-time'), c=sound?340:3e8, s=t*(sound?1e-3:1e-9), r=Q2.tof(c,s);
  $('tof-time-value').textContent=t+(sound?' ms':' ns');
  const x=60+380*t/60;
  $('tof').innerHTML=line([40,50],[40,110],'#233b48',8)+text([20,135],'sensor')+line([x,30],[x,120],orange,6)+text([x-10,140],'wall',orange)
   +line([48,65],[x-6,65],blue,2)+text([(48+x)/2-20,58],'out',blue)+line([x-6,95],[48,95],green,2,true)+text([(48+x)/2-20,88],'back',green);
  $('tof-readout').textContent='Wave covers c·t = '+f(r.roundTrip,3)+' m (round trip, Lec 1 p. 36). Object range = c·t/2 = '+f(r.range,3)+' m (Lec 1 p. 38).';
 }
 function pinhole() {
  const y=val('pin-y'), z=val('pin-z'), s=val('pin-s'), Y=s*y, Z=s*z, [u,v]=Q2.project(800,400,300,0,Y,Z);
  const P=(zz,yy)=>[40+zz*22,150-yy*30];
  let g=line(P(0,0),P(21,0),grey,1)+text([470,170],'z (m)')+line(P(1,-4.6),P(1,4.6),blue,2)+text([P(1,0)[0]+4,22],'z = 1 plane',blue);
  g+=line(P(0,0),P(Z,Y),orange,2)+line(P(0,0),P(21,21*y/z),orange,1,true)+dot(P(Z,Y),orange)+dot(P(1,y/z),green)+dot(P(0,0),'#233b48',4)+text([P(Z,Y)[0]+8,P(Z,Y)[1]-8],'point',orange);
  $('pinhole').innerHTML=g;
  $('pinhole-readout').textContent='m̄ = (0, '+f(Y)+', '+f(Z)+') m → m = (0, '+f(Y/Z,3)+', 1) → pixel (u, v) = ('+f(u,1)+', '+f(v,1)+'). Change λ: the point moves, the pixel does not.';
 }
 function fusion() {
  const z1=val('f-z1'),s1=val('f-s1'),z2=val('f-z2'),s2=val('f-s2'),r=Q2.fuse(z1,s1,z2,s2);
  const X=x=>40+(x-5)*12, pdf=(x,m,v)=>Math.exp(-((x-m)**2)/(2*v))/Math.sqrt(2*Math.PI*v);
  const peak=pdf(0,0,Math.min(s1,s2,r.P)), Y=p=>200-p/peak*170;
  const path=(m,v,c,w)=>{let d='';for(let i=0;i<=200;i++){const x=5+i*0.2;d+=(i?'L':'M')+f(X(x),1)+','+f(Y(pdf(x,m,v)),1)+' ';}return '<path d="'+d+'" fill="none" stroke="'+c+'" stroke-width="'+w+'"/>';};
  let g=line([40,200],[500,200],grey,1);
  for(const t of [10,20,30,40]) g+=text([X(t)-8,220],t);
  g+=path(z1,s1,blue,2)+path(z2,s2,orange,2)+path(r.x,r.P,green,3.5)+text([48,22],'sensor 1',blue)+text([130,22],'sensor 2',orange)+text([212,22],'fused',green);
  $('fusion').innerHTML=g;
  $('fusion-readout').textContent='Weights: '+f(r.w1,3)+' on z₁, '+f(r.w2,3)+' on z₂. Fused x̂ = '+f(r.x,3)+', variance P = '+f(r.P,3)+' (below both '+s1+' and '+s2+'). Sequential view: K = σ₁²/(σ₁²+σ₂²) = '+f(r.K,3)+'.';
 }
 for(const [ids,update] of [[['tof-medium','tof-time'],tof],[['pin-y','pin-z','pin-s'],pinhole],[['f-z1','f-s1','f-z2','f-s2'],fusion]]) {
  if(!$(ids[0])) continue;
  const run=()=>{ids.forEach(id=>{const o=$(id+'-value');if(o&&id!=='tof-time')o.textContent=$(id).value;});update();};
  ids.forEach(id=>$(id).addEventListener('input',run));run();
 }
 const tally=()=>document.querySelectorAll('.score').forEach(el=>{
  const sec=$(el.dataset.for), all=sec.querySelectorAll('.check').length, done=sec.querySelectorAll('.check button[data-result=correct]').length;
  el.textContent=done+'/'+all; el.classList.toggle('complete',done===all);
 });
 document.querySelectorAll('.check button').forEach(button=>button.addEventListener('click',()=>{
  const field=button.closest('fieldset'),correct=button.dataset.correct==='true';
  field.querySelectorAll('button').forEach(b=>{delete b.dataset.result;b.removeAttribute('aria-pressed');});
  button.dataset.result=correct?'correct':'wrong';button.setAttribute('aria-pressed','true');
  field.querySelector('.feedback').textContent=(correct?'Correct. ':'Not quite. ')+button.dataset.feedback;
  tally();
 }));
 tally();
 const dlg=document.querySelector('dialog.page-view');
 dlg.querySelector('button').addEventListener('click',()=>dlg.close());
 dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close();});
 document.querySelectorAll('a[data-pages]').forEach(a=>a.addEventListener('click',e=>{
  e.preventDefault();
  const [stem,range]=a.dataset.pages.split(':'), [lo,hi]=range.split('-').map(Number);
  dlg.querySelector('strong').textContent=a.textContent+' — '+stem.replace(/^part-2-/,'')+(lo===hi?' p. '+lo:' pp. '+lo+'–'+hi);
  dlg.querySelector('.bar a').href=a.href;
  let imgs='';for(let p=lo;p<=hi;p++) imgs+='<img loading="lazy" alt="Slide '+p+'" src="quiz2-pages/'+stem+'-p'+String(p).padStart(3,'0')+'.jpg">';
  dlg.querySelector('.pages').innerHTML=imgs; dlg.showModal(); dlg.scrollTop=0;
 }));
}
