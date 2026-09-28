# Frank Pepper resume (website export)

`index.html` is the whole interactive resume in one file. Upload it to any static host
(GitHub Pages, Netlify Drop, Cloudflare Pages, or your own web space) and it works as-is.

Regenerate it after editing `../frank-pepper-robertson.html`:

    { printf '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'; cat ../frank-pepper-robertson.html; printf '\n</html>\n'; } > index.html
