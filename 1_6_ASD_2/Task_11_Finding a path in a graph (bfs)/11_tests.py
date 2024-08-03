import unittest
from SimpleGraph import SimpleGraph
class TestSimpleGraphBFS(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(5)
        for i in range(5):
            self.graph.AddVertex(i)
        # Добавляем рёбра для создания графа
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(3, 4)

    def test_direct_path(self):
        # Граф:
        # 0 - 1 - 2 - 3 - 4
        path = self.graph.BreadthFirstSearch(0, 4)
        self.assertEqual(len(path), 5)
        # Ожидаемый результат: длина пути 5

    def test_reverse_path(self):
        # Граф:
        # 4 - 3 - 2 - 1 - 0
        path = self.graph.BreadthFirstSearch(4, 0)
        self.assertEqual(len(path), 5)
        # Ожидаемый результат: длина пути 5

    def test_no_path(self):
        self.graph.RemoveEdge(1, 2)
        # Граф:
        # 0 - 1   2 - 3 - 4
        path = self.graph.BreadthFirstSearch(0, 4)
        self.assertEqual(path, [])
        # Ожидаемый результат: []

    def test_cycle_graph(self):
        self.graph.AddEdge(4, 0)
        # Граф:
        # 0 - 1 - 2 - 3 - 4
        # |______________|
        path = self.graph.BreadthFirstSearch(0, 3)
        self.assertEqual(len(path), 3)
        # Ожидаемый результат: длина пути 4

    def test_disconnected_graph(self):
        self.graph = SimpleGraph(6)
        for i in range(6):
            self.graph.AddVertex(i)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(2, 3)
        self.graph.AddEdge(4, 5)
        # Граф:
        # 0 - 1   2 - 3   4 - 5
        path = self.graph.BreadthFirstSearch(0, 5)
        self.assertEqual(path, [])
        # Ожидаемый результат: []

    def test_grid_graph(self):
        self.graph = SimpleGraph(9)
        for i in range(9):
            self.graph.AddVertex(i)
        # Добавляем рёбра для создания графа в виде квадрата 3x3
        edges = [
            (0, 1), (1, 2),  # Верхняя строка
            (3, 4), (4, 5),  # Средняя строка
            (6, 7), (7, 8),  # Нижняя строка
            (0, 3), (1, 4), (2, 5),  # Левый столбец
            (3, 6), (4, 7), (5, 8)  # Правый столбец
        ]
        for v1, v2 in edges:
            self.graph.AddEdge(v1, v2)

        # Граф:
        # 0 - 1 - 2
        # |   |   |
        # 3 - 4 - 5
        # |   |   |
        # 6 - 7 - 8

        path = self.graph.BreadthFirstSearch(0, 8)
        self.assertEqual(len(path), 5)
        # Ожидаемый результат: длина пути 5

    def test_same_vertex(self):
        # Граф:
        # 0 - 1 - 2 - 3 - 4
        path = self.graph.BreadthFirstSearch(0, 0)
        self.assertEqual(len(path), 1)
        # Ожидаемый результат: длина пути 1 (сам на себя)

if __name__ == '__main__':
    unittest.main()
