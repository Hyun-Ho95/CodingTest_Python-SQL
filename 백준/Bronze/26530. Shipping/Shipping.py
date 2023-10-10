# 26530 Shipping
n = int(input())

for _ in range(n):
    x = int(input())
    cnt = 0
    for _ in range(x):
        product, quantity, price = input().split()
        cnt +=int(quantity)*float(price)
    print(f'${cnt:.2f}')