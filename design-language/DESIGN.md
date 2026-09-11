# DESIGN.md: Tenex (www.tenex.co)

## Source
- URL: https://www.tenex.co/
- Capture date: 2026-09-10
- Evidence: Firecrawl `branding` + `images` scrape (`.firecrawl/tenex-branding.json`), page markdown (`.firecrawl/tenex-home.md`), full-page screenshot (`.firecrawl/tenex-screenshot.png`, 1920x4639)
- Firecrawl confidence: colors 0.9, buttons 0.9, overall 0.9

> Third-party reference only. Tenex's logo, wordmark, statue imagery, GIFs, partner logos, and copy are theirs. Reuse the **system** (structure, rhythm, contrast strategy, motion ideas) and rebuild every asset and line of copy as altr's own.

## Reference Screenshot
![Full-page screenshot of Tenex](../.firecrawl/tenex-screenshot.png)

Use the screenshot as the visual source of truth for layout, hierarchy, density, and feel. The tokens below describe the same page in machine-readable form.

## Design Summary

A near-black, high-contrast consulting site that reads like a manifesto rather than a brochure. Almost the entire page is `#000000` with white text; a single electric yellow (`#FFE501`) does all the accent work. Zero border radius anywhere: hard rectangles, hairline 1px borders, no shadows. Enormous display type (h1 ~120px) in a quirky pixel/retro serif sits directly on top of desaturated black-and-white classical-statue imagery (animated GIFs), which is the entire visual identity: ancient marble doing modern things. Sections are separated by huge vertical voids rather than dividers, with one full-bleed yellow diagonal marquee as the only chromatic interruption. Copy is short, declarative, and slightly confrontational ("Win the next decade.", "AI isn't scary. Ignoring it is.").

## Design Tokens

### Colors

| Role | Value | Notes |
|---|---|---|
| `--bg` | `#000000` | Observed. Dominant page ground. |
| `--surface` | `#0E1520` | Observed (reported as secondary). Very dark blue-black; card/panel ground. |
| `--surface-2` | `#1E2733` | Observed (reported as link color). Hairline borders and hover fills. |
| `--accent` | `#FFE501` | Observed. Electric yellow. Primary *and* accent: one accent only. |
| `--text` | `#FFFFFF` | Observed. |
| `--text-dim` | `#8A8A8A` approx | Inferred from screenshot. The de-emphasized half of split headlines ("AI-absent to AI-native") and card body copy. |
| `--border` | `rgba(255,255,255,0.18)` approx | Inferred. 1px hairline card outlines. |
| Button primary | bg `#FFFFFF`, text `#000000`, border `#000000` | Observed. |
| Button secondary | bg `#000000`, text `#FFFFFF`, border `#FFFFFF` | Observed. |

Color scheme is declared `dark`. There is no light mode.

Accent discipline: yellow appears in roughly four places on the whole page -- the logo mark, one word in the subhead, one clause in the pull-quote, and the marquee band. That scarcity is the point.

### Typography

Observed font families (four, layered):

| Role | Family | Fallbacks |
|---|---|---|
| Display (h1, section headlines) | `Mondwest` | `Arial, sans-serif` |
| Heading | `Avenir Next` | system sans |
| Body | `Inter Tight` | `Avenir Next, system-ui, sans-serif` |
| Body alt | `GT Standard L` | system sans |

Observed sizes: `h1` 120px, `h2` 36px, body 20px.

Mondwest is the signature: a pixel-flavored transitional serif that carries the "ancient meets machine" idea. Avenir Next / Inter Tight handle everything functional. Body copy inside cards drops to roughly 13-14px with generous line-height, which makes the 120px display type feel even larger.

Inferred scale (px, desktop): `120 / 56 / 36 / 20 / 16 / 13`. Eyebrow labels ("OUR APPROACH") are ~11px, uppercase, letter-spaced ~0.12em, white.

Heading treatment: headlines wrap to 2-3 short lines and are set tight (line-height ~0.95-1.0). Two-tone headlines are common: first clause white or yellow, remainder in `--text-dim`.

Substitution note for altr: Mondwest is licensed. Either pair a characterful display serif with the existing `--serif` Lora, or keep Clash Grotesk for display and move the "quirk" into imagery instead.

### Spacing And Layout

- Base unit: `4px` (observed). Practical scale: `4 / 8 / 16 / 24 / 40 / 64 / 96 / 160`.
- Border radius: `0px` everywhere (observed) -- buttons, cards, images, marquee.
- Shadows: `none` (observed).
- Borders: 1px hairline only.
- Content column: roughly 1180-1280px centered, but content is frequently pushed off-center. The hero headline sits left-of-center over a centered image; the approach section is a 40/60 split.
- Section rhythm: very large, 160px+ of vertical air between sections. Black emptiness is the separator; there are no rules.
- Full-bleed breaks: statue photography and the yellow marquee run edge-to-edge, ignoring the container.

## Components

**Nav.** Fixed, transparent over black. Left: small yellow mark plus "Tenex" wordmark. Right: hamburger even on desktop. The full link set (Home / AI Transformation / AI Engineering / Who We Are / Careers, plus a Resources group of Blog / Playbooks / Newsletter) lives behind it, with a single "Get Started" CTA. Minimal chrome, maximum hero.

**Hero.** Centered animated GIF of a classical statue holding a phone, with the 120px display headline overlapping it: type sits in front of the image, the statue's head rising above the baseline. Below, a left-aligned yellow-accented subhead, one line of body copy, a long thin horizontal rule that terminates in an arrowhead, and a white "Learn more" button. That rule-into-arrow is the site's signature connector.

