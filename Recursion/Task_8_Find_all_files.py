import os

def find_files(dir_path):
    all_files = []

    if not os.path.isdir(dir_path):
        return []

    # Получаем список всех файлов и директорий
    files_and_dirs = os.listdir(dir_path)

    for file_or_dir in files_and_dirs:
        full_path = os.path.join(dir_path, file_or_dir)

        # Если полный путь является директорией, рекурсивно вызываем функцию
        if os.path.isdir(full_path):
            all_files.extend(find_files(full_path))
        else:
            # Добавляем путь к файлу в список
            all_files.append(full_path)

    return all_files

# Пример использования
directory = 'C:/Users/User/Downloads'
files = find_files(directory)
for file in files:
    print(file)
print(f"Всего файлов: {len(files)}")
