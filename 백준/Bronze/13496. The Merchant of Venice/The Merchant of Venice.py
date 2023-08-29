# 13496 The Merchant of Venice
k = int(input())

for i in range(k):
    # n = 배의 수, s = 배의속도 (1일/마일), d = 빚변제까지 남은 날짜
    n, s, d = map(int,input().split())
    cnt = 0
    for _ in range(n):
        # di = 배에서 베니스까지의 거리 , vi = 배에 있는 두카트의 값
        di,vi = map(int,input().split())
        if di / s <= d:
            cnt += vi
    print(f'Data Set {i+1}: \n{cnt}')
    print('')