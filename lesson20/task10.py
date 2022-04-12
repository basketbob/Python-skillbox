str = 'abcde'
tpl = (10,20,30,40)

gener = ((str[i], tpl[i]) for i in range(len(str)))

print(gener)
for g in gener:
    print(g)
