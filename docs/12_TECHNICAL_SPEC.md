# Technical Specification

## Recommended stack
- Astro
- TypeScript
- Astro Content Collections / Markdown or MDX
- Plain CSS or SCSS with design tokens
- Small client-side TypeScript islands only where interaction requires it
- Playwright for E2E/accessibility smoke tests
- Vitest for pure state utilities
- Lighthouse CI or equivalent automated quality check
- Vercel deployment

## Architecture principle
Server/static-render all meaningful content. Hydrate only the room interactions, quest state, audio toggle, and optional window behavior.

## Suggested source tree
```text
src/
├── components/
│   ├── adventure/
│   ├── content/
│   ├── navigation/
│   └── ui/
├── content/
│   └── projects/
├── layouts/
├── pages/
├── scripts/
├── styles/
└── data/
```

## Rendering
- Core pages: static HTML.
- Room interactivity: client island.
- Project data: content collection.
- Quest state: localStorage, not backend.
- Contact: external link/form endpoint only if needed.

## No mandatory dependencies
Avoid adopting a UI framework just to emulate old UI. Custom CSS is smaller and easier to art-direct.

## Progressive enhancement
Every primary route works without room JS. The room becomes an enhancement over normal links/articles.
