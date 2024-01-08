# 1592번 영식이와 친구들(BronzeII)
from collections import deque
n,m,l = map(int,input().split())

deq = deque([0 for _ in range(n)])
deq[0] += 1
cnt = 0

while True:
    if max(deq) == m:
        break
    
    
    if deq[0] %2 ==0:
        deq.rotate(-l)
        deq[0] += 1
        cnt += 1
    else:
        deq.rotate(l)
        deq[0] += 1
        cnt += 1
print(cnt)    