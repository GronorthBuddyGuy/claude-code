# LinkedIn document carousel: 1080x1350 slides, VantageOS branding only.
import base64, html, json
from tourdata import T
from soon import ROLES, ALARM, ALARM_BY_ROLE

W, H = 1080, 1350
FONTS = open("fonts/embed.css").read()
e = html.escape

def img(f):
    return "data:image/jpeg;base64," + base64.b64encode(open("screens/" + f, "rb").read()).decode()

LOGO = '<span class="mark">V</span><span class="word">Vantage<b>OS</b></span>'

# (screen, module kicker, headline, which callouts to keep, optional shorter texts)
SHOTS = [
 ("005.jpg", "Mission Control", "The project knows what it doesn't know.", [0, 2],
  ["Every node is something real on the job: a phase, a permit, a risk. Lines show what depends on what.",
   "Gaps become plain questions. Answer them and the graph fills in."]),
 ("079.jpg", "Safety Command", "Safety, escalated before it's a headline.", [1, 2], None),
 ("084.jpg", "Safety Command · Risk register", "Risk scores that move when controls go in.", [1, 2], None),
 ("085.jpg", "Safety Command · Follow-up", "Done isn't closed until someone checks it worked.", [0, 1], None),
 ("134.jpg", "People · Schedule", "Drag a face onto a task. That's scheduling.", [1, 2, 3], None),
 ("131.jpg", "People · Team", "Incidents route up the real chain of command.", [2, 3], None),
 ("066.jpg", "Field Operations · ERMD", "One button alerts the whole project.", [1, 3], None),
 ("075.jpg", "Digital Foreman", "An assistant that answers from codes, not the internet.", [1, 2], None),
 ("015.jpg", "Executive Command · Finance", "Cost conversations that start from official numbers.", [1, 3], None),
]

