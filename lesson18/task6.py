txt = 'WRONG'

while True:
    pwd = input('password: ')
    if (len(pwd) < 8):
        print(txt, 'length, need min 8 chars')
        continue
    if (len([x for x in pwd if (x.isupper())]) == 0):
        print(txt, 'upper case, need at least 1')
        continue
    if (len([x for x in pwd if (x.isdigit())]) < 3):
        print(txt, 'digits, need at list 3 digits')
        continue
    break

print('OK')
