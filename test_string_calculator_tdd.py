import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        """
        Computes the sum of numbers provided as a string.
        Supports default (comma, newline) and custom delimiters.

        Args:
            numbers (str): The input string containing numbers separated by delimiters.

        Returns:
            int: The sum of the numbers in the input string.
        """
        if not numbers:
            return 0

        # Check for custom delimiter
        custom_delimiter = None
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split("\n", 1)
            custom_delimiter = re.escape(delimiter_section[2:])

        # Combine default delimiters with custom delimiter (if any)
        delimiters = [",", "\n"]
        if custom_delimiter:
            delimiters.append(custom_delimiter)

        # Split numbers using the delimiters
        split_pattern = "|".join(map(re.escape, delimiters))
        number_list = re.split(split_pattern, numbers)
        return sum(int(num) for num in number_list if num)


# Unit tests
import unittest

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_its_value(self):
        self.assertEqual(self.calculator.add("5"), 5)

    def test_two_numbers_comma_separated(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers_with_commas_and_newlines(self):
        self.assertEqual(self.calculator.add("1,2\n3"), 6)

    def test_custom_delimiter(self):
        """Test that a custom delimiter can be used."""
        self.assertEqual(self.calculator.add("//;\n1;2;3"), 6)
        self.assertEqual(self.calculator.add("//*\n4*5*6"), 15)

if __name__ == "__main__":
    unittest.main()