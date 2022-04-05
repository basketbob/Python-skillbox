
def wrong_elem(list):
    ind = 0

    print('Неподходящие значения:', end=' ')
    for elem in list:
        if (elem < ind):
            print(elem, end = ' ')
        ind += 1

list = [1,2,3,4,8,9,10,5,6,12,20]
wrong_elem(list)