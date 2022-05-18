def how_are_you(func):

    def wrap():
        qstn = input('Kak dela?')
        print('U menya otlichno! Ladno, derzhi svoyu function:')
        func()

    return wrap


@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()