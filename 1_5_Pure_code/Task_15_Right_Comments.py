#В несите 12 правок в свои комментарии, дополнительно указывая, по какому из
# вышеприведённых пунктов была сделана та или иная правка.

# Исходный код
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Добавить книгу в библиотеку
        self.books.append(book)

    def remove_book(self, isbn):
        # Проверка, что книга с данным ISBN существует в библиотеке
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def find_book_by_title(self, title):
        # Поиск книги по названию
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, isbn):
        # Проверка, что книга доступна для взятия
        for book in self.books:
            if book.isbn == isbn and not book.borrowed:
                book.borrowed = True
                return True
        return False

    def return_book(self, isbn):
        # Возвращение книги в библиотеку
        for book in self.books:
            if book.isbn == isbn:
                book.borrowed = False
                return True
        return False


# Улучшенный код с комментариями

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False  # Книга по умолчанию не занята

class Library:
    def __init__(self):
        self.books = []

    # Добавить книгу в библиотеку
    def add_book(self, book):
        self.books.append(book)

    # Удалить книгу из библиотеки по ISBN, если она существует
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    # Найти книгу по названию
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    # Взять книгу из библиотеки по ISBN, если она доступна
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.borrowed:
                book.borrowed = True
                return True
        return False

    # Вернуть книгу в библиотеку по ISBN
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.borrowed = False
                return True
        return False

    # Получить все книги в библиотеке
    def get_all_books(self):
        return self.books

    # Найти книги по автору
    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    # Удалить все книги из библиотеки
    def clear_library(self):
        self.books = []

    # Вернуть количество книг в библиотеке
    def get_book_count(self):
        return len(self.books)

    # Проверить, есть ли книга в библиотеке по ISBN
    def has_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return True
        return False

    # TO_DO: Реализовать функцию экспорта библиотеки в файл
    def export_library(self, filename):
        pass

# Описание правок
#
#     Информативные комментарии:
#         комментарий к полю self.borrowed в конструкторе класса Book: # Книга по умолчанию не занята.
#         комментарий к методу add_book: # Добавить книгу в библиотеку.
#         комментарий к методу remove_book: # Удалить книгу из библиотеки по ISBN, если она существует.
#         комментарий к методу find_book_by_title: # Найти книгу по названию.
#         комментарий к методу borrow_book: # Взять книгу из библиотеки по ISBN, если она доступна.
#         комментарий к методу return_book: # Вернуть книгу в библиотеку по ISBN.
#
#     Представление намерений:
#         метод get_all_books: # Получить все книги в библиотеке.
#         метод find_books_by_author: # Найти книги по автору.
#         метод clear_library: # Удалить все книги из библиотеки.
#         метод get_book_count: # Вернуть количество книг в библиотеке.
#         метод has_book: # Проверить, есть ли книга в библиотеке по ISBN.
#
#     Комментарии TO_DO:
#         метод export_library с комментарием # TO_DO: Реализовать функцию экспорта библиотеки в файл.