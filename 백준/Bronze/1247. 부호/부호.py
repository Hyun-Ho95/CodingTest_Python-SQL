# 1247번 부호
import sys

for _ in range(3):
    answer = 0
    test = int(sys.stdin.readline())
    for i in range(test):
        cnt = int(sys.stdin.readline())
        answer += cnt
    if answer == 0:
        print('0')
    elif answer <0:
        print('-')
    else:
        print('+')