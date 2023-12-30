# 2501번 약수 구하기 (Bronze III)
n,k = map(int,input().split())
result = []
for i in range(1,n+1):
    if n % i==0:
        result.append(i)
result.sort()
print(result[k-1]) if len(result) >= k else print(0)