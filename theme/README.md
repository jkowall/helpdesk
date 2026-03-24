# Freshdesk Theme Source

This directory is the canonical source of truth for the latest Freshdesk rollout code.

Files map directly to Freshdesk theme sections:

- `head.html`
- `layout.html`
- `header.html`
- `footer.html`
- `portal_home.html`
- `styles.css`

Sensitive values stay out of tracked files. Use `.env` with:

- `EMBRACE_ORG_ID`
- `EMBRACE_CLIENT_ID`

Then run:

```bash
python3 scripts/render_templates.py
python3 scripts/check_sync.py
```

Rendered local copies with secrets injected are written to `dist/`.
The sync check verifies that the canonical `theme/` widget, preview surface, deploy snippets, and standalone widget snippet have not drifted on key copy and behavior.
