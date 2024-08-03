from collections import deque
class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False

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

    def RemoveVertex(self, v):
        # Удаление вершины и всех её рёбер
        if self.vertex[v] is not None:
            # Удаляем все рёбра, связанные с вершиной
            for i in range(self.max_vertex):
                self.m_adjacency[v][i] = 0
                self.m_adjacency[i][v] = 0
            self.vertex[v] = None

    def DepthFirstSearch(self, VFrom, VTo):
        for v in self.vertex:
            if v:
                v.Hit = False
        stack = []
        path = []
        stack.append(self.vertex[VFrom])
        self.vertex[VFrom].Hit = True

        while stack:
            current = stack[-1]
            path.append(current)
            if current == self.vertex[VTo]:
                return path

            found_unvisited = False
            for i in range(self.max_vertex):
                if self.m_adjacency[self.vertex.index(current)][i] == 1 and not self.vertex[i].Hit:
                    self.vertex[i].Hit = True
                    stack.append(self.vertex[i])
                    found_unvisited = True
                    break

            if not found_unvisited:
                stack.pop()
                path.pop()

        return []

    def BreadthFirstSearch(self, VFrom, VTo):
        for v in self.vertex:
            if v:
                v.Hit = False

        queue = deque()
        parents = {VFrom: None}
        queue.append(VFrom)
        self.vertex[VFrom].Hit = True

        while queue:
            current = queue.popleft()
            if current == VTo:
                path = []
                while current is not None:
                    path.append(self.vertex[current])
                    current = parents[current]
                return list(reversed(path))

            for i in range(self.max_vertex):
                if self.m_adjacency[current][i] == 1 and not self.vertex[i].Hit:
                    self.vertex[i].Hit = True
                    queue.append(i)
                    parents[i] = current

        return []