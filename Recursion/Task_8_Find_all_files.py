import os

def find_all_files(directory):
    all_files = []
    find_files_recursive(directory, all_files)
    return all_files

def find_files_recursive(current_directory, all_files):
    for entry in os.listdir(current_directory):
        full_path = os.path.join(current_directory, entry)
        if os.path.isdir(full_path):
            find_files_recursive(full_path, all_files)
        elif os.path.isfile(full_path):
            all_files.append(full_path)


directory = 'C:/Users/User/Downloads'
files = find_all_files(directory)
for file in files:
    print(file)
print(f"Всего файлов: {len(files)}")