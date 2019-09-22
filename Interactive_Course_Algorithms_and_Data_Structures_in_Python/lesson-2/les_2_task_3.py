n = int(input("Введите число: "))
m = 0
while n > 0:
    m = m * 10 + n % 10
    print(m)
    n = n // 10
print(m)