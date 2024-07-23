class aBST:
    def __init__(self, depth):
        # правильно рассчитываем размер массива для дерева глубины depth
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size # массив ключей

    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree):
            if self.Tree[index] is None:
                return -index  # возвращаем отрицательный индекс для незаполненного слота
            if self.Tree[index] == key:
                return index  # ключ найден
            if key < self.Tree[index]:
                index = 2 * index + 1  # переход к левому потомку
            else:
                index = 2 * index + 2  # переход к правому потомку
        return None  # дерево полностью пройдено и ключ не найден

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1  # дерево полностью заполнено и ключ не может быть добавлен
        if index <= 0:
            self.Tree[-index] = key
            return -index
        return index  # ключ уже существует в дереве

