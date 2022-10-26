#!/usr/bin/env python3
from unittest import TestCase
import unittest
from EX2003 import calculate_factorial

class MyTests(TestCase):

    def _assert(self, inp, expected):
        actual = calculate_factorial(inp)
        self.assertEqual(actual, expected)

    # return none
    def test_return_none(self):
        self.assertIsNone(calculate_factorial(None))
    
    # if not possible to convert to int -> error
    def test_string(self):
        self.assertRaises(TypeError, calculate_factorial, 's')

    def test_negative_numbers_integer(self):
        self.assertRaises(ValueError, calculate_factorial, -1)

    def test_negative_numbers_string(self):
        self.assertRaises(ValueError, calculate_factorial, "-1")

    def test_number_too_large_integer(self):
        self.assertRaises(ValueError, calculate_factorial, 11)

    def test_number_too_large_string(self):
        self.assertRaises(ValueError, calculate_factorial, "11")

    def test_case_zero_integer(self):
        self._assert(0, 1)

    def test_case_zero_string(self):
        self._assert("0", 1)

    def test_larger_than_zero_integer(self):
        self._assert(7, 5040)

    def test_larger_than_zero_string(self):
        self._assert("7", 5040)