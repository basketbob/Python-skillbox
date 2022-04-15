BRUCE_WILLIS = 42

input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except (ValueError):
    print('невозможно преобразовать к числу')
except (IndexError):
    print('выход за границы списка')
except:
    print('остальные исключения')