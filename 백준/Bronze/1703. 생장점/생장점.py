# 1703번 생장점
while True:
    trees = list(map(int,input().split()))
    if trees == [0] :
        break
    else:
        leafs = trees[1:]
        cnt = 0
        for idx,k in enumerate(leafs):
            if idx ==0:
                cnt += k
            else:
                if idx%2==0:
                    cnt *= k
                else:
                    cnt -= k
        print(cnt)
                