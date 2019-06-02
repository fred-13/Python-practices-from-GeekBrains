
print("---------------------Task-1--------------------------\n")


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage)
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage)
            if self.health <= 0:
                self.health = 0

        print('{} получил урон и теперь имеет {} здоровья, {} брони'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person.__damage(self.damage)


class Player(Person):

    def __info(self):
        print("It is Player!")


class Enemy(Person):

    def __info(self):
        print("It is Enemy!")


class Fight:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print('\n {} победил!'.format(person1.name))
                break
            person2.punch(person1)
            if person1.health == 0:
                print('\n {} победил!'.format(person2.name))


player = Player('Player 1', 100, 20, 50)
enemy = Enemy('Player 2', 100, 20, 50)

fighting = Fight(player, enemy)
fighting.start(player, enemy)


print("\n-----------------------------------------------------")