# 28940 Дневник Гравити Фолз
w, h = map(int,input().split())
n, a, b = map(int,input().split())
if a>w or b>h:
    print(-1)
else:
    if n % ((w//a) * (h//b)) ==0:
        print( n // ((w//a) * (h//b)) )
    else:
        print(n // ((w//a) * (h//b)) + 1)