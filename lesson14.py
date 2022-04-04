numm = int(input('число:'))
degree = int(input('степень:'))


def power(a, n):
    global numm

    n = n - 1 if (n > 0) else n + 1
    if (n != 0):
        numm *= a
        power(a, n)
    else:
        print('Рекурсия закончилась!')


power(numm, degree)
print(numm)
