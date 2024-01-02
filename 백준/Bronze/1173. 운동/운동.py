# 1173번 운동 (BronzeII)
# N: 운동 시간 / m: 초기 맥박(최저 맥박)
# M: 최대 맥박 /  T: 맥박 증가량 / R: 맥박 감소량
N,m,M,T,R = map(int,input().split())
min_heart = m
health = 0
cnt = 0

if m + T > M:
    print(-1)
else:
    while True:
        if N == health:
            print(cnt)
            break
        else:
            if m + T <= M:
                health += 1
                cnt += 1
                m += T
            else:
                if m - R < min_heart:
                    m = min_heart
                    cnt += 1
                else:
                    m -= R
                    cnt += 1