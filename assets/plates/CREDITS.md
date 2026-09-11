# Plate credits

Engraved plates from the *Encyclopedie, ou dictionnaire raisonne des sciences, des
arts et des metiers* (Diderot and d'Alembert, Paris, 1751-1772), scanned by
Wikimedia Commons. All are **public domain** - the works are centuries out of
copyright and the Commons scans carry a public domain mark.

Each file here is a duotone of the Commons scan, remapped to altr's paper and ink
and resized to 1400px wide. The originals are unaltered on Commons.

| File | Plate | Source |
|---|---|---|
| `plate-hero.webp` | Tailleur d'Habits - a tailoring workshop and the trade's tools | [Encyclopedie volume 8-156](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-156.png) |
| `plate-process.webp` | Serrurerie - one machine drawn once per stage of its operation | [Encyclopedie volume 8-100](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-100.png) |
| `plate-pattern.webp` | Serrurerie - a catalogue of forms, each drawn to the same standard | [Encyclopedie volume 8-072](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-072.png) |
| `plate-shop.webp` | Tourneur - a turner's shop lit by one window | [Encyclopedie volume 9-170](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_9-170.png) |
| `plate-wide.webp` | Sellier-Carossier - a carriage in elevation with its parts separated | [Encyclopedie volume 8-030](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-030.png) |

## Cutouts

Five alpha cutouts, one per page family, each taken from a line-art plate. Every
pixel lighter than the plate's own paper is transparent, so the drawing carries
no ground and sits directly on the page.

| File | Plate | Used on | Source |
|---|---|---|---|
| `cut-lathe.webp` | Tourneur - lathes and turning tools | Home | [Encyclopedie volume 9-198](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_9-198.png) |
| `cut-barrels.webp` | Tonnelier - casks, tubs and vessels | Non-profits | [Encyclopedie volume 9-142](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_9-142.png) |
| `cut-frames.webp` | Tabletier-Cornetier - saws and frames | Ecommerce | [Encyclopedie volume 8-128](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-128.png) |
| `cut-carriage.webp` | Sellier-Carossier - a carriage and its parts | Commercial real estate | [Encyclopedie volume 8-030](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-030.png) |
| `cut-machine.webp` | Serrurerie - a martinet, one stage of its operation | Law firms | [Encyclopedie volume 8-100](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-100.png) |

`bg-workshop.webp` and `bg-shop.webp` are the soft washes used behind the
argument sections. `plate-pattern.webp` supplies the six blog thumbnails.

## Why these

The Encyclopedie plates document how skilled work actually got done, one trade at
a time: the shop floor on top, the tools laid out beneath, every part labelled.
That is the same thing altr does with a workflow, which is why they belong here
rather than as decoration.

## Regenerating

`duotone.py` (kept with the session scratch files) pulls the named Commons files,
converts to greyscale, autocontrasts, and maps through a four-stop ramp from warm
near-black to paper white. Whites stay pure so `mix-blend-mode: multiply` lets the
page's paper show through untouched.
