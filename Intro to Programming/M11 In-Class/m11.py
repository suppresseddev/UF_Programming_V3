import unittest as ut
from functions import *
class m11Tests(ut.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

        #Test Case 2 says is_prime(-1) is true <- fiction
        #Test Case 1 says is_prime(-1) is false <- reality

        # self.assertTrue(is_prime(-1))
        self.assertFalse(is_prime(-11))
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("Apple"), "ppl")
        self.assertEqual(remove_vowels("Pancake"), "Pnck")
        self.assertEqual(remove_vowels("Yapper"), "Yppr")
        self.assertEqual(remove_vowels("AEIOU"), "")
        self.assertEqual(remove_vowels("lynn"), "lynn")