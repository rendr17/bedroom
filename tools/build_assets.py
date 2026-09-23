"""Build the assets/ tree from the composite sheets.

Crops semantic sprites out of assets/sheets/*.png into assets/<category>/,
composes backgrounds/bedroom-night.png from the sheet-01 room modules, and
regenerates ASSET_MANIFEST.json. Re-run any time the source sheets change.

Usage:
    python tools/build_assets.py
"""

import json
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHEETS = os.path.join(ROOT, "assets", "sheets")
EXTRACTED = os.path.join(ROOT, "tools", "_extracted")
OUT = os.path.join(ROOT, "assets")

# filename stems of extracted sprites, per sheet
E = {
    "01": os.path.join(EXTRACTED, "01-room-assets"),
    "02": os.path.join(EXTRACTED, "02-ui-kit"),
    "03": os.path.join(EXTRACTED, "03-icon-sprite-sheet"),
    "04": os.path.join(EXTRACTED, "04-desk-essentials"),
    "05": os.path.join(EXTRACTED, "05-room-props"),
    "06": os.path.join(EXTRACTED, "06-decor-sticker-sheet"),
    "07": os.path.join(EXTRACTED, "07-character-and-game-ui"),
}


def sheet(num):
    return Image.open(os.path.join(SHEETS, os.listdir(SHEETS)[0])).convert("RGBA")


def load_sheet(name):
    return Image.open(os.path.join(SHEETS, name)).convert("RGBA")


def extracted(num, stem):
    path = os.path.join(E[num], stem + ".png")
    return Image.open(path).convert("RGBA")


def save(img, rel):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print(" ", rel, img.size)


def trim(img):
    """Trim fully-transparent borders."""
    bbox = img.split()[-1].getbbox()
    return img.crop(bbox) if bbox else img


# ---------------------------------------------------------------- icons
ICON_COPIES = {
    # nav — sheet 03
    "icons/nav/about.png": ("03", "001_x305y53_216x231"),
    "icons/nav/projects.png": ("03", "006_x268y333_214x180"),
    "icons/nav/experience.png": ("03", "002_x582y64_249x220"),
    "icons/nav/skills.png": ("03", "003_x877y60_230x231"),
    "icons/nav/contact.png": ("03", "004_x1164y93_252x181"),
    "icons/nav/extras.png": ("03", "011_x21y577_240x156"),
    # system — sheet 03
    "icons/system/arrow.png": ("03", "021_x710y809_98x137"),
    "icons/system/muted.png": ("03", "015_x1000y569_170x164"),
    "icons/system/quest.png": ("03", "024_x970y919_164x151"),
    "icons/system/sound.png": ("03", "014_x759y569_195x159"),
    # system — sheet 07
    "icons/system/hotspot.png": ("07", "006_x1013y309_115x133"),
    "icons/system/info.png": ("07", "008_x1290y308_127x130"),
}

POSTER_COPIES = {
    "posters/small-developer.png": ("06", "000_x46y60_353x437"),
    "posters/better-web.png": ("06", "001_x419y60_336x437"),
    "posters/good-code.png": ("06", "003_x1136y106_270x347"),
    "posters/build-repeat.png": ("06", "006_x850y500_184x349"),
}

PROP_COPIES = {
    "props/books.png": ("04", "012_x1082y838_346x215"),
    "props/envelope.png": ("03", "004_x1164y93_252x181"),
    "props/floppy.png": ("03", "012_x287y552_188x181"),
    "props/folder.png": ("03", "000_x31y72_227x210"),
    "props/gamepad.png": ("03", "011_x21y577_240x156"),
    "props/gear.png": ("03", "003_x877y60_230x231"),
    "props/mug.png": ("04", "001_x347y124_238x335"),
    "props/notebook.png": ("04", "002_x638y163_332x298"),
    "props/avatar-placeholder.png": ("07", "000_x20y54_325x388"),
}


def main():
    print("copies:")
    for rel, (num, stem) in {
        **ICON_COPIES,
        **POSTER_COPIES,
        **PROP_COPIES,
    }.items():
        save(extracted(num, stem), rel)

    print("manual crops:")
    s03 = load_sheet("03-icon-sprite-sheet.png")
    s07 = load_sheet("07-character-and-game-ui.png")
    s02 = load_sheet("02-ui-kit.png")

    # close button = rightmost of the 3-button window-controls strip
    save(trim(s03.crop((1125, 797, 1240, 908))), "icons/system/close.png")

    # warning = red "!" marker without its "Active" label
    marker = s07.crop((1263, 478, 1407, 595))
    save(trim(marker), "icons/system/warning.png")

    # retro window frame (generic window with scrollbar)
    save(trim(s02.crop((388, 140, 895, 515))), "ui/retro-window.png")

    print("compose bedroom-night:")
    compose_room()

    print("manifest:")
    write_manifest()


def compose_room():
    s01 = load_sheet("01-room-assets.png")
    s05 = load_sheet("05-room-props.png")

    wall_art = s01.crop((22, 64, 625, 499))        # wall segment w/ posters+corkboard
    crt = s01.crop((652, 93, 1061, 442))           # CRT monitor
    window = s01.crop((1091, 28, 1421, 462))       # night city window
    bed = s01.crop((20, 526, 385, 915))            # bed
    frame = s01.crop((665, 463, 1031, 718))        # framed landscape
    desk = s01.crop((395, 720, 1060, 910))         # desk table
    shelf = s01.crop((1104, 474, 1428, 940))       # bookshelf
    drawers = s01.crop((442, 958, 1070, 1046))     # drawer unit
    plate = s01.crop((1107, 956, 1414, 1061))      # blue room sign

    cat = s05.crop((26, 56, 416, 280))             # sleeping cat
    plant = s05.crop((416, 26, 666, 296))          # pothos plant
    clock = s05.crop((681, 121, 976, 266))         # digital clock

    W, H = 1600, 900
    FLOOR_Y = 620
    img = Image.new("RGBA", (W, H))
    px = img.load()
    for y in range(H):
        for x in range(W):
            if y < FLOOR_Y:
                px[x, y] = (43, 55, 88, 255)       # navy wall
            else:
                px[x, y] = (26, 33, 56, 255)       # darker floor
    # baseboard line
    for y in range(FLOOR_Y, FLOOR_Y + 6):
        for x in range(W):
            px[x, y] = (17, 22, 40, 255)

    def place(im, x, y, scale=1.0):
        if scale != 1.0:
            im = im.resize(
                (round(im.width * scale), round(im.height * scale)),
                Image.NEAREST,
            )
        img.alpha_composite(im, (x, y))

    place(wall_art, 30, 40)
    place(frame, 730, 95)
    place(window, 1130, 30)
    place(shelf, 1245, 505, 0.75)
    place(bed, 55, 500)
    place(cat, 185, 555, 0.5)
    place(plant, 330, 585, 0.75)
    place(desk, 430, 680)
    place(drawers, 620, 795)
    place(crt, 560, 370)
    place(clock, 920, 600, 0.8)

    save(img.convert("RGB"), "backgrounds/bedroom-night.png")


def write_manifest():
    entries = []
    for dirpath, _dirs, files in os.walk(OUT):
        for f in sorted(files):
            if f == "ASSET_MANIFEST.json":
                continue
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            entries.append({"path": rel, "bytes": os.path.getsize(full)})
    entries.sort(key=lambda e: e["path"])
    with open(os.path.join(OUT, "ASSET_MANIFEST.json"), "w") as fh:
        json.dump(entries, fh, indent=2)
        fh.write("\n")
    print(f"  {len(entries)} entries")


if __name__ == "__main__":
    main()
