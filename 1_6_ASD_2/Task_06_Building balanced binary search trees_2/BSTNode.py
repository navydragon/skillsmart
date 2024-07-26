class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла

class BalancedBST:
    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        # Создаем дерево с нуля из неотсортированного массива a
        if not a:
            self.Root = None
            return

        # Сортируем массив
        a.sort()

        # Строим сбалансированное дерево
        self.Root = self.build_balanced_tree(a, None, 0)

    @staticmethod
    def build_balanced_tree(arr, parent, level):
        if not arr:
            return None

        mid = len(arr) // 2
        root = BSTNode(arr[mid], parent)
        root.Level = level

        root.LeftChild = BalancedBST.build_balanced_tree(arr[:mid], root, level + 1)
        root.RightChild = BalancedBST.build_balanced_tree(arr[mid + 1:], root, level + 1)

        return root

    def IsBalanced(self, root_node):
        # Проверка сбалансированности дерева с корнем root_node
        def check_balance(node):
            if node is None:
                return 0, True

            left_height, left_balanced = check_balance(node.LeftChild)
            right_height, right_balanced = check_balance(node.RightChild)

            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            return max(left_height, right_height) + 1, balanced

        _, is_balanced = check_balance(root_node)
        return is_balanced
