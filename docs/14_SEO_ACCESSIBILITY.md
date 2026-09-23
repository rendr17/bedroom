# SEO & Accessibility

## SEO
- Unique title/description per route.
- Canonical URLs.
- Open Graph/Twitter metadata.
- Sitemap.xml and robots.txt.
- Semantic project articles.
- `Person` schema for portfolio owner where appropriate.
- `CreativeWork`/`SoftwareApplication` schema only when data is accurate.

## Accessibility
- One H1 per route.
- Landmarks: header/nav/main/footer.
- Hotspots implemented as buttons/links, never bare divs.
- Visible focus.
- Single-click alternatives to any desktop-like behavior.
- Keyboard order follows visual logic.
- Dialog focus trap + return focus.
- `aria-live` only for meaningful status updates.
- Alt text describes content, not decorative style.
- Decorative room props use empty alt or CSS background.
- Do not make text part of an unreadable raster image when it conveys essential information.
- Honor reduced motion.
- Audio default off.

## Mobile
Touch targets >=44×44 CSS px; do not require precision clicking on tiny props.
