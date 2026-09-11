# altrwork.com debt audit: verbiage and technical

Scope: all 50 HTML pages, styles.css (6,063 lines), redesign.css (1,606 lines),
9 JS files, _redirects, sitemap.xml, robots.txt, llms.txt, assets/. Branch
design/tenex-language. Read-only audit; every count below was produced by
scripts run against the files (word counts are main-column text only, nav and
footer excluded; reading time is words / 230).

Site total: 30,801 words of main-column copy across 50 pages. 13 pages are
over 700 words. The two Tampa landing pages alone carry 3,199 words (10.4% of
the site) and say the same thing twice.

The short version: the copy is not bloated sentence by sentence. It is bloated
page by page. The same five blocks (the gap, who this is for, the three-step
process, the Tampa Bay coverage paragraph, the FAQ) are rebuilt on 12 pages
with new wording each time, so a visitor who reads two pages reads the pitch
twice. The technical side has the same shape: two CSS files that partly
overlap, a nav rebuilt by JavaScript on every load, and about 1,400 lines of
CSS plus two JS files that style or animate nothing.

---------------------------------------------------------------------------

## 0. Prioritized action list

Ranked by value against effort. Each item: do X to files Y, because Z,
SEO impact W. "Words" are main-column words removed.

1. Cut ai-consulting-tampa.html from 1,692 words to about 900 and
   workflow-automation-consultant-tampa.html from 1,507 to about 700.
   Remove from each: the three-industry "Who this is for" block (duplicated
   between them and against index.html), the "Coverage" section (fold its
   one useful sentence into the hero), two of the six FAQs (the "Location"
   and "Difference" answers repeat the hero), and the compare table's fourth
   column on the workflow page. Because: 8 sentences are verbatim identical
   across the two pages, the section skeletons are identical, and the pages
   are the top two by reading burden (7.4 and 6.6 minutes).
   SEO impact: positive. Both URLs, titles, H1s, FAQ schema and LocalBusiness
   blocks stay. Removing the repeated "AI consultant in Tampa" anchor text
   from the workflow page (used 3 times there) reduces the two pages
   competing for the same query. Do not merge these two pages: they hold
   distinct high-intent local queries.

