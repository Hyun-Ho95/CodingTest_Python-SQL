# 28097 모범생 포닉스
n = int(input())
plan_list = list(map(int,input().split()))
cnt = 0
for idx,k in enumerate(plan_list):
    if idx == len(plan_list)-1:
        cnt += k
    else:
        cnt += k + 8
print(cnt//24,cnt%24)