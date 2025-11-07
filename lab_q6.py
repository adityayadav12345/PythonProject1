# ============================================================================
# 6. TYPE CHECKING ASSERTIONS
# ============================================================================
from typing import List, Dict, Any


def get_user_age() -> int:
    return 25


def convert_string_to_list(text: str) -> List[str]:
    return list(text)


def create_user_dict(name: str, age: int) -> Dict[str, Any]:
    return {"name": name, "age": age}


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class TestTypeChecking:
    def test_function_return_types(self):
        result = get_user_age()
        assert isinstance(result, int)
        assert type(result) == int

    def test_type_conversion_functions(self):
        result = convert_string_to_list("hello")
        assert isinstance(result, list)
        assert all(isinstance(char, str) for char in result)
        assert len(result) == 5

    def test_dictionary_types(self):
        user = create_user_dict("Alice", 30)
        assert isinstance(user, dict)
        assert isinstance(user["name"], str)
        assert isinstance(user["age"], int)

    def test_custom_class_instances(self):
        person = Person("Bob", 25)
        assert isinstance(person, Person)
        assert hasattr(person, "name")
        assert hasattr(person, "age")
        assert type(person.name) == str
        assert type(person.age) == int
