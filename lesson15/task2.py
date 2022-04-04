numbers = []
for new_num in range(101):
    numbers.append(new_num)
print(numbers)

emp_cnt = int(input('epmloyers count:'))
emp_ids = []
for emp in range(emp_cnt):
    emp_ids.append(int(input('ID emp:')))

search_id = int(input('which id searching?'))

working = False
for id in emp_ids:
    if (id == search_id):
        working = True

if (not working):
    print('Employer don\'t working!')
else:
    print('All are working!')
