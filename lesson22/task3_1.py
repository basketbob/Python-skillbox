file = open('../../test_files/testFile.txt', 'r', encoding='utf-8')
# data = file.read()
# print(data)
for s in file:
    print(s, end='')
file.close()
