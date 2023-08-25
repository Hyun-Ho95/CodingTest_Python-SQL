# 10480 Oddities
n = int(input())
for i in range(n):
    a = int(input())
    if abs(a)%2==0:
        print(f'{a} is even')
    else:
        print(f'{a} is odd')