import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class StringCalculator:
    def __init__(self):
        """
        Initializes the StringCalculator with default delimiters (comma and newline).
        """
        self.default_delimiters = [",", "\n"]
        logging.info("StringCalculator initialized with default delimiters: %s", self.default_delimiters)

    def add(self, numbers: str) -> int:
        """
        Computes the sum of numbers provided as a string.
        Supports default (comma, newline) and custom delimiters.

        Args:
            numbers (str): The input string containing numbers separated by delimiters.

        Returns:
            int: The sum of the numbers in the input string.
        """
        logging.info("Adding numbers: %s", numbers)

        if not numbers:
            logging.info("Input is empty, returning 0.")
            return 0

        # Extract custom delimiter if present
        custom_delimiter, numbers = self._extract_custom_delimiter(numbers)

        # Combine default delimiters with custom delimiter
        delimiters = self.default_delimiters.copy()
        if custom_delimiter:
            delimiters.append(custom_delimiter)

        # Split numbers and compute the sum
        number_list = self._split_numbers(numbers, delimiters)
        total = sum(self._to_int(num) for num in number_list if num)
        logging.info("Computed sum: %d", total)
        return total

    def _extract_custom_delimiter(self, numbers: str) -> (str, str):
        """
        Extracts a custom delimiter from the input string if it is specified.

        Args:
            numbers (str): The input string.

        Returns:
            Tuple[str, str]: A tuple containing the custom delimiter (if any) and the remaining number string.
        """
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split("\n", 1)
            custom_delimiter = delimiter_section[2:]
            logging.info("Custom delimiter detected: %s", custom_delimiter)
            return custom_delimiter, numbers
        return None, numbers

    def _split_numbers(self, numbers: str, delimiters: list) -> list:
        """
        Splits the input string into a list of numbers based on the provided delimiters.

        Args:
            numbers (str): The string of numbers to split.
            delimiters (list): A list of delimiters to use for splitting.

        Returns:
            list: A list of numbers as strings.
        """
        split_pattern = "|".join(map(re.escape, delimiters))
        split_numbers = re.split(split_pattern, numbers)
        logging.debug("Numbers split into: %s", split_numbers)
        return split_numbers

    def _to_int(self, number: str) -> int:
        """
        Converts a string to an integer, raising a ValueError if the string is invalid.

        Args:
            number (str): The string to convert.

        Returns:
            int: The converted integer.

        Raises:
            ValueError: If the input string is not a valid number.
        """
        try:
            return int(number)
        except ValueError:
            logging.error("Invalid number encountered: %s", number)
            raise ValueError(f"Invalid number: {number}")


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

    def test_invalid_number_raises_exception(self):
        """Test that invalid numbers raise a ValueError."""
        with self.assertRaises(ValueError):
            self.calculator.add("1,abc")

    def test_invalid_custom_delimiter_number(self):
        """Test that invalid numbers with custom delimiters raise a ValueError."""
        with self.assertRaises(ValueError):
            self.calculator.add("//*\n4*abc*6")

    def test_multiple_custom_delimiters(self):
        """Test support for multiple custom delimiters."""
        self.assertEqual(self.calculator.add("//;\n1;2;3\n4"), 10)

    def test_large_numbers(self):
        """Test handling of large numbers."""
        self.assertEqual(self.calculator.add("1000,2000,3000"), 6000)

    def test_consecutive_delimiters(self):
        """Test consecutive delimiters."""
        self.assertEqual(self.calculator.add("1,,2"), 3)

    def test_whitespace_around_numbers(self):
        """Test numbers with surrounding whitespace."""
        self.assertEqual(self.calculator.add(" 1 , 2 "), 3)


if __name__ == "__main__":
    unittest.main()
