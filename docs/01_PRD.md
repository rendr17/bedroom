# Product Requirements Document

## 1. Product
**Rendi's Portfolio Adventure** — a personal software-developer portfolio with an interactive Retro Bedroom Adventure interface.

## 2. Problem
Most developer portfolios use similar landing-page structures and card grids. The goal is to create a memorable experience while still serving the practical needs of recruiters, collaborators, clients, and technical peers.

## 3. Goals
1. Present Rendi as a software developer focused on practical web systems, AI integration, operations, and digital products.
2. Showcase projects with enough context to understand problem, role, approach, technology, and impact.
3. Make the site memorable through a point-and-click retro bedroom experience.
4. Keep direct URLs, semantic HTML, accessibility, SEO, and mobile usability intact.
5. Keep content maintainable through structured project data/MDX rather than hardcoded page markup.

## 4. Target audiences
### Recruiter / hiring manager
Needs fast proof of role, experience, projects, stack, and contact details.

### Technical peer
Wants architecture, implementation decisions, integrations, tradeoffs, and project details.

### Client / collaborator
Wants confidence that Rendi can solve real operational problems and ship usable products.

### Curious visitor
Can explore the room, quest log, props, mini interactions, and easter eggs.

## 5. Core user stories
- As a visitor, I can skip the intro and access the room immediately.
- As a visitor, I can click the CRT monitor to open Projects.
- As a visitor, I can use persistent navigation instead of exploring hotspots.
- As a recruiter, I can open `/projects/antero` directly from a shared URL.
- As a keyboard user, I can navigate all hotspots and dialogs without a mouse.
- As a mobile user, I receive a simplified touch-first version rather than a tiny desktop scene.
- As a visitor with reduced-motion preferences, I can use the site without cinematic transitions.
- As a visitor, audio never starts without my action.

## 6. Core sections
1. Home / Adventure Room
2. About
3. Projects
4. Project Details
5. Experience
6. Skills
7. Contact
8. Extras / Easter Eggs

## 7. Featured projects
- Antero Platform — enterprise logistics/internal operations platform.
- JejakBahari — open-source Indonesian RoRo/maritime tracking concept.
- Quick Order — pay-first dine-in ordering workflow.
- Dock & Disorder — web-game project concept.

## 8. Core room hotspots
| Object | Opens | Importance |
|---|---|---|
| CRT monitor | Projects | Primary |
| Notebook/photo frame | About | Primary |
| Shelf / binders | Experience | Primary |
| Tool drawers / keyboard | Skills | Primary |
| Desk phone / envelope | Contact | Primary |
| Gamepad | Extras / mini-game | Optional |
| Cat | Easter egg | Optional |
| Floppy disk | Hidden README | Optional |
| Posters | Small quotes/details | Optional |

## 9. Functional requirements
- Responsive interactive room.
- Hotspot focus/hover/active states.
- Direct navigation bar.
- Route-aware modal/window or page panels.
- Project index and project detail pages.
- Keyboard navigation and focus trapping in dialogs.
- Quest log tracking visited sections locally.
- Optional persisted settings: sound, motion, intro seen.
- Contact links/form.
- Download/open CV when provided.
- Shareable project URLs.
- 404 page in the same art direction.

## 10. Game-like requirements
- Quest log marks core sections as explored.
- Intro offers `New Game`, `Continue`, and `Skip to Portfolio` semantics, but never blocks content.
- Exploration rewards are cosmetic only.
- No required puzzle, score, or combat.
- Progress stored locally only.

## 11. Content requirements
Each case study should contain:
- summary
- role
- context/problem
- responsibilities
- solution
- features
- technology
- notable technical decisions
- impact/results
- screenshots or diagrams
- links/status where publishable

## 12. Quality targets
- Mobile-first semantic content underneath interactive presentation.
- Lighthouse targets: Performance >=90, Accessibility >=95, Best Practices >=95, SEO >=95 on production representative pages.
- No required interaction dependent only on hover or double-click.
- No autoplay audio.
- Core content usable with JavaScript disabled or failed.

## 13. Out of scope for MVP
- Character walking around the room.
- Physics/collision.
- Real multiplayer/chat.
- Full virtual OS.
- Backend/CMS.
- Complex account/authentication.
- Required mini-games.
