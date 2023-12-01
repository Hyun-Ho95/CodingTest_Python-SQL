# 2292번 벌집
n = int(input())
honey_comb = 1
cnt = 1

while n > honey_comb:
    honey_comb += cnt * 6
    cnt += 1
print(cnt)