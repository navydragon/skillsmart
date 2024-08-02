import unittest
from SimpleTree import SimpleTreeNode, SimpleTree

class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        # Общий метод для установки дерева
        self.root = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.root)

    def test_empty_tree(self):
        empty_tree = SimpleTree(None)
        self.assertEqual(empty_tree.EvenTrees(), [])
        # Дерево:
        # None

    def test_single_node_tree(self):
        self.assertEqual(self.tree.EvenTrees(), [])
        # Дерево:
        # 1

    def test_two_node_tree(self):
        n2 = SimpleTreeNode(2, self.root)
        self.tree.AddChild(self.root, n2)
        self.assertEqual(self.tree.EvenTrees(), [])
        # Дерево:
        # 1
        # |
        # 2

    def test_even_tree(self):
        n2 = SimpleTreeNode(2, self.root)
        n3 = SimpleTreeNode(3, self.root)
        self.tree.AddChild(self.root, n2)
        self.tree.AddChild(self.root, n3)
        self.assertEqual(self.tree.EvenTrees(), [])
        # Дерево:
        #  1
        # / \
        # 2   3
        # Ожидаемый результат: []


    def test_unbalanced_tree(self):
        n2 = SimpleTreeNode(2, self.root)
        n3 = SimpleTreeNode(3, n2)
        n4 = SimpleTreeNode(4, n3)
        n5 = SimpleTreeNode(5, n4)
        n6 = SimpleTreeNode(6, n5)

        self.tree.AddChild(self.root, n2)
        self.tree.AddChild(n2, n3)
        self.tree.AddChild(n3, n4)
        self.tree.AddChild(n4, n5)
        self.tree.AddChild(n5, n6)

        self.assertEqual(self.tree.EvenTrees(), [n2, n3, n4, n5])
        # Дерево:
        # 1
        # |
        # 2
        # |
        # 3
        # |
        # 4
        # |
        # 5
        # |
        # 6
        # Ожидаемый результат: [4, 5, 2, 3, 1, 2]


if __name__ == '__main__':
    unittest.main()
