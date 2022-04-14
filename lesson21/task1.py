def my_sum(*args, total_sum=0):
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, list):
            for j_elem in i_elem:
                total_sum = my_sum(j_elem, total_sum=total_sum)
    return total_sum

print(my_sum(1,2,3,4,5,6))
print(my_sum([1,[2,3],4,5,6]))