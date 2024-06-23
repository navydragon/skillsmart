"""
В рамках данного задания использовались заготовки из самообучния Django REST,  где дедался API для
'клона' IMDB
"""
# Выполните 12 улучшений имён функций/методов в вашем коде в формате "было - стало - ваш комментарий

Было: def get_all()
Стало: def get_all_movies()
Комментарий: Уточнено, что метод получает все фильмы.

Было: def add(data)
Стало: def add_movie(data)
Комментарий: Уточнено, что метод добавляет фильм.

Было: def update(id, data)
Стало: def update_movie(id, data)
Комментарий: Уточнено, что метод обновляет информацию о фильме.

Было: def remove(id)
Стало: def delete_movie(id)
Комментарий: Уточнено, что метод удаляет фильм.

Было: def info(user_id)
Стало: def get_user_info(user_id)
Комментарий: Уточнено, что метод получает информацию о пользователе.

Было: def update_profile(user_id, data)
Стало: def update_user_profile(user_id, data)
Комментарий: Уточнено, что метод обновляет профиль пользователя.

Было: def add_review(data)
Стало: def create_movie_review(data)
Комментарий: Уточнено, что метод создаёт отзыв на фильм.

Было: def get_reviews()
Стало: def get_movie_reviews()
Комментарий: Уточнено, что метод получает отзывы на фильмы.

Было: def add_actor(data)
Стало: def create_actor(data)
Комментарий: Уточнено, что метод добавляет актёра.

Было: def get_actors()
Стало: def list_actors()
Комментарий: Уточнено, что метод возвращает список актёров.

Было: def details(id)
Стало: def get_movie_details(id)
Комментарий: Уточнено, что метод получает детали фильма.

Было: def update_review(review_id, data)
Стало: def update_movie_review(review_id, data)
Комментарий: Уточнено, что метод обновляет отзыв на фильм.