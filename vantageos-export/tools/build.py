import json, re
import soon
from tourdata import T, ORDER, ALIAS

src = open("orig.html").read().split("\n")
L = lambda n: src[n - 1]  # 1-based

# Sanity: the regions being replaced are where we expect them.
assert L(451).startswith("/* The product tour"), L(451)
assert L(481).startswith(".tour-cap b"), L(481)
assert L(571).startswith('<div class="tour" id="tour"'), L(571)
assert L(580) == "</div>", L(580)
assert L(667).startswith('  <p class="serif">Every module shares'), L(667)
assert L(1051).lstrip().startswith("/* The product tour"), L(1051)
assert L(1109) == "  });", L(1109)
assert "Walk through" in L(1119)

CSS = r"""/* The product tour: the real app, with a guide beside it */
.modcard .shots{font:600 .7rem var(--m);color:var(--orange-ink)}
.modcard[disabled]{opacity:.55;cursor:default}
.modcard[disabled]:hover{transform:none;border-color:var(--line)}
.modcard .soon{font:500 .7rem var(--m);color:var(--ink-faint)}
.tourhow{display:flex;flex-wrap:wrap;gap:8px 18px;font:500 .8rem var(--m);color:var(--ink-soft)}
.tourhow span{display:inline-flex;align-items:center;gap:7px}
.tourhow i{font:800 .72rem var(--b);font-style:normal;width:20px;height:20px;border-radius:50%;display:inline-grid;place-items:center;background:var(--hv-orange);color:#1A0A00}
.tourhow i.o{background:transparent;border:2px dashed var(--hv-orange);color:var(--orange-ink)}
.tour{position:fixed;inset:0;z-index:60;background:rgba(8,9,11,.86);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);
  display:flex;align-items:center;justify-content:center;padding:calc(14px + env(safe-area-inset-top,0px)) 14px calc(14px + env(safe-area-inset-bottom,0px))}
.tour[hidden]{display:none}
.tour-in{width:min(1480px,100%);max-height:100%;display:grid;grid-template-columns:minmax(0,1fr) 350px;grid-template-areas:"win side" "foot side" "cap side";gap:10px 16px;color:#F2EDE6;min-height:0}
@media (max-width:1000px){.tour-in{grid-template-columns:minmax(0,1fr);grid-template-areas:"win" "now" "foot" "side" "cap";overflow:auto;padding-bottom:64px}}
.tour-now{grid-area:now;display:none}
@media (max-width:1000px){
  .tour-now{display:grid;grid-template-columns:26px minmax(0,1fr);gap:2px 10px;background:#12161B;border:1.5px solid var(--hv-orange);border-radius:12px;padding:10px 12px;font-size:.9rem;line-height:1.45;color:#C0B8AE}
  .tour-now i{grid-row:span 2;width:24px;height:24px;border-radius:50%;background:var(--hv-yellow);color:#1A0A00;font:800 .78rem var(--b);font-style:normal;display:grid;place-items:center}
  .tour-now b{color:#F2EDE6}
  .tour-nav{position:fixed;left:0;right:0;bottom:0;z-index:2;background:#0B0F14;border-top:1px solid rgba(255,255,255,.14);padding:10px 14px calc(10px + env(safe-area-inset-bottom,0px))}
}
.tour-win{grid-area:win;background:#0B0F14;border:1px solid rgba(255,255,255,.14);border-radius:14px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.6);display:flex;flex-direction:column;min-height:0}
.tour-bar{display:flex;align-items:center;gap:12px;padding:9px 12px;background:#161B21;border-bottom:1px solid rgba(255,255,255,.1)}
.tour-bar .lights{display:flex;gap:6px}
.tour-bar .lights i{width:11px;height:11px;border-radius:50%;background:#3A4048}
.tour-bar .lights i:first-child{background:#FF5F57}.tour-bar .lights i:nth-child(2){background:#FEBC2E}.tour-bar .lights i:nth-child(3){background:#28C840}
.tour-bar .where{flex:1;min-width:0;font:500 .8rem var(--m);background:#0B0F14;border-radius:999px;padding:5px 12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#C0B8AE}
.tour-bar .where b{color:#F2EDE6;font-weight:600}
.tour-bar button{flex:none;width:32px;height:32px;border-radius:50%;border:1px solid rgba(255,255,255,.25);background:none;color:#F2EDE6;font-weight:800}
.tour-screen{position:relative;overflow:auto;max-height:calc(100vh - 170px)}
@media (max-width:1000px){.tour-screen{max-height:58vh}}
.tour-stage{position:relative;min-width:720px}
.tour-stage img{display:block;width:100%;height:auto}
.tour-hot,.tour-marks{position:absolute;inset:0}
.tour-marks{pointer-events:none}
.tour-hot button{position:absolute;border:0;background:transparent;border-radius:8px;padding:0;cursor:pointer}
.tour-hot button:hover,.tour-hot button:focus-visible,.tour-hot.show button{outline:2px dashed var(--hv-orange);outline-offset:1px;background:rgba(255,106,19,.12)}
.tour-hot.hint button{animation:hint 1.6s ease-in-out 2}
@keyframes hint{50%{background:rgba(255,106,19,.22);outline:2px solid rgba(255,106,19,.7)}}
.tour-spot{position:absolute;border-radius:10px;outline:3px solid var(--hv-orange);box-shadow:0 0 0 200vmax rgba(5,6,8,.55);transition:left .3s,top .3s,width .3s,height .3s,opacity .2s}
.tour-spot[hidden]{display:block;opacity:0}
.tour-pin{position:absolute;pointer-events:auto;width:26px;height:26px;margin:-11px 0 0 -11px;border-radius:50%;border:2px solid #1A0A00;background:var(--hv-orange);color:#1A0A00;font:800 .8rem var(--b);display:grid;place-items:center;padding:0;box-shadow:0 2px 8px rgba(0,0,0,.5);cursor:pointer;transition:transform .15s}
.tour-pin:hover,.tour-pin[aria-current="true"]{transform:scale(1.2);background:var(--hv-yellow)}
.tour-foot{grid-area:foot;display:flex;align-items:center;gap:8px;min-width:0}
.tour-foot>span{flex:none;font:600 .7rem var(--m);letter-spacing:.1em;text-transform:uppercase;color:#958C82}
.tour-tabs{flex:1;min-width:0;display:flex;gap:6px;overflow-x:auto;padding-block:2px;scrollbar-width:thin}
.tour-tabs button{flex:none;border:1.5px solid rgba(255,255,255,.2);background:rgba(255,255,255,.04);color:#F2EDE6;border-radius:999px;padding:6px 13px;font:600 .8rem var(--b)}
.tour-tabs button b{font:800 .72rem var(--m);margin-right:6px;opacity:.7}
.tour-tabs button[aria-current="true"]{background:var(--hv-orange);border-color:var(--hv-orange);color:#1A0A00}
.tour-side{grid-area:side;background:#12161B;border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:18px 18px 16px;display:flex;flex-direction:column;gap:12px;min-height:0;overflow:auto;align-self:stretch}
.tour-side .kick{font:600 .7rem var(--m);letter-spacing:.12em;text-transform:uppercase;color:#FF9A5C}
.tour-side h3{font:800 1.9rem/1 var(--d);color:#F2EDE6}
.tour-side .sum{color:#C0B8AE;font-size:.95rem;line-height:1.5}
.tour-notes{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.tour-notes button{width:100%;text-align:left;display:grid;grid-template-columns:26px minmax(0,1fr);gap:2px 10px;align-items:start;background:rgba(255,255,255,.03);border:1.5px solid rgba(255,255,255,.1);border-radius:10px;padding:9px 10px;color:#F2EDE6}
.tour-notes button i{grid-row:span 2;width:24px;height:24px;border-radius:50%;background:var(--hv-orange);color:#1A0A00;font:800 .78rem var(--b);font-style:normal;display:grid;place-items:center}
.tour-notes button b{font:700 .92rem var(--b)}
.tour-notes button span{grid-column:2;font-size:.86rem;line-height:1.45;color:#B3B9BF;display:none}
.tour-notes button:hover{border-color:rgba(255,255,255,.3)}
.tour-notes button[aria-current="true"]{border-color:var(--hv-orange);background:rgba(255,106,19,.1)}
.tour-notes button[aria-current="true"] i{background:var(--hv-yellow)}
.tour-notes button[aria-current="true"] span{display:block}
.tour-live{display:flex;flex-direction:column;gap:8px;border:1px dashed rgba(255,106,19,.55);border-radius:10px;padding:10px 12px;font-size:.84rem;color:#C0B8AE}
.tour-live b{color:#F2EDE6}
.tour-live button{align-self:flex-start;border:1.5px solid rgba(255,255,255,.3);background:none;color:#F2EDE6;border-radius:999px;padding:5px 12px;font:600 .78rem var(--b)}
.tour-live button[aria-pressed="true"]{background:var(--hv-orange);border-color:var(--hv-orange);color:#1A0A00}
.tour-nav{display:flex;gap:8px;margin-top:auto;padding-top:4px}
.tour-nav button{border-radius:999px;font-weight:700;font-size:.9rem;padding:10px 16px;border:2px solid rgba(255,255,255,.3);background:none;color:#F2EDE6}
.tour-nav button.next{flex:1;background:var(--hv-orange);border-color:var(--hv-orange);color:#1A0A00;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tour-nav button:disabled{opacity:.35;cursor:default}
.tour-cap{grid-area:cap;font-size:.82rem;color:#958C82}
.tour-cap b{color:var(--hv-yellow)}"""

