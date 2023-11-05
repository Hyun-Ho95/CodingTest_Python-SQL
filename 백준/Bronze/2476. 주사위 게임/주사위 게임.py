# 2476번 주사위 게임
answer = []
n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if a==b==c:
        answer.append(10000 + a*1000)
    elif (a==b or a==c):
        answer.append(1000 + a*100)
    elif b==c:
        answer.append(1000 + b*100)
    else:
        answer.append(max(a,b,c)*100)
print(max(answer))