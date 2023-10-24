# 27890 특별한 작은 분수
x, N = map(int,input().split())
for i in range(N):
    if x % 2 ==0:
        x = int(x/2)^6
    else:
        x = (2*x)^6   
print(x)