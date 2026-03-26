# AI Agent Instructions

## Canonical Theme Source (`theme/`)

The latest Freshdesk rollout code now lives in the `theme/` directory.

- `theme/head.html`
- `theme/layout.html`
- `theme/header.html`
- `theme/footer.html`
- `theme/portal_home.html`
- `theme/styles.css`

- **Sync Policy**: Treat `theme/` as the source of truth. Generated or compatibility files must follow it, not the other way around.
- **Secrets**: Sensitive values such as Embrace credentials must stay in `.env` and never be hardcoded into tracked files.

## AI Widget Snippet (`freshdesk-widget-snippet.html`)

This is the standalone code designed to be pasted into the Freshdesk portal footer or header.

- **Sync Policy**: This snippet must always be in sync with the canonical widget logic from `theme/header.html`, `theme/footer.html`, and `theme/styles.css`.
- **Primary Text**: Must be **"Get Instant Help"**.
- **Branding**: Uses `#004b87` (dark blue) for the bar and `#90c226` (Paessler green) for primary buttons.
- **Relativity**: Action links (like Create Ticket) should be relative (`/en/support/tickets/new`) for use within the same domain.

## Freshdesk Template Sync (`freshdesk-template.html`)

- **CRITICAL**: This file must strictly match the structure of the provided Liquid code.
- It is a combined snapshot of the canonical `theme/` section files.
- Functional links should point to the actual production services at `https://helpdesk.paessler.com`.

## Preview And Deploy Sync

- **Always update preview surfaces** when widget UI or copy changes. In particular, keep `theme-preview.html` aligned for anything visible in the expanded chat window, including disclaimers, labels, buttons, and helper text.
- **Always update compatibility/deploy files** when canonical widget behavior changes. Keep these in sync with `theme/`:
  - `deploy/1-custom-css.css`
  - `deploy/2-header-widget.html`
  - `deploy/4-footer-script.html`
- **Do not treat previews as optional**: if the user is likely to validate a change in the preview, the preview must reflect the same visible behavior as the canonical theme.
- **Always verify the hosted copy/paste path** after deploy-fragment changes. The user pastes from `https://jkowall.github.io/helpdesk/copy-paste-workbench.html`, so do not consider a change ready until the hosted workbench or its raw file URLs reflect the updated deploy files.
- **Do not rely on repo sync alone**: passing `scripts/check_sync.py` is necessary but not sufficient when the user is copying from the GitHub Pages workbench.
- **Always update `copy-paste-workbench.html`** if files are added, removed, or renamed — keep the `groups` object in its `<script>` block current so the hosted workbench reflects all deployable files.

## AI Widget Branding

- The primary text for the AI widget top bar should be **"Get Instant Help"**.
- The AI disclosure ("Powered by AI") should remain subtle.
- The widget should be functional across all mockups with a consistent "Expand/Collapse" logic.
