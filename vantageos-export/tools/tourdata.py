# Curated guided tour: which screens to keep, what each shows, and numbered callouts.
# Box coordinates are in the 1440x900 screenshot space: [x, y, w, h, title, text].
import json

def B(x0, y0, x1, y1, title, text):
    return [x0, y0, x1 - x0, y1 - y0, title, text]

T = {}

# ── Mission Control ─────────────────────────────────────────────
T["003.jpg"] = dict(title="Interactive Workspace", sum="The project cockpit. The knowledge graph and the evidence locker sit side by side, so you can see what the platform knows about the project and what it can prove.", notes=[
    B(95, 76, 664, 105, "Four views, one project", "Tactical Overview, Interactive Workspace, Mission Evidence and Knowledge Graph all read the same records. Click a tab in the picture to switch."),
    B(682, 345, 1027, 800, "The graph asks what it doesn't know", "Each unanswered question (site address, project type, jurisdiction) is a gap. Type an answer, skip it, or let the platform derive it from records already on file. Integrity climbs as gaps close."),
    B(1073, 215, 1396, 627, "Mission Evidence", "Photos, documents and field evidence for the project, gathered in one place. Generate turns them into an evidence pack for an owner, insurer or regulator."),
])
T["005.jpg"] = dict(title="Knowledge Graph", sum="The same graph at full size. Every node is a real thing on the project (a permit, a phase, a risk) and the lines show what depends on what.", notes=[
    B(145, 324, 982, 778, "Nodes you can read at a glance", "Site Prep, Permit V1 and Foundations are phases and approvals; Zoning Delay (high) and Supply Chain (medium) are risks hanging off the core mission. Colour shows status."),
    B(173, 678, 336, 751, "Live derivations", "The platform keeps re-deriving the graph as records arrive. “All systems nominal” means nothing is contradicting itself right now."),
    B(1000, 342, 1355, 778, "Fill the gaps", "The same gap questions as the workspace. Answering here updates the graph immediately."),
])

# ── Executive Command ───────────────────────────────────────────
T["011.jpg"] = dict(title="Operational Command", sum="The operations view for leadership: every project's delivery status, risk and the decisions made on it, rolled up to the region.", notes=[
    B(9, 191, 300, 482, "Strategy, Ops, Finance", "Executive Command is split three ways. The sidebar shows which one you're in; here it's Ops."),
    B(345, 113, 682, 136, "Pick the lens", "Regional SVP, Preconstruction and Capital Desk each re-cut the same projects for a different job."),
    B(382, 287, 1364, 385, "Portfolio at a glance", "Active projects, how many are at risk, how many on track, and average completion. This demo has one project, so the averages are thin."),
    B(382, 409, 973, 691, "Portfolio delivery matrix", "One row per project: region, phase, % complete, schedule, cost and health. Operation Fraser Crossing is in preconstruction."),
    B(1000, 409, 1382, 855, "Decisions", "Decisions recorded on any project's log land here, so leadership sees what was decided without reading every log."),
])
T["015.jpg"] = dict(title="Economic Intelligence", sum="The finance lens. Official Statistics Canada releases for the project's province, so cost and labour conversations start from real numbers, not guesses.", notes=[
    B(365, 182, 1056, 291, "Indicators, signals, forecasts", "Switch between raw indicators, the signals drawn from them, forecasts and analytics."),
    B(375, 318, 1387, 345, "Official signal feed", "A ticker of headline releases for British Columbia, each tagged positive, neutral or negative for the project."),
    B(375, 382, 680, 682, "Where the numbers come from", "Every figure is backed by an official monthly release: 5 of 5 series covered, with the latest release date shown."),
    B(729, 400, 1347, 836, "The indicators", "Shelter price index, consumer price index, employment and participation rate, each with its change since the last release and the source table."),
])

