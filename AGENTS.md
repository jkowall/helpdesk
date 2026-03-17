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

## AI Widget Branding

- The primary text for the AI widget top bar should be **"Get Instant Help"**.
- The AI disclosure ("Powered by AI") should remain subtle.
- The widget should be functional across all mockups with a consistent "Expand/Collapse" logic.