2. Delete events.html and 301 it to ai-workshop.html. Move the one
   paragraph events.html has that ai-workshop.html lacks ("We also speak at
   Tampa Bay community events and meetups... tell us the audience and the
   workflow") into ai-workshop.html as a short section. Because: the
   rendered nav (nav-dropdown.js) already sends "Events" to
   ai-workshop.html, not events.html; events.html has 2 inbound links, lists
   the same September 22 session, and its "Three formats" block restates the
   enablement-workshop page. Update: index.html nav link, ai-consulting-tampa
   .html link, sitemap.xml, llms.txt, _redirects.
   SEO impact: neutral to positive. events.html title "AI Workshops and Demos
   in Tampa" competes with ai-workshop.html for "AI workshop Tampa". One page
   with Event/EventSeries schema is stronger than two.

3. Delete forward-deployed-engineering.html and 301 it to
   how-we-altr-work.html, after rewriting how-we-altr-work.html into the
   single "how we work" page (item 4). Because: FDE has zero inbound links,
   its nav still points at what-we-do.html (retired) and a different Calendly
   (calendly.com/jarredrobidoux), and its own first paragraph says it is "not
   something you buy on its own." Keep an H2 "Forward deployed engineering"
   on the target page so the phrase (in index.html knowsAbout schema) stays
   indexed. SEO impact: neutral. 0 inbound links means no equity to lose;
   the 301 preserves the URL.

4. Reconcile how-we-altr-work.html with the rest of the site. It currently
   sells "a 7-day audit", a "30-day Roadmap", "each build is priced up front",
   and "most clients keep us on as their embedded engineering team". Every
   other page (and README.md, and FDE) says: no published hour or day counts,
   discovery is free, enablement first, retainer is advisory only, no
   embedded headcount. Pick one. Also: h1 is two <span>s with no space and
   reads "Find where AIimproves your business" in the accessibility tree;
   "scattered with scattered pilots" and "opportunites" are typos; about.html
   links here as "Read the full 4D framework" and the page contains no 4D.
   SEO impact: neutral. Keep URL and title.

5. Delete site-motion.js and its 33 <script> tags, and home-typewriter.js
   (loaded by no page). Because: redesign.css lines 1448-1455 set
   `opacity:1 !important; transform:none !important; transition:none
   !important` on every element site-motion.js touches, so the file runs an
   IntersectionObserver on 33 pages to produce no visible change.
   SEO impact: none (slightly less JS per page).

6. Delete the six dead blocks in styles.css (about 1,157 lines): pricing page
   3720-3990, offers/notes/qa 4044-4300, old home hero and chat typewriter
   4301-4620, price-strip 4716-4862, learning-lanes 1042-1160,
   strategy-lens-grid 5728-5770 and its media-query echoes. 98 class names
   in styles.css match no markup in any HTML or JS file (list in 2.1).
   Then delete the 26 retired components in redesign.css (register, ledger,
   plate, ticker, connector, wash, hero-split, process-split; 51 selectors).
   SEO impact: none.

7. Move the nav into static HTML. nav-dropdown.js builds the Services, Work
   and Resources dropdowns client-side, so the HTML nav (14 variants across
   50 files) and the rendered nav differ, and crawlers that do not execute JS
   see links to events.html and index.html#who-we-serve that users never
   see. Write one nav block, paste it into all 50 files, keep only the
   mobile toggle in JS. SEO impact: positive (consistent internal links,
   real anchors to real-estate.html, nonprofits.html, ecommerce.html,
   mortr.html on every page).

8. Delete resources.html and 301 to tutorials.html. It lists 11 of the same
   articles, already canonicalizes to tutorials.html, and has inbound links
   only from 404.html and tutorials.html. Delete internal-products.html
   (80 words, one card) and 301 to mortr.html; point the Work dropdown at
   mortr.html directly. SEO impact: none for resources (already
   canonicalized away, not in sitemap); neutral for internal-products
   (title "Internal Products | altr Tampa" targets nothing).

9. Fix the broken and stale links: law-firms.html links
   uploads/2024/01/FL-Bar-Ethics-Op-24-1.pdf which does not exist (404);
   forward-deployed-engineering.html links what-we-do.html 4 times; footer
   "Terms" on 49 pages goes to terms.html (the client Master Services
   Agreement) while website-terms.html (the actual site terms, 0 inbound
   links) is unreachable. SEO impact: positive (no 404s, no orphan).

10. Standardize the CTA. There are 39 distinct CTA labels and 3 booking
    paths (nav -> Calendly direct; body -> start-a-conversation.html
    intercepted by intake-modal.js; the page itself with JS off). Pick
    "Book a call" (already 18 uses) for every primary button and one path.
    SEO impact: none.

11. Compress images. The four CRE guide headers are 1.6 MB PNGs each with
    .webp siblings that are only used on tutorials.html thumbnails; the
    ai-workshop hero is a 2.5 MB PNG; 04_bull_trout_pair.png is 1.3 MB;
    mortr.html's two images have no width/height. 26 <img> tags on the four
    CRE pages have no loading="lazy". Delete the 32 unreferenced files
    (9.3 MB, list in 2.4). SEO impact: positive (Core Web Vitals).

12. Trim the three industry pages' shared skeleton. nonprofits.html,
    ecommerce.html and law-firms.html each carry a "How it works" 01/02/03
    block and a "Where should we start?" FAQ that are the same content with
    the nouns changed. Replace the block with one sentence linking to
    how-we-altr-work.html; keep only the two industry-specific FAQs.
    Saves about 150 words per page. SEO impact: neutral; the industry
    keywords live in the H1, the four use-case items, and the case study,
    all of which stay.

13. Fix metadata length and consistency: mortr.html description is 261
    characters (truncates at about 160), law-firms 174, costar 173,
    skills-vs-mcp 167; index.html has three different one-line company
    descriptions (meta, og, twitter); og:image is missing on 6 pages;
    geo.region only on index.html. Add `/pricing.html /#who-we-serve 301!`
    to _redirects and delete the meta-refresh stub. SEO impact: positive.

14. Decide law-firms.html. It is noindex, not in the sitemap, not in the nav
    dropdown, has 0 inbound links, and is the only industry page with a
    real differentiator (the Florida Bar Opinion 24-1 section). Either
    publish it (remove noindex, add to sitemap and dropdown, fix the PDF
    link) or delete it. As it stands it costs maintenance and earns nothing.
    SEO impact: publishing is upside only; today it has zero footprint.

---------------------------------------------------------------------------

## Part 1: Verbiage debt

### 1.1 Reading burden

Full per-page table in Appendix A. The 13 pages over 700 words, worst first:

| File | Words | Sections | CTAs | Minutes | What could go |
|---|---:|---:|---:|---:|---|
| terms.html | 3,721 | 0 | 0 | 16.2 | Nothing. It is the MSA. Leave it, but stop linking it from every footer as "Terms" (see item 9). |
| ai-consulting-tampa.html | 1,692 | 9 | 3 | 7.4 | "Who this is for" trio (280 words, repeats index and workflow page); "Coverage" section (110); FAQs 2, 3, 4 (240); the "Proof" grid duplicates case-studies.html (130). Target ~900. |
| workflow-automation-consultant-tampa.html | 1,507 | 8 | 3 | 6.6 | Same skeleton as above. "Who this is for" trio (270), "Coverage" (100), FAQs 3, 4 (170), "AI consultant" compare column (60). Target ~700. |
| real-estate.html | 1,255 | 8 | 3 | 5.5 | "How altr works" 01/02/03 block (120); FAQ "How does altr start an AI project" (60, repeats it); FAQ "How can CRE teams use AI" (60, verbatim repeat of the hero lede); one of the two operating-model decompositions (see 1.2 cluster F). Target ~900. |
| ai-enablement-workshop.html | 1,149 | 7 | 4 | 5.0 | Three separate "this is paid, not the free workshop" disclaimers (70); six topic cards each with 3 bullets (cut bullets, keep title + one line: ~250); "What people leave with" four-card grid restates "The premise" (150). Target ~650. |
| mortr.html | 1,091 | 9 | 5 | 4.7 | The dated-records disclaimer appears 21 times ("dated"), "Agency debt may be absent" 7 times, "not a live" 4 times. One in the hero, one in the FAQ. "Chat research" section (120) restates "Four jobs". Target ~700. Keep every FAQ question: they carry the product keywords. |
| privacy.html | 963 | 0 | 0 | 4.2 | Leave. Legal, well written. |
| website-terms.html | 868 | 0 | 0 | 3.8 | Leave. Link it from the footer instead of the MSA. |
| claude-cre-connectors.html | 857 | 11 | 1 | 3.7 | "Connectors turn Claude from a chatbot into a working member of your team" said twice (lede and body); "Want this built into your workflow?" pitch block (110) duplicates the closer beneath it. Target ~700. |
| claude-cre-skills.html | 852 | 10 | 1 | 3.7 | "But first, why should you listen to us? Who are we?" digression (90 words on altr's thesis); the 66%/5% statistic used twice; "Keep reading." Target ~700. |
| law-firms.html | 756 | 6 | 3 | 3.3 | "How it works" block (110), "Where should we start?" FAQ (50). Keep the Florida Bar section; it is the only industry page with real differentiation. |
| claude-cre-scheduled-tasks.html | 737 | 9 | 1 | 3.2 | CoStar stock-chart aside (60); "Want this built" pitch block (90) duplicating the closer. |
| claude-skills-vs-mcp.html | 703 | 8 | 1 | 3.1 | Fine. One CTA, clear structure. Leave. |

Pages that are too short to do their job: internal-products.html (80 words,
one card), pricing.html (21 words, meta-refresh stub), start-a-conversation
.html (54 words; acceptable as a form page).

CTA density: index.html has 4 CTAs in main plus the nav CTA; ai-enablement-
workshop 4; mortr 5. Everything else is 1-3.

### 1.2 Redundancy map

Sentence-level check: 17 sentences of 9+ words appear verbatim on two or more
pages. That is low, and it is misleading. The copy is paraphrased, not
pasted, so the duplication is structural: same sections, same argument, new
wording. The table shows the clusters.

| Cluster | Files | Genuinely different | Duplicated |
|---|---|---|---|
| A. Tampa local landing pages | ai-consulting-tampa.html, workflow-automation-consultant-tampa.html | Target query (AI consultant vs workflow automation consultant); the "automation trap" framing on the workflow page. | Identical 9-section skeleton: gap, who-for (same 3 industries, same three "One concrete example" sentences), how-we-work steps, coverage, compare table, 6 FAQs, closer. Verbatim: "Connecting to your tools is usually an MCP server or connector, not a migration." / "People leave with prompts and workflows they built during the session rather than notes about someone else's use case." / "Fees stay unpublished until we can quote the scope in writing before you commit." / "Your team keeps the prompts, documentation, and operating notes." / "We will recommend an automation shop when that is honestly the better next step." / "Remote when the work is already clear on video." / "Use this to set the right expectation before the first call." / "Often jumps straight to zaps, bots, and integrations." |
| B. The three-step process | index.html, about.html, real-estate.html, nonprofits.html, ecommerce.html, law-firms.html, ai-consulting-tampa.html, workflow-automation-consultant-tampa.html, how-we-altr-work.html, forward-deployed-engineering.html, three-phases-ai-deployment.html, custom-agents.html (FAQ) | Nothing. | The same sequence under six different names: "Map / Prove it with the team / Deploy what earns a role" (index); "Discovery / Enablement / Deployment" (about, real-estate, nonprofits, ecommerce, law-firms); "Workflow discovery / Enablement / Team workshop / Deployment" (ai-consulting-tampa); "Discovery / Decision / Enablement / Deployment" (workflow page); "Map / Build / Adoption" (how-we-altr-work); "Embed and learn / Build agent infrastructure / Accelerate production / Transfer and compound" (FDE); "audit / pilot / rollout" (three-phases article). Twelve pages, six vocabularies, one process. |
| C. Workshops and events | ai-enablement-workshop.html, ai-workshop.html, events.html | Paid vs free; the six topic cards (enablement); the Luma registration and venue (ai-workshop). | events.html "Upcoming: Claude AI for Small Business, September 22" repeats ai-workshop.html's hero; events.html "Enablement session" format card repeats the enablement page's lede almost word for word ("People leave with prompts and workflows they built during the session, not notes about someone else's example"); "Public Claude Small Business Workshop sessions are separate and free." verbatim on enablement and events. |
| D. Method and positioning | how-we-altr-work.html, about.html, forward-deployed-engineering.html, index.html "Why teams call us" band | how-we-altr-work has the opportunity-map and roadmap demos. | All four explain "we embed, we build only what earns a role, the team owns it after." FDE: "Everything we build stays with you." About: "We leave behind operating notes, prompts, workflows." Custom-agents FAQ: "Every engagement ends with the prompts, system instructions, documentation, and operating notes handed over." Tampa pages: "Your team keeps the prompts, documentation, and operating notes." Same promise, five phrasings. |
| E. Industry pages | nonprofits.html, ecommerce.html, law-firms.html (real-estate.html is a different, larger shape) | The four "Where AI fits" items and the one case study on each. | Section order (Where AI fits / How it works / Related work / Common questions / closer); the 01/02/03 block; FAQ "Where should we start?" on all three with the same answer shape ("Choose a recurring process with clear inputs and a clear output: ..."); FAQ "Will this replace staff?" (nonprofits) = "Does this make legal judgments?" (law) = "Can AI publish automatically?" (ecommerce) in function; closer "Bring us one process ... We will help you determine whether it needs training, a custom build, or a simpler fix." vs "training, a build, or nothing at all." |
| F. CRE operating model | real-estate.html, ai-in-real-estate-guide.html, the four claude-cre-*.html pages | Each is a different depth. | Three incompatible decompositions of one model within two clicks of each other: real-estate.html "A useful AI workflow has five parts" (Sources, Playbook, Workspace, Deliverable, Review); the guide "The four-layer operating model" (playbooks, connections, workspace access, routines); the series' four parts (Skills, Connectors, Cowork, Scheduled Tasks). |
| G. Cowork | claude-cowork.html, claude-cre-cowork.html | claude-cowork is the generic explainer with a "how a team uses it" pattern; claude-cre-cowork is the screenshot walkthrough. | Verbatim: "If the workflow is upload, prompt, download, open, revise, and upload again, the team is still carrying the work between systems." / "It is a model that can continue working on the same approved files your team will actually use." / the "Working idea" pull quote. Both pages open with the same browser-vs-desktop distinction. |
| H. CRE series pitch blocks | claude-cre-skills.html, claude-cre-connectors.html, claude-cre-cowork.html, claude-cre-scheduled-tasks.html | The tutorial content. | Each ends with a "Want this built into your workflow?" block ("You just watched us ... for free, in minutes. Now imagine ... That is altr. ... book a call with us.") followed by a second closer CTA block. Verbatim on 3-4 pages: "If your team is using Claude but it is not making a real impact, book a call with us." / "We help CRE teams get real value from AI through hands-on enablement and custom deployment work built around the business." / "Continue with the commercial real estate AI workflow hub, or read the original version in the altr'd newsletter on LinkedIn." |
| I. Blog indexes | tutorials.html, resources.html | tutorials adds the CRE field-guide strip and filters. | resources.html lists 11 articles all present on tutorials.html with reworded blurbs; canonical already points to tutorials.html. |
| J. Workflow audit | workflow-audit.html (service), ai-workflow-audit-small-business.html (article), Tampa pages' "Workflow discovery" step | Service vs how-to intent. Both earn their place. | The service page H1 says "Workflow discovery"; its URL, the article, the blog card, and 12 other mentions say "workflow audit". One term. |
| K. Coverage paragraph | ai-consulting-tampa.html, workflow-automation-consultant-tampa.html, custom-agents.html (FAQ), ai-enablement-workshop.html (FAQ schema), start-a-conversation.html, index.html | Nothing. | "We are based in Tampa, Florida and work on-site with teams across Tampa Bay, St. Petersburg, and Clearwater. Remote engagements run the same way" in 5 wordings. "St. Petersburg" appears 18 times on 9 pages. |

### 1.3 Merge plan

Decisive list. "Keep" items are named so nobody re-litigates them.

| Action | From | To (surviving URL) | Keep from the removed page | 301 |
|---|---|---|---|---|
| Merge | events.html | ai-workshop.html | The community-demo / "bring us to your meetup" paragraph, as one section. The "Workflow review" format mention can go; it is the free consultation. | /events.html -> /ai-workshop.html |
| Merge | forward-deployed-engineering.html | how-we-altr-work.html | The .page-note ("This is a method, not a headcount contract...") and the four-line "Engineers in the room / Agent infrastructure / Production systems" list, as an H2 "Forward deployed engineering" section. Drop "Accelerate production" copy. | /forward-deployed-engineering.html -> /how-we-altr-work.html |
| Delete | resources.html | tutorials.html | Nothing; every article is already on tutorials.html. | /resources.html -> /tutorials.html |
| Delete | internal-products.html | mortr.html | Nothing. Point the Work dropdown at mortr.html with the label "mortr". | /internal-products.html -> /mortr.html |
| Delete | pricing.html | / (fragment #who-we-serve) | Nothing. | /pricing.html -> /#who-we-serve |
| Keep, cut 45% | ai-consulting-tampa.html | (same) | - | - |
| Keep, cut 50% | workflow-automation-consultant-tampa.html | (same) | - | - |
| Keep, dedupe | claude-cowork.html + claude-cre-cowork.html | both | Cut the browser-vs-desktop explainer paragraphs from claude-cre-cowork.html and link to claude-cowork.html for them; keep the screenshots. Do not merge: the CRE page is part of a numbered four-part series. | - |
| Keep, rename H1 | workflow-audit.html | (same) | H1 "Workflow audit" to match URL and the other 12 mentions. | - |
| Keep, decide | law-firms.html | (same) | Publish or delete (item 14). | - |
| Keep | all 13 articles, 5 case studies, 4 CRE guides, guide + thank-you, mortr, about, start-a-conversation, 404, 3 legal pages | - | - | - |

Result: 50 pages -> 45. Roughly 4,900 words removed from the pages that
remain (items 1, 4, 12 and the trims in 1.1), about 16% of the site.

### 1.4 Per-page clarity

Format: the five-second read the page owes the visitor; does it deliver;
smallest edit.

index.html. Owes: "altr maps a workflow your operations team repeats, trains
the people, and builds software only if the work needs it. Tampa." Delivers:
yes, the H1 and lede do it. Friction: the page describes the company three
ways in one <head> (title "AI Strategy and Consulting", meta "Enablement,
custom deployment, and full-day team workshops", kicker "Software and AI
strategy"), and the "Why teams call us" band is a fourth restatement.
Smallest edit: one company line, used in title, meta, og, twitter and
kicker; cut the "Why teams call us" band.

ai-consulting-tampa.html. Owes: "AI consultant in Tampa for ops teams; we
start with one workflow." Delivers: the H1 does. Then 1,600 more words say it
eight more times. Smallest edit: delete the "Who this is for" and "Coverage"
sections; the hero already names the three industries and the cities.

workflow-automation-consultant-tampa.html. Owes: "We map the process before
we automate it." Delivers: yes ("who will not skip discovery" is the best H1
on the site). Smallest edit: same two deletions as above; cut the fourth
compare column, which argues with the sibling page.

real-estate.html. Owes: "AI for CRE teams: research, underwriting, file work,
market monitoring, with the broker still owning the assumptions. Here is the
field guide." Delivers: yes, but the lede is one 49-word list sentence that
is repeated verbatim as the first FAQ answer. Smallest edit: cut the lede to
20 words; delete the "How altr works" block and the FAQ that repeats it.

ai-enablement-workshop.html. Owes: "Paid, hands-on AI training on your own
work. Two formats." Delivers: partly. H1 "AI enablement workshop" is a label,
and the lede spends its second half saying what the page is not. Smallest
edit: one disclaimer line under the price chip, delete the other two; topic
cards to title plus one sentence.

how-we-altr-work.html. Owes: "How an engagement runs, start to finish."
Delivers: no. It sells a different product (7-day audit, 30-day roadmap,
embedded engineering team) from the one on the other 49 pages, and the H1
"Find where AI improves your business" could head any AI vendor's site.
Smallest edit: H1 "How an engagement runs"; steps renamed Discovery /
Enablement / Deployment; day counts removed or adopted sitewide.

about.html. Owes: "Two founders in Tampa, what they believe." Delivers: yes.
Friction: "Our mission" is followed only by the Romans 12:1 quotation with no
framing sentence, so a visitor expecting a mission statement gets a verse
with no bridge. That is the founders' call; if it stays, one sentence before
it would make the intent legible. "Read the full 4D framework" links to a
page without a 4D framework. Smallest edit: fix the link text; add or remove
the bridge sentence.

case-studies.html. Owes: "Here is the work." Delivers: yes. Friction: a
search box, four category checkboxes, a view toggle and a clear button for
five items; a closer in a different voice from the rest of the site
("Interested in Learning More? Let's explore how AI can support your goals
and unlock new opportunities."). Smallest edit: remove the filter UI and
impact-ui.js; rewrite the closer in the house voice ("Bring us one
workflow.").

custom-agents.html. Owes: "We build agents after enablement, one fixed fee."
Delivers: yes, the price chip does it in six words. Smallest edit: cut the
"Location" FAQ (sitewide boilerplate).

nonprofits.html / ecommerce.html. Owe: "AI for the admin around the mission /
the order." Deliver: yes; both H1s are good. Smallest edit: replace the
01/02/03 block with one sentence and a link; cut to two FAQs.

ai-workshop.html. Owes: "Free Claude workshop, Sept 22, St. Petersburg,
register on Luma." Delivers: yes. Fine as the merge target for events.html.

### 1.5 Voice and verbiage

Tics measured across main copy: "actually" 35 uses on 18 pages; "real work"
21 on 15; "review point(s)" 24 on 12; "chatbot" 16 on 7; "human review" 18 on
13; "St. Petersburg" 18 on 9; "In practice" as a kicker on 14 pages; "Working
rule" on 11 and "Working idea" on 5 (the same device under two names).
Boilerplate repeated verbatim or near-verbatim across 4+ pages: "People leave
with prompts and workflows they built during the session" (4 pages); "Bring
us one process..." closers (4); "Start with one process" (4); "book a call
with us" (4); "Hopefully by now" (4); "You just watched us ... for free, in
minutes" (4); "Fees stay unpublished" (4 uses, 2 pages).

Fifteen worst examples with rewrites:

1. ai-consulting-tampa.html, hero lede (76 words): "An AI consultant in Tampa
   helps a team make AI reliable inside work they already own. At altr, that
   means mapping one repeated workflow, training people on their own tools
   (enablement), and only then building agents or connectors when the
   process earns software. We work on site across Tampa Bay including St.
   Petersburg, Wesley Chapel, and Clearwater and focus on operations heavy
   teams in commercial real estate, nonprofits, and ecommerce rather than
   selling a chatbot or a strategy deck alone."
   -> "We map one workflow your team repeats, train your people on your own
   tools, and build software only where the work proves it needs it. On site
   across Tampa Bay. CRE, nonprofits, ecommerce." (36 words)

2. ai-consulting-tampa.html: "That gap is where the money goes, and it is the
   only thing this Tampa AI consulting practice works on."
   -> "That gap is all we work on."

3. ai-consulting-tampa.html: "Searching for an AI consultant near me in Tampa
   Bay usually means you want someone who will sit with the ops owner, not
   only ship remote deliverables."
   -> Cut. It is written for a search engine ("near me") and the visitor can
   tell.

4. workflow-automation-consultant-tampa.html: "Searching for a workflow
   automation consultant in Tampa Bay usually means you want someone who
   will sit with the ops owner, not only ship remote zaps."
   -> "We sit with the person who owns the process."

5. forward-deployed-engineering.html: "With engineers and agents working in
   concert, we ship production systems at a pace your team hasn't
   experienced before. Real features, real infrastructure, real users." and
   "Your team is permanently faster after we leave than before we arrived."
   -> Cut both. Unverifiable claims in a voice the rest of the site avoids.

6. how-we-altr-work.html: "A 30-day plan to an AI-native operation. We
   sequence the work into phases that compound, so the business isn't
   scattered with scattered pilots."
   -> "A 30-day plan, sequenced so each pilot builds on the last." (Also fix
   "opportunites" in the Days 3-6 row.)

7. case-studies.html closer: "Interested in Learning More? Let's explore how
   AI can support your goals and unlock new opportunities."
   -> "Bring us one workflow. We will tell you what it needs."

8. about.html: "altr works with businesses who want AI to become part of the
   way their teams actually work. We run practical workshops, build demos
   around real workflows, and deploy automations close to the people who
   will use them."
   -> "We train teams on their own work, then build the automations that
   follow."

9. claude-cre-skills.html: "There is a reason for this, and this series of
   articles will help you understand why. But first, why should you listen
   to us? Who are we? altr is an AI services company that helps businesses
   get real value out of AI. The altr thesis: model capability is advancing
   faster than most businesses can apply it. We do this in two ways: ..."
   -> Cut the 90-word digression. The byline and the closer carry it.

10. claude-cre-connectors.html: "A connector bridges Claude directly to an
    external app, service, or data source. That turns it from a chatbot
    waiting for pasted context into a working member of the team." then,
    six paragraphs later: "A connector bridges Claude directly to external
    apps, services, and data sources. Connectors turn Claude from a simple
    chatbot into a working member of your team."
    -> Keep the first, delete the second.

11. real-estate.html lede, repeated verbatim as FAQ answer 1: "Commercial
    real estate teams can use AI to organize property research, prepare
    underwriting inputs, work across approved files and systems, draft
    review-ready deliverables, and monitor recurring market signals. The
    right workflow keeps brokers, analysts, asset managers, and principals
    in control of assumptions and decisions."
    -> Lede: "AI for CRE teams: property research, underwriting inputs, file
    work, and market monitoring. The broker or analyst still owns every
    assumption." FAQ answer: keep the long version there only.

12. ai-enablement-workshop.html, three disclaimers: "This is a paid
    engagement. It is not the free public Claude Small Business Workshop." /
    "Looking for the free public sessions? Those are the Claude Small
    Business Workshop dates, listed separately." / "This is a paid
    engagement, quoted on a call. Public Claude Small Business Workshop
    sessions are separate and free."
    -> One line under the price chip: "Paid. The free Claude Small Business
    Workshop is a different thing." with the link.

13. events.html: "Events are separate from our services, but they follow the
    same mindset: concrete examples, live demos, and discussion around the
    workflows teams are actually trying to improve."
    -> Cut with the page.

14. mortr.html: "Hillsborough, Pinellas, Pasco, and Polk are the coverage set
    today. They name where Florida property records are available in mortr.
    They do not make mortr an official county office or a substitute for
    recorded instruments you will rely on."
    -> "Four counties: Hillsborough, Pinellas, Pasco, Polk. Dated public
    records; confirm against the source before you act." Once in the hero,
    once in the FAQ, and delete the other 19 "dated" mentions.

15. impact-spark-labs.html: "The result was not just a pair of automations,
    but a repeatable way for the spARK Labs team to launch and operate these
    workflows inside Claude Cowork. By packaging the process into skills and
    connecting the right tools through MCP, the team can move from intake to
    output with a simple command and a clear set of steps."
    -> "The team now runs both workflows from one slash command in Claude
    Cowork."

Sitewide substitutions: "actually" can be deleted in every one of its 35
uses without changing meaning. "review point" and "human review" are the
same idea; pick one. "Working rule" and "Working idea" are the same device;
pick one.

---------------------------------------------------------------------------

## Part 2: Technical debt

### 2.1 CSS

Measured (comment-stripped rule parse; class usage verified against every
HTML file plus class names added in JS):

| | styles.css | redesign.css |
|---|---:|---:|
| Lines | 6,063 | 1,606 |
| Rules | 893 | 205 |
| Distinct class names in selectors | 375 | 150 |
| Class names matching no markup or JS | 98 | 26 |
| Selectors containing a dead class | 229 | 51 |
| linear/radial-gradient declarations | 27 | 13 |
| box-shadow declarations | 40 | 17 |
| !important | 10 | 5 |
| Selectors declared more than once in the same file | 17 | 16 |

Dead in styles.css (98 classes), grouped by the feature they belonged to:

- Pricing page (deleted): price-hero, price-hero-note, price-ladder,
  price-rung, price-rung-lead, price-rung-start, price-step, price-figure,
  price-amount, price-qualifier, price-basis, price-tag, price-meta,
  price-meta-grid, price-strip, ps-name, ps-desc, ps-price, ps-when. Lines
  3720-3990 and 4716-4862.
- Offer catalog (replaced by the industry grid): offer, offer-list,
  offer-step, offer-head, offer-price, offer-what, offer-gets, offer-fine,
  offer-cta, offer-lead, offer-body, note, note-row, qa, qa-block, qa-list.
  Lines 4044-4300.
- Old home hero with chat typewriter: home-hero, home-hero-inner,
  home-about, home-about-hero, home-about-chat, home-about-statement,
  home-about-actions, home-chat-message, home-chat-user, home-chat-assistant,
  home-chat-label, home-chat-prompt, home-chat-model-mark, home-chat-answer,
  home-chat-thinking, home-section, band-quiet, statement-sub. Lines
  4301-4620. Companion file home-typewriter.js is loaded by no page.
- Generic hero (pre page-hero): hero, hero-main, hero-content,
  hero-narrative, hero-headline. Lines 520-570 and 3510-3520.
- Learning lanes (old tutorials layout): learning-lanes, learning-lane,
  learning-lanes-simple, learning-lane-simple, learning-lane-note,
  learning-lane-header, learning-feature-section, learning-feature-grid.
  Lines 1042-1160, 3215, 3610-3625.
- Work list / featured work (old case-studies layout): work-index-section,
  work-list, work-list-action, work-list-copy, work-list-media,
  work-list-right, featured-work-copy, featured-work-media, case-grid,
  case-card, case-stat, impact-card-logo, impact-card-logo-wrap,
  page-hero-logo.
- Misc: brand-line, service-badge, service-arm-grid, framework-strip,
  framework-figure, modern-gap, modern-proof-band, proof-logos, logo-img-wide,
  logo-tone-flat, logo-tone-warm, trust-list, article-lede, video-embed,
  pull-quote, strategy-lens-grid, tutorial-thumb-automation,
  tutorial-tag-automation.

About 1,157 lines sit in the six contiguous dead blocks alone; with the
scattered selectors it is closer to 1,400 lines, or 23% of the file.

Dead in redesign.css (26 classes, 51 selectors): register, register-id,
register-datum, ledger, ledger-row, ledger-index, ledger-datum, plate,
plate-caption, plate-tall, plate-wide, plate-bleed, process-plate,
process-split, hero-split, hero-col, connector, ticker, wash, closer-note,
band-quiet, home-section, service-badge, service-arm-grid,
tutorial-thumb-automation, tutorial-tag-automation. SYSTEM.md documents the
register line, ticker and plate mark as built then cut; the CSS was not cut
with them. "Ledger" and "wash" are described in SYSTEM.md as live components
but no page uses the class names (the home steps use .home-how .step
instead). Lines 191-240, 317-380, 617-735, 1128-1150, 1215-1265, 1419-1470.

Duplicated within one file: styles.css declares :root twice (lines 21 and
4863), .nav three times (191, 4003, 4867), .nav-links .nav-cta twice,
.impact-card twice, .impact-grid twice, .tutorials-sidebar twice, and the
680px nav media block twice (3351-3440 and 5081-5110). redesign.css declares
.closer three times (405, 846, 1364), .hero-plate and its four children
twice (496-562 and 1155-1192), .home-how .step-num three times, :root twice.
Each duplicate is a place where a later edit silently wins.

The two-file cost. 40 selectors appear in both files; only 8 of those have
every styles.css property redeclared (fully overridden and deletable at
source: .button.primary, .button:active, .about-page-simple,
.about-beliefs h2, .closer, .closer h2, .home-hero-actions, .band). The other
32 are partial patches (for example .nav: 18 properties in styles.css, 3
re-set in redesign.css). So redesign.css is mostly additive, not an
override layer, and the real cost is not conflicting declarations but
resolution: every rendered value for .nav, .button, .footer, .step-num,
.work-card, .section-top, .statement, the six tutorial-thumb classes and
:root tokens requires reading two files, and cascade order depends on the
<link> order being identical in 50 hand-edited files (it is; but
privacy.html, terms.html and website-terms.html load styles.css with no
cache-busting query while mortr.html uses ?v=20260907a and the rest
?v=20260906b).

Fonts: styles.css line 1 @imports Clash Grotesk from api.fontshare.com; the
HTML <link>s JetBrains Mono from Google Fonts with weights 500;700 while a
url() in styles.css requests it again with 400;500;700. Lora is self-hosted
via @font-face. assets/fonts/SpaceGrotesk-*.ttf/.woff2 (183 KB) are
referenced only by assets/impact-spark-labs-og.html.

Recommendation: collapse to one file. Order of work: (1) delete the six dead
blocks and the 98 dead classes from styles.css; (2) delete the 26 retired
components from redesign.css; (3) for the 40 shared selectors, write the
merged declaration into styles.css and delete it from redesign.css; (4)
append what is left of redesign.css to styles.css under one header; (5) one
<link>, one version string, on 50 pages. Expected result around 5,000 lines
from 7,669, with a single source of truth per selector. AUDIT.md item 4
("strip the gradients and soft shadows... keep exactly one shadow") is not
done: 57 box-shadow declarations remain across the two files.

### 2.2 HTML

Repeated markup that should be one shared block:

- The gtag snippet (11 lines) is pasted in all 50 files.
- <head> boilerplate (favicon x2, apple-touch-icon, preconnect x2, font link,
  two stylesheets) is pasted in 49 files, with drift: pricing.html has none
  of it; geo.region/geo.placename appear only on index.html; og:title and
  twitter:card are missing on 404.html, ai-in-real-estate-guide-thank-you
  .html, privacy.html, terms.html, website-terms.html; og:image is missing
  on 6 pages.
- The nav exists in 14 distinct HTML variants (hash of the <header>). The
  differences: CTA text "Book free consultation" (3 pages) vs "Book a free
  consultation" (46); index.html has an Events link nobody else has;
  ai-workshop.html has its own Events link pointing at itself;
  forward-deployed-engineering.html links what-we-do.html and
  calendly.com/jarredrobidoux; aria-current placement varies. Then
  nav-dropdown.js replaces the Services, Work and Blog anchors with three
  dropdowns at runtime, so what is in the HTML is not what renders. A
  crawler without JS sees "Services -> index.html#who-we-serve" and no link
  to real-estate.html, nonprofits.html, ecommerce.html, how-we-altr-work
  .html, internal-products.html or mortr.html from the nav.
- The footer exists in 9 variants. Tagline "AI services for teams who want
  to do real work" on 46 pages vs "Software and AI strategy for teams who
  want to do real work" on index.html and how-we-altr-work.html; the three
  legal pages omit "Tampa, FL"; whitespace differences account for the rest.
- Every article page repeats the same Article + Organization + WebPage
  JSON-LD with only the title/description/date changed, and the four CRE
  guides use Person author while the other nine use Organization.
- The intake modal markup lives in a JS template string (intake-modal.js)
  and again as static HTML on start-a-conversation.html, with different
  label text ("What are you interested in solving?" vs "...discussing?").

Inconsistent class usage for one component: the AUDIT.md count still holds.
engagement-item (120), tutorial-card (13), resource-item (11), work-card (6),
workshop-topic-card (6), impact-card (5), real-estate-card (4), founder-card
(2) all render "a bordered thing with a heading and a paragraph". Ten hero
class combinations for six page types. Section wrappers: product-page-section
(59), article-block (91), cta-section (29), article-section (17), band (5),
strategy-section (3).

Orphaned or leftover elements: the filter UI on case-studies.html (search,
4 checkboxes, view toggle, clear) for 5 items and on tutorials.html for 17;
the "Quoted / scoped on a call" price chips are counted as CTAs by their
markup (they are <a> with button classes); assets/impact-spark-labs-og.html
is a share-card generator deployed at a public URL with no canonical or
noindex; design-language/hero-variants.html, plate-library.html and
redesign-preview.html are deployed (they do carry noindex).

Accessibility: every page has exactly one h1, no heading-level skips, and
every <img> has alt text. Problems: how-we-altr-work.html h1 is
`<span>Find where AI</span><span>improves your business</span>` with no
space, so the accessible name and any copied text read "Find where
AIimproves your business"; mortr.html's two images have no width/height
(layout shift); the mono kicker style is 11px uppercase at reduced ink
(SYSTEM.md "dim ink") - contrast is unverified here, measure the rendered
color against #F7F3EC and hold 4.5:1; the hero canvas on how-we-altr-work
.html and the scan/roadmap loops in ai-strategy.js animate indefinitely,
against the design rule that nothing moves longer than 150ms (they do
respect prefers-reduced-motion).

Broken: law-firms.html -> uploads/2024/01/FL-Bar-Ethics-Op-24-1.pdf (file
does not exist); forward-deployed-engineering.html -> what-we-do.html (4
links; covered by a _redirects rule so it resolves, but the nav item marked
aria-current="page" points at a redirect).

### 2.3 JS

| File | Lines | Pages | Verdict |
|---|---:|---:|---|
| nav-dropdown.js | 214 | 49 | Used. Rebuilds the nav client-side; move the dropdown markup into HTML and keep only the toggle/escape/click-outside logic (about 60 lines). |
| intake-modal.js | 129 | 39 | Used; it is the funnel. Loaded on 39 pages; missing on 10 (the legal pages, guide pages, start-a-conversation, 404, pricing, impact-real-estate-property-intelligence.html, ai-workshop.html), so "Book a call" behaves differently on those. Load it everywhere or nowhere. |
| site-motion.js | 89 | 33 | Dead. It adds .reveal-on-scroll and toggles .is-visible; redesign.css 1448-1455 forces those elements visible with !important. 33 script tags doing nothing. Delete. |
| home-typewriter.js | 73 | 0 | Dead. No page includes it; its markup (data-typewriter, home-chat-*) exists on no page; its CSS is in the dead home-chat block. Delete. |
| hero-keys.js | 163 | 1 | Used only on how-we-altr-work.html (canvas keycap field). Keep if that hero stays; it is the one animation the brand guide endorses. |
| ai-strategy.js | 100 | 1 | Half dead. Its reveal logic is neutralized by the same !important rule ([data-strategy-reveal]); the scan and roadmap demo loops run. If the page is rewritten (item 4), the demos likely go and the file with them. |
| impact-ui.js | 76 | 1 | Duplicate of tutorials-ui.js with the selectors renamed (grid id, card class, desc class). Either one 75-line file parameterized by data attributes, or delete both by removing the filter UI. |
| tutorials-ui.js | 75 | 1 | See above. |
| lead-magnet-form.js | 23 | 1 | Used. Fine. |

Also: assets/particles.min.js is referenced by nothing; delete.

### 2.4 Assets

118 files under assets/, altr-brand-assets/ and uploads/ (46.2 MB on disk;
109 asset files are git-tracked and therefore deployed). 32 files (9.3 MB)
are referenced by no HTML, CSS, JS, llms.txt, README or design-language
file (basename grep):

altr-brand-assets/assets/hero-computer-logo-background.png (1,923 KB),
assets/bebrief logo-2.png (1,227), assets/bebrief logo.png (1,221),
assets/plates/cut-masontools.webp (845), assets/operations-mcp-sbs.pdf (630),
assets/operations-mcp.pdf (556), assets/plates/plate-hero-scene.webp (403),
assets/fishin-prints logo-2.png (345), assets/fishin-prints logo.png (339),
assets/plates/plate-shop-scene.webp (322), assets/altr-delegation-framework
.png (230), altr-brand-assets/assets/logo-w-background.png (182),
uploads/robot.png (177), assets/fonts/SpaceGrotesk-VariableFont_wght.ttf
(134), assets/altr_key_logo_cream_taupe_transparent.png (105),
assets/altr-4d-framework.png (102), assets/nonprofit-member-onboarding.png
(94), uploads/fde.png (90), assets/altr-discernment-loop.png (75),
assets/fonts/SpaceGrotesk-VariableFont_wght.woff2 (49),
assets/altr_social_avatar_ivory.png (48), altr-brand-assets/assets/logo-banner
.png (46), assets/spark-logo-transparent.png (28), assets/particles.min.js,
and the remaining small files in the script output.

Plates: 23 .webp in assets/plates; CSS references 9 (bg-shop, bg-workshop,
cut-plan, cut-stone, cut-vault, cut-window, plate-pattern, wash-brick,
wash-workshop). The other 14 (cut-barrels 853 KB, cut-carriage 602,
cut-frames, cut-lathe, cut-machine, cut-masontools 845, plate-hero,
plate-hero-scene, plate-process, plate-shop, plate-shop-scene, plate-wide,
wash-facade, wash-quarry; about 6.5 MB) are referenced only from
design-language docs. SYSTEM.md and IMAGERY.md describe the cutouts as
lathe/casks/saws/carriage/martinet; the CSS ships plan/vault/window/stone.
One of the two is stale (unverified which was intended).

Oversized files in use: uploads/videos/event-request-final-web.mp4 7.4 MB
(impact-spark-labs.html), output/pdf/ai-in-real-estate-field-guide.pdf
7.0 MB, assets/claude-small-business-workshop-header.png 2.5 MB (ai-workshop
hero; a 355 KB .webp sibling exists), the four claude-cre-*.png headers at
1.6 MB each (used as the article hero <img src>; their .webp siblings are
used only as tutorials.html thumbnails), assets/04_bull_trout_pair.png
1.3 MB, assets/real-estate-case-study-placeholder.png 776 KB (two pages),
assets/plates/wash-brick.webp 948 KB. Every <img> has width and height
except the two on mortr.html. Missing loading="lazy": 26 of the 27 images on
the four CRE guide pages (the first is the hero and should stay eager), the
two mortr images, the guide covers, the ai-workshop hero (correctly eager).

### 2.5 Correctness

- Sitemap: all 42 URLs resolve to files and self-canonicalize (the existing
  tests/seo_integrity_test.py enforces this). Not in the sitemap: law-firms
  .html (noindex), resources.html (canonical elsewhere), privacy.html,
  terms.html, website-terms.html, 404.html, the thank-you page, pricing.html.
  The legal pages could be added; nothing else should be.
- _redirects: `/pricing -> /pricing.html` lands on a noindex meta-refresh
  stub; `/law-firms -> /law-firms.html` lands on a noindex page. No rule
  points at a missing file. After the merges, the five `/x -> /x.html`
  rules for removed pages must be replaced (exact lines in 3.4).
- Canonicals: no duplicates except resources.html -> tutorials.html
  (intentional) and pricing.html -> https://altrwork.com/#who-we-serve (a
  fragment canonical; Google ignores fragments, so this is effectively a
  canonical to the homepage on a noindex page - harmless, but delete the
  page).
- Titles: no duplicates. mortr.html title is 63 characters. Suffix drift:
  "| altr" (39), "| altr Tampa" (7), and three one-offs.
- Descriptions: no duplicates. Over 160 characters: mortr.html 261,
  law-firms.html 174, can-claude-connect-to-costar.html 173,
  claude-skills-vs-mcp.html 167.
- Broken internal links: 1 hard 404 (law-firms PDF), 4 soft (FDE ->
  what-we-do.html via redirect).
- Orphans (zero inbound HTML links): forward-deployed-engineering.html,
  internal-products.html (reachable only via the JS dropdown), law-firms
  .html, website-terms.html, plus the intentional 404/thank-you/pricing.
- Three LocalBusiness/ProfessionalService blocks (index.html,
  ai-consulting-tampa.html, workflow-automation-consultant-tampa.html) share
  the same @id https://altrwork.com/#business, which is the correct way to
  say "same entity"; fine as is. Verify the areaServed lists agree (index
  names 6 places, the workflow page 8) - unverified whether that is
  intentional.
- The footer "Terms" link on 49 pages resolves to the MSA, not the website
  terms.

---------------------------------------------------------------------------

## Part 3: SEO footprint check

### 3.1 Pages proposed for removal

| Page | Canonical | Title | Meta description (start) | Inferred target keywords | Inbound links (HTML) | In sitemap | 301 target | Target carries the keywords? |
|---|---|---|---|---|---:|---|---|---|
| events.html | https://altrwork.com/events.html | AI Workshops and Demos in Tampa \| altr | "AI workshops, demos, and live enablement sessions from altr for Tampa Bay teams exploring practical AI at work." | AI workshop Tampa, AI demo Tampa, altr events | 2 (index.html nav, ai-consulting-tampa.html) | Yes | ai-workshop.html | Yes: H1 "Claude workshops for Tampa Bay small businesses", h2 "See every Tampa Bay Claude AI workshop", Event/EventSeries schema with Place. Add "demos" to one heading when merging the community-demo paragraph. |
| forward-deployed-engineering.html | https://altrwork.com/forward-deployed-engineering.html | Forward Deployed AI Engineering \| altr Tampa | "How altr works: engineers build next to the people doing the work, so agents and automations land in real workflows. A method, not headcount for hire." | forward deployed engineering, forward deployed AI engineer | 0 | Yes | how-we-altr-work.html | Only if the target gains an H2 "Forward deployed engineering" and the .page-note. The phrase is in index.html schema knowsAbout, so keep it on a live heading. |
| resources.html | https://altrwork.com/tutorials.html (already) | Journal \| AI Consulting and Automation Notes from altr | "Technical and operator notes from altr on AI automation, workflow design, MCP..." | none owned; canonicalized to tutorials | 2 (404.html, tutorials.html) | No | tutorials.html | Yes; the target already owns the canonical. |
| internal-products.html | https://altrwork.com/internal-products.html | Internal Products \| altr Tampa | "Products from the altr studio, including mortr for Florida property owner and parcel research in chat." | mortr, Florida property owner research (both owned by mortr.html) | 0 (JS dropdown only) | Yes | mortr.html | Yes; mortr.html title and H1 carry "Florida property owner", "parcel", "research in chat". |
| pricing.html | https://altrwork.com/#who-we-serve | Pricing \| altr | "Explore the industries altr serves and book a call..." | altr pricing | 0 | No (noindex) | /#who-we-serve | The homepage does not say "pricing" anywhere. README says no fees are published by policy, so there is nothing to carry. Accept. |

### 3.2 Keyword cannibalization

- "AI consultant Tampa" / "AI consulting Tampa": index.html (title "AI
  Strategy and Consulting in Tampa"), ai-consulting-tampa.html (title and
  H1), workflow-automation-consultant-tampa.html (uses "AI consultant in
  Tampa" as anchor text 3 times and in two FAQ answers), about.html (title
  "Tampa AI Automation and Enablement Studio"). Fix without merging: let
  ai-consulting-tampa.html own the phrase; cut it to one cross-link on the
  workflow page; give index.html a brand-first title ("altr | Software and
  AI strategy for operations teams, Tampa") so the two do not fight.
- "workflow automation Tampa": workflow-automation-consultant-tampa.html
  should own it. ai-consulting-tampa.html mentions "workflow automation
  consultant in Tampa" once as a cross-link; fine.
- "AI workshop Tampa": ai-workshop.html, events.html, ai-enablement-workshop
  .html. Merging events.html into ai-workshop.html improves this: one page
  with Event schema for the free public session, one page for the paid
  engagement. The paid page's title is "AI Enablement Workshop for Teams |
  altr Tampa", so all three pages currently carry "workshop" and "Tampa".
  After the merge two do; for a clean split, retitle the paid page around
  "AI enablement" or "team AI training" and leave "workshop" to the free
  session.
- "workflow audit": workflow-audit.html (service) vs
  ai-workflow-audit-small-business.html (how-to). Different intents; keep
  both, but the service page's H1 "Workflow discovery" gives the query away.
  Change the H1 to "Workflow audit".
- "Claude Cowork": claude-cowork.html vs claude-cre-cowork.html. The generic
  page should rank for the bare term; the CRE page for "Claude Cowork
  underwriting / CRE". The shared intro paragraphs blur that; deduping them
  (1.3) sharpens both.
- "how altr works / AI strategy": how-we-altr-work.html vs about.html vs
  forward-deployed-engineering.html. Merging FDE in consolidates the
  "method" pages to one. Positive.
- "MCP": mcp-server-design-internal-ai-tools.html, mcp-agents-function-
  calling.html, claude-skills-vs-mcp.html, impact-spark-labs-mcp.html.
  Distinct modifiers (design / vs function calling / vs skills / case
  study). No action.

### 3.3 Do not touch

- index.html, ai-consulting-tampa.html, workflow-automation-consultant-tampa
  .html: the local commercial-intent set. Trim copy inside them; keep URLs,
  titles, H1s, FAQPage and LocalBusiness JSON-LD.
- real-estate.html (the CRE hub), mortr.html (owns "Florida property owner
  lookup", "Florida parcel lookup"; keep every FAQ question), can-claude-
  connect-to-costar.html (a query nobody else answers), the four
  claude-cre-*.html guides (a numbered series; keep as four URLs),
  ai-in-real-estate-guide.html and its thank-you page (lead magnet with
  DigitalDocument schema).
- Every <script type="application/ld+json"> block, every <link
  rel="canonical">, sitemap.xml, robots.txt.
- llms.txt: do not delete or restructure. It must be edited for URL changes
  only: it links events.html, forward-deployed-engineering.html and
  resources.html, which would 301 after the merges. Update those three lines
  and nothing else.
- The 13 article pages: distinct queries, one CTA each, 394-703 words. They
  are the best-behaved pages on the site.

### 3.4 Exact _redirects changes

Replace these existing lines:

    /events                                       /events.html                                  301!
    /forward-deployed-engineering                 /forward-deployed-engineering.html            301!
    /resources                                    /resources.html                               301!
    /internal-products                            /internal-products.html                       301!
    /pricing                                      /pricing.html                                 301!

with:

    /events.html                                  /ai-workshop.html                             301!
    /events                                       /ai-workshop.html                             301!
    /forward-deployed-engineering.html            /how-we-altr-work.html                        301!
    /forward-deployed-engineering                 /how-we-altr-work.html                        301!
    /resources.html                               /tutorials.html                               301!
    /resources                                    /tutorials.html                               301!
    /internal-products.html                       /mortr.html                                   301!
    /internal-products                            /mortr.html                                   301!
    /pricing.html                                 /#who-we-serve                                301!
    /pricing                                      /#who-we-serve                                301!

Then: remove events.html, forward-deployed-engineering.html and
internal-products.html from sitemap.xml; update the three llms.txt links;
update index.html and ai-consulting-tampa.html links to events.html; update
nav-dropdown.js (or the new static nav) Work menu to link mortr.html;
re-run tests/seo_integrity_test.py.

---------------------------------------------------------------------------

## Appendix A: per-page table

Words = main-column text (nav, footer, scripts excluded). Sections = count
of <section> elements. CTAs = anchors in main with button classes or pointing
at start-a-conversation.html, Calendly or mailto. Min = words / 230. Inbound
= number of other HTML files linking to the page (JS-generated nav links not
counted). Sorted worst to best by words.

| # | File | Words | Sections | CTAs | Min | Inbound | Sitemap | Title |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | terms.html | 3721 | 0 | 0 | 16.2 | 49 | no | Master Services Agreement \| altr |
| 2 | ai-consulting-tampa.html | 1692 | 9 | 3 | 7.4 | 46 | yes | AI Consulting in Tampa \| AI Consultant for Ops Teams \| altr |
| 3 | workflow-automation-consultant-tampa.html | 1507 | 8 | 3 | 6.6 | 1 | yes | Workflow Automation Consultant in Tampa \| altr |
| 4 | real-estate.html | 1255 | 8 | 3 | 5.5 | 11 | yes | AI for Commercial Real Estate Teams \| altr |
| 5 | ai-enablement-workshop.html | 1149 | 7 | 4 | 5.0 | 10 | yes | AI Enablement Workshop for Teams \| altr Tampa |
| 6 | mortr.html | 1091 | 9 | 5 | 4.7 | 2 | yes | mortr \| Florida Property Owner & Parcel Research in Chat \| altr |
| 7 | privacy.html | 963 | 0 | 0 | 4.2 | 49 | no | Privacy Policy \| altr |
| 8 | website-terms.html | 868 | 0 | 0 | 3.8 | 0 | no | Website Terms of Use \| altr |
| 9 | claude-cre-connectors.html | 857 | 11 | 1 | 3.7 | 6 | yes | Claude in CRE: Connectors \| altr |
| 10 | claude-cre-skills.html | 852 | 10 | 1 | 3.7 | 5 | yes | Claude in CRE: Skills \| altr |
| 11 | law-firms.html | 756 | 6 | 3 | 3.3 | 0 | no | AI for Law Firms \| AI Consulting \| altr |
| 12 | claude-cre-scheduled-tasks.html | 737 | 9 | 1 | 3.2 | 5 | yes | Claude in CRE: Scheduled Tasks \| altr |
| 13 | claude-skills-vs-mcp.html | 703 | 8 | 1 | 3.1 | 4 | yes | Claude Skills vs MCP: when to use each \| altr |
| 14 | can-claude-connect-to-costar.html | 681 | 8 | 1 | 3.0 | 7 | yes | Can Claude connect to CoStar? \| altr |
| 15 | claude-cre-cowork.html | 635 | 8 | 1 | 2.8 | 6 | yes | Claude in CRE: Cowork \| altr |
| 16 | claude-cowork.html | 622 | 8 | 1 | 2.7 | 7 | yes | Claude Cowork: what it is and how a team uses it \| altr |
| 17 | impact-spark-labs-mcp.html | 616 | 3 | 2 | 2.7 | 7 | yes | spARK Labs Remote MCP Server Impact Study \| altr |
| 18 | tutorials.html | 606 | 4 | 2 | 2.6 | 49 | yes | Blog \| Notes and guides on practical AI \| altr |
| 19 | forward-deployed-engineering.html | 537 | 5 | 3 | 2.3 | 0 | yes | Forward Deployed AI Engineering \| altr Tampa |
| 20 | custom-agents.html | 534 | 6 | 3 | 2.3 | 10 | yes | Custom AI Agents and Workflow Automations \| altr Tampa |
| 21 | impact-spark-labs.html | 515 | 3 | 3 | 2.2 | 6 | yes | spARK Labs AI Automation Impact Study \| altr |
| 22 | how-we-altr-work.html | 513 | 5 | 3 | 2.2 | 2 | yes | AI Strategy \| How altr Works \| altr |
| 23 | ai-workflow-audit-small-business.html | 510 | 8 | 1 | 2.2 | 5 | yes | AI Workflow Audit for Small Businesses \| altr |
| 24 | writing-a-skill-md.html | 503 | 8 | 1 | 2.2 | 4 | yes | How to write a SKILL.md that actually gets used \| altr |
| 25 | ai-governance-lite-smb.html | 497 | 8 | 1 | 2.2 | 5 | yes | AI Governance Lite for SMBs \| altr |
| 26 | nonprofits.html | 493 | 6 | 3 | 2.1 | 3 | yes | AI for Nonprofits \| AI Consulting \| altr |
| 27 | ecommerce.html | 487 | 6 | 3 | 2.1 | 3 | yes | AI Consulting for Ecommerce Teams \| altr |
| 28 | three-phases-ai-deployment.html | 457 | 8 | 1 | 2.0 | 5 | yes | The Three Phases of AI Deployment \| altr |
| 29 | mcp-server-design-internal-ai-tools.html | 429 | 8 | 1 | 1.9 | 6 | yes | MCP Server Design for Internal AI Tools \| altr |
| 30 | context-engineering-large-codebases.html | 419 | 8 | 1 | 1.8 | 6 | yes | Context Engineering for Large Codebases \| altr |
| 31 | llm-retrieval-grounded-answers.html | 408 | 8 | 1 | 1.8 | 3 | yes | How LLM Retrieval Grounds Answers \| altr |
| 32 | ai-code-review-judge-agents.html | 403 | 8 | 1 | 1.8 | 4 | yes | AI Code Review With Judge Agents \| altr |
| 33 | workflow-audit.html | 402 | 5 | 3 | 1.7 | 6 | yes | Workflow Audit for AI Automation \| altr Tampa |
| 34 | mcp-agents-function-calling.html | 399 | 8 | 1 | 1.7 | 4 | yes | MCP vs Agents and Function Calling \| altr |
| 35 | rag-evaluation-internal-knowledge-bases.html | 394 | 8 | 1 | 1.7 | 4 | yes | RAG Evaluation for Internal Knowledge Bases \| altr |
| 36 | events.html | 389 | 5 | 1 | 1.7 | 2 | yes | AI Workshops and Demos in Tampa \| altr |
| 37 | index.html | 384 | 6 | 4 | 1.7 | 50 | yes | altr \| AI Strategy and Consulting in Tampa |
| 38 | ai-workshop.html | 373 | 5 | 2 | 1.6 | 4 | yes | Free Claude Workshops for Tampa Bay Small Businesses \| altr |
| 39 | about.html | 371 | 6 | 1 | 1.6 | 49 | yes | About altr \| Tampa AI Automation and Enablement Studio |
| 40 | impact-bebrief.html | 349 | 3 | 2 | 1.5 | 3 | yes | BeBrief AI Enablement Impact Study \| altr |
| 41 | impact-real-estate-property-intelligence.html | 346 | 3 | 1 | 1.5 | 2 | yes | Accelerating Property Research with AI-Powered Tools \| altr |
| 42 | resources.html | 330 | 2 | 0 | 1.4 | 1 | no | Journal \| AI Consulting and Automation Notes from altr |
| 43 | impact-fishin-prints.html | 307 | 4 | 2 | 1.3 | 3 | yes | Fishin Prints AI Workflow Impact Study \| altr |
| 44 | ai-in-real-estate-guide.html | 268 | 3 | 0 | 1.2 | 3 | yes | AI in Real Estate Field Guide \| Free PDF from altr |
| 45 | case-studies.html | 202 | 3 | 1 | 0.9 | 49 | yes | AI Work and Case Studies \| altr Tampa |
| 46 | internal-products.html | 80 | 2 | 0 | 0.3 | 0 | yes | Internal Products \| altr Tampa |
| 47 | 404.html | 69 | 2 | 2 | 0.3 | 0 | no | Page not found \| altr |
| 48 | start-a-conversation.html | 54 | 2 | 0 | 0.2 | 38 | yes | Book a Call \| altr Tampa |
| 49 | ai-in-real-estate-guide-thank-you.html | 47 | 1 | 2 | 0.2 | 0 | no | Your AI in Real Estate Field Guide \| altr |
| 50 | pricing.html | 21 | 1 | 0 | 0.1 | 0 | no | Pricing \| altr |

Total main-column words: 30,801. Pages over 700 words: 13. Pages with 3+ CTAs: 14.
