# 1773번 폭죽쇼(BronzeII)
import sys
n,c = map(int,input().split())
arr = [0]*(c+1)

for _ in range(n):
    t = int(sys.stdin.readline())
    for j in range(t,c+1,t):
        arr[j] = 1
print(sum(arr))