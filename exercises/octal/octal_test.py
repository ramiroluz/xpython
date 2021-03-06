"""Tests for the octal exercise

Implementation note:
If the string supplied to parse_octal cannot be parsed as an octal number
your program should raise a ValueError with a meaningful error message.
"""
import unittest

from octal import parse_octal


class OctalTest(unittest.TestCase):
    def test_octal_1_is_decimal_1(self):
        self.assertEqual(1, parse_octal("1"))

    def test_octal_10_is_decimal_8(self):
        self.assertEqual(8, parse_octal("10"))

    def test_octal_17_is_decimal_15(self):
        self.assertEqual(15, parse_octal("17"))

    def test_octal_130_is_decimal_88(self):
        self.assertEqual(88, parse_octal("130"))

    def test_octal_2047_is_decimal_1063(self):
        self.assertEqual(1063, parse_octal("2047"))

    def test_octal_1234567_is_decimal_342391(self):
        self.assertEqual(342391, parse_octal("1234567"))

    def test_8_is_seen_as_invalid(self):
        self.assertRaises(ValueError, parse_octal, "8")

    def test_invalid_octal_is_recognized(self):
        self.assertRaises(ValueError, parse_octal, "carrot")

    def test_6789_is_seen_as_invalid(self):
        self.assertRaises(ValueError, parse_octal, "6789")

    def test_valid_octal_formatted_string_011_is_decimal_9(self):
        self.assertEqual(9, parse_octal("011"))


if __name__ == '__main__':
    unittest.main()
