# START HERE

## 1. Review before coding
Read in this order:
1. `docs/00_PROJECT_BRIEF.md`
2. `docs/01_PRD.md`
3. `docs/02_MVP_SCOPE.md`
4. `docs/07_DESIGN_SYSTEM.md`
5. `docs/12_TECHNICAL_SPEC.md`
6. `docs/19_DEVELOPMENT_PHASES.md`
7. `AGENTS.md`

## 2. Prepare the repo
Scaffold Astro in `app/` if you want to keep this handoff package at repository root. Copy `starter-snippets/design-tokens.css` into the app style system and use `starter-snippets/hotspots.ts` as the first hotspot map.

## 3. Start only with Phase 0
Do not implement the interactive room first. Build the semantic content routes, then add the room as an enhancement. This preserves accessibility, SEO, maintainability, and direct-link behavior.

## 4. Asset usage
- Primary reference: `assets/concept/reference_user_selected.png`
- Modular backgrounds: `assets/backgrounds/`
- Navigation icons: `assets/icons/nav/`
- Props: `assets/props/`
- Posters: `assets/posters/`
- UI cues: `assets/audio/`
- Asset index: `assets/ASSET_MANIFEST.json`

## 5. Replace before launch
- `assets/props/avatar-placeholder.png`
- placeholder project screenshots
- final CV
- exact public contact/social links
- any project wording that should not be public

## 6. First coding prompt
Use the Phase 0 template from `docs/21_AGENT_PROMPTS.md`. Finish its acceptance criteria, commit, then proceed to Phase 1.
