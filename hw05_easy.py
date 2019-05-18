
from add_dir import add_dirs, remove_dirs
import os, shutil

print("---------------------Task-1--------------------------\n")

key = input("Введите 1 - если хотите создать директории, 2 - если удалить их: ")

if key == '1':
    add_dirs()
elif key == '2':
    remove_dirs()
else:
    print("Вы не сделали выбор")

print("\n-----------------------------------------------------\n")

print("---------------------Task-2--------------------------\n")

print([x[0] for x in os.walk(os.getcwd())])

print("\n-----------------------------------------------------\n")

print("---------------------Task-3--------------------------\n")

print(os.path.basename(__file__))
shutil.copyfile(os.path.basename(__file__), "COPY-" + os.path.basename(__file__))

print("\n-----------------------------------------------------")