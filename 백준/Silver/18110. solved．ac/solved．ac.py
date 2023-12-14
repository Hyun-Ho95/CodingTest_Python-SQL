# 18110 solved.ac (Silver IV)
import sys
from collections import deque
n = int(input())

def rround(n): return int(n)+1 if n-int(n)>=0.5 else int(n) # 사사오입 공식
p = rround(n*0.15) # 절사 값
level_list = []

if n == 0:
    print(0)
else:
    for i in range(n):
        level_list.append(int(sys.stdin.readline().rstrip()))
    level_list = deque(sorted(level_list))
    
    if p != 0:
        for _ in range(p):
            level_list.popleft()
            level_list.pop()
    print(rround(sum(level_list)/len(level_list)))
        