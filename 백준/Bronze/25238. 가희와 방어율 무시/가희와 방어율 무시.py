# 25238 가희와 방어율 무시
a, b = map(int,input().split())
if a - (a * (b/100)) >=100:
    print(0)
else:
    print(1)