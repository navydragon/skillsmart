import unittest


def is_palindrome(s):
    # Удаляем все пробелы и приводим строку к нижнему регистру для корректного сравнения
    s = s.replace(" ", "").lower()

    # Базовый случай: строка с длиной 0 или 1 является палиндромом
    if len(s) <= 1:
        return True

    # Сравниваем первый и последний символы
    if s[0] != s[-1]:
        return False

    # Рекурсивно проверяем оставшуюся часть строки
    return is_palindrome(s[1:-1])


class TestIsPalindromeFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("aba"))
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("казак"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("рекурсия"))
        self.assertFalse(is_palindrome("hello"))

    def test_palindromes_with_spaces_and_capitals(self):
        self.assertTrue(is_palindrome("А роза упала на лапу Азора  "))
        self.assertTrue(is_palindrome("Аргентина манит негра"))
        self.assertTrue(is_palindrome("Во гробик довод киборгоВ"))

    def test_non_palindromes_with_spaces_and_capitals(self):
        self.assertFalse(is_palindrome("Какие числа считаются палиндромами?"))


if __name__ == '__main__':
    unittest.main()
