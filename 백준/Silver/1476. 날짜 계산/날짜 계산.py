# 1476번 날짜 계산(SilverV)
e,s,m = map(int,input().split())
earth = 1
sun = 1
moon = 1
year = 1
while True:
    if earth == e and sun == s and moon == m:
        print(year)
        break
    earth += 1
    sun += 1
    moon += 1
    year += 1
    if earth > 15:
        earth = 1
    
    if sun > 28:
        sun = 1
    
    if moon > 19:
        moon = 1
    