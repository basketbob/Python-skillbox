def remove_from_list(list):
    maxnum = 0
    for elem in list:
        if (elem > maxnum):
            maxnum = elem

    new_list = []
    for elem in list:
        if (elem != maxnum):
            new_list.append(elem)

    return new_list


videocards = []
cnt = int(input('count: '))
for i in range(cnt):
    print(i+1, 'videocard', end=' ')
    videocards.append(int(input()))

print('старый:', videocards)
print('new:', remove_from_list(videocards))
