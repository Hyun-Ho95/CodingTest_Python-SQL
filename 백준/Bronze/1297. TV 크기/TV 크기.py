# 1297번 TV 크기(Bronze II)
import math
d,h,w = map(int,input().split())
# TV 너비(가로) : x / TV 높이(세로) : y
x = (w*d)/math.sqrt((h**2)+(w**2))
y = (h*d)/math.sqrt((h**2)+(w**2))
# y = (h*x)/w
print(int(y),int(x))