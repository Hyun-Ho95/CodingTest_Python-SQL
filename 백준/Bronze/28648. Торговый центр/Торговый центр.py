# 28648 Торговый центр
n = int(input())
result = []
for _ in range(n):
    a, b = map(int,input().split())
    result.append(a+b)
print(min(result))