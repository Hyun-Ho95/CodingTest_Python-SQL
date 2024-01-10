# 1681번 줄 세우기(BronzeII)
n,l = map(int,input().split())
cnt = 0
ans = 0
num = 0 
while True:
    if num == n:
        break
    cnt += 1
    if str(l) not in str(cnt):
        num += 1
        if ans < cnt:
            ans = cnt
        
print(ans)