import unittest
from tasks.task5 import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = Queue()
        values = [10, 20, 30, 40, 50]
        for value in values:
            queue.enqueue(value)

        self.assertEqual(len(values), queue.size())
        for value in values:
            a = queue.dequeue()
            self.assertEqual(value, a)
        self.assertEqual(0, queue.size())

    def test_enqueue_dequeue_big(self):
        queue = Queue()
        for i in range(10000):
            queue.enqueue(i + 1)

        for i in range(10000):
            queue.enqueue(queue.dequeue())

        self.assertEqual(10000, queue.size())

    def test_dequeue_empty(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())



if __name__ == '__main__':
    unittest.main()