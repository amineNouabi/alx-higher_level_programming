#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [10, 9, 100, 3]
        self.assertEqual(max_integer(unordered), 100)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [88, 7, 4, 22, 11]
        self.assertEqual(max_integer(max_at_beginning), 88)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [8]
        self.assertEqual(max_integer(one_element), 8)

    def test_floats(self):
        """Test a list of floats."""
        floats = [7.78, 6.33, 2.123, 18.2, 67.99]
        self.assertEqual(max_integer(floats), 67.99)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [2.14, 15, -10.3, 12.5, -2]
        self.assertEqual(max_integer(ints_and_floats), 15)

    def test_string(self):
        """Test a string."""
        string = "azerty"
        self.assertEqual(max_integer(string), 'z')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["qwerty", "layout", "is", "the", "best"]
        self.assertEqual(max_integer(strings), "the")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
