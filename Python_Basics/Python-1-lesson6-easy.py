
print("---------------------Task-1--------------------------\n")

class TownCar:

    def __init__(self, speed, color, name, is_police):
        self.speeds = speed
        self.colors = color
        self.names = name
        self.is_polices = is_police

    def go(self):

        print("the car went")

    def stop(self):

        print("the car stopped")

    def turn(self):

        print("the car turned")


class SportCar:

    def __init__(self, speed, color, name, is_police):
        self.speeds = speed
        self.colors = color
        self.names = name
        self.is_polices = is_police

    def go(self):

        print("the car went")

    def stop(self):

        print("the car stopped")

    def turn(self):

        print("the car turned")


class WorkCar:

    def __init__(self, speed, color, name, is_police):
        self.speeds = speed
        self.colors = color
        self.names = name
        self.is_polices = is_police

    def go(self):

        print("the car went")

    def stop(self):

        print("the car stopped")

    def turn(self):

        print("the car turned")


class PoliceCar:

    def __init__(self, speed, color, name, is_police):
        self.speeds = speed
        self.colors = color
        self.names = name
        self.is_polices = is_police

    def go(self):

        print("the car went")

    def stop(self):

        print("the car stopped")

    def turn(self):

        print("the car turned")


car_1 = TownCar("80km/h", "Red", "MiniCuper", "H102CV")
car_2 = SportCar("300km/h", "Yellow", "Lamborghini", "B201DC")
car_3 = WorkCar("120km/h", "White", "Lada_Granta", "Y152KL")
car_4 = PoliceCar("180km/h", "Blue", "UAZ_Patriot", "A452JW")

print("\n-----------------------------------------------------\n")

print("---------------------Task-2--------------------------\n")


class TownCar:

    def __init__(self, speed, color, name, is_police):
        self.speeds = speed
        self.colors = color
        self.names = name
        self.is_polices = is_police

    def go(self):
        print("the car went")

    def stop(self):

        print("the car stopped")
    def turn(self):
        print("the car turned")

    def who_is(self):
        print("this is a city driver's car")

class SportCar(TownCar):

    def car_racer(self):
        print("this is a car racer")

class WorkCar(TownCar):

    def who_is(self):
        print("this is a hard worker car")

class PoliceCar(TownCar):

    def who_is(self):
        print("this is a police car")


car_1 = TownCar("80km/h", "Red", "MiniCuper", "H102CV")
car_2 = SportCar("300km/h", "Yellow", "Lamborghini", "B201DC")
car_3 = WorkCar("120km/h", "White", "Lada_Granta", "Y152KL")
car_4 = PoliceCar("180km/h", "Blue", "UAZ_Patriot", "A452JW")


print("\n-----------------------------------------------------\n")