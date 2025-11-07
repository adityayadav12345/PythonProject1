import pytest


# ============================================
# Calculator Functions (System Under Test)
# ============================================

class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def multiply(self, a, b):
        return a * b

    def power(self, a, b):
        return a ** b


# ============================================
# Fixtures
# ============================================

@pytest.fixture(scope="module")
def calc():
    print("\n[Setup] Initializing Calculator instance")
    calculator = Calculator()
    yield calculator
    print("\n[Teardown] Cleaning up Calculator instance")


@pytest.fixture(scope="function")
def sample_data():
    return {
        "integers": (5, 3),
        "floats": (2.5, 0.5),
        "mixed": (-2, 4)
    }


# ============================================
# Test Groups using Markers
# ============================================

@pytest.mark.addition
def test_addition(calc, sample_data):
    a, b = sample_data["integers"]
    assert calc.add(a, b) == 8
    assert calc.add(-2, 5) == 3
    assert calc.add(-4, -6) == -10

@pytest.mark.calculation
@pytest.mark.division
def test_division(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3

    # Verify error handling
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


@pytest.mark.multiplication
def test_multiplication(calc, sample_data):
    a, b = sample_data["floats"]
    assert calc.multiply(a, b) == 1.25

    a, b = sample_data["mixed"]
    assert calc.multiply(a, b) == -8

@pytest.mark.calculation
@pytest.mark.power
def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(9, 0.5) == 3.0  # square root
