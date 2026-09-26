import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root='/home/user/claude-code/vantageos-website';
const types={'.html':'text/html','.jpg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml'};
const srv=http.createServer((q,r)=>{let p=path.join(root,decodeURIComponent(q.url.split('?')[0]));if(p.endsWith('/'))p+='index.html';fs.readFile(p,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':types[path.extname(p)]||'application/octet-stream'});r.end(d)})}).listen(8770);
const b=await chromium.launch();const errs=[];
for(const contact of ['', 'mailto:hello@example.com']){
 const pg=await b.newPage({viewport:{width:1440,height:900}});pg.on('pageerror',e=>errs.push(e.message));
 if(contact) await pg.addInitScript(c=>{Object.defineProperty(window,'VOS_CONTACT',{get:()=>c,set:()=>{}})},contact);
 await pg.goto('http://localhost:8770/');await pg.waitForTimeout(500);
 await pg.locator('.modcard').nth(3).click();await pg.click('#tourNext');await pg.waitForTimeout(300);
 const walls=await pg.evaluate(()=>getComputedStyle(document.getElementById("wallH")).display+" "+document.getElementById("wallH").textContent.slice(0,30));const t=await pg.textContent('#tourTitle');const img=await pg.$eval('#tourImg',i=>i.naturalWidth);await pg.keyboard.press('Escape');
 await pg.click('#mAlarm');
 const core=await pg.evaluate(()=>({msg:document.getElementById('coreMsg').textContent,wall:getComputedStyle(document.getElementById("nerdWallH")).display,cards:document.getElementById('cards').hidden,btn:[...document.querySelectorAll('#coreBox a.btn')].map(a=>a.textContent+' '+a.href)}));
 console.log(JSON.stringify({contact,t,img,walls,core}));
 if(contact){await pg.locator('#coreBox').scrollIntoViewIfNeeded();await pg.waitForTimeout(300);await pg.locator('#coreBox').screenshot({path:'core.png'});}
}
console.log('errors',errs);await b.close();srv.close();
