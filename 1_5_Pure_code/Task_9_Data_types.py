"""
Данные задание выполнено в контексте Django REST API для 'клона' IMDB
"""

"""
Внесите 12 правок в свой код с учётом рекомендаций из 
данного занятия, и напишите по каждой, как и что конкретно вы улучшили.
"""


from django.db import models

# models.py
# Константы
TITLE_MAX_LENGTH = 255
DIRECTOR_MAX_LENGTH = 255
DEFAULT_RATING = 0.0

class Movie(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=DIRECTOR_MAX_LENGTH)
    rating = models.FloatField(default=DEFAULT_RATING)


# Улучшения:
# 1. TITLE_MAX_LENGTH - заменяет магическое число 255 для длины названия.
# 2. DIRECTOR_MAX_LENGTH - заменяет магическое число 255 для длины имени режиссера.
# 3. DEFAULT_RATING - заменяет магическое значение 0.0 для начального рейтинга.


# utils.py
# Константы для утилит
MIN_RATING = 0.0
MAX_RATING = 10.0

def calculate_average_rating(total_rating, number_of_ratings):
    if number_of_ratings == 0:
        return MIN_RATING
    return total_rating / number_of_ratings


# Улучшения:
# 4. MIN_RATING - заменяет магическое число 0.0 для минимального рейтинга.
# 5. Добавлена проверка деления на ноль в calculate_average_rating.



# permissions.py
from rest_framework.permissions import BasePermission

# Константы для разрешений
ADMIN_ROLE = 'admin'
USER_ROLE = 'user'

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.role == ADMIN_ROLE

# Улучшения:
# 7. ADMIN_ROLE - заменяет магическую строку 'admin'.
# 8. USER_ROLE - заменяет магическую строку 'user'.

# models.py

from django.utils.translation import gettext_lazy as _

class Movie(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=DIRECTOR_MAX_LENGTH)
    rating = models.FloatField(default=DEFAULT_RATING)

    class Meta:
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')

# Улучшения:
# 9. Использование _('Movie') и _('Movies') для интернационализации строковых констант.

# views.py
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        is_admin = self.request.user.role == ADMIN_ROLE
        if is_admin:
            return Movie.objects.all()
        return Movie.objects.filter(is_public=True)


# Улучшения:
# 10. Использование логической переменной is_admin для упрощения условия в методе get_queryset.

# models.py
class Movie(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH, unicode=True)
    description = models.TextField(unicode=True)
    release_date = models.DateField()
    director = models.CharField(max_length=DIRECTOR_MAX_LENGTH, unicode=True)
    rating = models.FloatField(default=DEFAULT_RATING)


# 11. Поддержка Unicode для строковых полей в модели Movie.


# utils.py
import locale

# Установка локали для преобразования строковых типов
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def format_currency(value):
    return locale.currency(value, grouping=True)

# Улучшения:
# 12. Установка локали и преобразование строковых типов для форматирования валют в format_currency.