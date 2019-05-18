
print("---------------------Task-1--------------------------\n")

from add_dir import add_dirs, remove_dirs

key = input("Введите 1 - если хотите создать директории, 2 - если удалить их: ")

if key == '1':
    add_dirs()
elif key == '2':
    remove_dirs()

print("\n-----------------------------------------------------\n")