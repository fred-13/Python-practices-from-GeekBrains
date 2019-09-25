from random import random
N = 10
arr = [0] * N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)