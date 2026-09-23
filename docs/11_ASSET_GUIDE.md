# Asset Guide

## Source art

All production art comes from the pixel-asset pack in `assets/sheets/` — seven
composite, transparent-background sprite sheets:

| Sheet | Contents |
| --- | --- |
| `01-room-assets.png` | room modules: wall segment, CRT, window, bed, desk, drawers, shelf, bookshelf, sign |
| `02-ui-kit.png` | title bars, windows, scrollbars, quest log, dialogue box, buttons, tabs, badges, taskbar |
| `03-icon-sprite-sheet.png` | folders, document, image, link, camera, gamepad, floppy, CD, speakers, clock, plant, cat, star, cursor, window controls, alert bubble, quest scroll |
| `04-desk-essentials.png` | lamp, mug, notebook, pencil, phone, gameboy, floppies, walkman, camera, mouse, keyboard, speakers, book stack |
| `05-room-props.png` | cat, plant, clock, figures, book stacks, polaroids, sticky notes, map, framed art, gadgets, posters |
| `06-decor-sticker-sheet.png` | posters, sticky notes, polaroids, clock, labeled books, nav labels |
| `07-character-and-game-ui.png` | avatar expressions, cursors, markers, checkboxes, speech bubbles, dialogue UI |

Art direction: retro bedroom adventure, early-2000s PC game/web aesthetic,
pixelated, warm navy/blue + orange accent palette.

## Extracting sprites

The sheets are composite sources — crop/export the pieces you need.

- `python tools/extract_sprites.py assets/sheets/<sheet>.png <outdir>` detects
  sprites automatically (connected alpha regions) and writes numbered PNGs plus
  an annotated `_map.png` for identification. Tune with `--merge`/`--pad`.
- `python tools/build_assets.py` rebuilds the current exported set (crops +
  composed `backgrounds/bedroom-night.png`) and regenerates
  `ASSET_MANIFEST.json`. Update its mapping tables when adding new exports.
- Exported pieces land in `assets/<category>/` and are mirrored to
  `app/public/assets/` (sheets stay out of `public/` — they are source
  material, not runtime files).

## Included exports

### Backgrounds
- `bedroom-night.png` (composed from sheet-01 room modules + sheet-05 props)

### Navigation icons
- about, projects, experience, skills, contact, extras (gamepad)

### System/UI icons
- close, quest, info, warning, sound, muted, arrow (cursor), hotspot marker

### Props
- mug, floppy, notebook, gamepad, envelope, folder, gear, books,
  avatar-placeholder

### Posters
- small developer / bigger tomorrow
- better web / brighter tomorrow
- good code / better days
- build / learn / improve / repeat

### Audio
Original minimal WAV UI cues: startup, click, open, success.

## Production recommendations
- PNG for exported sprites; WebP/AVIF variants when optimizing for launch.
- Keep room background under ~500–800 KB where possible.
- Use responsive `<picture>` sizes.
- Lazy-load project screenshots.

## Naming convention
`category-purpose-state.ext`
Examples:
- `icon-projects-active.png`
- `prop-notebook.png`
- `poster-better-web.png`
- `bg-bedroom-night.webp`

## User-specific assets not generated here
A portrait intended to resemble the user should be created only from a current
reference image. The included avatar is a neutral placeholder, not a likeness.
