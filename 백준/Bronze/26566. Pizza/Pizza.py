# 26566 Pizza
from math import pi 
n = int(input())
for _ in range(n):
    a1, p1 = map(float,input().split())
    r1, p2 = map(float,input().split())
    val1, val2 = a1/p1, (pi*r1**2)/p2
    print(['Slice of pizza','Whole pizza'][val1<val2]) 
    # 리스트형태로 [Condition True일때 실행할 내용,Condition False일 때 실행할 내용][Condition]