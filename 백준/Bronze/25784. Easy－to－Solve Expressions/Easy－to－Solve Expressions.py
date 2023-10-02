# 25784 Easy-to-Solve Expressions (쉽게 풀 수 있는 표현식)
a, b, c = map(int,input().split())
if (a == b+c) or (b == a+c) or (c == a+b):
    print(1)
elif (a == b*c) or (b == a*c) or (c == a*b):
    print(2)
else:
    print(3)