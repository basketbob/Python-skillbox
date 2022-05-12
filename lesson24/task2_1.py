import random

class Toyota:
    color = 'red'
    cost = 1000000
    max_speed = 200
    current_speed = 0

car1 = Toyota()
car2 = Toyota()
car3 = Toyota()

car1.current_speed = random.randint(0, 200)
car2.current_speed = random.randint(0, 200)
car3.current_speed = random.randint(0, 200)

print(car1.current_speed)
print(car2.current_speed)
print(car3.current_speed)

