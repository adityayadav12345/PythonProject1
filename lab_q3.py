# ============================================================================
# 3. LIST & DATA STRUCTURE ASSERTIONS
# ============================================================================
from typing import Dict, List


def sort_list(data: List) -> List:
    return sorted(data)


def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    return {**dict1, **dict2}


def set_union(set1: set, set2: set) -> set:
    return set1.union(set2)


def set_intersection(set1: set, set2: set) -> set:
    return set1.intersection(set2)


class TestDataStructures:
    def test_list_sorting_integers(self):
        data = [5, 2, 8, 1, 9]
        assert sort_list(data) == [1, 2, 5, 8, 9]

    def test_list_sorting_strings(self):
        data = ["zebra", "apple", "mango", "banana"]
        assert sort_list(data) == ["apple", "banana", "mango", "zebra"]

    def test_dictionary_operations(self):
        dict1 = {"name": "John", "age": 30}
        dict2 = {"city": "Chennai", "country": "India"}
        result = merge_dicts(dict1, dict2)

        assert result["name"] == "John"
        assert result["city"] == "Chennai"
        assert len(result) == 4

    def test_set_union(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result = set_union(set1, set2)

        assert result == {1, 2, 3, 4, 5}
        assert len(result) == 5

    def test_set_intersection(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        result = set_intersection(set1, set2)

        assert result == {3, 4}
        assert len(result) == 2

    def test_list_comprehensions(self):
        numbers = [1, 2, 3, 4, 5]
        squares = [x ** 2 for x in numbers]

        assert squares == [1, 4, 9, 16, 25]
        assert all(isinstance(x, int) for x in squares)
