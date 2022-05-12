import math


class Circle:
    x = 0
    y = 0
    r = 1

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def sqr(self):
        print('square =', math.pi * self.r**2)

    def perimetr(self):
        print('perimetr =', 2 * math.pi * self.r)

    def increase(self, k):
        self.r *= k

    def cross(self, circle2):
        d = math.sqrt((self.x - circle2.x)**2 + (self.y - circle2.y)**2)
        if d > self.r+circle2.r:
            print('Circumference are not intersect')
        else:
            print('Circumference are intersect')


c1 = Circle(1, 2, 3)
c2 = Circle(3, 4, 5)

c1.sqr()
c2.sqr()
print()

c1.perimetr()
c2.perimetr()
print()

c1.cross(c2)
