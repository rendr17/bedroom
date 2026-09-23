"""Extract individual sprites from a composite asset sheet.

The sheets in assets/sheets/ are transparent-background composites. This tool
finds connected alpha regions (with a dilation pass so detached parts like
steam, cables, or sparkles stay with their sprite) and exports each region as
its own PNG. It also writes an annotated map (_map.png) with index numbers so
sprites can be identified and renamed into assets/ categories.

Usage:
    python tools/extract_sprites.py <sheet.png> <outdir> [--merge N] [--pad N]

    --merge N   dilation radius in px used to group nearby parts (default 14)
    --pad N     padding added around each cropped sprite (default 2)
"""

import argparse
import os
from collections import deque

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def label_components(mask: np.ndarray) -> tuple[np.ndarray, int]:
    """Two-pass connected-component labeling (4-connectivity)."""
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    parent = [0]  # union-find parent table; parent[i] for label i
    next_label = 0

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    for y in range(h):
        row = mask[y]
        prev_run = 0
        for x in range(w):
            if not row[x]:
                continue
            left = labels[y, x - 1] if x > 0 else 0
            up = labels[y - 1, x] if y > 0 else 0
            if left == 0 and up == 0:
                next_label += 1
                parent.append(next_label)
                labels[y, x] = next_label
            elif left != 0 and up == 0:
                labels[y, x] = left
            elif left == 0 and up != 0:
                labels[y, x] = up
            else:
                labels[y, x] = min(left, up)
                union(left, up)
            prev_run = x

    # second pass: flatten to root labels
    for y in range(h):
        for x in range(w):
            v = labels[y, x]
            if v:
                labels[y, x] = find(v)
    return labels, next_label


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet")
    ap.add_argument("outdir")
    ap.add_argument("--merge", type=int, default=14)
    ap.add_argument("--pad", type=int, default=2)
    ap.add_argument("--min-area", type=int, default=200)
    args = ap.parse_args()

    img = Image.open(args.sheet).convert("RGBA")
    alpha = np.array(img.split()[-1])
    mask = alpha > 8

    # dilate mask so detached parts merge with their sprite
    dil = Image.fromarray(mask).filter(
        ImageFilter.MaxFilter(args.merge * 2 + 1)
    )
    dilated = np.array(dil) > 0

    labels, _ = label_components(dilated)

    h, w = mask.shape
    boxes = []
    for lab in np.unique(labels):
        if lab == 0:
            continue
        comp = labels == lab
        # only keep components that contain real pixels (not just dilation)
        if not (comp & mask).any():
            continue
        ys, xs = np.where(comp & mask)
        area = len(ys)
        if area < args.min_area:
            continue
        y0, y1 = ys.min(), ys.max() + 1
        x0, x1 = xs.min(), xs.max() + 1
        boxes.append((x0, y0, x1, y1, area))

    # sort top-to-bottom, left-to-right (row-clustered)
    boxes.sort(key=lambda b: (b[1] // 200, b[0]))

    os.makedirs(args.outdir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(args.sheet))[0]
    annotated = img.copy()
    draw = ImageDraw.Draw(annotated)

    for i, (x0, y0, x1, y1, area) in enumerate(boxes):
        px0 = max(0, x0 - args.pad)
        py0 = max(0, y0 - args.pad)
        px1 = min(w, x1 + args.pad)
        py1 = min(h, y1 + args.pad)
        crop = img.crop((px0, py0, px1, py1))
        name = f"{i:03d}_x{px0}y{py0}_{px1 - px0}x{py1 - py0}.png"
        crop.save(os.path.join(args.outdir, name))
        draw.rectangle([x0, y0, x1 - 1, y1 - 1], outline=(255, 64, 64, 255), width=2)
        draw.text((x0 + 3, y0 + 3), str(i), fill=(255, 255, 0, 255))

    annotated.save(os.path.join(args.outdir, "_map.png"))
    print(f"{stem}: extracted {len(boxes)} sprites -> {args.outdir}")


if __name__ == "__main__":
    main()
