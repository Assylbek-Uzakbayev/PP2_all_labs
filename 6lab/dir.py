import os
def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    return directories, files, all_items

path = "."
directories, files, all_items = list_directories_files(path)
print("Каталоги:", directories)
print("Файлы:", files)
print("Все:", all_items)



import os
def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

path = "."
exists, readable, writable, executable = check_path_access(path)
print(f"Существует: {exists}, Читаемый: {readable}, Записываемый: {writable}, Исполняемый: {executable}")




import os
def check_path_and_get_info(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return directory, filename
    else:
        return None, None

path = "example.txt"
directory, filename = check_path_and_get_info(path)
if directory and filename:
    print(f"Каталог: {directory}, Имя файла: {filename}")
else:
    print("Путь не существует")



def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file_path = "example.txt"
num_lines = count_lines_in_file(file_path)
print(f"Количество строк: {num_lines}")



def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

file_path = "output.txt"
lst = ["apple", "banana", "cherry"]
write_list_to_file(file_path, lst)



import string
def create_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")

create_text_files()
print("Файлы A.txt - Z.txt созданы")



def copy_file_content(src, dst):
    with open(src, 'r') as source_file:
        content = source_file.read()
    with open(dst, 'w') as destination_file:
        destination_file.write(content)

src = "source.txt"
dst = "destination.txt"
copy_file_content(src, dst)
print(f"Содержимое файла {src} скопировано в {dst}")



import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False

path = "example.txt"
if delete_file(path):
    print(f"Файл {path} удален")
else:
    print(f"Не удалось удалить файл {path}")




import os
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False

path = "example.txt"
if delete_file(path):
    print(f"Файл {path} удален")
else:
    print(f"Не удалось удалить файл {path}")



























