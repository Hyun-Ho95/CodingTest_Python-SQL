# 27294 멫개고 ?
t, s = map(int,input().split())
if (t<12 or t > 16) or s==1:
    print(280)
elif (12 <= t <= 16 ) or s==0:
    print(320)