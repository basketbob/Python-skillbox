file = open('../../test_files/testFile.txt', 'r', encoding='utf-8')

data = file.read().split('\n')
lines_cnt = len(data)
words_cnt = 0
chr_cnt = 0

i = 1
for line in data:
    line = line.split()
    words_cnt += len(line)

    for word in line:
        for char in word:
            if not char.isalpha():
                word = word.replace(char, '')
        chr_cnt += len(word)

print('lines:', lines_cnt)
print('words:', words_cnt)
print('chrs:', chr_cnt)
