S = input('Введите строку: ')
new_str = ''
cnt = 0
for symb in S:
    if (symb == ':'):
        new_str += ';'
        cnt += 1
    else:
        new_str += symb
print(new_str)
print(cnt)