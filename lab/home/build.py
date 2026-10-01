"""Builds four full homepage design options into lab/home/ from one copy deck.
Run from the repo root: python lab/home/build.py"""

C = {
    "eyebrow": "AI audits, automation and training for small and medium-sized businesses",
    "h1": ["Do more with", "the team", "you have."],
    "lede": "We find the work that eats your team's week, automate it, and train your people to use AI on the rest.",
    "services": [
        ("AI Audit", "../../how-we-altr-work.html", "We sit with the people who do the work and find where the hours go. You get a ranked list: what to automate, what to train, what to leave alone.", "Walk us through your week."),
        ("Automation", "../../custom-agents.html", "Systems that do the repetitive work inside the tools you already use: orders entered, bills matched, intake sorted, reports written. Anything unusual waits for a person.", "Send us twenty recent examples of the paperwork."),
        ("AI Training", "../../ai-enablement-workshop.html", "We set up Claude for your company and train your team on their real work, so they leave with tools that already do part of their job.", "Bring the team and one task each."),
    ],
    "teams": [("Office and admin", "Bills, forms, filing and the shared inbox."), ("Operations", "Orders, scheduling and the hand-offs between them."),
              ("Sales and service", "Follow-ups, quotes and customer requests."), ("Finance and billing", "Invoices, statements and month-end."),
              ("Owners and managers", "The Monday summary and the decisions behind it.")],
    "work": [("Slice of Heaven Cakes", "Every cake order in one place, answered on arrival.", "../../impact-slice-of-heaven-cakes.html"),
             ("Fishin Prints", "From a customer's catch photo to print-ready art.", "../../impact-fishin-prints.html"),
             ("CRE Harness", "From a property address to a branded broker opinion of value.", "../../impact-real-estate-property-intelligence.html")],
    "faq": [("We already pay for ChatGPT and almost nobody uses it. Why is this different?", "We train people on their own work, not on features, and save what they build where the whole team can use it."),
            ("I don't have an IT person. Who keeps this running?", "We do, for as long as you want. It runs on the tools you already have, and you get the notes to take it over."),
            ("Will this replace my staff?", "No. It takes the retyping and chasing off their plate. Most owners use the time to grow without hiring."),
            ("Is our data safe?", "Stored encrypted, seen only by your team and ours, and never used to train AI. Nothing is sent or approved without your say.")],
}
LOGOS = [("../../assets/clients/vector-cre.svg", "Vector Commercial Real Estate", ""), ("../../assets/clients/spark-labs.svg", "spARK Labs", "mono"),
         ("../../assets/clients/fishin-prints.webp", "Fishin Prints", ""), ("../../assets/clients/bebrief.webp", "BeBrief", "")]
CAL = "https://calendly.com/altrwork/30min?utm_source=altr_site&amp;utm_medium=lab"


