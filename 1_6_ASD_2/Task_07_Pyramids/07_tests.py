import unittest
from Heap import Heap

class TestHeap(unittest.TestCase):

    def test_empty_heap(self):
        heap = Heap()
        heap.MakeHeap([], 0)
        self.assertEqual(heap.HeapArray, [None])
        self.assertEqual(heap.GetMax(), -1)
        # Пирамида: []

    def test_single_element_heap(self):
        heap = Heap()
        heap.MakeHeap([10], 0)
        self.assertEqual(heap.HeapArray, [10])
        self.assertEqual(heap.GetMax(), 10)
        self.assertEqual(heap.HeapArray, [None])
        # Пирамида:
        # [10]
        # []

    def test_two_elements_heap(self):
        heap = Heap()
        heap.MakeHeap([5, 10], 1)
        self.assertEqual(heap.HeapArray, [10, 5, None])
        self.assertEqual(heap.GetMax(), 10)
        self.assertEqual(heap.HeapArray, [5, None, None])
        # Пирамида:
        #    10
        #   /
        #  5
        # После удаления:
        #    5

    def test_three_elements_heap(self):
        heap = Heap()
        heap.MakeHeap([5, 10, 20], 1)
        self.assertEqual(heap.HeapArray, [20, 5, 10])
        self.assertEqual(heap.GetMax(), 20)
        self.assertEqual(heap.HeapArray, [10, 5, None])
        # Пирамида:
        #    20
        #   /  \
        #  5    10
        # После удаления:
        #    10
        #   /
        #  5

    def test_unbalanced_heap(self):
        heap = Heap()
        heap.MakeHeap([15, 10, 20, 17, 8], 2)
        self.assertEqual(heap.HeapArray, [20, 17, 15, 10, 8, None, None])
        self.assertEqual(heap.GetMax(), 20)
        self.assertEqual(heap.HeapArray, [17, 10, 15, 8, None, None, None])
        # Пирамида:
        #      20
        #     /  \
        #   17    15
        #   / \
        #  10  8
        # После удаления:
        #      17
        #     /  \
        #   10    15
        #   /
        #  8

    def test_add_element_to_heap(self):
        heap = Heap()
        heap.MakeHeap([15, 10, 20, 17, 8], 2)
        self.assertTrue(heap.Add(25))
        self.assertEqual(heap.HeapArray, [25, 17, 20, 10, 8, 15, None])
        self.assertTrue(heap.Add(30))
        self.assertEqual(heap.HeapArray, [30, 17, 25, 10, 8, 15, 20])
        self.assertFalse(heap.Add(35))  # Массив полностью заполнен
        # Пирамида после добавления:
        #      30
        #     /  \
        #   17    25
        #   / \   / \
        #  10  8 15 20

    def test_get_max_empty_heap(self):
        heap = Heap()
        self.assertEqual(heap.GetMax(), -1)
        # Пирамида: []


if __name__ == '__main__':
    unittest.main()