# ── Project Delivery ────────────────────────────────────────────
T["028.jpg"] = dict(title="Work Orders", sum="Where field work is handed out. A work order says what needs doing, who's doing it, where, and by when. This demo project hasn't issued any yet, so the board is empty.", notes=[
    B(38, 345, 292, 709, "Everything in Project Delivery", "Planning, Work Orders, Changes, Lessons and Platform. Each has a one-line description so new users know where to go."),
    B(356, 191, 1402, 218, "The board's status line", "To do, in progress, blocked and done, plus what's late, due this week, or waiting on approval."),
    B(356, 242, 747, 267, "Find a work order", "Search by what, who or where, and filter by priority. Cards drag between columns to change status."),
    B(658, 300, 1113, 385, "Start here", "An empty board explains itself and offers to create the first work order."),
])
T["027.jpg"] = dict(title="Lessons Learned: Retrospective", sum="The retrospective station. Crews log what happened and why, and the platform turns those lessons into a brief the next project can use.", notes=[
    B(764, 149, 1178, 187, "Three modes", "Retrospective to capture, Intelligence to watch live signals, Patterns to find what keeps happening."),
    B(127, 242, 1367, 313, "The tally", "Lessons captured, critical alerts, active signals, anomalies, patterns and AI confidence."),
    B(131, 364, 578, 855, "Log a lesson", "Title, which unit it belongs to (Ops here), what happened and the root cause. That's all it takes."),
    B(1133, 415, 1327, 469, "Summarise with AI", "Turns the project's lessons into an executive brief. Nothing to summarise yet on this project."),
])
T["040.jpg"] = dict(title="Lessons Learned: Intelligence", sum="The same station in Intelligence mode: a live stream of signals worth learning from, as they happen.", notes=[
    B(516, 233, 655, 265, "Intelligence mode", "Selected here. The lesson intake stays on the left so you can log something the moment you spot it."),
    B(855, 442, 1373, 869, "Live intelligence stream", "Critical signals from across the project, filterable. None in scope on this demo project today."),
])
T["041.jpg"] = dict(title="Lessons Learned: Patterns", sum="Patterns mode looks across all the lessons for things that keep recurring, so the same mistake isn't made twice.", notes=[
    B(655, 233, 767, 267, "Patterns mode", "Selected here."),
    B(855, 436, 1376, 864, "Pattern recognition matrix", "Recurring causes and adverse signals. It needs a few lessons on file before it has anything to match."),
])

# ── Field Operations ────────────────────────────────────────────
T["066.jpg"] = dict(title="ERMD Command", sum="Emergency response for the site. One button alerts everyone on the project at once; the rest of the screen shows who would be on the roll.", notes=[
    B(36, 127, 300, 391, "Field Operations", "Site Ops (live map and telemetry), Drones, Fleet and ERMD. The live map needs a mapping key this demo doesn't have, so the tour starts at ERMD."),
    B(591, 136, 1167, 258, "Declare an emergency", "Alerts everyone on the project at once. It says plainly that it doesn't replace calling 911."),
    B(827, 302, 935, 342, "Run a drill", "Practise the same flow without alarming anyone. The last drill was a barge fire tabletop."),
    B(887, 376, 1313, 536, "Who would be on the roll", "200 people are on the project, and each checks in from their own phone once an emergency is declared."),
])

# ── Digital Foreman ─────────────────────────────────────────────
T["075.jpg"] = dict(title="Digital Foreman", sum="An AI assistant for the people running the work. It answers from building codes, trade rules and the project's own lessons, not the open internet.", notes=[
    B(15, 418, 296, 578, "Where it lives", "Under Specialized Command. Foreman is the context-aware assistant; the Knowledge Base tab holds what it knows."),
    B(456, 436, 1305, 527, "Things to ask", "Code lookups (IBC egress for a 3-storey building), retrospectives (past electrical overruns), trade logic (which trades a healthcare job needs)."),
    B(429, 791, 1320, 845, "Ask in plain words", "Type a question and press Enter. Answers cite the records they came from."),
])

# ── Emergency Command ───────────────────────────────────────────
T["078.jpg"] = dict(title="Emergency Response & Control", sum="The emergency command centre: the same declare-and-muster flow as ERMD, as its own module for the people who run crisis response.", notes=[
    B(15, 338, 296, 491, "ERCC", "Crisis orchestration and links to emergency services."),
    B(593, 96, 1169, 218, "Declare an emergency", "One press alerts every person on the project."),
    B(447, 338, 875, 502, "Last drill or emergency", "What happened last time and how long each step took."),
    B(885, 338, 1309, 502, "The roll", "Who's expected to check in. On-site location isn't tracked yet, and the screen says so."),
])

