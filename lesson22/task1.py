file = open('../../test_files/testFile.txt', 'r', encoding='utf-8')
summa = 0
data = file.read()
data = data.split()
for n in data:
    if n.isnumeric():
        summa += int(n)

file.close()
print(summa)

file = open('../../test_files/answer.txt', 'w', encoding='utf-8')
file.write(str(summa))
file.close()