CSS = FONTS + r"""
*{box-sizing:border-box;margin:0;padding:0}
@page{size:1080px 1350px;margin:0}
html,body{background:#05070A}
body{font-family:'Public Sans',sans-serif;color:#E9EEF2}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;break-after:page;
  background:radial-gradient(ellipse 90% 60% at 100% 0%,rgba(8,190,210,.20),transparent 60%),radial-gradient(ellipse 70% 50% at 0% 100%,rgba(8,190,210,.10),transparent 60%),#0A0E13;
  padding:72px 72px 0;display:flex;flex-direction:column}
.slide::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:54px 54px;pointer-events:none}
.slide>*{position:relative}
.slide:last-child{break-after:auto}
.brand{display:flex;align-items:center;gap:18px}
.mark{width:64px;height:64px;border-radius:16px;background:linear-gradient(145deg,#12D6E8 0%,#0891A6 55%,#0B2A33 100%);display:grid;place-items:center;font:800 34px 'Public Sans';color:#fff;box-shadow:0 0 30px rgba(18,214,232,.35)}
.word{font:800 40px 'Public Sans';letter-spacing:-.01em;color:#F2F5F7}
.word b{color:#22D3EE;font-weight:800}
.foot{position:absolute;left:72px;right:72px;bottom:44px;display:flex;align-items:center;justify-content:space-between;font:600 20px 'JetBrains Mono';color:#6B7884}
.foot .brand .mark{width:38px;height:38px;border-radius:10px;font-size:20px;box-shadow:none}
.foot .brand .word{font-size:24px}
.foot .brand{gap:12px}
.kick{font:600 22px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase;color:#22D3EE}
h1{font:900 118px/.9 'Big Shoulders Display';text-transform:uppercase;letter-spacing:.005em;color:#fff}
h2{font:900 76px/.95 'Big Shoulders Display';text-transform:uppercase;color:#fff;margin-top:14px}
.lede{font:400 34px/1.4 'Public Sans';color:#B8C4CC;max-width:30ch}
.swipe{display:inline-flex;align-items:center;gap:14px;font:700 30px 'Public Sans';color:#0A0E13;background:#22D3EE;border-radius:999px;padding:18px 30px;align-self:flex-start}
/* screenshot slides */
.shot{position:relative;margin:34px -24px 0;border-radius:18px;overflow:hidden;border:2px solid rgba(34,211,238,.35);box-shadow:0 30px 70px rgba(0,0,0,.6)}
.shot img{display:block;width:100%}
.shot .spot{position:absolute;border-radius:10px;outline:4px solid #22D3EE;box-shadow:0 0 0 4px rgba(34,211,238,.25)}
.shot .dim{position:absolute;inset:0;background:rgba(3,5,8,.45)}
.shot .clear{position:absolute;border-radius:10px;box-shadow:0 0 0 2000px rgba(3,5,8,.5)}
.shot .pin{position:absolute;width:48px;height:48px;margin:-20px 0 0 -20px;border-radius:50%;background:#22D3EE;color:#05070A;font:800 26px 'Public Sans';display:grid;place-items:center;border:3px solid #05070A;box-shadow:0 4px 12px rgba(0,0,0,.6)}
.notes{list-style:none;display:flex;flex-direction:column;gap:22px;margin-top:40px}
.notes li{display:grid;grid-template-columns:52px 1fr;gap:4px 20px;align-items:start}
.notes i{grid-row:span 2;width:48px;height:48px;border-radius:50%;background:#22D3EE;color:#05070A;font:800 26px 'Public Sans';font-style:normal;display:grid;place-items:center}
.notes b{font:700 32px/1.2 'Public Sans';color:#fff}
.notes span{font:400 27px/1.4 'Public Sans';color:#A9B6BF}
.demo{position:absolute;right:16px;bottom:14px;font:600 16px 'JetBrains Mono';letter-spacing:.08em;text-transform:uppercase;background:rgba(5,7,10,.85);color:#9AA7B1;border-radius:8px;padding:6px 10px}
/* modules grid */
.mods{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:44px}
.mods div{background:rgba(255,255,255,.04);border:1.5px solid rgba(255,255,255,.12);border-radius:16px;padding:18px 20px;font:700 27px/1.2 'Public Sans';color:#fff}
.mods div small{display:block;font:400 20px/1.35 'Public Sans';color:#8A98A3;margin-top:6px}
.mods div.soon{border-style:dashed;color:#9AA7B1}
/* phones */
.soontag{align-self:flex-start;font:700 22px 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase;color:#05070A;background:repeating-linear-gradient(45deg,#FFD000 0 14px,#FFE45C 14px 28px);border-radius:8px;padding:8px 16px}
.phones{display:flex;gap:26px;justify-content:center;margin-top:40px}
.pcol{display:flex;flex-direction:column;align-items:center;gap:16px}
.pcol>b{font:700 26px 'Public Sans';color:#fff}
.phone{width:300px;height:614px;border-radius:48px;background:#020304;padding:13px;box-shadow:0 0 0 3px #2A2E34,0 30px 60px rgba(0,0,0,.6);position:relative}
.phone::before{content:"";position:absolute;top:22px;left:50%;transform:translateX(-50%);width:90px;height:26px;border-radius:999px;background:#000;z-index:2}
.pscreen{height:100%;border-radius:36px;overflow:hidden;background:#0B0F14;display:flex;flex-direction:column;font:14px/1.35 'Public Sans'}
.pscreen.alarm{background:#3A0A0C}
.pstat{display:flex;justify-content:space-between;padding:15px 24px 0;font:600 12px 'JetBrains Mono';color:#9AA4AD}
.phead{padding:28px 16px 10px;display:flex;flex-direction:column;gap:2px}
.phead small{font:600 11px 'JetBrains Mono';letter-spacing:.1em;text-transform:uppercase;color:#22D3EE}
.alarm .phead small{color:#FF9A9A}
.phead b{font:800 21px/1.1 'Public Sans';color:#fff}
.alarm .phead b{font-size:18px}
.phead span{font-size:12px;color:#9AA4AD}
.pnow{margin:0 12px 10px;border-radius:16px;padding:11px 12px;background:linear-gradient(135deg,rgba(34,211,238,.22),rgba(34,211,238,.06));border:1px solid rgba(34,211,238,.4);display:flex;flex-direction:column;gap:3px}
.pnow em{font:600 10px 'JetBrains Mono';font-style:normal;letter-spacing:.1em;text-transform:uppercase;color:#67E8F9}
.pnow b{font-size:15px;color:#fff}
.pnow span{font-size:12px;color:#B8C2CA}
.alarm .pnow{background:#E5484D;border-color:#FF8A8D}
.alarm .pnow em,.alarm .pnow span{color:#FFE5E5}
.ptiles{flex:1;overflow:hidden;padding:0 12px 10px;display:grid;grid-template-columns:1fr 1fr;gap:8px;align-content:start}
.ptiles div{background:#141A21;border:1px solid #232B34;border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:3px;min-height:80px}
.ptiles div.w{grid-column:1/-1;min-height:0}
.ptiles i{font-style:normal;font-size:19px;line-height:1}
.ptiles b{font-size:13px;color:#fff}
.ptiles span{font-size:11px;color:#8C97A1;line-height:1.3}
.alarm .ptiles div{background:rgba(0,0,0,.28);border-color:rgba(255,138,141,.35)}
.pnav{display:flex;justify-content:space-around;padding:8px 10px 16px;border-top:1px solid #1C232B;font:600 10px 'JetBrains Mono';color:#6B7680}
.pnav span.on{color:#22D3EE}
.ctx{display:grid;grid-template-columns:1fr 1fr;gap:16px 30px;margin-top:40px}
.ctx div{font:400 25px/1.4 'Public Sans';color:#A9B6BF}
.ctx b{display:block;font:700 28px 'Public Sans';color:#fff;margin-bottom:2px}
.list{list-style:none;display:flex;flex-direction:column;gap:26px;margin-top:56px}
.list li{padding:26px 28px!important;background:rgba(255,255,255,.04);border:1.5px dashed rgba(255,255,255,.2);border-radius:18px;padding:20px 24px}
.list b{display:block;font:800 50px/1.05 'Big Shoulders Display';text-transform:uppercase;color:#fff}
.list span{font:400 28px/1.4 'Public Sans';color:#A9B6BF}
.list em{float:right;font:600 16px 'JetBrains Mono';font-style:normal;letter-spacing:.1em;text-transform:uppercase;color:#FFD000;border:1.5px solid #FFD000;border-radius:999px;padding:4px 10px}
.center{align-items:center;justify-content:center;text-align:center;padding-bottom:120px}
.center .lede{margin:0 auto}
"""

