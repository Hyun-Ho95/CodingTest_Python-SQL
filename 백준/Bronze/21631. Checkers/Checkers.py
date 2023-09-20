# 21631 Checkers
a, b = map(int,input().split())
if a ==0 and b==0:
    print(0)
elif a==0 and b!=0:
    print(1)
elif a>=b:
    print(b)
elif a<b:
    print(a+1)