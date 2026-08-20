# altr site

Static website for altr.

## Files

- `index.html` - primary landing page.
- `styles.css` - shared site styling.
- `service-detail-modal.js` - service card detail modal behavior.
- `intake-modal.js` - booking intake modal behavior.
- `altr-brand-assets/` - source brand assets and brand notes.
- `assets/` - optimized site assets and social preview images.
- `wireframes.html` - original design exploration reference (noindex, not deployed content).
- `ai-consulting-tampa.html` - local landing page for Tampa Bay search intent.
- `workflow-audit.html`, `ai-enablement-workshop.html` - standalone service pages.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `404.html` - crawl and discovery files.
- `tools/vcard-qr.py` - generates the vCard contact QR codes in `assets/qr/`.

## Contact QR codes

`assets/qr/vcard-alex.png` and `assets/qr/vcard-jarred.png` are vCard QR codes
("virtual business cards"). The contact data is encoded in the QR itself, so scanning
opens the native Add Contact sheet with no hosted redirect and no expiry. Edit the
`CARDS` dict in `tools/vcard-qr.py`, then regenerate both:

```sh
uv run --with "qrcode[pil]" --with opencv-python-headless tools/vcard-qr.py
```

Optional flags: `--card alex` for one card, `--mono` for a black-on-white PNG,
`--svg` for vector, `--animate` for an animated SVG (CSS, web) plus GIF (Slack,
email signatures, slides) where modules ripple in outside-in and the keycap lands
last, settling on the static scannable code.

The script picks a QR mask pattern that verifiably decodes and errors out if none does.

## Local preview

Open `index.html` directly in a browser, or run a simple static server:

```sh
python -m http.server 8000
```

Then visit `http://localhost:8000`.
