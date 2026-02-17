# AI Agent Instructions

## AI Widget Snippet (`freshdesk-widget-snippet.html`)

This is the standalone code designed to be pasted into the Freshdesk portal footer or header.

- **Sync Policy**: This snippet must always be in sync with the branding and logic found in `production-clone.html`.
- **Primary Text**: Must be **"Get Instant Help"**.
- **Branding**: Uses `#004b87` (dark blue) for the bar and `#90c226` (Paessler green) for primary buttons.
- **Relativity**: Action links (like Create Ticket) should be relative (`/en/support/tickets/new`) for use within the same domain.

## Freshdesk Template Sync (`freshdesk-template.html`)

- **CRITICAL**: This file must strictly match the structure of the provided Liquid code.
- Elements like the hero section, the 5-card grid, and the Community Forums section are derived from the Liquid source.
- Functional links should point to the actual production services at `https://helpdesk.paessler.com`.

## AI Widget Branding

- The primary text for the AI widget top bar should be **"Get Instant Help"**.
- The AI disclosure ("Powered by AI") should remain subtle.
- The widget should be functional across all mockups with a consistent "Expand/Collapse" logic.
