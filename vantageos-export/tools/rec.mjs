import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const V={width:1440,height:810};
const b=await chromium.launch();const ctx=await b.newContext({viewport:V,recordVideo:{dir:'vid/raw',size:V}});
await ctx.addInitScript(()=>{addEventListener('DOMContentLoaded',()=>{
 const c=document.createElement('div');c.style.cssText='position:fixed;z-index:2147483647;left:720px;top:900px;width:26px;height:26px;margin:-3px 0 0 -3px;pointer-events:none;transition:left .45s cubic-bezier(.3,.7,.3,1),top .45s cubic-bezier(.3,.7,.3,1)';
 c.innerHTML='<svg width="26" height="26" viewBox="0 0 26 26"><path d="M3 2 L3 21 L8.5 16 L12 24 L15.5 22.5 L12 15 L19.5 15 Z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/></svg>';
 document.body.appendChild(c);
 addEventListener('mousemove',e=>{c.style.left=e.clientX+'px';c.style.top=e.clientY+'px'},true);
 addEventListener('mousedown',e=>{const r=document.createElement('div');r.style.cssText='position:fixed;z-index:2147483646;pointer-events:none;left:'+e.clientX+'px;top:'+e.clientY+'px;width:12px;height:12px;margin:-6px;border-radius:50%;border:3px solid #22D3EE;transition:all .5s ease-out;opacity:1';document.body.appendChild(r);requestAnimationFrame(()=>{r.style.width=r.style.height='54px';r.style.margin='-27px';r.style.opacity='0'});setTimeout(()=>r.remove(),600)},true);
});});
const pg=await ctx.newPage();const w=ms=>pg.waitForTimeout(ms);const glide=async sel=>{await pg.hover(sel);await pg.waitForTimeout(500);await pg.click(sel)};const base='file://'+process.cwd()+'/vid/';
await pg.goto(base+'title.html');await w(3200);
await pg.goto(base+'page.html');await w(600);
await pg.evaluate(()=>{document.documentElement.style.scrollBehavior='auto'});
await pg.locator('#modsH').scrollIntoViewIfNeeded();await pg.evaluate(()=>window.scrollBy(0,-40));await w(1800);
await pg.evaluate(()=>{const h=document.querySelector('#modsH');window.scrollTo({top:h.getBoundingClientRect().top+scrollY+320,behavior:'smooth'})});await w(1600);
const card=pg.locator('.modcard',{hasText:'Safety Command'}).first();await card.hover();await w(900);await card.click();await w(2600);
for(let i=0;i<4;i++){await glide('#tourNext');await w(2300);}
await glide('#tourNext');await w(2400);
await glide('#tourShow');await w(1800);await glide('#tourShow');await w(400);
await pg.hover('#tourHot button[title="Go to Risks"]');await w(900);await glide('#tourHot button[title="Go to Risks"]');await w(2200);
for(let i=0;i<2;i++){await glide('#tourNext');await w(2300);}
await glide('#tourClose');await w(800);
const pc=pg.locator('.modcard',{hasText:'People'}).first();await pc.scrollIntoViewIfNeeded();await w(500);await pc.hover();await w(700);await pc.click();await w(2200);
await glide('#tourTabs button:nth-child(2)');await w(2000);
for(let i=0;i<3;i++){await glide('#tourNext');await w(2200);}
await glide('#tourClose');await w(600);
await pg.evaluate(()=>{const m=document.querySelector('.mobile');window.scrollTo({top:m.getBoundingClientRect().top+scrollY-30,behavior:'smooth'})});await w(2200);
for(const n of [1,2,3,4]){await glide(`#mRoles button:nth-child(${n})`);await w(1900);}
await glide('#mRoles button:nth-child(2)');await w(900);
await glide('#mAlarm');await w(3200);await glide('#mAlarm');await w(1200);
await pg.goto(base+'end.html');await w(3200);
await ctx.close();await b.close();
