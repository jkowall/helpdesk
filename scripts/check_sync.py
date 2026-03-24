#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def block(text: str, start: str, end: str) -> str | None:
    start_index = text.find(start)
    if start_index == -1:
        return None
    end_index = text.find(end, start_index)
    if end_index == -1:
        return None
    end_index += len(end)
    return text[start_index:end_index]


def css_from(text: str, marker: str) -> str | None:
    start_index = text.find(marker)
    if start_index == -1:
        return None
    return text[start_index:]


def css_between(text: str, start: str, end: str) -> str | None:
    start_index = text.find(start)
    if start_index == -1:
        return None
    end_index = text.find(end, start_index)
    if end_index == -1:
        return None
    return text[start_index:end_index]


def check_equal(
    name: str,
    left_label: str,
    left_text: str | None,
    right_label: str,
    right_text: str | None,
    failures: list[str],
) -> None:
    if left_text is None or right_text is None:
        failures.append(
            f"{name}: missing comparison block in {left_label if left_text is None else right_label}"
        )
        return
    if normalized(left_text) != normalized(right_text):
        failures.append(f"{name}: {left_label} and {right_label} are out of sync")


def check_contains(name: str, haystack_label: str, haystack: str, needle: str, failures: list[str]) -> None:
    if needle not in haystack:
        failures.append(f'{name}: missing "{needle}" in {haystack_label}')


def main() -> int:
    failures: list[str] = []

    theme_header = read("theme/header.html")
    deploy_header = read("deploy/2-header-widget.html")
    theme_styles = read("theme/styles.css")
    deploy_css = read("deploy/1-custom-css.css")
    theme_footer = read("theme/footer.html")
    preview = read("theme-preview.html")
    widget_snippet = read("freshdesk-widget-snippet.html")

    widget_start = '{% if portal.has_user_signed_in == true %}'
    widget_end = '{% endif %}'
    check_equal(
        "Header widget block",
        "theme/header.html",
        block(theme_header, widget_start, widget_end),
        "deploy/2-header-widget.html",
        block(deploy_header, widget_start, widget_end),
        failures,
    )

    check_equal(
        "Widget CSS core",
        "theme/styles.css",
        css_between(theme_styles, "#embrace-widget-container {", "@media (min-width: 992px)"),
        "deploy/1-custom-css.css",
        css_between(deploy_css, "#embrace-widget-container {", "@media (min-width: 992px)"),
        failures,
    )

    copy_checks = [
        ("Primary label", "Get Instant Help"),
        ("AI disclosure", "Powered by AI"),
        ("Expand CTA", "Expand Chat"),
        ("Input placeholder", "Ask Max a question..."),
        (
            "Disclaimer",
            "You’re chatting with Max, our AI assistant built to help you get answers quickly. If needed, he’ll guide you to the next best step.",
        ),
    ]

    for label, needle in copy_checks:
        check_contains(label, "theme/header.html", theme_header, needle, failures)
        check_contains(label, "theme-preview.html", preview, needle, failures)
        check_contains(label, "freshdesk-widget-snippet.html", widget_snippet, needle, failures)

    theme_behavior_checks = [
        ("Theme fullscreen class", "container.classList.toggle('widget-fullscreen')"),
        ("Theme collapse label", "Collapse Chat"),
        ("Theme hero handoff", "window.openFullscreenChat = function (message)"),
    ]

    for label, needle in theme_behavior_checks:
        check_contains(label, "theme/footer.html", theme_footer, needle, failures)

    preview_behavior_checks = [
        ("Preview fullscreen class", "widget.classList.add('widget-fullscreen')"),
        ("Preview collapse label", "Collapse Chat"),
        ("Preview ticket reveal", "ticketBtn.style.display = 'inline-flex'"),
    ]

    for label, needle in preview_behavior_checks:
        check_contains(label, "theme-preview.html", preview, needle, failures)

    if failures:
        print("Sync check failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Sync check passed.")
    print("Verified theme, deploy, snippet, and preview widget surfaces are aligned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