def foot(n, total):
    return f'<div class="foot"><div class="brand">{LOGO}</div><span>{n:02d} / {total:02d}</span></div>'

def phone(v, name, alarm=False, extra=None):
    tiles = list(v["tiles"])
    if extra: tiles = [("\U0001f4cb", extra[0], extra[1], True)] + tiles
    t = "".join(f'<div class="{"w" if len(x) > 3 and x[3] else ""}"><i>{x[0]}</i><b>{e(x[1])}</b><span>{e(x[2])}</span></div>' for x in tiles)
    nav = "".join(f'<span class="{"on" if i == 0 else ""}">{e(x)}</span>' for i, x in enumerate(v["nav"]))
    return (f'<div class="phone"><div class="pscreen{" alarm" if alarm else ""}"><div class="pstat"><span>09:41</span><span>{"&#9888; ALERT" if alarm else "5G &#9646;&#9646;&#9646;"}</span></div>'
            f'<div class="phead"><small>{e(name)}</small><b>{e(v["head"][0])}</b><span>{e(v["head"][1])}</span></div>'
            f'<div class="pnow"><em>{e(v["now"][0])}</em><b>{e(v["now"][1])}</b><span>{e(v["now"][2])}</span></div>'
            f'<div class="ptiles">{t}</div><div class="pnav">{nav}</div></div></div>')

def shot_slide(f, kick, head, keep, texts):
    notes = T[f]["notes"]
    kept = [notes[i] for i in keep]
    marks = ""
    for k, n in enumerate(kept):
        x, y, w, h = n[:4]
        marks += f'<div class="spot" style="left:{x/14.4}%;top:{y/9}%;width:{w/14.4}%;height:{h/9}%"></div>'
        marks += f'<div class="pin" style="left:{x/14.4}%;top:{y/9}%">{k+1}</div>'
    items = "".join(f'<li><i>{k+1}</i><b>{e(n[4])}</b><span>{e(texts[k] if texts else n[5])}</span></li>' for k, n in enumerate(kept))
    return (f'<div class="kick">{e(kick)}</div><h2>{e(head)}</h2>'
            f'<div class="shot"><img src="{img(f)}" alt="">{marks}<span class="demo">Real screen · demo project</span></div>'
            f'<ol class="notes">{items}</ol>')

