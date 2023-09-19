# 20867 Rulltrappa(에스컬레이터)
m, s, g = map(int,input().split())
a, b = map(float,input().split())
l,r = map(int,input().split())
if int(m/g)+int(l/a) > int(m/s)+int(r/b):
    print('latmask')
else:
    print('friskus')