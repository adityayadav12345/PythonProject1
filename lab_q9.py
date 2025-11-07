# ============================================================================
# 9. DATE & TIME ASSERTIONS
# ============================================================================

from datetime import datetime


def days_between(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days)


def calculate_age(birth_date: datetime) -> int:
    today = datetime.now()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def format_date(date: datetime, format_string: str) -> str:
    return date.strftime(format_string)


class TestDateTimeFunctions:
    def test_date_comparisons(self):
        date1 = datetime(2024, 1, 1)
        date2 = datetime(2024, 1, 10)

        assert date2 > date1
        assert date1 < date2
        assert date1 != date2

    def test_date_differences(self):
        date1 = datetime(2024, 1, 1)
        date2 = datetime(2024, 1, 11)

        assert days_between(date1, date2) == 10
        assert days_between(date2, date1) == 10

    def test_date_formatting(self):
        test_date = datetime(2024, 3, 15)

        assert format_date(test_date, "%Y-%m-%d") == "2024-03-15"
        assert format_date(test_date, "%d/%m/%Y") == "15/03/2024"
        assert format_date(test_date, "%B %d, %Y") == "March 15, 2024"

    def test_age_calculation(self):
        birth_date = datetime(2000, 1, 1)
        age = calculate_age(birth_date)

        assert isinstance(age, int)
        assert age >= 24  # As of 2024
