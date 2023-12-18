# 10845 큐 (Silver IV)
import sys
from queue import Queue
que = Queue()

for _ in range(int(input())):
    order = sys.stdin.readline().rstrip().split()
    
    if order[0] == 'push':
        que.put(order[1])
    elif order[0] == 'pop':
        print(que.get() if list(que.queue) else -1)
    elif order[0] == 'size':
        print(len(list(que.queue)))
    elif order[0] == 'empty':
        print(0 if list(que.queue) else 1)
    elif order[0] == 'front':
        print(list(que.queue)[0] if list(que.queue) else -1)
    elif order[0] == 'back':
        print(list(que.queue)[-1] if list(que.queue) else -1)