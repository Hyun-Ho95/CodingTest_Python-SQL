# 10866 덱 (Silver IV)
import sys
from collections import deque
answer = deque()

for _ in range(int(input())):
    order = sys.stdin.readline().rstrip().split() #명령을 딕셔너리에 넣지않고 공백을 기준으로 구분
    
    if order[0] == 'push_front':
        answer.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        answer.append(int(order[1]))
    elif order[0] == 'pop_front':
        if answer:
            print(answer.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if answer:
            print(answer.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(answer))
    elif order[0] == 'empty':
        print(0 if answer else 1)
    elif order[0] == 'front':
        print(answer[0] if answer else -1)
    elif order[0] == 'back':
        print(answer[-1] if answer else -1)