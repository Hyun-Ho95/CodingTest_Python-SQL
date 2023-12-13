# 4153 직각삼각형
while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    else:
        num = [a,b,c]
        num = sorted(num)
        if (num[0]**2) + (num[1]**2) == (num[2]**2):
            print('right')
        else:
            print('wrong')