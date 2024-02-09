# 1531번 투명(SilverV)
import sys

n,m = map(int,input().split())
drawing = [[0] * 101 for i in range(101)]
for _ in range(n):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            drawing[i][j] += 1
cnt = 0 
for x_axis in drawing:
    for j in x_axis:
        if j > m:
            cnt += 1
print(cnt)