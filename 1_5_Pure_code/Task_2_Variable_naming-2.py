"""
В рамках данного задания использовались заготовки из самообучния Django REST,  где дедался API для
'клона' IMDB
"""

"""
6.1. Разберите свой код, и сделайте пять примеров, где можно более наглядно учесть в именах переменных 
уровни абстракции.
"""
# Неправильное имя: get_movies()
# Правильное имя: fetch_movies_from_db()
# Уровень абстракции "fetch" указывает, что данные получаются из базы данных.

# Неправильное имя: calculate_average_rating()
# Правильное имя: compute_movie_average_rating()
# Уровень абстракции "compute" указывает на более точный процесс вычисления средней оценки для фильма.

# Неправильное имя: user_id
# Правильное имя: authenticated_user_id
# Уровень абстракции "authenticated" указывает, что речь идет об аутентифицированном пользователе.

# Неправильное имя: process_request()
# Правильное имя: handle_api_request()
# Уровень абстракции "handle" указывает на обработку запроса в контексте API.

# Неправильное имя: rate_movie()
# Правильное имя: submit_movie_rating()
# Уровень абстракции "submit" указывает на действие отправки рейтинга фильма.


"""
6.2. Приведите четыре примера, где вы в качестве имён переменных использовали или могли бы использовать технические термины из информатики.
"""

# cache_key
# "cache" указывает на ключ кэширования для сохранения данных.

# serializer_data
# "serializer" указывает на сериализацию данных для API.

# request_payload
# "payload" указывает на данные запроса, отправляемые клиентом.

# pagination_queryset
# "pagination" указывает на набор данных, используемый для постраничного вывода.

"""
6.3. Придумайте или найдите в своём коде три примера, когда имена переменных даны с учётом контекста (функции, метода, класса).
"""
# Пример в контексте класса:
class MovieViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        return MovieDetailSerializer

# Пример в контексте функции:
def filter_movies_by_genre(movies_queryset, genre):
    filtered_movies = movies_queryset.filter(genre=genre)
    return filtered_movies

# Пример в контексте метода:
class MovieRatingService:
    def calculate_average_rating(self, movie):
        total_ratings = movie.ratings.aggregate(Sum('score'))
        rating_count = movie.ratings.count()
        average_rating = total_ratings / rating_count
        return average_rating


"""
6.4. Найдите пять имён переменных в своём коде, длины которых не укладываются в 8-20 символов, и исправьте, чтобы они укладывались в данный диапазон.
"""
# row => user_score
# rate => user_rating
# total => total_revenue
# movies => movie_list
# curr => current_movie