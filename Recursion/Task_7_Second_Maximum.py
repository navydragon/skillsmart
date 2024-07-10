import unittest


def find_second_maximum_recursive(lst):
    if len(lst) < 2:
        raise ValueError("Должно быть хотя бы 2 элемента")

    def helper(index, first_max, second_max):
        if index == len(lst):
            return second_max

        current = lst[index]
        if current >= first_max:
            return helper(index + 1, current, first_max)
        elif current >= second_max:
            return helper(index + 1, first_max, current)
        else:
            return helper(index + 1, first_max, second_max)

    return helper(0, float('-inf'), float('-inf'))


class TestFindSecondMaximumRecursiveFunction(unittest.TestCase):
    def test_all_distinct_elements(self):
        self.assertEqual(find_second_maximum_recursive([2, 3, 5, 4]), 4)
        self.assertEqual(find_second_maximum_recursive([10, 20, 30, 40]), 30)
        self.assertEqual(find_second_maximum_recursive([5, 1, 2, 4, 3]), 4)

    def test_with_duplicates(self):
        self.assertEqual(find_second_maximum_recursive([2, 5, 4, 3, 5]), 5)
        self.assertEqual(find_second_maximum_recursive([7, 7, 6, 5, 6]), 7)
        self.assertEqual(find_second_maximum_recursive([1, 3, 3, 2]), 3)
        self.assertEqual(find_second_maximum_recursive([5, 5]), 5)

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            find_second_maximum_recursive([1])
        self.assertEqual(find_second_maximum_recursive([3, 3, 4]), 3)
        self.assertEqual(find_second_maximum_recursive([3, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
