# 2010번 플러그
import sys
input = sys.stdin.readline

cnt = 0 
n = int(input())

for _ in range(n):
    cnt += int(input())
    
print(cnt - (n-1)*1)