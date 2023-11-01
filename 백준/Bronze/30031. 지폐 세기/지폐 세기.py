# 30031 지폐 세기
money = {136 : 1000
        ,142 : 5000
        ,148 : 10000
        ,154 : 50000}
n = int(input())
cnt = 0 
for _ in range(n):
    a,b = map(int,input().split())
    cnt += money[a]
print(cnt)