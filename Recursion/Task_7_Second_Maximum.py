import unittest


def find_second_maximum(lst):
    if len(lst) < 2:
        raise ValueError("Должно быть хотя бы 2 элемента")
    return find_second_maximum_recursive(lst, 0, lst[0], lst[1])

def find_second_maximum_recursive(lst, index, first_max, second_max):
    if index == len(lst):
        if second_max == float('-inf'):
            raise ValueError("Список должен содержать хотя бы два различных элемента")
        return second_max

    current = lst[index]
    if current >= first_max:
        first_max, second_max = current, first_max
    elif current >= second_max:
        second_max = current

    return find_second_maximum_recursive(lst, index + 1, first_max, second_max)


class TestFindSecondMaximumRecursiveFunction(unittest.TestCase):
    def test_all_distinct_elements(self):
        self.assertEqual(find_second_maximum([2, 3, 5, 4]), 4)
        self.assertEqual(find_second_maximum([10, 20, 30, 40]), 30)
        self.assertEqual(find_second_maximum([5, 1, 2, 4, 3]), 4)

    def test_with_duplicates(self):
        self.assertEqual(find_second_maximum([2, 5, 4, 3, 5]), 5)
        self.assertEqual(find_second_maximum([7, 7, 6, 5, 6]), 7)
        self.assertEqual(find_second_maximum([1, 3, 3, 2]), 3)
        self.assertEqual(find_second_maximum([5, 5]), 5)

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            find_second_maximum([1])
        self.assertEqual(find_second_maximum([3, 3, 4]), 3)
        self.assertEqual(find_second_maximum([3, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
