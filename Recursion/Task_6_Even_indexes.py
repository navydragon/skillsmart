import unittest


def print_even_index_elements(lst, index):
    # Базовый случай
    if index >= len(lst):
        return
    # Если индекс четный, печатаем элемент
    if index % 2 == 0:
        print(lst[index])
    # Рекурсия
    print_even_index_elements(lst, index + 1)


# Вспомогательная функция для тестирования, чтобы собирать результаты в список
def get_even_index_elements(lst):
    result = []
    _collect_even_index_elements(lst, 0, result)
    return result


def _collect_even_index_elements(lst, index, result):
    if index >= len(lst):
        return
    if index % 2 == 0:
        result.append(lst[index])
    _collect_even_index_elements(lst, index + 1, result)


class TestPrintEvenIndexElementsFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_even_index_elements([]), [])

    def test_single_element(self):
        self.assertEqual(get_even_index_elements([1]), [1])

    def test_all_even_indices(self):
        self.assertEqual(get_even_index_elements([0, 1, 2, 3, 4, 5]), [0, 2, 4])

    def test_mixed_elements(self):
        self.assertEqual(get_even_index_elements(['a', 'b', 'c', 'd', 'e', 'f']), ['a', 'c', 'e'])

    def test_negative_numbers(self):
        self.assertEqual(get_even_index_elements([-1, -2, -3, -4, -5]), [-1, -3, -5])


if __name__ == '__main__':
    unittest.main()
