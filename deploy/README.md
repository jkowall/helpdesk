# Freshdesk Portal Deployment Guide

The latest rollout code now lives in [`theme/`](../theme/). The files in `deploy/` are the copy/paste fragments for Freshdesk admins.

## Secrets

- Do not commit `.env`
- Put `EMBRACE_ORG_ID` and `EMBRACE_CLIENT_ID` in `.env`
- Run `python3 scripts/render_templates.py` to create local rendered copies in `dist/`
- Run `python3 scripts/check_sync.py` after widget changes to confirm preview and deploy surfaces still match the canonical theme widget

## Deploy Files

- `1-custom-css.css`: custom CSS additions
- `2-header-widget.html`: signed-in widget header block
- `3-hero-button.html`: logged-in hero chat block
- `4-footer-script.html`: widget behavior and hero-to-chat wiring

## Source Of Truth

- `theme/head.html`
- `theme/layout.html`
- `theme/header.html`
- `theme/footer.html`
- `theme/portal_home.html`
- `theme/styles.css`
