def is_symmetric(list):
    new_list = []
    for v in list[::-1]:
        new_list.append(v)

    return new_list == list


#list = [1,2,3,4,5]
list = [1,2,1,2,2]
len_list = len(list)
answer = []
print('old list: ', list)
for i in range(len_list):
    if (is_symmetric(list[i:len_list])):
        answer = list[0:i]
        list.extend(answer[::-1])
        break

print('answer:', answer)
print('new list:', list)
