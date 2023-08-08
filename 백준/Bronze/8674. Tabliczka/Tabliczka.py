# 8674 Tabliczka
a, b = map(int,input().split()) # a : 열 , b : 행
if (a%2==0 and b%2==0) or (a%2==0) or (b%2==0):
    print(0)
else:
    if a > b:
        print(abs((a//2)*b-(a-(a//2))*b))
    else:
        print(abs((b//2)*a-(b-(b//2))*a))