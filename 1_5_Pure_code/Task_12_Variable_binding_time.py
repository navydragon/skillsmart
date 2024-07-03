"""
Сделайте 3 примера с разбором различного времени связывания
в вашем коде и поясните, почему в каждом случае был сделан такой выбор.
"""

# 1. Раннее связывание во время написания кода
# Контекст: Использование числовой константы для задания порога рейтинга фильма.


HIGH_RATING_THRESHOLD = 8.0

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def is_highly_rated(self):
        return self.rating >= HIGH_RATING_THRESHOLD

movie = Movie("Inception", 9.0)
print(movie.is_highly_rated())  # True

# Cвязывание переменной HIGH_RATING_THRESHOLD с её значением происходит во время написания кода.
# Плюсы: простота реализации, высокая производительность.
# Минусы: изменение порога требует изменения кода.


# 2. Связывание во время компиляции
# Контекст: Задание значений цветов через константы.

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

class Display:
    def __init__(self, title, color):
        self.title = title
        self.color = color

    def set_color(self, color):
        self.color = color

display = Display("Main Screen", COLOR_WHITE)
print(display.color)  # (255, 255, 255)

# Cвязывание переменных COLOR_WHITE и COLOR_BLACK с их значениями происходит во время компиляции кода.
# Плюсы: значения легко менять, не требуется изменение самой логики программы.
# Минусы: изменение цвета требует повторной компиляции кода, если значение меняется часто, то это неудобно.

# 3. Позднее связывание во время выполнения программы
# Контекст: Задание конфигурации через файл настроек.

import json

def read_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


config = read_config('config.json')

class Application:
    def __init__(self, title):
        self.title = title
        self.color = config['color']

    def set_color(self, color):
        self.color = color

app = Application("Main App")
print(app.color)  #  зависит от содержимого config.json

# Cвязывание переменной color с её значением происходит во время выполнения программы.
# Плюсы: высокая гибкость, изменение значений без перекомпиляции кода, удобство при изменении часто меняющихся настроек.
# Минусы: более сложная реализация, ниже производительность.


