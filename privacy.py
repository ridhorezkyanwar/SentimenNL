"""Small, dependency-free privacy helpers for public review text."""

from __future__ import annotations

import re

_EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
_PHONE = re.compile(
    r"(?<!\w)(?:\+?62|0)[ \t().-]*(?:\d[ \t().-]*){8,13}(?!\d)"
)


def scrub_personal_data(text: str) -> str:
    """Redact email addresses and likely Indonesian phone numbers from review text."""
    without_emails = _EMAIL.sub("[REDACTED_EMAIL]", text)
    return _PHONE.sub("[REDACTED_PHONE]", without_emails)
