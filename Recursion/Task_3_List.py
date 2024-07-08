import unittest


def recursive_len(lst):
    # Базовый случай: если список пуст, его длина равна 0
    if not lst:
        return 0
    # Удаляем первый элемент и рекурсивно вычисляем длину оставшегося списка
    lst.pop(0)
    return 1 + recursive_len(lst)


class TestRecursiveLenFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(recursive_len([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_len([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(recursive_len([1, 2, 3, 4, 5]), 5)
        self.assertEqual(recursive_len(['a', 'b', 'c']), 3)
        self.assertEqual(recursive_len([0, 0, 0, 0]), 4)

    def test_nested_lists(self):
        self.assertEqual(recursive_len([[1, 2], [3, 4], [5]]), 3)


if __name__ == '__main__':
    unittest.main()
