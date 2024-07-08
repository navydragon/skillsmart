import unittest


def power(base, degree):
    if degree == 0:
        return 1
    elif degree < 0:
        if base == 0:
            raise ValueError("Значение 0 не может быть возведено в отрицательную степень")
        return 1 / power(base, -degree)
    else:
        return base * power(base, degree - 1)


class TestPowerFunction(unittest.TestCase):
    def test_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 4), 625)
        self.assertEqual(power(3, 2), 9)

    def test_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 0), 1)

    def test_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(5, -1), 0.2)
        self.assertAlmostEqual(power(3, -3), 1 / 27)

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            power(0, -1)

        self.assertEqual(power(0, 5), 0)


if __name__ == '__main__':
    unittest.main()
