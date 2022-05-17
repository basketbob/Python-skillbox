def square_iter(n):
    for i_n in range(1, n+1):
        yield i_n**2


N = int(input('vvedite chislo:'))
gen = (i_n**2 for i_n in range(1, N+1))
for i in gen:
    print(i)
print('\n\n\n')


def compareGen(list1, list2, to_find):
    for x in list1:
        for y in list2:
            result = x * y
            yield ' '.join([str(x), str(y), str(result)])
            if result == to_find:
                yield 'Found!!!'
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
for x in compareGen(list_1, list_2, to_find):
    print(x)
