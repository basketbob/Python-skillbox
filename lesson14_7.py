first_year = int(input('1год:'))
second_year = int(input('2год:'))

print('Годы от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')
for year in range(first_year, second_year + 1):
    for n in str(year):
        cnt = 0
        for n_copy in str(year):
            if (n == n_copy):
                cnt += 1
        if (cnt == 3):
            print(year)
            break