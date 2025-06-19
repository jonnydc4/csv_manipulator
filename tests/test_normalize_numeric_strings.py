import unittest
from src.transformations.main import normalize_numeric_strings

class TestNormalizeNumericStrings(unittest.TestCase):

    def test_basic_numbers(self):
        data = [["1", "2.5", "3.4567"]]
        expected = [["1.00", "2.50", "3.46"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_leading_trailing_whitespace(self):
        data = [["  42 ", " 3.14  "]]
        expected = [["42.00", "3.14"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_scientific_notation(self):
        data = [["1e3", "5E2"]]
        expected = [["1000.00", "500.00"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_commas_in_numbers(self):
        data = [["1,000", "2,345.67"]]
        expected = [["1000.00", "2345.67"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_currency_symbols(self):
        data = [["$123.45", "$1,000.00"]]
        expected = [["123.45", "1000.00"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_negative_currency(self):
        data = [["-$123.45", "$-123.45"]]
        expected = [["-123.45", "-123.45"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_negative_numbers(self):
        data = [["-42", "-1,000", "-$2,000.00"]]
        expected = [["-42.00", "-1000.00", "-2000.00"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_preserve_non_numeric_strings(self):
        data = [["hello", "", " "]]
        expected = [["hello", "", " "]]
        self.assertEqual(normalize_numeric_strings(data), expected)

    def test_mixed_content(self):
        data = [["hello", "", " ", "$12.34", "-123", "1e2"]]
        expected = [["hello", "", " ", "12.34", "-123.00", "100.00"]]
        self.assertEqual(normalize_numeric_strings(data), expected)

if __name__ == "__main__":
    unittest.main()
