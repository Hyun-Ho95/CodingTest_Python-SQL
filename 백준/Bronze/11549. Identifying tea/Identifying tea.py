# 11549 Identifying tea
t = int(input())
contestant = list(map(int,input().split()))
cnt = 0

for i in contestant:
    if t == i:
        cnt += 1
print(cnt)