MODAL = """<div class="tour" id="tour" hidden role="dialog" aria-modal="true" aria-labelledby="tourTitle">
 <div class="tour-in">
  <div class="tour-win">
   <div class="tour-bar"><span class="lights" aria-hidden="true"><i></i><i></i><i></i></span><span class="where" id="tourWhere"></span><button type="button" id="tourClose" aria-label="Close the tour">×</button></div>
   <div class="tour-screen" id="tourScreen"><div class="tour-stage"><img id="tourImg" alt="" width="1440" height="900"><div class="tour-hot" id="tourHot"></div><div class="tour-marks" id="tourMarks"><div class="tour-spot" id="tourSpot" hidden></div></div></div></div>
  </div>
  <div class="tour-now" id="tourNow" aria-hidden="true"></div>
  <div class="tour-foot"><span>Screens</span><div class="tour-tabs" id="tourTabs" role="group" aria-label="Screens in this module"></div></div>
  <aside class="tour-side" aria-live="polite">
   <span class="kick" id="tourKick"></span>
   <h3 id="tourTitle"></h3>
   <p class="sum" id="tourSum"></p>
   <ol class="tour-notes" id="tourNotes" aria-label="What's on this screen"></ol>
   <div class="tour-live"><span><b>This picture is live.</b> The tabs and sidebar work like the app: click one to jump to that screen.</span><button type="button" id="tourShow" aria-pressed="false">Show clickable areas</button></div>
   <div class="tour-nav"><button type="button" id="tourPrev" aria-label="Back">←</button><button type="button" class="next" id="tourNext"></button></div>
  </aside>
  <p class="tour-cap" id="tourCap"></p>
 </div>
</div>"""

