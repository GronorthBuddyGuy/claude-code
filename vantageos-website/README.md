# vantageos.ca: the "What is VantageOS?" page

Built 2 October 2026 from `GronorthBuddyGuy/vantageos-v2.4`, branch `claude/tour-refresh-oct2b` (main at b365414b plus the open fixes)
(`scripts/overview/build_overview.py`, then `scripts/overview/build_site.py`).

| File | What it is |
|---|---|
| `index.html` | The whole page, with the 40 tour screenshots built in |
| `og-image.png` | The picture LinkedIn and others show when someone shares vantageos.ca |

## Putting it live (Netlify)

1. Open the vantageos.ca site in Netlify, then **Deploys**.
2. Drag this folder (both files) onto the deploy area.
3. Check the link preview at linkedin.com/post-inspector with `https://vantageos.ca/`.

The page names no other platform: the build refuses one that does.
