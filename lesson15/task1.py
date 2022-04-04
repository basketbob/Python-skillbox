numbers = [3, 7, 5]
while True:
    number = int(input('New number: '))
    numbers.append(number)
    print('Current list of numbers:', numbers)
    for i in numbers:
        print(i**2, i**3, i**4)
    print()