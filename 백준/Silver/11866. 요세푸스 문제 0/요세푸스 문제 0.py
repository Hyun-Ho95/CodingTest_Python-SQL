# 요세푸스 문제 0 (Silver V)
from collections import deque
k,n = map(int,input().split())
cnt = k
deq = deque()
answer = []

for i in range(1,k+1):
    deq.append(i)
while len(deq)>0:
    deq.rotate(-(n-1))
    answer.append(deq.popleft())
print('<' + ', '.join(map(str,answer)) + '>')