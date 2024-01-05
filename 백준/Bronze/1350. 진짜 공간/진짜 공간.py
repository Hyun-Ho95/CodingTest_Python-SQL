# 1350번 진짜 공간(Bronze II)
from collections import deque
n = int(input())
size = deque((map(int,input().split())))
cluster = int(input())
cnt = 0

for _ in range(n):
    current_size = size.popleft()
    
    if current_size ==0:
        cnt += 0 
    else:   
        if current_size > cluster:
            if current_size % cluster ==0:
                cnt += (current_size // cluster)
            else:
                cnt += (current_size // cluster) + 1
        else:
            cnt += 1
print(cnt*cluster)