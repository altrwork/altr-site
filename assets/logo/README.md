# Keycap marks

Four carved-stone renderings of the altr keycap, supplied by the client as
flat-backdrop product shots and cut out here.

| File | Stone | Reads on |
|---|---|---|
| `altr-key-marble.webp` | white marble, gold veining | **in use** - the only one that holds against the ink ground |
| `altr-key-sandstone.webp` | warm travertine | dark, slightly softer than the marble |
| `altr-key-serpentine.webp` | green serpentine | mid grounds |
| `altr-key-basalt.webp` | dark basalt | paper only; it disappears on ink |

Each is 512px wide, PNG and WebP, alpha-cut and trimmed to the cap.

## How the cut was made

Colour-distance keying fails on these: the marble cap against its cream
backdrop has almost no colour separation, and region-growing leaks through
the low-contrast edge into the cap. Tracing the contour does not work either: the span-based silhouette bulges
wherever the edge detector fires slightly outside the cap, which left a
ragged stepped halo around the mark.

What works is fitting the shape. The span-based silhouette gives an
unreliable contour but a reliable bounding box, and the cap is a rounded
rectangle, so the alpha is a rounded rect drawn into that box at 4x and
downsampled. Edges come out even, and a 2% inset keeps the feathered edge on
the cap rather than on the backdrop behind it.

The drop shadow is deliberately not kept. The house rule is one shadow, the
keycap press, and the mark is 84x56 in the nav where a shadow is mud.

## Sizing

The previous mark was a PNG with padding baked into the file, and four rules
zoomed it to 155-205% to crop that padding away. These cuts are trimmed to
the cap, so any zoom above 100% crops the cap itself. `.brand-mark` uses
`background-size: contain`. Keep it that way if you swap stones.
