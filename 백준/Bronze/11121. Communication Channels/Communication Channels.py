# 11121 Communication Cahnnels
t = int(input())

for i in range(t):
    a, b = input().split()
    cnt = 0
    for j in range(len(a)):
        if a[j]==b[j]:
            cnt += 1
    if cnt == len(a):
        print('OK')
    else:
        print('ERROR')