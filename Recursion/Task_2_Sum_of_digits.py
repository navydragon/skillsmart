import unittest


def sum_of_digits(n):
    # Работаем с абсолютным значением, чтобы поддерживать отрицательные числа
    n = abs(n)
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


class TestSumOfDigitsFunction(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(sum_of_digits(5), 5)
        self.assertEqual(sum_of_digits(9), 9)
        self.assertEqual(sum_of_digits(0), 0)

    def test_multiple_digits(self):
        self.assertEqual(sum_of_digits(123), 6)  # 1 + 2 + 3 = 6
        self.assertEqual(sum_of_digits(4567), 22)  # 4 + 5 + 6 + 7 = 22
        self.assertEqual(sum_of_digits(1001), 2)  # 1 + 0 + 0 + 1 = 2

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits(-123), 6)  # -123 -> 1 + 2 + 3 = 6
        self.assertEqual(sum_of_digits(-4567), 22)  # -4567 -> 4 + 5 + 6 + 7 = 22


if __name__ == '__main__':
    unittest.main()