def head(title, fonts, css):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8" /><title>{title} | altr design option</title>
<meta name="viewport" content="width=device-width, initial-scale=1" /><meta name="robots" content="noindex, nofollow" />
<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet" />
<style>*,*::before,*::after{{box-sizing:border-box}}body{{margin:0}}h1,h2,h3,p,ul,ol,figure{{margin:0}}ul,ol{{list-style:none;padding:0}}a{{color:inherit}}img{{display:block;max-width:100%;height:auto}}
:focus-visible{{outline:2px solid currentColor;outline-offset:4px}}.wrap{{width:min(1240px,calc(100% - 2*var(--m)));margin-inline:auto}}
.optbar{{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:99;display:flex;gap:4px;padding:6px;border-radius:10px;background:rgba(20,17,14,.92);border:1px solid rgba(242,237,228,.2);font:500 12.5px/1 system-ui,sans-serif}}
.optbar a{{color:#B9B0A3;text-decoration:none;padding:8px 10px;border-radius:6px}}.optbar a[aria-current]{{background:#F2EDE4;color:#14110E}}
@media (prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important}}}}
{css}</style></head><body>'''


def optbar(cur):
    names = [("ledger", "1 Ledger"), ("signal", "2 Signal"), ("desk", "3 Desk"), ("collage", "4 Collage"), ("../../index.html", "5 Current")]
    return '<nav class="optbar" aria-label="Design options">' + "".join(
        f'<a href="{(n if n.endswith(".html") else n + ".html")}"{" aria-current=\"page\"" if n == cur else ""}>{l}</a>' for n, l in names) + "</nav>"


def logos(cls=""):
    return '<ul class="logos ' + cls + '">' + "".join(f'<li class="{m}"><img src="{s}" alt="{a}" loading="lazy" /></li>' for s, a, m in LOGOS) + "</ul>"


def services(item):
    return "".join(item(*s) for s in C["services"])


def faq(cls="faq"):
    return f'<div class="{cls}">' + "".join(f'<details><summary><h3>{q}</h3></summary><p>{a}</p></details>' for q, a in C["faq"]) + "</div>"


REVEAL = '''<script>(()=>{const r=matchMedia('(prefers-reduced-motion: reduce)').matches;const els=document.querySelectorAll('[data-in]');
if(r||!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return}
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
els.forEach(e=>io.observe(e));setTimeout(()=>els.forEach(e=>e.classList.add('in')),3500)})()</script>'''

# ----------------------------------------------------------------- 1 LEDGER
ledger_css = '''
:root{--m:clamp(20px,5vw,72px);--paper:#F3EEE4;--paper-2:#EAE3D6;--ink:#1A1714;--ink-2:#4A4239;--ink-3:#756B5F;--copper:#9C4E22;--rule:rgba(26,23,20,.16)}
body{background:var(--paper);color:var(--ink);font:400 17px/1.6 "Geist",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.serif{font-family:"Instrument Serif",Georgia,serif;font-weight:400}
nav.top{display:flex;align-items:center;gap:28px;height:76px}nav.top .brand{font:400 30px/1 "Instrument Serif",serif;margin-right:auto;text-decoration:none}
nav.top a{text-decoration:none;font-size:15px;color:var(--ink-2)}nav.top a:hover{color:var(--ink)}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 24px;border-radius:999px;background:var(--ink);color:var(--paper);font-weight:500;text-decoration:none;transition:background .2s}
.btn:hover{background:var(--copper)}.btn.sm{min-height:40px;padding:0 18px;font-size:14.5px;color:var(--paper)!important}
.link{text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1px}
.hero{padding-block:56px 40px;border-bottom:1px solid var(--rule)}
.hero h1{font:400 clamp(4rem,11.5vw,10.5rem)/.86 "Instrument Serif",serif;letter-spacing:-.025em}
.hero h1 em{color:var(--copper)}
.hero-row{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:40px;align-items:end;margin-top:40px}
.hero-row p{font-size:clamp(1.1rem,1.5vw,1.3rem);line-height:1.5;color:var(--ink-2);max-width:32ch}
.hero-row .acts{display:flex;gap:22px;align-items:center;margin-top:28px;flex-wrap:wrap}
.hero-art{margin-top:-180px;justify-self:end;width:min(100%,640px);mix-blend-mode:multiply}
.eyebrow{font-size:14px;color:var(--ink-3);margin-bottom:24px}
.logos{display:flex;justify-content:space-between;align-items:center;gap:28px;flex-wrap:wrap;padding-block:34px}
.logos img{height:30px;width:auto;filter:brightness(0);opacity:.62}.logos .mono img{filter:invert(1) brightness(0)}
section.s{padding-block:clamp(72px,10vw,140px);border-top:1px solid var(--rule)}
.s-head{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:40px}
h2{font:400 clamp(2.4rem,4.6vw,4rem)/1 "Instrument Serif",serif;letter-spacing:-.015em}
.svc{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:40px;padding-block:34px;border-top:1px solid var(--rule);text-decoration:none}
.svc:first-child{border-top:0}.svc h3{font:400 clamp(2rem,3.6vw,3.2rem)/1 "Instrument Serif",serif;transition:color .2s}.svc:hover h3{color:var(--copper)}
.svc p{color:var(--ink-2);max-width:56ch}.svc small{display:block;margin-top:10px;font-size:15px;color:var(--ink)}
.teams li{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:24px;padding-block:20px;border-top:1px solid var(--rule)}
.teams b{font:400 1.75rem/1.1 "Instrument Serif",serif}.teams span{color:var(--ink-2)}
.feature{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,6fr);gap:48px;align-items:center;padding:clamp(28px,4vw,56px);background:var(--paper-2);border-radius:4px;text-decoration:none}
.feature img{width:min(100%,360px);margin-inline:auto;filter:invert(1) brightness(.2)}
.feature h3{font:400 clamp(1.9rem,3vw,2.7rem)/1.05 "Instrument Serif",serif}.feature p{color:var(--ink-2);margin-top:14px}.feature .meta{font-size:14px;color:var(--ink-3);margin-bottom:12px}
.list a{display:grid;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:24px;padding-block:20px;border-top:1px solid var(--rule);text-decoration:none}.list a:hover b{color:var(--copper)}
.list b{font-weight:500}.list span{color:var(--ink-2)}
.faq details{border-top:1px solid var(--rule)}.faq details:last-child{border-bottom:1px solid var(--rule)}
.faq summary{display:flex;justify-content:space-between;gap:20px;padding-block:22px;cursor:pointer;list-style:none}.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font:400 2rem/1 "Instrument Serif",serif;color:var(--copper)}.faq details[open] summary::after{content:"\\2013"}
.faq h3{font:400 1.55rem/1.2 "Instrument Serif",serif}.faq p{padding-bottom:24px;color:var(--ink-2);max-width:62ch}
.closer{background:var(--ink);color:var(--paper);padding-block:clamp(90px,12vw,170px)}
.closer h2{font-size:clamp(3rem,7vw,6.4rem);max-width:13ch}.closer p{color:#C9C0B2;margin-top:24px;max-width:40ch;font-size:1.15rem}
.closer .btn{background:var(--paper);color:var(--ink);margin-top:36px}.closer .btn:hover{background:#E8B48E}
footer{background:var(--ink);color:#A79C8D;padding-block:40px;border-top:1px solid rgba(242,237,228,.12);font-size:14px}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}footer a{color:#F2EDE4;text-decoration:none;margin-left:18px}
[data-in]{opacity:0;transform:translateY(22px);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform .9s cubic-bezier(.16,1,.3,1)}[data-in].in{opacity:1;transform:none}
.hero h1 .l{display:block;overflow:hidden}.hero h1 .l span{display:block;transform:translateY(105%);animation:up 1s cubic-bezier(.16,1,.3,1) forwards}
.hero h1 .l:nth-child(2) span{animation-delay:.08s}.hero h1 .l:nth-child(3) span{animation-delay:.16s}@keyframes up{to{transform:none}}
@media (max-width:860px){.hero-row,.s-head,.svc,.feature,.teams li,.list a{grid-template-columns:1fr}.hero-art{margin-top:24px;justify-self:center}nav.top a:not(.brand):not(.btn){display:none}}
'''
ledger = head("Ledger", "family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600", ledger_css) + f'''
<header class="wrap"><nav class="top" aria-label="Primary"><a class="brand" href="ledger.html">altr</a><a href="../../how-we-altr-work.html">AI Audit</a><a href="../../custom-agents.html">Automation</a><a href="../../ai-enablement-workshop.html">AI Training</a><a href="../../case-studies.html">Work</a><a href="../../about.html">About</a><a class="btn sm" href="{CAL}">Book a call</a></nav></header>
<main>
<section class="hero"><div class="wrap">
<p class="eyebrow">{C["eyebrow"]}</p>
<h1><span class="l"><span>{C["h1"][0]}</span></span><span class="l"><span>{C["h1"][1]}</span></span><span class="l"><span><em>{C["h1"][2]}</em></span></span></h1>
<div class="hero-row"><div data-in><p>{C["lede"]}</p><div class="acts"><a class="btn" href="../../start-a-conversation.html">Book a free call</a><a class="link" href="../../case-studies.html">See our work</a></div></div>
<img class="hero-art" data-in src="assets/press-ink.webp" alt="An 18th-century printing press from Diderot's Encyclopedie" /></div>
{logos()}</div></section>
<section class="s"><div class="wrap s-head"><h2 data-in>Three services.<br><em>Take one, or all three.</em></h2><div>{services(lambda n,h,d,f: f'<a class="svc" href="{h}" data-in><h3>{n}</h3><div><p>{d}</p><small>First step: {f.lower()}</small></div></a>')}</div></div></section>
<section class="s"><div class="wrap s-head"><h2 data-in>For the teams that keep a business running.</h2><ul class="teams" data-in>{"".join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in C["teams"])}</ul></div></section>
<section class="s"><div class="wrap"><h2 data-in style="margin-bottom:40px">Real businesses, by name.</h2>
<a class="feature" href="../../impact-spark-labs.html" data-in><img src="../../assets/clients/spark-labs.svg" alt="spARK Labs by ARK Invest" /><div><p class="meta">spARK Labs by ARK Invest &middot; St. Petersburg</p><h3>Expense and event paperwork, handled with one command.</h3><p>Receipts become finished expense reports and event forms become review-ready PDFs, connected to the four tools the team already uses.</p></div></a>
<div class="list" style="margin-top:28px">{"".join(f'<a href="{h}"><b>{n}</b><span>{t}</span></a>' for n,t,h in C["work"])}</div></div></section>
<section class="s"><div class="wrap s-head"><h2 data-in>Questions owners ask us first.</h2>{faq()}</div></section>
<section class="closer"><div class="wrap"><h2>Tell us what your team does <em>by hand.</em></h2><p>Thirty minutes, free. We'll tell you which of the three fits, or that none does.</p><a class="btn" href="../../start-a-conversation.html">Book a free call</a></div></section>
</main><footer><div class="wrap"><span>altr &middot; Tampa, Florida</span><span><a href="../../learn.html">Learn</a><a href="../../about.html">About</a><a href="../../contact.html">Contact</a></span></div></footer>
{optbar("ledger")}{REVEAL}</body></html>'''

# ----------------------------------------------------------------- 2 SIGNAL
signal_css = '''
:root{--m:clamp(20px,5vw,72px);--bg:#0B0A09;--fg:#F4F1EA;--fg-2:#A8A29A;--fg-3:#77716A;--accent:#E07A3F;--rule:rgba(244,241,234,.12)}
body{background:var(--bg);color:var(--fg);font:400 16.5px/1.6 "Geist",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.mono{font-family:"Geist Mono",ui-monospace,monospace;font-size:13px;letter-spacing:.02em;color:var(--fg-3)}
nav.top{display:flex;align-items:center;gap:26px;height:68px;border-bottom:1px solid var(--rule)}nav.top .brand{font-weight:600;font-size:20px;letter-spacing:-.03em;margin-right:auto;text-decoration:none}
nav.top a{text-decoration:none;font-size:14px;color:var(--fg-2)}nav.top a:hover{color:var(--fg)}
.btn{display:inline-flex;align-items:center;gap:10px;min-height:46px;padding:0 20px;border-radius:8px;background:var(--fg);color:var(--bg)!important;font-weight:500;font-size:15px;text-decoration:none;transition:transform .15s}
.btn:active{transform:translateY(1px)}.btn.ghost{background:transparent;color:var(--fg)!important;border:1px solid var(--rule)}.btn.sm{min-height:36px;padding:0 14px;font-size:13.5px}
.hero{padding-block:clamp(90px,14vw,190px) 64px}
.hero h1{font-weight:500;font-size:clamp(3.2rem,9.4vw,9rem);line-height:.92;letter-spacing:-.055em}
.cycle{display:block;color:var(--fg-3)}.cycle .w{display:inline-grid;vertical-align:top;overflow:hidden;height:.96em;line-height:.96;color:var(--accent);padding-right:.05em}
.cycle .w span{grid-area:1/1;line-height:.96;transform:translateY(110%);transition:transform .7s cubic-bezier(.7,0,.2,1)}.cycle .w span.on{transform:none}.cycle .w span.out{transform:translateY(-110%)}
.hero p{max-width:40ch;margin-top:36px;font-size:clamp(1.1rem,1.5vw,1.3rem);color:var(--fg-2)}
.hero .acts{display:flex;gap:12px;margin-top:36px;flex-wrap:wrap}
.logos{display:flex;justify-content:space-between;align-items:center;gap:28px;flex-wrap:wrap;padding-block:30px;border-block:1px solid var(--rule)}
.logos img{height:28px;width:auto;filter:brightness(0) invert(1);opacity:.55}.logos .mono img{filter:none;opacity:.7}
section.s{padding-block:clamp(80px,11vw,150px)}
h2{font-weight:500;font-size:clamp(2.2rem,4.6vw,4rem);line-height:1;letter-spacing:-.045em;max-width:16ch}
.cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;margin-top:56px;background:var(--rule);border:1px solid var(--rule)}
.col{background:var(--bg);padding:32px 28px 30px;display:flex;flex-direction:column;gap:14px;text-decoration:none;transition:background .2s}.col:hover{background:#141210}
.col h3{font-weight:500;font-size:1.6rem;letter-spacing:-.03em}.col p{color:var(--fg-2)}.col small{margin-top:auto;padding-top:14px;color:var(--fg);font-size:14px}
.col .mono{color:var(--accent)}
.teams{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:24px;margin-top:56px}
.teams li{border-top:1px solid var(--fg-3);padding-top:16px}.teams b{display:block;font-weight:500;font-size:1.08rem}.teams span{display:block;color:var(--fg-2);font-size:14.5px;margin-top:6px}
.feature{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:1px;margin-top:56px;background:var(--rule);border:1px solid var(--rule);text-decoration:none}
.feature>div{background:var(--bg);padding:40px}.feature .mark{display:grid;place-items:center;min-height:300px}.feature .mark img{width:min(70%,300px)}
.feature h3{font-weight:500;font-size:2rem;letter-spacing:-.035em;line-height:1.05}.feature p{color:var(--fg-2);margin-top:14px}
.list{margin-top:28px}.list a{display:flex;justify-content:space-between;gap:24px;padding-block:18px;border-top:1px solid var(--rule);text-decoration:none;color:var(--fg-2)}.list a b{color:var(--fg);font-weight:500}.list a:hover b{color:var(--accent)}
.faq{margin-top:56px;max-width:860px}.faq details{border-top:1px solid var(--rule)}.faq details:last-child{border-bottom:1px solid var(--rule)}
.faq summary{display:flex;justify-content:space-between;gap:20px;padding-block:22px;cursor:pointer;list-style:none}.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font:400 20px/1 "Geist Mono",monospace;color:var(--accent)}.faq details[open] summary::after{content:"\\2212"}
.faq h3{font-weight:500;font-size:1.2rem;letter-spacing:-.02em}.faq p{padding-bottom:22px;color:var(--fg-2);max-width:62ch}
.closer{padding-block:clamp(110px,15vw,220px);border-top:1px solid var(--rule);text-align:left}
.closer h2{font-size:clamp(3rem,8vw,7.4rem);max-width:12ch}.closer p{color:var(--fg-2);margin-top:24px;font-size:1.15rem}.closer .acts{display:flex;gap:12px;margin-top:36px}
footer{border-top:1px solid var(--rule);padding-block:34px;font-size:14px;color:var(--fg-3)}footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px}footer a{color:var(--fg-2);text-decoration:none;margin-left:18px}
[data-in]{opacity:0;transform:translateY(16px);filter:blur(6px);transition:opacity .8s cubic-bezier(.16,1,.3,1),transform .8s cubic-bezier(.16,1,.3,1),filter .8s}[data-in].in{opacity:1;transform:none;filter:none}
@media (max-width:900px){.cols,.feature{grid-template-columns:1fr}.teams{grid-template-columns:1fr 1fr}nav.top a:not(.brand):not(.btn){display:none}}
'''
signal = head("Signal", "family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500", signal_css) + f'''
<header class="wrap"><nav class="top" aria-label="Primary"><a class="brand" href="signal.html">altr</a><a href="../../how-we-altr-work.html">AI Audit</a><a href="../../custom-agents.html">Automation</a><a href="../../ai-enablement-workshop.html">AI Training</a><a href="../../case-studies.html">Work</a><a href="../../about.html">About</a><a class="btn sm" href="{CAL}">Book a call</a></nav></header>
<main>
<section class="hero"><div class="wrap">
<p class="mono" data-in>{C["eyebrow"]}</p>
<h1 data-in>Do more with the team you have.<span class="cycle">We handle the <span class="w" aria-hidden="true"><span class="on">bills.</span><span>orders.</span><span>reports.</span><span>follow-ups.</span><span>scheduling.</span><span>inbox.</span></span></span></h1>
<p data-in>{C["lede"]}</p><div class="acts" data-in><a class="btn" href="../../start-a-conversation.html">Book a free call &rarr;</a><a class="btn ghost" href="../../case-studies.html">See our work</a></div>
</div></section>
<div class="wrap">{logos()}</div>
<section class="s"><div class="wrap"><h2 data-in>Three services. Take one, or all three.</h2>
<div class="cols" data-in>{services(lambda n,h,d,f: f'<a class="col" href="{h}"><span class="mono">{n.split()[0].lower() if n!="AI Audit" else "audit"}</span><h3>{n}</h3><p>{d}</p><small>First step: {f.lower()} &rarr;</small></a>')}</div></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>For the teams that keep a business running.</h2><ul class="teams" data-in>{"".join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in C["teams"])}</ul></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>Real businesses, by name.</h2>
<a class="feature" href="../../impact-spark-labs.html" data-in><div class="mark"><img src="../../assets/clients/spark-labs.svg" alt="spARK Labs by ARK Invest" /></div><div><p class="mono">spARK Labs by ARK Invest &middot; St. Petersburg</p><h3 style="margin-top:14px">Expense and event paperwork, handled with one command.</h3><p>Receipts become finished expense reports and event forms become review-ready PDFs, connected to the four tools the team already uses.</p></div></a>
<div class="list">{"".join(f'<a href="{h}"><b>{n}</b><span>{t}</span></a>' for n,t,h in C["work"])}</div></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>Questions owners ask us first.</h2>{faq()}</div></section>
<section class="closer"><div class="wrap"><h2 data-in>Tell us what your team does by hand.</h2><p>Thirty minutes, free. We'll tell you which of the three fits, or that none does.</p><div class="acts"><a class="btn" href="../../start-a-conversation.html">Book a free call &rarr;</a></div></div></section>
</main><footer><div class="wrap"><span>altr &middot; Tampa, Florida</span><span><a href="../../learn.html">Learn</a><a href="../../about.html">About</a><a href="../../contact.html">Contact</a></span></div></footer>
{optbar("signal")}{REVEAL}
<script>(()=>{{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const w=[...document.querySelectorAll('.cycle .w span')];let i=0;
setInterval(()=>{{const a=w[i];i=(i+1)%w.length;const b=w[i];a.classList.remove('on');a.classList.add('out');b.classList.remove('out');b.classList.add('on');setTimeout(()=>a.classList.remove('out'),750)}},2100)}})()</script></body></html>'''

# ----------------------------------------------------------------- 3 DESK
desk_css = '''
:root{--m:clamp(20px,5vw,72px);--bg:#121110;--panel:#1B1917;--panel-2:#22201D;--fg:#EFEBE4;--fg-2:#A9A39A;--fg-3:#7A746B;--accent:#D9884F;--ok:#8FB38A;--rule:rgba(239,235,228,.1)}
body{background:var(--bg);color:var(--fg);font:400 16.5px/1.6 "Geist",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
nav.top{display:flex;align-items:center;gap:26px;height:70px}nav.top .brand{font-weight:600;font-size:21px;letter-spacing:-.03em;margin-right:auto;text-decoration:none}
nav.top a{text-decoration:none;font-size:14px;color:var(--fg-2)}nav.top a:hover{color:var(--fg)}
.btn{display:inline-flex;align-items:center;min-height:46px;padding:0 20px;border-radius:10px;background:var(--fg);color:var(--bg)!important;font-weight:500;font-size:15px;text-decoration:none}
.btn.sm{min-height:36px;padding:0 14px;font-size:13.5px}.link{color:var(--fg);text-decoration:none;border-bottom:1px solid var(--fg-3)}
.hero{padding-block:clamp(60px,9vw,120px) 30px;text-align:center}
.hero .eyebrow{font-size:14px;color:var(--fg-3)}.hero h1{font-weight:500;font-size:clamp(2.8rem,7vw,6.2rem);line-height:.98;letter-spacing:-.05em;margin-top:18px}
.hero p{max-width:44ch;margin:24px auto 0;font-size:1.2rem;color:var(--fg-2)}.hero .acts{display:flex;gap:22px;align-items:center;justify-content:center;margin-top:30px;flex-wrap:wrap}
.stage{position:relative;margin:56px auto 0;width:min(980px,100%);padding:1px;border-radius:16px;background:linear-gradient(180deg,rgba(239,235,228,.22),rgba(239,235,228,.04))}
.app{border-radius:15px;background:var(--panel);overflow:hidden;box-shadow:0 40px 120px -40px rgba(217,136,79,.25)}
.app-top{display:flex;align-items:center;gap:10px;padding:14px 18px;border-bottom:1px solid var(--rule);font-size:13.5px;color:var(--fg-2)}
.app-top b{color:var(--fg);font-weight:500}.app-top .count{margin-left:auto;font-variant-numeric:tabular-nums}
.rows{position:relative;height:360px;overflow:hidden}
.row{position:absolute;left:0;right:0;display:grid;grid-template-columns:minmax(0,2.2fr) minmax(0,1.6fr) 110px 120px;gap:14px;align-items:center;padding:0 18px;height:60px;border-bottom:1px solid var(--rule);font-size:14.5px;transition:transform .7s cubic-bezier(.16,1,.3,1),opacity .5s}
.row .who{font-weight:500}.row .what{color:var(--fg-2)}.row .amt{text-align:right;font-variant-numeric:tabular-nums}
.chip{justify-self:end;font-size:12.5px;padding:4px 10px;border-radius:99px;border:1px solid var(--rule);color:var(--fg-2);transition:all .4s}
.chip.ok{color:var(--ok);border-color:rgba(143,179,138,.4);background:rgba(143,179,138,.08)}.chip.need{color:var(--accent);border-color:rgba(217,136,79,.5);background:rgba(217,136,79,.1)}
.logos{display:flex;justify-content:center;align-items:center;gap:56px;flex-wrap:wrap;padding-block:64px 20px}
.logos img{height:28px;width:auto;filter:brightness(0) invert(1);opacity:.5}.logos .mono img{filter:none;opacity:.7}
section.s{padding-block:clamp(80px,10vw,140px)}
h2{font-weight:500;font-size:clamp(2.2rem,4.4vw,3.8rem);line-height:1.02;letter-spacing:-.045em;text-align:center;max-width:18ch;margin-inline:auto}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:56px}
.card{display:flex;flex-direction:column;gap:12px;padding:28px;border-radius:14px;background:var(--panel);border:1px solid var(--rule);text-decoration:none;transition:border-color .2s,transform .2s}.card:hover{border-color:rgba(217,136,79,.5);transform:translateY(-2px)}
.card h3{font-weight:500;font-size:1.45rem;letter-spacing:-.03em}.card p{color:var(--fg-2)}.card small{margin-top:auto;padding-top:12px;font-size:14px}
.teams{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:40px}.teams li{padding:10px 18px;border-radius:99px;border:1px solid var(--rule);background:var(--panel)}.teams b{font-weight:500}.teams span{color:var(--fg-3);margin-left:8px;font-size:14px}
.feature{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:40px;align-items:center;margin-top:56px;padding:44px;border-radius:16px;background:var(--panel);border:1px solid var(--rule);text-decoration:none}
.feature img{width:min(80%,280px);margin-inline:auto}.feature h3{font-weight:500;font-size:1.9rem;letter-spacing:-.035em;line-height:1.08}.feature p{color:var(--fg-2);margin-top:12px}.feature .meta{font-size:14px;color:var(--fg-3);margin-bottom:10px}
.list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:16px}.list a{padding:22px;border-radius:14px;border:1px solid var(--rule);text-decoration:none}.list b{display:block;font-weight:500}.list span{display:block;color:var(--fg-2);font-size:14.5px;margin-top:6px}
.faq{max-width:780px;margin:48px auto 0}.faq details{border-top:1px solid var(--rule)}.faq details:last-child{border-bottom:1px solid var(--rule)}
.faq summary{display:flex;justify-content:space-between;gap:20px;padding-block:20px;cursor:pointer;list-style:none}.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--accent);font-size:22px;line-height:1}.faq details[open] summary::after{content:"\\2212"}.faq h3{font-weight:500;font-size:1.15rem}.faq p{padding-bottom:20px;color:var(--fg-2)}
.closer{padding-block:clamp(100px,13vw,180px);text-align:center}.closer h2{font-size:clamp(2.8rem,6.4vw,5.6rem)}.closer p{color:var(--fg-2);margin-top:20px;font-size:1.15rem}.closer .btn{margin-top:32px}
footer{border-top:1px solid var(--rule);padding-block:32px;font-size:14px;color:var(--fg-3)}footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px}footer a{color:var(--fg-2);text-decoration:none;margin-left:18px}
[data-in]{opacity:0;transform:translateY(18px);transition:opacity .8s cubic-bezier(.16,1,.3,1),transform .8s cubic-bezier(.16,1,.3,1)}[data-in].in{opacity:1;transform:none}
@media (max-width:860px){.cards,.feature,.list{grid-template-columns:1fr}.row{grid-template-columns:minmax(0,1.6fr) 90px 104px}.row .what{display:none}nav.top a:not(.brand):not(.btn){display:none}}
'''
desk = head("Desk", "family=Geist:wght@400;500;600", desk_css) + f'''
<header class="wrap"><nav class="top" aria-label="Primary"><a class="brand" href="desk.html">altr</a><a href="../../how-we-altr-work.html">AI Audit</a><a href="../../custom-agents.html">Automation</a><a href="../../ai-enablement-workshop.html">AI Training</a><a href="../../case-studies.html">Work</a><a href="../../about.html">About</a><a class="btn sm" href="{CAL}">Book a call</a></nav></header>
<main>
<section class="hero"><div class="wrap">
<p class="eyebrow" data-in>{C["eyebrow"]}</p><h1 data-in>Do more with the team you have.</h1><p data-in>{C["lede"]}</p>
<div class="acts" data-in><a class="btn" href="../../start-a-conversation.html">Book a free call</a><a class="link" href="../../case-studies.html">See our work</a></div>
<div class="stage" data-in aria-label="Example: this morning's paperwork, handled"><div class="app"><div class="app-top"><b>This morning</b><span>Bills, orders and forms</span><span class="count" id="count">0 handled &middot; 0 for you</span></div><div class="rows" id="rows"></div></div></div>
</div></section>
<div class="wrap">{logos()}</div>
<section class="s"><div class="wrap"><h2 data-in>Three services. Take one, or all three.</h2>
<div class="cards">{services(lambda n,h,d,f: f'<a class="card" href="{h}" data-in><h3>{n}</h3><p>{d}</p><small>First step: {f.lower()} &rarr;</small></a>')}</div></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>For the teams that keep a business running.</h2><ul class="teams" data-in>{"".join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in C["teams"])}</ul></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>Real businesses, by name.</h2>
<a class="feature" href="../../impact-spark-labs.html" data-in><img src="../../assets/clients/spark-labs.svg" alt="spARK Labs by ARK Invest" /><div><p class="meta">spARK Labs by ARK Invest &middot; St. Petersburg</p><h3>Expense and event paperwork, handled with one command.</h3><p>Receipts become finished expense reports and event forms become review-ready PDFs, connected to the four tools the team already uses.</p></div></a>
<div class="list">{"".join(f'<a href="{h}" data-in><b>{n}</b><span>{t}</span></a>' for n,t,h in C["work"])}</div></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>Questions owners ask us first.</h2>{faq()}</div></section>
<section class="closer"><div class="wrap"><h2 data-in>Tell us what your team does by hand.</h2><p>Thirty minutes, free. We'll tell you which of the three fits, or that none does.</p><a class="btn" href="../../start-a-conversation.html">Book a free call</a></div></section>
</main><footer><div class="wrap"><span>altr &middot; Tampa, Florida</span><span><a href="../../learn.html">Learn</a><a href="../../about.html">About</a><a href="../../contact.html">Contact</a></span></div></footer>
{optbar("desk")}{REVEAL}
<script>(()=>{{const items=[["Palmetto Lumber","Bill · job 2618 · framing","$3,412.80","ok"],["Pelican Homes","Order · 3 items at your prices","$1,968.00","ok"],["Brightwater Drywall","Bill · no PO number","$20,950.00","need"],
["Gulf Coast Electric","Bill · job 2604 · electrical","$7,180.00","ok"],["Bayside Property Co.","Insurance certificate · current","—","ok"],["Harbor Supply","Order · price below your list","$842.50","need"],["Coastal Signs","W-9 · received and checked","—","ok"],["Sunrise Plumbing","Bill · job 2621 · plumbing","$4,260.00","ok"]];
const box=document.getElementById('rows'),count=document.getElementById('count'),reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;let i=0,ok=0,need=0,shown=[];
function add(){{const [w,t,a,s]=items[i%items.length];i++;const r=document.createElement('div');r.className='row';r.innerHTML=`<span class="who">${{w}}</span><span class="what">${{t}}</span><span class="amt">${{a}}</span><span class="chip">Reading…</span>`;
r.style.transform='translateY(-60px)';r.style.opacity='0';box.prepend(r);shown.unshift(r);
requestAnimationFrame(()=>{{shown.forEach((el,k)=>{{el.style.transform=`translateY(${{k*60}}px)`;el.style.opacity=k>5?'0':'1'}})}});
setTimeout(()=>{{const c=r.querySelector('.chip');c.className='chip '+s;c.textContent=s==='ok'?'Handled':'Needs you';s==='ok'?ok++:need++;count.textContent=`${{ok}} handled · ${{need}} for you`}},reduced?0:1100);
if(shown.length>7)shown.pop().remove()}}
for(let k=0;k<(reduced?6:1);k++)add();if(!reduced)setInterval(add,1700)}})()</script></body></html>'''

# ----------------------------------------------------------------- 4 COLLAGE
collage_css = '''
:root{--m:clamp(20px,5vw,72px);--paper:#EFE7DA;--paper-2:#E5DBCA;--ink:#1D1915;--ink-2:#4F463C;--ink-3:#7B7064;--copper:#A2542A;--rule:rgba(29,25,21,.16)}
body{background:var(--paper);color:var(--ink);font:400 17px/1.6 "Geist",system-ui,sans-serif;-webkit-font-smoothing:antialiased;background-image:radial-gradient(rgba(29,25,21,.05) 1px,transparent 1px);background-size:5px 5px}
nav.top{display:flex;align-items:center;gap:26px;height:76px}nav.top .brand{font:600 italic 30px/1 "Fraunces",serif;margin-right:auto;text-decoration:none}
nav.top a{text-decoration:none;font-size:15px;color:var(--ink-2)}nav.top a:hover{color:var(--ink)}
.btn{display:inline-flex;align-items:center;min-height:50px;padding:0 22px;border-radius:4px;background:var(--ink);color:var(--paper)!important;font-weight:500;text-decoration:none;box-shadow:3px 3px 0 var(--copper);transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translate(-1px,-1px);box-shadow:4px 4px 0 var(--copper)}.btn.sm{min-height:40px;padding:0 16px;font-size:14.5px;box-shadow:2px 2px 0 var(--copper)}
.link{text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1px}
.hero{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,6fr);gap:40px;align-items:center;padding-block:40px 80px;min-height:min(820px,88vh)}
.hero h1{font:500 clamp(3.4rem,7.4vw,7rem)/.92 "Fraunces",serif;letter-spacing:-.035em;font-variation-settings:"SOFT" 50,"WONK" 1}
.hero h1 em{font-style:italic;color:var(--copper)}.hero p{max-width:34ch;margin-top:28px;font-size:1.2rem;color:var(--ink-2)}.hero .acts{display:flex;gap:22px;align-items:center;margin-top:32px;flex-wrap:wrap}
.eyebrow{font-size:14px;color:var(--ink-3);margin-bottom:22px}
.collage{position:relative;aspect-ratio:1/1.05;width:100%}
.piece{position:absolute;filter:drop-shadow(0 10px 14px rgba(29,25,21,.22)) drop-shadow(0 2px 2px rgba(29,25,21,.2));transition:transform 1.2s cubic-bezier(.16,1,.3,1),opacity .8s;will-change:transform}
.p1{left:2%;top:6%;width:66%;--r:-5deg}.p2{right:0;top:24%;width:52%;--r:4deg}.p3{left:14%;bottom:4%;width:44%;--r:-2deg}.p4{right:8%;bottom:0;width:36%;--r:7deg}
.note{position:absolute;right:20%;top:6%;width:30%;padding:14px 14px 18px;background:#F7E7A6;font:500 15px/1.35 "Caveat",cursive;font-size:22px;color:#3a2f14;transform:rotate(6deg);box-shadow:0 8px 14px rgba(29,25,21,.18)}
.tape{position:absolute;width:90px;height:26px;background:rgba(246,238,222,.75);box-shadow:0 1px 2px rgba(0,0,0,.08);z-index:3}
.piece{opacity:0;transform:translateY(40px) rotate(calc(var(--r) * 2))}.in .piece{opacity:1;transform:rotate(var(--r))}
.in .p2{transition-delay:.15s}.in .p3{transition-delay:.3s}.in .p4{transition-delay:.45s}
.logos{display:flex;justify-content:space-between;align-items:center;gap:28px;flex-wrap:wrap;padding-block:30px;border-block:1px dashed var(--rule)}
.logos img{height:30px;width:auto;filter:brightness(0);opacity:.6}.logos .mono img{filter:invert(1) brightness(0)}
section.s{padding-block:clamp(80px,10vw,140px)}
h2{font:500 clamp(2.4rem,4.8vw,4.2rem)/1 "Fraunces",serif;letter-spacing:-.03em;max-width:16ch}h2 em{font-style:italic;color:var(--copper)}
.slips{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin-top:56px}
.slip{display:flex;flex-direction:column;gap:12px;padding:28px 26px;background:#F8F3EA;text-decoration:none;box-shadow:0 12px 24px -12px rgba(29,25,21,.35);transform:rotate(var(--r,0deg));transition:transform .3s}
.slip:nth-child(1){--r:-1.2deg}.slip:nth-child(2){--r:.8deg}.slip:nth-child(3){--r:-.6deg}.slip:hover{transform:rotate(0) translateY(-4px)}
.slip h3{font:500 1.9rem/1 "Fraunces",serif}.slip p{color:var(--ink-2)}.slip small{margin-top:auto;padding-top:12px;font-size:15px;color:var(--copper)}
.teams{columns:2;column-gap:56px;margin-top:48px}.teams li{break-inside:avoid;padding-block:16px;border-bottom:1px dashed var(--rule)}.teams b{font:500 1.5rem/1.1 "Fraunces",serif;display:block}.teams span{color:var(--ink-2)}
.feature{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:44px;align-items:center;margin-top:56px;text-decoration:none}
.feature .card{display:grid;place-items:center;aspect-ratio:4/3;background:#1D1915;transform:rotate(-1.5deg);box-shadow:0 18px 30px -16px rgba(29,25,21,.5)}.feature .card img{width:62%}
.feature h3{font:500 2.2rem/1.05 "Fraunces",serif}.feature p{color:var(--ink-2);margin-top:14px}.feature .meta{font-size:14px;color:var(--ink-3);margin-bottom:10px}
.list{margin-top:36px}.list a{display:flex;justify-content:space-between;gap:20px;padding-block:18px;border-top:1px dashed var(--rule);text-decoration:none;color:var(--ink-2)}.list b{color:var(--ink);font-weight:500}.list a:hover b{color:var(--copper)}
.faq{margin-top:48px;max-width:820px}.faq details{border-top:1px dashed var(--rule)}.faq details:last-child{border-bottom:1px dashed var(--rule)}
.faq summary{display:flex;justify-content:space-between;gap:20px;padding-block:22px;cursor:pointer;list-style:none}.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font:500 1.8rem/1 "Fraunces",serif;color:var(--copper)}.faq details[open] summary::after{content:"\\2013"}.faq h3{font:500 1.45rem/1.2 "Fraunces",serif}.faq p{padding-bottom:22px;color:var(--ink-2)}
.closer{background:#1D1915;color:var(--paper);padding-block:clamp(100px,13vw,180px)}.closer h2{color:var(--paper);font-size:clamp(3rem,7vw,6.2rem)}.closer p{color:#CFC4B3;margin-top:22px;font-size:1.15rem}
.closer .btn{background:var(--paper);color:var(--ink)!important;margin-top:34px}
footer{background:#1D1915;color:#A79C8D;padding-block:34px;border-top:1px solid rgba(239,231,218,.12);font-size:14px}footer .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px}footer a{color:var(--paper);text-decoration:none;margin-left:18px}
[data-in]{opacity:0;transform:translateY(18px);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform .9s cubic-bezier(.16,1,.3,1)}[data-in].in{opacity:1;transform:none}
@media (max-width:860px){.hero,.slips,.feature{grid-template-columns:1fr}.teams{columns:1}nav.top a:not(.brand):not(.btn){display:none}}
'''
collage = head("Collage", "family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,400..600,0..100,0..1;1,9..144,400..600,0..100,0..1&family=Geist:wght@400;500&family=Caveat:wght@500", collage_css) + f'''
<header class="wrap"><nav class="top" aria-label="Primary"><a class="brand" href="collage.html">altr</a><a href="../../how-we-altr-work.html">AI Audit</a><a href="../../custom-agents.html">Automation</a><a href="../../ai-enablement-workshop.html">AI Training</a><a href="../../case-studies.html">Work</a><a href="../../about.html">About</a><a class="btn sm" href="{CAL}">Book a call</a></nav></header>
<main>
<div class="wrap"><section class="hero">
<div><p class="eyebrow" data-in>{C["eyebrow"]}</p><h1 data-in>Do more with the team <em>you have.</em></h1><p data-in>{C["lede"]}</p>
<div class="acts" data-in><a class="btn" href="../../start-a-conversation.html">Book a free call</a><a class="link" href="../../case-studies.html">See our work</a></div></div>
<div class="collage" data-in id="collage" aria-hidden="true">
<img class="piece p1" src="assets/frag-port.webp" alt="" data-depth="18" /><img class="piece p2" src="assets/frag-bridge.webp" alt="" data-depth="34" />
<img class="piece p3" src="assets/frag-workshop.webp" alt="" data-depth="10" /><img class="piece p4" src="assets/frag-basilica.webp" alt="" data-depth="46" />
<div class="note piece" style="--r:6deg" data-depth="60">Bills, orders, follow-ups: handled.</div></div>
</section></div>
<div class="wrap">{logos()}</div>
<section class="s"><div class="wrap"><h2 data-in>Three services. <em>Take one, or all three.</em></h2>
<div class="slips">{services(lambda n,h,d,f: f'<a class="slip" href="{h}" data-in><h3>{n}</h3><p>{d}</p><small>First step: {f.lower()} &rarr;</small></a>')}</div></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>For the teams that keep a business <em>running.</em></h2><ul class="teams" data-in>{"".join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in C["teams"])}</ul></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>Real businesses, <em>by name.</em></h2>
<a class="feature" href="../../impact-spark-labs.html" data-in><div class="card"><img src="../../assets/clients/spark-labs.svg" alt="spARK Labs by ARK Invest" /></div><div><p class="meta">spARK Labs by ARK Invest &middot; St. Petersburg</p><h3>Expense and event paperwork, handled with one command.</h3><p>Receipts become finished expense reports and event forms become review-ready PDFs, connected to the four tools the team already uses.</p></div></a>
<div class="list">{"".join(f'<a href="{h}"><b>{n}</b><span>{t}</span></a>' for n,t,h in C["work"])}</div></div></section>
<section class="s" style="padding-top:0"><div class="wrap"><h2 data-in>Questions owners <em>ask us first.</em></h2>{faq()}</div></section>
<section class="closer"><div class="wrap"><h2>Tell us what your team does <em>by hand.</em></h2><p>Thirty minutes, free. We'll tell you which of the three fits, or that none does.</p><a class="btn" href="../../start-a-conversation.html">Book a free call</a></div></section>
</main><footer><div class="wrap"><span>altr &middot; Tampa, Florida</span><span><a href="../../learn.html">Learn</a><a href="../../about.html">About</a><a href="../../contact.html">Contact</a></span></div></footer>
{optbar("collage")}{REVEAL}
<script>(()=>{{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const ps=[...document.querySelectorAll('#collage [data-depth]')];
addEventListener('scroll',()=>{{const y=Math.min(scrollY,700);ps.forEach(p=>p.style.translate=`0 ${{-y*p.dataset.depth/300}}px`)}},{{passive:true}})}})()</script></body></html>'''

for name, html in [("ledger", ledger), ("signal", signal), ("desk", desk), ("collage", collage)]:
    open(f"lab/home/{name}.html", "w", encoding="utf-8", newline="\n").write(html)
print("built 4 options")
