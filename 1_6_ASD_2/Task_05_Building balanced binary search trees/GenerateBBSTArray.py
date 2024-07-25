import math

def GenerateBBSTArray(arr):
    if not arr:
        return []

    # Сортируем входной массив
    arr.sort()

    # Рассчитываем необходимую глубину дерева и размер массива
    depth = math.ceil(math.log2(len(arr) + 1)) - 1
    size = 2 ** (depth + 1) - 1

    # Инициализация массива для хранения BST
    bbst_array = [None] * size

    # Заполняем массив BST и возвращаем его
    return fill_bbst(arr, 0, len(arr) - 1, 0, bbst_array)

def fill_bbst(arr, start, end, index, bbst_array):
    if start > end:
        return bbst_array

    mid = (start + end) // 2
    bbst_array[index] = arr[mid]

    # Рекурсивно заполняем левую и правую части
    fill_bbst(arr, start, mid - 1, 2 * index + 1, bbst_array)
    fill_bbst(arr, mid + 1, end, 2 * index + 2, bbst_array)

    return bbst_array

