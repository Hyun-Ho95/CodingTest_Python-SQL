# 25377 빵
n = int(input())
cnt = 0
sol = []
for _ in range(n):
    a,b = map(int,input().split())
    if a > b:
        cnt +=1
    else:
        sol.append(b)
if cnt ==n:
    print(-1)
else:
    print(min(sol))