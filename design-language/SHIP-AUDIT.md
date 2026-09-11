# Ship-readiness audit: what is still wrong

Run against the 45 HTML pages, styles.css (4,181 lines), redesign.css
(1,533 lines), 5 JS files, _redirects, sitemap.xml, llms.txt, README.md and
the deployed asset folders, on main at 6c95dbd. Read-only. Every count came
from a script over the files; every quote was checked against the file at
the line given. Mobile findings were rendered in headless Chrome at a true
375px layout width (the page inside a 375px iframe; Chrome's window floor
is 504px, which is why naive --window-size=375 screenshots lie) and at 768px.

Not repeated here: anything DEBT-AUDIT.md, SLOP-AUDIT.md, AUDIT.md or
SYSTEM.md already reported and that has since been done (page merges,
static nav, CTA labels, ASCII punctuation, the 7-day audit). Prior findings
that are still open are listed once, at the end, so they do not get lost.

Main-column word count today (nav, footer, scripts excluded):
29,228 across 45 pages. Ten pages over 700 words, worst first:
terms 3,730; ai-consulting-tampa 1,234; real-estate 1,185;
ai-enablement-workshop 1,161; workflow-automation-consultant-tampa 1,161;
mortr 1,108; privacy 971; website-terms 878; claude-cre-connectors 873;
claude-cre-skills 868. The enablement page grew (1,149 -> 1,161) since the
last audit; real-estate barely moved (1,255 -> 1,185).

---------------------------------------------------------------------------

## CONFIRMED, ranked

### P0. These would embarrass you in front of a CRE prospect

**1. The homepage sells three outcomes it cannot back.**
index.html:188-200, the "Who this is for" band:

    L189  <h3>More deals through the door</h3>
    L190  The work that finds and closes business stops sitting behind the
          work nobody wanted to do.
    L194  <h3>Hours back every week</h3>
    L195  The steps your team repeats by hand get handled by a system
          instead, and the week opens up.
    L199  <h3>More volume, same team</h3>
    L200  You take on more without hiring for it, and the cost of carrying
          each deal comes down.

