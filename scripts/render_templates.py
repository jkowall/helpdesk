#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

PLACEHOLDERS = {
    "__EMBRACE_ORG_ID__": "EMBRACE_ORG_ID",
    "__EMBRACE_CLIENT_ID__": "EMBRACE_CLIENT_ID",
}

FILES_TO_RENDER = [
    "theme/head.html",
    "theme/layout.html",
    "theme/header.html",
    "theme/footer.html",
    "theme/portal_home.html",
    "theme/styles.css",
    "deploy/1-custom-css.css",
    "deploy/2-header-widget.html",
    "deploy/3-hero-button.html",
    "deploy/4-footer-script.html",
    "freshdesk-widget-snippet.html",
]


def load_dotenv(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def missing_env_keys(env: dict[str, str]) -> list[str]:
    return [env_key for env_key in PLACEHOLDERS.values() if not env.get(env_key)]


def render_text(text: str, env: dict[str, str]) -> str:
    rendered = text
    for placeholder, env_key in PLACEHOLDERS.items():
        rendered = rendered.replace(placeholder, env[env_key])
    return rendered


def render_file(relative_path: str, env: dict[str, str]) -> None:
    source = ROOT / relative_path
    target = DIST / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    rendered = render_text(source.read_text(encoding="utf-8"), env)
    target.write_text(rendered, encoding="utf-8")


def build_combined_template() -> None:
    sections = [
        ("HEAD", ROOT / "theme/head.html"),
        ("LAYOUT", ROOT / "theme/layout.html"),
        ("HEADER", ROOT / "theme/header.html"),
        ("FOOTER", ROOT / "theme/footer.html"),
        ("PORTAL_HOME", ROOT / "theme/portal_home.html"),
        ("CSS", ROOT / "theme/styles.css"),
    ]
    parts: list[str] = []
    for title, path in sections:
        parts.append(f"<!-- {title} -->")
        parts.append(path.read_text(encoding="utf-8").rstrip())
        parts.append("")
    combined = "\n".join(parts).rstrip() + "\n"
    (ROOT / "freshdesk-template.html").write_text(combined, encoding="utf-8")


def main() -> None:
    env = load_dotenv(ROOT / ".env")
    build_combined_template()
    missing = missing_env_keys(env)
    if missing:
        joined = ", ".join(missing)
        print(f"Skipping dist render. Missing required values in .env: {joined}")
        return
    for relative_path in FILES_TO_RENDER:
        render_file(relative_path, env)


if __name__ == "__main__":
    main()
