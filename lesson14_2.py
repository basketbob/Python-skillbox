print('1point:')
x1 = float(input('x:'))
y1 = float(input('y:'))

print('\n2point:')
x2 = float(input('x:'))
y2 = float(input('y:'))

x_diff = x1 - x2
y_diff = y1 - y2
k = 0 if x_diff == 0 else y_diff / x_diff
b = y2 - k * x2

print('уравнение')
print('y = ', k, '* x +', b)
