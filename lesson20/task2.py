def is_prime(n):
    return isinstance(n, int)


def self_obj(obj):
    return [i for i, v in iter(obj) if is_prime(i)]

objct = {1:'test1','b':'test2',2:'test3','r':'test4',3:'test5'}
str = 'sfgsdgdsfg'
lst = [1,2,3,4,5,6,7]
tpl = (1,2,3,4,5)
for v in iter(tpl):
    print(v)
#print(self_obj(objct))
