# 1964번 오각형, 오각형, 오각형...(BronzeII)
n = int(input())
cnt = 0

for i in range(1,(n+2)):
    cnt += i
cnt *= 2
cnt -= 1
for j in range(n):
    cnt += j
print(cnt%45678)