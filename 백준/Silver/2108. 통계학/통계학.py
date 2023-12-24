# 2108번 통계학(Silver III)
import math
from collections import Counter
import sys
num_list = []

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()
cnt = Counter(num_list).most_common(2)

print(round(sum(num_list)/len(num_list)))
print(num_list[len(num_list)//2])

if len(cnt) >1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
      print(cnt[0][0])
print(max(num_list)-min(num_list))