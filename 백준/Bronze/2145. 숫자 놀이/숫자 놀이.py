# 2145번 숫자놀이(BronzeII)
while True:
    n = int(input())
    if n==0:
        break
    else:
        cnt = n
        while True:
            ans = 0
            if len(str(cnt))==1:
                print(cnt)
                break
            else:
                for i in str(cnt):
                    ans += int(i)
                cnt = ans