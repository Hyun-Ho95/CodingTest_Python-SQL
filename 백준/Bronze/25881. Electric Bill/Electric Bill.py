# 25881 Electric Bill(전기요금)
a, b = map(int,input().split())
n = int(input())
for _ in range(n):
    i = int(input())
    if i <= 1000:
        print(i, i*a)
    else:
        print(i, 1000*a + (i-1000)*b)