# Step-by-Step Development Prompts

Use one prompt per phase. Do not combine phases unless the previous phase is green.

## Prompt template
```text
You are implementing Phase {N} of a portfolio named "Rendi's Portfolio Adventure".
Read these first:
- docs/01_PRD.md
- docs/07_DESIGN_SYSTEM.md
- docs/09_INTERACTION_SPEC.md
- docs/14_SEO_ACCESSIBILITY.md
- docs/19_DEVELOPMENT_PHASES.md

Implement ONLY Phase {N}. Preserve all working behavior from earlier phases.
Before coding, inspect the existing repo and list the files you will change.
After implementation:
1. run typecheck/build/tests relevant to the phase,
2. fix failures,
3. report files changed,
4. report acceptance criteria status,
5. do not start the next phase.
```

## Special instruction for visual phases
Use the composite sheets in `assets/sheets/` as the single art source. Export modular pieces from them (see `tools/extract_sprites.py`); do not flatten the whole site into a screenshot background with fake HTML hotspots.

## Special instruction for content
Do not invent private employer/client metrics or confidential details. Keep placeholders clearly marked when final public wording has not been approved.
