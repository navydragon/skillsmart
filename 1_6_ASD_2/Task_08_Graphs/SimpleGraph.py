class Vertex:
    def __init__(self, val):
        self.Value = val

class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # Добавление новой вершины
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return
        raise ValueError("Нет свободного места для добавления новой вершины")

    def RemoveVertex(self, v):
        # Удаление вершины и всех её рёбер
        if self.vertex[v] is not None:
            # Удаляем все рёбра, связанные с вершиной
            for i in range(self.max_vertex):
                self.m_adjacency[v][i] = 0
                self.m_adjacency[i][v] = 0
            self.vertex[v] = None

    def IsEdge(self, v1, v2):
        # Проверка наличия ребра между вершинами
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            return self.m_adjacency[v1][v2] == 1
        return False

    def AddEdge(self, v1, v2):
        # Добавление ребра между вершинами
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # Удаление ребра между вершинами
        if self.vertex[v1] is not None and self.vertex[v2] is not None:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
