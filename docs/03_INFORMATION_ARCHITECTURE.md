# Information Architecture & Sitemap

```text
/
├── /about
├── /projects
│   ├── /projects/antero
│   ├── /projects/jejakbahari
│   ├── /projects/quick-order
│   └── /projects/dock-disorder
├── /experience
├── /skills
├── /contact
├── /extras
└── /404
```

## Navigation model
The bedroom is the experiential navigation layer; URLs remain conventional.

### Desktop
- Hotspot click opens content panel/window and updates URL.
- Bottom navigation is always visible or one click away.
- Browser Back/Forward reflects route history.

### Mobile
- Room becomes a vertically composed scene with large hotspot buttons.
- Section content opens as full-page panels.
- No draggable windows.

## URL behavior
- `/` = room.
- `/projects/antero` can be loaded directly and should render the room shell + Antero panel, or a full accessible article when JS is unavailable.
- Deep links must never require boot animation before content appears.
