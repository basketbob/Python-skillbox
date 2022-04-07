import random

cmd1 = [round(random.uniform(5.00, 9.99), 2) for _ in range(20)]
cmd2 = [round(random.uniform(5.00, 9.99), 2) for _ in range(20)]
winners = [cmd1[i] if cmd1[i] > cmd2[i] else cmd2[i] for i in range(20)]
print('комманда 1: ', cmd1)
print('комманда 2: ', cmd2)
print('winners: ', winners)
