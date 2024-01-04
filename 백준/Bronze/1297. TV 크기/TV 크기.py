# 1297번 TV 크기(Bronze II)
import math
d,h,w = map(int,input().split())
y = (w*d)/math.sqrt((h**2)+(w**2))
x = (h*d)/math.sqrt((h**2)+(w**2))
# x = math.floor((h*y)/w)
print(int(x),int(y))