# 1668번 트로피 진열(Bronze II)
from collections import deque

arr = []
cnt_l = 0
cnt_r = 0

for _ in range(int(input())):
    arr.append(int(input()))
    
left = deque(arr[:arr.index(max(arr))+1])
right = deque((arr[arr.index(max(arr)):]))

# 왼쪽 시점
max_left = 0
while True:
    if left == deque([]):
        break
    
    if left[0] > max_left:
        cnt_l += 1
        max_left = left[0]
        left.popleft()
    else:
        left.popleft()
    
# 오른쪽 시점    
max_right = 0
while True:
    if right == deque([]):
        break

    if right[-1] > max_right :
        cnt_r += 1
        max_right = right[-1]
        right.pop()
    else:
        right.pop()     
print(cnt_l)
print(cnt_r)
