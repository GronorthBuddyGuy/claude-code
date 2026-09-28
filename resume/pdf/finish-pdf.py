"""Adds bookmarks and document metadata to the resume PDF built by build-pdf.cjs."""
import re
import sys

import pymupdf

path = sys.argv[1]
doc = pymupdf.open(path)

SECTIONS = [
    ("Summary", "FRANK PEPPER"),
    ("Qualification fit", "QUALIFICATION FIT"),
    ("Delivery timeline", "DELIVERY TIMELINE"),
    ("Course framework draft", "WORKING DRAFT FOR THE COURSE DEVELOPER"),
    ("Working with your team", "WORKING WITH YOUR TEAM"),
    ("Certificates (133)", "CONTINUING EDUCATION"),
    ("Credentials", "EDUCATION, CERTIFICATION, TOOLS"),
]


def find(needle, start=0):
    for i in range(start, len(doc)):
        hits = doc[i].search_for(needle)
        if hits:
            return i, hits[0].y0
    return None


MODULES = ["Foundations of project work", "Initiating & stakeholders", "Scope & the WBS", "Schedule",
           "Cost & earned value", "Risk & uncertainty", "Executing, team & quality", "Change, closing & lessons learned"]

toc = []
last = 0
for title, needle in SECTIONS:
    hit = find(needle, last)
    if not hit:
        print("bookmark not found:", title)
        continue
    last = hit[0]
    toc.append([1, title, hit[0] + 1, hit[1]])
    if title.startswith("Course framework"):
        for i in range(hit[0], len(doc)):
            for n in range(1, 9):
                for r in doc[i].search_for(f"MODULE {n} OF 8"):
                    toc.append([2, f"Module {n}: {MODULES[n - 1]}", i + 1, r.y0])

toc.sort(key=lambda t: (t[2], t[3]))
# Chromium paints its own #121212 page canvas behind the margins; repaint it in the
# page colour (#070B13) so the margins match the design.
GREY = b".0706 .0706 .0706 RG .0706 .0706 .0706 rg"
NAVY = b".0275 .0431 .0745 RG .0275 .0431 .0745 rg"
for page in doc:
    for xref in page.get_contents():
        stream = doc.xref_stream(xref)
        if GREY in stream:
            doc.update_stream(xref, stream.replace(GREY, NAVY, 1))

# Frame each page: a thin rounded border inset from the edge, with a short amber
# accent on the top edge, so the content sits inside a defined page.
INSET = 30  # points (~0.42in)
for page in doc:
    r = page.rect
    frame = pymupdf.Rect(INSET, INSET, r.x1 - INSET, r.y1 - INSET - 12)
    page.draw_rect(frame, color=(0.149, 0.204, 0.31), width=1, radius=0.025)
    page.draw_line(pymupdf.Point(frame.x0 + 22, frame.y0), pymupdf.Point(frame.x0 + 110, frame.y0), color=(1, 0.69, 0.125), width=2)

doc.set_toc([[lvl, title, page, {"kind": pymupdf.LINK_GOTO, "page": page - 1, "to": pymupdf.Point(0, max(y - 12, 0))}] for lvl, title, page, y in toc])
doc.set_metadata({
    "title": "Frank Pepper - Project Management Subject Matter Expert",
    "author": "Frank Pepper",
    "subject": "Application for the Project Management Subject Matter Expert contract, Robertson College",
    "keywords": "project management, PMI, PDU, course development, subject matter expert, AI, Robertson College",
    "creator": "Chromium",
    "producer": "PyMuPDF",
})
doc.set_pagemode("UseOutlines")
doc.save(path + ".tmp", garbage=3, deflate=True)
doc.close()

import os
os.replace(path + ".tmp", path)
print("bookmarks:", len(toc))
