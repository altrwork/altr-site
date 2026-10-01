# altr site

Static website for altr, live at **https://altrwork.com**. This repository is
public and ranks for the brand name, so the first link here is the site.

## Structure

The nav is four items plus the booking CTA, written as static HTML into every
page so crawlers and users get the same links. Everything else is a detail page
reached from within the content, so it keeps its URL and search rankings without
crowding the header.

| Nav item | Page |
|---|---|
| Services | the three services (`how-we-altr-work.html` Strategy, `ai-enablement-workshop.html` Enablement, `custom-agents.html` Engineering) and the four industries |
| Work | `case-studies.html` -> the `impact-*.html` case studies; `mortr.html` internal products |
| Resources | `ai-workshop.html` events, `tutorials.html` blog |
| About | `about.html` |

The three services are one vocabulary: Strategy takes a team from zero to one,
Enablement trains the people doing the work, Engineering takes it from one to
ten. Do not introduce a fourth name for any of them.

Detail pages not in the nav: `workflow-audit.html` and the local landing pages
(`ai-consulting-tampa.html`, `workflow-automation-consultant-tampa.html`).
Retired URLs redirect in `_redirects`; `design-language/` is internal notes and
is 404'd there so it is not served.

## Files

- `index.html` - home page.
- `styles.css` - the base stylesheet. Colors are CSS custom properties in
  `:root`. The site is dark: `#14110E` ground, `#F2EDE4` type, 16.1:1. The
  token names (`--paper`, `--bone`, `--night`) were never renamed from the
  original dark theme, so the whole palette is a value swap at the bottom of
  `redesign.css` rather than a second stylesheet. `--veil-rgb` and `--ink-rgb`
  carry the two colours that gradients and hairlines are built from, so a
  theme change does not mean editing 53 gradient stops.
- `redesign.css` - the design layer, loaded after `styles.css` and holding the
  house rules: one hairline, one radius, one shadow (the keycap press), one
  accent. The rules are stated once with their exceptions listed rather than
  enumerated per component, and they need `!important` because a universal
  selector has specificity zero and loses to any class.
- `intake-modal.js` - booking intake modal behavior. Every page that links to
  `start-a-conversation.html` must load it, or the same button behaves
  differently depending on the page.
- `nav.js` - nav toggling only; the nav markup itself is static on every page.
- `filter-grid.js` - card filtering, search and list/grid toggle, shared by the
  work index and the blog index.
- `hero-keys.js`, `lead-magnet-form.js` - page behavior.
- `altr-brand-assets/` - source brand assets and brand notes.
- `assets/` - site assets. Images are served as WebP with PNG/JPEG fallbacks.
- `assets/headers/` - each article's hand-drawn header, also used as its learning
  center card and link preview. The source drawings are in
  `design-language/headers/svgs/`. Make or change one with the `sketch-header`
  Claude Code skill in `.claude/skills/sketch-header/`.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `404.html` - crawl and discovery files.
- `.github/workflows/indexnow.yml` and `.github/indexnow.py` - after every push
  to main that touches a page, tell IndexNow (Bing and the other IndexNow
  engines) which sitemap pages changed. The site is on Netlify with Cloudflare
  DNS only, so Cloudflare Crawler Hints never sees it change. Run
  `python .github/indexnow.py` by hand to resubmit the whole sitemap. Its key is
  the 32-hex `.txt` file at the site root, which must stay deployed.
- `learn.html` - the learning center: every plain-answer page, grouped. A new
  learning page goes in four places in the same commit: `learn.html`,
  `sitemap.xml`, `llms.txt` and an extensionless rule in `_redirects`.
  `tests/seo_integrity_test.py` checks all four.
- `ai-news-for-business-<month>-2026.html` and `ai-news-archive.html` - the
  monthly digest. Only the newest month sits on `learn.html`; the rest live in
  the archive. A new month means: the page, a row at the top of the archive,
  moving the learn.html card to it and updating the "Past months" line, the
  Previous/All/Next pager on it and on the month before, and the sitemap,
  llms.txt and `_redirects` entries. `test_news_months_are_catalogued_and_chained`
  checks all of it.
