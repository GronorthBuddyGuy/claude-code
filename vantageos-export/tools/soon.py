# "Coming soon": the mobile companion app (interactive phone mock) and interfaces still being built.
import json

CSS = r"""
/* Coming soon */
.soonsec{display:flex;flex-direction:column;gap:18px;margin-top:18px;padding-top:30px;border-top:3px dashed var(--line)}
.soonhead{display:flex;flex-direction:column;gap:8px}
.soonhead h3{font:900 clamp(1.9rem,3.6vw,2.7rem)/1 var(--d);text-transform:uppercase}
.soontag{align-self:flex-start;font:700 .7rem var(--m);letter-spacing:.12em;text-transform:uppercase;color:var(--sign-ink);background:repeating-linear-gradient(45deg,var(--hv-yellow) 0 10px,#FFE45C 10px 20px);border:2px solid var(--sign-ink);border-radius:6px;padding:4px 10px}
.mobile{display:grid;grid-template-columns:minmax(0,1fr) 300px minmax(0,1fr);gap:22px 30px;align-items:start;background:var(--slab);border:2px solid var(--hv-orange);border-radius:22px;padding:24px}
@media (max-width:1100px){.mobile{grid-template-columns:minmax(0,1fr) 300px}.mobile .mright{grid-column:1/-1}}
@media (max-width:700px){.mobile{grid-template-columns:minmax(0,1fr);padding:18px}.mobile .phonewrap{order:2}.mobile .mright{order:3}}
.mobile h4{font:900 2rem/1 var(--d);text-transform:uppercase}
.mobile .mleft,.mobile .mright{display:flex;flex-direction:column;gap:12px}
.mobile p{color:var(--ink-soft);font-size:.95rem}
.mobile .lab{font:600 .68rem var(--m);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-faint)}
.roles{display:flex;flex-wrap:wrap;gap:6px}
.roles button{background:transparent;border:2px solid var(--line);border-radius:999px;padding:6px 12px;font-weight:700;font-size:.84rem}
.roles button:hover{border-color:var(--ink)}
.roles button[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:var(--band)}
.ctxsw{display:flex;align-items:center;gap:10px;font-weight:700;font-size:.88rem}
.ctxsw button{position:relative;width:52px;height:30px;border-radius:999px;border:2px solid var(--line);background:var(--concrete);padding:0;flex:none}
.ctxsw button::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:var(--ink-faint);transition:left .2s,background .2s}
.ctxsw button[aria-pressed="true"]{background:#E5484D;border-color:#E5484D}
.ctxsw button[aria-pressed="true"]::after{left:25px;background:#fff}
.mright ul{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:7px;color:var(--ink-soft);font-size:.92rem}
.mright ul b{color:var(--ink)}
.feeds{display:flex;flex-wrap:wrap;gap:6px}
.feeds span{font:600 .7rem var(--m);border:1.5px solid var(--hv-orange);color:var(--ink);border-radius:999px;padding:3px 9px}
.phonewrap{display:flex;justify-content:center}
.phone{width:280px;height:572px;border-radius:44px;background:#050608;padding:12px;box-shadow:0 0 0 2px #2A2E34,0 24px 50px rgba(0,0,0,.35);position:relative}
.phone::before{content:"";position:absolute;top:20px;left:50%;transform:translateX(-50%);width:84px;height:24px;border-radius:999px;background:#000;z-index:2}
.pscreen{height:100%;border-radius:33px;overflow:hidden;background:#0B0F14;color:#E9EEF2;display:flex;flex-direction:column;font:13px/1.35 var(--b);transition:background .3s}
.pscreen.alarm{background:#3A0A0C}
.pstat{display:flex;justify-content:space-between;padding:14px 22px 0;font:600 .7rem var(--m);color:#9AA4AD}
.phead{padding:26px 16px 10px;display:flex;flex-direction:column;gap:2px}
.phead small{font:600 .62rem var(--m);letter-spacing:.1em;text-transform:uppercase;color:#22D3EE}
.pscreen.alarm .phead small{color:#FF9A9A}
.phead b{font:800 1.25rem/1.1 var(--b)}
.pscreen.alarm .phead b{font-size:1.05rem}
.phead span{font-size:.72rem;color:#9AA4AD}
.pnow{margin:0 12px 10px;border-radius:16px;padding:11px 12px;background:linear-gradient(135deg,rgba(34,211,238,.22),rgba(34,211,238,.06));border:1px solid rgba(34,211,238,.4);display:flex;flex-direction:column;gap:3px}
.pnow em{font:600 .6rem var(--m);font-style:normal;letter-spacing:.1em;text-transform:uppercase;color:#67E8F9}
.pnow b{font-size:.92rem}
.pnow span{font-size:.72rem;color:#B8C2CA}
.pscreen.alarm .pnow{background:#E5484D;border-color:#FF8A8D}
.pscreen.alarm .pnow em,.pscreen.alarm .pnow span{color:#FFE5E5}
.ptiles{flex:1;overflow:auto;padding:0 12px 10px;display:grid;grid-template-columns:1fr 1fr;gap:8px;align-content:start;scrollbar-width:none}
.ptiles div{background:#141A21;border:1px solid #232B34;border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:3px;min-height:74px}
.ptiles div.w{grid-column:1/-1;min-height:0}
.ptiles i{font-style:normal;font-size:1.05rem;line-height:1}
.ptiles b{font-size:.78rem}
.ptiles span{font-size:.66rem;color:#8C97A1;line-height:1.3}
.pscreen.alarm .ptiles div{background:rgba(0,0,0,.28);border-color:rgba(255,138,141,.35)}
.pnav{display:flex;justify-content:space-around;padding:8px 10px 14px;border-top:1px solid #1C232B;font:600 .58rem var(--m);color:#6B7680}
.pnav span.on{color:#22D3EE}
.pscreen.alarm .pnav{border-color:rgba(255,138,141,.3)}
.soongrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:10px}
.soongrid article{background:var(--panel);border:2px dashed var(--line);border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.soongrid b{font:800 1.3rem/1.05 var(--d)}
.soongrid p{font-size:.88rem;color:var(--ink-soft);line-height:1.45}
.soongrid .st{align-self:flex-start;font:600 .64rem var(--m);letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:2px 9px;border:1.5px solid currentColor}
.soongrid .st.build{color:var(--orange-ink)} .soongrid .st.tsoon{color:var(--steel)}
.soongrid .why{font:400 .72rem var(--m);color:var(--ink-faint);margin-top:auto;padding-top:4px}
"""

