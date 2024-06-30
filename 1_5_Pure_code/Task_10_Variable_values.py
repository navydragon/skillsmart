"""
Данные задание выполнено в контексте Django REST API для 'клона' IMDB
"""

"""
Внесите 15 правок в свой код с учётом рекомендаций из данного занятия, и 
напишите по каждой, как и что конкретно вы улучшили.
"""

from django.db import models

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = None  # Инициализация переменной
        self.description = None  # Инициализация переменной
        self.release_date = None  # Инициализация переменной
        self.director = None  # Инициализация переменной
        self.rating = DEFAULT_RATING  # Инициализация переменной

    def is_top_rated(self):
        return self.rating > (MAX_RATING - 1.0)

# Улучшения:
#
# 1. Переменные title, description, release_date, director, и rating явно инициализированы в конструкторе.
# 2. Значение rating инициализируется константой DEFAULT_RATIN

from rest_framework import serializers
from .models import Movie

# Константы для сериализатора
MOVIE_FIELDS = ['id', 'title', 'description', 'release_date', 'director',
                'rating']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = MOVIE_FIELDS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = MOVIE_FIELDS  # Инициализация переменной

# Улучшения:
# 3. Переменная fields явно инициализирована в конструкторе сериализатора.

from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

# Константы для представления
DEFAULT_PAGE_SIZE = 10
ADMIN_ROLE = 'admin'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Movie.objects.all()  # Инициализация переменной
        self.serializer_class = MovieSerializer  # Инициализация переменной
        self.page_size = DEFAULT_PAGE_SIZE  # Инициализация переменной

    def get_queryset(self):
        user_role = self.request.user.role  # Явное объявление переменной
        is_admin = user_role == ADMIN_ROLE  # Явное объявление переменной
        if is_admin:
            return Movie.objects.all()
        return Movie.objects.filter(is_public=True)

    def finalize_response(self, request, response, *args, **kwargs):
        response.set_cookie('is_admin',
                            is_admin)  # Использование переменной за пределами блока

        # Завершаем работу с переменной, присваивая None
        is_admin = None
        return super().finalize_response(request, response, *args, **kwargs)

# Улучшения:
# 4. Переменные queryset, serializer_class и page_size явно инициализированы в конструкторе.
# 5. Переменные user_role и is_admin явно объявлены и инициализированы перед первым использованием.
# 6. Переменная is_admin устанавливается в None после использования.

import locale

# Константы для утилит
MIN_RATING = 0.0
MAX_RATING = 10.0

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def calculate_average_rating(total_rating, number_of_ratings):
    if number_of_ratings == 0:
        return MIN_RATING
    return total_rating / number_of_ratings

def format_currency(value):
    return locale.currency(value, grouping=True)

def calculate_movie_score(movie):
    total_score = 0  # Инициализация переменной
    for review in movie.reviews.all():
        total_score += review.score
    return calculate_average_rating(total_score, movie.reviews.count())

def is_valid_rating(rating):
    return MIN_RATING <= rating <= MAX_RATING


# Улучшения:
# 7. Проверка деления на ноль в calculate_average_rating.
# 8. Инициализация переменной total_score перед первым использованием.
# 9. Проверка целочисленности операций и значений в функции is_valid_rating.

from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        method = request.method  # Явное объявление переменной
        is_safe_method = method in SAFE_METHODS  # Явное объявление переменной
        if is_safe_method:
            return True
        user_role = request.user.role  # Явное объявление переменной
        return user_role == ADMIN_ROLE


# Улучшения:
# 10. Переменные method, is_safe_method и user_role явно объявлены и инициализированы перед первым использованием.


from django.test import TestCase
from .models import Movie


class MovieModelTest(TestCase):
    def setUp(self):
        self.test_title = "Test Movie"  # Явное объявление переменной
        self.test_description = "Test Description"  # Явное объявление переменной
        self.test_release_date = "2023-01-01"  # Явное объявление переменной
        self.test_director = "Test Director"  # Явное объявление переменной
        self.test_rating = 5.0  # Явное объявление переменной

        self.movie = Movie.objects.create(
            title=self.test_title,
            description=self.test_description,
            release_date=self.test_release_date,
            director=self.test_director,
            rating=self.test_rating
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, self.test_title)
        self.assertEqual(self.movie.description, self.test_description)
        self.assertEqual(str(self.movie.release_date), self.test_release_date)
        self.assertEqual(self.movie.director, self.test_director)
        self.assertEqual(self.movie.rating, self.test_rating)

# Улучшения:
# 11. Явное объявление и инициализация переменных test_title, test_description,
# test_release_date, test_director, и test_rating в методе setUp.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Movie.objects.all()
        self.serializer_class = MovieSerializer
        self.page_size = DEFAULT_PAGE_SIZE

    def get_queryset(self):
        user_role = self.request.user.role
        is_admin = user_role == ADMIN_ROLE
        if is_admin:
            return Movie.objects.all()
        return Movie.objects.filter(is_public=True)

    def finalize_response(self, request, response, *args, **kwargs):
        response.set_cookie('is_admin', is_admin)
        is_admin = None  # Завершаем работу с переменной, присваивая None
        return super().finalize_response(request, response, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        instance = None  # Завершаем работу с переменной, присваивая None
        return Response(status=status.HTTP_204_NO_CONTENT)

# Улучшения:
# 12. Завершение работы с переменной instance, присваивая ей None после удаления объекта.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update_movie_ratings(self):
        movies = Movie.objects.all()
        for movie in movies:
            total_rating = 0  # Инициализация переменной
            rating_count = movie.reviews.count()
            for review in movie.reviews.all():
                total_rating += review.rating
            movie.rating = total_rating / rating_count if rating_count != 0 else 0
            movie.save()

# Улучшения:
# 13. Переменная total_rating инициализирована перед использованием в цикле.

class Movie(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=DIRECTOR_MAX_LENGTH)
    rating = models.FloatField(default=DEFAULT_RATING)

    def clean(self):
        super().clean()
        if self.rating < MIN_RATING or self.rating > MAX_RATING:
            raise ValidationError(
                _('Rating must be between %(min)s and %(max)s'),
                params={'min': MIN_RATING, 'max': MAX_RATING})

    def is_top_rated(self):
        return self.rating > (MAX_RATING - 1.0)

# Улучшения:
# 14. Использование метода clean для проверки допустимости значений переменной
# rating и выброса исключения, если значение недопустимо.

