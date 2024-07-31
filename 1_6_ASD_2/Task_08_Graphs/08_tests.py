import unittest
from SimpleGraph import SimpleGraph

class TestSimpleGraph(unittest.TestCase):

    def test_add_vertex(self):
        graph = SimpleGraph(3)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)

        # Проверка, что вершины добавлены
        self.assertEqual(graph.vertex[0].Value, 10)
        self.assertEqual(graph.vertex[1].Value, 20)
        self.assertEqual(graph.vertex[2].Value, 30)
        self.assertRaises(ValueError, graph.AddVertex, 40)  # Нет свободного места для добавления вершины
        # Граф:
        # 10  20  30

    def test_add_edge(self):
        graph = SimpleGraph(3)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        # Проверка наличия рёбер
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(0, 2))
        # Граф:
        # 10 -- 20 -- 30

    def test_remove_edge(self):
        graph = SimpleGraph(3)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        # Удаление рёбер
        graph.RemoveEdge(0, 1)
        graph.RemoveEdge(1, 2)

        # Проверка отсутствия рёбер
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 2))
        # Граф после удаления рёбер:
        # 10    20    30

    def test_remove_vertex(self):
        graph = SimpleGraph(3)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        # Удаление вершины
        graph.RemoveVertex(1)

        # Проверка, что вершина и её рёбра удалены
        self.assertIsNone(graph.vertex[1])
        self.assertFalse(graph.IsEdge(0, 1))
        self.assertFalse(graph.IsEdge(1, 2))
        # Граф после удаления вершины 20:
        # 10       30

    def test_add_remove_vertices_and_edges(self):
        graph = SimpleGraph(5)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)
        graph.AddVertex(40)
        graph.AddVertex(50)
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 4)

        # Проверка наличия рёбер
        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 2))
        self.assertTrue(graph.IsEdge(2, 3))
        self.assertTrue(graph.IsEdge(3, 4))

        # Удаление нескольких вершин и рёбер
        graph.RemoveVertex(2)
        graph.RemoveEdge(3, 4)

        # Проверка состояния графа
        self.assertIsNone(graph.vertex[2])
        self.assertFalse(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(3, 4))
        # Граф после удаления вершины 30 и рёбер (20--30) и (40--50):
        # 10 -- 20    40    50
    def test_add_non_adjacent_edges(self):
        graph = SimpleGraph(5)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)
        graph.AddVertex(40)
        graph.AddVertex(50)

        # Добавляем рёбра между не соседними вершинами
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 3)
        graph.AddEdge(0, 4)

        # Проверка наличия рёбер
        self.assertTrue(graph.IsEdge(0, 2))
        self.assertTrue(graph.IsEdge(1, 3))
        self.assertTrue(graph.IsEdge(0, 4))
        self.assertFalse(graph.IsEdge(2, 3))

        # Граф:
        # 10 -- 30
        # |     |
        # 20    40
        # |
        # 50

    def test_remove_non_adjacent_edges(self):
        graph = SimpleGraph(5)
        graph.AddVertex(10)
        graph.AddVertex(20)
        graph.AddVertex(30)
        graph.AddVertex(40)
        graph.AddVertex(50)

        # Добавляем рёбра
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 3)
        graph.AddEdge(0, 4)

        # Удаляем рёбра между не соседними вершинами
        graph.RemoveEdge(0, 2)
        graph.RemoveEdge(1, 3)
        graph.RemoveEdge(0, 4)

        # Проверка отсутствия рёбер
        self.assertFalse(graph.IsEdge(0, 2))
        self.assertFalse(graph.IsEdge(1, 3))
        self.assertFalse(graph.IsEdge(0, 4))
        self.assertFalse(graph.IsEdge(2, 3))

        # Граф после удаления рёбер:
        # 10    30
        #       |
        # 20    40
        # |
        # 50


if __name__ == '__main__':
    unittest.main()