# ── Safety Command ──────────────────────────────────────────────
T["079.jpg"] = dict(title="Safety Overview", sum="The safety centre's front page: what's on record, what's escalated, and what needs someone's attention now.", notes=[
    B(345, 73, 1045, 95, "Nine safety tabs", "Overview, incidents, hazards, zones, risks, follow-up, meetings, drills and certifications. Click any in the picture."),
    B(355, 127, 982, 336, "Safety on record", "Certifications, WHMIS, PPE assignments and open risks, with an escalated warning when something's past due."),
    B(355, 555, 855, 873, "Escalation queue", "Property damage, near misses and environmental exceedances flagged critical, with where they happened."),
    B(1009, 127, 1391, 509, "Safety intel", "Safety plans, ERPs, WHMIS sheets and incident evidence tied to places on site."),
])
T["082.jpg"] = dict(title="Hazards & Observations", sum="Every hazard and good catch recorded on the project: 175 you can see, 14 still open.", notes=[
    B(109, 127, 1391, 160, "Filter the list", "Open, hazards, good catches or all. Record an observation adds one from here or from the field."),
    B(109, 173, 1391, 278, "One observation", "What was seen, when, where, who saw it and what was done on the spot."),
    B(1255, 178, 1382, 233, "Risk before and after", "Risk medium to medium, the owner, and whether it's still open."),
    B(1295, 233, 1378, 265, "Close it out", "The owner closes it once it's fixed, and the close-out is recorded."),
])
T["084.jpg"] = dict(title="Risk Register", sum="34 risks, 2 of them critical right now. Each risk carries its score, its controls, when it was last reviewed and what's planned in response.", notes=[
    B(109, 178, 1391, 309, "A risk, fully described", "Manual materials handling: who owns it, which phase, and the controls already in place."),
    B(1255, 182, 1382, 236, "The score", "Likelihood × severity. 4×4 = 16 is critical. Next review date sits underneath."),
    B(109, 491, 1391, 627, "Scores that move", "Worker overboard was 16 (critical) and is now 12 (high) because controls went in. The register keeps both."),
    B(1282, 282, 1382, 302, "Plan a response", "No response planned yet, so the register says so and offers to plan one."),
])
T["085.jpg"] = dict(title="Follow-up", sum="Corrective actions on the left, audits and inspections on the right. Nothing is closed until someone verifies the fix actually worked.", notes=[
    B(111, 127, 738, 873, "Corrective actions", "93 actions, none overdue. Each has an owner, a due date and the control type (training, PPE, engineering)."),
    B(620, 182, 729, 211, "Verify it worked", "Done isn't closed. Someone has to confirm the fix worked in the field."),
    B(756, 127, 1391, 873, "Audits & inspections", "Owner audits, WorkSafeBC inspections and marine safety checks, with findings and orders issued."),
    B(1265, 291, 1384, 364, "Scores and follow-up", "Auditor's score, critical findings, and whether the follow-up is still open."),
])
T["086.jpg"] = dict(title="Safety Meetings", sum="Toolbox talks and safety meetings: 65 on record, 43 below the required attendance.", notes=[
    B(109, 133, 964, 869, "Every talk on record", "Topic, date, who ran it, which crews, and the languages it was delivered in."),
    B(845, 178, 964, 224, "Attendance", "29 of 31 attended. Talks below the required attendance are flagged for a refresher."),
    B(978, 133, 1391, 324, "Compliance metrics", "PPE compliance and valid certifications, once those are recorded."),
])

# ── Regulatory Compliance ───────────────────────────────────────
T["089.jpg"] = dict(title="Permit Control", sum="The compliance hub's permit pipeline: every permit, who's reviewing it, and what's been verified. This demo project has no permits synced yet, so the pipeline is empty.", notes=[
    B(347, 69, 747, 96, "Three parts", "Permit control, regulatory audits, and the government review side."),
    B(338, 105, 1411, 169, "Permit pipeline", "Total permits and how many are verified, with reviewer communications kept alongside."),
    B(345, 178, 655, 305, "Active uplinks", "Connections to the agencies' own systems. Pick one to see its permits in the right-hand pane."),
    B(15, 360, 296, 527, "Compliance", "Regulatory tracking and compliance monitoring."),
])

