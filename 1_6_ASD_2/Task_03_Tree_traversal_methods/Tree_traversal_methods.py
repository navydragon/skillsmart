from collections import deque

class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если в дереве вообще нет узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        result = BSTFind()
        current_node = self.Root
        while current_node is not None:
            if key == current_node.NodeKey:
                result.Node = current_node
                result.NodeHasKey = True
                return result
            elif key < current_node.NodeKey:
                if current_node.LeftChild is None:
                    result.Node = current_node
                    result.ToLeft = True
                    return result
                current_node = current_node.LeftChild
            else:
                if current_node.RightChild is None:
                    result.Node = current_node
                    result.ToLeft = False
                    return result
                current_node = current_node.RightChild
        return result

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False  # ключ уже есть в дереве

        new_node = BSTNode(key, val, find_result.Node)
        if find_result.ToLeft:
            find_result.Node.LeftChild = new_node
        else:
            find_result.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        current_node = FromNode
        if FindMax:
            while current_node.RightChild is not None:
                current_node = current_node.RightChild
        else:
            while current_node.LeftChild is not None:
                current_node = current_node.LeftChild
        return current_node

    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False  # узел не найден

        node_to_delete = find_result.Node
        if node_to_delete.LeftChild is None and node_to_delete.RightChild is None:  # нет потомков
            if node_to_delete.Parent is not None:
                if node_to_delete.Parent.LeftChild == node_to_delete:
                    node_to_delete.Parent.LeftChild = None
                else:
                    node_to_delete.Parent.RightChild = None
            else:
                self.Root = None

        elif node_to_delete.LeftChild is None or node_to_delete.RightChild is None:  # один потомок
            child = node_to_delete.LeftChild if node_to_delete.LeftChild is not None else node_to_delete.RightChild
            if node_to_delete.Parent is not None:
                if node_to_delete.Parent.LeftChild == node_to_delete:
                    node_to_delete.Parent.LeftChild = child
                else:
                    node_to_delete.Parent.RightChild = child
            else:
                self.Root = child
            child.Parent = node_to_delete.Parent

        else:  # два потомка
            successor = self.FinMinMax(node_to_delete.RightChild, False)
            node_to_delete.NodeKey = successor.NodeKey
            node_to_delete.NodeValue = successor.NodeValue
            if successor.Parent.LeftChild == successor:
                successor.Parent.LeftChild = successor.RightChild
            else:
                successor.Parent.RightChild = successor.RightChild
            if successor.RightChild is not None:
                successor.RightChild.Parent = successor.Parent

        return True

    def Count(self):
        return self._count_nodes(self.Root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.LeftChild) + self._count_nodes(node.RightChild)

    def WideAllNodes(self):
        if self.Root is None:
            return ()

        result = []
        queue = deque([self.Root])

        while queue:
            node = queue.popleft()
            result.append(node)
            if node.LeftChild is not None:
                queue.append(node.LeftChild)
            if node.RightChild is not None:
                queue.append(node.RightChild)

        return tuple(result)

    def DeepAllNodes(self, order):
        if self.Root is None:
            return ()

        result = []

        if order == 0:  # in-order
            self._in_order(self.Root, result)
        elif order == 1:  # post-order
            self._post_order(self.Root, result)
        elif order == 2:  # pre-order
            self._pre_order(self.Root, result)

        return tuple(result)

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.LeftChild, result)
            result.append(node)
            self._in_order(node.RightChild, result)

    def _post_order(self, node, result):
        if node is not None:
            self._post_order(node.LeftChild, result)
            self._post_order(node.RightChild, result)
            result.append(node)

    def _pre_order(self, node, result):
        if node is not None:
            result.append(node)
            self._pre_order(node.LeftChild, result)
            self._pre_order(node.RightChild, result)
