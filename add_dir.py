
import os

def add_dirs():

    try:
        for i in range(1, 10):
            os.mkdir(os.path.join(os.getcwd(), "dir_" + str(i)))
    except FileExistsError:
        print("Эти директории уже созданы!")

def remove_dirs():

    try:
        for i in range(1, 10):
            os.rmdir(os.path.join(os.getcwd(), "dir_" + str(i)))
    except OSError:
        print("Эти директории уже удалены!")

