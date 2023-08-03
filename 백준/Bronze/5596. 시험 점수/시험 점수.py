# 5596 시험 점수
minkuk = list(map(int,input().split()))
manse = list(map(int,input().split()))

if sum(minkuk) == sum(manse):
    print(sum(minkuk))
else:
    print(max(sum(minkuk),sum(manse)))