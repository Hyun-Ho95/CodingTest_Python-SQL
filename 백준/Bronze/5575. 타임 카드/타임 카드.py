# 5575 타임 카드
for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int,input().split())
    # 전부 다 초로 환산하여 계산
    t1 = h1*60*60 + m1*60 + s1
    t2 = h2*60*60 + m2*60 + s2
    t = t2 - t1

    # t는 현재 초이므로 시간(h)을 구하려면 3600으로 나눈 몫 구하기
    # 그리고 시간이므로 24시간이 넘으면 24로 나눈 나머지 시간구하기 (문제에선 이렇게 나올 일 없음)
    h = t//60//60 % 24 

    # 마찬가지로 분(m)을 구하려면 60으로 나눈 몫 구하기
    # 그리고 분이므로 60분이 넘으면 60으로 나눈 나머지 시간 구하기
    m = t//60 % 60

    # 초(s)는 t를 60으로 나눈 나머지 구하기
    s = t % 60

    print(h,m,s)