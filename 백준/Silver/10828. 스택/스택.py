# 10828 스택 (Silver IV)
import sys
stack = []

for _ in range(int(input())):
    order = sys.stdin.readline().rstrip().split()
    
    if order[0] == 'push':
        stack.append(order[1])
    
    elif order[0] == 'top':
        print(stack[-1] if stack else -1)
        
    elif order[0] == 'pop':
        print(stack.pop() if stack else -1)
    
    elif order[0] == 'size':
        print(len(stack))
    
    elif order[0] == 'empty':
        print(0 if stack else 1)