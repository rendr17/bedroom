# Analytics, Privacy & Security

## Analytics events worth tracking
- room_enter
- hotspot_open(section)
- nav_open(section)
- project_open(slug)
- cv_open
- contact_click(channel)
- sound_toggle

Avoid tracking every mouse movement or decorative click.

## Privacy
Quest progress remains in localStorage. Do not transmit it unless there is a clear product reason and disclosure.

## Security
- Escape/sanitize user-generated contact content if a backend is added.
- Add rate limiting/spam protection to any server-side form endpoint.
- Avoid exposing service keys.
- External links use appropriate `rel` attributes.
- Validate redirects and URL inputs.
