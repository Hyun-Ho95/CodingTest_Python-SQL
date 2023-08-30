# 13623 Zero or one (0또는1)
a,b,c = map(int,input().split())
if a==b==c:
    print('*')
elif a==b!=c:
    print('C')
elif a!=b==c:
    print('A')
elif a==c!=b:
    print('B')