Revenue, time and unit-cost claims with no case study, number or client
behind them. The site contradicts itself on this within one click:
ai-consulting-tampa.html:279 says "No invented hours saved stats." The same
promise recurs on how-we-altr-work.html:119 ("decide how AI moves time,
margin, and revenue") and in index.html:32 twitter:description ("so your
best people spend those hours on the deals"). This is the exact category
the client killed the 7-day audit for.
Severity: P0. Fix: delete the band or rewrite each card as a thing a named
client did ("spARK Labs stopped retyping receipts into Excel"), and drop
"margin, and revenue" from how-we-altr-work.html:119.

**2. The only CRE proof is anonymous, undated and stock-illustrated.**
impact-real-estate-property-intelligence.html is the one case study a CRE
prospect will open. It names no client, and its "Impact" section is three
paragraphs of unfalsifiable outcome:

    L158  cre harness has improved how multiple CRE teams conduct property
          research, pursue new assignments, and produce client facing
          materials.
    L159  Teams can evaluate more opportunities, reduce time spent moving
          between disconnected research tools, and create polished
          deliverables faster.
    L160  ... gives teams greater confidence in their work and provides a
          differentiated capability they can bring into owner conversations.

"Multiple CRE teams" is a count with no names. The hero image is
assets/real-estate-case-study-placeholder.webp (the filename says
placeholder; case-studies.html:205-206). On case-studies.html:211-212 this
card is the only one of five with no case number and no date (the others
read "Case Study 04 / Jun 26, 2026"). The title uses "AI-Powered", a slop
adjective the rest of the site avoids. real-estate.html:197 and
:201-204 lean on this page as "Applied CRE work".
Severity: P0. Fix: either name the client (or "a Tampa Bay brokerage, name
withheld at their request") and state one observed fact per capability, or
recast the page honestly as the cre harness product page and stop calling
it a case study. Give it a number and a date on the index card.

**3. Embedded / forward-deployed engineering is still on the site.**
The test guards only how-we-altr-work.html. Elsewhere:

    workflow-audit.html:227   When the workflow spans teams and no single
      person sees all of it, the audit extends into forward deployed
      engineering: an engineer embedded in the operating context.
    custom-agents.html:275    Remote engagements run the same way, with the
      embedding phase done over video.
    impact-bebrief.html:170   We embed, build, and transfer ownership.
    index.html:95             knowsAbout: "forward deployed engineering"
    llms.txt:44               - [Forward deployed engineering]
      (https://altrwork.com/how-we-altr-work.html): the method behind our
      engagements ...

how-we-altr-work.html contains the word "forward" zero times
(`grep -c -i forward how-we-altr-work.html` -> 0), so llms.txt sends
LLM crawlers to a page that does not say what the link promises.
Severity: P0. Fix: cut the four sentences, drop the knowsAbout entry and
the llms.txt line, and extend
test_ai_strategy_page_sells_what_the_rest_of_the_site_sells to every page.

**4. Price, duration and sequence contradict each other across pages.**

- ai-consulting-tampa.html:245 `<h3><a href="workflow-audit.html">Workflow
  discovery</a> &middot; free</h3>`. The linked service page
  (workflow-audit.html) never says free; index.html:217-219 calls the same
  thing service "01 Strategy" with no price; llms.txt:13 says only "no
  separate charge for the intro call". Is the zero-to-one service free or
  not?
- custom-agents.html:189 "one fixed fee, quoted after enablement" and
  llms.txt:16 "Every engagement starts with enablement", versus
  index.html:213 "You can also start in the middle if you already know
  where the work is."
- ai-enablement-workshop.html:220, 235, 250, 265, 280, 295 publish "Half or
  full day", "Full day" (x3), "Half day" (x2); ai-consulting-tampa.html:254
  "A full day workshop"; index.html:16 meta "full-day team workshops".
  ai-enablement-workshop.html:316 on the same page: "We set the length with
  you on the call". README.md:68-71: "Session length is not published
  either. No hour counts anywhere."
Severity: P0 (a prospect will ask "so is discovery free?" on the first
call). Fix: one rule, applied everywhere: discovery call free / Strategy
quoted / durations set on the call, and delete the six day labels.

**5. The About page globe claims clients across the United States and
plots one dot.**
about.html:174:

    <canvas id="client-globe" ... aria-label="Globe showing client
    locations across the United States">Clients across the United States,
    based in Tampa, Florida.</canvas>

about.html:331-333, the marker list: `markers: [ { location: [27.9506,
-82.4572], size: 0.08 } ]`. That is Tampa. One marker. Screen readers and
any text-mode reader get "Clients across the United States"; sighted users
get a globe with a single dot on Florida. Also: about.html:292 `import
createGlobe from "https://esm.sh/cobe@0.6.4"` loads a third-party module at
runtime with no SRI and no fallback; about.html:335 `if (!pointerInteraction)
phi += 0.003;` spins it forever with no prefers-reduced-motion check.
SYSTEM.md: "Motion is one thing. The key press... nothing animates for
longer than 150ms." The CSS `animation: none !important` rule cannot reach a
JS render loop.
Severity: P0 for the claim, P1 for the dependency and motion. Fix: replace
with the Tampa plate or a static line naming real client cities.

### P1. Claims and copy that still read as generated or unsupported

**6. Unquantified "faster / reduces / improves" in the case studies.**
Attached to named clients, so lower severity than item 1, but the same
shape: a result word with no number or observation behind it.

    impact-fishin-prints.html:159  This cuts down the time and cost required
      to produce each piece and gives customers a smoother experience
    impact-fishin-prints.html:180  That consistency is what reduces
      production time and improves the customer experience.
    case-studies.html:271          ... faster, lowering manual production
      time and improving the buying experience.
    ecommerce.html:108             needed a faster and more consistent route
    impact-spark-labs-mcp.html:176 onboard new members faster ... New team
      members connect in minutes
    how-we-altr-work.html:132      After launch, some teams keep us on in an
      advisory retainer. Most do not need to.   (a frequency claim over
      four published clients)

Fix: replace each with what was observed ("the artist no longer transcribes
species details from the photo") or a number the client signed off on.

**7. Two Tampa pages are still one page written twice.**
8-word shingle comparison across all 42 non-legal pages
(scratchpad/verbiage.py): 332 shingles shared by 2+ pages; 196 of them are
the ai-consulting-tampa <-> workflow-automation-consultant-tampa pair. The
next pair is 43 (claude-cowork <-> claude-cre-cowork). Longest verbatim
spans between the two Tampa pages: 47 words (ai-consulting-tampa.html:302 /
workflow page :287, the "Automation shop" card), 38 words (:250 / :253,
the "Enablement" card), 29 (:289 / :278), 27 (:258 / :257), 24 (:351 / :354
closers), 17, 16, 15, 15, 14. Both pages still carry the "Who this is for"
section (:225-231 / :265-268) and the "Coverage" section (:266-269 /
:303-306) that DEBT-AUDIT item 1 said to delete; the hero lede on
ai-consulting-tampa.html:205 is still the 76-word sentence DEBT-AUDIT 1.5
#1 rewrote. Word counts fell (1,692 -> 1,234; 1,507 -> 1,161) but the
skeleton and the duplicated cards did not change.
Fix: delete Coverage on both (the hero names the cities); delete "Who this
is for" on the consulting page; rewrite the two shared cards so each page
argues its own query.

**8. Four sentences lost their punctuation when the dashes were removed.**
ai-consulting-tampa.html only; the sibling page kept a colon in the same
sentence (:287).

    :205  ...Wesley Chapel, and Clearwater and focus on operations heavy
          teams...                          (needs a comma before "and")
    :241  ...starts only after enablement or a build not as a vague monthly
          AI subscription.                   (needs a comma or colon)
    :302  ...mapped inputs, review, and ownership you get a faster version
          of a broken path.                  (needs a colon; :287 on the
          workflow page has one)
    :351  ...an automation, or nothing at all then quote the next step in
          writing...                         (needs a comma)

**9. One process, five vocabularies; one service, four names.**
Counted over visible main copy:

| Vocabulary | Where |
|---|---|
| Strategy / Enablement / Engineering, "Zero to one / One / One to ten" | index.html:217-231 and the nav only. "zero to one" or "one to ten": 4 occurrences, all on index.html. |
| Map / Prove / Deploy | index.html:245-255, how-we-altr-work.html:118-128 |
| Discovery / Enablement / Deployment | about.html:248-258 (as h2s), nonprofits.html:102-104, ecommerce.html:101-103, law-firms.html:103-105 |
| Workflow discovery / Enablement / Team workshop / Deployment | ai-consulting-tampa.html:245-258 |
| Discovery / Decision / Enablement / Deployment | workflow-automation-consultant-tampa.html:244-257 |

The first service is "Strategy" in the nav and on index, "AI strategy" in
the eyebrow of how-we-altr-work.html:97 (the word "strategy" appears 3
times on that page and never as a service name), "Workflow discovery" in
workflow-audit.html:155 (H1), ai-consulting-tampa.html:245 and llms.txt:41,
and "workflow audit" in workflow-audit.html's title and URL,
custom-agents.html:260, ai-enablement-workshop.html:361 and 404.html:88.
The third service is "Engineering" in the nav and index.html:230; its page
(custom-agents.html) H1 is "Custom Agents" and the word "engineering"
appears there once, inside "agentic coding systems ... engineering tasks".
Fix: three nouns, one triad, everywhere; retitle workflow-audit.html H1 to
match its title; put "Engineering" in the eyebrow of custom-agents.html.

**10. Link text promising things the target does not have.**

    about.html:262        <a href="how-we-altr-work.html">Read the full 4D
                          framework &rarr;</a>
    custom-agents.html:185  <a class="button secondary"
                          href="how-we-altr-work.html">View the framework</a>

`grep -c -i framework how-we-altr-work.html` -> 0. (DEBT-AUDIT item 4
flagged the 4D link; it was not fixed, and a second one exists.) about:262
also reintroduces a non-ASCII arrow; the site's remaining non-ASCII glyphs
outside JSON-LD: middle dot 24 (deliberate label separator), right arrow 2
(can-claude-connect-to-costar.html:99, claude-cre-connectors.html:81), left
arrow 1 (impact-real-estate-property-intelligence.html:83).

**11. Headings that name a category instead of making a claim.**
From the h2 sweep (short, verbless): how-we-altr-work.html:111 "Three
phases"; impact-real-estate-property-intelligence.html:142/146/157 "The
Challenge / The Solution / The Impact"; impact-spark-labs.html:167/175
"Expense Reports / Event Request"; impact-bebrief.html:154 "What we built";
about.html:248/253/258 "Discovery / Enablement / Deployment" as h2s
(heading level misuse as well: they are list items); 404.html:87/95
"Services / Blog"; "Related reading" on all 13 articles (acceptable).
case-studies.html:303 `<h2>Interested in<br />Learning More?</h2>` is
still the title-case agency heading; the SLOP pass rewrote only the
paragraph under it.

**12. Cards of identical length.**
Word counts per <article> (scratchpad/verbiage.py, CV = stdev/mean):
about.html beliefs n=6 cv=0.05 (29-34 words each); nonprofits n=13
cv=0.13 (20-31); ecommerce n=13 cv=0.13 (20-31); tutorials n=17 cv=0.14;
ai-consulting-tampa n=13 cv=0.16; index gap-grid 3 cards of ~20 words. Six
30-word beliefs in a row is the "sections the same length because the
generator was asked for sections" tell from SLOP-AUDIT section 3.
Fix: let one belief be a sentence and one be a paragraph.

**13. The CRE series still ends four times with the same pitch.**
"If your team is using Claude but it is not making a real impact, book a
call with us" verbatim on claude-cre-connectors.html:132,
claude-cre-cowork.html:112, claude-cre-scheduled-tasks.html:121. "That is
altr. We help CRE teams get real value from AI through hands-on enablement
and custom deployment work built around the business" (24 words) on
connectors:131 and scheduled-tasks. claude-cre-skills.html:97-100 still has
"But first, why should you listen to us? Who are we?" (DEBT-AUDIT 1.5 #9).
claude-cowork <-> claude-cre-cowork still share 43 shingles including a
26-word sentence (claude-cowork.html:162).

**14. Voice tics, recounted.**
"actually" 31 uses on 16 pages (was 35); "review point(s)" 25/13 and
"human review" 15/11 (same idea, two names); "Working rule" 11 pages and
"Working idea" 5 pages (same device, two names); "chatbot" 18/9, seven of
them on ai-consulting-tampa.html alone; "one (repeated) process/workflow"
43/20; a "Bring (us) one ..." closer on 23 of 42 pages; "by hand" 21/13;
"someone else's use case" 5/5.

**15. Five-second test failures.**
- how-we-altr-work.html:98 H1 "Find where AI improves your business" is
  the H1 DEBT-AUDIT 1.4 called "could head any AI vendor's site"; unchanged.
  This is the page the nav calls "Strategy"; the word appears once, in the
  eyebrow.
- case-studies.html:127 lede: "Case studies from partner work, plus
  practical field guides for teams putting AI to work in their industry."
  There are no field guides on the page.
- impact-real-estate-property-intelligence.html hero: no client, no date,
  no industry kicker beyond "Real Estate . Case Study". A CRE reader cannot
  tell whose story it is.
- mortr.html:195-196: two stacked buttons, both labelled "Book a call", one
  to start-a-conversation.html and one to Calendly (the CTA unification
  collapsed "Request access" into a duplicate). Visible in the 375px
  render.
- The blog is "Resources > Blog" in the nav, "Blog." as H1, "Tutorials" and
  "the Journal" (both -> tutorials.html) on 404.html:96, "Blog" in the
  footer. The Work menu says "Internal products" for one product.

### P1. Design-language consistency

**16. Ten hero implementations, still.**
First hero class per page: `page-hero article-hero` 13, `page-hero` 10,
none 5 (about.html and the four utility/legal pages), `page-hero
impact-page-hero` 5, `page-hero article-hero cre-article-hero` 4,
`page-hero page-hero-cut` 4, `lead-magnet-hero` 1, `strategy-hero` 1,
`hero-plate` 1, `page-hero learning-hero learning-hero-compact
learning-hero-simple` 1. SYSTEM.md promised "Three heroes, not ten".
about.html has no hero class at all and its own five wrapper classes.

**17. The `.hero-title-long` H1 is smaller than the H2s on phones.**
styles.css:476-477 `.page-hero h1.hero-title-long { font-size: clamp(17px,
5.4vw, 58px) }` -> 20px at 375px, while section H2s render at ~30px. Used
on ai-consulting-tampa.html, workflow-automation-consultant-tampa.html,
real-estate.html, mortr.html: the two local landing pages and the CRE hub.
Confirmed in the 375px renders of ai-consulting-tampa and real-estate: the
H1 is visibly the smallest heading on the page. Fix: clamp(28px, 7vw, 58px)
or drop the class.

**18. One-page classes.**
Classes used on exactly one page: tutorials.html 29, index.html 25,
case-studies.html 18, about.html 15, how-we-altr-work.html 12,
ai-in-real-estate-guide.html 11, ai-enablement-workshop.html 7. Section
wrappers: `article-block` 91, bare `section` 89, `cta-section` 28, `band`
6, `closer` 4, `strategy-section` 2, four `about-*` one-offs,
`product-page-section` 1 (mortr). The redesign's `.closer` component is on
4 pages; 28 pages still use `cta-section`.

**19. House rules the !important block does not reach.**
- styles.css:707-712 `.intake-note` two-layer copper gradient, visible in
  the start-a-conversation.html 375px render as a pink-to-white wash on
  both panels. Gradient declarations remaining: styles.css 20, redesign.css
  13 (some are the intended scrims).
- redesign.css:~530 form fields `border-radius: 8px` versus SYSTEM.md "One
  radius, and it belongs to the keycap. --radius: 2px".
- The About globe (item 5) is the only thing on the site that moves for
  more than 150ms.

**20. Footer and nav variants.**
Nav: 15 hashes, all explained by aria-current placement; fine. Footer: 7
variants. index.html and how-we-altr-work.html tagline "Software and AI
strategy for teams who want to do real work"; 43 pages "AI services for
teams who want to do real work"; the three legal pages drop the "Tampa, FL"
link; the rest is whitespace. Footer "Services" -> index.html#who-we-serve
while the nav "Services" is a dropdown.

**21. The booking funnel still has three paths.**
Nav "Book a call" -> calendly.com/altrwork/30min directly. Body "Book a
call" -> start-a-conversation.html, intercepted by intake-modal.js on 36
pages. intake-modal.js is absent on how-we-altr-work.html,
impact-real-estate-property-intelligence.html and
ai-in-real-estate-guide.html (all three have Book a call buttons, two are
CRE-facing), so the same button behaves differently there.

### P2. Technical debt

**22. redesign.css:635-644 shrinks the home hero to 460px on tablets.**
Inside `@media (max-width: 980px)`: `.hero-plate { max-width: 460px; }`.
This was written for the old plate image; `.hero-plate` is now the whole
home hero section. Confirmed at 768px: the hero is a 460px column against
the left gutter with ~300px of bare paper to its right. Nothing at 900px
resets it. Fix: delete lines 642-644 (and 646-649, `.process-plate` is
dead).

**23. Dead CSS.**
styles.css: 276 classes in selectors, 45 match no markup or JS: case-grid,
case-stat, featured-work-card, framework-step, framework-strip, hero,
hero-actions, hero-copy, home-about, home-about-hero, impact-card-logo-wrap,
is-running, learning-brief, learning-feature-card, learning-feature-grid,
learning-lane-header, learning-resource-list, learning-tabs, modern-gap,
note, offer, page-hero-logo, price-meta-grid, proof-logos, pull-quote,
resource-item, service-arm, service-arm-grid, service-badge,
strategy-cadence, strategy-demo, strategy-lens-grid, strategy-motion-ready,
strategy-output-copy, strategy-output-number, strategy-output-row,
strategy-outputs, strategy-roadmap-demo, strategy-scan-demo,
strategy-workflow-tags, trust-panel, work-list-action, work-list-item.
redesign.css: 141 classes, 23 dead: closer-note, connector,
featured-work-card, hero-actions, home-section, learning-brief,
learning-feature-card, learning-index-section, lede-hero, ledger-row,
motion-ready, plate-caption, process-plate, reveal-on-scroll, service-arm,
service-arm-grid, service-badge, strategy-outputs, trust-panel,
tutorial-tag-automation, wash. (SYSTEM.md still documents "Ledger" and
"wash" as live components.) Duplicate selectors within a file: styles.css
70 (.nav x5, .nav-links x6, .nav-links .nav-cta x4, :root x2, `h1, h2, h3,
h4` x3), redesign.css 21 (.closer x3, .hero-plate x3,
.hero-plate-bg::after x4). Selectors present in both files: 42, of which
9 are fully re-declared in redesign.css and deletable from styles.css:
.about-beliefs h2, .about-page-simple, .band, .button.primary,
.button:active, .closer, .closer h2, .home-hero-actions,
.home-industry-grid. `!important` count: styles.css 6, redesign.css 17.

**24. 27 deployed files nothing references (10 MB).**
altr-brand-assets/assets/hero-computer-logo-background.png 1,878 KB;
assets/bebrief logo-2.png 1,198; assets/bebrief logo.png 1,192;
assets/plates/cut-barrels.webp 833; assets/operations-mcp-sbs.pdf 615;
assets/plates/cut-carriage.webp 587; assets/operations-mcp.pdf 542;
assets/plates/wash-quarry.webp 505; assets/plates/cut-lathe.webp 485;
assets/plates/cut-frames.webp 414; assets/plates/cut-machine.webp 382;
assets/fishin-prints logo-2.png 336; assets/fishin-prints logo.png 330;
assets/plates/wash-facade.webp 304; altr-brand-assets/assets/logo-w-
background.png 177; uploads/robot.png 173; assets/fonts/SpaceGrotesk-
VariableFont_wght.ttf 130 and .woff2 47; assets/altr_key_logo_cream_taupe_
transparent.png 102; assets/altr-4d-framework.png 99; assets/nonprofit-
member-onboarding.png 91; uploads/fde.png 88; assets/altr-discernment-
loop.png 73; assets/altr_social_avatar_ivory.png 47; altr-brand-assets/
assets/logo-banner.png 45; assets/spark-logo-transparent.png 27;
assets/particles.min.js 22. Two of these are PDFs at public URLs
(operations-mcp*.pdf) with no page linking them.

**25. README.md describes the previous site.**
README.md:14 resources.html; :15 "the 4D framework"; :18-19
forward-deployed-engineering.html, events.html; :21 pricing.html; :29
nav-dropdown.js; :30 impact-ui.js, tutorials-ui.js, site-motion.js; :66-70
the FDE page and its .page-note. None of these exist.

**26. Head drift.**
styles.css cache-bust: `?v=20260906b` on 41 pages, `?v=20260907a` on
mortr.html, none on privacy/terms/website-terms. The gtag snippet is pasted
on all 45 pages. about.html is the only page that loads a third-party
module (esm.sh).

### P2. SEO (footprint is intact; these are hygiene)

**27. Nothing is broken.** All 40 sitemap URLs resolve and self-canonicalize
(tests pass, 15/15). No duplicate titles or descriptions. Every JSON-LD
block parses; no schema URL points at a missing file. Zero broken internal
hrefs or asset paths. Every page except 404 and the thank-you page is
reachable within 2 clicks of index.html. _redirects covers every merged or
retired URL: events, forward-deployed-engineering, resources,
internal-products, pricing, what-we-do, frameworks, impact-studies, plus
index.html -> /.

**28. Still open from DEBT-AUDIT 13:** descriptions over 160 chars:
mortr.html 261 (title 67), law-firms.html 174,
can-claude-connect-to-costar.html 173, claude-skills-vs-mcp.html 167.

**29. Title-level cannibalization on "AI consulting".** It appears in five
titles: index ("AI Strategy and Consulting in Tampa"), ai-consulting-tampa
(the page that should own it), nonprofits ("AI for Nonprofits | AI
Consulting | altr"), law-firms ("AI for Law Firms | AI Consulting | altr"),
ecommerce ("AI Consulting for Ecommerce Teams"). Fix: "AI for Nonprofits |
altr" etc.; the industry pages rank on the industry, not on "consulting".
workflow-audit.html still has title "Workflow Audit for AI Automation" over
H1 "Workflow discovery" (DEBT-AUDIT 3.2, open).

**30. Thin body-link support for the commercial pages.** Body inbound
(nav and footer excluded): workflow-automation-consultant-tampa.html 1,
mortr.html 1, law-firms.html 1, about.html 0, index.html 2. The workflow
page targets a high-intent local query and has one body link (from
ai-consulting-tampa.html).

**31. areaServed disagrees with itself.** index LocalBusiness: Tampa, Tampa
Bay, St. Petersburg, Clearwater, Orlando, Lakeland. ai-consulting-tampa:
adds Wesley Chapel. workflow page: Wesley Chapel but no Orlando or Lakeland.
Service schemas: three cities (enablement, custom-agents, workflow-audit)
or "US" (industry pages). Visible copy: Tampa pages say "Wesley Chapel";
start-a-conversation.html:151 says "Orlando, and Lakeland". Pick one list.

**32. llms.txt content drift.** llms.txt:41 "Workflow discovery" and :44
"Forward deployed engineering" as services, :45 "Events" -> ai-workshop; the
Engagements paragraph (:11-30) is 330 words describing a retainer with
"up to ten hours a month", which no HTML page mentions. It is the one file
the client's AI-search visitors read verbatim.

### P2. Mobile (rendered at a true 375px)

Thirteen pages rendered at 375px show no horizontal overflow and the
hamburger nav, stacked buttons and single-column grids all hold. Every
multi-column grid in both stylesheets has a collapse rule (checked by
script; the two without one, `.engagement-grid-2up` and
`.home-industry-grid`, are collapsed by redesign.css:1285 with !important).
What does break:

- Item 22: home hero at 460px on tablets (768px render).
- Item 17: 20px H1 under 30px H2s on the two Tampa pages, real-estate and
  mortr (375px render).
- Item 15: mortr.html two identical "Book a call" buttons stacked (375px
  render).
- ai-workshop.html:186-195 Luma iframe has `width="600"` in markup; CSS
  `.workshop-calendar iframe { width: 100% }` (styles.css:2218-2222) saves
  it, but the attribute should go.
- styles.css:2917-2935 (inside the 680px block) `.page-lede, .page-note,
  .section-header p, .about-copy p, .founder-card p { max-width: 315px;
  margin: auto; overflow-wrap: anywhere }`: `overflow-wrap: anywhere` will
  break words mid-word wherever a lede has a long token; not observed in
  the 13 renders but it is a landmine.

---------------------------------------------------------------------------

## SUSPECTED (could not verify from the repo)

- ai-workshop.html:154 "altr is an approved Claude SMB trainer." No link,
  badge or program name. If Anthropic has a partner listing, link it; if
  "approved" means "we applied and were accepted to run sessions", say that.
  As written it reads as a certification.
- claude-cre-skills.html:91 "66% of CRE professionals use AI weekly or
  daily, but only 5% trust it enough to inform real decisions" is cited to
  First American Data & Analytics and DealGround. The numbers appear three
  times (:91, :100, :151). Confirm the source pages say exactly this; the
  5% figure in particular is load-bearing for the whole series.
- claude-cre-connectors.html:91 "Claude supports hundreds of packaged
  connectors." Plausible from Anthropic's directory; uncited.
- ai-in-real-estate-guide.html:103 "Free 18-page field guide": the PDF has
  18 /Type /Page objects (checked). Fine. Its "30-day pilot plan" (:143,
  llms.txt:60) is a timeframe the site otherwise avoids; make sure the PDF
  frames it as the reader's plan, not altr's delivery promise.
- Contrast of the 11px uppercase mono kickers on paper was not measured
  (DEBT-AUDIT flagged it; still unmeasured).
- Whether cre harness is a shipped product with users or an internal tool
  used on one engagement. The copy ("multiple CRE teams") implies the
  former; nothing on the site substantiates it.

---------------------------------------------------------------------------

## Still open from prior audits (not re-argued here)

DEBT-AUDIT 1: Coverage and Who-this-is-for sections on both Tampa pages.
DEBT-AUDIT 4: "Read the full 4D framework" link. DEBT-AUDIT 10: three
booking paths. DEBT-AUDIT 12: the 01/02/03 block on the three industry
pages. DEBT-AUDIT 13: four long meta descriptions, mortr title length.
DEBT-AUDIT 1.4: how-we-altr-work H1; case-studies filter UI for five items
(now driven by filter-grid.js, still 4 checkboxes + search + view toggle
for 5 cards). DEBT-AUDIT 1.5 #1, #9, #11: the 76-word Tampa lede, the
"Who are we?" digression, the real-estate lede repeated verbatim as FAQ
answer 1 (real-estate.html:156 vs :245, still identical for the first 27
words). DEBT-AUDIT 2.2: mortr images without width/height. SLOP-AUDIT 3.1:
this document.

---------------------------------------------------------------------------

## Verdict

Not ready for a CRE prospect. The structure, nav, SEO plumbing and mobile
layout are in good shape and would pass. What fails is exactly what the
client said they cared about: the homepage's outcome band promises revenue,
hours and unit cost with nothing behind it; the single CRE case study is
anonymous, undated, illustrated with a file called placeholder, and says
"multiple CRE teams"; embedded engineering is still on four pages after
being removed from one; and a prospect reading two pages will find
discovery both free and unpriced, sessions both half-day and unfixed, and
enablement both mandatory-first and skippable. Fix items 1-5 and 8 (one
afternoon of edits, no design work) and the site is fit to send. Items
6-21 are the difference between fit-to-send and convincing.

Scripts used (scratchpad, not committed): extract.py (visible text with
line numbers, word counts), seo.py (head, JSON-LD, links, click depth,
sitemap, includes), verbiage.py (8-word shingles, section/article CV, h2
sweep), css_consistency.py (orphan classes, hero combos, wrappers, nav and
footer hashes, dead CSS, duplicate selectors, cross-file overrides,
unreferenced assets, JS usage). Renders: headless Chrome, pages served
locally, each page inside a 375px iframe and at a 768px window.