HTML = """  <div class="soonsec" aria-labelledby="soonH">
   <div class="soonhead"><span class="soontag">Coming soon</span><h3 id="soonH">What's being built next</h3>
    <p class="serif">Everything above is running today. These are the interfaces still on the way, starting with the one that puts the platform in every worker's pocket.</p></div>
   <div class="mobile">
    <div class="mleft">
     <span class="lab">Planned · not built yet</span>
     <h4>The mobile companion</h4>
     <p>A phone app that isn't a shrunken copy of the desktop. It knows <b>who you are</b>, <b>where you are on site</b> and <b>what's happening right now</b>, and shows only what matters to you in that moment.</p>
     <p>It's also a working part of the platform, not only a window onto it. Every phone on site sends in check-ins, photos, voice notes and sign-offs as they happen. That fills gaps the platform has today: the emergency roll currently has no sign-in or location source, and the app becomes that source.</p>
     <span class="lab">Pick a role</span>
     <div class="roles" id="mRoles" role="group" aria-label="Role"></div>
     <div class="ctxsw"><button type="button" id="mAlarm" aria-pressed="false" aria-label="Emergency declared"></button><span>Emergency declared</span></div>
    </div>
    <div class="phonewrap"><div class="phone" aria-live="polite"><div class="pscreen" id="mScreen"></div></div></div>
    <div class="mright">
     <span class="lab">For this role</span>
     <p id="mRoleSum"></p>
     <ul id="mRoleList"></ul>
     <span class="lab">What it feeds back into the platform</span>
     <div class="feeds" id="mFeeds"></div>
     <span class="lab">Context-aware, everywhere</span>
     <ul>
      <li><b>Place:</b> walk into a site zone and its hazards, permits and the task you're on come to the top.</li>
      <li><b>Moment:</b> when an emergency is declared, everything else steps aside for the muster check-in. Try the switch.</li>
      <li><b>Person:</b> tickets, language and equipment authorisations shape what you're offered and in what language.</li>
      <li><b>No signal:</b> captures are kept on the phone and sync to the project record when you're back in range.</li>
     </ul>
    </div>
   </div>
   <div class="soongrid" id="soonGrid"></div>
  </div>"""

