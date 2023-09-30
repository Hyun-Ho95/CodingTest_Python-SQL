# 25591 푸앙이와 종윤이
m,n = map(int,input().split())
a = 100-m
b = 100-n
c = 100-(a+b)
d = a*b
if d > 99:
    q = d//100
    r = d%100
    print(a,b,c,d,q,r)
    print(c+q, r)
else:
    q = d//100
    r = d%100
    print(a,b,c,d,q,r)
    print(c, d)