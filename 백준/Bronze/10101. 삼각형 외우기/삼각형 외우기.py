# 10101 삼각형 외우기
a = int(input())
b = int(input())
c = int(input())
if a==b==c==60:
    print('Equilateral')
elif (a+b+c == 180) and (a==b or b==c or a==c):
    print('Isosceles')
elif (a+b+c == 180) and (a!=b or b!=c or a!=c):
    print('Scalene')
elif a+b+c != 180:
    print('Error')