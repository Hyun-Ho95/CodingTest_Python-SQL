# 2574번 사탕 선생 고창영 (Bronze III)
import sys
t = int(input())
for _ in range(t):
    cnt = 0
    empty_line = input()
    num = int(sys.stdin.readline())
    for i in range(num):
        i = int(sys.stdin.readline())
        cnt += i
    if cnt % num ==0:
        print('YES')
    else:
        print('NO')
              
        