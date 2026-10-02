# Website-ready package: VantageOS branding only, no hosting dependencies.
import os, shutil, zipfile, base64, json, re
from tourdata import ORDER

OUT = "/home/user/claude-code/vantageos-website"
h = open("index.html").read()
h = h.replace("window.claude", "window.__vosRuntime")          # host-only features fall back cleanly
assert "claude" not in h.lower()

body_start = h.index("<body>\n<title>") + len("<body>\n")
body = h[body_start:-len("</body></html>")]
body = re.sub(r"^<title>.*?</title>\n", "", body)
host_css = h[h.index("<style>"):h.index("</style>") + 8]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>What is VantageOS? A first look</title>
<meta name="description" content="One platform for the whole job site. Safety, schedule, people, field operations and supply chain, all working from the same records. Take a guided tour of the real app.">
<meta name="theme-color" content="#0A0E13">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<!-- Link previews (LinkedIn, Slack, X). Replace SITE_URL with the page's full address, e.g. https://www.yourdomain.com/first-look/ -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="VantageOS">
<meta property="og:title" content="What is VantageOS? A first look">
<meta property="og:description" content="One platform for the whole job site. Take a guided tour of the real app, and see the mobile companion that's coming next.">
<meta property="og:url" content="SITE_URL">
<meta property="og:image" content="SITE_URLog-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta property="og:image:alt" content="VantageOS: one platform for the whole job site">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="SITE_URLog-image.png">
<script>
/* Where the "Talk to the team" button at the bottom of the page goes.
   Use a mailto: address or a page on your site, e.g. "mailto:hello@yourdomain.com" or "/contact".
   Leave it empty to hide the button. */
window.VOS_CONTACT = "";
</script>
""" + host_css + "\n</head>\n<body>\n"

os.makedirs(OUT, exist_ok=True)
for sub in ("screens", "media"):
    shutil.rmtree(os.path.join(OUT, sub), ignore_errors=True)
os.makedirs(OUT + "/screens"); os.makedirs(OUT + "/media")
open(OUT + "/index.html", "w").write(HEAD + body.strip() + "\n</body>\n</html>\n")
for f in [f for fs in ORDER.values() for f in fs]:
    shutil.copy("screens/" + f, OUT + "/screens/" + f)
shutil.copy("/home/user/claude-code/vantageos-export/VantageOS-first-look.mp4", OUT + "/media/")
shutil.copy("/home/user/claude-code/vantageos-export/VantageOS-first-look-carousel.pdf", OUT + "/media/")
open(OUT + "/favicon.svg", "w").write(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
 '<stop offset="0" stop-color="#12D6E8"/><stop offset=".55" stop-color="#0891A6"/><stop offset="1" stop-color="#0B2A33"/></linearGradient></defs>'
 '<rect width="64" height="64" rx="15" fill="url(#g)"/><path d="M18 17h8l6 20 6-20h8L36 47h-8z" fill="#fff"/></svg>')

# Standalone single-file copy (screens embedded) for the downloads, same clean page.
shots = {f: "data:image/jpeg;base64," + base64.b64encode(open("screens/" + f, "rb").read()).decode()
         for f in [f for fs in ORDER.values() for f in fs]}
full = open(OUT + "/index.html").read()
i = full.index("<script>\n/* Where")
sa = full[:i] + "<script>window.SHOTS=" + json.dumps(shots) + ";</script>\n" + full[i:]
open("standalone.html", "w").write(sa)
print("ok")
