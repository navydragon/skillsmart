import unittest
from tasks.task10 import PowerSet


class TestPowerSet(unittest.TestCase):

    def setUp(self):
        self.p1 = PowerSet()
        self.p2 = PowerSet()

    def test_put(self):
        self.p1.put(1)
        self.p1.put(2)
        self.p1.put(2)
        self.assertEqual(self.p1.size(), 2)
        self.assertTrue(self.p1.get(1))
        self.assertFalse(self.p1.get(3))

    def test_remove(self):
        self.p1.put(1)
        self.p1.put(2)
        self.assertTrue(self.p1.remove(1))
        self.assertEqual(self.p1.size(), 1)
        self.assertFalse(self.p1.get(1))
        self.assertFalse(self.p1.remove(3))

    def test_intersection(self):
        self.p1.put(1)
        self.p1.put(2)
        self.p2.put(1)
        self.p2.put(3)
        result = self.p1.intersection(self.p2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get(1))
        self.assertFalse(result.get(2))
        self.assertFalse(result.get(3))

    def test_union(self):
        self.p1.put(1)
        self.p1.put(2)
        self.p2.put(2)
        self.p2.put(3)
        result = self.p1.union(self.p2)
        self.assertEqual(result.size(), 3)
        self.assertTrue(result.get(1))
        self.assertTrue(result.get(2))
        self.assertTrue(result.get(3))

    def test_difference(self):
        self.p1.put(1)
        self.p1.put(2)
        self.p2.put(2)
        self.p2.put(3)
        result = self.p1.difference(self.p2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get(1))
        self.assertFalse(result.get(2))

    def test_issubset(self):
        self.p1.put(1)
        self.p1.put(2)
        self.p2.put(1)
        self.assertTrue(self.p1.issubset(self.p2))
        self.p2.put(3)
        self.assertFalse(self.p1.issubset(self.p2))
        self.p1.put(3)
        self.assertTrue(self.p1.issubset(self.p2))



if __name__ == '__main__':
    unittest.main()
