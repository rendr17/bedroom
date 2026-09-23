# Interaction Specification

## Room exploration
- Pointer enters hotspot → marker brightens and label appears.
- Click/tap → route transition + content opens.
- Keyboard focus → same label/state as hover.

## Intro
`New Game` resets quest-progress only after confirmation.  
`Continue` uses locally stored visited state.  
`Skip Intro` enters room immediately.

## Navigation
Direct nav is available regardless of quest progress.

## Visited state
After opening a core section:
- mark quest item complete
- optional tiny confirmation sound if sound is enabled
- do not show modal congratulations for routine actions

## Easter eggs
- Cat click: short visual reaction.
- Floppy disk: README dialog.
- Gamepad: Extras page.
- Posters: optional short caption.

## Persistence keys
Suggested:
```text
portfolio:introSeen
portfolio:visitedSections
portfolio:soundEnabled
portfolio:reducedEffects
```

## Pointer rules
Use single click/tap. Double-click must never be required.
