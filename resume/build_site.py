"""Builds the FrankPepper.com static site from the resume page and the tab partials.

Outputs:
  site/index.html            personal site with Work / Research / Music tabs
  site/robertson/index.html  the full Robertson College application page
  site/CNAME                 custom domain for GitHub Pages

Run from this directory:  python3 build_site.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = (HERE / "frank-pepper-robertson.html").read_text()
RESEARCH = (HERE / "parts" / "research.html").read_text()
MUSIC = (HERE / "parts" / "music.html").read_text()
OUT = HERE / "site"

DESC = ("Frank Pepper, founder of VantageOS: building the future of project management in Canada. "
        "Career, research and music.")


def doc(body, title_desc):
    head = ('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<meta name="description" content="{title_desc}">\n<meta name="theme-color" content="#070B13">\n')
    return head + body + "\n</html>\n"


def between(s, start, end, inclusive=True):
    i = s.index(start)
    j = s.index(end, i) + (len(end) if inclusive else 0)
    return s[i:j]


def sub1(s, old, new):
    if old not in s:
        raise SystemExit(f"build_site: expected text not found: {old[:70]!r}")
    return s.replace(old, new, 1)


# ---------------------------------------------------------------- Robertson page
rob = SRC
rob = sub1(rob, '    <nav aria-label="Sections">',
           '    <nav aria-label="Sections">\n      <a href="../">← FrankPepper.com</a>')
(OUT / "robertson").mkdir(parents=True, exist_ok=True)
(OUT / "robertson" / "index.html").write_text(doc(rob, "Frank Pepper: application for the Project Management "
                                                        "Subject Matter Expert contract at Robertson College."))

# ---------------------------------------------------------------- Personal site
style = between(SRC, "<title>", "</style>", inclusive=False)
style = style.replace("<title>Frank Pepper Resume</title>", "<title>Frank Pepper</title>")
style += (HERE / "parts" / "site.css").read_text() + "</style>\n"

logo = re.search(r'<a class="vmark"[^>]*>.*?</a>', SRC, re.S).group(0)
bar = f'''
<div class="bar">
  <div class="wrap">
    {logo.replace('class="vmark"', 'class="vmark" title="VantageOS.ca"')}
    <nav class="tabs" role="tablist" aria-label="Site sections">
      <a role="tab" href="#work" id="t-work" aria-controls="work">Work</a>
      <a role="tab" href="#research" id="t-research" aria-controls="research">Research</a>
      <a role="tab" href="#music" id="t-music" aria-controls="music">Music</a>
      <a class="ext" href="robertson/index.html">Robertson application ↗</a>
    </nav>
  </div>
</div>
'''

hero = between(SRC, '  <header class="hero">', "  </header>")
hero = sub1(hero, '<p class="eyebrow pill">Resume · Project Management SME · Robertson College</p>',
            '<p class="eyebrow pill">Founder, VantageOS · Lloydminster, SK</p>')
hero = sub1(hero, "      <div>Remote · up to 20 h/wk</div>\n", "")

summary = between(SRC, '  <div class="summary">', "    </dl>\n  </div>")
summary = re.sub(r" For Robertson's Project Management course I bring[^<]*", "", summary)
summary = summary.replace('      <div><dt>Availability</dt><dd data-k="avail">Immediate</dd></div>\n', "")
summary = summary.replace("</p>\n    <dl", " I bring the theory, the jobsite examples, and the recorded audio and video to everything I teach and build.</p>\n    <dl", 1)

vband = between(SRC, '  <section class="vband"', "  </section>")
timeline = between(SRC, "  <section id=\"timeline\">", "  </section>")
certs = between(SRC, '  <section id="certs">', "  </section>")
creds = between(SRC, '  <section id="credentials">', "  </section>")
footer = between(SRC, "  <footer>", "  </footer>")

script = between(SRC, "<script>", "</script>")
# The Work tab has no qualification-fit or course-framework sections.
script = re.sub(r"  /\* ---------- Fit matrix ---------- \*/.*?(?=  /\* ---------- Gantt)", "", script, flags=re.S)
script = re.sub(r"  /\* ---------- Course framework ---------- \*/.*?(?=  /\* ---------- Certificates)", "", script, flags=re.S)
script = script.replace("})();\n</script>", (HERE / "parts" / "site.js").read_text() + "})();\n</script>")

body = f'''{style}{bar}
<main class="wrap">
{hero}
{summary}

<div class="tabpanel" id="work" role="tabpanel" aria-labelledby="t-work">
{vband}
{timeline}
{certs}
{creds}
</div>

<div class="tabpanel" id="research" role="tabpanel" aria-labelledby="t-research">
{RESEARCH}
</div>

<div class="tabpanel" id="music" role="tabpanel" aria-labelledby="t-music">
{MUSIC}
</div>

{footer}
</main>

{script}
'''
(OUT / "index.html").write_text(doc(body, DESC))
(OUT / "CNAME").write_text("frankpepper.com\n")
print("built", OUT / "index.html", "and", OUT / "robertson" / "index.html")
