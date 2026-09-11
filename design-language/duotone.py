"""Download the chosen Encyclopedie plates and duotone them to altr's paper/ink."""
import io
import json
import os

import requests
from PIL import Image, ImageOps

API = 'https://commons.wikimedia.org/w/api.php'
H = {'User-Agent': 'altr-site-design/1.0 (alex.britton@drivelinebaseball.com)'}
ROOT = r'C:\Users\alex.britton\projects\altr\altr-site'
DEST = os.path.join(ROOT, 'assets', 'plates')
os.makedirs(DEST, exist_ok=True)

PICKS = {
    'plate-hero': ('File:Encyclopedie volume 8-156.png',
                   'Tailleur d\'Habits: a tailoring workshop with its bench, and the trade\'s tools drawn below.'),
    'plate-process': ('File:Encyclopedie volume 8-100.png',
                      'Serrurerie: one machine drawn three times, once for each stage of its operation.'),
    'plate-pattern': ('File:Encyclopedie volume 8-072.png',
                      'Serrurerie: a catalogue of forms, each one drawn to the same standard.'),
    'plate-shop': ('File:Encyclopedie volume 9-170.png',
                   'Tourneur: a turner\'s shop lit by one window, with the tools of the trade below.'),
    'plate-wide': ('File:Encyclopedie volume 8-030.png',
                   'Sellier-Carossier: a four-wheeled carriage drawn in elevation, with its parts separated out.'),
}

# duotone ramp: warm near-black in the lines, warm mid, paper white at the top
# so `mix-blend-mode: multiply` lets the page's paper show through untouched
STOPS = [(0.00, (36, 30, 24)), (0.45, (94, 74, 58)), (0.78, (198, 184, 166)), (1.00, (255, 255, 255))]


def ramp():
    lut = []
    for ch in range(3):
        for i in range(256):
            t = i / 255
            for (a, ca), (b, cb) in zip(STOPS, STOPS[1:]):
                if a <= t <= b:
                    f = (t - a) / (b - a)
                    lut.append(round(ca[ch] + (cb[ch] - ca[ch]) * f))
                    break
            else:
                lut.append(cb[ch])
    return lut


LUT = ramp()

titles = [v[0] for v in PICKS.values()]
r = requests.get(API, params={
    'action': 'query', 'format': 'json', 'titles': '|'.join(titles),
    'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata', 'iiurlwidth': 2000},
    headers=H, timeout=90)
info = {p['title']: p for p in r.json()['query']['pages'].values() if p.get('imageinfo')}
print(len(info), 'resolved', flush=True)

credits = []
for name, (title, caption) in PICKS.items():
    p = info.get(title)
    if not p:
        print('MISSING', title, flush=True)
        continue
    ii = p['imageinfo'][0]
    raw = requests.get(ii['thumburl'], headers=H, timeout=120).content
    im = Image.open(io.BytesIO(raw)).convert('L')
    im = ImageOps.autocontrast(im, cutoff=(0.6, 1.4))
    im = Image.merge('RGB', (im, im, im)).point(LUT)
    w = 1400
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(os.path.join(DEST, f'{name}.webp'), 'WEBP', quality=86, method=6)
    print(f'{name}.webp {im.size}', flush=True)
    em = ii.get('extmetadata', {})
    credits.append({
        'file': f'assets/plates/{name}.webp',
        'caption': caption,
        'source_title': title,
        'source_url': f"https://commons.wikimedia.org/wiki/{title.replace(' ', '_')}",
        'license': em.get('LicenseShortName', {}).get('value', 'Public domain'),
    })

json.dump(credits, open(os.path.join(DEST, 'credits.json'), 'w'), indent=1)
print('DONE', len(credits), flush=True)
