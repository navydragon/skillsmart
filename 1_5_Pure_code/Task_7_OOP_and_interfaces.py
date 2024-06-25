"""
Данные задание выполнено в контексте Django REST API для 'клона' IMDB
"""

"""
3.1. Сделайте в своём коде три примера наглядных методов-фабрик.
"""

# 1
class UserFactory:
    @staticmethod
    def create_with_email(username, email, password):
        return User.objects.create_user(username=username, email=email, password=password)

    @staticmethod
    def create_without_email(username, password):
        return User.objects.create_user(username=username, password=password)

# 2
class MovieFactory:
    @staticmethod
    def create_with_full_details(title, description, release_date, director):
        return Movie.objects.create(title=title, description=description, release_date=release_date, director=director)

    @staticmethod
    def create_basic(title, release_date):
        return Movie.objects.create(title=title, release_date=release_date)

# 3
class ReviewFactory:
    @staticmethod
    def create_with_rating_and_comment(movie, user, rating, comment):
        return Review.objects.create(movie=movie, user=user, rating=rating, comment=comment)

    @staticmethod
    def create_with_rating_only(movie, user, rating):
        return Review.objects.create(movie=movie, user=user, rating=rating)
"""
3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы, 
напишите несколько примеров их правильного именования.
"""

# не использовал но попробую

# Абстрактный класс для сервиса рецензий

from abc import ABC, abstractmethod

class ReviewService(ABC):
    @abstractmethod
    def add_review(self, movie, user, rating, comment=None):
        pass

    @abstractmethod
    def get_reviews(self, movie):
        pass

class DefaultReviewService(ReviewService):
    def add_review(self, movie, user, rating, comment=None):

        pass

    def get_reviews(self, movie):
        pass