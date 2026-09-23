# State & Routing

## Route is source of truth
Content visibility follows URL, not hidden internal-only window state.

## Local UI state
Safe to persist:
- intro seen
- sound enabled
- visited sections
- optional selected room theme

Do not persist:
- form messages
- personal visitor data
- arbitrary window positions unless proven useful

## Route-to-hotspot map
```ts
/              -> room
/about         -> about
/projects      -> projects
/experience    -> experience
/skills        -> skills
/contact       -> contact
/extras        -> extras
```

## Back button
Browser Back must work naturally. Avoid intercepting history in ways that trap visitors in a modal stack.
