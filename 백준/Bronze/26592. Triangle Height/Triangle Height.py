# 26592 Triangle Height
n = int(input())
for _ in range(n):
    a, b = map(float,input().split())
    result = (2*a)/b
    print(f'The height of the triangle is {result:.2f} units')