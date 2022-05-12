import random

class Toyota:
    color = 'red'
    cost = 1000000
    max_speed = 200
    current_speed = 0

    def print_info(self):
        print("Color: {}, cost: {}, max speed: {}, speed: {}".format(
            self.color, self.cost, self.max_speed, self.current_speed
        ))

    def set_speed(self, speed):
        self.current_speed = speed

car1 = Toyota()
car2 = Toyota()
car3 = Toyota()

car1.set_speed(random.randint(0, 200))
car2.set_speed(random.randint(0, 200))
car3.set_speed(random.randint(0, 200))

car1.print_info()
car2.print_info()
car3.print_info()

