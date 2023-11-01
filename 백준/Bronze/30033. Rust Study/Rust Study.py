# 30033 Rust Study
n = int(input())
plan_pages = list(map(int,input().split()))
study_pages = list(map(int,input().split()))
cnt = 0

for idx,k in enumerate(plan_pages):
    if k <= study_pages[idx]:
        cnt += 1
print(cnt)