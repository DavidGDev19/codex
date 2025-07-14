"""Security helper functions."""

import html
import re
import secrets


def sanitize_str(value: str) -> str:
    """Return HTML-escaped string."""
    return html.escape(value)


def validate_id(value: str) -> bool:
    """Validate that value is numeric."""
    return bool(re.fullmatch(r"\d+", value))


def csrf_token() -> str:
    """Generate CSRF token."""
    return secrets.token_hex(16)
