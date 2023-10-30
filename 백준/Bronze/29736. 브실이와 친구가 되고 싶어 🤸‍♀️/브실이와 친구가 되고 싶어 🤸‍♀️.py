# 29736 브실이와 친구가 되고 싶어
a, b = map(int,input().split())
k, x = map(int,input().split())
friends = [i for i in range(a,b+1)]
beusil = [j for j in range(k-x,k+x+1)]
cnt = 0 
for k in friends:
    if k in beusil:
        cnt += 1
        
if cnt ==0:
    print('IMPOSSIBLE')
else:
    print(cnt)