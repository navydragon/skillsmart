# Прокомментируйте 7 мест в своём коде там, где это явно уместно.

from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Модель книги
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField()

    def __str__(self):
        return self.title

# Сериализатор для модели книги
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'page_count']

# Представление для управления книгами
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Переопределение метода для создания книги
    def create(self, request, *args, **kwargs):
        # Проверка на наличие книги с таким же ISBN
        isbn = request.data.get('isbn')
        if Book.objects.filter(isbn=isbn).exists():
            return Response({'error': 'Book with this ISBN already exists'}, status=400)
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def recent_books(self, request):
        """Получение списка книг, опубликованных в этом году."""
        from datetime import date
        current_year = date.today().year
        recent_books = Book.objects.filter(published_date__year=current_year)
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_pages(self, request, pk=None):
        """Добавление страниц к книге."""
        book = self.get_object()
        additional_pages = int(request.data.get('additional_pages', 0))
        book.page_count += additional_pages
        book.save()
        return Response({'status': 'pages added'})


# Если вы раньше делали комментарии к коду, найдите 5 мест, где эти комментарии были излишни, удалите их и сделайте сам код более наглядным.

# Контекст: Пример кода для управления списком задач.

# Исходный код
tasks = []

# Добавить задачу в список задач
def add_task(task):
    # Проверка, что задача не пустая
    if task:
        tasks.append(task)
        return True
    return False

# Удалить задачу из списка задач
def remove_task(task):
    # Проверка, что задача в списке
    if task in tasks:
        tasks.remove(task)
        return True
    return False

# Получить все задачи
def get_all_tasks():
    # Вернуть копию списка задач
    return list(tasks)

# Код дбез комментариев
tasks = []

def add_task(task):
    if task:
        tasks.append(task)
        return True
    return False

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return True
    return False

def get_all_tasks():
    return list(tasks)

