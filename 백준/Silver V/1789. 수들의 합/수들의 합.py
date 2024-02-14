# 1789번 수들의 합(SilverV)
s = int(input())
cnt = 0
x = 0

while True:
    if s > x:
        x += 1
        s = s-x
        cnt += 1
    else:
        print(cnt)
        break