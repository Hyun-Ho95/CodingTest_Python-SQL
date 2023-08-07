# 6810 ISBN
start_num = 91
a = int(input())
b = int(input())
c = int(input())

start_num += 1 * a
start_num += 1 * c
start_num += 3 * b

print(f'The 1-3-sum is {start_num}')