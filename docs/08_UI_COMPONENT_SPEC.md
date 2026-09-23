# UI Component Specification

## Hotspot
States: idle, hover, focus, active, visited, disabled.
- Desktop target >= 44×44 px even when visual marker is smaller.
- Label appears on hover/focus and remains readable over busy art.
- Touch devices show visible labels; no hover dependency.

## Quest Log
- Shows 5 required sections + optional easter-egg line.
- `visited` stored locally.
- Completion is decorative, never used as access control.

## RetroWindow
- Header, title, close button, optional maximize.
- Desktop: centered or contextual panel; dragging optional after MVP.
- Mobile: full-page route/panel.
- Escape closes only when safe; route history respected.

## Project Explorer
- Folder/list metaphor.
- Must include normal text links for every project.

## Project Detail
Desktop can use game-panel/installer framing; article semantics remain normal.
Sections: Overview, Problem, Role, Solution, Features, Tech, Decisions, Impact, Gallery.

## Bottom Navigation
Always provides About, Projects, Experience, Skills, Contact.
Current route indicated with text + visual state.

## Tooltips
- Delay 250–400 ms on pointer hover.
- Immediate on keyboard focus.
- No critical content in tooltip only.

## Dialog
Use for optional interactions and easter eggs, not project-length content.
