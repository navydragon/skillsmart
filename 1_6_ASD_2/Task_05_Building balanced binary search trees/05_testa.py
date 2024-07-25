import unittest
from GenerateBBSTArray import GenerateBBSTArray

class TestGenerateBBSTArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_single_element_array(self):
        self.assertEqual(GenerateBBSTArray([10]), [10])

    def test_two_elements_array(self):
        self.assertEqual(GenerateBBSTArray([10, 5]), [5, None, 10])

    def test_three_elements_array(self):
        self.assertEqual(GenerateBBSTArray([10, 5, 15]), [10, 5, 15])

    def test_unbalanced_four_elements_array(self):
        self.assertEqual(GenerateBBSTArray([10, 5, 15, 2]), [5, 2, 10, None, None, None, 15])

    def test_balanced_seven_elements_array(self):
        self.assertEqual(GenerateBBSTArray([4, 2, 6, 1, 3, 5, 7]), [4, 2, 6, 1, 3, 5, 7])

    def test_large_array(self):
        arr = list(range(1, 16))  # Полный массив для дерева глубины 3
        expected = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(GenerateBBSTArray(arr), expected)

    def test_duplicate_elements_array(self):
        self.assertEqual(GenerateBBSTArray([10, 10, 10]), [10, 10, 10])

if __name__ == '__main__':
    unittest.main()
