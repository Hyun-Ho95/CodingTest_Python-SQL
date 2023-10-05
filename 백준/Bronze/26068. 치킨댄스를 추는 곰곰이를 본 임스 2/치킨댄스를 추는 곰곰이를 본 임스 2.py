# 26068 치킨댄스를 추는 곰곰이2
n = int(input())
cnt = 0
for _ in range(n):
    x = int(input().split('-')[-1])
    if x <= 90:
        cnt += 1
print(cnt)