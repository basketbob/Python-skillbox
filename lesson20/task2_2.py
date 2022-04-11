import math

def full_s(r, h):
    side = 2 * math.pi * r * h
    S = math.pi * r**2
    full = side + 2 * S
    return side, full

r = int(input('r = '))
h = int(input('h = '))
full = full_s(r, h)
print(full[0])
print(full[1])