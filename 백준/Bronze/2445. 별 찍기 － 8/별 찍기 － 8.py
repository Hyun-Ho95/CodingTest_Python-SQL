# 2445번 별 찍기 - 8
n = int(input())
for i in range(1,2*n):
    if i > n:
        i = 2*n-i
        print('*'*i + ' '*(2*(n-i)) + '*'*i)
    else:
        print('*'*i + ' '*(2*(n-i)) + '*'*i)