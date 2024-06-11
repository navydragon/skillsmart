import unittest
from tasks.task12 import NativeCache


class TestNativeCache(unittest.TestCase):

    def setUp(self):
        self.cache = NativeCache(5)

    def test_put_and_get(self):
        self.cache.put("a", 1)
        self.cache.put("b", 2)
        self.cache.put("c", 3)
        self.assertEqual(self.cache.get("a"), 1)
        self.assertEqual(self.cache.get("b"), 2)
        self.assertEqual(self.cache.get("c"), 3)
        self.assertEqual(self.cache.get("d"), None)

    def test_eviction(self):
        self.cache.put("a", 1)
        self.cache.put("b", 2)
        self.cache.put("c", 3)
        self.cache.put("d", 4)
        self.cache.put("e", 5)
        self.cache.put("f", 6)
        self.assertEqual(self.cache.size, 5)

    def test_hits(self):
        self.cache.put("a", 1)
        self.cache.put("b", 2)
        self.cache.put("c", 3)
        self.cache.get("a")
        self.cache.get("a")
        self.cache.get("b")
        self.cache.put("d", 4)
        self.cache.put("e", 5)
        self.cache.put("f", 6)
        self.assertEqual(self.cache.get("a"), 1)  # "a" не вытеснен
        self.assertEqual(self.cache.get("b"), 2)  # "b" не вытеснен
        self.assertEqual(self.cache.get("c"), 3)  # "c" не вытеснен

if __name__ == '__main__':
    unittest.main()