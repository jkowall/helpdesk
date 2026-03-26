# Project Instructions

## File Sync Rules

When making CSS or HTML changes, **all copies must be kept in sync**. The following files share overlapping content and must all be updated together:

| Canonical Source | Synced Copies |
|---|---|
| `theme/styles.css` | `deploy/1-custom-css.css`, `freshdesk-widget-snippet.html` (inline `<style>`), `freshdesk-template.html` (inline `<style>`), `theme-preview.html` (inline `<style>`) |
| `theme/header.html` | `deploy/2-header-widget.html`, `freshdesk-template.html` |
| `theme/footer.html` | `deploy/4-footer-script.html`, `freshdesk-template.html` |
| `theme/head.html` | `freshdesk-template.html` |
| `theme/portal_home.html` | `deploy/3-hero-button.html`, `freshdesk-template.html` |

## Workbench Page

`copy-paste-workbench.html` is the hosted workbench at https://jkowall.github.io/helpdesk/copy-paste-workbench.html — it dynamically loads the source files listed above at runtime. If you add new files or rename existing ones, update the `groups` object in `copy-paste-workbench.html` so the workbench stays current.

## Deployment

- **GitHub Pages**: Push to `main` — the site auto-deploys to https://jkowall.github.io/helpdesk/
- **Freshdesk Portal**: Copy contents from `deploy/` files (or use the workbench) and paste into the Freshdesk admin panel manually.

## Preview Pages

- `theme-preview.html` — full theme preview (standalone)
- `widget-preview.html` — chat widget preview (loads `freshdesk-widget-snippet.html`)
- `copy-paste-workbench.html` — copy/paste workbench for deploying to Freshdesk
