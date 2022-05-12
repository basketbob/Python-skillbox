from random import randint


class Human:
    satiety = 50

    def __init__(self, name):
        self.home = Home()
        self.name = name

    def eat(self):
        self.satiety += 1
        self.home.food -= 1

    def work(self):
        self.satiety -= 1
        self.home.money += 1

    def game(self):
        self.satiety -= 1

    def shop(self):
        self.home.food -= 1
        self.home.money -= 1

    def do_action(self):
        alive = True
        for i in range(365):
            cube = randint(1, 6)

            if self.satiety < 20:
                self.eat()
            elif self.home.food < 10:
                self.shop()
            elif self.home.money < 50:
                self.work()
            elif cube == 1:
                self.work()
            elif cube == 2:
                self.eat()
            else:
                self.game()

            if self.satiety < 0:
                alive = False
                break

        print(self.name, 'alive' if alive else 'Wasted!')


class Home:
    food = 50
    money = 0


h1 = Human('Vasya')
h1.do_action()