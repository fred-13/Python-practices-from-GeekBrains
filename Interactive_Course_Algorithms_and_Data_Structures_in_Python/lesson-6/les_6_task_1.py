
import sys
size_value = [] # обнулять перед запуском 2 варианта
def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, object={x}')
    size_value.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

# 1 вариант
a = [0] * 8
b = [i for i in range(2, 100)]

for i in b:
    if i % 2 == 0:
        a[0] += 1
    if i % 3 == 0:
        a[1] += 1
    if i % 4 == 0:
        a[2] += 1
    if i % 5 == 0:
        a[3] += 1
    if i % 6 == 0:
        a[4] += 1
    if i % 7 == 0:
        a[5] += 1
    if i % 8 == 0:
        a[6] += 1
    if i % 9 == 0:
        a[7] += 1
print(a)
show_size(i)
print(sum(size_value))
show_size(a)
print(sum(size_value))
show_size(b)
print(sum(size_value))

# 2 вариант
a = [0] * 8
i = 2

while i <= 9:
    for num in b:
        if num % i == 0:
            a[i - 2] += 1
    i += 1
print(a)

size_value = []
print(a)
show_size(i)
print(sum(size_value))
show_size(a)
print(sum(size_value))
