emp_cnt = int(input('emp count: ')) + 1
emps = []
for i in range(1, emp_cnt):
    emps.append(int(input('Зарплата ' + str(i) + ' сотрудника: ')))

for zp in emps:
    if (zp == 0):
        emps.remove(0)
print(emps)
