# 1312번 소수(SilverV)
a,b,n = map(int,input().split())
cnt = 0
for _ in range(n):
    a = (a%b)*10
    cnt = a//b
print(cnt)