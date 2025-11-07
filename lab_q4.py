# ============================================================================
# 4. EXCEPTION HANDLING TESTS
# ============================================================================
import pytest


class CustomError(Exception):
    """Custom exception for testing"""
    pass


def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Cannot convert {value} to integer")


def raise_custom_error():
    raise CustomError("This is a custom error message")


class TestExceptionHandling:
    def test_division_by_zero_exception(self):
        with pytest.raises(ZeroDivisionError) as exc_info:
            divide_numbers(10, 0)
        assert "not allowed" in str(exc_info.value)

    def test_file_not_found_exception(self):
        with pytest.raises(FileNotFoundError) as exc_info:
            read_file("nonexistent_file.txt")
        assert "not found" in str(exc_info.value)

    def test_invalid_type_conversion(self):
        with pytest.raises(ValueError):
            convert_to_int("abc")

        with pytest.raises(ValueError):
            convert_to_int("12.5.6")

    def test_custom_exception(self):
        with pytest.raises(CustomError) as exc_info:
            raise_custom_error()
        assert "custom error message" in str(exc_info.value)
