# 1284번 집 주소
while True:
    n = input()
    cnt = 0
    if n =='0':
        break
    else:
        for i in n:
            if i=='1':
                cnt += 2
            elif i =='0':
                cnt += 4
            else:
                cnt += 3
        cnt += len(n)+1
    print(cnt)