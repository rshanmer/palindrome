''' Tests for Permutations '''

import unittest

from palindrome import Palindrome 

class TestTestCase(unittest.TestCase):
    def setUp(self):
        self.pal = Palindrome()

    def test_testtest(self):
        result = self.pal.test_test("A")
        self.assertTrue(result == "A")

    def test_generate_permutations(self):
        result = self.pal.generate_permutations("a b")
        self.assertTrue(result == ["a","b","ab","ba"])
        result = self.pal.generate_permutations("a b c")
        self.assertTrue(result == ['a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca',
        'cb', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_check_palindromes(self):
        self.assertTrue(self.pal.check_palindrome("a"))
        self.assertTrue(self.pal.check_palindrome("9"))
        self.assertTrue(self.pal.check_palindrome("aa"))
        self.assertTrue(self.pal.check_palindrome("aba"))
        self.assertTrue(self.pal.check_palindrome("abba"))
        self.assertTrue(self.pal.check_palindrome("1234321"))
        self.assertFalse(self.pal.check_palindrome("ab"))
        self.assertFalse(self.pal.check_palindrome("98"))
        self.assertFalse(self.pal.check_palindrome("abca"))
        self.assertFalse(self.pal.check_palindrome("abcda"))
        self.assertFalse(self.pal.check_palindrome("1234521"))

    def test_look_for_palindromes(self):
        result = self.pal.look_for_palindromes(["ab","aba","abcb","abcba"])
        self.assertTrue(result == ["aba","abcba"])

if __name__ == '__main__':
    unittest.main()

