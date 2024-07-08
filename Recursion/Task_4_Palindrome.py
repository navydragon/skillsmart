import unittest


def is_palindrome(s, left=None, right=None):
    # очищаем строку при первом вызове
    if left is None and right is None:
        s = s.replace(" ", "").lower()
        left = 0
        right = len(s) - 1

    # Базовый случай
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    # рекурсия
    return is_palindrome(s, left + 1, right - 1)


class TestIsPalindromeFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("aba"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("abc"))
        self.assertFalse(is_palindrome("hello"))

    def test_palindromes_with_spaces_and_capitals(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("No lemon no melon"))

    def test_non_palindromes_with_spaces_and_capitals(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))


if __name__ == '__main__':
    unittest.main()
