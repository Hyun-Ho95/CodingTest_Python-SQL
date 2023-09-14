# 18398 HOMWRK
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        ai, bi = map(int,input().split())
        print(ai+bi, ai*bi)