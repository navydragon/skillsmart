import unittest
from tasks.task3 import DynArray


class TestDynArray(unittest.TestCase):
    def setUp(self):
        self.arr = DynArray()

    def tearDown(self):
        del self.arr

    def test_index_error(self):
        arr = self.make_dummy_array(self.arr,15)
        self.assertRaises(IndexError, lambda: arr[16])
        self.assertRaises(IndexError, lambda: arr[-1])

    def test_index_error_insert(self):
        arr = self.make_dummy_array(self.arr, 10)
        self.assertRaises(IndexError, lambda: self.arr.insert(13, 99))
        self.assertRaises(IndexError, lambda: self.arr.insert(-1, 99))

    def test_index_error_delete(self):
        arr = self.make_dummy_array(self.arr, 10)
        self.assertRaises(IndexError, lambda: self.arr.delete(13))
        self.assertRaises(IndexError, lambda: self.arr.delete(-1))

    def test_insert_no_resize(self):
        arr = self.make_dummy_array(self.arr, 10)
        self.arr.insert(5, 99)
        self.assertEqual(self.arr[5], 99)
        self.assertEqual(len(self.arr), 11)
        self.assertEqual(self.arr.capacity, 16)

    def test_insert_with_resize(self):
        arr = self.make_dummy_array(self.arr, 16)
        self.arr.insert(8, 99)
        self.assertEqual(self.arr[8], 99)
        self.assertEqual(len(self.arr), 17)
        self.assertEqual(self.arr.capacity, 32)

    def test_insert_index_error(self):
        self.assertRaises(IndexError, lambda: self.arr.insert(1, 99))
        self.assertRaises(IndexError, lambda: self.arr.insert(-1, 99))

    def test_delete_no_resize(self):
        arr = self.make_dummy_array(self.arr, 10)
        self.arr.delete(5)
        self.assertEqual(len(self.arr), 9)
        self.assertEqual(self.arr.capacity, 16)

    def test_delete_with_resize(self):
        arr = self.make_dummy_array(self.arr, 64)
        for _ in range(33):
            self.arr.delete(0)
        self.assertEqual(len(self.arr), 31)
        self.assertEqual(self.arr.capacity, 42)

    def test_insert_index_error_in_empty_array(self):
        self.arr.insert(0,99)
        self.assertEqual(self.arr.count,1)


    @staticmethod
    def make_dummy_array(arr: DynArray, val: int):
        for i in range(0,val):
            arr.append(i+1)
        return arr


if __name__ == '__main__':
    unittest.main()