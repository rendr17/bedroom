# Performance Budget

## Targets
- Initial JS: keep interaction bundle small; target under ~150–200 KB gzip when practical.
- Critical image: responsive and compressed.
- Do not preload all project screenshots.
- Audio loads only after explicit interaction or idle after core content.
- Avoid large animation libraries for basic window transitions.

## Loading strategy
1. HTML/CSS/core room illustration.
2. Primary interaction JS.
3. Project thumbnails near viewport.
4. Optional props/easter eggs.
5. Audio only on demand.

## Monitoring
Check on realistic 4G/mobile throttling, not desktop broadband only.
