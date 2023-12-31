# 1009번 분산처리
t = int(input())
answer =[]

for _ in range(t):
    a,b = map(int,input().split())
    b %= 4
    
    if b%4==0:
        b=4
    
    s = a**b
    
    if s%10 ==0:
        answer.append(10)
    else:
        answer.append(s%10)

for i in answer:
    print(i)
