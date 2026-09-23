# Retro Bedroom Adventure — Portfolio Development Kit

A development-ready handoff for **Rendi's Portfolio Adventure**, an interactive portfolio inspired by 2000–2005 bedroom PCs, point-and-click games, early web UI, CRT displays, pixel icons, and personal internet culture.

## Product principle

**Portfolio first. Game-like second.** A visitor must be able to understand who Rendi is, open projects, review experience/skills, and reach contact information without solving a puzzle.

## Package contents

- `docs/` — PRD, UX, technical, content, motion, accessibility, performance, testing, deployment, analytics, security, and phase plan.
- `assets/` — original SVG/PNG/WAV assets plus concept references.
- `content/` — structured project/content examples ready to move into Astro Content Collections.
- `starter-snippets/` — design tokens, hotspot data, content types, route plan, and implementation notes.
- `checklists/` — per-phase definition of done and launch checks.

## Recommended build order

Follow `docs/19_DEVELOPMENT_PHASES.md`. Do not jump directly to easter eggs or audio. Build the accessible content routes first, then layer the room/game experience over them.

## Core routes

- `/`
- `/about`
- `/projects`
- `/projects/antero`
- `/projects/jejakbahari`
- `/projects/quick-order`
- `/projects/dock-disorder`
- `/experience`
- `/skills`
- `/contact`
- `/extras`

## Visual references

The selected concept is in `assets/concept/reference_user_selected.png`. Production code should use modular assets rather than flattening the entire interface into one background image.

## Fonts

No font files are bundled. Use system-safe fonts such as Tahoma/Verdana and optionally load a properly licensed pixel font in the project itself.

## Development

The Astro app lives in `app/` (see `app/package.json` for dev/build/check/lint scripts). The kit's `docs/`, `assets/`, `content/`, and `starter-snippets/` remain at the repository root as the handoff reference.
