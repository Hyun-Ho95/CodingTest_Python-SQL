# 21633 Bank Transfer(계좌 이체)
k = int(input())
if k*(1/100)+25 >=2000:
    print(f'{2000:.2f}')
elif k*(1/100)+25 <= 100:
    print(f'{100:.2f}')
else:
    print(f'{k*(1/100)+25:.2f}')