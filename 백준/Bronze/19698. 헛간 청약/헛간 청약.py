# 19698 헛간 청약
n, w, h, l = map(int,input().split())
if n <= (w//l)*(h//l):
    print(n)
else:
    print((w//l)*(h//l))