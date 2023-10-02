# 25828 Corona Virus Testing (코로나 바이러스 검사)
g, p, t = map(int,input().split())
if g*p < g + p*t:
    print(1)
elif g*p > g + p*t:
    print(2)
elif g*p == g +p*t:
    print(0)