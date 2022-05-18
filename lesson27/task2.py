import time

def slowly(func):
    def wrap():
        time.sleep(5)
        func()
    return wrap


@slowly
def some_func():
    print('here!')


some_func()