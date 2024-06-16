"""
В рамках данного задания использовались заготовки из самообучния Django REST,  где дедался API для
'клона' IMDB
"""
"""
7.1. Приведите пять примеров правильного именования булевых переменных в вашем 
коде в формате "было - стало".
"""
# errorFlag - isError
# userExists - isUserExists
# notFound - isFound
# processingComplete - isProcessingComplete
# valid - isValid
"""
7.2. Найдите несколько подходящих случаев, когда в вашем коде можно использовать
типичные имена булевых переменных.
"""
# Было:
operation_status = False
if perform_operation():
    operation_status = True

# Стало:
success = False
if perform_operation():
    success = True

# Было:
user_present = False
if user in user_list:
    user_present = True

# Стало:
found = False
if user in user_list:
    found = True

"""
7.3. Проверьте, правильно ли вы даёте имена индексам циклов. Попробуйте найти 
случай, когда вместо i j k нагляднее использовать более выразительное имя.
"""

# Было:
for i in range(len(movie_list)):
    # обработка каждого фильма

# Стало:
for movie_index in range(len(movie_list)):
    # обработка каждого фильма

# Было:
for j in range(len(reviews)):
    # обработка каждого отзыва

# Стало:
for review_index in range(len(reviews)):
    # обработка каждого отзыва


"""
7.4. Попробуйте найти в своих решениях два-три случая, когда можно
использовать пары имён - антонимы.
"""
# Было:
access_granted = False
if user.has_permission():
    access_granted = True

# Стало:
locked = True
if user.has_permission():
    locked = False

# Было:
for i in range(len(movie_list)):
    if i == 0:
        process_start = True
    if i == len(movie_list) - 1:
        process_end = True

# Стало:
process_start = False
process_end = False
for movie_index in range(len(movie_list)):
    if movie_index == 0:
        process_start = True
    if movie_index == len(movie_list) - 1:
        process_end = True


"""
7.5. Всем ли временным переменным в вашем коде присвоены выразительные имена? 
Найдите несколько случаев, когда временные переменные надо переименовать, и 
поищите, возможно, от некоторых временных переменных вам получится вообще полностью избавиться.
"""

# Было:
temp = Movie.objects.filter(title='Inception')
if temp.exists():
    movie = temp.first()

# Стало:
matching_movies = Movie.objects.filter(title='Inception')
if matching_movies.exists():
    movie = matching_movies.first()


# Было:
temp_user = User.objects.get(id=1)
if temp_user.is_active:
    active_user = temp_user

# Стало:
user = User.objects.get(id=1)
if user.is_active:
    active_user = user
