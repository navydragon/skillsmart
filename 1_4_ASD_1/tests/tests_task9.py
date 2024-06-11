import unittest
from tasks.task9 import NativeDictionary

class TestNativeDictionary(unittest.TestCase):
    def setUp(self):
        self.dict_ = NativeDictionary(10)
        self.dict_2 = NativeDictionary(1)
    def test_empty_dictionary(self):
        self.assertIsNone(self.dict_2.get('key1'))
        self.assertEqual(self.dict_2.is_key('key1'),False)
    def test_put_and_get(self):
        self.dict_.put('key1', 1)
        self.assertEqual(self.dict_.get('key1'), 1)
        self.dict_.put('key1', 2)
        self.assertEqual(self.dict_.get('key1'), 2)
        self.dict_.put('key2', 3)
        self.assertEqual(self.dict_.get('key2'), 3)
        self.assertEqual(self.dict_.get('key1'), 2)

    def test_is_key(self):
        self.assertFalse(self.dict_.is_key('key1'))
        self.dict_.put('key1', 1)
        self.assertTrue(self.dict_.is_key('key1'))

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.dict_.get('key1'))

    def test_large_number_of_keys(self):
        for i in range(10):
            self.dict_.put(f'key{i}', i)
        for i in range(10):
            self.assertEqual(self.dict_.get(f'key{i}'), i)

if __name__ == '__main__':
    unittest.main()