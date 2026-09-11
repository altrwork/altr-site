# altr design system

What is actually built, and the rules that keep 50 pages reading as one site.
Evidence in [AUDIT.md](AUDIT.md), reference study in [RESEARCH.md](RESEARCH.md).
Everything lives in one file, `redesign.css`, loaded after `styles.css`.

## The spine

Nav, then hero, then content. Nothing sits between them.

The research proposed a "register line" under the nav carrying a page type and
index (`HOME`, `INDUSTRY 01`, `CASE 05`). It was built across all 50 pages and
then cut: in practice it read as a caption on a page that had not asked for
one, and it was the loudest of several labels competing before the reader
reached the headline. Cut with it: the plate mark in the hero corner, the
scrolling ticker, and the mono line under the closer buttons.

What holds the site together instead is the material - one hairline weight,
one radius, one accent, one label style, two heroes, two list shapes. A site
does not need a badge on every page to feel like one site.

## Two heroes, not ten

**Plate hero.** The engraving is a true alpha cutout: every pixel lighter than
the plate's own paper is transparent, so the drawing carries no ground and
sits directly on the page. No box, no panel, no scrim, nothing to blend -
the way a statue photographed on no background has nothing behind it.

Making one: crop a figure from a line-art plate, force everything above the
paper threshold to full transparency, map what is left onto warm ink, drop
every connected component under ~900px to clear the plate's stray labels and
foxing, then trim to the bounding box. `cut-machine.webp` is the worked
example.

Reserved for **eight pages**: Home, the four industry pages, the case index,
About, and How we work. Nowhere else.

**Ruled hero.** Kicker, headline, lede, buttons, hairline underneath. No image.
Every other page.

## Two list shapes, not eight cards

**Ledger** - for anything that is a list. A 64px mono index column, title,
body, optional right-aligned mono datum. Hairline between rows, none after the
last. Rows are not cards: hover turns the title copper and nothing moves.
Process steps, services, FAQs, index pages, related articles.

**Cell grid** - for anything that is a set. Equal columns, **shared 1px
borders and zero gap**, square, flat. The parent draws top and left, each cell
draws right and bottom. Hover fills the cell with sunk paper. No lift, no
shadow, no radius.

Between them these replace `engagement-item`, `tutorial-card`, `resource-item`,
`work-card`, `workshop-topic-card`, `impact-card`, `real-estate-card` and
`founder-card`.

## Rules that hold everywhere

**One hairline weight.** `rgba(26,23,20,0.13)`, 1px. A heavier
`rgba(26,23,20,0.28)` opens a block; nothing else draws a line.

**One radius, and it belongs to the keycap.** `--radius: 2px`, used on buttons
only. Everything else is square. The only rounded things on the site are the
ones you can press.

**One shadow.** The keycap press: 3px of travel, shadow compressing under it,
120ms. There is no other shadow.

**One accent, four roles.** Copper `#A65529` is the keycap fill, the single
two-tone word in a headline, the active and hover state, and the register
label. Nothing else is colored. The second accent `--bay` is gone, and so are
the lavender, amber and cornflower category tints.

**A closed label system, used sparingly.** Mono, 11px, 0.15em, uppercase, dim
ink: section kickers, category labels, ledger indices, the colophon. Nothing
else on the site is uppercase or monospace. One label per section, and none
that only restates what the heading beside it already says.

**Three spacing steps.** `--air-s` 40-64px, `--air-m` 64-112px, `--air-l`
96-176px. Nothing in between. Rules sit on top of sections, never underneath.

**Motion is one thing.** The key press. Scroll reveals, blur-ins and the
ticker are off; nothing animates for longer than 150ms.

## Imagery

Five duotoned Encyclopedie plates, credited in
[../assets/plates/CREDITS.md](../assets/plates/CREDITS.md). Two soft washes for
hero backgrounds, three high-contrast plates for figures and textures.

Rationed deliberately: full-bleed on the eight plate-hero pages, detail crops
as captioned figures at most once per page elsewhere, and **none at all on
roughly thirty of the fifty pages**. Blog thumbnails are six crops of one
plate, so a category reads as a region of a known engraving rather than as a
color.

The plates are the most expensive thing on the site and the fastest to wear
out. When in doubt, leave them off the page.
