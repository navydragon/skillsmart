import os


def find_files(dir_path):
    # Проверяем, является ли указанный путь допустимой директорией
    if not os.path.isdir(dir_path):
        return

    # Получаем список всех файлов и директорий в указанной директории
    files_and_dirs = os.listdir(dir_path)

    # Итерация по списку файлов и директорий
    for file_or_dir in files_and_dirs:
        # Создаем полный путь к файлу или директории
        full_path = os.path.join(dir_path, file_or_dir)

        # Если полный путь является директорией, рекурсивно вызываем функцию для поиска файлов в этой директории
        if os.path.isdir(full_path):
            find_files(full_path)
        else:
            # Печатаем путь к файлу
            print(full_path)


# Пример использования
directory = 'C:/Users/User/Downloads'
find_files(directory)
