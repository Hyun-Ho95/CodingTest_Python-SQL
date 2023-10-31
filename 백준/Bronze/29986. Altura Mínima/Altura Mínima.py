# 29986 Altura Mínima
n, h = map(int,input().split())
rides = list(map(int,input().split()))
cnt = 0
for i in rides:
    if h >= i:
        cnt += 1
print(cnt)