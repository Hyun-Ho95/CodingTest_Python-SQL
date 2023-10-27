# 28519 Планеты двух измерений(초콜릿 번갈아 먹기)
n, m = map(int,input().split())
if n == m or abs(n-m)==1:
    print(n+m)
elif abs(n-m) ==2:
    print(n+m-1)
elif abs(n-m) >=3:
    print(2*min(n,m)+1)