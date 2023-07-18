# 10872번 팩토리얼
n = int(input())
result = 1

for i in range(n,1,-1):
    result = result * i
print(result)