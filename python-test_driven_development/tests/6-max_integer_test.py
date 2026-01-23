#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 2.4]), 2.5)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_equal_elements(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

if __name__ == "__main__":
    unittest.main()
