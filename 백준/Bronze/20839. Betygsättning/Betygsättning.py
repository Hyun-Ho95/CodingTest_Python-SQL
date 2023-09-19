# 20839 평가
# x개의 기준 A, y개의 기준 C, z개의 기준 E
# E등급을 받으려면 기준E 만족
# C등급을 받으려면 기준C,E 만족
# A등급을 받으려면 기준A,C,E 만족
x1, y1, z1 = map(int,input().split())
x2, y2, z2 = map(int,input().split())
if z1 == z2 and y1==y2 and x1==x2:
    print('A')
elif z1 == z2 and y1==y2 and int((x1+1)/2)<=x2:
    print('B')
elif z1 == z2 and y1==y2:
    print('C')
elif z1 == z2 and int((y1+1)/2)<=y2:
    print('D')
else:
    print('E')