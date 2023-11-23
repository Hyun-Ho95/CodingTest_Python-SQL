# 1676 번 팩토리얼 0의 개수
n = int(input())
num = 1
cnt = 0

for i in range(n,0,-1):
    num *= i
ans = str(num)[::-1]

for j in ans:
    if j == '0':
        cnt +=1
    else:
        break
print(cnt)