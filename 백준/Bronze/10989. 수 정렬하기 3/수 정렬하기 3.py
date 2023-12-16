# 10989 수 정렬하기 3
import sys
cnt_array = [0 for _ in range(10001)]

for _ in range(int(input())):
    cnt_array[int(sys.stdin.readline())] += 1

for idx,k in enumerate(cnt_array):
    if k !=0:
        for _ in range(k):
            print(idx)