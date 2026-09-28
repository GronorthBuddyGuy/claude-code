// Renders resume.html to Frank_Pepper_Resume.pdf. Run: NODE_PATH=$(npm root -g) node build.cjs
const path = require("path");
const { chromium } = require("playwright");
(async () => {
  const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
  const p = await b.newPage();
  await p.goto("file://" + path.join(__dirname, "resume.html"), { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, "Frank_Pepper_Resume.pdf"), format: "Letter", preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
