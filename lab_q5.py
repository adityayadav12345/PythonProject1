# ============================================================================
# 5. BOOLEAN LOGIC ASSERTIONS
# ============================================================================

def check_age_and_license(age: int, has_license: bool) -> bool:
    return age >= 18 and has_license


def is_valid_username(username: str) -> bool:
    return username and len(username) >= 3 and username.isalnum()


def check_empty_collection(collection) -> bool:
    return not collection


class TestBooleanLogic:
    def test_multiple_and_conditions(self):
        assert check_age_and_license(20, True) is True
        assert check_age_and_license(20, False) is False
        assert check_age_and_license(16, True) is False
        assert check_age_and_license(16, False) is False

    def test_truthy_falsy_values(self):
        assert bool([1, 2, 3]) is True
        assert bool([]) is False
        assert bool("text") is True
        assert bool("") is False
        assert bool(0) is False
        assert bool(1) is True

    def test_none_type_checking(self):
        value = None
        assert value is None
        assert value == None
        assert not value

        value = "something"
        assert value is not None

    def test_empty_collection_validations(self):
        assert check_empty_collection([]) is True
        assert check_empty_collection([1]) is False
        assert check_empty_collection({}) is True
        assert check_empty_collection(set()) is True
        assert check_empty_collection("") is True

