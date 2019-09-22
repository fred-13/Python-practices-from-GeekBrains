n = int(input("Input number: "))
s = 0
for i in range(1, n+1):
    s += i
m = n * (n + 1) // 2
print("Summ = ", s)
print("n(n+1)/2 = ", m)