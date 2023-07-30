# 4696 St. Ives
while True:
    n = float(input())
    if n !=0:
        cnt = 0
        if n != 0:
            for i in range(5):
                cnt += (n**i)
        if str(cnt)[-1]=='0':
            print(f'{cnt:.2f}')
        else:
            print(round(cnt,2))
    else:
        break