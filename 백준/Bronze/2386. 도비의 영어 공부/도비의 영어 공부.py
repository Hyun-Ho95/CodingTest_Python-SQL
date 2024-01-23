# 2386번 도비의 영어공부(BronzeII)
while True:
    alp, *sen = input().split()
    cnt = 0 
    if alp == '#':
        break
    for i in sen:
        cnt += i.count(alp) + i.count(alp.upper())
    print(alp,cnt)