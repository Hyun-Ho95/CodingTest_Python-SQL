# 28490 Area
n = int(input())
result = []
for i in range(n):
    h, w = map(int,input().split())
    result.append(h*w)
print(max(result))