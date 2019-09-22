from random import random

m1 = int(input("Введите первое целое число: "))
m2 = int(input("Введите второе целое число: "))
n = int(random() * (m2 - m1 + 1)) + m1
print(n)

m1 = float(input("Введите первое вещественное число: "))
m2 = float(input("Введите второе вещественное число: "))
n = random() * (m2 - m1) + m1
print(round(n, 3))

m1 = ord(input("Введите первый символ: "))
m2 = ord(input("Введите второй символ: "))
n = int(random() * (m2 - m1 + 1)) + m1
print(chr(n))