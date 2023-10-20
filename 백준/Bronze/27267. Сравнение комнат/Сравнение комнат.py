# 27267 Сравнение комнат(방 비교)
a, b, c, d = map(int,input().split())
if a*b > c*d:
    print('M')
elif a*b < c*d:
    print('P')
else:
    print('E')