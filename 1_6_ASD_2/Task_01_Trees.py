class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        # добавляем новый дочерний узел к существующему узлу ParentNode
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        # удаляем существующий узел NodeToDelete вместе с его поддеревом
        if NodeToDelete.Parent:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    def GetAllNodes(self):
        # возвращаем список всех узлов дерева в определённом порядке
        if not self.Root:
            return []
        return self._traverse_tree(self.Root)

    def _traverse_tree(self, node):
        # вспомогательный метод для обхода дерева
        nodes = [node]
        for child in node.Children:
            nodes.extend(self._traverse_tree(child))
        return nodes

    def FindNodesByValue(self, val):
        # возвращаем список узлов с заданным значением
        if not self.Root:
            return []
        return [node for node in self._traverse_tree(self.Root) if node.NodeValue == val]

    def MoveNode(self, OriginalNode, NewParent):
        # перемещаем узел вместе с его поддеревом
        if OriginalNode.Parent:
            OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        # возвращаем количество всех узлов в дереве
        if not self.Root:
            return 0
        return len(self._traverse_tree(self.Root))

    def LeafCount(self):
        # возвращаем количество листьев в дереве
        if not self.Root:
            return 0
        return len([node for node in self._traverse_tree(self.Root) if not node.Children])

    def AssignLevels(self):
        # присваиваем уровни каждому узлу дерева
        if not self.Root:
            return
        self._assign_levels(self.Root, 0)

    def _assign_levels(self, node, level):
        # вспомогательный метод для присвоения уровней узлам
        node.level = level
        for child in node.Children:
            self._assign_levels(child, level + 1)