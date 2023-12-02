# 2751번 수 정렬하기 2
import sys

n = int(input())
answer = []
for _ in range(n):
    answer.append(int(sys.stdin.readline().strip()))
answer.sort()

print('\n'.join(map(str,answer)))