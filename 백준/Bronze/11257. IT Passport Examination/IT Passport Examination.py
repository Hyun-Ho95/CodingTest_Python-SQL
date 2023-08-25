# 11257 IT Passport Examination
n = int(input())
for i in range(n):
    a, b, c, d = map(int,input().split())
    x = b+c+d
    if x >= 55 and b>10 and c>7 and d>=12:
        print(f'{a} {x} PASS')
    else:
        print(f'{a} {x} FAIL')