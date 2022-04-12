def sort_tuple(tpl):
    list_tpl = list(tpl)
    sorted_tpl = []
    for t in tpl:
        if (type(t) != int):
            return tpl

    for _ in range(len(tpl)):
        min_val = min(list_tpl)
        sorted_tpl.append(min_val)
        list_tpl.pop(list_tpl.index(min_val))

    return tuple(sorted_tpl)

a = (1,3,2,8,4)
print(sort_tuple(a))
