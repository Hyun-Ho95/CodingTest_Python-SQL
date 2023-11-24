# 1874번 스택 수열 
import sys
n = int(input())
stack = []
answer = []

flag = 0
cnt = 1
# sys.stdin.readline().strip()
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    while cnt <= num: 
        stack.append(cnt)
        answer.append('+')
        cnt += 1
        
    if stack[-1]==num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)