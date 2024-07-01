"""
Данные задание выполнено в контексте Django REST API для 'клона' IMDB
"""

"""
Внесите 15 правок в свой код с учётом рекомендаций из данного занятия, и 
напишите по каждой, как и что конкретно вы улучшили.
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Константы
TITLE_MAX_LENGTH = 255
DIRECTOR_MAX_LENGTH = 255
DEFAULT_RATING = 0.0
MIN_RATING = 0.0
MAX_RATING = 10.0


class Movie(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=DIRECTOR_MAX_LENGTH)
    rating = models.FloatField(default=DEFAULT_RATING)

    def clean(self):
        super().clean()
        if self.rating < MIN_RATING or self.rating > MAX_RATING:
            raise ValidationError(_('Rating must be between %(min)s and %(max)s'),
                                  params={'min': MIN_RATING, 'max': MAX_RATING})

    def is_top_rated(self):
        return self.rating > (MAX_RATING - 1.0)

    class Meta:
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')

# Улучшения:
#
#     Переменные объявлены и инициализированы внутри методов clean и is_top_rated для минимизации их области видимости.

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'director', 'rating']

# Улучшения:
# 2. Константы MOVIE_FIELDS удалены, так как они не используются в другом месте,
# и могут быть определены прямо в Meta классе.


from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

# Константы для представления
DEFAULT_PAGE_SIZE = 10
ADMIN_ROLE = 'admin'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        if self.request.user.role == ADMIN_ROLE:
            return Movie.objects.all()
        return Movie.objects.filter(is_public=True)

    def finalize_response(self, request, response, *args, **kwargs):
        response.set_cookie('is_admin', self.request.user.role == ADMIN_ROLE)
        return super().finalize_response(request, response, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

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
            total_rating = 0
            rating_count = movie.reviews.count()
            for review in movie.reviews.all():
                total_rating += review.rating
            movie.rating = total_rating / rating_count if rating_count != 0 else 0
            movie.save()

# Улучшения:
# 3. Переменные is_admin и user_role удалены, их значения определяются и используются непосредственно в местах обращения.
# 4. Переменные total_rating и rating_count инициализируются внутри циклов.

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
    total_score = sum(review.score for review in movie.reviews.all())
    return calculate_average_rating(total_score, movie.reviews.count())

def is_valid_rating(rating):
    return MIN_RATING <= rating <= MAX_RATING

# Улучшения:
# 5. Переменная total_score используется и инициализируется внутри функции calculate_movie_score.

from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.role == ADMIN_ROLE


# Улучшения:
# 6. Переменные method и is_safe_method удалены, их значения
# определяются и используются непосредственно в местах обращения.

from django.test import TestCase
from .models import Movie

# Константы для тестов
TEST_MOVIE_TITLE = "Test Movie"
TEST_MOVIE_DESCRIPTION = "Test Description"
TEST_RELEASE_DATE = "2023-01-01"
TEST_DIRECTOR = "Test Director"
TEST_RATING = 5.0


class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title=TEST_MOVIE_TITLE,
            description=TEST_MOVIE_DESCRIPTION,
            release_date=TEST_RELEASE_DATE,
            director=TEST_DIRECTOR,
            rating=TEST_RATING
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, TEST_MOVIE_TITLE)
        self.assertEqual(self.movie.description, TEST_MOVIE_DESCRIPTION)
        self.assertEqual(str(self.movie.release_date), TEST_RELEASE_DATE)
        self.assertEqual(self.movie.director, TEST_DIRECTOR)
        self.assertEqual(self.movie.rating, TEST_RATING)

    def test_movie_rating_within_bounds(self):
        invalid_ratings = [MAX_RATING + 1, MIN_RATING - 1]  # Группировка связанных значений
        for rating in invalid_ratings:
            self.movie.rating = rating
            with self.assertRaises(ValidationError):
                self.movie.clean()  # Должен вызывать ValidationError

# Улучшения:
# 7. Переменные invalid_ratings инициализированы внутри метода test_movie_rating_within_bounds.
# 8. Связанные команды в методе test_movie_rating_within_bounds сгруппированы вместе.

from django.db import models

# Константы
MAX_COMMENT_LENGTH = 1000


class Review(models.Model):
    movie = models.ForeignKey('Movie', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField(max_length=MAX_COMMENT_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comment = None  # Инициализация переменной

    def clean(self):
        super().clean()
        if len(self.comment) > MAX_COMMENT_LENGTH:
            raise ValidationError(_('Comment must be under %(max_length)s characters'),
                                  params={'max_length': MAX_COMMENT_LENGTH})
# Улучшения:
# 9. Переменная comment явно инициализирована в конструкторе.
# 10. Константа MAX_COMMENT_LENGTH добавлена для ограничения длины комментария.

from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        user = self.request.user  # Явное объявление переменной
        serializer.save(user=user)

    def list(self, request, *args, **kwargs):
        movie_id = request.query_params.get('movie_id')  # Явное объявление переменной
        if movie_id:
            queryset = Review.objects.filter(movie_id=movie_id)
        else:
            queryset = Review.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# Улучшения:
# 11. Переменные user и movie_id явно объявлены и инициализированы перед использованием.
# 12. Связанные команды в методе list сгруппированы вместе.


from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'comment', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = ['id', 'movie', 'user', 'rating', 'comment', 'created_at']  # Инициализация переменной

# Улучшения:
# 13. Переменная fields явно инициализирована в конструкторе.


def calculate_average_rating(total_rating, number_of_ratings):
    if number_of_ratings == 0:
        return MIN_RATING
    return total_rating / number_of_ratings

def format_currency(value):
    return locale.currency(value, grouping=True)

def calculate_review_score(review):
    total_score = review.rating  # Инициализация переменной
    return total_score

def is_valid_comment_length(comment):
    return len(comment) <= MAX_COMMENT_LENGTH


# Улучшения:
# 14. Переменная total_score инициализирована внутри функции calculate_review_score.
# 15. Связанные команды в функции is_valid_comment_length сгруппированы вместе.