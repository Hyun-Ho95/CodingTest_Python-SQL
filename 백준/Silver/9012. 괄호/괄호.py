# 9012 괄호 (Silver IV)
import sys
from collections import deque

for _ in range(int(input())):
    deq = deque()
    vps = sys.stdin.readline().rstrip()
    for i in vps:
        if i == '(':
            deq.append(i)
        elif i ==')':
            if deq:
                deq.pop()
            else:
                print('NO') #처음부터 괄호가 들어온다면 이미 모양이 맞지않으므로 'NO' 출력
                break
    else:
        print('NO') if deq else print('YES')