import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch(); const errs=[];
for (const [w,h,name] of [[1440,900,'m1'],[390,844,'m2']]){
const pg=await b.newPage({viewport:{width:w,height:h}}); pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file:///home/user/claude-code/vantageos-export/What-is-VantageOS.html'); await pg.waitForTimeout(400);
await pg.locator('.mobile').scrollIntoViewIfNeeded(); await pg.waitForTimeout(300);
await pg.click('#mRoles button:nth-child(2)'); await pg.waitForTimeout(200);
await pg.locator('.mobile').screenshot({path:name+'a.png'});
await pg.click('#mAlarm'); await pg.waitForTimeout(300);
await pg.locator('.mobile').screenshot({path:name+'b.png'});
if(w>1000){await pg.locator('#soonGrid').screenshot({path:'m1c.png'});
 console.log(await pg.$$eval('.modcard[disabled] .soon',x=>x.map(e=>e.textContent)));}
}
console.log('errors',errs); await b.close();
