# 25893 Majestic 10 (마제스틱 10)
n = int(input())
for _ in range(n):
    a, b, c = map(int,input().split())
    if (a<10) and (b<10) and (c<10):
        print(a,b,c)
        print('zilch')
        print('')
    elif (a>=10 and b>=10 and c>=10):
        print(a,b,c)
        print('triple-double')
        print('')
    elif (a>=10 and b>=10) or (b>=10 and c>=10) or (a>=10 and c>=10):
        print(a,b,c)
        print('double-double')
        print('')
    elif (a>=10) or (b>=10) or (c>=10):
        print(a,b,c)
        print('double')
        print('')