def boolka(func):
    def wrapped_func(*args, **kwargs):
        print('</----------\>')
        func(*args, **kwargs)
        print('<\______/>')
        return

    return wrapped_func

def ingridienty(func):
    def wrapped_func(*args, **kwargs):
        print('#помидоры#')
        func(*args, **kwargs)
        print('~salad~')
        return

    return wrapped_func


@boolka
@ingridienty
def sandwich():
    print('--vetchina--')


sandwich()
