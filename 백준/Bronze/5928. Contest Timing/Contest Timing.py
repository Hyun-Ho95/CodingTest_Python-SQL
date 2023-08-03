# 5928 Contest Timing
d, h, m = map(int,input().split())
if ((d-11)*24*60) + ((h-11)*60) + (m-11) < 0:
    print(-1)
else:
    print(((d-11)*24*60) + ((h-11)*60) + (m-11))