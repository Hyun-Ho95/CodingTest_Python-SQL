# 1871번 좋은 자동차 번호판(BronzeII)
alphabet = {chr(65+i) : i for i in range(26)}

for _ in range(int(input())):
    cnt1,cnt2 = 0,0
    alp, num = input().split('-')

    for idx,k in enumerate(alp):
        cnt1 += alphabet[k] * (26**(len(alp)-idx-1))
    
    cnt2 = int(num)

    if abs(cnt1-cnt2) <=100:
        print('nice')
    else:
        print('not nice')