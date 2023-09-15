# 19944 뉴비의 기준은 뭘까?
n, m = map(int,input().split())
if m <= n and m!=1 and m!=2:
    print('OLDBIE!')
elif m > n and m!=1 and m!=2:
    print('TLE!')
elif m==1 or m==2:
    print('NEWBIE!')
    