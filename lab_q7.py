# ============================================================================
# 7. MATHEMATICAL FUNCTION TESTING
# ============================================================================
from typing import List

import pytest


def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


def calculate_median(numbers: List[float]) -> float:
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    return sorted_numbers[n // 2]


def circle_area(radius: float) -> float:
    return 3.14159 * radius ** 2


class TestMathematicalFunctions:
    def test_fibonacci_generation(self):
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

    def test_prime_number_identification(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(4) is False
        assert is_prime(17) is True
        assert is_prime(20) is False
        assert is_prime(1) is False

    def test_mean_calculation(self):
        assert calculate_mean([1, 2, 3, 4, 5]) == 3.0
        assert calculate_mean([10, 20, 30]) == 20.0
        assert calculate_mean([5]) == 5.0

    def test_median_calculation(self):
        assert calculate_median([1, 2, 3, 4, 5]) == 3
        assert calculate_median([1, 2, 3, 4]) == 2.5
        assert calculate_median([5]) == 5

    def test_geometric_formulas(self):
        assert circle_area(1) == pytest.approx(3.14159, rel=0.01)
        assert circle_area(2) == pytest.approx(12.56636, rel=0.01)
        assert circle_area(5) == pytest.approx(78.53975, rel=0.01)
