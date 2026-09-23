# Testing Strategy

## Unit
- quest reducer/state utility
- localStorage parsing fallback
- route/hotspot mapping
- reduced-motion logic

## E2E
- intro can be skipped
- every primary hotspot opens correct route
- direct nav opens same route
- browser Back returns correctly
- deep project URL loads content
- contact links reachable
- quest completion updates after visits

## Accessibility smoke
- keyboard-only primary journey
- focus visible
- Escape behavior
- automated axe/Playwright scan
- reduced-motion media query

## Responsive
Test at minimum:
- 360×800
- 390×844
- 768×1024
- 1366×768
- 1440×900
- 1920×1080

## Browser
Current stable Chrome/Edge/Firefox/Safari representative environments.

## Visual regression
Capture screenshots for room and every core route at desktop + mobile.
