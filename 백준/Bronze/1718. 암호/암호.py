# 1718번 암호(BronzeII)
from collections import deque
line = input()
key = input()
dic = {chr(i+96) : i for i in range(1,27)}
cnt = 0
ans = []

for i in line:
    if i == ' ':
        ans.append(' ')
        if cnt == len(key)-1:
            cnt = 0
        else:
            cnt += 1
        continue

    if dic[i] - dic[key[cnt]] > 0:
        for k,v in dic.items():
            if v == dic[i] - dic[key[cnt]]:
                ans.append(k)
                break
        if cnt == len(key)-1:
            cnt = 0
        else:
            cnt += 1
    else:
        for k,v in dic.items():
            if v == dic[i] - dic[key[cnt]] + 26:
                ans.append(k)
                break
        if cnt == len(key)-1:
            cnt = 0
        else:
            cnt += 1
print(''.join(ans))