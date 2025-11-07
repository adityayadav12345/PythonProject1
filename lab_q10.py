# ============================================================================
# 10. REGULAR EXPRESSION ASSERTIONS
# ============================================================================
import re

import pytest


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))


def validate_password(password: str) -> bool:
    # At least 8 chars, 1 uppercase, 1 lowercase, 1 digit
    if len(password) < 8:
        return False
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    return has_upper and has_lower and has_digit


def validate_url(url: str) -> bool:
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(pattern, url))


class TestRegularExpressions:
    def test_email_validation(self):
        assert validate_email("user@example.com") is True
        assert validate_email("test.user@domain.co.in") is True
        assert validate_email("invalid.email@") is False
        assert validate_email("@example.com") is False
        assert validate_email("notemail.com") is False

    def test_phone_validation(self):
        assert validate_phone("1234567890") is True
        assert validate_phone("+911234567890") is True
        assert validate_phone("12345") is False
        assert validate_phone("abcd1234567") is False

    def test_password_strength(self):
        assert validate_password("Password123") is True
        assert validate_password("Weak1") is False  # Too short
        assert validate_password("nouppercas1") is False
        assert validate_password("NOLOWERCASE1") is False
        assert validate_password("NoDigits") is False

    def test_url_validation(self):
        assert validate_url("http://example.com") is True
        assert validate_url("https://www.google.com") is True
        assert validate_url("https://site.com/path/to/page") is True
        assert validate_url("not-a-url") is False
        assert validate_url("ftp://example.com") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])