ROLES = [
 dict(id="crew", name="Crew member", who="Tradespeople and labourers",
  sum="The simplest version. Where to be, what's on today, and a way to speak up in seconds.",
  list=["Check in and out of site with one tap. That's what puts you on the emergency roll.",
        "Report a hazard or near miss with a photo and a voice note, in your own language.",
        "Sign in to toolbox talks by tapping the QR code at the talk.",
        "Keep your tickets and certifications in a wallet that warns before they expire."],
  feeds=["Emergency roll","Safety · hazards","Safety meetings","People · tickets"],
  head=("Good morning, Tyler","Ironworker · Operation Fraser Crossing"),
  now=("On now","Rebar, Pile caps Pier 1","Crew: Kenji, Nguyen · Coffer dam East · 07:00–15:30"),
  tiles=[("✅","Check in","You're on site · 06:52"),("⚠️","Report something","Photo + voice, 30 sec"),("\U0001f4cb","Toolbox talk","07:15 · Heat stress"),("\U0001faaa","My tickets","Fall protection due Nov")],
  nav=["Today","Report","Talks","Me"]),
 dict(id="foreman", name="Foreman", who="Foremen and superintendents",
  sum="Running a crew from the deck, not the trailer. The schedule, the crew and the Digital Foreman, in one hand.",
  list=["See who's checked in against who's scheduled, and move people between tasks.",
        "Dictate the daily log. It's written up and filed to Project Delivery.",
        "Hand out and close work orders on the spot, with photos as proof.",
        "Ask the Digital Foreman code and trade questions without leaving the pour."],
  feeds=["Schedule","Work orders","Daily log","Digital Foreman","Messages · RFIs"],
  head=("Crew board","General Superintendent · Greg Munroe"),
  now=("Slipping","Pile caps Pier 1: rebar late","Delivery moved to Thursday. Move the pour to Friday?"),
  tiles=[("\U0001f465","Crew 14 / 16","2 not checked in"),("\U0001f399️","Daily log","Hold to dictate"),("\U0001f527","Work orders","3 due today"),("\U0001f916","Ask Foreman","IBC egress, 3-storey?"),("❓","RFI","1 waiting on engineer",True)],
  nav=["Crew","Log","Orders","Ask"]),
 dict(id="safety", name="Safety lead", who="Safety advisors and coordinators",
  sum="The safety centre in a pocket, built for walking the site rather than sitting at a desk.",
  list=["Escalations arrive as they happen, routed up the chain of command.",
        "Run inspections and audits from a checklist, offline, with photos pinned to the spot.",
        "Verify corrective actions in the field before they're closed.",
        "Watch reporting deadlines per jurisdiction count down, and declare an emergency or run a drill."],
  feeds=["Escalation queue","Audits & inspections","Corrective actions","Regulatory obligations"],
  head=("Safety walk","Senior Safety Advisor · Howard Kramer"),
  now=("Escalated","Near miss, Coffer dam East","Reported 4 min ago by Maya T. · WorkSafeBC clock started"),
  tiles=[("\U0001f4dd","Inspection","Coffer dam · 12 items"),("✔️","Verify fixes","6 awaiting you"),("⏱️","Deadlines","1 due in 22 h"),("\U0001f6a8","Emergency","Declare · or run a drill")],
  nav=["Walk","Queue","Actions","Alert"]),
 dict(id="exec", name="Executive", who="Project executives and owners",
  sum="The project in thirty seconds, and the decisions that are waiting on you.",
  list=["A pulse: progress, risk index, safety and cost, with the change since yesterday.",
        "Approve the high-stakes tasks the AI workers are not allowed to do alone.",
        "Hear about serious incidents and declared emergencies first, with who's accounted for.",
        "Record decisions by voice straight into the project log."],
  feeds=["Mission Control approvals","Decisions log","Executive Command"],
  head=("Project pulse","JV CEO / Project Executive · Rob Callaghan"),
  now=("Needs your sign-off","2 AI tasks waiting","Supplier switch for rebar · change order CO-014"),
  tiles=[("\U0001f4c8","15% done","+0.4% today"),("\U0001f6e1️","Risk index 22","2 critical risks"),("\U0001f4b0","Cost","On budget"),("\U0001f5f3️","Decide","Dictate a decision")],
  nav=["Pulse","Approve","Risks","Log"]),
 dict(id="inspector", name="Inspector", who="Structural inspectors and reviewers",
  sum="Hold points and sign-offs where the work is, with the drawings and history to hand.",
  list=["Inspection requests arrive with the location, the drawings and the last result.",
        "Pass, fail or hold with photos and notes, tied to the exact element.",
        "Permit and review status for the pieces you're signing off."],
  feeds=["Inspections","Project Media","Permit control"],
  head=("Hold points","Structural Inspector · Fatima Al-Rashid"),
  now=("Requested","Pier 1 pile cap rebar","Ready Friday 07:00 · drawing S-201 rev C"),
  tiles=[("\U0001f4d0","Drawings","S-201 rev C"),("\U0001f4f7","Pass / fail","Photo per element"),("\U0001f4dc","Permits","1 pending review"),("\U0001f5c2️","History","Last: pass · Pier 2")],
  nav=["Requests","Inspect","Permits","History"]),
 dict(id="sub", name="Subcontractor", who="Subcontractors and suppliers",
  sum="Your slice of the project, and only yours: the walls between companies still apply.",
  list=["Your company's work orders and schedule, nobody else's.",
        "Check deliveries in at the gate, with photos and a signature.",
        "Upload insurance, safety programs and tickets before they're asked for."],
  feeds=["Work orders","Logistics audit","Compliance documents"],
  head=("Apex Environmental","Subcontractor · 3 crew on site"),
  now=("Delivery","Turbidity curtains at Gate 2","Arriving 10:30 · check in on arrival"),
  tiles=[("\U0001f69a","Check in delivery","Gate 2 · 10:30"),("\U0001f527","Our orders","2 open"),("\U0001f4c1","Documents","WCB clearance expires"),("\U0001f4ac","Messages","GC · 1 unread")],
  nav=["Today","Orders","Docs","Chat"]),
]

