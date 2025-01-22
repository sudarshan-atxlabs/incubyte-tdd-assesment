class StringCalculator:
    def add(self, numbers: str) -> int:
        """
        Computes the sum of numbers provided as a string separated by commas.

        Args:
            numbers (str): The input string containing numbers separated by commas.

        Returns:
            int: The sum of the numbers in the input string.
        """
        if not numbers:
            return 0

        number_list = numbers.split(",")
        return sum(int(num) for num in number_list if num)


# Unit tests
import unittest

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0."""
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_its_value(self):
        """Test that a single number returns its integer value."""
        self.assertEqual(self.calculator.add("5"), 5)

    def test_two_numbers_comma_separated(self):
        """Test that two comma-separated numbers are summed correctly."""
        self.assertEqual(self.calculator.add("1,2"), 3)

if __name__ == "__main__":
    unittest.main()
