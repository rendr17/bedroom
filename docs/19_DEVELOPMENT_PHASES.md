# Development Plan — Small Phases

Each phase must end with a working, reviewable state. Commit after the acceptance criteria pass.

## Phase 0 — Repository foundation
**Build:** Astro project, TypeScript strict mode, formatting/linting, base folders, global tokens.  
**Done when:** dev/build commands work and a blank semantic page deploys.

## Phase 1 — Content-first routes
**Build:** `/about`, `/projects`, `/experience`, `/skills`, `/contact` as plain accessible pages.  
**Done when:** all information is navigable without game UI or JavaScript.

## Phase 2 — Project content model
**Build:** project schema/content collection + four project entries.  
**Done when:** `/projects/[slug]` renders from structured content.

## Phase 3 — Global visual shell
**Build:** typography, background colors, bottom navigation, focus states, retro UI primitives.  
**Done when:** all routes share consistent art direction.

## Phase 4 — Title screen
**Build:** New Game / Continue / Skip UI.  
**Done when:** Skip is immediate, Continue is safe with empty storage, reduced-motion mode works.

## Phase 5 — Adventure Room static scene
**Build:** room artwork, responsive framing, desktop/tablet/mobile composition.  
**Done when:** scene scales without clipping primary navigation.

## Phase 6 — Primary hotspots
**Build:** About, Projects, Experience, Skills, Contact hotspots.  
**Done when:** mouse, touch, and keyboard all reach the same routes.

## Phase 7 — Quest Log
**Build:** visited-state tracking in localStorage.  
**Done when:** visiting sections checks them off; corrupt/blocked storage never breaks navigation.

## Phase 8 — About presentation
**Build:** notebook/photo-frame themed presentation.  
**Done when:** content remains readable at mobile and 200% zoom.

## Phase 9 — Projects explorer
**Build:** CRT/file-explorer styled project index.  
**Done when:** all project cards/folders are ordinary links underneath the visual metaphor.

## Phase 10 — Antero case study
**Build:** first full project-detail design and reusable case-study components.  
**Done when:** Overview → Impact can be read with JS disabled.

## Phase 11 — Remaining case studies
**Build:** JejakBahari, Quick Order, Dock & Disorder content using the same system with small project-specific visual variants.  
**Done when:** no bespoke page breaks the shared component model.

## Phase 12 — Experience + Skills presentation
**Build:** binders/archive for Experience; drawers/tools for Skills.  
**Done when:** information hierarchy is clear and no fake skill percentages are used.

## Phase 13 — Contact
**Build:** phone/envelope themed panel, social links, CV link, optional form.  
**Done when:** keyboard/mobile submission/link flow works and errors are accessible.

## Phase 14 — Easter eggs
**Build:** cat reaction, floppy README, gamepad Extras.  
**Done when:** disabling/removing extras does not affect core navigation.

## Phase 15 — Audio
**Build:** sound toggle and original UI cues.  
**Done when:** default is silent, user choice persists, no audio blocks interaction.

## Phase 16 — Motion polish
**Build:** hotspot feedback, subtle window transitions, optional CRT intro.  
**Done when:** reduced-motion version remains polished and complete.

## Phase 17 — Responsive/mobile refinement
**Build:** touch-first hotspot list, full-screen content panels, landscape handling.  
**Done when:** no tiny desktop interactions remain mandatory on mobile.

## Phase 18 — SEO/accessibility pass
**Build:** metadata, sitemap, schema, heading/focus review, screen-reader labels.  
**Done when:** automated + manual checks meet project targets.

## Phase 19 — Performance pass
**Build:** asset compression, lazy loading, bundle audit, remove unused JS.  
**Done when:** Lighthouse targets are consistently close to or above budget on representative production pages.

## Phase 20 — QA & launch
**Build:** browser matrix, visual regression, broken-link check, analytics verification, production deploy.  
**Done when:** launch checklist passes and direct URLs are verified in production.