INTRO = """  <p class="serif">Every module shares the same projects, people and records, so nothing is typed twice. Open any module for a guided tour of the real, running app on Operation Fraser Crossing, a demo project. Each screen comes with a short explanation, and numbered callouts walk you round it one part at a time.</p>
  <div class="tourhow"><span><i>1</i>Numbered callouts explain each part of a screen</span><span><i class="o">↗</i>Tabs and sidebar in the picture are clickable</span><span><i>→</i>Arrow keys step through the tour</span></div>"""

JS = r"""  /* The product tour: real screens of the running app, a guide beside each, and live tabs in the picture. */
  var SC=OVERVIEW.screens&&OVERVIEW.screens.list?OVERVIEW.screens:null,BYF={},BYMOD={};
  if(SC){
    SC.list.forEach(function(s){BYF[s.f]=s});
    Object.keys(TOUR.order).forEach(function(m){
      BYMOD[m]=TOUR.order[m].map(function(f){var s=BYF[f];s.info=TOUR.screens[f];return s}).filter(function(s){return s&&s.info});
      if(!BYMOD[m].length)delete BYMOD[m];
    });
  }
  function shotsFor(name){
    if(BYMOD[name])return BYMOD[name];
    var k=Object.keys(BYMOD).filter(function(x){return x.toLowerCase().indexOf(name.toLowerCase())===0})[0];
    return k?BYMOD[k]:null;
  }
  function stops(list){return list.reduce(function(n,s){return n+s.info.notes.length},0)}
  function resolve(s){
    if(!s)return null;var f=s.f;
    if(Object.prototype.hasOwnProperty.call(TOUR.alias,f))f=TOUR.alias[f];
    return f&&BYF[f]&&BYF[f].info?BYF[f]:null;
  }
  function first(cands){for(var i=0;i<cands.length;i++){var r=resolve(cands[i]);if(r)return r}return null}
  var tour=document.getElementById("tour"),tImg=document.getElementById("tourImg"),tHot=document.getElementById("tourHot"),
      tMarks=document.getElementById("tourMarks"),tSpot=document.getElementById("tourSpot"),
      tTabs=document.getElementById("tourTabs"),tWhere=document.getElementById("tourWhere"),tCap=document.getElementById("tourCap"),
      tScreen=document.getElementById("tourScreen"),tKick=document.getElementById("tourKick"),tTitle=document.getElementById("tourTitle"),
      tSum=document.getElementById("tourSum"),tNotes=document.getElementById("tourNotes"),tShow=document.getElementById("tourShow"),
      tPrev=document.getElementById("tourPrev"),tNext=document.getElementById("tourNext"),tNow=document.getElementById("tourNow"),tIn=tour.querySelector(".tour-in"),
      cur=null,curList=[],note=-1,opener=null,hinted=false;
  function target(h,s){
    var kind=h[0],lab=h[1],mine=SC.list.filter(function(x){return x.m===s.m});
    if(kind==="s"){
      if(BYMOD[lab])return BYMOD[lab][0];
      return first(mine.filter(function(x){return x.s===lab}));
    }
    return first(mine.filter(function(x){return x.t===lab&&x.s===s.s}))||first(mine.filter(function(x){return x.t===lab}))||first(mine.filter(function(x){return x.s===lab}));
  }
  function pct(v,of){return (v/of*100)+"%"}
  function place(e,n){e.style.left=pct(n[0],SC.w);e.style.top=pct(n[1],SC.h);e.style.width=pct(n[2],SC.w);e.style.height=pct(n[3],SC.h)}
  function go(s,n){
    cur=s;curList=BYMOD[s.m]||[s];note=n==null?-1:n;
    var info=s.info,i=curList.indexOf(s);
    tImg.src="screens/"+s.f;tImg.alt=s.m+", "+info.title+": a screen of the VantageOS app";
    tWhere.innerHTML="";tWhere.appendChild(el("b",null,"VantageOS"));tWhere.appendChild(document.createTextNode(" › "+s.m+" › "+info.title));
    tKick.textContent=s.m+" · screen "+(i+1)+" of "+curList.length;
    tTitle.textContent=info.title;tSum.textContent=info.sum;
    tHot.innerHTML="";
    (s.h||[]).forEach(function(h){
      var to=target(h,s);if(!to||to===s)return;
      var b=el("button");b.type="button";b.title="Go to "+h[1];b.setAttribute("aria-label","Go to "+h[1]);
      place(b,h.slice(2));b.onclick=function(){go(to)};tHot.appendChild(b);
    });
    if(!hinted){tHot.classList.add("hint");hinted=true;}else tHot.classList.remove("hint");
    [].slice.call(tMarks.querySelectorAll(".tour-pin")).forEach(function(p){p.remove()});
    tNotes.innerHTML="";
    info.notes.forEach(function(nt,k){
      var p=el("button","tour-pin",String(k+1));p.type="button";p.setAttribute("aria-label","Callout "+(k+1)+": "+nt[4]);
      p.style.left=pct(nt[0],SC.w);p.style.top=pct(nt[1],SC.h);p.onclick=function(){setNote(k)};tMarks.appendChild(p);
      var li=el("li"),b=el("button");b.type="button";
      b.appendChild(el("i",null,String(k+1)));b.appendChild(el("b",null,nt[4]));b.appendChild(el("span",null,nt[5]));
      b.onclick=function(){setNote(note===k?-1:k)};li.appendChild(b);tNotes.appendChild(li);
    });
    tTabs.innerHTML="";
    curList.forEach(function(x,k){var b=el("button");b.type="button";b.appendChild(el("b",null,String(k+1)));b.appendChild(document.createTextNode(x.info.title));
      b.setAttribute("aria-current",x===s);b.onclick=function(){go(x)};tTabs.appendChild(b);if(x===s)setTimeout(function(){b.scrollIntoView({block:"nearest",inline:"nearest"})},0)});
    tScreen.scrollTop=0;tScreen.scrollLeft=0;
    [curList[i+1],curList[i-1]].forEach(function(x){if(x){var im=new Image();im.src="screens/"+x.f}});
    setNote(note);
  }
  function setNote(k){
    note=k;var notes=cur.info.notes;
    [].slice.call(tNotes.querySelectorAll("button")).forEach(function(b,j){b.setAttribute("aria-current",j===k)});
    [].slice.call(tMarks.querySelectorAll(".tour-pin")).forEach(function(b,j){b.setAttribute("aria-current",j===k)});
    tNow.innerHTML="";
    if(k<0){tNow.appendChild(el("i",null,"i"));tNow.appendChild(el("b",null,cur.info.title));tNow.appendChild(el("span",null,cur.info.sum));}
    else{tNow.appendChild(el("i",null,String(k+1)));tNow.appendChild(el("b",null,notes[k][4]));tNow.appendChild(el("span",null,notes[k][5]));}
    if(getComputedStyle(tNow).display!=="none")tIn.scrollTop=0;
    if(k<0){tSpot.hidden=true;}
    else{
      var n=notes[k];tSpot.hidden=false;place(tSpot,n);
      var H=tScreen.clientHeight,W=tScreen.clientWidth,sc=tImg.clientWidth/SC.w,top=n[1]*sc,left=n[0]*sc;
      if(top<tScreen.scrollTop||top+Math.min(n[3]*sc,H)>tScreen.scrollTop+H)tScreen.scrollTo({top:Math.max(0,top-40),behavior:"smooth"});
      if(left<tScreen.scrollLeft||left+Math.min(n[2]*sc,W)>tScreen.scrollLeft+W)tScreen.scrollTo({left:Math.max(0,left-20),behavior:"smooth"});
    }
    var i=curList.indexOf(cur),nx=curList[i+1];
    tPrev.disabled=(k<0&&i===0);
    tNext.textContent=k<notes.length-1?(k<0?"Start: ":"Next: ")+notes[k+1][4]+" →":nx?"Next screen: "+nx.info.title+" →":"Finish the tour ✓";
  }
  function step(d){
    var i=curList.indexOf(cur),n=cur.info.notes.length;
    if(d>0){if(note<n-1)setNote(note+1);else if(curList[i+1])go(curList[i+1]);else closeTour();}
    else{if(note>-1)setNote(note-1);else if(curList[i-1]){var p=curList[i-1];go(p,p.info.notes.length-1);}}
  }
  function openTour(name,btn){
    var list=shotsFor(name);if(!list)return;
    opener=btn;tour.hidden=false;document.documentElement.style.overflow="hidden";
    tCap.innerHTML="";tCap.appendChild(document.createTextNode("The real app, signed in as the "));tCap.appendChild(el("b",null,(SC.person&&SC.person.title)||"project executive"));
    tCap.appendChild(document.createTextNode(" on Operation Fraser Crossing, a demo project with its data entered by hand, so some screens are still sparse. Esc closes."));
    go(list[0]);tNext.focus();
  }
  function closeTour(){tour.hidden=true;document.documentElement.style.overflow="";if(opener)opener.focus();}
  document.getElementById("tourClose").onclick=closeTour;
  tPrev.onclick=function(){step(-1)};
  tNext.onclick=function(){step(1)};
  tShow.onclick=function(){var on=tShow.getAttribute("aria-pressed")!=="true";tShow.setAttribute("aria-pressed",on);tHot.classList.toggle("show",on);tShow.textContent=on?"Hide clickable areas":"Show clickable areas"};
  tour.addEventListener("click",function(e){if(e.target===tour)closeTour()});
  document.addEventListener("keydown",function(e){
    if(tour.hidden)return;
    if(e.key==="Escape")closeTour();else if(e.key==="ArrowRight")step(1);else if(e.key==="ArrowLeft")step(-1);
  });"""

