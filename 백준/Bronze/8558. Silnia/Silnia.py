# 8558 Silnia
n = int(input())
cnt = 1
if n==0 or n==1:
    cnt *= 1  
for i in range(n,1,-1):
    cnt *= i
print(str(cnt)[-1])