class aBST:
    def __init__(self, depth):
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
        if index < 0:
            self.Tree[-index] = key
            return -index
        return index  # ключ уже существует в дереве

# Пример использования
depth = 3
tree = aBST(depth)

keys_to_add = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]
added_indices = []

for key in keys_to_add:
    index = tree.AddKey(key)
    added_indices.append(index)
    print(f"Added key {key} at index {index}")

print("\nFinal tree:")
print(tree.Tree)

# Поиск ключей
search_keys = [50, 31, 43, 99]
for key in search_keys:
    index = tree.FindKeyIndex(key)
    print(f"Key {key} found at index {index}")
