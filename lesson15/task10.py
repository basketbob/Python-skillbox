list = [1,4,-3,0,10]
loop_cnt = len(list) - 1
for _ in range(loop_cnt):
    for i in range(loop_cnt):
        if (list[i] > list[i+1]):
            list[i], list[i+1] = list[i+1], list[i]

print(list)