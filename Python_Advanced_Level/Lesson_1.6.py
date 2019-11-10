import locale

RESURS_STRING = ['сетевое программирование', 'сокет', 'декоратор']

with open('resurs.txt', 'w+') as f_n:
    for i in RESURS_STRING:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)

FILE_CODING = locale.getpreferredencoding()

with open('resurs.txt', 'r', encoding=FILE_CODING) as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)
