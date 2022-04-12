def interests_sname_cnt(dict):
    lst = []
    string = ''
    for i, stud in dict.items():
        lst += stud['interests']
        string += stud['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs = [(i, stud['age']) for i, stud in students.items()]
print(pairs)
my_lst, l = interests_sname_cnt(students)
print(my_lst, l)