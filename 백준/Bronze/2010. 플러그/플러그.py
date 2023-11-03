# 2010번 플러그
import sys

cnt = 0 
n = int(input())

for _ in range(n):
    cnt += int(sys.stdin.readline())
print(cnt - (n-1)*1)