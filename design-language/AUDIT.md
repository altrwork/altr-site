# Cohesion audit: why the site reads as sporadic

Counted across all 50 HTML pages and the 6,063-line `styles.css`, before any
system work. This is the evidence behind "looks sporadic" - it is not a feeling,
it is component sprawl.

## 1. There are really only six page types

| Count | Hero class | What the pages are |
|---:|---|---|
| 17 | `page-hero` | Services, industries, offers |
| 13 | `page-hero article-hero` | Blog posts and tutorials |
| 5 | `page-hero impact-page-hero` | Case studies |
| 4 | `page-hero article-hero cre-article-hero` | CRE field guides |
| 2 | `learning-hero` (+2 modifier classes each) | Index pages: tutorials, resources |
| 1 | `strategy-hero` | how-we-altr-work |
| 1 | `lede-hero` | Legal |
| 1 | `lead-magnet-hero` | Guide download |
| 1 | `hero-plate` | Home |
| 1 | `about-simple` | About |
| 3 | none | 404, redirect stub, thank-you |

Six real types are doing the work of ten hero implementations: **home, service,
article, case study, index, utility.** Every extra hero class is a place where
the site can drift, and it has drifted.

## 2. Eight card components where one or two would do

| Uses | Component |
|---:|---|
| 120 | `engagement-item` |
| 13 | `tutorial-card` |
| 11 | `resource-item` |
| 6 | `work-card` |
| 6 | `workshop-topic-card` |
| 5 | `impact-card` |
| 4 | `real-estate-card` |
| 2 | `founder-card` |

`engagement-item` alone covers 120 of roughly 167 card instances. The other
seven exist for specific pages and each carries its own padding, border, radius,
and hover behavior. A reader moving between two pages sees two different
languages for the same idea.

## 3. Section wrappers are equally split

`product-page-section` (59), `article-block` (91), `cta-section` (29),
`article-section` (17), `band` (5), `strategy-section` (3), plus one-offs for
tutorials, workshops, real estate, guides, and about. Several set their own
vertical padding, so the rhythm changes from page to page.

## 4. The decorative layer fights "raw and industrial"

`styles.css` carries **25 `linear-gradient`** declarations and **40
`box-shadow`** declarations. Several core surfaces - `content-split`,
`intake-panel`, `impact-detail`, `featured-work-card` - are built from a copper
diagonal gradient over a translucent fill, with a radius and a soft shadow.

That combination is the house style of generic SaaS. Raw and industrial is the
opposite: flat ground, hairline rules, square corners, and contrast carried by
type and structure rather than by light effects. The keycap press is the one
shadow that earns its place, because it is the brand metaphor doing real work.

## 5. The palette has drifted

Counting every color literal in `styles.css`, the warm family holds almost
everywhere: ink `rgba(26,23,20)` 47 uses, copper `rgba(166,85,41)` 20, paper
`rgba(247,243,236)` 14, plus sage and steel at 6 each.

Then three colors appear that belong to no palette anywhere else on the site:

| Color | Uses | Where |
|---|---:|---|
| `#b48cc8` lavender | 3 | `.tutorial-thumb-rag` |
| `#dcad50` amber | 3 | `.tutorial-thumb-automation` |
| `#8fa8d4` cornflower | 3 | `.tutorial-thumb-skills` |

They are the category tints on blog thumbnails. Six tutorial thumbnails are
colored diagonal gradients, three of them off-palette. On a warm paper site
these read as pastel stickers, and the blog index is where a reader forms their
impression of whether the site is one thing or several.

## 6. What this means for the fix

The work is consolidation, not more design:

1. Collapse ten hero implementations into **one hero archetype with six
   documented variants**, one per page type.
2. Collapse eight card components into **two**: a bordered card for things you
   click, a hairline row for things you read.
3. Put **every section on one vertical rhythm** driven by a single token.
4. **Strip the gradients and soft shadows** from surfaces. Keep exactly one
   shadow: the keycap press on buttons.
5. **Retire the three off-palette category tints** and give the blog thumbnails
   a treatment drawn from the plates instead.
6. Ration the engraved plates deliberately so they stay an event rather than
   wallpaper.

Reference study and the archetype spec live in [RESEARCH.md](RESEARCH.md).
