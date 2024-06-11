import unittest
from tasks.task8 import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10, 3)

    def test_hash_fun(self):
        self.assertEqual(self.hash_table.hash_fun("test"), sum(ord(char) for char in "test") % 10)

    def test_put_and_find(self):
        self.assertIsNotNone(self.hash_table.put("test"))
        self.assertIsNotNone(self.hash_table.find("test"))
        self.assertIsNone(self.hash_table.find("nonexistent"))

    def test_collisions(self):
        self.assertIsNotNone(self.hash_table.put("collision1"))
        self.assertIsNotNone(self.hash_table.put("collision2"))
        self.assertIsNotNone(self.hash_table.find("collision1"))
        self.assertIsNotNone(self.hash_table.find("collision2"))

if __name__ == '__main__':
    unittest.main()
