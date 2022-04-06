list = [1,2,3]
second_list = [2,4,6,3,3,2,1]
new_list = []

list.extend(second_list)
while len(list) > 0:
    v = list[0]
    new_list.append(v)
    cnt = list.count(v)
    for _ in range(cnt):
        list.remove(v)
print(new_list)
