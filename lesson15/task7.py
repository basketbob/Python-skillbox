list = [1,2,3,4,5,6,7,8]
cnt = len(list)
shift = int(input('vvedite sdvig: '))
new_list = []
for v in list:
    new_list.append(v)

for sh in range(shift):
    if (sh != 0):
        for ind in range(cnt):
            list[ind] = new_list[ind]
    for i in range(cnt):
        ind = (i + 1) if i < (cnt - 1) else 0
        new_list[ind] = list[i]

print(list)
print(new_list)
