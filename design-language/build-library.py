"""Build a picker: every processed plate, plus the candidate pool to choose from."""
import io
import os
from concurrent.futures import ThreadPoolExecutor

import requests
from PIL import Image

API = 'https://commons.wikimedia.org/w/api.php'
H = {'User-Agent': 'altr-site-design/1.0 (alex.britton@drivelinebaseball.com)'}
ROOT = r'C:\Users\alex.britton\projects\altr\altr-site'
CAND = os.path.join(ROOT, '.firecrawl', 'candidates')
os.makedirs(CAND, exist_ok=True)

# plate id -> what it shows. Only entries verified by eye on the contact sheets.
CANDIDATES = [
    ('1-196', 'Architecture', 'Column order, drawn and dimensioned'),
    ('1-199', 'Architecture', 'Rusticated stone piers and bases'),
    ('1-202', 'Architecture', 'Window bays with entablature'),
    ('1-205', 'Architecture', 'Six window and door surrounds'),
    ('1-208', 'Architecture', 'Public fountain: elevation and plan'),
    ('1-211', 'Architecture', 'First-floor plan of a royal library'),
    ('1-214', 'Architecture', 'Elevation of the Bibliotheque Royale'),
    ('1-217', 'Architecture', 'Ground-floor plan of a large hotel'),
    ('1-220', 'Architecture', 'Plan of a private house'),
    ('1-223', 'Architecture', 'Interior elevation of a gallery'),
    ('1-226', 'Architecture', 'Interior wall elevations'),
    ('1-229', 'Architecture', 'Room plan, walls in solid black'),
    ('1-232', 'Architecture', 'Staircase in section and plan'),
    ('1-235', 'Coupe des Pierres', 'Stone-cutting setting-out, gothic arch'),
    ('1-238', 'Coupe des Pierres', 'Arch geometry, struck with lines'),
    ('1-241', 'Architecture', 'Moving stone in a workshop'),
    ('1-244', 'Maconnerie', 'Brick coursing and wall sections'),
    ('1-247', 'Maconnerie', 'Foundation piers and a hoist wheel'),
    ('1-250', 'Maconnerie', 'Well shafts and chimney sections'),
    ('1-253', 'Maconnerie', 'Mason tools and roof truss forms'),
    ('1-256', 'Maconnerie', 'A plaster quarry, with tools below'),
    ('1-259', 'Architecture', 'Vaults, arches and their sections'),
    ('1-064', 'Machine', 'A large geared machine in perspective'),
    ('1-075', 'Machine', 'Machine in a masonry housing'),
    ('1-086', 'Jardinage', 'Formal garden parterre, in plan'),
    ('1-108', 'Laboratory', 'A workshop interior with apparatus'),
    ('8-030', 'Sellier-Carossier', 'A carriage, whole and in parts'),
    ('8-072', 'Serrurerie', 'Catalogue of identical hardware forms'),
    ('8-100', 'Serrurerie', 'One machine drawn once per stage'),
    ('8-128', 'Tabletier', 'Saws and frames'),
    ('8-156', "Tailleur d'Habits", 'A tailoring workshop and its tools'),
    ('8-198', 'Tanneur', 'A tannery in elevation'),
    ('9-114', 'Machines de Theatre', 'Roof truss and stage machinery'),
    ('9-142', 'Tonnelier', 'Casks, tubs and vessels'),
    ('9-170', 'Tourneur', "A turner's shop lit by one window"),
    ('9-198', 'Tourneur', 'Lathes and turning tools'),
]

titles = [f'File:Encyclopedie volume {c[0]}.png' for c in CANDIDATES]
pages = {}
for i in range(0, len(titles), 45):
    r = requests.get(API, params={
        'action': 'query', 'format': 'json', 'titles': '|'.join(titles[i:i + 45]),
        'prop': 'imageinfo', 'iiprop': 'url', 'iiurlwidth': 620},
        headers=H, timeout=90)
    for p in r.json()['query']['pages'].values():
        if p.get('imageinfo'):
            pages[p['title']] = p['imageinfo'][0]['thumburl']
print(len(pages), 'candidate thumbs resolved', flush=True)


def grab(item):
    pid, trade, desc = item
    t = f'File:Encyclopedie volume {pid}.png'
    if t not in pages:
        return None
    out = os.path.join(CAND, f'{pid}.webp')
    if not os.path.exists(out):
        try:
            im = Image.open(io.BytesIO(requests.get(pages[t], headers=H, timeout=60).content))
            im.convert('RGB').save(out, 'WEBP', quality=82, method=4)
        except Exception:
            return None
    return item


with ThreadPoolExecutor(10) as ex:
    got = [g for g in ex.map(grab, CANDIDATES) if g]
print(len(got), 'saved', flush=True)

