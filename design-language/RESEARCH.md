# RESEARCH: raw / industrial cohesion for altrwork.com

Date: 2026-09-10
Method: every site below was fetched live on this date with Firecrawl (viewport
and full-page screenshots, branding extraction, raw HTML, and for Oxide and
Hadrian the compiled CSS). Anything not directly observed is marked
"unverified" or "inferred". No page from altr-site was changed.

The brief in one line: the client wants 50 pages that feel like one object,
and wants that object to feel raw and industrial rather than decorative.
The finding in one line: the sites that pull this off do not have more design;
they have fewer section types, one persistent mono label system, one rule
weight, and one accent used in no more than four roles. Everything else is
restraint.

---

## 1. Reference study

Ten primary references, ordered by relevance to a consultancy site. Four
secondary sites checked and noted briefly at the end of this section.

### 1.1 Oxide Computer Company - https://oxide.computer/

What they do: build and sell a rack-scale "cloud computer" (integrated
hardware plus software) for on-premises deployment. Hardware company with a
software voice. The closest thing in this set to a technical firm selling a
serious, expensive, engineered thing.

Pages examined: home (full page, 9974px tall), /product/compute,
/solutions/finance, /principles, /blog. All live.

Mechanics that make it read industrial, not decorative:
- Figure labels. The hero rack carries a boxed mono label "FIG. 1 | OXIDE
  CLOUD COMPUTER". Console screenshots further down carry "FIG. 2 OXIDE WEB
  CONSOLE" and "FIG. 3". Every image is treated as a plate in a manual.
- The mono label system is one CSS class, measured from their stylesheet:
  `.text-mono-sm` = mono, 12px (0.75rem), uppercase, letter-spacing 0.04rem,
  weight 400, line-height 16px. `.text-mono-xs` is the same at 11px. Nav
  items, eyebrows, dates, spec keys, button labels, and footer column heads
  all use these two classes. Nothing else is uppercase.
- Display type is quiet. `.text-sans-3xl` = 36px/42px, weight 400,
  letter-spacing -0.013em. Section titles are regular weight, not bold. The
  contrast comes from size and from mono-vs-sans, not from weight.
- Eyebrow with trailing rule: "POWERING THE BEST TEAMS" followed by a 1px
  hairline that runs to the right edge of the column.
- Connector lines: a thin angled hairline runs from the terminal panel in the
  hero to the rack, like a callout on an engineering drawing.
- Cell grids, not cards. The 4-up feature row and the 3x2 "workloads" grid are
  1px-bordered cells with a 2px radius, sharing borders, no gap, no shadow, no
  fill change. The cell IS the card.
- Spec table: a two-column key/value list with 1px rules between rows, mono
  keys, sans values. Used on product pages and reads like a datasheet.
- Numbered hardware list "1 5TH GENERATION AMD EPYC SERVER CPU / 2 TWELVE
  CHANNEL ... / 3 ..." with mono index numbers.
- Blog card dates carry a small corner-bracket glyph before the mono date
  ("28 JUL 2026"). A tiny repeated mark that marks metadata as metadata.
