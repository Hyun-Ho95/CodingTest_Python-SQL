# 27855 Cornhole
h1, b1 = map(int,input().split())
h2, b2 = map(int,input().split())

if 3*h1+b1 > 3*h2+b2:
    print(1, (3*h1+b1)-(3*h2+b2))
elif 3*h1+b1 < 3*h2+b2:
    print(2, (3*h2+b2)-(3*h1+b1))
else:
    print('NO SCORE')