PROCESSED = [
    ('wash-facade.webp', 'Wash', 'Bibliotheque Royale elevation', 'Home hero - live'),
    ('wash-brick.webp', 'Wash', 'Brick coursing and wall sections', 'Home closing band - live'),
    ('wash-quarry.webp', 'Wash', 'Plaster quarry', 'staged, unused'),
    ('wash-workshop.webp', 'Wash', 'Tailoring workshop', 'previous hero'),
    ('bg-shop.webp', 'Wash', "Turner's shop", 'closing bands sitewide'),
    ('bg-workshop.webp', 'Wash', 'Tailoring workshop, soft', 'superseded'),
    ('cut-plan.webp', 'Cutout', 'Hotel ground-floor plan', 'Commercial real estate - live'),
    ('cut-vault.webp', 'Cutout', 'Vaults and arches', 'Non-profits - live'),
    ('cut-window.webp', 'Cutout', 'Window and door bays', 'Ecommerce - live'),
    ('cut-stone.webp', 'Cutout', 'Stone-cutting setting-out', 'Law firms - live'),
    ('cut-lathe.webp', 'Cutout', 'Lathes and turning tools', 'available'),
    ('cut-barrels.webp', 'Cutout', 'Casks, tubs and vessels', 'available'),
    ('cut-frames.webp', 'Cutout', 'Saws and frames', 'available'),
    ('cut-carriage.webp', 'Cutout', 'A carriage and its parts', 'available'),
    ('cut-machine.webp', 'Cutout', 'A martinet machine', 'available'),
    ('plate-pattern.webp', 'Texture', 'Catalogue of hardware forms', 'blog thumbnails'),
    ('plate-hero.webp', 'Plate', 'Tailoring workshop, full plate', 'available'),
    ('plate-process.webp', 'Plate', 'One machine, three stages', 'available'),
    ('plate-shop.webp', 'Plate', "Turner's shop, full plate", 'available'),
    ('plate-wide.webp', 'Plate', 'Carriage in elevation', 'available'),
]

rows_p = '\n'.join(
    f'''    <figure class="card {'cut' if k == 'Cutout' else 'flat'}">
      <div class="thumb"><img src="../assets/plates/{f}" alt="{d}" loading="lazy"></div>
      <figcaption><span class="k">{k}</span><b>{d}</b><span class="u">{u}</span>
      <code>{f}</code></figcaption>
    </figure>'''
    for f, k, d, u in PROCESSED if os.path.exists(os.path.join(ROOT, 'assets', 'plates', f)))

rows_c = '\n'.join(
    f'''    <figure class="card flat">
      <div class="thumb"><img src="../.firecrawl/candidates/{pid}.webp" alt="{desc}" loading="lazy"></div>
      <figcaption><span class="k">{trade}</span><b>{desc}</b><code>volume {pid}</code></figcaption>
    </figure>'''
    for pid, trade, desc in got)

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>altr plate library</title>
<link rel="stylesheet" href="../styles.css?v=20260906b">
<link rel="stylesheet" href="../redesign.css?v=20260911a">
<style>
  .lib {{ max-width: 1500px; margin: 0 auto; padding: 40px clamp(20px,4vw,44px) 80px; }}
  .lib h1 {{ max-width: none; margin: 0 0 10px; font-size: clamp(2rem,3.4vw,3rem); }}
  .lib .lede {{ max-width: 70ch; color: var(--bone-soft); margin: 0 0 8px; }}
  .lib h2 {{ max-width: none; margin: 56px 0 6px; font-size: 1.5rem;
             padding-top: 20px; border-top: 1px solid var(--rule-ink); }}
  .lib h2 + p {{ max-width: 70ch; color: var(--bone-dim); margin: 0 0 26px; font-size: 15px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
           border-top: 1px solid var(--rule-ink); border-left: 1px solid var(--rule); }}
  .card {{ margin: 0; padding: 16px 16px 18px;
           border-right: 1px solid var(--rule); border-bottom: 1px solid var(--rule); }}
  .thumb {{ height: 230px; display: flex; align-items: center; justify-content: center;
            overflow: hidden; }}
  .card.flat .thumb {{ background: #fff; border: 1px solid var(--rule); }}
  .thumb img {{ max-width: 100%; max-height: 100%; object-fit: contain; display: block; }}
  figcaption {{ display: grid; gap: 3px; margin-top: 12px; }}
  .k {{ font-family: var(--mono); font-size: 10px; letter-spacing: .14em;
        text-transform: uppercase; color: var(--copper); }}
  figcaption b {{ font-weight: 500; font-size: 14px; line-height: 1.25; }}
  .u {{ font-size: 12px; color: var(--bone-dim); }}
  figcaption code {{ font-family: var(--mono); font-size: 10px; color: var(--bone-dim); }}
</style>
</head>
<body>
<div class="site-shell"><main class="lib">
  <h1>Plate library</h1>
  <p class="lede">Everything available, and everything that could be. Tell me a
  file name or a volume number and I will put it where you want it.</p>

  <h2>Processed and ready</h2>
  <p>Already cut, levelled and sized. Cutouts sit on the page ground with no
  box; washes go behind type; textures tile or crop.</p>
  <div class="grid">
{rows_p}
  </div>

  <h2>Candidates</h2>
  <p>Raw plates from the Encyclopedie, not yet processed. Any of these can
  become a wash or a cutout in a few minutes. Architecture and masonry first,
  then the trades.</p>
  <div class="grid">
{rows_c}
  </div>
</main></div>
</body>
</html>
'''
open(os.path.join(ROOT, 'design-language', 'plate-library.html'), 'w', encoding='utf-8').write(html)
print('WROTE design-language/plate-library.html', flush=True)
