import random

class Unit:
    health = 100
    def __init__(self, name):
        self.name = name

    def hit(self, enemy):
        enemy.health -= 20

    def print_info(self):
        print(self.name, self.health)

u1 = Unit('Vova')
u2 = Unit('Petya')
while u1.health > 0 and u2.health > 0:
    who = random.getrandbits(1)
    if (who):
        u1.hit(u2)
    else:
        u2.hit(u1)
    u1.print_info()
    u2.print_info()
    print()
