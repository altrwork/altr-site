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

## Architecture set

The working set, chosen so the drawing argues what the page argues. The plan is
in [../design-language/IMAGERY.md](../design-language/IMAGERY.md).

### Washes (behind type)

| File | Plate | Used on | Source |
|---|---|---|---|
| `wash-facade.webp` | Architecture - elevation of the Bibliotheque Royale, one bay repeated | Home hero | [volume 1-214](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-214.png) |
| `wash-brick.webp` | Architecture, Maconnerie - brick coursing and wall sections | Home closing band | [volume 1-244](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-244.png) |
| `wash-quarry.webp` | Architecture, Maconnerie - a plaster quarry | staged, unused | [volume 1-256](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-256.png) |
| `bg-shop.webp` | Tourneur - a turner's shop lit by one window | closing bands sitewide | [volume 9-170](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_9-170.png) |

### Cutouts (beside the copy)

Alpha-cut: every pixel lighter than the plate's own paper is transparent, so the
drawing carries no ground.

| File | Plate | Used on | Source |
|---|---|---|---|
| `cut-plan.webp` | Architecture - ground-floor plan of a large hotel | Commercial real estate | [volume 1-217](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-217.png) |
| `cut-vault.webp` | Architecture - vaults, arches and their sections | Non-profits | [volume 1-259](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-259.png) |
| `cut-window.webp` | Architecture - window and door bays with entablature | Ecommerce | [volume 1-202](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-202.png) |
| `cut-stone.webp` | Architecture, Coupe des Pierres - stone-cutting setting-out | Law firms | [volume 1-235](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_1-235.png) |

### Trade set (earlier, still on disk)

`cut-lathe`, `cut-barrels`, `cut-frames`, `cut-carriage`, `cut-machine`,
`plate-hero`, `plate-process`, `plate-shop`, `plate-wide`, `wash-workshop`,
`bg-workshop`. Sources for these are listed in the table at the top.
`plate-pattern.webp` ([volume 8-072](https://commons.wikimedia.org/wiki/File:Encyclopedie_volume_8-072.png))
supplies the six blog thumbnails.

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
