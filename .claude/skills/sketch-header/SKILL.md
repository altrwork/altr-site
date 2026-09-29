---
name: sketch-header
description: Draw a custom hand-drawn "sketchbook" header illustration for an altrwork.com article, guide, or case study, and export it as the page's header, card image, and link preview. Use when adding or updating a learning center article, when a page needs a header image or social/OG image, or when asked to design, redraw, or change one of these headers.
---

# Sketchbook header illustrations

Every learning center article gets one custom illustration in the sketchbook style: wobbly
hand-drawn ink lines, soft sage, steel blue and copper fills, and a handwritten Kalam title on
warm white. It matches the CRE field guide art. It is the chosen house style for article
headers, so do not offer other styles unless asked.

Each drawing is a small SVG written by hand. The drawing holds only shapes and class names.
`sketch.css` supplies every color and the hand-drawn wobble, so the whole set stays
consistent and a restyle is one CSS edit.

## Where this runs

- **In the altr-site repo (Claude Code):** follow all four steps below. Steps 3 and 4 render
  with a browser and write the site's images.
- **Anywhere else (claude.ai, or no repo checked out):** do steps 1 and 2, writing the drawing
  to any file. Then run `python header.py standalone <drawing.svg>` from this skill's folder.
  It needs nothing installed and writes `<drawing>-header.svg`, one self-contained file with
  the style and font built in. Open it or read it back to check it. Hand the user both files:
  the plain drawing, which goes in the repo's `design-language/headers/svgs/<slug>.svg`, and
  the standalone preview. Exporting and wiring into the site (steps 3 and 4) happen later in
  the repo.

## Files

- `design-language/headers/svgs/<slug>.svg` - the source drawing for `<slug>.html`. One per page.
- `sketch.css` (in this skill) - the style. Don't restyle a single drawing.
- `header.py` (in this skill) - renders previews, exports, and standalone files.
- `examples/` (in this skill) - four finished drawings to match for level of detail.
- `assets/headers/<slug>.png` and `.webp` - the exported images the site serves.

## 1. Choose the idea

Read the page first: at least its h1, short answer, and section headings. Then pick ONE
visual idea that shows what the article argues. It can be a metaphor or a small, legible
diagram of how the thing works. Examples from the set:

- What is an MCP server? - a chat bubble reaches CRM, files and data only through one door.
- What is a BOV? - a balance scale weighs the subject building against a pan of comps.
- Can Claude connect to CoStar? - a fork in the road: the licensed data is fenced off behind a "Terms" barrier, and the open path leads to county records and your own files.

Avoid these:

- number or stat cards
- robots, brains, glowing orbs, or a laptop with nothing specific on it
- walls of text
- vendor logos (use neutral stand-ins and text labels)

Vary the layout. Run `sheet` (see step 3) and check that the new drawing isn't the same
layout as its neighbors. Layouts that have worked: left-to-right flow, central object,
before/after split, loop, stack, map, funnel, balance, timeline, fork in the road, staircase.

## 2. Write the SVG

`design-language/headers/svgs/<slug>.svg` holds inner SVG markup only: no `<svg>` wrapper,
no `<defs>`, no background. The first two lines are required comments:

```
<!-- title: Short headline, 30 characters max -->
<!-- concept: one sentence on what the picture shows -->
```

The script draws the title centered at the top (baseline y=118). It can be a tightened
version of the article title.

**Canvas:** viewBox `0 0 1200 630`. Keep all art and labels inside x 70-1130, y 180-590.
A label at 26px Kalam takes about 15px per character. Keep labels to 1-2 words, 12
characters at most, and leave room to their right.

**Classes.** Give every element exactly one:

| class | draws |
|---|---|
| `ln` | ink outline, no fill: lines, curves, small details |
| `f1` | white shape with ink outline: cards, sheets, bubbles |
| `f2` | sage fill |
| `f3` | steel blue fill |
| `f4` | copper fill. Use it sparingly, for the one thing that matters. |
| `acc` | copper stroke, no fill: the main flow or arrow shaft |
| `dash` | dotted connector |
| `lbl` | text label |

**Rules:**
- Arrowheads are small `<polygon class="f4">`.
- Use only rect (rx is fine), circle, ellipse, line, polyline, polygon, path, and text (x/y, optional `text-anchor="middle"`).
- No markers, gradients, filters, images, `<use>`, clipPaths, or `style=`/`fill=`/`stroke=`/font attributes.
- Paint order is document order, so draw back to front.
- Aim for 20-60 elements: enough to feel illustrated, clean enough to read on a card about 400px wide.
- Reference drawings: `examples/` in this skill, starting with `what-is-an-mcp-server.svg`.

## 3. Check it

Run from the repo root:

```
uv run --no-project --with playwright --with pillow python .claude/skills/sketch-header/header.py preview <slug>
```

Read `design-language/headers/preview/<slug>.png`. Look for these problems:
- clipped or overlapping labels
- lines running through text
- art too small at card size
- anything that reads as generic

Make one fix pass, then move on. `header.py sheet` renders every drawing on one contact
sheet (`preview/_sheet.png`), which is the quickest check that the set still looks like one family.

If Playwright says the browser is missing, run
`uv run --no-project --with playwright python -m playwright install chromium` once.

## 4. Export and wire it in

```
uv run --no-project --with playwright --with pillow python .claude/skills/sketch-header/header.py export <slug>
```

This writes `assets/headers/<slug>.png` (1200x630) and `assets/headers/<slug>.webp`. Then
update the page. Follow `claude-cre-skills.html`, which already does the first three:

- `og:image` and `twitter:image` -> `https://altrwork.com/assets/headers/<slug>.png`
- the Article schema `"image"` -> `https://altrwork.com/assets/headers/<slug>.webp`
- the header figure under the h1: `<figure class="cre-hero-image"><picture><source srcset="assets/headers/<slug>.webp" type="image/webp" /><img src="assets/headers/<slug>.webp" width="1200" height="630" alt="..." /></picture></figure>`, with alt text that describes the picture
- the page's card in `learn.html`. The cards currently use a `<span class="cell-mark mark-*">` engraving. Swapping in the header image is a layout change, so confirm the card treatment with the user the first time.

`preview/` is scratch output. Delete it or leave it untracked; don't commit it. Commit the
`.svg` source together with the exported images, so the source always matches the site.
Commit or push only when the user asks.