**Service cards (3).** Stacked in one column on the right half of a two-column section. Each: 1px white hairline border, black fill, 0 radius, generous inner padding. Large bold sans title (~28px), 3-4 lines of dim body, a "Learn more" link with arrow, and a line-art outline icon (brain / hammer / globe) at the right. Each icon ships as an outline PNG plus a photo WebP, which implies a hover crossfade from wireframe to photograph.

**Split headline block.** Eyebrow label, then a headline where the first words are brand-colored and the rest fades to grey: "**Tenex** helps you shift from *AI-absent to AI-native*." A yellow logo glyph anchors the bottom-left.

**Pull-quote over full-bleed image.** Statue wearing VR goggles bleeds off the left edge; a two-tone line ("AI isn't scary." white / "Ignoring it is." yellow) sits right, over a faint grid pattern.

**Partner strip.** A black bar with a 1px border overlapping the image above it: "Partnered with the best:" followed by monochrome wordmarks (Anthropic, OpenAI, Vercel, Lovable, LangChain, Braintrust) all rendered white.

**Marquee band.** Full-bleed yellow bar rotated ~2deg, scrolling black text "Built by builders, trusted by leaders" repeated with bullet separators. The one loud chromatic moment in the page.

**Closing CTA.** Centered yellow glyph, a two-line grey display headline, a single white "Get Started" button, then a full-width GIF (statues around a laptop) as the closer.

**Footer.** Sparse: logo, copyright, two links (Blog, Playbooks), an email address, two social glyphs. No sitemap, no newsletter form, no columns.

**Buttons.** Rectangular, 0 radius, no shadow. Primary is white fill with black text. Secondary is black fill with a white 1px border. Both carry a small trailing arrow glyph in a boxed cap.

## Page Patterns

Section order: Nav, hero (image with overlapping display type), positioning subhead plus CTA, approach split (eyebrow and two-tone headline on the left, three service cards on the right), full-bleed image with pull-quote, partner strip, yellow diagonal marquee, closing CTA, full-bleed closing GIF, footer.

Repeating moves worth stealing:
1. Type overlapping imagery instead of sitting beside it.
2. Two-tone headlines that use color to mark the thesis clause.
3. A thin rule ending in an arrowhead as the CTA connector.
4. Outline-icon to photo crossfade on card hover.
5. One rotated full-bleed band as the sole color interruption.
6. Black voids as section dividers: no rules, no alternating backgrounds.

Responsive (inferred): single column below ~900px, display type scales to roughly 48-64px, service cards remain stacked, full-bleed images crop rather than letterbox, the marquee keeps its rotation.

## Content Style

Voice: short, imperative, high-stakes. Headlines are complete sentences ending in periods: "Win the next decade." / "Stay on the right side of history." Positioning is one line ("Your AI transformation partner."), proof is one line ("We set & execute your enterprise AI strategy at startup speed.").

Service copy leads with the anti-pitch -- "No 6-month strategy work. No 200-slide presentations." -- naming what they refuse to do before what they deliver. Engineering copy sells the pricing model as the differentiator: "you pay for features delivered, not hours logged."

CTA wording is minimal: "Learn more" and "Get Started" only. One repeated tagline ("Built by builders, trusted by leaders") does the brand work in the marquee.

Copy density is very low. The entire homepage is roughly 150 words.

## Agent Build Instructions

altr currently runs the inverse palette: warm paper (`--paper #F7F3EC`), ink (`--bone #1A1714`), copper accent (`#A65529`), 8px radius, Clash Grotesk plus Lora. Tenex is stark black, 0 radius, electric yellow. Do not port the colors wholesale. Port the structural decisions, which are palette-independent:

1. **Keep altr's palette and type.** Take the layout system, not the skin. If a dark treatment is wanted, scope it to one section rather than inverting the site.
2. **Adopt the vertical rhythm.** Increase section spacing to ~160px desktop / ~96px mobile and delete divider rules. Let empty ground separate sections.
3. **Adopt the overlapping hero.** Move the hero headline to overlap its visual rather than sitting in a column beside it. altr already has an animated keycap hero, so layering the headline over it is a small change.
4. **Adopt two-tone headlines.** First clause in `--bone`, remainder in `--bone-dim`, with `--copper` on the single thesis word. One copper word per headline, maximum.
5. **Adopt the anti-pitch card copy.** Rewrite the three service cards to lead with what altr refuses to do, then what it delivers, in 3-4 lines. Cap each card at ~35 words.
6. **Adopt the rule-into-arrow connector** as a reusable inline SVG next to secondary CTAs.
7. **Adopt the outline-to-photo card hover** only if real photography exists. A crossfade to stock imagery would cheapen it.
8. **Consider one rotated full-bleed band** in copper carrying a single altr tagline. Exactly one per page.
9. **Do not adopt**: the desktop hamburger (altr's nav dropdown already works, and hiding nav hurts SEO), the 120px display size at altr's line lengths, or the near-empty footer (altr's footer carries Services / Work / Blog / About / Terms / Privacy and should keep them).
10. **Imagery direction.** Tenex's whole identity is one committed visual idea (monochrome classical statuary doing modern things) executed consistently on every section. The transferable lesson is *commit to one idea*, not *use statues*. Pick altr's equivalent and repeat it site-wide.

Accessibility: Tenex's dim grey on black is the weak point. Several dim headline halves fall near or below 4.5:1. If porting two-tone headlines, verify `--bone-dim` (`#5C544B` on `#F7F3EC`, about 7.3:1) stays above 4.5:1 at every size used.

## Rerun Inputs
workflow: firecrawl-website-design-clone
source_url: https://www.tenex.co/
target_stack: static HTML + CSS (altr-site, no framework)
output: design-language/DESIGN.md
