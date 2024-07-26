import unittest
from BSTNode import BalancedBST, BSTNode

class TestBalancedBST(unittest.TestCase):

    def test_empty_array(self):
        bst = BalancedBST()
        bst.GenerateTree([])
        self.assertIsNone(bst.Root)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево: []

    def test_single_element_array(self):
        bst = BalancedBST()
        bst.GenerateTree([10])
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 10)
        self.assertIsNone(bst.Root.LeftChild)
        self.assertIsNone(bst.Root.RightChild)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #    10
        #   /  \
        # None None

    def test_two_elements_array(self):
        bst = BalancedBST()
        bst.GenerateTree([10, 5])
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 10)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 5)
        self.assertIsNone(bst.Root.RightChild)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #    10
        #   /  \
        #  5   None

    def test_three_elements_array(self):
        bst = BalancedBST()
        bst.GenerateTree([10, 5, 15])
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 10)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.RightChild.NodeKey, 15)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #    10
        #   /  \
        #  5    15

    def test_unbalanced_four_elements_array(self):
        bst = BalancedBST()
        bst.GenerateTree([10, 5, 15, 2])
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 10)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.RightChild.NodeKey, 15)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 2)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #    10
        #   /  \
        #  5    15
        # /
        # 2

    def test_balanced_seven_elements_array(self):
        bst = BalancedBST()
        bst.GenerateTree([4, 2, 6, 1, 3, 5, 7])
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 4)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 2)
        self.assertEqual(bst.Root.RightChild.NodeKey, 6)
        self.assertEqual(bst.Root.LeftChild.LeftChild.NodeKey, 1)
        self.assertEqual(bst.Root.LeftChild.RightChild.NodeKey, 3)
        self.assertEqual(bst.Root.RightChild.LeftChild.NodeKey, 5)
        self.assertEqual(bst.Root.RightChild.RightChild.NodeKey, 7)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #      4
        #     / \
        #    2   6
        #   / \ / \
        #  1  3 5  7

    def test_large_array(self):
        bst = BalancedBST()
        arr = list(range(1, 16))  # Полный массив для дерева глубины 3
        bst.GenerateTree(arr)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #             8
        #          /     \
        #        4         12
        #       / \       /  \
        #      2   6     10  14
        #     / \ / \   / \  / \
        #    1  3 5  7 9 11 13 15

    def test_duplicate_elements_array(self):
        bst = BalancedBST()
        bst.GenerateTree([10, 10])
        self.assertIsNotNone(bst.Root)
        self.assertEqual(bst.Root.NodeKey, 10)
        self.assertEqual(bst.Root.LeftChild.NodeKey, 10)
        self.assertIsNone(bst.Root.RightChild)
        self.assertTrue(bst.IsBalanced(bst.Root))
        # Дерево:
        #    10
        #   /  \
        #  10  None


if __name__ == '__main__':
    unittest.main()