# ── Intelligence Engine ─────────────────────────────────────────
T["099.jpg"] = dict(title="Risk Intelligence", sum="Where the project's risks are heading, worked out from the risk register and what has actually happened on site.", notes=[
    B(15, 424, 296, 687, "Command, Analysis, Governance", "Agent oversight, risk and site intelligence, and Sentinel-X security."),
    B(376, 178, 1382, 251, "Four ways in", "Overview, matrix, scenarios and anomalies."),
    B(393, 305, 1349, 533, "Live context", "What's driving risk: safety & compliance 29%, task pipeline 55%, with the signal count behind each."),
    B(1184, 324, 1284, 355, "CRI index", "One composite risk index for the project, 22 today."),
])
T["100.jpg"] = dict(title="Sentinel-X Governance", sum="Security monitoring for the platform itself: threats seen, what was done about them, and red/blue team views.", notes=[
    B(355, 127, 991, 245, "Five views", "Blue team (defence), red team (attack testing), global intel, vault and analytics."),
    B(358, 291, 1045, 436, "Live threat monitor", "Threat vector, origin, target and the action taken, as it happens."),
    B(1069, 291, 1400, 436, "Autonomous response", "What was mitigated automatically in the last hour. Nothing on this quiet demo."),
])

# ── Project Media ───────────────────────────────────────────────
T["112.jpg"] = dict(title="Documents Hub", sum="Every drawing, document, photo and video on the project, with an intake that classifies files as they arrive. This demo hasn't uploaded files yet.", notes=[
    B(38, 309, 296, 545, "Project Media", "Blueprints (2D markup), BIM (3D models), Site Plan (editable plan) and Documents."),
    B(356, 233, 1384, 309, "What's on file", "Totals by kind: AI-written, technical docs, field photos and video."),
    B(365, 355, 684, 855, "Drop files in", "Choose a classification, then ingest PDFs, images or video. Indexing makes them searchable."),
    B(720, 355, 1384, 418, "Find anything", "Search by name, filter by category or by document, photo or video."),
])

# ── Trades Network ──────────────────────────────────────────────
T["121.jpg"] = dict(title="Network", sum="The industry side of the platform: people, a marketplace, apprenticeships, advice and a shared knowledge base, open across companies.", notes=[
    B(345, 109, 1027, 136, "Seven areas", "Home, people, marketplace, apprenticeships, knowledge, advice and regulatory."),
    B(358, 169, 600, 424, "People on the network", "Tradespeople with their trade and home base. Browse to find someone."),
    B(618, 169, 1113, 442, "The wall", "Share a win, ask a question or say who you're looking for."),
    B(1127, 169, 1400, 487, "Openings and answers", "Apprenticeships sponsors have posted, knowledge base articles, and open questions."),
])
T["124.jpg"] = dict(title="Contract Architect", sum="Commercial Ops: assemble a contract from a standard template, simulate what-ifs, and see the risk before anyone signs.", notes=[
    B(109, 116, 527, 142, "Commercial Ops", "Contracts, org links between companies, sub-tier suppliers and the 1099 desk."),
    B(160, 300, 618, 342, "Build, simulate, weigh risk", "Builder to draft, Simulator for what-ifs, Risk to see exposure."),
    B(160, 400, 845, 745, "Parties by jurisdiction", "Who the client and contractor are, and whose law governs."),
    B(885, 400, 1336, 700, "Start from a standard", "Pick a template such as CCDC 2 stipulated price, and apply it."),
])

