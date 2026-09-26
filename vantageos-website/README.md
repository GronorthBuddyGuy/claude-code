# VantageOS first look: website package

A self-contained page. It needs no build step, no server code and no outside services beyond Google Fonts.

## Files

| File | What it is |
|---|---|
| `index.html` | The page: guided module tours, the mobile companion preview and what's coming |
| `screens/` | The 34 app screenshots the tours use. Keep them next to `index.html` |
| `favicon.svg`, `apple-touch-icon.png` | VantageOS icon for browser tabs and phone home screens |
| `og-image.png` | The 1200×627 image LinkedIn, Slack and X show when someone shares the link |
| `media/` | The LinkedIn carousel (PDF) and the walkthrough video (MP4), to post or embed |

## Putting it on your site

1. Copy the whole folder to your site, e.g. as `/first-look/`, so the page is at `https://yourdomain.com/first-look/`.
2. In `index.html`, replace every `SITE_URL` (4 places, all in `<head>`) with that full address, ending in `/`.
   LinkedIn needs full addresses to show the preview image.
3. Optional: set `window.VOS_CONTACT` near the top of `index.html` to a `mailto:` address or your contact page.
   A "Talk to the team" button then appears at the bottom of the page. Leave it empty to hide it.
4. Check the preview with LinkedIn's Post Inspector (linkedin.com/post-inspector) before you post the link.

If your site is built with a framework (Next.js, Astro, Webflow, etc.), serve this folder as static files
(e.g. Next.js `public/first-look/`) rather than converting the page into components.