slides = []
slides.append(("cover", f'''<div class="brand">{LOGO}</div>
<div style="margin-top:auto;display:flex;flex-direction:column;gap:34px;padding-bottom:150px">
 <div class="kick">First look</div>
 <h1>One platform<br>for the whole<br>job site.</h1>
 <p class="lede">Safety, schedule, people, field operations and supply chain, all working from the same records. Here's a look inside.</p>
 <span class="swipe">Swipe to look inside &rarr;</span>
</div>'''))
mods = [("Mission Control","The daily cockpit"),("Executive Command","Strategy, ops, finance"),("Project Delivery","Plan, work orders, lessons"),
        ("People","Team, schedule, hiring"),("Field Operations","Site, drones, fleet, ERMD"),("Safety Command","Incidents to audits"),
        ("Intelligence Engine","Risk and AI oversight"),("Project Media","Drawings, BIM, documents"),("Supply Chain","Stock, logistics, automation"),
        ("Trades Network","People, contracts, apprenticeships"),("Digital Foreman","AI assistant for the field"),("Regulatory Compliance","Permits and reviews"),
        ("Emergency Command","Declare, muster, drill"),("Cortex","Ask the project a question"),("Mobile companion","Coming soon")]
grid = "".join(f'<div class="{"soon" if s == "Coming soon" else ""}">{e(m)}<small>{e(s)}</small></div>' for m, s in mods)
slides.append(("mods", f'''<div class="kick">What it is</div><h2>Nothing typed twice.</h2>
<p class="lede" style="margin-top:24px;max-width:36ch">Every module shares the same projects, people and records. Report an incident once and safety, the schedule and leadership all see it.</p>
<div class="mods">{grid}</div>'''))
for s in SHOTS:
    slides.append(("shot", shot_slide(*s)))
R = {r["id"]: r for r in ROLES}
slides.append(("mobile", f'''<span class="soontag">Coming soon</span><h2>The mobile companion.</h2>
<p class="lede" style="margin-top:20px;max-width:40ch">Not a shrunken desktop. It knows who you are, where you are on site and what's happening, and shows each role only what it needs.</p>
<div class="phones">
 <div class="pcol">{phone(R["crew"], "Crew member")}<b>Crew member</b></div>
 <div class="pcol">{phone(R["foreman"], "Foreman")}<b>Foreman</b></div>
 <div class="pcol">{phone(ALARM, "All roles", True, ALARM_BY_ROLE["foreman"])}<b>Emergency declared</b></div>
</div>'''))
slides.append(("mobile2", f'''<span class="soontag">Coming soon</span><h2>A working part of the platform.</h2>
<p class="lede" style="margin-top:20px;max-width:40ch">Every phone on site sends in check-ins, photos, voice notes and sign-offs as they happen, so the office sees the job as it is.</p>
<div class="ctx">
 <div><b>Place</b>Walk into a site zone and its hazards, permits and your task come to the top.</div>
 <div><b>Moment</b>When an emergency is declared, every phone switches to the muster check-in.</div>
 <div><b>Person</b>Your tickets, language and equipment authorisations shape what you see.</div>
 <div><b>No signal</b>Captures stay on the phone and sync when you're back in range.</div>
</div>
<div class="phones" style="margin-top:36px;zoom:.82">
 <div class="pcol">{phone(R["safety"], "Safety lead")}<b>Safety lead</b></div>
 <div class="pcol">{phone(R["exec"], "Executive")}<b>Executive</b></div>
</div>'''))
slides.append(("next", '''<div class="kick">What's next</div><h2>Still being built.</h2>
<ul class="list">
 <li><em>Coming soon</em><b>Mobile companion</b><span>Role-specific apps for crews, foremen, safety, executives, inspectors and subcontractors.</span></li>
 <li><em>Coming soon</em><b>Site sign-in &amp; location</b><span>Who's actually on site, feeding the live emergency roll.</span></li>
 <li><em>Coming soon</em><b>Subcontractor dashboard</b><span>A sub's own work, safety records and documents in one place.</span></li>
 <li><em>Coming soon</em><b>Live site map</b><span>Units, fleet, plant and risk on one map of the site.</span></li>
</ul>'''))
slides.append(("end", f'''<div style="margin:auto 0;display:flex;flex-direction:column;align-items:center;gap:40px;text-align:center;padding-bottom:110px">
 <div class="brand" style="transform:scale(1.6)">{LOGO}</div>
 <h2 style="margin-top:30px">This is a first look.</h2>
 <p class="lede" style="max-width:32ch">Which module would you open first on your job site? Tell us in the comments.</p>
 <span class="swipe" style="align-self:center">Follow for the next look</span>
</div>'''))

total = len(slides)
body = "".join(f'<section class="slide k-{k}">{c}{foot(i+1, total) if k not in ("cover","end") else ""}</section>' for i, (k, c) in enumerate(slides))
open("carousel.html", "w").write(f'<!doctype html><html><head><meta charset="utf-8"><title>VantageOS first look</title><style>{CSS}</style></head><body>{body}</body></html>')
print("slides", total)
