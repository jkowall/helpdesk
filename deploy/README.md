# Freshdesk Portal Deployment Guide

Deploy the AI "Get Instant Help" widget to your Freshdesk portal in 3 steps.

## Prerequisites

- Freshdesk Admin access → **Admin → Portals → Edit → Appearance**
- Clone the live "Marina" theme before editing (for safety)
- Your Embrace AI credentials: `org-id` and `client-id`

---

## Step 1: Custom CSS → `layout.css` or Stylesheet tab

Paste the contents of **[1-custom-css.css](./1-custom-css.css)** into your theme's
CSS file (usually `layout.css`) or the global Stylesheet tab.

> **Path:** Admin → Portals → Edit → Appearance → CSS tab (or Stylesheet)

---

## Step 2: Header Code → `header.html`

Paste the contents of **[2-header-widget.html](./2-header-widget.html)** into your
`header.html` file, **above** the existing `{{ header }}` Liquid tag.

> **Path:** Admin → Portals → Edit → Appearance → Pages → Header

---

## Step 3: Home Page Hero → `home_page.html`

Add the "Get Instant Help" button to the hero section of your home page.
Paste the contents of **[3-hero-button.html](./3-hero-button.html)** into
`home_page.html`, inside the hero/search section, after the search form.

> **Path:** Admin → Portals → Edit → Appearance → Pages → Home

---

## Step 4: Footer Script → `footer.html`

Paste the contents of **[4-footer-script.html](./4-footer-script.html)** into your
`footer.html` file, **before** the closing `{{ footer }}` Liquid tag.

> **Path:** Admin → Portals → Edit → Appearance → Pages → Footer

---

## Important Notes

1. **CSP/Nonce**: The Marina theme uses Content Security Policy. All `<style>` and
   `<script>` tags include `nonce="{{portal.nonce}}"` to comply.
2. **Replace Credentials**: Search for `YOUR_ORG_ID` and `YOUR_CLIENT_ID` and
   replace with your actual Embrace AI values.
3. **Test First**: Clone your theme, apply changes to the clone, preview, then
   activate when satisfied.
4. **Relative Links**: All ticket/solution links use relative paths (`/en/support/...`)
   so they work within your Freshdesk domain.
