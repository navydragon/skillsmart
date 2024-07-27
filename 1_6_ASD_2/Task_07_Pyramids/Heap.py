class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        # Вычисляем размер массива кучи на основе глубины
        size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * size

        # Заполняем кучу из массива a
        for key in a:
            self.Add(key)

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1  # Куча пуста

        # Сохраняем максимальный элемент (корень)
        root = self.HeapArray[0]

        # Перемещаем последний элемент на место корня
        last_index = self._find_last_index()
        self.HeapArray[0] = self.HeapArray[last_index]
        self.HeapArray[last_index] = None

        # Восстанавливаем свойство кучи
        self._sift_down(0)

        return root

    def Add(self, key):
        # Найти первое свободное место
        index = self._find_first_empty_index()
        if index == -1:
            return False  # Куча заполнена

        self.HeapArray[index] = key
        self._sift_up(index)
        return True

    def _find_last_index(self):
        # Находим индекс последнего элемента в куче
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] is not None:
                return i
        return -1

    def _find_first_empty_index(self):
        # Находим первое свободное место в куче
        for i in range(len(self.HeapArray)):
            if self.HeapArray[i] is None:
                return i
        return -1

    def _sift_up(self, index):
        # Просеивание вверх
        parent_index = (index - 1) // 2
        while index > 0 and self.HeapArray[parent_index] < self.HeapArray[index]:
            self.HeapArray[parent_index], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        # Просеивание вниз
        size = len(self.HeapArray)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.HeapArray[left] is not None and self.HeapArray[left] > self.HeapArray[largest]:
                largest = left

            if right < size and self.HeapArray[right] is not None and self.HeapArray[right] > self.HeapArray[largest]:
                largest = right

            if largest == index:
                break

            self.HeapArray[largest], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[largest]
            index = largest