# ── People ──────────────────────────────────────────────────────
T["131.jpg"] = dict(title="Team & Chain of Command", sum="Who's on the job, what they do, and who they report to, company by company. Incidents route up this chain.", notes=[
    B(347, 109, 665, 136, "Two views", "Team and chain of command, and crew performance."),
    B(1065, 178, 1402, 206, "Company role", "General contractor here, and whether this company runs the site safety program."),
    B(362, 169, 1402, 745, "Everyone on the project", "Name, role and permission level. “No account yet” means they're on the roster but haven't signed in."),
    B(918, 251, 1073, 727, "Reports to", "Set anyone's supervisor with Change. With nobody on record, incidents go to the project admins."),
])
T["134.jpg"] = dict(title="Schedule", sum="The project schedule as a Gantt chart: what's planned, who's on it, and what's slipping.", notes=[
    B(120, 136, 1156, 182, "Progress and views", "15% of the work done. Switch between the Gantt, resources and changes."),
    B(547, 245, 1365, 545, "The Gantt", "Pile driving and pile caps at Pier 1, with critical-path, float, over-budget and baseline markers."),
    B(556, 364, 1256, 391, "Drag a face onto a task", "Each circle is a crew member. Drop one on a task to put them on it."),
    B(162, 745, 475, 873, "AI suggestions", "Two tasks lack crews. The assistant offers to assign them."),
])
T["135.jpg"] = dict(title="Hiring", sum="Add a person to the company roster. Name, role, reference and start date are all that's needed now; tickets and the rest can follow.", notes=[
    B(109, 120, 509, 142, "Hiring areas", "Add a person, openings, crews and the company kit."),
    B(113, 178, 800, 869, "The form", "Role, union local, competency level, languages, home base and the equipment they're authorised on."),
    B(836, 178, 1382, 287, "Company roster", "Everyone on file and how many have their tickets recorded."),
])
T["136.jpg"] = dict(title="Messages", sum="Conversations with the crew and the people around the job, tied to the work they're about.", notes=[
    B(102, 233, 338, 505, "Channels", "One per piece of work. Here, Pile caps, Pier 1."),
    B(365, 224, 973, 687, "The conversation", "“Pile cap rebar delivery slipped to Thursday. Can the pour move to Friday?”"),
    B(998, 233, 1389, 796, "Inspector desk", "Turn a message into a record (an RFI here) and dispatch it, without leaving the thread."),
])
T["137.jpg"] = dict(title="Registers", sum="The catch-all register for logs that don't have a screen of their own yet: workforce assignments, attendance, training and more.", notes=[
    B(127, 255, 982, 300, "Pick the record type", "Workforce assignment is selected. Each type keeps its own register."),
    B(124, 218, 982, 873, "Fill it in", "Reference, date, title, detail, status and priority. The raw data is kept too."),
    B(1000, 236, 1382, 300, "Recent records", "What's been filed of this type. Nothing yet on this project."),
])
T["138.jpg"] = dict(title="Stakeholders", sum="Every company and body with a stake in the project, how much they matter, and how they'll be kept informed. 18 on the register.", notes=[
    B(111, 173, 1011, 873, "Companies on the project", "Subcontractors, the owner (BC Ministry of Transportation) and the general contractor."),
    B(356, 233, 656, 273, "Influence and interest", "Rate each one. Nobody has been assessed on this project yet."),
    B(656, 215, 1002, 273, "Owns the relationship", "Name the person responsible for each stakeholder."),
    B(1029, 182, 1393, 627, "Where they sit", "The influence/interest grid: manage closely, keep satisfied, keep informed, or monitor."),
])

