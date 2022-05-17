class CountIterator:
    cnt = 0
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        temp_cnt = self.cnt
        self.cnt += 1
        return temp_cnt


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
