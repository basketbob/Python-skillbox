def func_1(x):
    return x + 10


def func_2(func, *args, **kwargs):
    result = func(*args, **kwargs)
    return result**2


print(func_2(func_1, 9))

import time as t


def timer(func, *args, **kwargs):
    start = t.time()
    f = func(*args, **kwargs)
    end = t.time()
    return round(end - start, 4)


print(timer(func_1, 999999))
