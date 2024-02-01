# 1417번 국회의원 선거(SilverV)
n = int(input())
candidates = []
dasom = 0 
cnt = 0

for i in range(n):
    x = int(input())

    # 후보자가 다솜 한명일 경우는 0 출력 후 종료
    if n==1:
        print(0)
        break
    else:
        if i == 0:
            dasom = x
        else:
            candidates.append(x)
else:
    while True:
        if dasom > max(candidates):
            break
        dasom += 1
        candidates[candidates.index(max(candidates))] = max(candidates)-1
        cnt += 1
    print(cnt)
