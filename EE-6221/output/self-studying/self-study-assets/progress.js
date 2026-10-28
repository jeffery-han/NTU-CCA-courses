'use strict';
// Keep answered checks across refreshes. Load after the page's lesson script: saved answers are replayed
// through the existing click handlers, so feedback and tallies rebuild themselves. A check is keyed by its
// section id + legend (asserted unique by check-visual-lessons.cjs). Without storage (private mode, blocked
// site data) the page still works; progress is simply not kept.
(()=>{
 const key='self-study-progress:'+location.pathname;
 const id=f=>(f.closest('section')||{}).id+'|'+((f.querySelector('legend')||{}).textContent||'');
 let saved={},replaying=true;
 try{saved=JSON.parse(localStorage.getItem(key))||{};}catch{}
 const store=()=>{try{localStorage.setItem(key,JSON.stringify(saved));}catch{}};
 document.addEventListener('click',e=>{
  const b=e.target.closest('.check button');
  if(!b||replaying) return;
  const f=b.closest('fieldset'),input=f.querySelector('input');
  saved[id(f)]=input?{v:input.value}:{b:[...f.querySelectorAll('button')].indexOf(b)};
  store();
 });
 document.querySelectorAll('.check').forEach(f=>{
  const s=saved[id(f)],input=f.querySelector('input'),buttons=f.querySelectorAll('button');
  if(!s) return;
  if(input&&'v' in s){input.value=s.v;buttons[0].click();}
  else if(!input&&buttons[s.b]) buttons[s.b].click();
 });
 replaying=false;
 document.querySelectorAll('[data-reset-progress]').forEach(b=>b.addEventListener('click',()=>{
  try{localStorage.removeItem(key);}catch{}
  location.reload();
 }));
})();