- One accent (green #00D892) in four roles only: the one filled CTA, live
  status chips inside product mockups, the wordmark, and single-word
  highlights inside product UI. Never as a background, never on headings.

System-level cohesion (checked across five pages):
- Same nav on every page: wordmark left, six mono uppercase items center,
  two small buttons right, one filled.
- Same column (roughly 1180px) and same left alignment of all section titles.
- The product page, the solutions page, and the principles page are all
  built from the same seven blocks: hero (eyebrow, two-tone h1, one image),
  statement, cell grid (3 or 4), split text (short claim left, body right),
  media pair, spec table, CTA band. I could not find a section type on the
  inner pages that does not exist on the home page.
- Two-tone headings everywhere: white first clause, grey second clause
  ("On-demand virtual machines" / "Provision and manage instances").
- The closing block is identical on every page: giant "The cloud you own"
  statement left, four link columns right.

Signature move: the figure label. FIG. n plus a boxed caption on imagery.

Steal: the figure label, the two-class mono system, the shared-border cell
grid, the key/value spec table, the seven-block page kit, the closing
statement footer, the regular-weight display type.
Does not transfer: dark ground (altr is paper), product-UI mockups as
imagery (altr has no product UI to show), the terminal panel.

### 1.2 Hadrian - https://www.hadrian.co/

What they do: automated precision-manufacturing factories for aerospace and
defense. A real industrial company; the site is small (six internal pages).

Pages examined: home (full page, 3639px). /about attempted, did not render in
scrape; unverified.

Mechanics:
- The nav carries a live clock strip: "CA | 07:44PM PDT | AZ | 07:44PM MST |
  AL | 09:44PM CDT | DC | 10:44PM EDT". Measured from source: mono, 12px,
  1px border on each cell, 26px tall. Real operational data as ornament.
- Buttons are the industrial signature. From their compiled classes:
  `font-mono uppercase`, 14px (16px on md), padding 10-14px by 14-18px, 1px
  border in currentColor, no fill. On hover the border box scales to 0.975
  over 800ms with a cubic-bezier(0.625,0.05,0,1) ease. That is the whole
  hover. Each label ends with an arrow: "WHAT WE BUILD" + down arrow,
  "CAREERS AT HADRIAN" + right arrow.
- The hero illustration is a CAD-style line drawing inside a 1px frame whose
  lower corners are chamfered at 45 degrees. Not a rounded rectangle: a cut
  one. The chamfer is the single most "machined" detail in this set.
- Display h1 at 72px, light weight (Soehne Breit), 2 lines, on a flat navy
  ground with no image behind it.
- Eyebrow "OUR MODEL" in the amber accent, 11-12px mono, above the section
  title. Three columns, each heading underlined by a 1px rule that spans only
  its own column.
- Marquee strip "MANUFACTURE THE FUTURE AT HADRIAN" repeating in amber, set
  inside a bordered box rather than full bleed.
- One accent (amber #F3A000) in four roles: the eyebrow, the marquee, one
  filled button ("VIEW OPEN ROLES"), and highlight lines within the drawing.
- Roughly 600px of empty navy between the hero and the next section. The
  void is a section.
- Footer: wordmark, three mono links, "HADRIAN AUTOMATION" and "UNITED STATES
  OF AMERICA" in mono. Radius 4px declared but nothing visible is rounded.

System-level cohesion: home page is four sections. With six pages total,
cohesion is achieved by having almost nothing to keep consistent. The lesson
for a 50-page site is the inverse: the fewer blocks you allow, the closer you
get to a six-page site's cohesion.

Signature move: mono uppercase bordered buttons with a terminal arrow, and
the border-scale hover.

Steal: the button spec (mono, uppercase, 1px border, arrow suffix), the
chamfered frame as the one allowed corner treatment, the column-width rule
under column headings, real data in the header (altr could show Tampa local
time or the current week number, since the pitch is "workflows a team repeats
every week").
Does not transfer: the marquee (one is fine, but altr's brief says "not
sporadic" and a marquee is the loudest block on any page), the navy ground.

### 1.3 Sanctuary Computer - https://www.sanctuary.computer/

What they do: a New York design and engineering studio building digital
products and technical systems for clients (Google, Stripe, Brooklyn Museum).
The closest business model to altr in this set.

Pages examined: home (full page, 8947px).

Mechanics:
- Numbered list as the primary content structure: "We specialize in three
  things" left; "1 Product & MVPs / 2 Greenfield Innovation / 3 Sophisticated
  Websites" right, each with a one-line mono-ish sublist and a dotted 1px
  rule between rows.
- A 1px vertical rule divides a 40/60 split, and the same split with the same
  rule is reused three times down the page (specialize, deliver, mission).
  That reuse is why the page feels like one object.
- Statement blocks: one long sentence in 40px regular grotesk, max ~60ch,
  followed by a small "Read more ->" link. No heading above it.
- Exactly two ground changes on the page: light grey, then near-black for
  "Selected Work" and "Mission", then back. The dark section is a chapter,
  not a stripe.
- Work grid: 3 columns, image, title, one-line description. No border, no
  shadow, no hover card. Six items, then one "View all work ->" button.
- The one soft voice is a serif used for "Mission" and the closing "We're
  open-sourcing our entire business model." Structurally identical to altr's
  Lora-for-asides rule, and the site limits it to two moments.
- Testimonials are three columns of plain text with the client wordmark
  below, no quote marks, no cards, no photos.
- A small dark "instrument panel" in the hero corner cycles through values
  ("NETWORKS", "ANTI-FRAGILE", "PATIENCE", "TRUST") with a wireframe diagram
  above and four dots. Mono labels. It reads as a gauge.

System-level cohesion: one split layout with a vertical rule, reused; one
grid; one statement block; two ground colors. Perhaps five section types on a
long page.

Signature move: the vertical hairline splitting claim from evidence.

Steal: the numbered "three things" ledger, the vertical-rule split, plain-text
testimonials with a wordmark and no card, capping the serif to two moments per
page.
Does not transfer: the blurred full-bleed video hero (soft, and the opposite
of raw), the gauge widget (fun, but it is a second metaphor and altr already
has the keycap).

### 1.4 basement.studio - https://basement.studio/

What they do: an Argentine digital studio doing websites, branding, and
launch campaigns for tech companies (Vercel, Daylight, MrBeast).

Pages examined: home (full page, 7318px).

Mechanics:
- Exposed grid. "Trusted by Visionaries" is an 8x5 logo grid where every cell
  has a 1px border and the borders are shared. The grid lines are visible and
  are the design.
- Featured projects as full-width ledger rows: image left (about 60%), then a
  right column carrying a short description top-left, the project title
  top-right, and category tags bottom-left. A hairline separates rows. The
  same row repeats five times with zero variation.
- Nav with counts: "Showcase (26)", "Blog (49)", plus an "Online (43)"
  indicator. Numbers as texture.
- Giant condensed grotesk headline directly below the hero visual, flush left,
  two lines, then a 2-line body at roughly 13px. Extreme size contrast, one
  weight.
- Service columns end in small grey tag chips ("Product Strategy", "UX/UI
  Design") with zero radius.
- Footer is a single word: "BSMNT.26" at the full column width.
- Radius 0 everywhere. No shadows.

System-level cohesion: the shared-border grid and the repeated ledger row do
all the work; the rest is type size.

Signature move: the shared-border cell grid.

Steal: shared borders (border-collapse thinking applied to layout), the
project ledger row, counts in nav, the versioned footer wordmark ("altr.26"
would be a light touch that says "this is an edition").
Does not transfer: black ground, the 3D rendered hero, the tone of the copy.

### 1.5 The Public Domain Review - https://publicdomainreview.org/

What they do: an online journal publishing essays and curated collections of
out-of-copyright art, books, and imagery. Directly relevant because it is the
one site here built on the same raw material altr is using: historical
engravings.

Pages examined: home (full page, 4864px), /essays/.

Mechanics:
- Masthead centered, a serif wordmark with italic "The" and "REVIEW", then a
  nav row with a hairline above and below it. This exact block repeats on the
  essays page.
- Centered section titles set between rules: "LATEST ESSAYS" and "ESSAYS"
  sit in the middle of a double hairline that runs the full column. The rule
  is the section marker, not a background change.
- The about blurb in the left column has a 2px blue vertical rule on its
  left edge only. One heavier rule for one purpose.
- The engravings are used two ways, and neither is as a background: (a) as
  the featured image, cropped hard to a rectangle at full column width, with
  no scrim and no text over it; (b) as small cutout figures (a hare, a hand
  holding a page, a row of twelve grotesque figures in the footer) placed as
  spot art beside forms and at section ends. The cutout has no frame and no
  ground; it sits on the paper.
- Tags in colored serif ("Art & Illustration", "Books", "Philosophy & Ideas"),
  date right-aligned on the same line. Metadata line, not a chip row.
- Sidebar boxes with a flat light-grey ground, a centered small-caps heading,
  and one image. No border, no shadow.
- A navy full-bleed bar closes the page.

System-level cohesion: masthead + ruled nav + centered ruled title on every
page. The image treatment is the identity and is never softened.

Signature move: the title set between rules, and engraved cutouts as spot art.

Steal: hard-cropped plates with no scrim; cutout figures from the plates used
as spot art at fixed sizes; the metadata line (tags left, date right); the
heavier single rule for one role.
Does not transfer: the centered layout (altr is left-aligned and should stay
so), the serif body, the density.

### 1.6 Teenage Engineering - https://teenage.engineering/

What they do: Stockholm hardware company making synthesizers, samplers, and
audio gear (OP-1, Pocket Operators, EP-133).

Pages examined: home (viewport).

Mechanics:
- The nav is a device panel: four groups, each an icon plus a lowercase label
  ("products", "store", "latest", "finder") with a three-line sublist under
  it, laid out across the top like controls on a faceplate.
- Product codes as typography: a three-row table "EP-133 2.5 / EP-40 2.5 /
  EP-1320 1.5" with hairline rows, code left, firmware version right in the
  single orange accent. Everything they make is named like a part number.
- One custom typeface (te-20) at every size. Giant black condensed display,
  small regular labels, no third voice.
- A block of Japanese mission text at 9-10px in the header as texture.
- Hand-drawn black line illustration at full width; no photo in the first
  viewport.
- Radius 0 (declared and observed). Base unit 4.

System-level cohesion: the code-and-version table is the site's reusable
atom; the faceplate nav is on every page (inferred from one page; unverified
for inner pages).

Signature move: part-number typography.

Steal: naming altr's offerings with a code system in mono (for example
"WA-01 Workflow Audit", "WS-02 Workshop") and letting that code appear as the
kicker on the service page, the card, the pricing row, and the footer link.
That single move ties four page types together.
Does not transfer: the illustration style, the lowercase-everything voice.

### 1.7 Commercial Type - https://commercialtype.com/

What they do: New York and London type foundry; retail and custom typefaces.

Pages examined: home (viewport).

Mechanics:
- Boxed nav: "Catalog | Custom | Design | News | Goods | About | EULA | Login",
  each item a white box with a 1px black border, adjacent boxes sharing the
  border. Wordmark boxed top-left, "VIEW CART" boxed top-right.
- Full-bleed flat color bands (cyan, coral, black), each carrying exactly one
  type specimen and one caption ("14 Styles") centered. No gradient, no
  photo, no texture.
- Radius 0. Base unit 12 (declared). Body and h1 both at 22px: the specimen
  is the display type; the UI has one size.

System-level cohesion: every specimen page is a band of one color with one
word on it (inferred from the home page bands; inner pages unverified).

Signature move: the shared-border boxed nav.

Steal: boxed nav items sharing a hairline; the idea that a section can be one
flat color and one sentence.
Does not transfer: saturated color bands (altr's palette is paper and copper).

### 1.8 Lineto - https://lineto.com/

What they do: Zurich type foundry (LL Unica77, LL Brown, LL Schema).

Pages examined: home (viewport).

Mechanics:
- Specimens shown as scanned printed spreads, with mono page labels under
  each ("pp. 1-2", "pp. 3-4"). The website admits it is a book.
- Nav is two black tabs ("LLineto", "Schema") plus a circle search button.
  Two pill buttons bottom-left ("Buy Edition", "-> Schema"). Radius 24px on
  the pills, but the pills are the only rounded thing.
- Horizontal scroll of spreads at full height.

Signature move: pagination captions in mono.

Steal: the "pp." idea. Case studies and long articles on altr could carry a
mono page-number or section-number caption under each figure, tying every
figure to the same manual.
Does not transfer: pills, horizontal scroll.

### 1.9 Herzog & de Meuron - https://www.herzogdemeuron.com/

What they do: Basel architecture practice.

Pages examined: home (viewport), /projects/ (viewport). Project numbering
confirmed from the fetched text ("526 Hauptpost Basel", "648 Sotheby's
Madison Avenue", "492.1 Villa Roccabruna").

Mechanics:
- Every project has a number, and the number precedes the name everywhere.
  Sub-projects get a decimal (492.1). An archive index applied to the work.
- Two voices: a heavy grotesk for the identity ("H&dM", "Menu", "Projects")
  and a mono for every UI control ("Filter", "Search", "Grid", "List",
  "Map", "-> Search for something..."). Same split as Oxide.
- Category chips as outlined mono pills on the home page.
- The projects page is a 16-column grid of tiny thumbnails with a boxed "-/+"
  zoom control. Archive density on purpose.

Signature move: the project number.

Steal: numbering. altr's five case studies become "01 Spark Labs", "02
BeBrief", "03 Fishin' Prints" and so on, with the number in mono on the card,
the page h1, the nav dropdown, and the footer. Sub-engagements get decimals
("01.2 Spark Labs MCP").
Does not transfer: the thumbnail wall.

### 1.10 Craighill - https://www.craighill.co/

What they do: Brooklyn studio designing and manufacturing metal objects
(rulers, carabiners, puzzles, lighters).

Pages examined: home (full page, 8329px).

Mechanics:
- Product grid with 1px vertical rules between cells, running full bleed
  edge to edge. Product name left, price right, in small caps on one line.
  Small square swatches under the name.
- Every product photographed on the same flat grey ground at the same scale.
  Uniform photo treatment is what makes a grid of different objects read as
  one catalog.
- Condensed caps section titles ("COMMUNITY FAVORITES", "DAILY CARRY",
  "DESK") flush left with "View all ->" flush right on the same baseline.
- Nav items separated by 1px vertical rules. A single orange notice bar at the
  very top. Buttons are 1px-bordered rectangles with an arrow, radius 0.
- Body copy in a serif at ~13px under a condensed caps headline: the
  editorial-catalog pairing.

Signature move: the ruled product grid on a uniform ground.

Steal: uniform image treatment (altr's duotone does this already; the
finding is that it must apply to every image with no exceptions, including
headshots and screenshots); title-left / "View all ->" right on one baseline
as the only section header pattern.
Does not transfer: e-commerce density.

### Secondary checks (live, viewed, not analyzed in depth)

- Anduril (https://www.anduril.com/): black ground, a 3px lime rule across the
  very top of the viewport, full-bleed silhouette photography, nav of three
  words ("Sea", "Land", "Air"). Confirms the "one colored rule as the brand"
  move. Radius 2px declared.
- Klim Type Foundry (https://klim.co.nz/): home hero is a solid orange plate
  edge to edge with a two-item nav and one caption ("Die Grotesk") bottom
  left; the Sohne page is a black plate with a single 300px word. Confirms
  the full-bleed one-color, one-word hero. Footer prints "Site build 10
  September 2026 at 11:28am": a build timestamp as colophon.
- Are.na (https://www.are.na/): lettered list "a. / b. / c. +" as the hero
  structure, one hairline rule between sections, 12.5px body. Confirms
  ledger lists as heroes.
- Dinamo (https://abcdinamo.com/): mono used only inside the yellow
  notification cards, with outlined mono tags ("Font Release Event",
  "Hardware"). Confirms mono as the "system message" voice.
- Field Notes (https://fieldnotesbrand.com/): 4-column product grid with
  hairline cells, condensed caps labels, a kraft-paper footer. Confirms the
  catalog grid on a paper ground.

---

## 2. What "raw and industrial" means mechanically

A checklist of binary decisions. For each: the industrial choice, the
polished-SaaS choice, and why the first one reads the way it does. Where a
reference does it, it is named.

1. Corners.
   Industrial: 0-2px radius on everything (Oxide 2px, Commercial Type 0,
   Teenage Engineering 0, Craighill 0, basement 0). The one allowed
   alternative is a 45-degree chamfer (Hadrian).
   SaaS: 8-16px on cards, 999px pills on buttons and tags.
   Why: radius is a softening gesture; machined parts have chamfers, not
   fillets. altr's `.button` currently sits at 10px, and redesign.css carries
   0, 8, and 10 in different rules. Pick one.

2. Rules.
   Industrial: one hairline weight (1px at 13-28% ink) used everywhere, plus
   at most one heavier rule (2-3px) reserved for one role (PDR's 2px blue
   left rule; Anduril's 3px lime top rule).
   SaaS: no rules; separation by background tint and shadow.
   Why: a rule is drawn; a tint is painted. Drawn things read as
   specification.

3. Grid exposure.
   Industrial: borders are shared between adjacent cells (basement's logo
   grid, Oxide's feature cells, Craighill's product grid). The grid is
   visible.
   SaaS: floating cards with gaps, each with its own border and shadow.
   Why: shared borders say "these were cut from one sheet"; gaps say "these
   were placed." Implementation: parent gets `border-top` and `border-left`,
   each cell gets `border-right` and `border-bottom`, gap 0.

4. Shadows.
   Industrial: none. The single exception on altr is the keycap press, which
   is a physical shadow that changes with travel, not an elevation shadow.
   SaaS: layered soft shadows on cards, dropdowns, buttons.
   Why: soft shadows imply glass and plastic surfaces floating over each
   other. Paper and metal do not float.

5. Labels and wayfinding.
   Industrial: mono, uppercase, 11-12px, tracked 0.04-0.15em, and used as a
   closed system: kicker, figure caption, date, tag, spec key, button label,
   nav item. Nothing else is uppercase, nothing else is mono (Oxide's two
   classes; Hadrian's buttons; H&dM's controls).
   SaaS: sans-serif eyebrows in brand color, semibold, sentence case, often
   with an icon.
   Why: mono says "this was typed into a system." It also cannot be made
   pretty, which is the point.

6. Numbering.
   Industrial: things are numbered and the number is shown: FIG. 1, 01/02/03,
   pp. 1-2, project 526, EP-133 v2.5, Showcase (26).
   SaaS: icons in colored circles instead of numbers; no counts.
   Why: numbers imply an index exists behind the page. That is exactly what a
   consultancy that "maps workflows" should imply.

7. Display type.
   Industrial: one family, large, regular or medium weight, tight tracking
   (Oxide 400 weight at 36px, -0.013em; Hadrian light at 72px; Sanctuary
   regular at 40px). Contrast comes from size and from mono vs sans.
   SaaS: bold or extrabold headings with gradient text or a colored word.
   Why: heavy weight is emphasis; regular weight at large size is
   confidence. altr's h1/h2 are already 500 weight at -0.032em; keep that.

8. Two-tone headings.
   Industrial: first clause full ink, second clause dim ink (Oxide on every
   inner page). At most one accent word, and not in every heading.
   SaaS: gradient text, or the brand color on the "important" word every
   time.
   Why: dimming is subtraction; coloring is addition.

9. Imagery.
   Industrial: one treatment applied to every image with no exception
   (Craighill's grey ground; Oxide's green mockups; PDR's untouched scans;
   altr's duotone). Hard rectangular crops. No scrim gradients over images;
   if text must sit on an image, put the text on a flat paper panel that
   overlaps the image with a hard edge (PDR's sidebar boxes do this beside
   images; Hadrian's chamfered frame contains its drawing).
   SaaS: photos with soft gradient overlays, rounded corners, and a blur.
   Why: a gradient scrim is a fade, and fades are the softest thing a page
   can do. altr's current `.hero-plate-bg::after` stacks a 5-stop horizontal
   gradient on a 4-stop vertical one. That is the single largest source of
   "not raw" on the home page.

10. Captions.
    Industrial: every image has a mono caption or figure label, and it sits
    in a fixed position (Oxide: boxed label top-right of the figure; Lineto:
    centered under; PDR: metadata line under).
    SaaS: no captions; alt text only.
    Why: a caption turns a picture into evidence.

11. Buttons.
    Industrial: rectangle, 1px border or flat fill, mono or sans uppercase
    label, arrow suffix that states direction (Hadrian: down arrow for
    in-page, right arrow for navigation). Hover changes one property.
    SaaS: pill, gradient fill, glow on hover, icon on the left.
    Why: the button should look like a control, not a badge. altr's keycap
    press is compatible with this as long as the cap is square-cornered
    (real keycaps have roughly 1-2mm radius at scale; 2-4px is honest, 10px
    is not).

12. Section headers.
    Industrial: one pattern only. Rule on top, kicker (mono) directly under
    the rule, then the title; or title flush left with the "View all ->"
    link flush right on the same baseline (Craighill). Left aligned.
    SaaS: centered eyebrow, centered title, centered subtitle, on every
    section.
    Why: centered stacks are symmetrical and symmetrical is decorative.

13. Density and void.
    Industrial: dense where the content is dense (spec tables, ledgers,
    archive grids at 13px) and empty where it is not (Hadrian's 600px void;
    Oxide's 200px between blocks). The contrast between the two is the
    rhythm.
    SaaS: uniform medium density; every section the same height with the
    same padding.
    Why: a manual has dense pages and blank pages. A brochure has neither.

14. Metadata as content.
    Industrial: build timestamps (Klim), live clocks (Hadrian), item counts
    (basement), edition numbers (BSMNT.26), addresses in mono in the footer
    (Oxide, Hadrian, Teenage Engineering).
    SaaS: social icons and a newsletter form.
    Why: metadata proves the thing is running.

15. Motion.
    Industrial: one physical motion tied to one metaphor (altr's key travel;
    Hadrian's border contraction), 100-800ms, no bounce, no fade-in-on-scroll
    for content, no parallax.
    SaaS: staggered fade-up on every section, hover lift on every card,
    animated gradient backgrounds.
    Why: fade-ins say "this page is a presentation." Content that is already
    there when you arrive says "this page is a document." Any motion beyond
    the key press should be cut or made invisible (under 150ms opacity
    only).

16. Color.
    Industrial: two inks (full and dim) on one ground, one accent in at most
    four named roles (Oxide, Hadrian, Anduril, Teenage Engineering all hold
    to this). No second accent.
    SaaS: a primary, a secondary, semantic greens and reds, tinted section
    backgrounds.
    Why: one accent means every appearance of it is a decision. altr's
    redesign.css carries a second color `--bay: #2F4A52`; see cuts.

---

## 3. Cohesion mechanics for a 50-page site

### 3.1 The minimum viable set of section archetypes

Observed counts: Oxide's five examined pages use seven blocks total. Sanctuary
uses about five on a very long home page. Hadrian's home uses four. basement's
home uses five. None of these sites has a "special" section that appears once
and nowhere else, except a closing statement footer, which is then identical
everywhere.

The practical floor is 7-9 archetypes: two heroes, one statement, one ledger,
one grid, one figure, one prose column, one CTA band, one footer. Fewer than
seven and the article and case-study pages lack a body type; more than nine
and you are back to designing pages instead of assembling them.

The test for whether a block is an archetype: it must appear on at least three
page types. If it appears on one page, it is a bespoke component and it is the
reason the site feels sporadic.

### 3.2 Page-type taxonomy for a consultancy

Derived from the 50 files in altr-site and checked against what Oxide and
Sanctuary need. Eight page types cover all of them.

| Page type | altr examples (count) | Composition, in order |
|---|---|---|
| Home | index (1) | Plate Hero, Statement, Ledger (how we work, 3 rows), Grid (services, 3 cells), Figure (one case), Ledger (writing, 3 rows), Press Band, Footer |
| Service | workflow-audit, ai-workshop, custom-agents, internal-products, forward-deployed-engineering, ai-enablement-workshop, ai-governance-lite-smb, ai-workflow-audit-small-business, pricing (9) | Ruled Hero, Statement, Ledger (what happens, numbered), Grid (who it is for or deliverables), Ledger (FAQ or pricing rows), Press Band, Footer |
| Industry | real-estate, nonprofits, ecommerce, law-firms, claude-cre-* (8) | Plate Hero (one plate per industry, reused across that industry's pages), Statement, Grid (workflows we see, 4 cells), Figure (one case), Ledger (services for this industry), Press Band, Footer |
| Case study | impact-* (5), case-studies index (1) | Ruled Hero with mono meta line (client, sector, duration, number), Statement (the problem), Prose column with Figures, Ledger (outcomes as key/value), Press Band, Footer |
| Article / guide | claude-*, mcp-*, rag-*, llm-*, context-engineering-*, writing-a-skill-md, three-phases-*, can-claude-connect-to-costar, ai-code-review-* (about 14) | Ruled Hero with mono meta line (date, reading time, series number), Prose column with Figures and mono sidenotes, Ledger (related, 3 rows), Press Band, Footer |
| Index | resources, tutorials, events, case-studies (4) | Ruled Hero, Ledger (every item is a row: number, title, one line, date), Footer. No grid, no cards. |
| Conversion | start-a-conversation, ai-in-real-estate-guide and its thank-you, local SEO pages (about 5) | Ruled Hero, Statement, form or Ledger, Footer. No Press Band (the page is the press). |
| Utility | about, how-we-altr-work, privacy, terms, website-terms, 404 (6) | Ruled Hero, Prose column, Footer |

Rule: a page type's composition is fixed. A service page cannot add a
testimonial carousel because one client said something nice; the quote goes
in the Statement block as a plain-text quote with a wordmark, the way
Sanctuary does it.

### 3.3 The spine: what makes every page the same site

The spine is the set of elements present on 100% of pages, in the same
position, at the same size. Observed spines:

- Oxide: nav (identical), page column width, mono label class, closing
  statement + link columns.
- PDR: masthead, ruled nav, centered ruled title, footer figures.
- Craighill: notice bar, ruled nav, section header pattern, footer.

For altr the spine should be five things:

1. Nav: identical markup on every page, hairline under it, wordmark left,
   items in mono uppercase 12px, one keycap CTA right.
2. Register line: directly under the nav on every page, a full-column
   hairline with a mono label at each end. Left: page type ("SERVICE",
   "CASE 03", "GUIDE", "INDEX"). Right: one datum (date for articles,
   client sector for cases, "TAMPA, FL" or the week number elsewhere). This
   is the FIG. label idea applied to the page itself. It costs one line and
   it is on every page.
3. Section header: one pattern, one spacing. Hairline, then kicker (mono
   11px, 0.15em, uppercase, dim ink, with an optional two-digit index "02"),
   then title.
4. Press Band: identical on every page except Conversion and Utility. One
   sentence, one keycap.
5. Footer with colophon: link columns, then a mono colophon line with the
   plate credit, the build date, and "altr LLC, Tampa, FL". Identical
   everywhere.

If a page has all five, it belongs to the site even if its middle is unusual.

### 3.4 Vertical rhythm and spacing scale

The sporadic feeling on a multi-page site usually comes from three spacing
systems fighting: component padding, section padding, and hero padding, each
with its own clamp. Observed fix: one base unit and a short ladder.

- Base unit 8px. Component-level: 8 / 16 / 24 / 40.
- Section-level, three steps only: S 64px, M 112px, L 176px on desktop;
  48 / 72 / 112 on mobile. altr's `--section-air: clamp(60px, 7.2vw, 112px)`
  is the M step; add S and L as named tokens and use nothing else.
- Assignment: M between every pair of sections by default. L only after a
  hero and before the Press Band (the Hadrian void). S only inside a ledger
  between its heading and its first row.
- Rules go on top of sections, never on the bottom, so the space above a rule
  is always L or M and the space below it (to the kicker) is always 24px.
  One number people can check.
- Heroes get the same top padding as a section (M), not their own clamp.
  altr's `.hero-plate-inner` has `clamp(36px, 5vw, 68px)` and `.hero-plate`
  has `min-height: min(74vh, 660px)`; a viewport-relative hero height is
  the reason heroes look different from page to page. Fix the plate hero at
  a set height (for example 560px desktop, 420px mobile) and let the ruled
  hero be content-height plus M.
- Line-height ladder: display 1.0, statement 1.14, body 1.5, mono 1.35. No
  other values.

### 3.5 One accent across 50 pages

The observed rule is four roles maximum, and each role is named.

Recommended copper roles for altr:
1. The primary keycap fill (one per page, in the Press Band; a second is
   allowed in the hero on Home and Industry pages only).
2. The one accent word in a two-tone heading, at most one per page, and only
   in the hero.
3. The active state: current nav item underline, hovered link underline,
   pressed keycap.
4. The register line's left label (the page-type label), so copper marks
   "where you are" on every page at the same spot.

Everything else is ink or dim ink: icons, tags, dates, kickers, rules,
figure labels, chart lines. Never copper as a background larger than a
button, never on body text, never on more than two elements visible in one
viewport. `--bay` and any other secondary is removed. If a chart needs a
second series color, use dim ink and a dashed stroke.

---

## 4. Specific recommendations for altr

### 4.1 Eight section archetypes, specified to build

All measurements desktop; mobile collapses to one column and the mobile
spacing steps from 3.4. Column: existing `--page-max` (1180px) with
`--gutter`. Ink `#1A1714`, dim `#5C544B`, soft `#3B342B`, rule
`rgba(26,23,20,0.13)`, copper `#A65529`, paper `#F7F3EC`, plate ground
`#EDE4D6`.

A. Plate Hero
- Fixed height 560px (420px mobile). Engraving as `background-size: cover`,
  duotoned, positioned so the densest part of the plate is on the right
  40%.
- No gradient scrim. Instead a paper panel: a block of `--paper` at 100%
  opacity, left aligned, width 52% of the column, padding 40px, with a
  1px rule on its right edge. The panel overlaps the plate with a hard edge.
  Contents: kicker (mono 11px), h1 (Clash Grotesk 500, clamp 2.35-4rem,
  max 17ch, two-tone allowed), lede (soft ink, 1.5 line-height, max 44ch),
  one keycap.
- Figure label: boxed mono 11px in the plate's top-right corner, 1px rule
  border, 4px 8px padding, paper fill: "PL. 04 / DIDEROT, MENUISERIE".
- Used on Home, four Industry pages, Case Studies index, About. Nowhere
  else.

B. Ruled Hero
- Padding M top, M bottom. Register line already sits above it.
- Kicker with index ("SERVICE 02"), h1 (same spec as A), lede, optional mono
  meta line under the lede: items separated by "  /  " (two spaces, slash,
  two spaces) in mono 11px dim: "CLIENT SPARK LABS / SECTOR PROPTECH /
  8 WEEKS".
- Hairline under the whole block. No image.
- Used on every page that does not get A.

C. Statement
- One sentence, Clash Grotesk 500, clamp(1.6rem, 3.4vw, 2.9rem), max 22ch,
  two-tone (ink, then dim). Existing `.statement` and `.two-tone` cover it.
- Optional Lora italic aside to the right in a 33% column, max 38ch, with
  a 1px rule on its left edge. Cap: one Statement with an aside per page.
- Also the home of testimonials: the quote is the statement in regular
  weight, the attribution is a mono line under it, the client wordmark is
  duotoned ink, 20px tall. No quote marks, no card, no photo.

D. Ledger
- A list where every row is: mono index (11px, dim, "01") in a 64px
  column, title (Clash 500, 1.25rem), body (soft, 1rem, max 60ch), optional
  right-aligned mono datum (date, price, duration). Hairline between rows,
  hairline on top of the first row, none under the last.
- Row padding 24px top and bottom. Rows are not cards; hover changes only the
  title color to copper if the row is a link.
- Used for: process steps, services list, FAQ, pricing rows, outcomes
  (key/value), index pages (every item), related articles, footer link
  columns (without the index).
- This replaces every card list on the site that is a list.

E. Cell Grid
- 2, 3, or 4 equal columns, shared 1px borders (parent border-top and
  border-left; cells border-right and border-bottom), gap 0, radius 0,
  paper fill, no hover lift. Cell padding 32px. Cell content: kicker, title,
  body, optional "->" link in mono at the bottom.
- Every cell is the same height in a row; if content differs, the shorter
  cells keep their empty paper. Do not add an icon unless every cell in the
  grid has one, and then it is a 20px ink line icon in the top-left.
- Used for: services on Home, "workflows we see" on Industry pages,
  deliverables on Service pages, logo grids (client wordmarks duotoned,
  centered, 40px tall).
- This replaces the existing `.card` and `.cards`.

F. Figure
- Image at column width or at 66% left with caption in the remaining 33%.
  Hard rectangular crop, radius 0, duotone applied to every image without
  exception including screenshots and headshots. Optional 1px rule border.
- Caption is mandatory: mono 11px dim, "FIG. 02  /  Intake queue before and
  after the audit" under the image (left aligned) or in the right column
  (top aligned). Numbers restart on each page.
- Plates in this archetype appear as detail crops (a hand, a tool, one
  stage of the machine), 66% or 33% width, never full bleed.
- Used in case studies, articles, and once on Home and Industry pages.

G. Prose Column
- 68ch max, body 1.0625rem, line-height 1.5, ink. H2 at 1.6rem with the
  section-header pattern (hairline, kicker with index, title). H3 at
  1.2rem, no rule.
- Mono sidenotes: 11px dim, in the left gutter on wide screens (the 64px
  index column from D), inline as a ruled block on mobile. Used for
  definitions, dates, source references.
- Lists inside prose use the ledger index style (mono "01") rather than
  bullets.
- Used on articles, case studies, About, How we work, legal pages.

H. Press Band
- Hairline top. Padding L top, L bottom. Left: one sentence in Statement
  size, max 18ch. Right, baseline-aligned: one primary keycap (copper) and
  one mono text link. Nothing else. Same copy on every Service, Industry,
  Case, and Article page; Home may have its own sentence.
- Followed by the footer with no additional spacing.

Footer (not counted as an archetype because it is spine): link columns as
Ledgers without indices, then a colophon line in mono 10-11px: plate
credit, "Built 2026-09-10", "altr LLC / Tampa, FL". The existing
`.plate-credit-foot` becomes this line.

Buttons across all archetypes: the keycap. Radius 2px (4px maximum). Label
in Clash 500 or mono uppercase; pick one for the whole site (mono uppercase
is the more industrial choice and matches Hadrian and Oxide). Primary: copper
fill, paper text. Secondary: 1px ink border, no fill. Both end with an arrow
glyph in the label: "->" for navigation, "v" (or a down arrow character
rendered as SVG, not unicode text) for in-page. Press: 3px translate, shadow
compresses, 120ms, as already built.

### 4.2 Rationing the engraved plates across 50 pages

The plates are the most expensive thing on the site and the fastest to wear
out. Observed discipline: PDR uses one large scan per essay and small cutouts
for spot art; Klim uses one flat plate per page; Oxide uses one hero figure
per page and UI mockups elsewhere. Nobody uses a background image on every
section.

Allocation:
- Full-bleed plate hero (archetype A): 8 pages. Home, Real estate,
  Nonprofits, Ecommerce, Law firms, Case studies index, About, How we work.
  That is 16% of the site.
- Detail crop as a Figure (archetype F): at most one per page on Service,
  Industry, and Case pages; none on Articles unless the article is about the
  workflow the plate depicts. Never behind text.
- Cutout spot figure (a single worker or tool lifted from a plate, no
  ground, 120-200px tall, ink only): allowed in exactly two fixed places
  site-wide, the 404 page and the Press Band on Home. Not scattered.
- Zero plates: Articles, Index pages, Conversion pages, legal, thank-you.
  These pages get their identity from the register line and the ledger, not
  from imagery. Roughly 30 of 50 pages will have no engraving at all, and
  that is what keeps the other 20 special.

Plate library: 6-8 distinct plates total, not one per page. Assign one plate
to each family and reuse it: the workshop floor for Home and How we work;
one trade per industry (real estate, nonprofits, ecommerce, law) reused on
every page in that industry family, so the plate becomes the industry's mark;
one "machine in stages" plate for the Case studies index and its detail crops
across all five case pages. Number the plates ("PL. 01" to "PL. 08") in their
figure labels and list them in the footer colophon. A plate that appears on
six related pages is a system; a different plate on every page is wallpaper.

Treatment: one duotone recipe (paper to ink) with no variation in contrast or
tint per page. Hard crops only. No scrims, no blur, no vignettes.

### 4.3 The one signature move for every page

The register line. A full-column hairline directly under the nav with a mono
label at each end: page type and index on the left in copper ("SERVICE 02",
"CASE 03", "GUIDE 011", "INDEX", "HOME"), one datum on the right in dim ink
("TAMPA, FL / WK 37", or the article date, or the client's sector). Same
height (32px), same type (mono 11px, 0.15em, uppercase), same position on
all 50 pages including 404 and legal.

Why this and not the keycap or the plates: the keycap is on most pages but
not all (index and legal pages have no CTA), and the plates must be rationed.
The register line costs nothing, tolerates every page type, carries the
numbering system that ties services, cases, and guides together, and is the
first thing the eye passes on every page. It is Oxide's FIG. label and
H&dM's project number applied to the page itself.

### 4.4 Cuts to make the current direction more cohesive

1. Cut the gradient scrim on the plate hero. `.hero-plate-bg::after`
   currently layers a 5-stop horizontal gradient on a 4-stop vertical one.
   Replace with the hard-edged paper panel from archetype A. This is the
   single biggest step from "editorial" toward "raw."

2. Cut all radii except one. redesign.css declares 0, 8, and 10px in
   different rules and `.button` is 10px. Set one token, `--radius: 2px`,
   and use it on the keycap only; everything else is 0. The keycap still
   reads as a key at 2px.

3. Cut the second color. `--bay: #2F4A52` is a second accent. Remove it and
   any tinted section grounds; the plate ground `#EDE4D6` stays because it
   is a paper tone, not a color.

4. Cut the second hero. There are three hero shapes in the CSS (`.hero-plate`,
   `.hero-split`, `.page-hero` / `.hero-col`). Keep the plate hero for eight
   pages and the ruled hero for the rest; delete `.hero-split`.

5. Cut the card. `.card` / `.cards` with gaps become the shared-border Cell
   Grid, and every card list that is actually a list becomes a Ledger. A site
   with 98 `.section` instances and 61 `.section-header` instances has
   enough repetition to be cohesive; the cards are where the variation is
   leaking in.

6. Cut motion to one. Filenames suggest a typewriter effect
   (home-typewriter.js), an animated key field (hero-keys.js), and general
   site motion (site-motion.js); I did not audit their contents, so treat
   this as inferred. The rule: the key press is the only motion with
   duration over 150ms. No scroll-triggered fades, no typewriter, no
   parallax. If the animated keycap field in the home hero stays, it is the
   one exception and it exists only on Home.

7. Reduce Lora to two moments per page maximum (one aside, one pull quote),
   and zero on Service and Index pages. Sanctuary caps its serif at two
   moments on a very long page; more than that and the second voice becomes
   the texture instead of the exception.

---

## Sources

Every URL below was fetched live on 2026-09-10 and rendered or parsed as
noted. Firecrawl scrapes and screenshots are in the session scratchpad, not
in the repo.

Primary references (screenshot plus branding extraction; CSS where stated):
- https://oxide.computer/ (full page), https://oxide.computer/product/compute,
  https://oxide.computer/solutions/finance, https://oxide.computer/principles,
  https://oxide.computer/blog; stylesheet
  https://oxide.computer/assets/index-Be2_tqAA.css (mono label classes
  measured). https://oxide.computer/product returned "Page not found".
- https://www.hadrian.co/ (full page; button and clock classes read from raw
  HTML). https://www.hadrian.co/about did not render in scrape; unverified.
- https://www.sanctuary.computer/ (full page)
- https://basement.studio/ (full page)
- https://publicdomainreview.org/ (full page), https://publicdomainreview.org/essays/
- https://teenage.engineering/ (viewport)
- https://commercialtype.com/ (viewport)
- https://lineto.com/ (viewport)
- https://www.herzogdemeuron.com/ (viewport), https://www.herzogdemeuron.com/projects/
- https://www.craighill.co/ (full page)

Secondary checks (viewport or full page, viewed, not analyzed in depth):
- https://www.anduril.com/
- https://klim.co.nz/, https://klim.co.nz/retail-fonts/soehne/
- https://www.are.na/
- https://abcdinamo.com/
- https://fieldnotesbrand.com/ (full page)

Fetched as text only, not used for visual claims:
- https://press.stripe.com/

Local files read for the altr-specific sections:
- C:\Users\alex.britton\projects\altr\altr-site\redesign.css
  (tokens, `.section-kicker`, `.button`, `.hero-plate*`, `.statement`)
- C:\Users\alex.britton\projects\altr\altr-site\design-language\DESIGN.md
  (earlier Tenex reference study; not re-verified here)
- Page inventory: 50 top-level HTML files in the repo root, counted on disk.
