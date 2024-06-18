"""
В рамках данного задания использовались заготовки из самообучния Django REST,  где дедался API для
'клона' IMDB
"""

# views.py

# Было:
def get_input_data(input):
    # логика

# Стало:
def get_input_data(user_input):
    # логика

# Было:
recordNum = Movie.objects.count()

# Стало:
total_records = Movie.objects.count()

# Было:
fileNumber = 5

# Стало:
file_index = 5

# Было:
file1 = request.FILES['file']

# Стало:
movie_file = request.FILES['file']

# Было:
int = movie.rating

# Стало:
rating_value = movie.rating

# Было:
sum = Movie.objects.aggregate(Sum('rating'))['rating__sum']

# Стало:
total_ratings = Movie.objects.aggregate(Sum('rating'))['rating__sum']

# Было:
max = Movie.objects.aggregate(Max('rating'))['rating__max']

# Стало:
max_rating = Movie.objects.aggregate(Max('rating'))['rating__max']

# Было:
var = some_function()

# Стало:
variable_value = some_function()

# Было:
result = query.execute()

# Стало:
query_result = query.execute()

# Было:
value = form.cleaned_data['value']

# Стало:
parameter_value = form.cleaned_data['value']

# Было:
table = Movie.objects.all()

# Стало:
movie_data = Movie.objects.all()

# Было:
variable = some_temp_value

# Стало:
temp_variable = some_temp_value