import unittest


def print_even_numbers(lst, index):
    if index >= len(lst):
        return
    if lst[index] % 2 == 0:
        print(lst[index])
    print_even_numbers(lst, index + 1)

# Вспомогательная функция для тестирования, чтобы собирать результаты в список
def get_even_numbers(lst):
    result = []
    _collect_even_numbers(lst, 0, result)
    return result

def _collect_even_numbers(lst, index, result):
    if index >= len(lst):
        return
    if lst[index] % 2 == 0:
        result.append(lst[index])
    _collect_even_numbers(lst, index + 1, result)



class TestPrintEvenNumbersFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_even_numbers([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(get_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_all_odd_numbers(self):
        self.assertEqual(get_even_numbers([1, 3, 5, 7]), [])

    def test_mixed_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_negative_numbers(self):
        self.assertEqual(get_even_numbers([-2, -3, -4, -5]), [-2, -4])


if __name__ == '__main__':
    unittest.main()
