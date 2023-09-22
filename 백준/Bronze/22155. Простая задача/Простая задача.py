## 22155 간단한 문제
n = int(input())
for _ in range(n):
    i,f = map(int,input().split())
    if (i<=1 and f<=2) or (f<=1 and i<=2):
        print('Yes')
    else:
        print('No')