# 2231번 분해합
n = int(input())
for i in range(1,n+1):
    if i + sum([int(j) for j in str(i)]) == n:
        print(i)
        break
else: 
    print(0)