def summa(n):
    summ = 0
    if (n > 0):
        for i in range(n+1):
            summ += i
    return summ

def num_count(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10

    return cnt

n = int(input('число:'))
sm = summa(n)
nc = num_count(n)
print('summa=', sm)
print('count=', nc)
print('raznost=', sm - nc)