ALARM = dict(head=("EMERGENCY DECLARED","Operation Fraser Crossing · 09:41"),
  now=("Muster now","Go to Muster Point B, north gate","Leave tools. Don't use the barge ramp."),
  tiles=[("✅","I'm safe","Tap at the muster point"),("\U0001f198","I need help","Sends your location"),("\U0001f4de","Call 911","This app doesn't replace it"),("\U0001f5fa️","Route","Map to Muster Point B")],
  nav=["Muster","Help","Call","Map"])
ALARM_LIST = ["Checking in at the muster point marks you safe on the live roll.",
  "\u201cI need help\u201d sends your location to the safety lead and your supervisor.",
  "Supervisors see their own crew's roll; the safety lead sees the whole site.",
  "Everything else waits until the all-clear."]
ALARM_BY_ROLE = {
  "foreman": ("Your crew","12 of 14 accounted for · Tap to see who's missing"),
  "safety": ("The roll","184 of 200 accounted for · 16 unconfirmed"),
  "exec": ("Accounted for","184 of 200 · updated live"),
}

SOON = [
 ("Site sign-in and location","build","The emergency roll works today but knows nothing about who is actually on site. The mobile app's check-in becomes that source.","The app says so: “no sign-in or location source is connected”"),
 ("Subcontractor dashboard","build","One screen for a subcontractor's own work, safety records and documents. Today these are spread across Project Delivery and Safety.","The Sub-Tier tab says it isn't built yet"),
 ("Dedicated register screens","build","Workforce assignments, attendance, training and other logs each get a screen of their own instead of sharing the catch-all register.","Registers is labelled “no screen of their own yet”"),
 ("Live site map","build","The map of units, fleet, plant and risk on Site Operations, once a mapping service is connected.","Shows “Restricted” on the demo project"),
 ("Marketing OS","tsoon","Campaigns and business development for executive roles. Built, but not captured for the tour.","Restricted for the role the tour signs in as"),
 ("Platform Admin","tsoon","Accounts, billing, disputes, onboarding, the developer console and system status.","Built · tour coming soon"),
 ("Government Portal","tsoon","Legislative review, permits and the interfaces agencies use.","Built · tour coming soon"),
 ("Risk Intelligence","tsoon","Per-project risk state feeding the Monte Carlo forecasts, and its sovereign controls.","Built · tour coming soon"),
]

