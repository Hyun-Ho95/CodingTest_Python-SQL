# 27262 Лифт엘리베이터
n, k, a, b = map(int,input().split())
elevator = 0
stairs = 0

# 계단 이용시간 
stairs += a*(n-1)

# 엘리베이터 이용시간
if b > 1:
    elevator += b*(k-1) + b*(n-1)
else:
    elevator += b*(n-1)

print(elevator,stairs)