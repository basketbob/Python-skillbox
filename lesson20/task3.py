def slice_tuple(tpl, elm):
    cnt = tpl.count(elm)
    result = ()
    if (cnt == 1):
        result = tpl[tpl.index(elm):]
    elif (cnt > 1):
        last_ind = len(tpl) - tpl[::-1].index(elm)
        result = tpl[tpl.index(elm):last_ind]

    return result

tpl = ('a', 'b', 'c', 'd', 'b', 'e', 'b', 'f')
print(slice_tuple(tpl, 'b'))