# ── Supply Chain ────────────────────────────────────────────────
T["174.jpg"] = dict(title="Supply Chain Resilience", sum="Material liquidity, logistics risk and shortage forecasting. On this demo project nothing is disrupted, so the table is quiet.", notes=[
    B(15, 424, 296, 724, "Supply Chain", "Resilience, Inventory (stock and procurement) and Automation (digital workers)."),
    B(393, 315, 1393, 382, "Signals", "Active signals, critical, forecasts, near-term impact and how many are ready to mitigate."),
    B(393, 442, 702, 669, "Autonomous sourcing", "Flags a disruption forecast and offers alternatives. Review forecasts opens them."),
    B(742, 442, 1393, 860, "Disruptions", "Each disruption with confidence, impact window, severity and actions."),
])
T["179.jpg"] = dict(title="Inventory & Logistics", sum="Stock on hand, assets, lane security, forecasts and sourcing, with an audit trail of every delivery and transfer.", notes=[
    B(384, 187, 1202, 324, "Five views", "Stock, assets, lane security, forecast and source."),
    B(384, 369, 1356, 442, "At a glance", "Material index, critical stock, fleet size, logistics health (100%) and 12 live uplinks."),
    B(393, 496, 1038, 860, "Logistics audit", "Delivery records, staging evidence and transfer ledgers. Generate builds a report."),
    B(1073, 496, 1356, 860, "Material ledger", "Every item, where it is, how much, and its status. Filter to depleted stock."),
])
T["184.jpg"] = dict(title="Automation: Capabilities", sum="Digital workers: AI agents that take on routine tasks. This view shows what they're allowed to do and the rules they work under.", notes=[
    B(391, 229, 845, 265, "Five views", "Agents, queue, forensics (why an agent did what it did), capabilities and submit."),
    B(391, 305, 1367, 360, "The fleet", "Active agents, queue depth, decision records, success rate."),
    B(895, 396, 1367, 647, "Guardrails", "High-stakes tasks need explicit human sign-off through Mission Control. Agents can't skip it."),
])
T["185.jpg"] = dict(title="Automation: Submit", sum="Hand a task to a digital worker. Every decision it makes is written to the audit log for regulatory review.", notes=[
    B(520, 496, 1227, 556, "What and how urgent", "Pick the instruction type and priority."),
    B(493, 405, 1253, 860, "Describe the job", "The objective and any constraints, in plain words."),
    B(520, 789, 1253, 833, "Recorded", "Submitting assigns a digital worker and records its decisions for review."),
])

# ── O Canada ────────────────────────────────────────────────────
T["203.jpg"] = dict(title="CanadaBuys Gateway", sum="Federal tenders from CanadaBuys, searchable inside the platform so bid teams don't work from a separate site.", notes=[
    B(355, 82, 945, 209, "Four views", "Opportunities, tracking, intelligence and analytics."),
    B(355, 242, 1409, 309, "The pipeline", "Live tenders, how many you're tracking, award rate, top agency and total contract value."),
    B(355, 336, 669, 609, "Search", "Keywords and jurisdiction (all federal here)."),
    B(687, 336, 1409, 873, "Results", "Each opportunity with status, closing date, value and actions."),
])

# ── Cortex ──────────────────────────────────────────────────────
T["204.jpg"] = dict(title="Cortex Insights", sum="Ask the project a question. Each answer is worked out from the project's own records, and shows which ones.", notes=[
    B(365, 155, 1393, 336, "Safety questions", "Are incidents trending up? Where do hazards cluster? How fast do corrective actions close?"),
    B(365, 355, 1393, 427, "Risk questions", "What could the open risks cost us?"),
    B(347, 69, 602, 100, "Doc Intelligence", "The second tab reads documents for cause and effect."),
])

