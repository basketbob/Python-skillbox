N = [1,2,3,4,5,6,7,8,9,10,11,12]
K = 4
players = []
for n in range(len(N)//K):
    temp = []
    for k in range(n*K, n*K+K):
        temp.append(N[k])
    players.append(temp)

print(players)