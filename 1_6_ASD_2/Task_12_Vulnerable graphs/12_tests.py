import unittest
from SimpleGraph import SimpleGraph
class TestSimpleGraphWeakVertices(unittest.TestCase):

    def setUp(self):
        self.graph = SimpleGraph(9)
        for i in range(9):
            self.graph.AddVertex(i)

    def test_no_edges(self):
        # Граф:
        # 0   1   2
        # 3   4   5
        # 6   7   8
        # Ожидаемый результат: все вершины слабые
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_full_triangle(self):
        graph = SimpleGraph(3)
        for i in range(3):
            graph.AddVertex(i)
        # Граф:
        # 0 - 1
        #  \ /
        #   2
        # Ожидаемый результат: нет слабых вершин
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 0)
        weak_vertices = graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [])

    def test_partial_graph(self):
        graph = SimpleGraph(4)
        for i in range(4):
            graph.AddVertex(i)
        # Граф:
        # 0 - 1   2
        #  \ /
        #   3
        # Ожидаемый результат: 2 слабая вершина
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 3)
        graph.AddEdge(0, 3)
        weak_vertices = graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [2])

    def test_disconnected_graph(self):
        graph = SimpleGraph(5)
        for i in range(5):
            graph.AddVertex(i)
        # Граф:
        # 0 - 1   2 - 3
        #         |
        #         4
        # Ожидаемый результат: 0, 1, 2, 3, 4 слабые вершины
        graph.AddEdge(0, 1)
        graph.AddEdge(2, 3)
        graph.AddEdge(2, 4)
        weak_vertices = graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [0, 1, 2, 3, 4])

    def test_complex_graph(self):
        graph6 = SimpleGraph(6)
        for i in range(6):
            graph6.AddVertex(i)
        # Граф:
        # 0 - 1 - 2
        # |   | / |
        # 3 - 4 - 5
        # Ожидаемый результат: 0, 1, 2, 3, 4, 5 слабые вершины
        graph6.AddEdge(0, 1)
        graph6.AddEdge(1, 2)
        graph6.AddEdge(0, 3)
        graph6.AddEdge(1, 4)
        graph6.AddEdge(2, 4)
        graph6.AddEdge(2, 5)
        graph6.AddEdge(3, 4)
        graph6.AddEdge(4, 5)
        weak_vertices = graph6.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [0, 3])

    def test_grid_graph(self):
        # Граф:
        # 0 - 1 - 2
        # |   |   |
        # 3 - 4 - 5
        # |   |   |
        # 6 - 7 - 8
        # Ожидаемый результат: 0, 1, 2, 3, 4, 5, 6, 7, 8 слабые вершины
        edges = [
            (0, 1), (1, 2),
            (3, 4), (4, 5),
            (6, 7), (7, 8),
            (0, 3), (1, 4), (2, 5),
            (3, 6), (4, 7), (5, 8)
        ]
        for v1, v2 in edges:
            self.graph.AddEdge(v1, v2)
        weak_vertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weak_vertices], [0, 1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
