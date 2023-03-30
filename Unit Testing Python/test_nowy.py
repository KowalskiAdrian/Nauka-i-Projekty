def is_even(num):
    return num % 2 == 0

import unittest

class TestIsEven(unittest.TestCase):
    def test_is_even_true(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))

    def test_is_even_false(self):
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(7))
