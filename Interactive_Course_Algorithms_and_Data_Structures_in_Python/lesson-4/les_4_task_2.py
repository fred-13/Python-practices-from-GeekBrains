import math

#-------------------Решето Эратосфена 1---------------------#
def eratosfen(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return print(b)

#-------------------Решето Эратосфена 2---------------------#

def eratosfen_2(N):
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
    return print(sieve)

print("Решето Эратосфена метод первый: ")
eratosfen(20)

print("Решето Эратосфена метод второй: ")
eratosfen_2(20)

#--------------------Решето Сундарама---------------------#

def sundaram(n):
    b = list()
    a = [0] * n
    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0
        for i in range(1, n):
            if a[i] == 0:
                b.append(2 * i + 1)
        return print(b)

print("Решето Сундарама")
sundaram(20)