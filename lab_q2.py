# ============================================================================
# 2. STRING MANIPULATION ASSERTIONS (Wikipedia Example)
# ============================================================================

import requests


def fetch_page_text(url: str) -> str:
    """Fetches the page content from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text


class TestStringManipulations:
    def setup_method(self):
        """Setup runs before each test."""
        self.url = "https://www.wikipedia.org"
        self.page_text = fetch_page_text(self.url)

    def test_extract_and_verify_page_title(self):
        """Extract and verify the page title."""
        start = self.page_text.find("<title>") + len("<title>")
        end = self.page_text.find("</title>")
        title = self.page_text[start:end].strip()

        # Assertions
        assert "Wikipedia" in title
        assert len(title) > 5
#
#     def test_check_specific_text_exists(self):
#         """Check if specific text exists on the page."""
#         assert "Wikipedia" in self.page_text
#         assert "encyclopedia" in self.page_text.lower()  # case-insensitive
#
#     def test_verify_string_length_constraints(self):
#         """Verify that the page text length is within expected range."""
#         length = len(self.page_text)
#         assert length > 1000, f"Page content too short: {length}"
#         assert length < 1000000, f"Page content too long: {length}"
#
#     def test_case_sensitivity_in_text_comparisons(self):
#         """Test case sensitivity in text comparisons."""
#         assert "Wikipedia" in self.page_text
#         assert "wikipedia" not in self.page_text  # case-sensitive test
