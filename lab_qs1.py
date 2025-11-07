import pytest

# -----------------------------
# Calculator functions
# -----------------------------
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b


# -----------------------------
# Tests for calculator
# -----------------------------
def test_addition():
    # Addition of positive and negative numbers
    assert add(5, 3) == 8
    assert add(-2, 5) == 3
    assert add(-4, -6) == -10

def test_division():
    # Division with proper error handling for zero
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

    # Check division by zero raises an error
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_multiplication():
    # Multiplication with decimal numbers
    assert multiply(2, 0.5) == 1.0
    assert multiply(1.5, 2) == 3.0
    assert multiply(-3, 2.5) == -7.5

def test_power():
    # Power operations
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(9, 0.5) == 3.0  # square root
