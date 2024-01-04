# 1453번 피시방 알바(BronzeII)
seat = [0] * 100
n = int(input())
cnt = 0
customer = list(map(int,input().split()))
for i in customer:
    if seat[i-1] == 0:
        seat[i-1] += 1
    else:
        cnt += 1
print(cnt)