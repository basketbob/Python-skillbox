list = [1,2,3,4,5] #[1,2,1,2,2]
len_list = len(list)
answer = []
print('old list: ', list)
for i in range(len_list):
    temp_list = list[i:len_list]
    if (temp_list == temp_list[::-1]):
        answer = list[0:i]
        list.extend(answer[::-1])
        break

print('answer:', answer)
print('new list:', list)