# Screens dropped because they duplicate a kept one (hotspots to them resolve to the kept screen).
ALIAS = {
    "004.jpg": None, "008.jpg": "011.jpg", "017.jpg": "011.jpg", "021.jpg": "015.jpg",
    "023.jpg": None, "025.jpg": "028.jpg", "026.jpg": None, "029.jpg": None, "031.jpg": "028.jpg", "032.jpg": None,
    "033.jpg": "027.jpg", "034.jpg": None, "036.jpg": "028.jpg", "037.jpg": None, "038.jpg": "027.jpg", "039.jpg": "027.jpg",
    "042.jpg": None, "044.jpg": "028.jpg", "045.jpg": None, "046.jpg": "027.jpg", "047.jpg": "027.jpg", "048.jpg": "040.jpg",
    "049.jpg": "041.jpg", "050.jpg": None, "052.jpg": "028.jpg", "053.jpg": None, "054.jpg": "027.jpg", "055.jpg": "027.jpg",
    "056.jpg": "040.jpg", "057.jpg": "041.jpg",
    "058.jpg": None, "059.jpg": None, "062.jpg": "066.jpg", "063.jpg": None, "067.jpg": None, "070.jpg": "066.jpg", "071.jpg": None, "074.jpg": "066.jpg",
    "076.jpg": "075.jpg", "080.jpg": "079.jpg", "083.jpg": None, "088.jpg": None,
    "090.jpg": "089.jpg", "091.jpg": "089.jpg", "092.jpg": "089.jpg",
    "096.jpg": "099.jpg", "102.jpg": "099.jpg", "097.jpg": "100.jpg", "103.jpg": "100.jpg",
    "104.jpg": None, "105.jpg": None, "106.jpg": None, "108.jpg": "112.jpg", "109.jpg": None, "110.jpg": None, "113.jpg": None, "114.jpg": None,
    "116.jpg": "112.jpg", "117.jpg": None, "118.jpg": None, "120.jpg": "112.jpg",
    "122.jpg": "121.jpg", "123.jpg": "121.jpg", "125.jpg": "121.jpg", "126.jpg": "124.jpg", "127.jpg": "124.jpg", "128.jpg": None, "129.jpg": None, "130.jpg": None,
    "132.jpg": "131.jpg", "133.jpg": "131.jpg", "139.jpg": "134.jpg", "146.jpg": "135.jpg", "153.jpg": "136.jpg", "160.jpg": "137.jpg", "167.jpg": "138.jpg",
    "175.jpg": "174.jpg", "178.jpg": "174.jpg", "186.jpg": "174.jpg", "176.jpg": "179.jpg", "187.jpg": "179.jpg",
    "177.jpg": None, "180.jpg": None, "181.jpg": None, "182.jpg": None, "183.jpg": None, "188.jpg": None, "189.jpg": None, "190.jpg": None, "191.jpg": None,
    "192.jpg": "184.jpg", "193.jpg": "185.jpg",
    "205.jpg": "204.jpg", "206.jpg": "204.jpg", "207.jpg": "204.jpg", "208.jpg": "204.jpg",
}
# People: the Team/Schedule/... tabs repeated under every sub-page map onto the six kept screens.
for base, keep in (("140", "131"), ("147", "131"), ("154", "131"), ("161", "131"), ("168", "131")):
    ALIAS[base + ".jpg"] = keep + ".jpg"
for i, keep in enumerate(["134", "135", "136", "137", "138"]):
    for row in (141, 148, 155, 162, 169):
        ALIAS[f"{row + i}.jpg"] = keep + ".jpg"
# Marketing OS: every capture was a Supply Chain page behind "Access Restricted", so it has no tour.
for n in range(194, 203):
    ALIAS[f"{n}.jpg"] = None

ORDER = {  # tour order within each module
    "Mission Control": ["003.jpg", "005.jpg"],
    "Executive Command": ["011.jpg", "015.jpg"],
    "Project Delivery": ["028.jpg", "027.jpg", "040.jpg", "041.jpg"],
    "Field Operations": ["066.jpg"],
    "Digital Foreman": ["075.jpg"],
    "Emergency Command (ERCC)": ["078.jpg"],
    "Safety Command": ["079.jpg", "082.jpg", "084.jpg", "085.jpg", "086.jpg"],
    "Regulatory Compliance": ["089.jpg"],
    "Intelligence Engine": ["099.jpg", "100.jpg"],
    "Project Media": ["112.jpg"],
    "Trades Network": ["121.jpg", "124.jpg"],
    "People": ["131.jpg", "134.jpg", "135.jpg", "136.jpg", "137.jpg", "138.jpg"],
    "Supply Chain Management": ["174.jpg", "179.jpg", "184.jpg", "185.jpg"],
    "O Canada": ["203.jpg"],
    "Cortex AI Intelligence": ["204.jpg"],
}

if __name__ == "__main__":
    o = json.load(open("overview.json"))
    L = o["screens"]["list"]
    allf = {x["f"] for x in L}
    kept = {f for fs in ORDER.values() for f in fs}
    assert kept <= allf and set(T) == kept, (kept - set(T), set(T) - kept)
    missing = allf - kept - set(ALIAS)
    assert not missing, sorted(missing)
    print("kept", len(kept), "aliased", sum(1 for v in ALIAS.values() if v), "dropped", sum(1 for v in ALIAS.values() if not v))
