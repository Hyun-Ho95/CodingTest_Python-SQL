# 25704 출석 이벤트
n = int(input())
p = int(input())

if n >=20:
    if p < 2000:
        print(0)
    else:
        print(min((p-2000),(int(p*0.75))))
elif n >=15:
    if p < 2000:
        print(0)
    else:
        print(min((p-2000),(int(p*0.9))))
elif n >=10:
    if p < 500:
        print(0)
    else:
        print(min((p-500),(int(p*0.9))))
elif n >=5:
    if p < 500:
        print(0)
    else:
        print(p-500)
else:
    print(p)   