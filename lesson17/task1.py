def vowels_in_text(txt):
    vowels = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
    txt_vowels = []

    for chr in txt:
        cnt = vowels.count(chr)
        if (cnt > 0):
            txt_vowels.append(chr)
    return txt_vowels

txt = input('text: ')
txt_vowels = vowels_in_text(txt)
print(txt_vowels)
print(len(txt_vowels))
