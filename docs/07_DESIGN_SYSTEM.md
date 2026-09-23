# Design System

## Direction
Retro Bedroom Adventure: cozy physical room + early-2000s digital UI + pixel-game framing.

## Palette
```css
--bg-deep: #0f172a;
--surface: #1f2937;
--primary: #1e4a94;
--secondary: #4a90e2;
--accent: #ffd166;
--warm: #e58a3a;
--success: #4fbf73;
--danger: #e15353;
--text: #f4f1e8;
--text-dark: #151515;
--window: #ece9d8;
--border-light: #ffffff;
--border-dark: #3b4553;
```

## Typography
- UI: Tahoma, Verdana, Arial, sans-serif.
- Body: Verdana, Tahoma, sans-serif.
- Terminal: `Lucida Console`, `Courier New`, monospace.
- Pixel headings: optional licensed web font; always provide system fallback.

Do not bundle or redistribute font files in this kit.

## Spacing scale
4, 8, 12, 16, 24, 32, 48, 64 px.

## Radius
Keep mostly square. 0–4px for digital UI; physical props can be naturally rounded.

## Borders
Classic raised/sunken UI can use paired light/dark borders, but do not replicate Windows assets exactly.

## Focus state
2–3px high-contrast outline plus offset. Never rely only on color.

## Major components
- TitleScreen
- AdventureRoom
- Hotspot
- QuestLog
- BottomNav
- RetroWindow
- Dialog
- ProjectExplorer
- ProjectCaseStudy
- SkillGroup
- ContactPanel
- Tooltip
- AudioToggle
- ReducedMotionToggle
