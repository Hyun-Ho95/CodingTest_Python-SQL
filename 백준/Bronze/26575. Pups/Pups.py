# 26575 Pups
import math
n = int(input())
for i in range(n):
    d, k, p =  map(float,input().split())
    dkp = d*k*p
    print('$%.2f' % dkp)