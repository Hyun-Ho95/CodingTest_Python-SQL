# 1547번 공
n = int(input())
loc = 1
for _ in range(n):
    x, y = map(int,input().split())
    if loc == x:
        loc = y
    elif loc == y:
        loc = x
print(loc)