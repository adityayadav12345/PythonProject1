import pytest


@pytest.fixture
def user_data():
    return {"username": "testuser", "email": "test@example.com"}


@pytest.fixture
def user_profile(user_data):
    """Fixture that depends on another fixture"""
    profile = user_data.copy()
    profile["premium"] = True
    profile["joined_date"] = "2024-01-01"
    return profile


@pytest.fixture
def complete_user(user_profile):
    """Fixture with multiple dependencies"""
    user_profile["settings"] = {"theme": "dark", "notifications": True}
    return user_profile


def test_user_profile(user_profile):
    assert user_profile["username"] == "testuser"
    assert user_profile["premium"] is True
    assert "joined_date" in user_profile


def test_complete_user(complete_user):
    assert complete_user["username"] == "testuser"
    assert complete_user["settings"]["theme"] == "dark"
    assert complete_user["settings"]["notifications"] is True
