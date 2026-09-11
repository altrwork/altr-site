# AI slop: what it is, and what was on this site

Run against all 45 pages and both stylesheets. Every count below came from a
script over the files, not from reading a sample.

The headline finding is not what I expected. The **copy** is close to clean: 12
slop-word instances on the whole site, and most of those are false positives.
The **visuals** were not: `styles.css` still carried 19 soft drop shadows, 21
different border radii, 20 gradients and an ambient background animation, all
of which the design system had supposedly already banned.

Slop, on this site, was a CSS problem wearing a copy problem's reputation.

## 1. What AI slop actually is

### Visual tells

| Tell | Why it reads as generated |
|---|---|
| Soft drop shadows (`0 20px 40px rgba(...)`) on every card | A default of every template and UI kit. Printed matter has edges, not glows. It is the single clearest tell. |
| Many different border radii in one page | A human picks one radius and holds it. Generated pages inherit 4px here, 12px there, a 999px pill somewhere else. |
| Diagonal gradients over a translucent fill | The house style of SaaS landing pages since roughly 2019, and the default of every AI page builder. |
| Ambient background blobs, slowly drifting | Decoration with no referent. Nothing in the content is round, purple or moving. |
| Scroll-triggered fade-and-rise on every block | Motion applied by selector list rather than by meaning, so everything animates and nothing is emphasized. |
| Corporate Memphis illustration | Unmistakable, and unattached to any specific business. |
| Generic line icons, one per feature card | Icons chosen to fill a slot, not to show a thing. A wrench for "tools", a rocket for "launch". |
| Three feature cards, equal length, equal weight | The most templated layout on the web. |
| Stock photography of people at laptops | Says nothing a reader could not assume. |

### Copy tells

Vocabulary: unlock, elevate, seamless, empower, leverage (as a verb), robust,
revolutionize, game-changing, cutting-edge, harness, supercharge, transformative,
holistic, bespoke, curated, delve, navigate, journey, landscape, in today's
fast-paced world.

Constructions, which matter more than the vocabulary:

- "It is not just X, it is Y"
- "Whether you are A or B"
- The rhetorical question opener
- "Now imagine..."
- Rule-of-three everything: three benefits, three steps, three adjectives
- Every section the same length, because the generator was asked for sections
- Headings that name a category ("Our Process") instead of making a claim
- Em dashes and curly quotes, because the model emits them and a person typing
  in an editor usually does not

The deepest tell is structural: **claims with nothing behind them.** "Improves
margin, drives revenue, frees your team" is slop not because of the words but
because no evidence follows. A human who did the work names the client, the
workflow, or the constraint.

### What avoids it

Specifics. Named clients. Numbers that come from somewhere. Admitting what you
do not do. Sentences of uneven length. One visual idea carried all the way
through instead of decoration applied per section.

## 2. What was found here

### 2.1 Copy: 12 slop-word instances, 5 real

Most hits were false positives: `cre-harness` is a product name (6), "where the
leverage lives" is the noun, "Comprehensive state privacy laws" is a legal term
of art, "unlock building entry" is literal.

Five were real and are fixed:

| File | Was | Now |
|---|---|---|
| `case-studies.html` | "Let's explore how AI can support your goals and unlock new opportunities." | "Tell us the process your team keeps repeating and we will tell you whether AI belongs in it." |
| `claude-cre-skills.html` | "custom solutions tailored to your business and the bottlenecks you currently face" | "around the workflow your team already runs and the place it actually breaks" |
| `claude-cre-connectors.html` | "Now imagine every system your team runs on wired together" | "The same applies to every system your team runs on" |
| `claude-cre-scheduled-tasks.html` | same sentence, second page | rewritten |
| `claude-cre-skills.html` | same sentence, third page | rewritten |

That last one is the interesting case: the identical "Now imagine..." opener
appeared on three pages. A template used three times is a stronger tell than any
single word.

### 2.2 Punctuation: 73 instances

34 em dashes, 24 curly apostrophes, 14 curly quotes, 1 en dash, plus entity
forms. All normalized to ASCII across 52 files. This is both an AI-text tell and
the house standard.

### 2.3 Visuals: the actual problem

`styles.css` carried, after the earlier cleanup:

- **19 non-keycap box-shadows**, including `0 24px 56px`, `0 18px 40px`,
  `0 28px 70px`
- **21 distinct border-radius values**: 999px pills, 50%, 24px, 18px, 12px,
  10px, 8px, 6px, 5px, 4px, 3px
- **20 gradients**
- **`ambient-drift`**, an 18-second infinite background animation
- **21 transitions longer than 150ms**

The design system had banned all of this. It did not hold because the earlier
pass enumerated components by name, and any component not on the list kept its
shadow. The fix is to state the rule once and list the exceptions:

```css
*, *::before, *::after { box-shadow: none; border-radius: 0; animation: none; }
```

with the keycap press, the focus ring, the current-page underline and the form
fields added back explicitly. 95 lines replace what enumeration could not cover.

### 2.4 Animated fake demos

`how-we-altr-work.html` shipped two animated demonstrations of deliverables that
do not exist: an "Opportunity Map" that scanned, and a "30-day Roadmap" that
filled in. 100 lines of JavaScript drove them. This is the purest form of slop
on the site, because the animation existed to make an invented product feel real.
Both are gone, with the product they advertised.

## 3. What is left

Honest remaining work, not yet done:

1. **Unverified claims.** "Improves margin, drives revenue" and similar appear
   on several pages with no case study behind them. Same category as the 7-day
   audit: a specific-sounding promise with nothing under it. Needs the client to
   say what is actually provable.
2. **Section length uniformity.** Several pages still run sections of
   near-identical length, which reads as generated even when each section is
   individually fine.
3. **Mobile.** Never verified on a real device.
