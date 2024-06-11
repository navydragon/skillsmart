import unittest
from tasks.task11 import BloomFilter

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloom = BloomFilter()

    def test_add_and_contains(self):
        test_strings = [
            "0123456789", "1234567890", "2345678901",
            "3456789012", "4567890123", "5678901234",
            "6789012345", "7890123456", "8901234567",
            "9012345678"
        ]

        for string in test_strings:
            self.bloom.add(string)
            self.assertTrue(self.bloom.is_value(string))

        # Проверка ложноположительных срабатываний
        false_strings = ["abcdefghij", "klmnopqrst"]
        for string in false_strings:
            self.assertFalse(self.bloom.is_value(string))


if __name__ == '__main__':
    unittest.main()