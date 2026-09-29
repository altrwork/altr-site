"""Render sketchbook header illustrations.

Run from the repo root:
    uv run --with playwright --with pillow python .claude/skills/sketch-header/header.py preview <slug> [...]
    uv run --with playwright --with pillow python .claude/skills/sketch-header/header.py export <slug> [...] | --all
    uv run --with playwright --with pillow python .claude/skills/sketch-header/header.py sheet
    python header.py standalone <drawing.svg> [out.svg]   (no dependencies, no browser)

preview/export/sheet need Playwright and Pillow and run inside the altr-site repo.
standalone works anywhere, including claude.ai: it writes one self-contained .svg
(style and font embedded) that opens in any browser.

preview -> design-language/headers/preview/<slug>.png (check it, never deployed)
export  -> assets/headers/<slug>.png (1200x630, link previews) and .webp (cards, page)
sheet   -> design-language/headers/preview/_sheet.png, every drawing at card size
"""
import asyncio, base64, html, io, pathlib, re, sys

SKILL = pathlib.Path(__file__).resolve().parent
ROOT = SKILL.parents[2]
SRC = ROOT / "design-language" / "headers" / "svgs"
PREVIEW = ROOT / "design-language" / "headers" / "preview"
OUT = ROOT / "assets" / "headers"
# embedded: a page opened with set_content may not load file:// fonts
FONT = "data:font/ttf;base64," + base64.b64encode((SKILL / "fonts" / "Kalam-Bold.ttf").read_bytes()).decode()
DEFS = ('<defs><filter id="rough" x="-5%" y="-5%" width="110%" height="110%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7"/>'
        '<feDisplacementMap in="SourceGraphic" scale="4"/></filter></defs>')


def svg(slug, raw=None):
    raw = raw if raw is not None else (SRC / f"{slug}.svg").read_text(encoding="utf-8")
    m = re.search(r"<!--\s*title:\s*(.*?)\s*-->", raw)
    if not m:
        sys.exit(f"{slug}.svg has no <!-- title: ... --> comment")
    title = html.escape(m.group(1))
    body = re.sub(r"<!--.*?-->", "", raw, flags=re.S).strip()
    return (f'<svg class="hdr" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">'
            f'{DEFS}<rect class="bg" width="1200" height="630"/><text class="ttl" x="600" y="118">{title}</text>'
            f'<g class="art">{body}</g></svg>')


def page(inner, extra_css=""):
    css = (SKILL / "sketch.css").read_text(encoding="utf-8")
    return (f'<html><head><style>@font-face{{font-family:"Kalam";src:url("{FONT}");font-weight:700}}'
            f'body{{margin:0}} {css} {extra_css}</style></head><body>{inner}</body></html>')


async def shoot(pg, doc, path, full=False):
    await pg.set_content(doc, wait_until="load")
    await pg.evaluate("document.fonts.ready")
    await pg.screenshot(path=str(path), full_page=full)


def standalone(src, out):
    """One self-contained SVG: style and font inlined, nothing to install."""
    css = (SKILL / "sketch.css").read_text(encoding="utf-8")
    style = f'<style>@font-face{{font-family:"Kalam";src:url("{FONT}");font-weight:700}} {css}</style>'
    doc = svg(src.stem, src.read_text(encoding="utf-8")).replace("<defs>", f"<defs>{style}", 1)
    out.write_text(doc, encoding="utf-8")
    print(out)


async def main(cmd, slugs):
    from playwright.async_api import async_playwright
    from PIL import Image
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1200, "height": 630})
        if cmd == "sheet":
            PREVIEW.mkdir(parents=True, exist_ok=True)
            cells = "".join(f"<div>{svg(s)}<p>{s}</p></div>" for s in slugs)
            grid = ".g{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:10px;background:#999;font:12px sans-serif} svg{width:100%;display:block} p{margin:3px 0}"
            await pg.set_viewport_size({"width": 1600, "height": 900})
            await shoot(pg, page(f'<div class="g">{cells}</div>', grid), PREVIEW / "_sheet.png", full=True)
            print(PREVIEW / "_sheet.png")
        for s in slugs if cmd != "sheet" else []:
            doc = page(svg(s), "svg{display:block;width:1200px;height:630px}")
            if cmd == "preview":
                PREVIEW.mkdir(parents=True, exist_ok=True)
                await shoot(pg, doc, PREVIEW / f"{s}.png"); print(PREVIEW / f"{s}.png")
            else:
                OUT.mkdir(parents=True, exist_ok=True)
                await pg.set_content(doc, wait_until="load"); await pg.evaluate("document.fonts.ready")
                img = Image.open(io.BytesIO(await pg.screenshot())).convert("RGB")
                img.save(OUT / f"{s}.png", optimize=True)
                img.save(OUT / f"{s}.webp", quality=88, method=6)
                print(OUT / f"{s}.png", "+ .webp")
        await b.close()


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("preview", "export", "sheet", "standalone"):
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "standalone":
        if not args:
            sys.exit("name the drawing file")
        src = pathlib.Path(args[0])
        standalone(src, pathlib.Path(args[1]) if len(args) > 1 else src.with_name(src.stem + "-header.svg"))
        sys.exit()
    if cmd == "sheet" or args == ["--all"]:
        args = sorted(p.stem for p in SRC.glob("*.svg"))
    if not args:
        sys.exit("name at least one slug, or --all")
    asyncio.run(main(cmd, args))
