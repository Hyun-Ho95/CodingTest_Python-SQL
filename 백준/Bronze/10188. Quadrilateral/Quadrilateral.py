# 10188 Quadrilateral
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    for k in range(b):
        print('X'*a)
    print('')