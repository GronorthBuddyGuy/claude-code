import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root='site';
const srv=http.createServer((q,r)=>{let p=path.join(root,decodeURIComponent(q.url.split('?')[0]));if(p.endsWith('/'))p+='index.html';fs.readFile(p,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':p.endsWith('.html')?'text/html':'image/jpeg'});r.end(d)})}).listen(8765);
const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1440,height:900}});
const errs=[]; pg.on('pageerror',e=>errs.push(e.message)); pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await pg.goto('http://localhost:8765/');
await pg.waitForTimeout(800);
const cards=await pg.$$eval('.modcard',bs=>bs.map(b=>b.querySelector('b').textContent+' | '+b.querySelector('.ms').textContent+(b.disabled?' [disabled]':'')));
console.log(cards.join('\n'));
await pg.locator('.modcard',{hasText:'Safety Command'}).click();
await pg.waitForTimeout(500);
await pg.screenshot({path:'shot1.png'});
await pg.click('#tourNext'); await pg.click('#tourNext'); await pg.waitForTimeout(600);
await pg.screenshot({path:'shot2.png'});
console.log('kick',await pg.textContent('#tourKick'),'| next:',await pg.textContent('#tourNext'),'| hot',await pg.$$eval('#tourHot button',x=>x.map(b=>b.title).join(',')));
// click a live hotspot: Risks tab
await pg.click('#tourHot button[title="Go to Risks"]'); await pg.waitForTimeout(400);
console.log('after hotspot:',await pg.textContent('#tourTitle'));
// walk every module to the end
for(const c of cards.filter(c=>!c.includes('disabled'))){
  const name=c.split(' | ')[0];
  await pg.keyboard.press('Escape');
  await pg.locator('.modcard',{hasText:name}).first().click();
  let n=0; while(!(await pg.isHidden('#tour')) && n<80){await pg.keyboard.press('ArrowRight');n++}
  console.log(name,'steps',n);
}
await pg.setViewportSize({width:390,height:844});
await pg.locator('.modcard',{hasText:'People'}).first().click();
await pg.click('#tourNext');await pg.waitForTimeout(600);
await pg.screenshot({path:'shot3.png'});
console.log('errors',errs);
await b.close(); srv.close();
