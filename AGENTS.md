# AGENTS.md — Portfolio Adventure

## Read before changes
1. `docs/01_PRD.md`
2. `docs/07_DESIGN_SYSTEM.md`
3. `docs/09_INTERACTION_SPEC.md`
4. `docs/12_TECHNICAL_SPEC.md`
5. `docs/14_SEO_ACCESSIBILITY.md`
6. `docs/19_DEVELOPMENT_PHASES.md`

## Product rules
- Portfolio first; game-like second.
- Never require a puzzle, double click, audio, drag, or hover to access core content.
- Direct route URLs are first-class.
- Primary content must exist as semantic HTML.
- Keep audio off by default.
- Respect reduced motion.
- No literal RendiOS/Windows clone branding.
- Avoid SaaS-style generic cards where the room metaphor can do the job.
- Do not add a large frontend framework without a clear need.
- Do not use percentage bars to claim skill level.

## Development rules
- Work one phase at a time.
- Keep scope of each PR/commit aligned with one phase.
- Run build/typecheck/test before marking a phase complete.
- Add/update tests for behavior changes.
- Preserve mobile + keyboard access.
- Optimize imagery before production.

## Commit rules
- Commit messages must not include "Generated with ..." tool trailers.
- Commit messages must not include "Co-Authored-By" lines.
- Keep commit messages focused on the change itself (subject + short body).

## Asset rules
- Use bundled original SVG/WAV assets freely inside this project.
- Concept images are references, not UI screenshots to embed as the final interactive experience.
- Do not bundle font files without license confirmation.
- Replace neutral avatar placeholder only with an approved user-specific image.
