
print("---------------------Task-1--------------------------\n")

def write_file(reports):

    filename = open('salary.txt', 'w', encoding='utf-8')
    for key, value in reports.items():
        filename.write(key + " - " + str(value) + "\n")
    filename.close()

def read_file(db):
    for i in range(len(db)):
        x = db[i].split(' - ')
        if int(x[1]) < 500000:
            print(x[0].upper() + " - " + str((int(x[1]) * 0.87)))

humans_list = ['Petr', 'Vasya', 'Ruslan', 'Ivan', 'Timur', 'Oleg', 'Andrey', 'Egor', 'Ilya']
wages_list = [5000, 12000, 110000, 10000, 250000, 9000, 15000, 500000, 14000]
dictionary = dict(zip(humans_list, wages_list))

write_file(dict(zip(humans_list, wages_list)))

filename2 = open('salary.txt', 'r', encoding='utf-8')
database = [line.strip() for line in filename2]
filename2.close()

read_file(database)

print("\n-----------------------------------------------------\n")