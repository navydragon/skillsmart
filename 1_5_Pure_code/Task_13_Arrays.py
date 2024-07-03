# Приведите 5 примеров вашего кода,
# где вместо массивов можно использовать более безопасные структуры данных,
# или же работа с самими массивами может выполняться без их прямой индексации.


# 1: Использование списка вместо массива с прямой индексацией

# Исходный код с массивами
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)):
    print(arr[i])

# Использование списка с итерацией
arr = [1, 2, 3, 4, 5]
for item in arr:
    print(item)

# Что дает Вместо индексации массива используется итерация по элементам списка - безопаснее

# 2: Использование встроенного deque вместо массива
# Миссия : Реализовать очередь задач с операциями добавления и извлечения задач.

# Исходный код с массивами
tasks = []
tasks.append('task1')
tasks.append('task2')
next_task = tasks.pop(0)
print(next_task)
print(tasks)


# Использование deque для очереди задач
from collections import deque
tasks = deque()
tasks.append('task1')
tasks.append('task2')
next_task = tasks.popleft()
print(next_task)
print(tasks)

# Улучшает производительность и делает код более читаемым.


# 3: Использование множества (set) вместо массива для уникальных элементов
# Задача: Хранить и проверять уникальные значения.

# Исходный код с массивами
values = [1, 2, 3, 1, 2, 4]
unique_values = []
for value in values:
    if value not in unique_values:
        unique_values.append(value)
print(unique_values)

# Использование set для хранения уникальных значений
values = [1, 2, 3, 1, 2, 4]
unique_values = set(values)
print(unique_values)

# Улучшает читаемость и компактность.

# 4: Чтение и обработка данных из файла
# Задача: Прочитать данные из файла и найти максимальное значение.

# Исходный код с массивами
with open('data.txt', 'r') as file:
    data = file.readlines()

max_value = float('-inf')
for i in range(len(data)):
    value = int(data[i].strip())
    if value > max_value:
        max_value = value
print(max_value)


# Использование map и max для обработки данных
with open('data.txt', 'r') as file:
    data = file.readlines()

values = map(int, map(str.strip, data))
max_value = max(values)
print(max_value)

# Улучшается читаемость, избегается прямая индексация массива

# 5. Группировка данных по ключу
# Исходный код с массивами
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped_data = {}
for i in range(len(data)):
    key = data[i][0]
    value = data[i][1]
    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append(value)
print(grouped_data)


# Использование defaultdict для группировки данных
from collections import defaultdict
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped_data = defaultdict(list)
for key, value in data:
    grouped_data[key].append(value)
print(grouped_data)

# Улучшается читаемость, избегается прямая индексация массива