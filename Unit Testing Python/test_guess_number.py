import random
import unittest
from unittest.mock import patch

def guess_number(odp):
    if odp == 7:
        return "Zgadłeś!"
    elif odp < 7:
        return "Za mało"
    else:
        return "Za dużo"
    
class TestGuessNumber(unittest.TestCase):
    def test_guess_number(self):
        self.assertEqual(guess_number(5), "Za mało")
        self.assertEqual(guess_number(7), "Zgadłeś!")
        self.assertEqual(guess_number(10), "Za dużo")


if __name__ == '__main__':
    unittest.main()
