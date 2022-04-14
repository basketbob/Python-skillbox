def multi2list(mlty_list):
    new_list = []
    for l in mlty_list:
        if not isinstance(l, list):
            new_list.append(l)
        else:
            new_list += multi2list(l)
    return new_list

nice_list = [1, 2, 3, 4, [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(multi2list(nice_list))