CARD = """      if(list){var k=stops(list);ms.appendChild(el("span","shots","Guided tour \\u00b7 "+list.length+" screen"+(list.length===1?"":"s")+", "+k+" callouts \\u2192"));b.onclick=function(){openTour(m[0],b)};}"""

tour_data = {
    "screens": {f: {"title": v["title"], "sum": v["sum"], "notes": v["notes"]} for f, v in T.items()},
    "order": ORDER,
    "alias": ALIAS,
}
TOURJS = "  var TOUR=" + json.dumps(tour_data, ensure_ascii=False, separators=(",", ":")) + ";"

out = src[:450] + [CSS + soon.CSS] + src[481:570] + [MODAL] + src[580:666] + [INTRO] + src[667:1050] + [TOURJS, JS + soon.js()] + src[1109:]
html = "\n".join(out)
old_card = L(1119)
assert html.count(old_card) == 1
html = html.replace(old_card, CARD)
mg='  <div class="col" id="modGroups" style="gap:28px"></div>'
assert html.count(mg)==1
html=html.replace(mg,mg+"\n"+soon.HTML)
oc='else{b.disabled=true;ms.appendChild(el("span","soon",m[2]?m[2]+" \\u00b7 not in this tour yet":"Not in this tour yet"));}'
assert html.count(oc)==1, "card"
html=html.replace(oc,'else{b.disabled=true;ms.appendChild(el("span","soon","Built \\u00b7 tour coming soon"));}')
n=html.count('"screens/"+'); assert n==2
html=html.replace('tImg.src="screens/"+s.f;','tImg.src=shot(s.f);').replace('im.src="screens/"+x.f}','im.src=shot(x.f)}')
html=html.replace('  function pct(v,of)','  function shot(f){return (window.SHOTS&&window.SHOTS[f])||"screens/"+f}\n  function pct(v,of)',1)
assert '"screens/"+x' not in html

wh='<h3 style="font:800 2rem var(--d);color:#FFE2C8">The nerd wall</h3>'
assert html.count(wh)==1
html=html.replace(wh,wh.replace('<h3 ','<h3 id="nerdWallH" '))
fb='cards.innerHTML="";cards.appendChild(el("p","serif","The wall shows when this page is opened on claude.ai."));return;'
assert html.count(fb)==1
html=html.replace(fb,'document.getElementById("nerdWallH").hidden=true;cards.hidden=true;msg.hidden=true;'
 +'document.getElementById("coreMsg").textContent="Almost nobody reads this far. The people who do are exactly the ones the team wants to talk to.";'
 +'if(window.VOS_CONTACT){var ta=el("a","btn","Talk to the team \\u2192");ta.href=window.VOS_CONTACT;ta.style.textDecoration="none";cbtn.parentNode.appendChild(ta);}return;')
assert "claude.ai" not in html.replace("window.claude","")
open("index.html", "w").write(html)
print("ok", len(html))
