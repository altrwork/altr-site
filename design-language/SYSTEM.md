# altr design system

What is actually built, and the rules that keep 50 pages reading as one site.
Evidence in [AUDIT.md](AUDIT.md), reference study in [RESEARCH.md](RESEARCH.md).
Everything lives in one file, `redesign.css`, loaded after `styles.css`.

## The spine

Three things appear on every page, in this order, and nothing else is allowed
to sit between the nav and the content.

1. **Nav.** Unchanged.
2. **Register line.** A 32px band under the nav: page type and index on the
   left in copper mono, one datum on the right in dim mono, hairline
   underneath. `HOME`, `INDUSTRY 01`, `SERVICE 08`, `CASE 05`, `GUIDE 12`,
   `INDEX`, `DOC`. This is the signature move. It costs nothing, survives the
   404 and the legal pages, and it carries the numbering that ties services,
   cases and guides to each other.
3. **Hero**, in one of two shapes only.

## Two heroes, not ten

**Plate hero.** Fixed 560px. The engraving runs full-bleed; a solid paper
panel bleeds off the left edge and stops against it with a hard vertical rule.
No gradient scrim - the join is an edge you can see, which is the single
biggest step from "editorial" to "raw". The plate carries a boxed mono mark in
its top-right corner: `PL. 01 / DIDEROT, TAILLEUR D'HABITS`.

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

**A closed label system.** Mono, 11px, 0.15em, uppercase, dim ink. Kickers,
category labels, ledger indices, plate marks, the register line, the colophon.
Nothing else on the site is uppercase or monospace - that is what keeps the
labels reading as a system rather than as decoration.

**Three spacing steps.** `--air-s` 40-64px, `--air-m` 64-112px, `--air-l`
96-176px. Nothing in between. Rules sit on top of sections, never underneath.

**Motion is one thing.** The key press. Scroll reveals, blur-ins and the
marquee are off; nothing animates for longer than 150ms.

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
