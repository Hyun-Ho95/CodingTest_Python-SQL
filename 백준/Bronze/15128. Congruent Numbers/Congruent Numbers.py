# 15128 ( Congruent Numbers )
p1, q1, p2, q2 = map(int,input().split())
triangle = p1*p2/q1/q2/2
if triangle ==int(triangle):
    print(1)
else: 
    print(0)