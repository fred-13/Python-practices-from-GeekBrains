
import os

def add_dirs(name_dir1, index1):
    if index1 == 2:
        try:
            for i in range(1, index1):
                os.mkdir(os.path.join(os.getcwd(), name_dir1))
        except FileExistsError:
            print("Эти директории уже созданы!")
    else:
        try:
            for i in range(1, index1):
                os.mkdir(os.path.join(os.getcwd(), name_dir1 + str(i)))
        except FileExistsError:
            print("Эти директории уже созданы!")

def remove_dirs(name_dir2, index2):
    if index2 == 2:
        try:
            for i in range(1, index2):
                os.rmdir(os.path.join(os.getcwd(), name_dir2))
        except OSError:
            print("Эти директории уже удалены!")
    else:
        try:
            for i in range(1, index2):
                os.rmdir(os.path.join(os.getcwd(), name_dir2 + str(i)))
        except OSError:
            print("Эти директории уже удалены!")
