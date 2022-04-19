user_str = input('user str: ')

try:
    file = open('test.txt', 'r')
    file.write(user_str)
    print('test')
except (FileNotFoundError):
    print('Проблема при открытии файла')
else:
    print('else block')
finally:
    print('finally block!')

print('end!')