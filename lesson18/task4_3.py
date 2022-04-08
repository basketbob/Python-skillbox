input_str = input('str: ')
l = 0
u = 0
for s in input_str:
    if (s.islower()):
        l += 1
    else:
        u += 1
print(input_str.lower() if l > u else input_str.upper())

