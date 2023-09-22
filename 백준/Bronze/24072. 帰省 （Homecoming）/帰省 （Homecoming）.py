# 24072 Homecoming(귀성)
a,b,c = map(int,input().split())
stay = [i for i in range(a,b+1)]
if c in stay[:-1]:
    print(1)
else:
    print(0)