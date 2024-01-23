# 2154번 수 이어 쓰기 3
n = int(input())
ans = ''
for i in range(1,n+1):
    ans = ans + str(i)
print(ans.index(str(n))+1)
