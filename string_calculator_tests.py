import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers_separated_by_comma(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_newlines_as_delimiters(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_single_character_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_custom_multi_character_delimiter(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)

    def test_negative_number_throws_exception(self):
        with self.assertRaisesRegex(ValueError, "negatives not allowed: -2"):
            self.calc.add("1,-2,3")

    def test_multiple_negative_numbers_throw_exception(self):
        with self.assertRaisesRegex(ValueError, "negatives not allowed: -2, -3"):
            self.calc.add("1,-2,-3")

    def test_numbers_greater_than_1000_are_ignored(self):
        self.assertEqual(self.calc.add("2,1001"), 2)


if __name__ == "__main__":
    unittest.main()
