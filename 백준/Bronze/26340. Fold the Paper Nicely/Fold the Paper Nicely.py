# 26340 Fold the Paper Nicely
import math
n = int(input())

for _ in range(n):
    a, b, c = map(int,input().split())
    a2 = a
    b2 = b
    for _ in range(c):
        if max(a2,b2) == a2:
            a2 = math.floor(max(a2,b2)/2)
        else:
            b2 = math.floor(max(a2,b2)/2)
    print(f'Data set: {a} {b} {c}')
    print(max(a2,b2),min(a2,b2))
    print('')