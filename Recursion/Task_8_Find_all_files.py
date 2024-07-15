import os

def find_files(dir_path):
    all_files = []

    def _find_files_recursive(current_directory):
        if not os.path.isdir(current_directory):
            return

        # Получаем список всех файлов
        files_and_dirs = os.listdir(current_directory)

        # Итерация
        for file_or_dir in files_and_dirs:
            full_path = os.path.join(current_directory, file_or_dir)

            if os.path.isdir(full_path):
                _find_files_recursive(full_path)
            else:
                all_files.append(full_path)

    _find_files_recursive(dir_path)
    return all_files


directory = 'C:/Users/User/Downloads'
files = find_files(directory)
for file in files:
    print(file)
print(f"Всего файлов: {len(files)}")
