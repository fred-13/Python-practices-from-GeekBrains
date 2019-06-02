
import os
from add_dir import add_dirs, remove_dirs

print("---------------------Task-1--------------------------\n")

print('''
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
''')

key = input("Выберите действие: ")

if key == '1':
    os.chdir(os.getcwd() + '/' + input("Введите название папки: "))
    print("Вы находитесь в директории: ", os.getcwd())
elif key == '2':
    print("\nСодержимое данной папки:\n")
    print(os.listdir())
elif key == '3':
    name_dir = input("Введите название папки которую хотите удалить: ")
    remove_dirs(name_dir, 2)
    print("Вы удалили: " + name_dir)
elif key == '4':
    name_dir = input("Введите название папки которую хотите создать: ")
    add_dirs(name_dir, 2)
    print("Вы создали: " + name_dir)

print("\n-----------------------------------------------------")
