# 17256 달달함이 흘러넘쳐
ax, ay, az = map(int,input().split())
cx, cy, cz = map(int,input().split())

bx = cx-az
by = cy/ay
bz = cz-ax
print(bx,int(by),bz)