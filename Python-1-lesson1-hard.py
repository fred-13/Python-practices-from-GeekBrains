#---------------------Task-1--------------------------

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
years_old = input("Сколько вам лет: ")
weight = input("Какой у вас вес (кг): ")

if (int(years_old) >= 20) and (int(years_old) <= 30):
    if (int(weight) > 50 and int(weight) < 120 ):
        print(name + " " + surname + " у вас хорошее состояние")
    else:
        print(name + " " + surname + " вам следует заняться собой")

elif (int(years_old) > 30) and (int(years_old) <= 50):
    if (int(weight) > 50 and int(weight) < 120 ):
        print(name + " " + surname + " у вас хорошее состояние")
    else:
        print(name + " " + surname + " вам следует обратится к врачу!")

#-----------------------------------------------------