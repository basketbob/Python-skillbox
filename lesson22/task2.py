file = open('../../test_files/testFile.txt', 'r', encoding='utf-8')

strings = file.read().split('\n')
for s in strings[::-1]:
    print(s)