- `tests/answer_engine_sim.py` - an offline proxy for how an AI answer engine
  picks a passage to cite, scored against `tests/answer_engine_queries.json`.
  Run it after any content change; it cannot measure domain trust, which is
  off-site.

`tools/` holds local build scripts and is gitignored, because this repo is the
deployment and those scripts should not be served from the site root:

- `assets/share/altr-home-transformation.jpg` - the link preview for the homepage and every
  non-article page: the marble key over the workshop engraving, with the tagline "AI
  Transformation for small and mid-size businesses". `assets/share/altr-home.jpg` is the
  previous card, kept so cached shares still resolve. `assets/altr_social_preview.png` is the
  retired card, kept only so old cached shares still resolve.
  Re-run it whenever the home page headline changes, or the card goes stale
  against the site.

## This repo is the website and nothing else

Everything client-facing or internal lives in a sibling folder under
`projects/altr/`, which is a plain local folder and not a repo: agreements and
invoicing in the private `altr-legal` repo, sales decks in `../decks` with client
artifacts in `../clients`, lead research in `../research`, and the brand assets
that documents use in `../brand`.

The `.gitignore` entries for `proposals/`, `research/`, `tools/`, and
`charge_card.py` stay as guards even though those paths no longer exist here.
This repo is public; those things must never land in it again.

## Design system notes

- Clash Display carries body copy and headings through Fontshare (`--text` and
  `--sans`), while Lora (`--serif`) remains a pull-quote face only.
- Token names were kept through both inversions, so every rule keeps
  resolving; only the values change. The accent is lifted to `#C2703A` on
  the dark ground, because `#A65529` only reaches 3.54:1 there and fails
  body text.
- The closing band inverts on purpose: `background: var(--bone)` with
  `color: var(--paper)`. On a dark site that makes it a paper band at the
  foot of the page, which is the same idea the other way up. Do not
  "fix" it to match the ground.
- The scene plates are toned for the ground they sit on. The dark set caps
  its highlights around `#D4C1A8` so the engraved paper reads as warm stone
  rather than a lamp.
- **No fees are published anywhere on the site.** Everything is quoted on a
  call. If pricing returns, update the homepage, `llms.txt`, structured data,
  and the service-page price chips together so the site stays consistent.
- Service-page `.price-inline-amount` chips carry "Quoted" or "Scoped". The
  homepage `OfferCatalog` has no `priceSpecification`, which is valid
  schema.org—do not add an empty one back.
- We do not sell engineer-days, embedded headcount, a fixed 7-day audit, or
  anything priced up front. These were removed from the site and
  `test_retired_claims_are_gone_from_every_page` checks every page and
  `llms.txt` so they cannot come back through one file. `about.html` keeps
  "forward deployed engineer" as a job title in a bio, which describes a
  person rather than a service.
- The three engagements are a sequence, not a menu: enablement first, a build
  only if enablement finds one, the retainer only after either. The `01/02/03`
  labels on the homepage encode that order, tagged zero to one / one / one to
  ten.
- Enablement has two formats and **either can come first**: a working session
  (1-4 people, hands-on, returns a written workflow map) or a team workshop
  (up to 10, broader). Do not write copy that makes the session a prerequisite
  for the workshop - a team that wants the whole office in a room first is a
  real case.
- **Session length is not published either.** No hour counts anywhere. The site
  says length is set with the client on the call; it names scheduling shapes
  ("one afternoon", "two mornings", "weekly blocks") but never a number.
- Fees, session length, and any credit or discount mechanics are call-time
  only. They are sales levers and lose their value in print, so they must not
  appear on the site, in `llms.txt`, or in schema.
- The retainer is advisory hours only. It is **not** a workshop allowance and
  **not** forward deployed or embedded engineering time. Additional sessions,
  additional workshops, and any real engineering are scoped and quoted as their
  own thing. Keep the homepage, service pages, structured data, and `llms.txt`
  in sync.
- Images must not be sized by width alone. An `<img>` width/height attribute is
  a presentational hint, so a rule setting only width leaves the attribute
  height standing and the image renders the wrong shape. `img { height: auto }`
  covers this; the deliberate `object-fit: cover` crops outrank it.
- Touch targets are 44px at 680px and below. Links inside prose are exempt:
  they are read, not aimed at.

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
