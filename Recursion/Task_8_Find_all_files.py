import os


def find_files(dir_path):
    if not os.path.isdir(dir_path):
        return []

    all_files = []
    stack = [dir_path]

    while stack:
        current_directory = stack.pop()

        files_and_dirs = os.listdir(current_directory)

        for file_or_dir in files_and_dirs:
            full_path = os.path.join(current_directory, file_or_dir)

            if os.path.isdir(full_path):
                stack.append(full_path)
            elif os.path.isfile(full_path):
                all_files.append(full_path)

    return all_files


# Пример использования
directory = 'C:/Users/User/Downloads'
files = find_files(directory)
for file in files:
    print(file)
print(f"Всего файлов: {len(files)}")
