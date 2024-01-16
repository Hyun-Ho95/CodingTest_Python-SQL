# 1919번 에너그램 만들기(BronzeII)
from collections import deque
word1 = deque(input())
word2 = deque(input())
w1_copy = deque(word1)
w2_copy = deque(word2)

cnt = 0

for i in word1:
    if i not in w2_copy:
        cnt += 1
    else:
        w2_copy.remove(i)

for j in word2:
    if j not in w1_copy:
        cnt += 1
    else:
        w1_copy.remove(j)
print(cnt) 