# 10773 제로 (Silver IV)
import sys
from collections import deque
deq = deque()

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num !=0:
        deq.append(num)
    else:
        deq.pop()
print(sum(deq))