JS = r"""
  /* Coming soon: the mobile companion, driven by role and by what's happening. */
  (function(){
    var M=__MOBILE__,roles=document.getElementById("mRoles"),scr=document.getElementById("mScreen"),alarm=document.getElementById("mAlarm"),
        rs=document.getElementById("mRoleSum"),rl=document.getElementById("mRoleList"),fd=document.getElementById("mFeeds"),cur=M.roles[0],on=false;
    function draw(){
      var v=on?M.alarm:cur,now=v.now;
      if(on&&M.alarmBy[cur.id])now=[v.now[0],v.now[1],v.now[2]];
      scr.className="pscreen"+(on?" alarm":"");scr.innerHTML="";
      var st=el("div","pstat");st.appendChild(el("span",null,"09:41"));st.appendChild(el("span",null,on?"⚠ ALERT":"5G ▮▮▮"));scr.appendChild(st);
      var h=el("div","phead");h.appendChild(el("small",null,on?"All roles":cur.name));h.appendChild(el("b",null,v.head[0]));h.appendChild(el("span",null,on?v.head[1]:v.head[1]));scr.appendChild(h);
      var n=el("div","pnow");n.appendChild(el("em",null,now[0]));n.appendChild(el("b",null,now[1]));n.appendChild(el("span",null,now[2]));scr.appendChild(n);
      var t=el("div","ptiles");
      var tiles=v.tiles.slice();if(on&&M.alarmBy[cur.id])tiles.unshift(["\U0001f4cb"].concat(M.alarmBy[cur.id]).concat([true]));
      tiles.forEach(function(x){var d=el("div",x[3]?"w":null);d.appendChild(el("i",null,x[0]));d.appendChild(el("b",null,x[1]));d.appendChild(el("span",null,x[2]));t.appendChild(d)});
      scr.appendChild(t);
      var nv=el("div","pnav");v.nav.forEach(function(x,i){nv.appendChild(el("span",i===0?"on":null,x))});scr.appendChild(nv);
      rs.textContent=on?"When an emergency is declared, every phone on the project drops what it was showing and switches to the muster screen, whatever the role."+(M.alarmBy[cur.id]?" The "+cur.name.toLowerCase()+" also sees who is accounted for.":""):cur.sum;
      rl.innerHTML="";(on?M.alarmList:cur.list).forEach(function(x){rl.appendChild(el("li",null,x))});
      fd.innerHTML="";(on?["Emergency roll","ERMD Command"]:cur.feeds).forEach(function(x){fd.appendChild(el("span",null,x))});
      [].slice.call(roles.children).forEach(function(b){b.setAttribute("aria-pressed",b.dataset.id===cur.id)});
    }
    M.roles.forEach(function(r){var b=el("button",null,r.name);b.type="button";b.dataset.id=r.id;b.title=r.who;b.onclick=function(){cur=r;draw()};roles.appendChild(b)});
    alarm.onclick=function(){on=!on;alarm.setAttribute("aria-pressed",on);draw()};
    draw();
    var g=document.getElementById("soonGrid");
    M.soon.forEach(function(s){var a=el("article");a.appendChild(el("span","st "+s[1],s[1]==="build"?"Being built":"Tour coming soon"));a.appendChild(el("b",null,s[0]));a.appendChild(el("p",null,s[2]));a.appendChild(el("span","why",s[3]));g.appendChild(a)});
  })();"""

def js():
    ab = {k: [v[0], v[1]] for k, v in ALARM_BY_ROLE.items()}
    data = dict(roles=[dict(r, tiles=[list(t) for t in r["tiles"]]) for r in ROLES],
                alarm=dict(ALARM, tiles=[list(t) for t in ALARM["tiles"]]), alarmBy=ab, alarmList=ALARM_LIST, soon=[list(s) for s in SOON])
    return JS.replace("__MOBILE__", json.dumps(data, ensure_ascii=False, separators=(",", ":"))).replace("\\U0001f4cb", "\U0001f4cb")
