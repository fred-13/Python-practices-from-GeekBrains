
from add_dir import add_dirs, remove_dirs
import os, shutil

print("---------------------Task-1--------------------------\n")

key = input("Введите 1 - если хотите создать директории, 2 - если удалить их: ")

if key == '1':
    add_dirs("dir_", 10)
elif key == '2':
    remove_dirs("dir_", 10)
else:
    print("Вы не сделали выбор")

print("\n-----------------------------------------------------\n")

print("---------------------Task-2--------------------------\n")

print([d for d in os.listdir(os.getcwd()) if os.path.isdir(d)])

print("\n-----------------------------------------------------\n")

print("---------------------Task-3--------------------------\n")

print(os.path.basename(__file__))
shutil.copyfile(os.path.basename(__file__), "COPY-" + os.path.basename(__file__))

print("\n-----------------------------------------------------")
