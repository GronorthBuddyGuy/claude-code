// Renders ../frank-pepper-robertson.html to a print-ready PDF with every
// interactive section expanded. Run: NODE_PATH=$(npm root -g) node build-pdf.cjs
const path = require("path");
const { chromium } = require("playwright");

const SRC = path.join(__dirname, "..", "frank-pepper-robertson.html");
const OUT = path.join(__dirname, "Frank_Pepper_Robertson_Application.pdf");

const PRINT_CSS = `
@page { size: Letter; margin: 0.78in 0.78in 0.9in; }
html, body { background: #070B13 !important; }
body { padding: 0 !important; font-size: 15px; }
.bar, .tools, .filters, .ctools, .editnote, #cempty, .mods, #modpanel, #detail, .course { display: none !important; }
header.hero { padding-top: 0 !important; }
section { padding-top: 30px !important; }
.sec-head { break-after: avoid; }
#course-print, #certs, #credentials { break-before: page; }
.fit details, .fit summary, .detail, .pmod, .work div, .item, .ctable tr { break-inside: avoid; }
.fit .ev { padding-bottom: 10px; }
.gantt { overflow: visible !important; }
.ginner { min-width: 0 !important; }
.gscale, .grow { grid-template-columns: 96px 1fr !important; gap: 8px !important; }
.grow .lane { font-size: .62rem !important; }
.gbar { box-shadow: none !important; }
.detail { margin-top: 14px; }
.pdetails { display: grid; gap: 4px; }
.pmods { display: grid; gap: 14px; }
.pmod { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 16px 20px; display: grid; gap: 12px; }
.pmod h3 { font-size: 1.25rem; font-stretch: 80%; text-transform: uppercase; }
.ctable { overflow: visible !important; border: 0 !important; }
.ctable table { min-width: 0 !important; font-size: .82rem; }
.ctable td { padding: 6px 8px !important; }
.ctable thead { display: table-header-group; }
a { text-decoration: none; }
footer { break-inside: avoid; }
.vstats { break-inside: avoid; }
.hero .eyebrow.pill { white-space: nowrap; }
.cstats { break-inside: avoid; }
`;

(async () => {
  const browser = await chromium.launch({
    executablePath: "/opt/pw-browsers/chromium",
  });
  const page = await browser.newPage({ colorScheme: "dark" });
  await page.goto("file://" + SRC, { waitUntil: "load" });
  // Google Fonts can't be reached from the renderer, so embed local copies
  // (fonts/fonts.css holds the latin faces as data URIs).
  await page.addStyleTag({ path: path.join(__dirname, "fonts", "fonts.css") });
  await page.evaluate(async () => {
    await Promise.all(["700 1em Sora", "400 1em 'IBM Plex Sans'", "600 1em 'IBM Plex Sans'", "400 1em 'JetBrains Mono'"].map((f) => document.fonts.load(f)));
    await document.fonts.ready;
  });

  await page.evaluate(() => {
    
    const $ = (s) => document.querySelector(s);

    // Qualification fit: every row open, all filters cleared.
    document.querySelectorAll(".fit details").forEach((d) => { d.open = true; d.hidden = false; });

    // Timeline: one detail block per bar, in chronological lane order.
    const bars = [...document.querySelectorAll("#gantt [data-id]")];
    const seen = new Set(), blocks = [];
    bars.sort((a, b) => parseFloat(b.style.left) - parseFloat(a.style.left));
    for (const b of bars) {
      if (seen.has(b.dataset.id)) continue;
      seen.add(b.dataset.id);
      b.click();
      blocks.push(`<div class="detail">${$("#detail").innerHTML}</div>`);
    }
    document.querySelectorAll("#gantt [aria-pressed]").forEach((b) => b.setAttribute("aria-pressed", "false"));
    $("#detail").insertAdjacentHTML("afterend", `<div class="pdetails">${blocks.join("")}</div>`);

    // Course framework: all modules as stacked cards.
    const mods = [...document.querySelectorAll("#mods button")].map((b) => {
      b.click();
      return `<div class="pmod">${$("#modpanel").innerHTML}</div>`;
    });
    const course = $("#course");
    course.id = "course-print";
    course.insertAdjacentHTML("beforeend", `<div class="pmods">${mods.join("")}</div>`);

    // Certificates: the full list.
    const all = document.querySelector('#ccats [data-c="All"]');
    if (all) all.click();

    // Drop on-screen instructions that make no sense on paper.
    document.querySelectorAll(".eyebrow").forEach((el) => {
      el.textContent = el.textContent.replace(/\s*·\s*select a (bar|step|stage)/i, "").replace(/^Select a (bar|step|stage)$/i, "");
    });
    document.querySelectorAll("#certs .sec-head p, #timeline .sec-head p, #course-print .sec-head p").forEach((el) => {
      el.innerHTML = el.innerHTML.replace(/\s*Use the filters to see the rest\./, "").replace(/\s*Select a bar[^.]*\./i, "");
    });

    // Unconfirmed placeholders stay out of the PDF.
    document.querySelectorAll(".ph").forEach((el) => {
      const line = el.closest("footer > span, dd, .item, p");
      if (line) line.remove();
    });
  });
  await page.addStyleTag({ content: PRINT_CSS });

  await page.pdf({
    path: OUT,
    format: "Letter",
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate: `<div style="width:100%;font:8px 'JetBrains Mono',monospace;color:#93A1BA;padding:0 0.42in;display:flex;justify-content:space-between">
      <span>Frank Pepper · Project Management SME · Robertson College</span>
      <span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
  // Bookmarks and document metadata are added by finish-pdf.py.
  require("child_process").execFileSync("python3", [path.join(__dirname, "finish-pdf.py"), OUT], { stdio: "inherit" });
  console.log("wrote", OUT);
})();
