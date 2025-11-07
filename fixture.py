import pytest

# -----------------------------
# Fixture 1: Module scope
# -----------------------------
@pytest.fixture(scope="module")
def db_connection():
    print("\n[Setup] Connecting to database (module-level)")
    conn = {"status": "connected"}
    yield conn
    print("\n[Teardown] Closing database connection (module-level)")
    conn["status"] = "disconnected"


# -----------------------------
# Fixture 2: Class scope
# -----------------------------
@pytest.fixture(scope="class")
def user_data():
    print("\n[Setup] Creating user data (class-level)")
    data = {"user": "Aditya", "role": "Tester"}
    yield data
    print("\n[Teardown] Clearing user data (class-level)")


# -----------------------------
# Fixture 3: Function scope (default)
# -----------------------------
@pytest.fixture(scope="function")
def log_function():
    print("\n[Setup] Starting test (function-level)")
    yield
    print("[Teardown] Finished test (function-level)")


# -----------------------------
# First Test Class
# -----------------------------
class TestUserModule:

    def test_user_name(self, db_connection, user_data, log_function):
        print("Running test_user_name")
        assert user_data["user"] == "Aditya"
        assert db_connection["status"] == "connected"

    def test_user_role(self, db_connection, user_data, log_function):
        print("Running test_user_role")
        assert user_data["role"] == "Tester"


# -----------------------------
# Second Test Class
# -----------------------------
class TestProductModule:

    def test_product_access(self, db_connection, log_function):
        print("Running test_product_access")
        assert db_connection["status"] == "connected"

    def test_product_availability(self, db_connection, log_function):
        print("Running test_product_availability")
        assert "status" in db_connection
