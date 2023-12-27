# 4949번 균형잡힌 세상(Silver IV)
import sys
while True:
    sen = sys.stdin.readline().rstrip()
    stack = []
    
    if sen == '.':
        break
    
    for i in sen:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) !=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
        elif i == ')':
            if len(stack) !=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)

    if len(stack)==0:
        print('yes')
    else:
        print('no')