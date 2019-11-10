VAR = ['разработка', 'администрирование', 'protocol', 'standard']

for i in VAR:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print('#' * 30)
