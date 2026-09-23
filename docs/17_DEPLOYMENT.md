# Deployment

## Recommended
Vercel static/SSR deployment depending on final contact implementation.

## Environments
- local
- preview per branch/PR
- production

## Pipeline
```text
install
→ typecheck
→ unit tests
→ build
→ Playwright smoke
→ Lighthouse/quality check
→ deploy preview/production
```

## Environment variables
Only add variables when needed for analytics/contact endpoints. Never place secrets in Astro public environment variables.

## Cache
Use immutable cache headers for fingerprinted assets. Keep HTML revalidation aligned with deployment platform defaults.
