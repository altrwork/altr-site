# altr site

Static website for altr.

## Structure

The nav is four items. Everything else is a detail page reached from within
the content, so it keeps its URL and search rankings without crowding the header.

| Nav item | Page |
|---|---|
| What we do | `what-we-do.html` - every engagement with its price on the same line |
| Work | `impact-studies.html` -> four `impact-*.html` case studies |
| Writing | `tutorials.html` -> the article pages; `resources.html` canonicals here |
| About | `about.html`, including the 4D framework; `how-we-altr-work.html` has the full version |

Detail pages not in the nav: the service pages (`custom-agents.html`,
`forward-deployed-engineering.html`, `workflow-audit.html`,
`ai-enablement-workshop.html`, `events.html`), the local landing page
(`ai-consulting-tampa.html`), and `frameworks.html`. `pricing.html` redirects to
`what-we-do.html`.

## Files

- `index.html` - home page.
- `styles.css` - the whole design system. Colors are CSS custom properties in
  `:root`; the theme is warm paper (`#F7F3EC` ground, `#1A1714` ink, 16:1).
- `intake-modal.js` - booking intake modal behavior.
- `nav-dropdown.js` - mobile nav toggle.
- `service-detail-modal.js` - service card modal (no longer used on the home page).
- `altr-brand-assets/` - source brand assets and brand notes.
- `assets/` - site assets. Images are served as WebP with PNG/JPEG fallbacks.
- `wireframes.html` - original design exploration reference (noindex, not deployed content).
- `sitemap.xml`, `robots.txt`, `llms.txt`, `404.html` - crawl and discovery files.

`tools/` holds local build scripts and is gitignored, because this repo is the
deployment and those scripts should not be served from the site root:

- `tools/vcard-qr.py` - generates the vCard contact QR codes in `assets/qr/`.
- `tools/social-preview.py` - regenerates `assets/altr_social_preview.png`.
  Re-run it whenever the home page headline or the headline prices change,
  or the card goes stale against the site.

## Design system notes

- Body copy is a system sans stack (`--text`), Space Grotesk (`--sans`) carries
  headings, and Lora (`--serif`) is a pull-quote face only.
- Token names were kept from the previous dark theme so every rule kept
  resolving through the inversion; only the values changed.
- Prices live in exactly two places: `what-we-do.html` and the `.price-strip`
  on the home page. Change both together, plus the `OfferCatalog` schema and
  `llms.txt`.

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
