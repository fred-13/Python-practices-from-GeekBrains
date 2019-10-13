enterprises = {}
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    ename = input(str(i + 1) + "-е предприятие: ")
    profit = 0
    for i in range(4):

        profit += int(input("Прибыль за {}-й квартал: ".format(i + 1)))
    enterprises[ename] = profit
    s += profit

avrg = s / n
print(enterprises)
print("\nСредния прибыль за год: {}. Предприятия, чья прибыль выше средне:".format(avrg))

for i in enterprises:
    if enterprises[i] > avrg:
        print(i)

print("\nСредния прибыль за год: {}. Предприятия, чья прибыль ниже средне:".format(avrg))

for i in enterprises:
    if enterprises[i] < avrg:
        print(i)